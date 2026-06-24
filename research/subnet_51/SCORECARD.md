# Subnet 51 — lium.io (Celium) — Mining EV Research

Date: 2026-06-23 · TAO/USD: $274.61 · Network: finney

## SCORECARD
```
SCORECARD
netuid: 51
name: lium.io
work_type: inference        # decentralized GPU compute/rental marketplace
alpha_price_tao: 0.0543
net_inflow_ema_tao: +0.0158
token_health: 4             # mid-tier price + POSITIVE inflow (rare) 
miner_pool_usd_per_day: 44100
effective_num_earners: 4.25
saturation: 2               # 29 earners but top-2 (whale + owner) ~88%
min_rig_cost_usd_per_day: 350
registration_cost_tao: 0.5277
mechanism_trap: stake_gated # collateral = rental_price/gpu/hr × n_gpus × 24
newcomer_friendliness: 3    # permissionless reg, demand-based fast cold-start, but collateral + datacenter-GPU barrier
edge_required: own in-demand datacenter GPUs (H200/B200) at below-market cost + high uptime + TAO collateral; commodity/consumer GPU = no edge
ev_usd_per_month_low: -10000
ev_usd_per_month_base: 1600
ev_usd_per_month_high: 17000
confidence: 3
recommendation: WATCH
composite_score: 15         # 4 + 2 + 3 + 3(WATCH) + 3
one_line_thesis: Rare healthy-token GPU-rental subnet with real demand and positive inflow, but the owner self-mines ~44% and one whale ~44%, leaving thin tail EV — only +EV if you already own in-demand datacenter GPUs cheaply.
```

## Evidence

### Phase 1 — Token economics (chain-verified)
- `btcli subnet list --network finney`, row 51:
  - alpha price (Τ_in/α_in) = **0.0543 τ** (mid-tier; cf. Chutes 0.0747, Targon 0.0524)
  - Market Cap = τ 282.48k
  - **Net Inflow EMA = +0.0158 τ (POSITIVE)** — rare; most subnets are melting (e.g. Targon −0.0046, SN24 −0.0040). Renters bringing TAO in to rent GPUs is the most likely driver.
  - Pool P (Τ_in, α_in) = **τ 118.14k / 2.18m α** → TAO-side depth ≈ $32.4M.
  - Supply 5.20m / 21M; Tempo 30–32 / 360 (≈20 tempos/day).
- **Miner pool**: sum of `Emissions` column for incentive>0 UIDs = 148.01 α/tempo × 20 = **~2,960 α/day** (confirms the ~2,950 heuristic; emission col is per-tempo).
  - = 2,960 × 0.0543 × $274.61 ≈ **$44,100/day** total across ALL miners.
- Token-health verdict: **4/5** — positive net inflow + healthy pool depth + mid-tier price. Strongest single positive vs the melting-token peers.

### Phase 2 — The work
- Repo: `github.com/Datura-ai/lium-io`; docs.lium.io. Lium (formerly Celium) = **decentralized peer-to-peer GPU rental marketplace**.
- Miners run **executor nodes** (Ubuntu + Docker, ≥50 Mbps, 100 GB disk, 8 GB RAM) attached to GPUs. Validators send synthetic/test jobs and score **GPU type, GPU count, bandwidth, uptime, speed, correctness**.
- **Demand-based bonus**: as renters rent more of a given GPU type, the algorithm raises the bonus for that type. → in-demand high-end GPUs (H200/B200) earn disproportionately.
- Hardware: datacenter-class GPUs. Min viable competitive rig ≈ 8× H100/H200. Cross-check rental: H100 ~$1.5–2/hr → 8-GPU rig ≈ **$300–400/day** (Vast/RunPod/Lambda).
- **Edge test**: reward is for commodity datacenter GPU → margin compresses toward GPU-rental economics. Only edge = owning in-demand GPUs below market + high uptime + capital to post collateral.

### Phase 3 — Incentive mechanism (traps)
- **Collateral gate (stake_gated)**: Required Collateral = (Rental Price/GPU/hr) × (n GPUs) × 24 — must lock ~1 day of rental value in TAO before earning. Real capital barrier.
- Distribution roughly **proportional** to scored GPU performance × count, modulated by demand.
- **Rich-get-richer-ish**: demand-based bonus favors GPU types/providers already serving rental demand.
- Permissionless registration (0.5277 τ recycle); not whitelisted. Demand-driven scoring means a fresh hotkey with good GPUs can earn within days.
- **Owner self-mining**: `Owner51` coldkey 5FqACM runs 5 hotkeys (UIDs 187–191) each at incentive 0.088136 → **44.1% of miner emissions captured by the subnet owner.**

### Phase 4 — Saturation / competition
- `btcli subnet metagraph --netuid 51`: **29 UIDs with incentive > 0**.
  - UID 47 (anon): **0.4407 share (44%)**.
  - Owner51 ×5: combined **0.4407 (44%)**.
  - → **top-2 entities ≈ 88%**; remaining ~12% across ~23 tail miners.
  - **Effective number of earners = 1/Σshareᵢ² = 4.25.**
- Registration cost (recycled): **0.5277 τ** ≈ $145 one-time (≈ $2.4/day amortized over 60d).

### Phase 5 — EV synthesis (per competitive 8×H100/H200 rig)
Assumptions: liquidation haircut 0.85 (deep pool, daily sell ≈0.14% of depth, positive inflow); GPU cost $300–400/day; ops $20–30/day; reg amortized $2.4/day.

| Case | Newcomer share | Gross $/day | Net $/day | Net $/month |
|------|---------------|-------------|-----------|-------------|
| LOW  | ~0.2% (tail)  | $88   | −$330 | **−$10,000** |
| BASE | ~1% (decent demand) | $441 | +$55 | **+$1,600** |
| HIGH | ~2.5% (in-demand GPUs, high uptime) | $1,100 | +$560 | **+$17,000** |

- **Biggest risk**: the owner structurally captures ~44% and a single whale another ~44% — the addressable pool for newcomers is only ~$5k/day across the entire tail, so marginal EV ≈ 0 unless your GPU type is in active rental demand.
- **What would most change the answer**: whether renters' rental payments flow to miners *separately from* alpha emissions (real cash yield). If yes, EV improves materially and this moves toward GO. Docs imply compensation is via TAO emissions; unconfirmed.
- **Verdict: WATCH.** GO only if you already own in-demand datacenter GPUs (H200/B200) at low/sunk cost and can post collateral; NO-GO if you'd rent commodity GPUs to enter (you'd do better renting them directly on Vast/RunPod).

## Sources
- btcli 9.20.0: `subnet list`, `subnet show --netuid 51`, `subnet metagraph --netuid 51` (finney) — raw metagraph saved at `research/subnet_51_raw_metagraph.txt`.
- TAO/USD $274.61 — CoinGecko/CoinMarketCap, mid-June 2026.
- github.com/Datura-ai/lium-io; docs.lium.io (overview, validator, executor, collateral).
```
```
