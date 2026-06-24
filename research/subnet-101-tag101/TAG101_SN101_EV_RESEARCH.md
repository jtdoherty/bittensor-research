# Bittensor Subnet 101 — Tag101: New-Miner EV Research

**Date:** 2026-06-23  ·  **Network:** finney  ·  **Analyst role:** mining-economics
**Subnet:** netuid 101 (Tag101) — decentralized social-post tagging / labeling
**Owner coldkey:** `5H8dNvi1jZRe1dcYN2FdknWKxfGx6u1o9pYm5zRMCZyy2Ex3` (UID 0, *Owner controlled*)
**Repo:** UNKNOWN (no public GitHub located — see Phase 2)  ·  **Tempo:** 360 blocks

> **Bottom line up front: WATCH (leaning NO-GO for real money).** Tag101 pays a
> **nearly *flat*, near-uniform reward to every registered miner** — there is no
> winner-take-all and a fresh hotkey earns its slice within a tempo (high cold-start
> friendliness). But that same flatness means **there is no skill edge**: it is a pure
> inflation-subsidy harvest already **Sybil-farmed by just 16 operators running up to 34
> hotkeys each**. The alpha token is **cheap (0.0058 τ, bottom tier)** with only marginally
> positive inflow (+0.0004). A single newcomer hotkey is ~break-even-to-mildly-positive and
> entirely a bet on alpha price; making real money requires registering *many* hotkeys
> (capital, not skill), which dilutes the pool and is reflexively self-defeating.

---

## PHASE 1 — Token economics (chain-verified)

Source: `btcli subnet list --network finney` (row 101); `btcli subnet show --netuid 101`.

| Metric | Value | Source |
|---|---|---|
| TAO/USD | ~$233 (range $215–268 across exchanges, 24h) | CoinGecko / CMC / Coinbase / Kraken, 2026-06-23 |
| Alpha price (Τ_in/α_in) | **0.0058 τ/ე** | subnet list |
| Market cap (α × price) | τ 16.43k | subnet list |
| Emission (Τ) share | τ 0.0015 | subnet list |
| **Net Inflow EMA (Τ)** | **+0.0004** (marginally POSITIVE) | subnet list |
| Pool reserves P (Τ_in, α_in) | τ 4.39k, 751.28k ე | subnet list |
| Stake (α_out) | 2.06m ე | subnet list |
| Supply / max | 2.81m ე / 21M (~13% emitted) | subnet list |
| Tempo | 360 blocks (~72 min → ~20/day) | subnet show |
| Registration cost (recycled) | **τ 0.3997** (~$93, one-time, per hotkey) | subnet show |

**Token-health verdict: 2/5.** Alpha 0.0058 τ is **bottom-tier** (calibration: SN24 Quasar
0.0099, Minos 0.0383 — Tag101 is *below* even the melting SN24 reference on price). Net inflow
is **technically positive but tiny (+0.0004)** — the token is roughly treading water, not
clearly accreting. Recent multi-week price trend: **UNKNOWN** (taostats subnet-101 chart not
machine-readable; obtain at taostats.io/subnets/101). Low price + razor-thin inflow + no
demonstrated demand narrative = weak token.

### Miner pool $/day
On-chain miner emissions (sum of `Emissions` over all incentive>0 UIDs) ≈ **~111 ე/tempo ×
~20 tempo/day ≈ ~2,220 ე/day** to the miner side (slightly below the ~2,950 default; the
balance flows to validators/owner as dividends). M_alpha source: **derived from metagraph
emissions column**, not the blanket default.

- **Miner pool $/day** = 2,220 × 0.0058 × $233 ≈ **~$3,000/day**, shared across **242
  registered miner hotkeys** → **~$12/day gross per hotkey** at the flat rate.

---

## PHASE 2 — What is the work?

**Work type: data / social-post tagging (CPU, no GPU).** Multiple ecosystem directories
(bittensor.ai/subnets, subnet listings) describe **Tag101 as "decentralized social-post
tagging"** — i.e. miners label/categorize/tag social media posts and validators score the
labels. **No GPU is implied**; this is a CPU + (likely) API/bandwidth task.

**Repo / scoring code: NOT located.** GitHub search for "Tag101 bittensor subnet" returns **0
repositories**; tao.app/subnets/101 returns HTTP 403; taostats/taomarketcap subnet pages did
not expose a repo link to the fetcher. **This is itself a yellow flag** — a subnet with no
discoverable miner docs/scoring code is hard to compete in *on merit* and easy to farm on
*flat weights*. (Mechanism below is therefore **inferred from the on-chain distribution**, not
read from code — reflected in the low confidence score.)

**Required hardware:** light. Social-post tagging needs **CPU + network + possibly an LLM/API
call per request**; a small CPU box (Vast/RunPod ≈ **$2–4/day** for one box hosting *many*
hotkeys) suffices. Per-hotkey compute is near-zero.

**EDGE TEST — FAIL (commodity).** The on-chain reward is **flat** (Phase 4): the top miner
earns only ~2× the floor and ~0.57% of the pool. A flat reward means the validator is **not
meaningfully differentiating miner quality** — so there is **no skill edge to capture**. The
only "edge" that scales reward here is **capital: registering more hotkeys**. That is the
definition of a commodity-subsidy farm, not a defensible niche.

---

## PHASE 3 — Incentive mechanism teardown (the traps)

Scoring/validator **code not found**; the following is **inferred from the live metagraph**
distribution (`raw_metagraph.txt`) — flagged as inference.

- **Distribution shape — FLAT / near-uniform across all miners.** 242 miner UIDs each carry
  incentive **0.0028–0.0057** (top10 all = 0.00568; floor ≈ 0.0028). Top miner share **0.57%**;
  **effective number of earners = 220.6**. There is **no winner-take-all and no steep
  ranking** — essentially everyone alive gets paid roughly the same.
- **The real lever is multi-registration (Sybil), not quality.** Because per-hotkey reward is
  ~flat, an operator's total take scales with **how many hotkeys they run**. The leaderboard is
  therefore a **capital contest**: top operators run 18–34 hotkeys each (Phase 4).
- **Cold-start: very friendly.** A fresh hotkey appears to earn the flat slice within a tempo
  or two — no whitelist, no orchestrator *choosing* who works, no obvious stake-gate beyond the
  reg cost. Miners do carry ~62 ე (~$80) of stake each, possibly a soft self-stake to mine.
- **Failure penalties: unclear** (code not found); the flatness suggests weak/soft penalties —
  consistent with low effort being enough to collect the subsidy.
- **Weight-setting / capture:** the **owner UID 0 takes 44.7% of *dividends*** (validator side)
  and named validators (tao.bot, Yuma/DCG, Kraken, 1T1B.AI, TAO.com, Rizzo) hold the rest —
  **all with incentive = 0** (they are stakers/validators, not miners). Miner emissions are
  spread flat.

**Mechanism trap: `rich_get_richer` (via multi-registration / Sybil capital), plus a flat-weight
subsidy farm.** Not winner-take-all, not a synchronized cohort, not orchestrator-assignment-
gated. The trap is subtler: **flat rewards + no edge = your share decays as anyone (including
you) adds hotkeys, and the people with the most capital already own the pool.**

---

## PHASE 4 — Saturation / competition

Source: `btcli subnet metagraph --netuid 101` (saved as `raw_metagraph.txt`).

- **Miner UIDs with incentive > 0: 242.** Sum of incentive = 0.9954. **effective earners (by
  UID) = 220.6** — *looks* wide open.
- **But by OPERATOR (coldkey) it is concentrated: only 16 distinct coldkeys** run those 242
  hotkeys. **Effective number of operators = 12.2.** Top operators:

  | Coldkey | Hotkeys | Share of miner pool |
  |---|---|---|
  | 5Gjgb4 | 22 | 11.9% |
  | 5G6BfE | 21 | 11.4% |
  | 5Ef7tk | 20 | 10.8% |
  | 5EHULU | 19 | 10.3% |
  | 5GKz92 | 34 | 9.0% |
  | 5DPD3U | 23 | 7.1% |
  | 5G8qfe | 22 | 6.9% |
  | … (10 more) | … | … |

  → The miner side is a **~12-operator oligopoly**, each scaling by brute-force hotkey count.
  The "220 earners" headline is an illusion created by Sybil farming.
- **Validators/stakers** (UID 0 owner, tao.bot, Yuma/DCG, Kraken, 1T1B.AI, TAO.com, Rizzo,
  PX9DGg) hold large stake + dividends but **incentive = 0** — not miner competitors.
- **No public miner heartbeat S3 bucket / capability dashboard** found (no repo located), so
  incumbent rigs can't be fingerprinted — but the task is light CPU regardless; the moat is
  **registration capital**, not hardware.
- **Registration cost:** **τ 0.3997 (~$93) per hotkey**, one-time, non-refundable. Matching a
  top operator (≈20 hotkeys) ≈ **$1,860 of reg capital** before any compute/ops.

**Saturation: 3/5.** Mechanically a newcomer *can* slot in and collect the flat reward
immediately (open entry, no gating), but the pool is already farmed by ~12 capitalized
operators, and adding hotkeys dilutes everyone — so headroom for *meaningful* income is
moderate-to-poor, even though headroom to earn *something small* is wide.

---

## PHASE 5 — EV synthesis

**Assumptions:** TAO = $233; alpha = 0.0058 τ; flat per-hotkey emission ≈ **9.2 ე/day**
(2,220 ე ÷ 242); per-hotkey gross ≈ 9.2 × 0.0058 × 233 ≈ **$12.4/day**. Realized-price factor
= liquidation haircut × trend ≈ **0.85** (pool 751k ე is deep vs a tiny daily sell → slippage
negligible; +0.0004 inflow is barely supportive; trend unconfirmed → modest discount). Per
hotkey: reg τ0.40 amortized over 60d ≈ **$1.55/day**; compute/ops shared across many hotkeys
≈ **$0.3/day** per hotkey. **Net per healthy hotkey ≈ 12.4 × 0.85 − 1.85 ≈ ~$8.7/day** —
*if* the flat reward holds and alpha doesn't slide.

Newcomer outcomes scale with **how many hotkeys you fund** (the only lever), so EV is presented
by operation size, then summarized LOW/BASE/HIGH:

| Scenario | Operation | Net $/day | **Net EV/month** |
|---|---|---|---|
| **LOW** | 1 hotkey; alpha drifts down / dilution bites; marginal entrant → near break-even | ~$0–2 | **~$30** |
| **BASE** | 3–5 hotkeys, flat reward holds, alpha flat | ~$25–40 | **~$900** |
| **HIGH** | 15–20 hotkeys (Sybil-farm like incumbents), alpha stable, ~$1.4–1.9k reg capital sunk | ~$110–140 | **~$3,500** |

> Honest caveats: (1) **There is no skill edge** — BASE/HIGH are *capital* plays, not merit
> plays, and free entry pushes the marginal hotkey's EV toward 0. (2) The whole thing is a
> **bet on a cheap, thin alpha token** (0.0058 τ); a modest price slide flips even BASE
> negative. (3) HIGH is **reflexive and fragile**: it requires out-capitalizing entrenched
> farmers, and the owner can re-weight or the validator can start differentiating at any time,
> instantly repricing a flat-farm strategy to zero.

- **Single biggest risk:** **alpha price depreciation on a flat, no-edge subsidy** — you are
  paid in a bottom-tier token whose only support is a razor-thin +0.0004 inflow; if it melts,
  EV goes negative regardless of how many hotkeys you run.
- **Single thing that would most change the answer:** finding the **scoring code** — if quality
  *is* in fact differentiated (and the flat distribution is just current-state collusion/low
  effort), a genuinely better tagger could break the flatness; if it is truly flat-by-design,
  it stays a pure capital farm. (Confidence is low precisely because the repo wasn't found.)
- **Minimum edge to be +EV:** **cheap registration capital + automation to run many hotkeys
  reliably** — i.e. a Sybil-farm operator's edge, not a tagging-quality edge. With one hotkey
  and no capital advantage: **not worth it**.

**Recommendation: WATCH** (small, cheap, low-effort experiment only; **NO-GO for anyone
expecting skill-based or sizeable income**).

---

## SCORECARD
```
SCORECARD
netuid: 101
name: Tag101
work_type: data              # decentralized social-post tagging / labeling (CPU, no GPU)
alpha_price_tao: 0.0058
net_inflow_ema_tao: +0.0004
token_health: 2              # bottom-tier price, razor-thin positive inflow, trend unknown
miner_pool_usd_per_day: 3000 # ~2,220 alpha/day to miners (metagraph-derived) × 0.0058 × $233
effective_num_earners: 220.6 # by UID (flat reward); but only 12.2 effective OPERATORS by coldkey
saturation: 3                # open entry + flat reward, but pool farmed by ~12 capitalized operators
min_rig_cost_usd_per_day: 3  # light CPU box hosting many hotkeys; ~$0.3/hotkey
registration_cost_tao: 0.3997  # ~$93 per hotkey, one-time
mechanism_trap: rich_get_richer  # flat-weight subsidy farmed via multi-registration (Sybil capital); not winner-take-all
newcomer_friendliness: 4     # fresh hotkey earns flat slice within a tempo; no whitelist/orchestrator gating
edge_required: none / commodity — only lever is registration capital (run many hotkeys); no tagging-quality edge rewarded
ev_usd_per_month_low: 30
ev_usd_per_month_base: 900
ev_usd_per_month_high: 3500
confidence: 2                # scoring code/repo not found; mechanism inferred from on-chain flat distribution
recommendation: WATCH
composite_score: 14          # token_health 2 + saturation 3 + newcomer_friendliness 4 + WATCH 3 + confidence 2
one_line_thesis: Tag101 pays a flat, no-edge inflation subsidy that a fresh hotkey can collect immediately, but it is a cheap-token capital farm already Sybil-run by ~12 operators — easy to earn a little, hard to earn much, and entirely a bet on a thin alpha price.
```

### Key evidence (with sources)
- **alpha 0.0058 τ, net inflow +0.0004, mcap τ16.43k, supply 2.81m/21M, tempo 360** —
  `btcli subnet list --network finney` (row 101), 2026-06-23.
- **Registration (recycled) τ 0.3997 per hotkey; owner coldkey 5H8dNv…2Ex3** —
  `btcli subnet show --netuid 101`.
- **Flat miner reward: 242 incentive>0 UIDs, each 0.0028–0.0057, top share 0.57%, effective
  earners 220.6** — `btcli subnet metagraph --netuid 101` (see `raw_metagraph.txt`).
- **Sybil concentration: only 16 coldkeys run the 242 hotkeys; top operators 19–34 hotkeys
  each; effective operators 12.2** — coldkey aggregation of the same metagraph.
- **Validators/stakers (owner UID0 44.7% dividends, tao.bot, Yuma/DCG, Kraken, 1T1B.AI,
  TAO.com, Rizzo) all have incentive = 0** — metagraph (not miner competitors).
- **Work = decentralized social-post tagging; light CPU, no GPU** — bittensor.ai/subnets and
  ecosystem subnet directories, 2026-06-23 (no GitHub repo locatable → mechanism inferred).
- **TAO ≈ $233 (215–268)** — CoinGecko / CoinMarketCap / Coinbase / Kraken, 2026-06-23.
- **Price trend: UNKNOWN** — taostats subnet-101 chart not machine-readable; obtain at
  taostats.io/subnets/101.
```
```

**Sources:**
- https://bittensor.ai/subnets
- https://www.coingecko.com/en/coins/bittensor
- https://coinmarketcap.com/currencies/bittensor/
- https://taostats.io/subnets/101
