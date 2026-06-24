# Subnet 56 (Gradients) — Mining EV Teardown

_Analysis date: 2026-06-23. Chain: finney. Analyst pass per SUBNET_EV_RESEARCH_PROMPT.MD._

**Gradients** (by **Rayon Labs**, repo `rayonlabs/G.O.D`, product `gradients.io`) is a
decentralized **AutoML / fine-tuning** platform. Paying customers upload a dataset and
pick a base model through a 4-click UI; the subnet's miners compete to produce the
best fine-tuned LLM or diffusion model. Critically, miners do **not** run a perpetual
inference service — they author **open-source training scripts** that **validators
execute on dedicated infrastructure** inside scheduled **knockout tournaments**.
Reward flows to whoever's script wins. It is a **stake-gated, rich-get-richer
tournament with a defending-champion "boss round."**

---

## PHASE 1 — Token economics (chain-verified)

Source: `btcli subnet list --network finney`, row netuid 56.

| Metric | Value | Source |
|---|---|---|
| TAO/USD | ~$225 (CMC $225, CoinGecko $218, some venues $235–264) | WebSearch CMC/CoinGecko |
| Alpha price (Τ_in/α_in) | **0.0189 τ/α** | subnet list |
| Market cap (α × price) | **τ 100.54k** (~top-6 subnet by α-cap) | subnet list |
| Emission (Τ) | 0.0029 τ/block | subnet list |
| **Net Inflow EMA (Τ)** | **−0.0090 τ (STRONGLY NEGATIVE / melting)** | subnet list |
| Pool P(Τ_in, α_in) | τ 54.22k, 2.88m α | subnet list |
| Stake (α_out) | 2.45m α | subnet list |
| Supply | 5.32m α / 21M | subnet list |
| Tempo (n) | 360 blocks (~20 tempos/day) | subnet show |
| Mechanisms | 1 | subnet list |
| Registration cost (recycled) | **τ 0.0005 (~$0.11 — effectively free)** | `btcli subnet show --netuid 56` |
| Owner coldkey | 5EJ1zb… (Owner56) | subnet show |
| Recent α trend | **−6.32% (downtrend)** | taostats.io/subnets/56 |

**Miner pool $/day.** Using protocol default M_alpha ≈ 2,950 α/day to miners
(~1 α/block × 41% × 7,200 blocks/day):

```
miner_pool_usd_per_day = 2,950 α × 0.0189 τ × $225 ≈ $12,545/day
```

**Token-health verdict: WEAK (2/5).** Two things pull in opposite directions. Positive:
α-market-cap τ100.54k makes this a large, prominent subnet (Rayon Labs flagship, real
paying customers ~3k), and the pool reserve τ54.22k is deep — a newcomer liquidating
even a few hundred $/day of alpha is a rounding error on slippage. Negative, and
decisive: **net inflow EMA is −0.0090 τ — strongly melting, more than 2× worse than the
Quasar reference (−0.0040)** — and alpha is in a **−6.3% recent downtrend**. You'd be paid
in a token whose supply is inflating into net selling pressure. The deep pool protects
against *slippage*, not against *trend*. Discount realized price meaningfully.

---

## PHASE 2 — What is the work?

Source: `github.com/rayonlabs/G.O.D` README + miner docs, learnbittensor.org, gradients.io.

- **Work type:** model **training / fine-tuning** (AutoML). LLM text fine-tunes and
  diffusion/image fine-tunes. Not inference, not bandwidth, not storage.
- **Who pays the big compute:** **validators run the winning/submitted training scripts on
  their own dedicated infra during tournaments.** Miners pay for **R&D compute** to develop
  and locally validate their training recipes — not for the production tournament runs.
  This inverts the usual "rent a fat GPU 24/7" cost structure.
- **Min viable rig (R&D):** a single A100/H100-class GPU rented *part-time* during recipe
  development. Cross-check Vast/RunPod H100 ≈ $2–3/hr; intermittent dev use ≈ **$15–25/day**
  amortized. No standing 24/7 production rig required of the miner.
- **EDGE TEST:** This is the rare subnet where the reward is **NOT** for commodity GPU-hours —
  it is for **better AutoML / fine-tuning methodology** (data curation, hyperparameter
  search, LoRA/full-FT recipes, eval gaming). A newcomer with genuine ML-research skill
  *can* in principle have a real, durable edge here. But the bar is "beat ~31 other teams
  including Rayon Labs' own," and the mechanism (below) hands incumbents a structural margin.

---

## PHASE 3 — Incentive mechanism teardown (the traps)

Sources: G.O.D README, learnbittensor.org SN56, themarketsunplugged SN56 review.

- **Distribution shape — knockout tournament, exponential to top performers.** Up to **32
  miners** per tournament compete on one challenge; **top-8 advance** to a knockout bracket,
  facing off until **one challenger** remains. Points scale **exponentially per round
  advanced** → strongly **winner-take-all-flavored**, not proportional.
- **Defending-champion "boss round" (the big trap).** The surviving challenger must beat the
  **current champion** in a multi-task boss round **by a 5–10% margin**, where the required
  margin **grows with how many times the champion has already defended**. This is an explicit
  **incumbent moat.** It is visible on-chain: **UID 38 = "Owner56" (the subnet owner) holds
  incentive 0.6659 — ~66.6% of ALL miner reward.** The owner is the entrenched champion.
- **Rich-get-richer (confirmed).** Tournament seeding is by **ALPHA stake in SN56**, and
  **miners who participated in prior tournaments receive a stake bonus** that helps them
  re-qualify. Past success → easier future entry → compounding.
- **Assignment / gating:** **stake-gated** qualification (must hold/stake alpha to enter the
  32-slot field) **plus an ~$80 buy-in per tournament.** Registration itself is near-free
  (τ0.0005), but earning is gated behind stake + buy-in + winning.
- **Weight-setting:** validators score tournament outcomes; base emission was ~10% (image) /
  15% (text), with strong performers able to earn up to **40% (image) / 60% (text)** — i.e.
  the schedule deliberately concentrates reward on winners.
- **Newcomer cold-start:** **cannot earn fast.** A fresh hotkey must acquire alpha stake to
  qualify, pay the buy-in, place top-8 against a strong field, win the bracket, then beat a
  defending champion by a widening margin. Days-to-first-reward is unrealistic without a
  top-tier recipe.

---

## PHASE 4 — Saturation / competition

Source: `btcli subnet show --netuid 56` incentive column (raw saved: `raw_subnet_show.txt`).

Incentive (miner reward) distribution among UIDs with incentive > 0:

| UID | Identity | Incentive share |
|---|---|---|
| 38 | **Owner56 (subnet owner / champion)** | **0.6659 (66.6%)** |
| 148 | ~ | 0.1450 |
| 76 | ~ | 0.0855 |
| 28 | ~ | 0.0396 |
| 44 | ~ | 0.0297 |
| 20 | ~ | 0.0296 |
| 203 | ~ | 0.0040 |
| 6× tail | ~ | ~0.0001 each |

- **Top-1 share = 66.6% (the owner).** Top-2 = 81.1%.
- **Effective number of earners = 1/Σ shareᵢ² = 2.1.** The entire ~$12.5k/day miner pool is
  effectively split between **~2 entities**, dominated by the owner-champion.
- Hundreds of UIDs are **registered** (metagraph runs to UID 255+) but **earning ~0** — the
  classic "registered ≠ earning" gap. Most non-zero-incentive UIDs outside the top 7 earn
  literal dust.
- **Registration cost:** τ0.0005 (~$0.11) — trivially cheap. The barrier is **not**
  registration; it's the stake-gate + buy-in + the champion moat.

**Saturation verdict: 2/5.** At the top it is highly concentrated (champion owns 2/3), but
unlike a frozen orchestrator-assigned subnet, the tournament *does* rotate challengers and
the 2nd–6th slots turn over — there's a live (if brutal) ladder. Net: saturated at the prize
tier, with a long tail earning nothing.

---

## PHASE 5 — EV synthesis

**Assumptions (stated):** marginal newcomer with *competent but not world-class* ML skill;
M_alpha = 2,950 α/day; alpha 0.0189 τ; TAO $225; pool $12.5k/day. Costs: R&D dev rig
~$20/day + tournament buy-in ~$80 (~1–2/week → ~$15–25/day amortized) + alpha stake lockup
(capital at risk in a melting token) + near-zero registration. Liquidation: pool is deep
(slippage ≈ 0) but **price-trend haircut ≈ 0.7** (−6.3% trend + negative inflow).

**Newcomer steady-state share (justified):**
- **LOW (likely, marginal entrant):** fails to consistently place top-8 → share ≈ 0%.
  Outcome = bleed buy-ins + watch staked alpha melt. **Net ≈ −$40/day → ≈ −$1,400/mo.**
- **BASE (solid ML, occasional mid-bracket finish ~0.5–1% of pool):** gross
  ~$60–125/day × 0.7 haircut ≈ $45–87 − ~$43 costs → **roughly breakeven, slightly negative.
  ≈ −$150 to $0/mo.**
- **HIGH (genuine top-tier AutoML team, reliably reaches late knockout / boss rounds,
  5–8% share, occasional champion capture):** gross ~$625–1,000/day × 0.75 ≈ $470–750 − $43
  → **≈ +$13,000 to +$21,000/mo.** The dream tail (become and defend champion → 40–66% of
  pool ≈ $5–8k/**day**) exists but is not "newcomer steady state."

| | EV/day | EV/month |
|---|---|---|
| LOW | −$45 | **−$1,400** |
| BASE | ~$0 | **−$150** |
| HIGH | +$450 | **+$13,500** |

**Biggest risk:** the **defending-champion boss round + stake-bonus rich-get-richer** — the
owner already captures 66.6%, and the margin you must beat them by *grows each time they
defend*. You can be the best *challenger* and still earn little if you can't dethrone the
champion. Compounded by a **melting token** (−0.0090 inflow, −6.3% price).

**Single thing that would most change the answer:** your actual **AutoML edge**. This is a
skill subnet, not a GPU subnet — if you can demonstrably out-fine-tune the field, the
near-free registration, validator-paid production compute, and deep liquidation pool make
the HIGH case real. If you're "competent but average," it's structurally −EV.

**Recommendation: NO-GO for a commodity/marginal newcomer.** Conditional **WATCH→GO only if
you bring a genuine, demonstrable fine-tuning research edge** (a recipe that beats Rayon
Labs' own team and ~30 others). Minimum edge required: **top-decile AutoML methodology**, not
cheap GPUs.

---

```
SCORECARD
netuid: 56
name: Gradients
work_type: training
alpha_price_tao: 0.0189
net_inflow_ema_tao: -0.0090
token_health: 2
miner_pool_usd_per_day: 12545
effective_num_earners: 2.1
saturation: 2
min_rig_cost_usd_per_day: 20
registration_cost_tao: 0.0005
mechanism_trap: rich_get_richer
newcomer_friendliness: 2
edge_required: top-decile AutoML/fine-tuning methodology (must beat the defending champion incl. Rayon Labs by a widening 5-10% margin); commodity GPU skill is NOT enough
ev_usd_per_month_low: -1400
ev_usd_per_month_base: -150
ev_usd_per_month_high: 13500
confidence: 4
recommendation: NO-GO
composite_score: 11
one_line_thesis: Skill-gated AutoML tournament with a defending-champion moat — the owner captures 66.6% of a melting-token pool; structurally -EV for a marginal newcomer, only +EV for a genuine top-tier fine-tuning team.
```

### Key evidence (with sources)
- **token_health 2/5:** alpha 0.0189 τ, mcap τ100.54k (large), but **net inflow −0.0090 τ
  (melting, 2× worse than Quasar)** and **−6.3% trend** — `btcli subnet list` row 56; taostats.io/subnets/56.
- **miner_pool ≈ $12.5k/day:** 2,950 α × 0.0189 τ × $225 — default M_alpha, prompt formula.
- **effective_num_earners 2.1 / saturation 2:** incentive column, `btcli subnet show --netuid 56`
  — **UID 38 (Owner56) = 66.6%**, top-2 = 81%, 1/Σshare² = 2.1 (raw_subnet_show.txt).
- **mechanism_trap rich_get_richer (+ stake_gated + winner-take-all):** 32-miner knockout,
  top-8 advance, exponential per-round points, **defending-champion boss round, beat-by-5–10%
  margin growing per defense, returning-miner stake bonus, ALPHA-stake seeding** —
  `rayonlabs/G.O.D` README; learnbittensor.org/subnets/rayonlabs/gradients; themarketsunplugged SN56 review.
- **newcomer_friendliness 2/5:** registration τ0.0005 (~$0.11, near-free) BUT stake-gated +
  ~$80/tournament buy-in + must dethrone entrenched champion — `btcli subnet show`; SN56 docs.
- **min_rig $20/day:** miners fund only R&D compute; validators run production training —
  G.O.D README; Vast/RunPod H100 ≈ $2–3/hr part-time.
- **recommendation NO-GO:** marginal newcomer EV ≈ −$150 to −$1,400/mo; only a top-tier ML
  edge reaches the +$13.5k/mo HIGH tail.
```
```
