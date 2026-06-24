# Bittensor Subnet 97 — Albedo: New-Miner EV Research

**Date:** 2026-06-23 · **Network:** finney · **Mechanism 0** · **Analyst role:** mining-economics
**Subnet:** netuid 97 (Albedo) — *Distil*: competitive LLM **distillation** contest
**Owner coldkey:** `5EUXD91ADceyH7nRWXCqG1wbaCEhsqosT4rjGhwaZDRR4ib6` (UID 0, dividends 0.998)
**Repo:** https://github.com/unarbos/distil · **TAO ≈ $235** (range $218–263 across sources)

> **Bottom line up front: WATCH (conditional).** This is **not** a commodity-GPU farm — it is a
> **winner-take-all model-distillation research contest**. The reward is binary: become the on-chain
> "king" (highest composite score, must beat the incumbent by **+5%**) and take ~100% of miner
> emissions, or earn **zero**. Median newcomer EV is **negative** (you pay registration + training
> compute and earn nothing). It is only +EV for a team with a **genuine SOTA distillation edge**.
> Two saving graces: (1) the field is currently **not** dominated by an entrenched king (5 miners
> sit tied at the floor → the crown looks contestable right now), and (2) entry is open (no stake/
> whitelist gating). Two red flags: token net inflow is **slightly negative** (flat/melting), and
> each hotkey gets **ONE permanent commitment** — a weak model wastes the ~$224 registration.

---

## PHASE 1 — Token economics (chain-verified)

Source: `btcli subnet list --network finney` (row 97), `btcli subnet show --netuid 97`.

| Metric | Value | Source |
|---|---|---|
| TAO/USD | ~$235 (range $218–263) | CoinGecko / Coinbase / CMC, 2026-06-23 |
| Alpha price (Τ_in/α_in) | **0.0271 τ/α** | subnet list |
| Market cap (α × price) | τ 24.15k (~$5.7M) | subnet list |
| Emission (Τ) share | τ 0.0140 | subnet list |
| **Net Inflow EMA (Τ)** | **−0.0002** (slightly NEGATIVE) | subnet list / show |
| Pool reserves P (Τ_in, α_in) | τ 7.10k, 262.40k α | subnet list |
| Stake (α_out) | 630.37k α | subnet list |
| Supply / max | 892.77k α / 21M (~4.2% emitted → **young**) | subnet list |
| Tempo | 189/360 blocks | subnet show |
| Registration cost (recycled) | **τ 0.9513 (~$224)** one-time, non-refundable | subnet show |

**Token-health verdict: 3/5.** Alpha price **0.0271 τ is mid-tier** — ~2.7× Quasar (0.0099), below
Chutes (0.0747) / lium (0.0542) / Minos (0.0383). Net inflow is **−0.0002** — essentially flat,
marginally melting (not accreting). Pool is **thin** (τ7.10k reserve / 262k α), so any sustained
sell pressure moves price. Young subnet (4.2% of supply emitted) → short price history. Decent price
but no inflow tailwind = 3.

### Miner pool $/day
- Total emission = **296.02 α/tempo** (chain footer); validator/owner side (UID 0) takes **147.86 α**,
  miner side = **148.02 α/tempo**.
- Tempo 360 blocks @ ~12s → ~20 tempos/day → **miner pool ≈ 2,960 α/day** (matches the ~2,950 heuristic).
- **Miner pool $/day = 2,960 × 0.0271 τ × $235 ≈ $18,850/day** — but see Phase 3: under winner-take-all
  this entire pool funnels to **one** king, not split.

---

## PHASE 2 — What is the work? (repo: `unarbos/distil`)

**Work type: model training / distillation (an ML research contest, NOT GPU-hours-for-tokens).**

- Miners **distill a 1T-param MoE teacher (Kimi-K2.6)** into a **≤33B Kimi-family student** and commit
  the HuggingFace model hash on-chain. Forward-KL distribution matching + reasoning-quality axes.
- Output is a **single artifact** (a model), scored once. This is closer to a Kaggle-style ML
  competition than to continuous mining.
- **Hardware (miners):** *"33B-class students typically need 4–8× H100/H200 for full-precision (bf16)
  training"*; LoRA + gradient checkpointing fits smaller rigs; 2×24GB only viable for sub-2B toys.
  Validators run 8×H200/H100. Cross-check rental: 8×H100 ≈ **$300–400/day** during a training burst
  (Vast/RunPod ~$1.5–2.5/H100-hr); a LoRA attempt can be **<$50/day**.
- **EDGE TEST → this rewards a NON-commodity edge.** Raw GPU farming does nothing; you win on the
  **quality of your distillation recipe** across 25+ math/code/reasoning/fidelity axes. A team with
  real distillation/ML-research skill *can* have a structural edge; a generic miner cannot.

---

## PHASE 3 — Incentive mechanism teardown (the traps)

Source: `unarbos/distil` README.

- **Distribution shape: WINNER-TAKE-ALL king-of-the-hill.** *"The king is whoever has the highest
  `composite.final`. Winner-take-all — best miner gets 100% of emissions on chain."* Non-king miners
  earn **zero** regardless of absolute quality. Composite = `0.75 × worst_3_mean + 0.25 × weighted`
  across 25+ procedurally-seeded axes (math, code, IFEval, logic, long-context, distillation fidelity,
  judge/coherence). Procedural items are block-hash-seeded so static-benchmark overfitting fails.
- **Rich-get-richer / incumbent moat:** challenger must beat the king by **+5%** (`challenger.final >
  incumbent.final × 1.05`) to dethrone. The king is **re-evaluated every round** on the same items
  (paired fairness), entrenching a strong incumbent.
- **One permanent commitment per hotkey:** *"commitments are permanent and cannot be changed."* A weak/
  buggy model = dead hotkey; you must re-register a new hotkey (another ~$224) to retry.
- **Failure penalties:** COPY (SHA256 dup / activation-fingerprint cosine ≥0.99999), REMOVED (model
  pulled from HF), or INVALID architecture → `composite.worst = 0`, $0, disqualified.
- **Assignment gating:** none beyond wallet registration — **no stake gate, no whitelist**. New
  commitments enter FIFO, capped at **10 challengers/round** + reference baseline.
- **Cold-start:** a fresh hotkey *can* win in one round if its model is top — but it's all-or-nothing.

> ⚠️ **Docs-vs-chain discrepancy (flag loudly):** the README describes strict winner-take-all (king gets
> 100%), yet the **live metagraph shows 5 miners each earning an identical 0.199985 incentive** (see
> Phase 4) — i.e. *no* single king dominates right now; the field sits tied at a saturated floor.
> Interpretation: the crown is currently **contestable** (good for a strong entrant), but the mechanism
> a newcomer must plan for is winner-take-all. Treat the 5-way split as a transient floor state, not
> the steady state.

---

## PHASE 4 — Saturation / competition (chain-verified)

Source: `btcli subnet show --netuid 97` (256 UIDs, full).

- **Registered:** 256/256 UIDs (subnet is full). **Earning (incentive > 0): exactly 5 UIDs.**
  | UID | Incentive | Emission (α/tempo) | Coldkey |
  |---|---|---|---|
  | 17 | 0.199985 | 29.60 | 5DU34L… |
  | 24 | 0.199985 | 29.60 | 5Gzxrj… |
  | 19 | 0.199985 | 29.60 | 5GgPHh… |
  | 11 | 0.199985 | 29.60 | 5DPmaA… |
  | 231 | 0.199985 | 29.60 | 5CeuMh… |
- **Perfectly equal split** (5 × 0.2 = 1.0). **Effective number of earners = 1/Σ shareᵢ² = 1/(5×0.2²)
  = 5.0.** Top-2 share = 0.40. This is *un*concentrated for a WTA subnet → consistent with "no
  entrenched king yet."
- **251 of 256 registered hotkeys earn ZERO.** Most hold dust stake; one coldkey (`5GWYvS…`) farms
  ~10 idle UIDs. UID 0 (owner) takes the validator/dividend side (0.998 dividends, 147.86 α/tempo).
- Validator weight-setting is **owner-captured** (UID 0 dividends ≈ 0.998) — standard, but means the
  owner's validator defines the scoring that decides the king.
- **Registration (recycled): τ0.9513 ≈ $224** — *not* trivial. Combined with one-shot permanent
  commitment, a failed attempt costs ~$224 + the training compute.

---

## PHASE 5 — EV synthesis

**Assumptions:** newcomer rents 4–8× H100 for a training burst (~$300/day for ~3–7 days = $900–2,100
per serious attempt) OR a LoRA attempt (~$50/day). One permanent commitment per ~$224 hotkey.
Liquidation haircut is **heavy**: the α-pool is only 262k α / τ7.10k and net inflow is negative, so a
king dumping ~2,960 α/day (≈1.1% of pool/day) realizes well below spot — assume **25–40% realized**.

| Scenario | your_share | Outcome | EV/month |
|---|---|---|---|
| **LOW** | 0 (never king) | mediocre model, earn 0, lose reg + 1 training run | **−$1,500 to −$2,500** |
| **BASE** | 0 (median) | competent-but-not-best model; WTA pays $0; a couple retries | **≈ −$1,000** |
| **HIGH** | ~1.0 for part of month | win the crown, hold it through dethrone attempts, dump α into thin/melting pool at ~25–40% realized | **+$30,000 to +$60,000** (highly variable, contingent) |

- **Spot ceiling if you hold the crown all month:** 2,960 α/day × 0.0271 × $235 ≈ $18,850/day spot ≈
  $565k/mo — but the thin, slightly-melting pool means you cannot realize that without crashing α;
  realistic realized ≈ 25–40%, and you will not hold the crown uncontested for a full month. Hence the
  $30–60k HIGH band, with wide error bars.
- **Single biggest risk:** **winner-take-all + heavy liquidation haircut.** Even a strong model that
  isn't *the* best earns exactly $0; and even the king can't cash out a thin/melting token at spot.
- **What would most change the answer:** whether you (a) actually have a top-tier distillation recipe
  and (b) the crown stays contestable (no entrenched king with a high composite). If a dominant king
  establishes and the +5% margin locks it in, this becomes a clear NO-GO.

**Verdict: WATCH** — conditional **GO only for an ML team with a genuine distillation edge** entering
*now* while the crown is unclaimed; **NO-GO for commodity miners**. Minimum edge required: a ≤33B
Kimi-architecture student that beats the field's `composite.final` by **>5%** across 25+ math/code/
reasoning/fidelity axes. Compute alone is worthless here.

---

## SCORECARD (machine-rankable)
```
SCORECARD
netuid: 97
name: Albedo
work_type: training              # competitive LLM distillation (Kimi-K2.6 teacher -> <=33B student)
alpha_price_tao: 0.0271
net_inflow_ema_tao: -0.0002
token_health: 3                  # mid-tier price, but flat/slightly-melting inflow + thin pool + young
miner_pool_usd_per_day: 18850    # 2960 alpha/day x 0.0271 tao x $235 (funnels to ONE king under WTA)
effective_num_earners: 5.0       # 5 UIDs tied at 0.199985 each; 251/256 earn 0 (no entrenched king yet)
saturation: 3                    # few earners + crown currently contestable, but WTA caps it at 1 winner
min_rig_cost_usd_per_day: 300    # 4-8x H100 for a bf16 training burst; LoRA path ~$50/day
registration_cost_tao: 0.9513    # ~$224, one-time, NON-refundable; one permanent commit per hotkey
mechanism_trap: winner_take_all  # + rich_get_richer (+5% dethrone margin, king re-eval'd every round)
newcomer_friendliness: 2         # open entry/no gating, but binary WTA + permanent one-shot commit
edge_required: a top-tier model-distillation recipe producing a <=33B Kimi-arch student that beats the field's composite by >5% across 25+ reasoning/code/math/fidelity axes; commodity GPU has zero edge
ev_usd_per_month_low: -2000
ev_usd_per_month_base: -1000
ev_usd_per_month_high: 45000     # contingent on winning the crown AND dumping a thin/melting token
confidence: 3                    # solid chain data; docs(WTA) vs chain(5 equal) divergence + haircut uncertainty
recommendation: WATCH
composite_score: 14              # token_health 3 + saturation 3 + newcomer_friendliness 2 + (WATCH=3) + confidence 3
one_line_thesis: A winner-take-all distillation research contest where one "king" takes ~100% of a ~$18.8k/day miner pool and everyone else earns zero; the crown is currently unclaimed (5 miners tied at floor) so a team with a genuine SOTA distillation edge could win big, but a melting thin token, a +5% incumbent moat, and a $224 one-shot permanent commitment make median newcomer EV negative.
```

## Key evidence (with sources)
- **Phase 1 — token (`btcli subnet list`/`show` row 97):** α 0.0271 τ; net inflow **−0.0002**; pool
  τ7.10k/262.40k α; supply 892.77k/21M (~4.2% emitted); reg cost **τ0.9513**; tempo 189/360. Miner
  pool ≈ 2,960 α/day → ~$18.8k/day spot.
- **Phase 2 — work (`unarbos/distil` README):** distill Kimi-K2.6 (1T MoE) → ≤33B Kimi-arch student;
  4–8× H100/H200 for bf16 training; rewards distillation skill, not commodity compute.
- **Phase 3 — mechanism (README):** *"Winner-take-all — best miner gets 100% of emissions on chain"*;
  +5% dethrone margin; king re-evaluated every round; one permanent commitment per hotkey; DQ on
  COPY/REMOVED/INVALID; block-hash-seeded procedural axes; FIFO 10 challengers/round.
- **Phase 4 — saturation (`btcli subnet show --netuid 97`, 256 UIDs):** exactly **5 earners**, each
  0.199985 incentive (29.60 α/tempo); effective earners = **5.0**; 251/256 earn 0; owner UID 0 captures
  validator side (0.998 dividends). Docs say WTA but chain shows 5-way tie → crown currently contestable.
- **Phase 5 — EV:** WTA + thin/melting pool ⇒ LOW/BASE negative (−$1–2.5k/mo), HIGH +$30–60k/mo only
  if you win and can realize the token. **WATCH** (GO only with a real distillation edge).
```
Raw chain dump saved alongside this file as raw_subnet_show.txt.
```
