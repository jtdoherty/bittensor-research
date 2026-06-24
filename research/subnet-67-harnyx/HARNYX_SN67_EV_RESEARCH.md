# Bittensor Subnet 67 — Harnyx: New-Miner EV Research

**Date:** 2026-06-23  ·  **Network:** finney  ·  **Analyst role:** mining-economics
**Subnet:** netuid 67 (Harnyx) — decentralized **deep-research agents** (agentic LLM research under a tool budget)
**Owner identity:** `Harnyx (*Owner)` — UID 0, hotkey `5Cm4fA…`, coldkey `5HEAv3…`
**Repo:** https://github.com/harnyx/harnyx  ·  **Listing:** https://subnetalpha.ai/subnet/harnyx/

> **Bottom line up front: WATCH** (conditional GO for a strong agent-builder; NO-GO for commodity).
> The work is *code/agent quality*, not GPU-hours — near-zero capex and a real, durable edge is
> available to someone who can build a better deep-research agent. BUT the mechanism is a
> **champion / "dethroning" contest** in which the **owner UID 0 self-captures 63.7% of all miner
> emissions** as the entrenched champion, and the remaining ~36% is a **flat, crowded participant
> pool split ~141 ways into dust** (~$14–28/day each). Token is low-priced (0.0100 τ) with only
> marginally positive net inflow. Easy to earn pocket change fast; hard to earn real money without
> dethroning the owner — which is reflexive and the owner controls the rules.

---

## PHASE 1 — Token economics (chain-verified)

Source: `btcli subnet list --network finney` (row 67), `btcli subnet show --netuid 67`.

| Metric | Value | Source |
|---|---|---|
| TAO/USD | ~$235 (range $225–265 across exchanges) | CoinGecko / CMC / Coinbase / MEXC, 2026-06-23 |
| Alpha price (Τ_in/α_in) | **0.0100 τ/α** | subnet list |
| Market cap (α × price) | τ 8.61k | subnet list |
| Emission (Τ) share | τ 0.0053 | subnet list |
| **Net Inflow EMA (Τ)** | **+0.0002** (marginally POSITIVE) | subnet list |
| Pool reserves P (Τ_in, α_in) | τ 2.60k, 259.14k α | subnet list |
| Stake (α_out) | 598.01k α | subnet list |
| Supply / max | 857.15k α / 21M (~4% emitted → very young) | subnet list |
| Tempo | 360 blocks | hyperparameters / show |
| Registration cost (recycled) | **τ 0.0703** (~$16.5, one-time, non-refundable) | `subnet show --netuid 67` |

**Token-health verdict: 2/5.** Alpha price **0.0100 τ is low** — same tier as the SN24 Quasar
calibration baseline (0.0099) and ~4× *below* SN107 Minos (0.0383). Net inflow is **+0.0002**, i.e.
**barely positive / essentially flat** — better than SN24's −0.0040 melt, but the token is *not*
meaningfully accreting. Pool depth is modest (τ2.6k / 259k α reserve), enough that a newcomer's tiny
daily sell won't crash it. Very young subnet (~4% of supply emitted) → short, thin price history;
recent multi-week trend **UNKNOWN** (confirm at taostats.io/subnets/67).

### Miner pool $/day — and the 63.7% owner-champion trap
Standard alpha emission ≈ 7,200 α/day per subnet; miner slice ≈ 41% ≈ **~2,950 α/day** (default
M_alpha; not separately verifiable per-subnet — flagged as assumption).

- **Gross miner pool** = 2,950 × 0.0100 × $235 ≈ **$6.9k/day** — misleading on its own.
- On-chain incentive: **UID 0 (Harnyx *Owner*) = 0.6365 incentive** → owner self-mines **63.7%** of
  the miner slice (≈ 1,878 α/day ≈ $4.4k/day to itself) as the standing **champion**.
- **Contestable participant pool = 36.3% ≈ ~1,072 α/day ≈ $2.5k/day**, split ~141 ways (see Phase 4).
  **This is the real number a newcomer competes for — and it's shared very flatly.**

---

## PHASE 2 — What is the work?

**Work type: agentic LLM "deep research" (code submission).** *Not* GPU inference, not training.

Miners **submit a Python agent** implementing a `query` entrypoint (text in → text out) that performs
multi-step research **"under a tight tool budget."** Validators **execute the submitted agent in
sandboxed containers** against batches of research tasks, judge the output, and set weights on-chain.
Harnyx's pitch: bridge the gap between fast/cheap web search and slow/expensive AI research —
comprehensive multi-step research at low cost (source: repo README + subnetalpha.ai listing).

**Required hardware (miner): effectively none.** The miner ships *code*; the **validator** runs it
and supplies the execution/tool budget. There is no miner-side GPU, no model hosting, no inference
rig to keep online. The constraint is the **tool budget** (token/tool-call cost the agent may spend
per task), not your hardware.

**Min viable rig cost: ~$1–2/day** (a dev box + light monitoring; no GPU). Compute capex is
**negligible** — unusual and attractive. The scarce input is *engineering skill at agent design*.

**EDGE TEST — PASS (conditional).** Reward is for **research-agent quality** (better workflow,
reasoning, and cost-efficiency under budget), **not commodity GPU-hours**. A skilled agent/LLM-tooling
engineer *can* hold a real, durable edge. A commodity template agent has **no edge** → lands in the
flat participant dust at best (Phase 3/4).

---

## PHASE 3 — Incentive mechanism teardown (the traps)

Source: repo README (github.com/harnyx/harnyx), read 2026-06-23. (Scoring *code* not line-audited;
mechanism summary below is from the documented design — confidence flagged accordingly.)

- **Distribution shape — split: champion + tiered participants.**
  - **Champion emission:** the incumbent **champion keeps the lion's share** unless a challenger
    clears a **"dethroning rule"** — must beat the champion by a **sufficient score margin OR better
    runtime/cost efficiency**. Critically, *"the champion is not always the highest score in the
    batch"* and the incumbent's newer submissions get an **ordering advantage**. → on-chain this is
    the owner UID 0 holding **63.7%**.
  - **Participant emission:** tiered by normalized score — **top 10% → 2× base, top 50% → 1× base,
    rest → 0.** This is the contestable ~36% pool, and it is **flat** (everyone in a tier earns the
    same) — see Phase 4 (99 UIDs at the 1× tier, 41 at the 2× tier).
  - **Scoring:** *"comparison_score: pairwise judge vs reference answer, run twice with swapped order"*;
    ties prefer **lower total tool cost**.
- **Rich-get-richer: YES (the core trap).** The champion *retains* rewards by default and enjoys an
  ordering advantage on re-submission — incumbency is structurally sticky. Whoever holds the champion
  slot keeps ~64% until *decisively* out-scored/out-efficient'd.
- **Assignment gating:** none observed — validators run *all* registered miners' agents against task
  batches (open assignment, no orchestrator hand-picking who works). No whitelist, no stake-gate seen.
- **Failure penalties:** soft — below top-50% simply earns **0** participant emission (no negative
  subtraction); a broken/over-budget agent just scores low.
- **Weight-setting:** aggregated validator scores → weights → on-chain via Bittensor; commit-reveal
  enabled (`commit_reveal_weights_enabled True`, period 1). Yuma v2. No single-validator capture
  evident (stake spread across tao.bot, Kraken, Yuma/DCG, TAO.com, 1T1B.AI, Rizzo).
- **Newcomer cold-start: FAST for dust.** A fresh hotkey whose agent lands in the **top 50%** of a
  batch earns **1× participant emission within days** — no gating, cheap reg (τ0.07). Earning *real*
  money requires **dethroning the owner-champion**, which is hard and reflexive.

**Mechanism trap (loud): `rich_get_richer`** (champion retention + ordering advantage) **plus owner
self-capture of 63.7%.** Not winner-take-all (participant tiers pay out broadly), not a synchronized
cohort, not assignment-gated. The danger is the *sticky champion*, not exclusion from work.

---

## PHASE 4 — Saturation / competition

Source: `btcli subnet metagraph --netuid 67` (saved as `raw_metagraph.txt`), 2026-06-23.

- **UIDs with incentive > 0: 142** (incl. owner UID 0). Incentive shares sum to 1.000.
- **Owner UID 0 = 0.6365 (63.7%)** — the standing champion.
- **Contestable participant pool (excl. UID 0) = 0.3634 of total**, and it is **extremely flat**:
  - **99 UIDs at incentive ≈ 0.001999** (the top-50% "1×" tier).
  - **41 UIDs at incentive ≈ 0.003998** (the top-10% "2×" tier).
  - Top-2 (owner + best participant) = **64.1%**; the #2 *miner* holds only ~0.4%.
  - **Effective number of earners = 1/Σshareᵢ² = 2.46** (dominated by the owner). Excluding the owner,
    the participant pool is spread across ~140 near-identical dust positions.
- **Per-head participant economics (BASE case math):** participant pool ≈ 0.3634 × 2,950 ≈ **1,072
  α/day**. Tier weights = 41×2 + 99×1 = **181 units** → **~5.9 α/day per "1×" unit**:
  - **top-10% (2×) miner ≈ 11.8 α/day ≈ $27.8/day gross**
  - **top-50% (1×) miner ≈ 5.9 α/day ≈ $13.9/day gross**
- **Big stakers present but NOT mining:** tao.bot (UID 12), Kraken (220), Yuma/DCG (11), TAO.com (197),
  1T1B.AI (7), Rizzo (5) all show **incentive = 0, large dividends** → they are validators/stakers, not
  miner competitors.
- **No public miner heartbeat / capability S3 bucket** found — irrelevant here anyway, since miners
  submit *code*, not rigs; there is no hardware fleet to fingerprint. The moat is **agent quality**.
- **Registration cost:** τ 0.0703 (~$16.5) one-time, recycled (non-refundable).

**Saturation: 2/5.** The participant pool is already **crowded (~140 miners) and flat** — entry earns
you a same-as-everyone dust slice, not a scalable share — while the single biggest prize (the ~64%
champion slot) is **held by the owner**. Headroom for *meaningful* earnings is narrow; headroom for
*token-dust* earnings is wide-open but tiny per head.

---

## PHASE 5 — EV synthesis

**Assumptions:** TAO = $235; alpha = 0.0100 τ (so 1 α ≈ $2.35); M_alpha ≈ 2,950 α/day (assumed);
participant pool ≈ 1,072 α/day; **miner capex ~$1.5/day** (no GPU — dev box only); registration
τ0.0703 amortized over 60 days ≈ $0.28/day; ops ~$1.5/day → **costs ≈ $3/day**. Realized-price factor
= liquidation haircut × trend ≈ **0.85** (deep reserve vs a newcomer's few-α daily sell → slippage
negligible; net inflow only marginally positive and price low → modest discount; trend unconfirmed).

Newcomer outcomes (the contest is *tiered*, so the participant cases are stable; the champion case is
bimodal & reflexive):

| Scenario | Behavior | Daily α | Gross $/day | **Net EV/day** | **Net EV/month** |
|---|---|---|---|---|---|
| **LOW** | Template agent; intermittently makes top-50% (1× tier), sometimes scores 0 | ~3 α | ~$7 | **~$3** | **~$100** |
| **BASE** | Competent custom agent; steady **top-10% (2×) participant** | ~11.8 α | ~$23.6 (×0.85 ≈ $20) | **~$17** | **~$500** |
| **HIGH** | Builds a genuinely superior, cost-efficient agent and **dethrones the owner-champion** for sustained periods (~capturing the ~64% slot) | up to ~1,878 α | up to ~$3.7k | **~$3,700** *(unstable)* | **up to ~$110k** *(unstable)* |

> Honest caveat: the **realistic mode for a commodity newcomer is LOW/BASE (~$100–500/mo)** — real
> but small. **HIGH requires actually beating the owner's champion agent by margin or efficiency**, and
> is **reflexive and fragile**: the owner gets an ordering advantage on re-submission, can re-tune its
> own agent, and *controls the subnet's scoring rules and hyperparameters*. Treat HIGH as a
> low-probability, owner-revocable ceiling, not a plan.

- **Single biggest risk:** the **owner self-captures ~64% as a sticky champion and writes the rules.**
  Even a great agent can be out-ordered, out-margined, or rule-changed out of the champion slot; the
  participant pool alone is dust-tier.
- **Single thing that would most change the answer:** whether **you can reliably clear the dethroning
  rule** (beat the champion on score margin AND/OR cost-efficiency). With that capability → GO; without
  it → the ceiling is ~$500/mo participant dust.
- **Minimum edge to be +EV:** a **measurably better deep-research agent** — superior multi-step
  workflow + reasoning *at lower tool cost* than incumbents. Commodity/template agents → ~$0–100/mo,
  roughly break-even after costs. (Costs are so low that even dust is *technically* +EV, but not
  worth the effort unless you can climb tiers.)

**Recommendation: WATCH** (conditional GO for a strong agentic-research engineer who can dethrone the
champion; NO-GO for a commodity miner expecting passive yield).

---

## SCORECARD
```
SCORECARD
netuid: 67
name: Harnyx
work_type: other            # agentic LLM "deep research" — miners submit Python agents, no GPU
alpha_price_tao: 0.0100
net_inflow_ema_tao: +0.0002
token_health: 2             # low price (0.0100, SN24 tier) + only marginally positive inflow; trend unknown
miner_pool_usd_per_day: 2500   # CONTESTABLE participant pool; gross ~$6.9k but 63.7% self-captured by owner UID0 champion
effective_num_earners: 2.46    # 1/Σshare² across all UIDs (owner-dominated); participant pool itself spread ~140 ways flatly
saturation: 2                  # ~140 miners already in a flat dust pool; the ~64% champion slot owner-held
min_rig_cost_usd_per_day: 1.5  # no GPU — miner submits code; validator runs it
registration_cost_tao: 0.0703
mechanism_trap: rich_get_richer   # sticky champion + ordering advantage + owner 63.7% self-capture
newcomer_friendliness: 3       # cold-start earns dust fast (top-50%=1x), open/no stake gate, cheap reg — but real money champion-gated
edge_required: a measurably better, more cost-efficient deep-research agent that can clear the dethroning rule vs the owner-champion; commodity/template agents = ~break-even dust
ev_usd_per_month_low: 100
ev_usd_per_month_base: 500
ev_usd_per_month_high: 110000   # owner-champion capture; LOW-PROBABILITY, reflexive, owner-revocable ceiling
confidence: 3
recommendation: WATCH
composite_score: 13            # token_health 2 + saturation 2 + newcomer_friendliness 3 + WATCH 3 + confidence 3
one_line_thesis: Near-zero-capex deep-research-agent contest where skill (not GPU) is the edge, but the owner self-captures ~64% as a sticky, rule-controlling champion and the rest is a flat ~140-way dust pool — only an engineer who can actually dethrone the champion is meaningfully +EV.
```

### Key evidence (with sources)
- **alpha 0.0100 τ, net inflow +0.0002, mcap τ8.61k, emission τ0.0053, reserve τ2.60k/259.14k α,
  supply 857k/21M, reg τ0.0703** — `btcli subnet list` / `subnet show --netuid 67` (finney), 2026-06-23.
- **Owner UID 0 incentive 0.6365 (63.7%)**; participant pool 0.3634 split across ~140 UIDs (99 @ 0.001999
  "1×" tier, 41 @ 0.003998 "2×" tier); **effective earners 2.46** — `btcli subnet metagraph --netuid 67`
  (see `raw_metagraph.txt`).
- **Work = agentic deep research; miners submit a Python `query` agent under a tool budget; validators
  sandbox-run and judge** — repo README, github.com/harnyx/harnyx + subnetalpha.ai/subnet/harnyx.
- **Mechanism = champion emission (dethroning rule: score margin or better runtime/cost; ordering
  advantage to incumbent) + tiered participant emission (top10%=2×, top50%=1×, rest=0); comparison_score
  pairwise judge run twice swapped; ties prefer lower tool cost** — repo README (design summary; code not
  line-audited).
- **No GPU / no model hosting on miner side; validator supplies execution + tool budget** — repo README.
- **Big stakers (tao.bot, Kraken, Yuma/DCG, TAO.com, 1T1B.AI, Rizzo) have incentive 0 = validators not
  miners** — metagraph.
- **TAO ≈ $235 (range 225–265)** — CoinGecko / CoinMarketCap / Coinbase / MEXC, 2026-06-23.
- **Price trend: UNKNOWN** — taostats subnet-67 chart not machine-readable; obtain at taostats.io/subnets/67.

**Sources:**
- https://github.com/harnyx/harnyx
- https://subnetalpha.ai/subnet/harnyx/
- https://www.coingecko.com/en/coins/bittensor
- https://coinmarketcap.com/currencies/bittensor/
- https://taostats.io/subnets/67
