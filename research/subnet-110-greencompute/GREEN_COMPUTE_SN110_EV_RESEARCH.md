# Subnet 110 (Green Compute) — Mining EV Teardown

_Analysis date: 2026-06-23. Chain: finney. Analyst pass per SUBNET_EV_RESEARCH_PROMPT.MD._

**Green Compute** (owner identity "Green Compute", coldkey `5D53sX…Bb75sL`) is a
decentralized **GPU-inference marketplace gated on verified renewable energy**.
The pitch: *"only verifiably clean compute gets paid."* Miners run **RTX 4090 /
5090** nodes, serve OpenAI-compatible inference, and must **prove their power is
green via an on-chain oracle** (carbon-registry + hardware-location attestation)
*before a single token is paid*. Verified green nodes get a **1.5× multiplier**.
Onboarding is **application-gated** (`green-compute.com/apply`). Enterprise demand
is billed in fiat, converted to TAO, and used to **buy back SN110 alpha**.

> **Headline finding:** despite 256 registered UIDs, **exactly one miner (UID 155)
> earns** — incentive = **1.000000**, capturing ~100% of the miner emission pool
> (~2,950 α/day ≈ $6.5k/day). For a generic newcomer with commodity GPUs this is a
> **NO-GO**: the work is application-gated AND green-energy-oracle-gated AND
> currently 100% captured. It is at best a **conditional WATCH** for someone who
> physically owns renewable-powered 4090/5090 hardware and gets approved early.

---

## PHASE 1 — Token economics (chain-verified)

Source: `btcli subnet list --network finney`, row netuid 110; `btcli subnet show --netuid 110`.

| Metric | Value | Source |
|---|---|---|
| TAO/USD | ~$225 (CMC $225.16; CoinGecko $218; Coinbase $235; cluster $218–265) | WebSearch CMC/CoinGecko |
| Alpha price (Τ_in/α_in) | **0.0098 τ/Ѐ** (low tier) | subnet list |
| Market cap (α × price) | τ 28.13k (~$6.3M) | subnet list |
| Emission (Τ) | 0.0009 τ/block (subnet's emission share) | subnet list |
| **Net Inflow EMA (Τ)** | **τ 0.0000 (FLAT — neither inflowing nor melting)** | subnet list |
| Pool P(Τ_in, α_in) | τ 5.86k, 593.94k Ѐ (thin) | subnet list |
| Stake (α_out) | 2.27m Ѐ | subnet list |
| Supply | 2.86m Ѐ / 21M | subnet list |
| Tempo (n) | 360 blocks (~20 tempos/day) | subnet show |
| Mechanisms | 1 | subnet list |
| Registration cost (recycled) | **τ 0.0005 (~$0.11)** — trivially cheap | `btcli subnet show --netuid 110` |
| Owner coldkey | 5D53sX6AwAzXUB24G85Ch35hYr5rCpXjYFWpFTe4uzBb75sL (Green Compute) | subnet show |

**Miner pool $/day.** Using protocol default M_alpha ≈ 2,950 α/day to miners
(~1 α/block × 41% × 7,200 blocks/day):

```
miner_pool_usd_per_day = 2,950 Ѐ × 0.0098 τ × $225 ≈ $6.5k/day
```

The single earning miner (UID 155) shows **148.01 Ѐ emission/tempo × ~20 tempos/day
≈ 2,960 Ѐ/day**, which matches the full ~2,950 α/day miner pool — confirming **one
hotkey takes essentially the entire miner subsidy**.

**Token-health verdict: 2/5.** Low alpha price (0.0098 τ, bottom-mid tier) and a
recent ~5% downtrend (taostats), partly offset by a **flat (0.0000) net-inflow
EMA** — it is *not* actively melting like many small subnets, and the
fiat→TAO→alpha **buyback mechanism** provides a structural bid. But thin pool
(τ 5.86k / 593.94k α) means liquidating any meaningful daily haul moves the price.

---

## PHASE 2 — What is the work?

- **Work type: GPU inference** (OpenAI-compatible serving). Source: green-compute.com.
- **Required hardware:** NVIDIA **RTX 4090 (24 GB)** or **RTX 5090 (32 GB Blackwell)**.
  Yield-calculator example on the site quotes **5.7 τ/month for 2× RTX 4090** (incl.
  the 1.5× green multiplier).
- **The hard gate (not hardware — energy):** miners must run on **verified
  renewable power** — biogas (prioritized first wave; UK on-farm anaerobic
  digesters), solar, hydro, wind, geothermal. Power source is attested via carbon
  registries + hardware-location proofs and verified by an **on-chain oracle**.
- **Min viable rig (commodity rental cross-check):** 2× RTX 4090 on Vast/RunPod ≈
  $0.30–0.40/GPU-hr → **~$17/day**. **BUT renting cloud GPUs does not satisfy the
  green-energy oracle** — you cannot prove a Vast instance runs on renewables.
  Effective min rig is **owned 4090/5090 hardware co-located with a renewable
  source**, i.e. real capex + a power asset, not a rental.

**EDGE TEST:** Reward is *not* for commodity GPU. The structural edge the subnet
pays for is **access to cheap verified-green electricity** (and the 1.5× multiplier
on it). If you own a biogas/solar/hydro site with GPUs, you have a genuine,
non-commodity edge. If you don't, you are ineligible by design.

---

## PHASE 3 — Incentive mechanism teardown (the traps)

No public GitHub/scoring repo was located (searches surface the unrelated SN27
Compute / commune-ai repos, not SN110). Mechanism reconstructed from the official
site + on-chain incentive distribution. **Flagged as a confidence limiter.**

- **Distribution shape (observed on-chain):** effectively **winner-take-all** —
  UID 155 has incentive 1.000000; every other UID is 0.000000.
- **Assignment gating: YES — the dominant red flag.** Two stacked gates:
  1. **Green-energy oracle verification** — no payment until your power is
     attested green.
  2. **Application whitelist** — `green-compute.com/apply`; the owner decides who
     becomes a miner.
- **Rich-get-richer / demand routing:** enterprise inference demand is routed and
  billed off-chain (fiat), then recycled into alpha buybacks. Whoever is the
  verified serving node captures the flow — strongly incumbent-favoring.
- **Failure penalties:** unverified or non-green nodes simply earn 0 (the current
  reality for 255 of 256 UIDs).
- **Weight-setting:** owner UID 0 holds the dominant stake/dividend
  (0.53 dividends) and the validator set is small/owner-centric — **owner-captured
  weight-setting**, another concentration risk.
- **Newcomer cold-start:** **locked.** A fresh hotkey that registers (τ0.0005) sits
  at incentive 0 indefinitely unless it (a) passes green verification and (b) is
  admitted via the application. Registration ≠ earning here in the strongest sense.

---

## PHASE 4 — Saturation / competition

Source: `btcli subnet metagraph --netuid 110 --network finney` (raw saved to
`raw_metagraph.txt`).

- **UIDs registered:** 256.
- **UIDs with incentive > 0:** **1** (UID 155, hotkey `5FmpAT…`, coldkey
  `5HVkV9…`, identity "~").
- **Top earner share:** 100%.
- **Effective number of earners (1/Σ shareᵢ²):** **1.0.**
- The rest of the table is stake/dividend holders (tao.bot, Yuma/DCG, Kraken,
  Datura, TAO.com, Rizzo, etc. — these are **validators/stakers earning dividends**,
  not miners earning incentive) plus a long tail of 0/0 placeholder UIDs, many under
  a single coldkey `5FH2GA…` (bulk-registered shells).
- **No public miner heartbeat bucket / capability dashboard** was found in repo
  search (no repo found), so incumbent rig sizing relies on the site's own claim:
  first-wave miners = UK farms running 4090s/5090s on on-farm biogas.
- **Registration cost (recycle):** τ0.0005 (~$0.11) one-time — cheap, but cheap
  registration is irrelevant when earning is gated.

**Interpretation:** Numerically "few earners" (which the scorecard scale would call
*open*), but functionally **closed** — the single earner sits behind an
application + green-oracle wall, not behind open competition you can out-compete by
spinning up more GPUs. Low numeric competition ≠ low barrier here.

---

## PHASE 5 — EV synthesis

**Assumptions:** newcomer brings 2× RTX 4090. Two regimes:

- **Commodity-GPU newcomer (the default reader):** ineligible — cannot pass the
  green oracle (rented cloud GPUs aren't green-attestable), likely never admitted.
  Realistic share ≈ **0**. EV ≈ **$0** minus the τ0.0005 registration.

- **Genuine green-power owner, admitted:** competes for / shares the ~$6.5k/day
  pool. Even here, one incumbent currently takes 100%; displacing or sharing is
  uncertain and owner-discretionary.

**Liquidation haircut:** pool τ5.86k / 593.94k α is thin; daily disposal of a
multi-thousand-dollar alpha haul would visibly move price. Apply ~0.55–0.65
haircut. Price trend ~−5%; net inflow flat with a buyback bid (mild support).

| Scenario | Daily share | Gross α→USD | After haircut − costs | EV/day | EV/month |
|---|---|---|---|---|---|
| **LOW** (commodity GPU, never verified/admitted) | 0% | $0 | −$0.11 reg | **~$0** | **$0** |
| **BASE** (applies, slow/partial verification, token-bid-only exposure) | ~1–3% | $65–195 | ×0.6 − $17 rig | **~$10–100/day** | **~$200/mo** |
| **HIGH** (owns verified green site, admitted early, co-dominant 30–40% share) | 30–40% | $2.0–2.6k | ×0.6 − $20 ops | **~$600/day** | **~$18k/mo** |

- **ev_usd_per_month_low: 0**
- **ev_usd_per_month_base: 200**
- **ev_usd_per_month_high: 18,000**

**Single biggest risk:** **assignment + green-oracle gating with 100% incumbent
capture.** You can register for $0.11 and earn nothing forever; the owner and the
verification process — not open competition — decide who is paid.

**Single thing that would most change the answer:** evidence the subnet is
**opening additional verified-green miner slots** (multiple UIDs with incentive > 0)
*and* a published, auditable scoring/oracle repo. That would convert this from a
closed showcase into a contestable market.

**Recommendation: NO-GO** for a generic newcomer. **WATCH** only if you (a)
physically control renewable-powered 4090/5090 capacity and (b) can get through the
`/apply` whitelist + oracle early. **Minimum edge required to be +EV:** owned
verified-green electricity (biogas/solar/hydro) — without it you are ineligible by
construction; commodity GPU margin here is structurally **0**.

---

## SCORECARD
```
SCORECARD
netuid: 110
name: Green Compute
work_type: inference
alpha_price_tao: 0.0098
net_inflow_ema_tao: 0.0000
token_health: 2
miner_pool_usd_per_day: 6505
effective_num_earners: 1.0
saturation: 2
min_rig_cost_usd_per_day: 17
registration_cost_tao: 0.0005
mechanism_trap: assignment_gated
newcomer_friendliness: 1
edge_required: owned verified-green electricity (biogas/solar/hydro/wind) + admission via /apply whitelist & on-chain green oracle; commodity rented GPU is ineligible -> EV 0
ev_usd_per_month_low: 0
ev_usd_per_month_base: 200
ev_usd_per_month_high: 18000
confidence: 3
recommendation: NO-GO
composite_score: 9
one_line_thesis: 256 UIDs, one earner taking 100% behind a green-energy oracle and an application whitelist — closed by design; only +EV if you physically own renewable-powered GPU capacity and get admitted early.
```
`composite = token_health 2 + saturation 2 + newcomer_friendliness 1 + recommendation(NO-GO=1) + confidence 3 = 9`

---

## Key evidence (with sources)
- **token_health 2** — alpha 0.0098 τ (low tier), market cap τ28.13k, **net inflow
  EMA 0.0000 (flat, not melting)**, ~−5% recent price trend; fiat→TAO→alpha buyback
  provides a structural bid. _Source: `btcli subnet list --network finney` row 110;
  taostats.io/subnets/110; green-compute.com._
- **saturation 2 / effective_num_earners 1.0** — 256 registered UIDs, **only UID 155
  has incentive (1.000000)**; its ~148 Ѐ/tempo ≈ 2,960 Ѐ/day ≈ the full miner pool.
  Numerically few earners but functionally closed. _Source: `btcli subnet metagraph
  --netuid 110` → `raw_metagraph.txt`; `btcli subnet show --netuid 110`._
- **newcomer_friendliness 1 / mechanism_trap assignment_gated** — must pass on-chain
  green-energy oracle (carbon-registry + hardware-location proofs) AND apply for
  admission (`green-compute.com/apply`) before any payment; owner UID 0 holds
  dominant stake/dividends. _Source: green-compute.com (Phase 2/3)._
- **min_rig_cost 17 / edge** — 2× RTX 4090 ≈ $17/day rented, but rentals can't be
  green-attested; the paid edge is owned renewable power + 1.5× green multiplier.
  _Source: green-compute.com; Vast/RunPod 4090 pricing._
- **registration_cost 0.0005 τ (~$0.11)** — cheap, but irrelevant given gated
  earning. _Source: `btcli subnet show --netuid 110` "Registration cost (recycled)"._
- **TAO/USD ~$225** — _Source: CoinMarketCap $225.16, CoinGecko $218._

### Sources
- [CoinMarketCap — Bittensor (TAO)](https://coinmarketcap.com/currencies/bittensor/)
- [CoinGecko — Bittensor (TAO)](https://www.coingecko.com/en/coins/bittensor)
- [Green Compute — official site](https://www.green-compute.com/)
- [taostats.io — Subnet 110](https://taostats.io/subnets/110/chart)
- Chain: `btcli subnet list / show / metagraph --netuid 110 --network finney` (BTCLI 9.20.0), 2026-06-23
