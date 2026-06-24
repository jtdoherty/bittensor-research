# Subnet 24 — Quasar (SILX Labs) — Mining EV Research [BASELINE]

_Analysis date: 2026-06-23 • Network: finney • Mechanism 0 • TAO ≈ $250 (range $218–$275 across sources)_

> This is the **calibration baseline** for the whole research effort — the first
> subnet torn down end-to-end and the reference NO-GO. Methodology in
> `../SUBNET_EV_RESEARCH_PROMPT.md` was derived from this analysis.

## SCORECARD (machine-rankable)
```
SCORECARD
netuid: 24
name: Quasar
work_type: training              # decentralized continued-PRETRAINING of an 18B/2B MoE
alpha_price_tao: 0.0099
net_inflow_ema_tao: -0.0040
token_health: 1                  # bottom-third price + NEGATIVE inflow (melting) + ~24% drawdown in days
miner_pool_usd_per_day: 7300     # 2960 alpha/day x 0.0099 tao x $250
effective_num_earners: 2.03      # 1/Sum(share^2); 2 miners = 99.1% of incentive
saturation: 1                    # ~37 registered rigs (many 8xH100/8xB200) but only 2 earn
min_rig_cost_usd_per_day: 45     # 1x H100 to test; realistically need 8xH100/B200 to compete (~$350+/day)
registration_cost_tao: 0.0444    # recycled, trivial (~$10) — barrier is NOT registration
mechanism_trap: synchronized_cohort   # + rich_get_richer + assignment_gated (triple-locked)
newcomer_friendliness: 1         # cold-start starts dead-last in rank; must hold pace in live cohort
edge_required: match incumbent 8xGPU scale AND stay synchronized in the live training cohort from a cold start while absorbing double-weighted failure penalties — effectively none for a newcomer
ev_usd_per_month_low: -1400      # rent 1x H100, never enter winning set, earn ~0
ev_usd_per_month_base: -1400     # same; the realistic case
ev_usd_per_month_high: 0         # best plausible newcomer outcome ≈ break-even after large capital
confidence: 5
recommendation: NO-GO
composite_score: 9               # token_health 1 + saturation 1 + newcomer_friendliness 1 + (NO-GO=1) + confidence 5
one_line_thesis: A melting-token (−inflow), saturated, triple-locked subnet — reward = tokens²/steps inside a synchronized DiLoCo cohort where 2 miners (2xB200 + 8xGPU class) take 99% and ~35 capable rigs earn ~0; a newcomer is structurally locked out, so EV is negative.
```

## Key evidence (with sources)

### Phase 1 — Token economics (`btcli subnet list --network finney`, row 24)
- alpha price **0.0099 τ/α** (bottom third; cf. Chutes 0.0747, lium 0.0543, Minos 0.0383, iota 0.0362).
- **Net Inflow EMA = −0.0040 τ (NEGATIVE / melting)** — capital leaving; the opposite of iota/lium/Chutes which are positive.
- Market Cap τ ~52k; Pool P = τ 13.16k / 1.34m α; Supply 5.26m / 21M; Tempo 87/360 (~20 tempos/day).
- **Miner pool**: incentive-bearing Emissions ≈ 148 α/tempo × 20 = **~2,960 α/day** (matches heuristic) → 2,960 × 0.0099 × $250 ≈ **$7,300/day total across ALL miners**.
- Alpha fell ~24% in the days before analysis. Token-health verdict: **1/5** — the weakest dimension; you'd be paid in a depreciating, thin token.

### Phase 2 — What is the work? (`silx-ai/Quasar-Preview` HF card; `SILX-LABS/QUASAR-SUBNET` repo)
- **Decentralized continued PRETRAINING** of `Quasar-Preview`: an **original from-scratch foundation model** (NOT a fine-tune of GLM/Qwen/Llama). ~**18B total / ~2B active**, MoE 256 experts/8-per-tok, hybrid Quasar+Raven+GLA (linear/gated-slot attention via flash-linear-attention), GQA, long-context to 5M tok. ~1–1.5T tokens trained; goal 10T+. MIT.
- Hardware: real multi-GPU datacenter training. `required_gpus` is enforced per job; a 6 GB consumer card is skipped outright. Competitive = 8×H100/B200.
- **EDGE TEST → commodity GPU + sync ability.** No proprietary edge; you compete on raw synchronized throughput.

### Phase 3 — Incentive mechanism (the traps — TRIPLE-LOCKED)
- **Reward weight = `tokens²/steps`** (`incentive/fragments/artifacts.py:453`) = quadratic in per-step throughput. 2× batch ≈ 4× reward for the same assigned tokens.
- **Synchronized DiLoCo-style cohort** (`orchestrator/run_manager.py:1802+`): `fragment_id = global_step % 24`; at each step all learners with positive weight on that fragment + meeting QUORUM are merged. **Fall behind the global step → stale fragment → excluded → earn 0.**
- **Rich-get-richer assignment rank** (`orchestrator/scheduler.py:134`): `trust × (1 + log1p(accepted_units)) × gpu_count / (1 + inflight)`. Fresh hotkey = `accepted_units 0` = bottom of the list.
- **Double-weighted failure penalty** (`scheduler.py:33`): `(accepted − 2×failed)/checked` — early instability demotes future assignment.
- **Registration-gated** (`require_registered_miners=True` default) and **quality gate**: validator applies your fragment and checks heldout-loss regression ≤ 0.02, gen-gap ≤ 0.10 (`validator/generalization.py`); failing = 0 and a penalty.
- Weight-setting effectively captured by the owner/orchestrator validator (UID with dividends ≈ 0.97).

### Phase 4 — Saturation / competition (the killer)
- `btcli subnet show --netuid 24`: incentive **UID43 = 0.524, UID48 = 0.467 → 99.1% in two miners**; ~5 others share <1%. **Effective earners = 1/Σshare² ≈ 2.0.**
- Public S3 bucket `quasar-incentive-sn24-529337356998-us-east-1` exposes miner **heartbeats anonymously** (worker IDs + capability JSON encode GPUs). Confirmed field of **~37 registered rigs**: ≥5× **8×H100 (648 GB)**, one **8×B200**, two **4×B200**, plus H200/4×H100/A100; #2 earner runs **2×B200 (363 GB)**. → **~35 capable rigs earn ~0** = equilibrium evidence that newcomer EV ≤ 0.
- Registration (recycled): **τ0.0444 ≈ $10** — trivial; the barrier is the sync/throughput lockout, not entry cost.

### Phase 5 — EV synthesis
- Realistic newcomer (rent 1× H100 ~$45/day): `P(in winning set) ≈ 0` → cannot hold cohort pace vs 8×B200 → your_share ≈ 0. Net ≈ **−$45/day ≈ −$1,400/mo**, ~0 upside.
- Even at 8×GPU scale you buy into a saturated contest paid in a melting token, against entrenched + rich-get-richer incumbents.
- **Biggest risk / decisive variable:** the synchronized-cohort + assignment lock — whether a fresh hotkey ever lands in `…/fragments/<run>/live_sync/.../accepted_updates.json`. Empirically, ~35 don't.
- **Verdict: NO-GO.** Fails 3 of 4 hunting criteria (melting token, saturated, mechanism trap). Only "low barrier to *enter*" passes — which is irrelevant when you can't earn.

## Sources
- `btcli 9.20.0`: `subnet list`, `subnet show --netuid 24` (finney).
- Repo `github.com/SILX-LABS/QUASAR-SUBNET`: `incentive/fragments/artifacts.py`, `orchestrator/{scheduler,run_manager}.py`, `validator/{scoring,rewards,generalization,quasar_update_eval}.py`.
- `huggingface.co/silx-ai/Quasar-Preview` (model card).
- Public bucket `quasar-incentive-sn24-529337356998-us-east-1` (anonymous heartbeat listing).
