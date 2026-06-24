# Subnet 9 (IOTA) — Mining EV Teardown

_Analysis date: 2026-06-23. Chain: finney. Analyst pass per SUBNET_EV_RESEARCH_PROMPT.MD._

IOTA = **Incentivised Orchestrated Training Architecture** by Macrocosmos. It is
distributed **pretraining** of an LLM: the model is split into layers
(pipeline-parallel) and miners each train a slice. This replaced the old SN9
"winner-take-all" full-model pretraining contest.

---

## PHASE 1 — Token economics (chain-verified)

Source: `btcli subnet list --network finney`, row netuid 9.

| Metric | Value | Source |
|---|---|---|
| TAO/USD | ~$225 (cluster: CoinGecko $218, CMC $225, Coinbase $234, Kraken $233) | WebSearch CoinGecko/CMC |
| Alpha price (Τ_in/α_in) | **0.0362 τ/ι** | subnet list |
| Market cap | τ 195.54k | subnet list |
| Emission (Τ) | 0.0045 τ/block | subnet list |
| **Net Inflow EMA (Τ)** | **+0.0130 τ** (POSITIVE) | subnet list |
| Pool reserves P(Τ_in, α_in) | τ 62.44k, 1.72m ι | subnet list |
| Stake (α_out) | 3.68m ι | subnet list |
| Supply | 5.40m ι / 21M | subnet list |
| Tempo (k/n) | 325/360 (~20 tempos/day) | subnet list |

**Miner pool $/day.** Metagraph `Emissions` are per-tempo; the two earning UIDs
take 148.0 α/tempo × ~20 tempos/day ≈ **2,960 α/day to miners** — which matches
the ~2,950 α/day protocol default and cross-checks against the Quasar reference
($6.4k/day at 0.0099 τ). So:

```
miner_pool_usd_per_day = 2,960 α × 0.0362 τ × $225 ≈ $24.1k/day
```

**Token-health verdict: GOOD (4/5).** IOTA sits in the top ~7 subnets by market
cap, alpha price 0.0362 τ is high-tier (3–4× most of the long tail), and **net
inflow is positive (+0.0130 τ)** — one of the healthiest inflows on the entire
chain (most subnets, incl. Quasar at −0.0040, are melting). Pool is reasonably
deep: liquidating ~107 τ/day of alpha against a 62.4k τ reserve is ~0.17% of
reserve/day → modest slippage. This is the opposite of the Quasar token picture.

---

## PHASE 2 — What is the work?

Source: `github.com/macrocosm-os/IOTA` README, arXiv 2507.17766, Macrocosmos docs.

- **Work type: model training (pretraining).** Pipeline-parallel distributed
  training of a **1.5B-param Llama-inspired model split into 3 layers**
  (bf16, ~2 GB footprint per shard). Each miner trains a layer slice; data
  streams through; the orchestrator triggers Butterfly All-Reduce weight merges.
- **Required hardware (low barrier):** "CUDA GPU with ≥16 GB VRAM (RTX 4090, for
  example)", single GPU sufficient (README). A "Training at Home" (TAH) mode
  even runs on modern Apple Silicon with 16–32 GB RAM. No 8×H100 rig needed —
  the whole point of IOTA vs. old SN9 is removing the full-model VRAM wall.
- **Min viable rig cost:** RTX 4090 on Vast/RunPod ≈ $0.30–0.45/hr →
  **~$8–12/day**. This is one of the cheapest entry rigs of any GPU subnet.
- **EDGE TEST:** Reward is "fixed compensation per processed activation /
  backward pass" → it is **commodity throughput on a small model**. There is no
  obvious structural edge for a newcomer beyond cheap reliable compute + running
  the (non-trivial) IOTA client correctly and staying in sync. Edge ≈ none /
  commodity, with a small edge for operational reliability.

---

## PHASE 3 — Incentive mechanism teardown (the traps)

Source: arXiv 2507.17766v1 (IOTA primer), docs.macrocosmos.ai.

- **Distribution shape:** Proportional to verified backward passes ("fixed
  compensation per processed activation"), NOT winner-take-all (deliberately
  removed). BUT it is a **pipeline-parallel synchronized system**: the
  orchestrator waits for a fraction of miners to hit B_min, then triggers a
  weight-merge; new miners must "wait until the next full synchronization period
  to start participating." → **synchronized-cohort element**.
- **Assignment gating: YES.** A central **orchestrator (run by Macrocosmos)
  assigns each miner a model layer** and triggers merges. You do not freely pick
  your work; the operator's orchestrator controls participation. → **assignment_gated**.
- **Rich-get-richer:** Some. Reliability/throughput compounds (stragglers
  contribute fewer batches → proportionally less), and validators "continuously
  measure each miner's contribution." CLASP outlier detection can demote
  suspected bad/malicious contributors.
- **Failure penalties:** Stragglers are not explicitly slashed but earn ~0;
  CLASP loss-attribution can flag and exclude outliers.
- **Weight-setting — RED FLAG:** The dominant validator is **Macrocosmos itself
  (UID 109, 35% of dividends)**, which is the **same entity as the subnet owner**
  (`Owner9`, UID 209) — and the owner's hotkey is simultaneously the **#1 miner
  earner (83% of incentive)**. One entity controls the orchestrator, the top
  validator (weight-setting), and the top miner payout. This is single-entity
  capture of all three sides.
- **Newcomer cold-start:** Mechanically open — register anytime, no whitelist,
  reg cost τ0.0005 (≈ free), join at next sync. Practically: only 2 UIDs of 257
  actually earn, so real cold-start success is unproven.

---

## PHASE 4 — Saturation / competition

Source: `btcli subnet metagraph --netuid 9` (257 UIDs), `btcli subnet show`.

**Incentive concentration (the headline):**

| UID | Identity | Incentive share | Emission (α/tempo) |
|---|---|---|---|
| 209 | **Owner9 (*Owner)** | **0.8300 (83%)** | 122.85 |
| 21 | ~ (anon) | 0.1700 (17%) | 25.16 |
| _all others (255)_ | — | 0.0000 | 0.000 |

- UIDs with incentive > 0: **2 of 257.**
- **Effective number of earners = 1 / Σ shareᵢ² = 1 / (0.83² + 0.17²) = 1.39.**
- Top validators (dividends): Macrocosmos 35%, TAO.com 31%, Yuma/DCG 10%,
  tao.bot 8%, Kraken, Crucible, Datura, Rizzo… — these are stake/validator
  players, not miners.

So by the raw metric this looks "wide open" (only ~1.4 earners against a $24k/day
pool) — but the openness is illusory: the single earning operator is the subnet
owner. Either (a) real distributed-miner participation is genuinely thin and the
owner runs nodes to keep training alive → a real gap a newcomer could fill, or
(b) credit structurally concentrates to the operator. The data cannot
distinguish these without a live test.

- **Registration cost (recycled): τ0.0005** (`btcli subnet show`) ≈ $0.0001.
  Non-refundable but negligible — registration is NOT the barrier.
- Public miner artifacts (S3 heartbeat bucket): not located in this pass —
  marked UNKNOWN; would be found in the IOTA repo (`grep -ri s3://`) or the
  iota.macrocosmos.ai dashboard to size incumbent rigs.

---

## PHASE 5 — EV synthesis

Assumptions: single RTX 4090 (≥16 GB), ~$12/day all-in compute+ops, reg
amortized ~$0. Pool $24.1k/day, alpha 0.0362 τ, TAO $225, net inflow positive so
price_trend ≈ flat-to-up; liquidation haircut ~0.55–0.70 (pool deep relative to a
small miner's daily sells).

The dominant unknown is **your_share**, because free entry + cheap 4090 + free
registration have NOT produced a crowd of earners — meaning the binding
constraint is the orchestrated/assignment-gated participation and possible
operator capture, not cost. Scenarios:

| Scenario | your_share | Gross/day | Realized (haircut) | Net/day | Net/month |
|---|---|---|---|---|---|
| LOW | ~0% (not credited / out-competed by operator) | $0 | $0 | −$12 | **−$360** |
| BASE | ~1% (some credited backward passes, small reliable rig) | $241 | ×0.6 ≈ $145 | $133 | **+$4.0k** |
| HIGH | ~5% (participation truly thin, you run reliable capable compute) | $1,206 | ×0.65 ≈ $784 | $772 | **+$23k** |

The spread is enormous and driven entirely by whether a fresh hotkey actually
gets credited. **Biggest single risk:** single-entity (Macrocosmos) control of
orchestrator + top validator + top miner payout — a newcomer may simply never
accrue meaningful incentive regardless of work done. **The one thing that would
most change the answer:** run a real IOTA miner on a fresh hotkey for ~1 week and
measure whether on-chain incentive accrues proportional to your backward passes.

**Verdict: WATCH.** Unlike Quasar (NO-GO: melting token, saturated, B200-class
barrier), IOTA has a healthy/positive-inflow token, a genuinely cheap entry rig,
and only ~1.4 effective earners against a $24k/day pool — a real potential gap.
But assignment-gated orchestration + owner/validator/miner capture by one entity
are serious red flags that block a confident GO. **Minimum edge to be +EV:**
ability to run the IOTA client reliably and sustain credited throughput against
an incumbent who controls the scoring — i.e. an operational/reliability edge plus
confirmation (via test) that fresh hotkeys are actually paid.

---

## SCORECARD

```
SCORECARD
netuid: 9
name: iota
work_type: training
alpha_price_tao: 0.0362
net_inflow_ema_tao: +0.0130
token_health: 4
miner_pool_usd_per_day: 24100
effective_num_earners: 1.39
saturation: 3
min_rig_cost_usd_per_day: 12
registration_cost_tao: 0.0005
mechanism_trap: assignment_gated
newcomer_friendliness: 3
edge_required: operational reliability running the IOTA orchestrated-training client + proof fresh hotkeys actually get credited; no commodity-compute edge by itself
ev_usd_per_month_low: -360
ev_usd_per_month_base: 4000
ev_usd_per_month_high: 23000
confidence: 2
recommendation: WATCH
composite_score: 15
one_line_thesis: Healthiest-token / cheapest-rig pretraining subnet with only ~1.4 effective earners against a $24k/day pool — but that single earner is the owner, who also runs the orchestrator and top validator, so the upside is real only if a fresh hotkey can actually get credited (untested).
```

### Key evidence behind each score
- **token_health 4** — alpha 0.0362 τ (top-tier price), **net inflow +0.0130 τ**
  (rare positive, vs Quasar −0.0040), top-7 market cap, deep pool
  (62.4k τ reserve). Source: `btcli subnet list`.
- **miner_pool $24.1k/day** — 2,960 α/day to miners (148 α/tempo × 20 tempos,
  matches ~2,950 default & Quasar cross-check) × 0.0362 τ × $225. Source:
  `btcli subnet metagraph` emissions.
- **effective_num_earners 1.39 / saturation 3** — only 2 of 257 UIDs have
  incentive>0 (Owner9 83%, anon 17%); 1/Σs² = 1.39. Few earners (looks open) but
  concentrated in the owner → score capped at 3. Source: metagraph.
- **min_rig $12/day** — README: "CUDA GPU ≥16 GB VRAM (RTX 4090)"; 1.5B/3-layer
  model; RTX 4090 rental ~$0.30–0.45/hr. Source: IOTA README, Vast/RunPod.
- **registration_cost τ0.0005** — `btcli subnet show --netuid 9`.
- **mechanism_trap assignment_gated** — orchestrator (Macrocosmos) assigns
  layers + triggers synchronized weight merges; new miners wait for next sync;
  CLASP can demote. Also synchronized_cohort + rich_get_richer present. Source:
  arXiv 2507.17766v1.
- **newcomer_friendliness 3** — no whitelist, free reg, join anytime
  (mechanically friendly) BUT only 2 UIDs ever earn and orchestrator gates real
  participation (practically unproven). Source: docs + metagraph.
- **confidence 2 / WATCH** — huge EV spread because credit-capture is the
  unknown; single-entity control of orchestrator+validator+top-miner is the
  dominant risk. Resolve by live-testing a fresh hotkey for a week.
```
```
