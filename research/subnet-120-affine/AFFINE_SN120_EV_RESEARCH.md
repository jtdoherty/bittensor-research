# Bittensor Subnet 120 — Affine: New-Miner EV Research

**Date:** 2026-06-23  ·  **Network:** finney  ·  **Analyst role:** mining-economics
**Subnet:** netuid 120 (Affine) — incentivized reinforcement-learning model competition
**Owner coldkey:** `5Fc3ZZQAYB3SPXKcFnd1WJeyQvArSZZeB6LU1rb7zvQ6XvDh` (const / "const_reborn" — Bittensor founder Const)
**Repo:** https://github.com/AffineFoundation/affine-cortex  ·  Site: affine.io

> Bottom line up front: **NO-GO** for a commodity newcomer. Affine is a **winner-take-all,
> strict-Pareto model contest**: you commit a HuggingFace `(model, revision)` and must beat the
> reigning champion **strictly across every RL environment** to earn — and **losers are
> "permanently terminated"** (the τ3.01 ≈ $700 registration is forfeit). The miner pool is
> currently split among **exactly 5 hotkeys at 0.20 incentive each**, the token is **melting
> (net inflow −0.0051)**, and the only edge that wins is **frontier-grade ML research** (training
> a model that Pareto-dominates on program synthesis / reasoning / code). Not a GPU-rental play.

---

## PHASE 1 — Token economics (chain-verified)

Source: `btcli subnet list --network finney` (row 120), `btcli subnet show --netuid 120`.

| Metric | Value | Source |
|---|---|---|
| TAO/USD | ~$235 (range $215–265 across exchanges) | CoinMarketCap / Coinbase / CoinGecko, 2026-06-23 |
| Alpha price (Τ_in/α_in) | **0.0590 τ/α** | subnet list |
| Market cap (α × price) | **τ 209.31k** | subnet list |
| Emission (Τ) share | τ 0.0125 | subnet list |
| **Net Inflow EMA (Τ)** | **−0.0051 (NEGATIVE — melting)** | subnet list / show |
| Pool reserves P (Τ_in, α_in) | τ 79.28k, 1.34m α | subnet list |
| Stake (α_out) | 2.21m α | subnet list |
| Supply / max | 3.55m α / 21M (~17% emitted) | subnet list |
| Tempo | 360 blocks | subnet show |
| **Registration cost (recycled)** | **τ 3.01 (~$707)** one-time, non-refundable | subnet show |

**Token-health verdict: 3/5.** Alpha price **0.0590 τ is high** vs peers (calibration: SN24
Quasar 0.0099, SN107 Minos 0.0383 — Affine is ~1.5–6× those) and market cap τ209k is large/
mature. **But net inflow is NEGATIVE (−0.0051)** — the token is **melting**: more value is
leaving the pool than entering, so realized payout depreciates over time. Recent multi-week
price trend: **UNKNOWN** (taostats chart not machine-readable; confirm at taostats.io/subnets/120).
High price + negative inflow = a "premium but draining" token — discount realized EV.

### Miner pool $/day
Standard alpha emission ≈ 7,200 α/day per subnet; miner slice ≈ 41% ≈ **~2,950 α/day**
(default M_alpha; not separately verified per-subnet — flagged as assumption).

- **Gross miner pool** = 2,950 × 0.0590 × $235 ≈ **~$40,900/day**.
- On-chain incentive sums to 1.000 across **exactly 5 hotkeys, each 0.199985** → **~$8,180/day
  per champion slot** (before liquidation haircut). **There is no owner self-capture of the
  miner pool** — owner UID 0 holds 0.70 *dividends* (validator/stake reward) but **0 incentive**.
- The catch: those 5 slots are held by whoever currently sits on the Pareto frontier; a newcomer
  earns **$0** until it dethrones an incumbent, and forfeits its model slot (and registration)
  if it tries and loses.

---

## PHASE 2 — What is the work?

**Work type: model training / submission (RL model competition).** *Not* a compute-rental subnet.

Miners **commit a HuggingFace `(model, revision)` pair on-chain**; **validators host the
inference** (currently via Targon, optionally an operator-run B300 fleet) and evaluate the model
on a **suite of RL environments** — program induction / synthesis, reasoning, and code generation.
The miner does **not** run continuous inference or serve GPU-hours; the miner's product is a
**better model artifact**.

**Required hardware (on-subnet):** effectively **none continuous** — you commit a model pointer
and validators run it. **The real cost is OFF-subnet: training/fine-tuning a competitive model**,
which for a frontier-grade reasoning/coding model is a large, lumpy R&D + GPU bill (potentially
$1k–$100k+ of training compute), not a metered daily rental. This makes "min rig cost/day"
misleading — the binding cost is model-development capital, not a Vast/RunPod box.

**EDGE TEST — FAIL for commodity; PASS only for a frontier ML lab.** Reward is **not** for
commodity GPU-hours and **not** for an off-the-shelf open model — it is for a model that
**strictly Pareto-dominates the current champion across every environment**. The required edge
is **genuine frontier ML research capability** (better RL fine-tuning / reasoning models than
existing well-funded incumbents). A newcomer downloading Qwen/Llama and committing it has **no
edge** and will be terminated on first contest.

---

## PHASE 3 — Incentive mechanism teardown (the traps)

Source: repo README (github.com/AffineFoundation/affine-cortex).

- **Distribution shape — winner-take-all, strict-Pareto dethroning.** "The winner-takes-all
  weight goes to the champion until they're dethroned." A challenger "**only dethrones the
  champion when they win strictly across all environments by a per-env margin; otherwise they're
  permanently terminated**." (The live metagraph shows the weight currently split equally across
  **5** hotkeys at 0.20 each — i.e. a small champion cohort, not a single UID — but the
  *mechanism* is strict winner-take-all per frontier position.)
- **Contest queue:** "the validator-side scheduler walks the queue of pending miners in
  `first_block` order"; each challenger "faces the current champion across every evaluation
  environment in a single back-to-back contest."
- **Task refresh:** "Every ~7200 blocks (~24h) the per-env task-id pool is refreshed" — so you
  can't pre-memorize the exact eval items.
- **Failure penalty — SEVERE.** Losing a contest = **"permanently terminated."** This is the
  loudest red flag: a failed challenge **burns your registration** (τ3.01 ≈ $700) with no
  participation reward. There is no soft "earn dust while you improve" path.
- **Anti-gaming:** explicitly "**sybil-proof, decoy-proof, copy-proof, overfitting-proof**" — you
  cannot multi-register, can't pack a single environment, can't copy the champion's model, and
  can't overfit one env. All four close the usual cheap-edge loopholes.
- **Cold-start:** a fresh hotkey earns **0** until it wins a contest outright; first action is a
  high-stakes all-or-nothing challenge.

**Mechanism trap (loud): `winner_take_all`** + **permanent-termination penalty** + strict-Pareto
gate. This is among the most newcomer-hostile reward structures of any subnet analyzed.

---

## PHASE 4 — Saturation / competition

Source: `btcli subnet metagraph --netuid 120` (saved as `raw_metagraph.txt`), `subnet show`.

- **UIDs with incentive > 0: exactly 5** — UIDs 78, 154, 161, 219, 229, **each 0.199985**
  (equal split). Incentive sums to 1.000.
- **Effective number of earners = 1 / Σ shareᵢ² = 1 / (5 × 0.20²) = 5.0.** Perfectly even
  among the 5 — no single dominator, but only 5 slots exist.
- Large named stakers (TAO.com, Yuma/DCG, Kraken, tao.bot, Rizzo) hold **dividends, incentive = 0**
  → they are validators/stakers, **not miners**. Owner UID 0 = 0.70 dividends, 0 incentive.
- **256 UIDs registered; only 5 earn** → ~251 registered-but-earning-0 (classic "registered ≠
  earning"). Many zero-stake hotkeys appear parked/churned — consistent with the
  "permanently terminated" loser dynamic burning through registrations.
- **No public miner heartbeat / capability S3 bucket** (inference is validator-hosted via Targon),
  so incumbent rigs can't be fingerprinted — but it's irrelevant here: the moat is **model
  quality**, not rig specs.
- **Registration cost: τ 3.01 (~$707)** one-time, non-refundable — and effectively at-risk because
  a losing challenge terminates you.

**Saturation: 2/5.** Only 5 earners *looks* open, but the slots are held by frontier-model
champions defended by a strict-Pareto + permanent-termination gate. Effective headroom for a
commodity entrant is near zero; this is "saturated by sophistication," not by headcount.

---

## PHASE 5 — EV synthesis

**Assumptions:** TAO = $235; alpha = 0.0590 τ; full miner pool ≈ 2,950 α/day (~$40.9k/day) split
across 5 champion slots ≈ **$8,180/day per slot**; registration τ3.01 ≈ $707 (at-risk, not just
amortized); ops/hosting nominal ~$50/day; **off-subnet model-training cost is the real, large,
uncounted line item**. Realized-price factor = liquidation haircut × trend ≈ **0.70** (pool is
deep at 1.34m α so slippage on a small daily sell is minor, but **negative net inflow + melting
token** forces a meaningful trend discount).

Outcomes are **extremely bimodal / all-or-nothing** by mechanism design:

| Scenario | Behavior | Slot capture | Gross $/day | **Net EV/day** | **Net EV/month** |
|---|---|---|---|---|---|
| **LOW** | Commodity newcomer commits an off-the-shelf model → loses first contest → **terminated** | 0 | $0 | **≈ −$24/day** (lost reg amortized + ops, $0 income) | **≈ −$707 one-off, then $0** |
| **BASE** | Strong fine-tuner briefly edges into/holds a slot intermittently, high variance, eventual displacement | ~0.3 slot intermittent | ~$2,450 | **~$1,650** (before training capex) | **~$50,000 minus training cost — highly uncertain** |
| **HIGH** | Genuine frontier ML lab trains a Pareto-dominant reasoning/code model, holds a full slot | ~1 slot | ~$8,180 | **~$5,650** (before training capex) | **~$170,000 minus large training cost** |

> Honest caveat: the **realistic mode for any non-frontier-lab newcomer is LOW (≈ loss of the
> ~$700 registration, $0 income, terminated).** BASE and HIGH **require frontier ML research
> capability** to produce a model that strictly Pareto-dominates incumbents — and even HIGH is
> reflexive (the moment you win, well-resourced rivals retrain to dethrone you, and the token is
> melting underneath the payout). Training capex is not netted in the table and can dwarf the
> on-chain costs.

- **Single biggest risk:** the **permanent-termination penalty** — a failed challenge burns your
  registration with zero consolation, so the downside is hard-capped-negative and the upside is
  gated behind beating a frontier model.
- **Single thing that would most change the answer:** whether *you* can train a model that
  **strictly Pareto-dominates the current champion across all environments**. With a genuine
  frontier-model edge → conditional GO (HIGH). Without it → hard NO-GO.
- **Minimum edge to be +EV:** frontier-grade RL/reasoning/code model development that can beat the
  reigning champion outright across every environment. Anything less than that = guaranteed loss
  of the registration.

**Recommendation: NO-GO** (conditional GO *only* for a well-capitalized frontier ML team that can
out-train the incumbent champions).

---

## SCORECARD
```
SCORECARD
netuid: 120
name: Affine
work_type: training            # commit HuggingFace (model,revision); validators host inference; RL env competition
alpha_price_tao: 0.0590
net_inflow_ema_tao: -0.0051
token_health: 3                # high alpha price + large mcap, BUT negative net inflow (melting); trend unconfirmed
miner_pool_usd_per_day: 40900  # total across 5 champion slots; ~$8,180/slot; no owner self-capture of miner pool
effective_num_earners: 5.0     # 1/Σshare² ; 5 hotkeys at 0.20 each (equal split)
saturation: 2                  # only 5 earners but defended by strict-Pareto + permanent-termination; near-zero headroom for commodity
min_rig_cost_usd_per_day: 50   # on-subnet near-zero (validators host inference); REAL cost = off-subnet model training (large, uncounted)
registration_cost_tao: 3.01
mechanism_trap: winner_take_all   # + permanent-termination of losers + strict-Pareto dethroning gate
newcomer_friendliness: 1       # cold-start = all-or-nothing challenge; lose => terminated + forfeit ~$707 reg
edge_required: frontier ML research — train a model that STRICTLY Pareto-dominates the champion across all RL envs; off-the-shelf/commodity = guaranteed loss
ev_usd_per_month_low: -707
ev_usd_per_month_base: 50000   # HIGHLY uncertain; before large training capex; requires real model edge
ev_usd_per_month_high: 170000  # frontier lab holding a full slot; before training capex; reflexive/contested
confidence: 3
recommendation: NO-GO
composite_score: 10            # token_health 3 + saturation 2 + newcomer_friendliness 1 + NO-GO 1 + confidence 3
one_line_thesis: Affine is a winner-take-all strict-Pareto model contest where losers are permanently terminated and forfeit a ~$707 registration; with only 5 frontier-champion slots and a melting token, it is NO-GO for any newcomer without genuine frontier-model training capability.
```

### Key evidence (with sources)
- **alpha 0.0590 τ, net inflow −0.0051 (melting), mcap τ209.31k, emission τ0.0125, reg τ3.01,
  tempo 360** — `btcli subnet list` / `subnet show --netuid 120` (finney), 2026-06-23.
- **Exactly 5 earners at 0.199985 incentive each (UIDs 78/154/161/219/229); effective earners 5.0;
  owner UID 0 = 0.70 dividends / 0 incentive; 256 UIDs registered, 5 earning** —
  `btcli subnet metagraph --netuid 120` (see `raw_metagraph.txt`).
- **Mechanism: commit HuggingFace (model,revision); validators host inference; winner-take-all to
  champion until dethroned; challenger must win STRICTLY across all envs or be PERMANENTLY
  TERMINATED; sybil/decoy/copy/overfitting-proof; ~24h task-pool refresh** — repo README,
  github.com/AffineFoundation/affine-cortex.
- **Owner = const (Bittensor founder, @const_reborn); work = RL envs (program synthesis, reasoning,
  code)** — affine.io / subnet listings / project X posts.
- **TAO ≈ $235 (range $215–265)** — CoinMarketCap / Coinbase / CoinGecko, 2026-06-23.
- **Price trend: UNKNOWN** — taostats subnet-120 chart not machine-readable; obtain at
  taostats.io/subnets/120.
```
```

**Sources:**
- https://github.com/AffineFoundation/affine-cortex
- https://subnetalpha.ai/subnet/affine/
- https://simplytao.ai/blog/your-simple-guide-to-affine-sn120
- https://coinmarketcap.com/currencies/bittensor/
- https://www.coinbase.com/price/bittensor
- https://taostats.io/subnets/120
