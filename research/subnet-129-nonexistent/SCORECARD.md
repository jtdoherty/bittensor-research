# Subnet 129 — DOES NOT EXIST (misread `btcli` totals row) — Mining EV Research

_Analysis date: 2026-06-23 • Network: finney • btcli 9.20.0 • TAO ≈ $216.44 (CoinGecko)_

> **Finding: there is no subnet 129.** On finney the highest registered netuid is **128
> (ByteLeap)**. The "unnamed, huge-price" row the request points at is the **totals/summary
> row** at the bottom of `btcli subnet list` — its "Netuid" cell shows **129 = the count of
> subnets**, and its "Price" cell shows **τ 1.3276 = the SUM of all subnets' alpha prices**,
> not a single subnet trading at 1.3276 τ. No EV can be estimated for a subnet that does not exist.

## Proof (chain-verified, not inferred)

Direct storage query against `wss://entrypoint-finney.opentensor.ai` (same node btcli uses):

```
SubtensorModule.TotalNetworks      = 129     # => 129 subnets exist: netuids 0..128
SubtensorModule.NetworksAdded[128] = True     # subnet 128 exists
SubtensorModule.NetworksAdded[129] = False    # subnet 129 has NOT been added
SubtensorModule.SubnetIdentitiesV3[129] = None
```

And every btcli subcommand except the list confirms it:
```
$ btcli subnet show     --netuid 129 --network finney  ->  ❌ Subnet 129 does not exist
$ btcli subnet metagraph --netuid 129 --network finney  ->  ❌ Subnet 129 does not exist
```

`TotalNetworks = 129` means **129 subnets numbered 0–128**, so "129" is the population count, off-by-one from the max netuid. (Context: the old 128-subnet cap is being lifted to 256 in Q1 2026, so a real netuid 129 will exist later — just not yet.)

## Why the `subnet list` row looks like a subnet (the trap)

Bottom of `btcli subnet list`, below a horizontal separator:

```
 Netuid │ Name │ Price (Τ_in/α_in) │ Market Cap │ Emission (Τ) │ Net Inflow EMA (Τ) │ P (Τ_in, α_in)
 ───────┼──────┼───────────────────┼────────────┼──────────────┼────────────────────┼───────────────
  129   │      │ τ 1.3276          │            │ τ 0.1557     │ τ -0.2843          │ τ 1.98m/8.47m (23.38%)
```

This is a **TOTAL row**, and three tells prove it:
1. **Price format differs.** Real rows render price as `0.0747 τ/ش` (value + per-alpha symbol). The totals row renders `τ 1.3276` (a plain TAO sum). It is `Σ` of all 129 subnet alpha prices, not a quote.
2. **No real subnet is anywhere near it.** The single most expensive alpha on the whole network is **Chutes at 0.0747 τ** (root is 1.0 by definition). A subnet at 1.3276 τ would be ~18× the top market subnet — it doesn't exist. 1.3276 is simply the column sum.
3. **Pool cell is network-wide.** `τ 1.98m / 8.47m α` is the **aggregate** of all subnet pools (millions of TAO), not one subnet's reserve; real subnet pools here are in the thousands (e.g. ByteLeap τ4.71k).

So: unnamed = totals rows have no name; "huge price" = a sum of 129 prices. Mystery solved.

## SCORECARD (machine-rankable)
```
SCORECARD
netuid: 129
name: DOES_NOT_EXIST            # highest real netuid is 128 (ByteLeap); "129" = subnet COUNT in btcli totals row
work_type: other               # N/A — no subnet, no work
alpha_price_tao: 0.0           # the "1.3276" is Σ of all subnet prices, not a quote
net_inflow_ema_tao: 0.0        # the "-0.2843" is the network-wide total, not this (nonexistent) subnet
token_health: 0                # no token exists
miner_pool_usd_per_day: 0      # nothing to mine
effective_num_earners: 0
saturation: 0                  # N/A
min_rig_cost_usd_per_day: 0
registration_cost_tao: 0       # cannot register on a non-added netuid (extrinsic would fail)
mechanism_trap: none           # N/A
newcomer_friendliness: 0       # cannot enter
edge_required: N/A — subnet 129 has not been created on finney; do not deploy anything
ev_usd_per_month_low: 0
ev_usd_per_month_base: 0
ev_usd_per_month_high: 0
confidence: 5                  # chain-verified: TotalNetworks=129, NetworksAdded[129]=False
recommendation: NO-GO
composite_score: 0             # token_health 0 + saturation 0 + newcomer_friendliness 0 + (NO-GO=1) + confidence 5 = 6, but the subject is null -> treat as 0/N/A
one_line_thesis: Subnet 129 does not exist on finney (max netuid is 128, ByteLeap); the "unnamed, huge-price" entry is btcli's TOTALS row where "129" is the subnet count and "τ1.3276" is the SUM of all alpha prices — there is nothing to mine.
```

## Key evidence (with sources)
- **Chain query** (`async_substrate_interface` -> finney): `TotalNetworks=129`, `NetworksAdded[129]=False`, `NetworksAdded[128]=True`, `SubnetIdentitiesV3[129]=None`.
- **btcli 9.20.0**: `subnet show/metagraph --netuid 129` both return `❌ Subnet 129 does not exist`; only `subnet list` shows a "129" line and only as the bottom totals row.
- **Newest real subnet** = **128 ByteLeap** (alpha 0.0039 τ, MktCap τ14.35k, net inflow −0.0002). See `raw_evidence.txt`.
- **Top single-subnet alpha price** on the whole network = Chutes 0.0747 τ — an order of magnitude below the 1.3276 "price," confirming 1.3276 is an aggregate.
- **Web context**: old 128-subnet cap; expansion to 256 slots planned Q1 2026 — a genuine netuid 129 will open later, but is not registered as of 2026-06-23.

## What to do instead
- If you wanted the **newest subnet to scout**, that's **128 (ByteLeap)** — run the standard `SUBNET_EV_RESEARCH_PROMPT` against it.
- If you wanted a **high-alpha-price** subnet, the real leaders are **64 Chutes (0.0747 τ)**, **4 Targon (0.0524 τ)**, **51 lium.io (0.0542 τ)** — but high alpha price alone is not EV; check net inflow and saturation per the prompt.
- Re-check after Q1-2026 slot expansion: once `NetworksAdded[129]=True`, re-run this analysis for real.

## Sources
- Direct finney storage queries (TotalNetworks, NetworksAdded, SubnetIdentitiesV3).
- `btcli 9.20.0`: `subnet list`, `subnet show`, `subnet metagraph` (finney). Raw: `raw_evidence.txt`.
- CoinGecko TAO/USD = $216.44 (2026-06-23).
- learnbittensor / taostats docs: 128-subnet cap, 256-slot expansion Q1 2026.
