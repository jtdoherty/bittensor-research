#!/usr/bin/env python3
"""
subnet_yield.py — Bittensor validator / staking EV analyzer.

Given on-chain JSON dumps (metagraph + hyperparameters + `subnet list`), compute
per-subnet validator economics:
  - alpha price, market cap, net TAO inflow (tao_flow_ema = token health)
  - whether the subnet is actually emitting alpha
  - active validator count, owner self-capture %, permit cutoff
  - floor-to-earn (smallest current validator stake)
  - expected yield on TAO staked (gross emission APY + after-take net APY)

KEY INSIGHT — why the yield is price-independent:
  You stake 1 TAO -> buy (1/price) alpha -> earn a pro-rata share of the
  validator alpha-emission pool. The TAO-denominated emission yield is therefore
      daily_yield = validator_alpha_emission_per_day / total_validator_alpha_stake
  and the alpha price cancels at entry. Price only matters via (a) melt/drift of
  the alpha principal you now hold, and (b) entry slippage. So a high emission APY
  on a MELTING token (negative tao_flow_ema) can still be a net loss. Always read
  APY next to tao_flow_ema.

DATA REFRESH (run in a Linux/WSL shell with btcli >= 9.23 installed via pipx):
    OUT=./data; mkdir -p "$OUT"
    btcli subnet list --json-output > "$OUT/list.json"
    for n in 116 69 40 16 26 58 108 82 78 36 47 122; do
      btcli subnet metagraph --netuid $n --network finney --json-output --no-prompt > "$OUT/sn$n.json"
      btcli subnet hyperparameters --netuid $n --json-output > "$OUT/hp$n.json"
    done
  Notes:
    * btcli native build fails on Windows (needs MSVC+OpenSSL); use WSL Ubuntu.
    * --json-output conflicts with the default --prompt on `metagraph`; add --no-prompt.
    * `list`/`hyperparameters` do NOT accept --no-prompt.
    * JSON identity strings contain raw control chars -> parse with strict=False.

USAGE:
    python subnet_yield.py --data ./data --netuids 116 69 40 16 26 58 [--tao-usd 204]
    python subnet_yield.py --data ./data --screen          # rank all subnets in list.json by net inflow
"""
import argparse, json, os, sys

BLOCK_S = 12.0          # ~12s/block on finney
DEFAULT_TAKE = 0.18     # typical validator delegation take (commission)
DEFAULT_TAO_USD = 204.0


def fz(x):
    try:
        return float(x)
    except (TypeError, ValueError):
        return 0.0


def load(path):
    if not os.path.exists(path):
        return None
    with open(path, encoding="utf-8", errors="replace") as f:
        return json.loads(f.read(), strict=False)   # strict=False: identities have control chars


def analyze(netuid, data_dir, list_subs, tao_usd, take):
    mg = load(os.path.join(data_dir, f"sn{netuid}.json"))
    hp = load(os.path.join(data_dir, f"hp{netuid}.json")) or []
    if not mg or "uids" not in mg:
        return None
    row = (list_subs or {}).get(str(netuid)) or (list_subs or {}).get(netuid) or {}

    name = str(mg.get("name", "?")).replace("\n", " ").strip().lstrip(":").strip() or f"sn{netuid}"
    price = fz(mg.get("rate"))                       # alpha price in TAO
    px_usd = price * tao_usd
    max_v = int(next((x["value"] for x in hp if x["hyperparameter"] == "max_validators"), 64))
    tempo = int(next((x["value"] for x in hp if x["hyperparameter"] == "tempo"), 360))
    tempos_day = 86400.0 / (tempo * BLOCK_S)

    owner = mg.get("owner")
    uids = mg["uids"]
    # Active validators = those currently receiving dividends.
    vals = [u for u in uids if fz(u.get("dividends")) > 0]
    v_stakes = sorted((fz(u.get("stake")) for u in vals), reverse=True)
    total_v = sum(v_stakes)
    floor = min(v_stakes) if v_stakes else 0.0
    owner_cap = (100 * sum(fz(u.get("stake")) for u in vals if u.get("coldkey") == owner) / total_v
                 if total_v else 0.0)

    # Permit cutoff: top-`max_v` neurons by stake hold a vPermit. If fewer than
    # max_v neurons have any stake, the permit is effectively open (cutoff ~0).
    all_stakes = sorted((fz(u.get("stake")) for u in uids), reverse=True)
    n_staked = sum(1 for s in all_stakes if s > 0)
    cutoff = all_stakes[max_v - 1] if n_staked >= max_v else 0.0

    # Validator emission pool per day (alpha) and the price-independent yield.
    val_emit_day = sum(fz(u.get("emissions")) for u in vals) * tempos_day
    emitting = val_emit_day > 0
    gross_apy = (val_emit_day / total_v * 365 * 100) if total_v else 0.0
    net_apy = gross_apy * (1 - take)
    flow = fz(row.get("tao_flow_ema"))

    return dict(netuid=netuid, name=name, price=price, px_usd=px_usd, flow=flow,
                emitting=emitting, max_v=max_v, n_val=len(vals), cutoff=cutoff,
                floor=floor, floor_usd=floor * px_usd, owner_cap=owner_cap,
                total_v=total_v, val_emit_day=val_emit_day,
                gross_apy=gross_apy, net_apy=net_apy)


def print_table(rows):
    h = (f"{'SN':>4} {'name':<13} {'pxUSD':>6} {'taoflow':>9} {'emit':>5} {'nVal':>4} "
         f"{'floor_a':>9} {'floor$':>8} {'own%':>5} {'grossAPY':>8} {'netAPY':>7}")
    print(h)
    print("-" * len(h))
    for r in rows:
        if not r:
            continue
        print(f"{r['netuid']:>4} {r['name'][:13]:<13} {r['px_usd']:>6.2f} {r['flow']:>+9.5f} "
              f"{('Y' if r['emitting'] else 'no'):>5} {r['n_val']:>4} {r['floor']:>9.0f} "
              f"{r['floor_usd']:>8.0f} {r['owner_cap']:>5.0f} {r['gross_apy']:>8.1f} {r['net_apy']:>7.1f}")
    print("\nAPY = gross alpha-emission yield at CONSTANT price (price cancels at entry).")
    print("Real return = APY - alpha price drift. netAPY is after ~18% delegation take.")
    print("Read APY next to taoflow: high APY on negative-flow (melting) token can be a net loss.")


def screen(list_subs, tao_usd, max_mcap=None):
    rows = []
    for k, r in list_subs.items():
        rows.append(dict(n=int(r.get("netuid", k)), name=str(r.get("subnet_name", "?"))[:16],
                         price=fz(r.get("price")), mcap=fz(r.get("market_cap")),
                         flow=fz(r.get("tao_flow_ema")),
                         tao_in=fz(r.get("liquidity", {}).get("tao_in"))))
    healthy = sorted([x for x in rows if x["flow"] > 0], key=lambda x: -x["flow"])
    print(f"=== {len(healthy)} of {len(rows)} subnets have POSITIVE net TAO inflow ===")
    print(f"{'SN':>4} {'name':<16} {'taoflow':>10} {'mcapTAO':>9} {'pxTAO':>8} {'liqTAO':>8}")
    for x in healthy:
        if max_mcap and x["mcap"] >= max_mcap:
            continue
        print(f"{x['n']:>4} {x['name']:<16} {x['flow']:>+10.5f} {x['mcap']:>9.0f} "
              f"{x['price']:>8.4f} {x['tao_in']:>8.0f}")


def main():
    ap = argparse.ArgumentParser(description="Bittensor validator/staking EV analyzer")
    ap.add_argument("--data", default="./data", help="dir with sn<N>.json/hp<N>.json/list.json")
    ap.add_argument("--netuids", type=int, nargs="*", default=[116, 69, 40, 16, 26, 58])
    ap.add_argument("--tao-usd", type=float, default=DEFAULT_TAO_USD)
    ap.add_argument("--take", type=float, default=DEFAULT_TAKE)
    ap.add_argument("--screen", action="store_true", help="rank all subnets in list.json by net inflow")
    ap.add_argument("--max-mcap", type=float, default=None, help="screen: only show mcap < this (TAO)")
    args = ap.parse_args()

    list_d = load(os.path.join(args.data, "list.json"))
    list_subs = (list_d or {}).get("subnets", {})

    if args.screen:
        if not list_subs:
            sys.exit("No list.json found in --data dir. Refresh per the module docstring.")
        screen(list_subs, args.tao_usd, args.max_mcap)
        return

    rows = [analyze(n, args.data, list_subs, args.tao_usd, args.take) for n in args.netuids]
    print_table(rows)


if __name__ == "__main__":
    main()
