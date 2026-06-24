# Bittensor Subnet 107 — Minos: New-Miner EV Research

**Date:** 2026-06-23  ·  **Network:** finney  ·  **Analyst role:** mining-economics
**Subnet:** netuid 107 (Minos) — decentralized genomic variant-calling & benchmarking
**Owner coldkey:** `5DA2vLrSXZxnT9G4Yrywx1Fpi4RXwMH1Ah7r8DTTWS7UZZBM` (Minos)
**Repo:** https://github.com/minos-protocol/minos_subnet  ·  **API:** https://api.theminos.ai

> Bottom line up front: **WATCH**. Healthy token (positive net inflow, mid-high alpha
> price) and a genuinely non-commodity niche (genomics), but **87.5% of miner emissions
> are self-captured by the owner UID 0**, and the remaining 12.5% is a **winner-take-all
> per-round** contest already ~69%-dominated by one incumbent. +EV only for an operator
> with real variant-calling / hyperparameter-tuning expertise who can win rounds outright.

---

## PHASE 1 — Token economics (chain-verified)

Source: `btcli subnet list --network finney` (row 107), `btcli subnet show --netuid 107`.

| Metric | Value | Source |
|---|---|---|
| TAO/USD | ~$235 (range $225–263 across exchanges) | WebSearch / CoinGecko / CMC, 2026-06-23 |
| Alpha price (Τ_in/α_in) | **0.0383 τ/ミ** | subnet list |
| Market cap (α × price) | τ 47.90k | subnet list |
| Emission (Τ) share | τ 0.0106 | subnet list |
| **Net Inflow EMA (Τ)** | **+0.0012** (POSITIVE) | subnet list |
| Pool reserves P (Τ_in, α_in) | τ 9.36k, 243.98k ミ | subnet list |
| Stake (α_out) | 1.01m ミ | subnet list |
| Supply / max | 1.25m ミ / 21M (~6% emitted → young) | subnet list |
| Tempo | 360 blocks | subnet show |
| Registration cost (recycled) | **τ 0.15** (~$35, one-time) | subnet show |

**Token-health verdict: 4/5.** Alpha price 0.0383 τ is *mid-to-high* vs peers
(calibration: SN24 Quasar 0.0099, Cacheon 0.0107, Poker44 0.0071 — Minos is ~4× those).
Net inflow is **positive** (+0.0012) — token is *accreting*, not melting. This is the
single most attractive fact about SN107. Recent multi-week price trend: **UNKNOWN**
(taostats chart not machine-readable; would confirm via taostats.io/subnets/107). Young
subnet (~6% of supply emitted), so price history is short.

### Miner pool $/day — and the 87.5% owner trap
Standard alpha emission ≈ 7,200 α/day per subnet; miner slice ≈ 41% ≈ **~2,950 α/day**
(default M_alpha; not separately verifiable per-subnet, flagged as assumption).

- **Gross miner pool** = 2,950 × 0.0383 × $235 ≈ **$26.5k/day** — but this is misleading.
- On-chain incentive shows **UID 0 (Minos *Owner*) = 0.8749 incentive** → the owner
  self-mines **87.5%** of the miner slice (≈ 2,581 α/day ≈ $23k/day to itself).
- **Contestable third-party pool = 12.5% ≈ ~369 α/day ≈ $3.3k/day** shared by all
  non-owner miners. **This is the real number a newcomer competes for.**

---

## PHASE 2 — What is the work?

**Work type: CPU bioinformatics (genomic variant calling).** *Not* GPU inference.

Miners download a synthetic BAM (genome alignment with injected/hidden mutations served
via short-lived presigned URLs over Cloudflare R2 / AWS S3 / Hippius SN75), then run a
**variant caller (GATK / DeepVariant / bcftools)** and submit the **tool configuration /
hyperparameters** they used. Validators re-execute the config, run the output VCF through
**hap.py against truth data**, and score accuracy 0–100 (normalized 0–1, "AdvancedScorer").

**Required hardware (miner):** 4+ CPU cores, 8–16 GB RAM (DeepVariant prefers 16 GB),
60 GB disk. **No GPU required** (GPU/TPU optional accel only). Dockerized tools.

**Min viable rig cost:** a 4-core / 16 GB / 60 GB CPU box on Vast/RunPod ≈ **$0.10–0.30/hr
≈ $3–7/day** (use **$5/day** base). Compute cost is *negligible* here — unusual and good.

**EDGE TEST — PASS (conditional).** Reward is **not** for commodity GPU-hours; it is for
**variant-calling accuracy** = skill at hyperparameter search / pipeline tuning over
GATK/DeepVariant/bcftools. A genomics- or bioinformatics-literate operator *can* hold a
real, durable edge here. A commodity operator running default DeepVariant has **no edge**
and compresses to ~0 (see Phase 3 — winner-take-all per round).

---

## PHASE 3 — Incentive mechanism teardown (the traps)

Source: repo README / scoring docs (github.com/minos-protocol/minos_subnet).

- **Distribution shape — winner-take-all *per round*.** Each ~72-min round (tempo-aligned,
  ~20 rounds/day): validators **burn 87% of weight** (→ owner UID 0), give the **top
  eligible miner 10%**, and split the remaining **3% as "ranked pruning dust" across ranks
  #2–#10** with 0.8 geometric decay. Per-round math: #2 ≈ 0.69%, #3 ≈ 0.55%, … #10 ≈ 0.14%.
  → **Only the #1 miner each round earns real money.** Ranks 2–10 are rounding error.
- **Lag scoring:** miners submit in cycle N; validators score cycle N while miners work N+1.
- **Eligibility gate:** must score in **≥10 of the last 20 rounds (including current)** or
  receive **0 weight**. ≈ 10–12 hours of valid continuous submissions to qualify.
- **Cold-start:** new hotkey earns **0 until it clears the 10-of-20 gate** — then can earn,
  but only meaningfully if it wins rounds. No whitelist, no stake-gate, no orchestrator
  *choosing* who works (open assignment) — so *qualifying* is fast; *earning* is hard.
- **Penalties:** soft — invalid/zero submissions simply don't score (no negative subtract),
  but they cost you the participation count toward the 10-of-20 gate.
- **Weight-setting / capture:** the dominant on-chain fact is the **87.5% self-allocation
  to owner UID 0**. Among third-party miners, incentive is EMA'd across rounds, so the
  steady #1 (UID 22) accumulates ~69% of the contestable pool → **rich-get-richer** in
  effect (whoever holds the best config wins most rounds).

**Mechanism trap (loud): `winner_take_all` (per round) + owner self-capture (87.5%).**
Secondary: `rich_get_richer` via EMA. These are major red flags.

---

## PHASE 4 — Saturation / competition

Source: `btcli subnet metagraph --netuid 107` (saved as `raw_metagraph.txt`).

- **UIDs with incentive > 0: 20** (incl. owner UID 0).
- Incentive shares sum to 1.000. **Owner UID 0 = 0.8749.**
- **Third-party miner pool (excl. UID 0) sums to 0.125.** Within it:
  - **UID 22 = 0.0863 → 69% of the contestable pool** (the entrenched incumbent).
  - Top-2 (UID 22 + UID 62) = **75.8%**.
  - **Effective number of earners = 1/Σshareᵢ² = 2.05** among third parties.
  - The other ~17 "earning" miners split ~25% — i.e. dust (most < 0.5% each).
- Named stakers present (Yuma/DCG, Kraken, TAO.com, Crucible Labs, OTF, Rizzo, 1T1B.AI)
  but these hold **dividends, incentive = 0** → they are *validators/stakers, not miners*.
- **No public miner heartbeat S3 bucket / capability dashboard** found in the repo (all
  data flows through the hosted `api.theminos.ai` via presigned URLs), so incumbent rig
  specs can't be fingerprinted — but hardware is cheap CPU regardless; the moat is the
  **config quality**, not the rig.
- **Registration cost:** τ 0.15 (~$35) one-time, non-refundable (recycled).

**Saturation: 3/5.** Few third-party earners (≈2 effective) *looks* open, but one incumbent
already holds 69% and the owner skims 87.5% off the top, so true headroom is moderate, not
wide-open.

---

## PHASE 5 — EV synthesis

**Assumptions:** TAO = $235; alpha = 0.0383 τ; contestable third-party pool ≈ 369 α/day
(~$3.3k/day); rig $5/day; registration τ0.15 amortized over 60 days ≈ $0.59/day; ops ~$1.5/day
→ **costs ≈ $7/day**. Realized-price factor = liquidation haircut × trend ≈ **0.85** (pool is
deep relative to a newcomer's tiny daily sell of a few α into 244k α reserve → slippage
negligible; positive net inflow supports price; trend unconfirmed so modest discount applied).

Newcomer outcomes are **bimodal** because the contest is winner-take-all per round:

| Scenario | Round-win behavior | Share of contestable pool | Gross $/day | **Net EV/day** | **Net EV/month** |
|---|---|---|---|---|---|
| **LOW** | Qualifies, rarely wins; mostly dust ranks #5–10 | ~1.5% | ~$50 | **~$35** | **~$1,000** |
| **BASE** | Competent config, wins ~5–10% of rounds + steady dust | ~7% | ~$232 | **~$190** | **~$5,500** |
| **HIGH** | Genomics specialist, out-tunes incumbent, wins ~20–30% of rounds | ~20% | ~$664 | **~$560** | **~$16,500** |

> Honest caveat: the **realistic mode for a commodity newcomer is LOW or below** (possibly
> ~$0 if it can't out-rank the ~19 existing miners for dust slots). BASE and HIGH **require a
> genuine variant-calling edge** to win rounds against the incumbent. HIGH is also reflexive:
> visibly winning invites copycats and the owner can retune scoring.

- **Single biggest risk:** the **87.5% owner self-capture** structurally caps the entire
  third-party opportunity at 1/8 of the subsidy — and the owner can change this at will.
- **Single thing that would most change the answer:** whether *you* possess a variant-calling
  config edge that wins rounds. With it → conditional GO; without it → NO-GO.
- **Minimum edge to be +EV:** ability to consistently land **top-1 (or reliably top-3)** in
  hap.py accuracy via superior GATK/DeepVariant/bcftools hyperparameter search. Commodity
  default pipelines → not +EV.

**Recommendation: WATCH** (conditional GO for a genomics specialist; NO-GO for commodity).

---

## SCORECARD
```
SCORECARD
netuid: 107
name: Minos
work_type: other            # CPU bioinformatics / genomic variant calling
alpha_price_tao: 0.0383
net_inflow_ema_tao: +0.0012
token_health: 4             # mid-high price + positive inflow; trend unconfirmed
miner_pool_usd_per_day: 3300   # CONTESTABLE third-party pool; gross ~$26.5k but 87.5% self-captured by owner UID0
effective_num_earners: 2.05    # among third-party miners (1/Σshare²); owner excluded
saturation: 3
min_rig_cost_usd_per_day: 5
registration_cost_tao: 0.15
mechanism_trap: winner_take_all   # per-round; + owner 87.5% self-capture + rich_get_richer (EMA)
newcomer_friendliness: 3       # fast qualify, no stake/whitelist gate, but winner-take-all earning
edge_required: genomics / variant-calling expertise — out-tune GATK/DeepVariant/bcftools to win rounds; commodity default pipelines = not +EV
ev_usd_per_month_low: 1000
ev_usd_per_month_base: 5500
ev_usd_per_month_high: 16500
confidence: 3
recommendation: WATCH
composite_score: 16            # token_health 4 + saturation 3 + newcomer_friendliness 3 + WATCH 3 + confidence 3
one_line_thesis: Healthy-token genomics niche with few earners, but 87.5% of emissions self-captured by the owner and a winner-take-all-per-round contest mean only a real variant-calling specialist who can win rounds is +EV.
```

### Key evidence (with sources)
- **alpha 0.0383 τ, net inflow +0.0012, mcap τ47.9k, reg τ0.15** — `btcli subnet list` /
  `subnet show --netuid 107` (finney), 2026-06-23.
- **Owner UID 0 incentive 0.8749 (87.5%)**; third-party pool 0.125; **UID 22 = 0.0863 (69%
  of contestable); effective earners 2.05** — `btcli subnet metagraph --netuid 107`
  (see `raw_metagraph.txt`).
- **Work = genomic variant calling; submit GATK/DeepVariant/bcftools config; scored via
  hap.py vs truth; 4-core/16GB/60GB CPU, no GPU** — repo README, github.com/minos-protocol/minos_subnet.
- **Mechanism: burn 87% → owner, 10% → top miner, 3% dust ranks #2–10 (0.8 geometric);
  eligibility = 10 of last 20 rounds; cold-start 0 until qualified** — repo scoring docs.
- **TAO ≈ $235 (225–263)** — CoinGecko / CoinMarketCap / Coinbase, 2026-06-23.
- **Price trend: UNKNOWN** — taostats subnet-107 chart not machine-readable; obtain at
  taostats.io/subnets/107.
```
```

**Sources:**
- https://github.com/minos-protocol/minos_subnet
- https://www.coingecko.com/en/coins/bittensor
- https://coinmarketcap.com/currencies/bittensor/
- https://taostats.io/subnets/107
