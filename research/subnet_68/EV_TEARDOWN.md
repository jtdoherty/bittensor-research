# Subnet 68 (NOVA) — Mining EV Teardown

_Analysis date: 2026-06-23. Chain: finney. Analyst pass per SUBNET_EV_RESEARCH_PROMPT.MD._

NOVA (by **Metanova Labs**) is decentralized **AI drug discovery**. Each ~1-hour
epoch the subnet fixes a **protein target**; miners search a ~1.75B-compound
synthesizable chemical library (SAVI 2020) for a small molecule that maximizes
predicted **binding affinity**, scored deterministically by the **PSICHIC** GNN
oracle that every validator runs. Submissions are timelock-encrypted
(Bittensor Drand / "BTDr" commit-reveal) so validators can't see candidates
before the deadline. Best molecule for the target wins the epoch. It is a
pure optimization race graded by a fixed oracle — **winner-take-all per epoch.**

---

## PHASE 1 — Token economics (chain-verified)

Source: `btcli subnet list --network finney`, row netuid 68.

| Metric | Value | Source |
|---|---|---|
| TAO/USD | ~$225 (cluster: CMC $225, CoinGecko ~$218, higher on some venues $250–264) | WebSearch CMC/CoinGecko |
| Alpha price (Τ_in/α_in) | **0.0220 τ/ظ** | subnet list |
| Market cap (α × price) | τ 112.40k (~11th-largest subnet) | subnet list |
| Emission (Τ) | 0.0035 τ/block | subnet list |
| **Net Inflow EMA (Τ)** | **+0.0020 τ (POSITIVE)** | subnet list |
| Pool P(Τ_in, α_in) | τ 42.61k, 1.94m ظ | subnet list |
| Stake (α_out) | 3.18m ظ | subnet list |
| Supply | 5.12m ظ / 21M | subnet list |
| Tempo (n) | 360 blocks (~20 tempos/day) | subnet show |
| Mechanisms | **2** (multi-mech subnet) | subnet list |
| Registration cost (recycled) | **τ 0.1077** (~$24) | `btcli subnet show --netuid 68` |
| Owner coldkey | 5EcdJL…iJNy4V12V | subnet show |

**Miner pool $/day.** Using the protocol default M_alpha ≈ 2,950 α/day to miners
(~1 α/block × 41% × 7,200 blocks/day):

```
miner_pool_usd_per_day = 2,950 ظ × 0.0220 τ × $225 ≈ $14.6k/day
```

Chain cross-check: observed incentive-earning emissions across both mechanisms
≈ 121 ظ/tempo × 20 tempos ≈ 2,420 ظ/day → ~$12.0k/day. So **~$12–14.6k/day**
total miner pool. Use ~$14.6k headline.

**Token-health verdict: MODERATE (3/5).** Alpha 0.0220 τ is mid-tier (not a
high-price subnet, not the bottom either), market cap ~τ112k is respectably in
the top dozen subnets, and crucially **net inflow is POSITIVE (+0.0020 τ)** —
genuinely uncommon (most of the long tail, incl. the Quasar reference at −0.0040,
is melting). Pool reserve τ42.6k is moderately deep. A skilled miner liquidating
even ~$200/day of alpha (~0.9 τ) is ~0.002% of the τ42.6k reserve → negligible
slippage. Positive inflow + decent cap offset the only-mid price.

---

## PHASE 2 — What is the work?

Source: `github.com/metanova-labs/nova` (README + validator docs),
DeepWiki system-architecture, subnetalpha.ai/subnet/nova, Metanova whitepaper.

- **Work type: `data`/search + ML inference (drug discovery).** Miners run a
  search/generation strategy over the ~1.75B-molecule SAVI library to propose a
  candidate that scores highest on **PSICHIC predicted binding affinity** to the
  current epoch's protein target. This is *not* GPU-hours-for-tokens commodity
  inference — it is a **combinatorial optimization / cheminformatics contest**.
- **Required hardware:** Validators need **2 GPUs** for parallel PSICHIC
  inference (README; Ubuntu 24.04, Python 3.10–3.12, CUDA 12.6). Miners run
  search + PSICHIC scoring locally; PSICHIC is a comparatively lightweight GNN,
  so a **single GPU (e.g. RTX 4090, ~$0.30–0.50/hr → ~$8–14/day)** is a viable
  floor. More compute buys more candidates evaluated per epoch, but compute is
  *not* the binding constraint — **search quality is.**
- **EDGE TEST — this is the rare subnet where a structural edge is real.**
  Reward is for *finding the best molecule*, not for burning GPU. A newcomer with
  genuine **computational chemistry / molecular generation / active-learning /
  docking** expertise can out-search incumbents and win epochs. Conversely a
  commodity miner with no chemistry edge will essentially never produce the
  single best candidate and earns ~$0. Edge = **domain/algorithmic, not compute.**

---

## PHASE 3 — Incentive mechanism teardown (the traps)

Source: DeepWiki `metanova-labs/nova` architecture, subnetalpha.ai, repo docs.

- **Distribution shape — WINNER-TAKE-ALL per epoch (the headline trap).**
  Each epoch (~360 blocks ≈ 1 hr) fixes one protein target; validators score
  every submission with the deterministic PSICHIC oracle and the **top molecule
  takes the epoch.** Confirmed on-chain: in **Mechanism 1 a single UID (54) holds
  incentive = 1.000000 (100%)**; in **Mechanism 0 the top two UIDs hold
  72%/28%.** Weights are set proportional to scores, but because scoring is a
  deterministic max over a shared library, realized payout collapses onto the
  current best searcher → effectively winner-take-all.
- **Commit-reveal:** timelock encryption (BTDr) hides submissions until after the
  deadline and **bars submissions in the last 10 blocks** — anti-copy/anti-snipe.
  Good for fairness, but it doesn't help a weaker searcher: the best molecule
  still wins.
- **Rich-get-richer:** Structural. The optimal molecule for a fixed target is a
  fixed point; whoever has the best search converges to it and keeps winning that
  target until the target rotates. Earning code is made public, so edges decay —
  but the incumbent operator re-optimizes each new target first.
- **Assignment gating: NO for miners** (open submission, no orchestrator picks
  who works). **Validators are gated** ("DM the NOVA team for an API key").
- **Weight-setting — RED FLAG: owner capture of both sides.** The subnet owner
  coldkey **`5EcdJL`** runs **UID 5 — the dominant validator (77.6% of
  dividends)** — *and* **UID 0 — the #1 miner (72% of Mechanism-0 incentive)**,
  both labelled `(*Owner controlled)`. One entity sets most of the weights *and*
  collects most of the miner emission. Remaining validator weight: TAO.com 11%,
  Yuma/DCG 8%, tao.bot 2%, Rizzo 1%.
- **Newcomer cold-start:** Mechanically open — register any time (τ0.1077 ≈ $24),
  submit immediately, no whitelist for miners. **Economically brutal:** with
  winner-take-all you earn **$0 every epoch you don't produce the single best
  molecule** — there is no proportional ramp for "pretty good" submissions.

---

## PHASE 4 — Saturation / competition

Source: `btcli subnet metagraph --netuid 68` (both mechanisms),
`btcli subnet show`. Raw saved to `raw_metagraph_mech0.txt`/`_mech1.txt`.

**Incentive concentration (combined across both mechanisms):**

| Mech | UID | Identity / coldkey | Incentive share | Emissions (ظ/tempo) |
|---|---|---|---|---|
| 0 | 0 | **(*Owner controlled)** `5EcdJL` | **0.7220 (72%)** | 86.56 |
| 0 | 61 | anon `5Haoap` | 0.2780 (28%) | 33.33 |
| 1 | 54 | anon `5F4UvY` | **1.0000 (100%)** | 1.48 |
| — | _all other ~189 UIDs_ | — | 0.0000 | 0.000 |

- UIDs with incentive > 0: **3 total** (2 in mech 0, 1 in mech 1) out of ~192
  miner slots.
- **Effective number of earners = 1 / Σ shareᵢ²** over combined miner emission
  (shares 0.713 / 0.275 / 0.012) **= 1 / 0.585 ≈ 1.71.**
- But **71% of all miner emission is the owner's own UID 0.** Net of the owner,
  there is effectively **~1 genuinely independent earner** (the anon at 27%).

So the raw metric ("only ~1.7 earners vs a $14.6k/day pool") *looks* wide open —
but the openness is illusory in the Quasar/IOTA pattern: the dominant earner is
the operator, and the mechanism is winner-take-all. Either (a) independent
miners genuinely can't beat the operator's search, or (b) the operator structurally
front-runs each new target. Live participation by outsiders is currently near-zero.

- **Registration cost (recycled): τ0.1077 (~$24)** — non-refundable but a minor
  barrier, not the constraint.
- Public miner artifacts (S3/heartbeat bucket sizing incumbent rigs): not located
  this pass — UNKNOWN. Would grep the repo for `s3://`/bucket/dashboard and check
  any NOVA leaderboard; incumbent rig class therefore inferred, not measured.

---

## PHASE 5 — EV synthesis

Assumptions: single RTX-4090-class rig + ops ≈ **$12–15/day**; reg τ0.1077 (~$24)
amortized over ~90 days ≈ $0.27/day. Pool ~$14.6k/day, alpha 0.0220 τ, TAO $225,
positive inflow so price_trend ≈ flat-to-up; liquidation haircut ~0.60 (deep pool
vs a small miner's daily sells). **The entire EV hinges on `your_share`, which
here is a function of search/chemistry skill, not compute** — and winner-take-all
makes it bimodal and high-variance.

| Scenario | Assumed your_share | Gross/day | Realized (×0.6) | Net/day | Net/month |
|---|---|---|---|---|---|
| LOW | ~0% — no chemistry edge, never the epoch winner | $0 | $0 | −$15 | **−$450** |
| BASE | ~1.5% — skilled searcher wins occasional epochs/targets | $219 | $131 | $119 | **+$3.6k** |
| HIGH | ~10% — strong drug-discovery/ML edge, wins many targets | $1,460 | $876 | $861 | **+$25.8k** |

The spread is enormous and driven entirely by whether you can repeatedly produce
the single best-scoring molecule against an operator who controls the top
validator *and* the top miner. **Biggest single risk:** owner capture — coldkey
`5EcdJL` is simultaneously the dominant validator (sets weights) and the #1 miner
(72% of payout); a newcomer may be structurally out-competed/under-weighted no
matter how good the molecule. **The one thing that would most change the answer:**
run a real NOVA miner with a serious search strategy for ~1–2 weeks and measure
whether a fresh hotkey actually wins any epochs and accrues incentive.

**Verdict: WATCH** (NO-GO for a generic/commodity miner). Unlike commodity-GPU
subnets, NOVA's reward genuinely rewards a *structural edge* a domain expert can
have, and the token is healthy (positive inflow, top-dozen cap). But
winner-take-all variance + single-entity (owner) control of both the dominant
validator and the top miner are serious red flags that block a confident GO.
**Minimum edge to be +EV:** real computational-chemistry / molecular-optimization
capability that can beat the incumbent operator's search on a deterministic
oracle — pure compute or a generic pipeline is not enough.

---

## SCORECARD

```
SCORECARD
netuid: 68
name: NOVA
work_type: data
alpha_price_tao: 0.0220
net_inflow_ema_tao: +0.0020
token_health: 3
miner_pool_usd_per_day: 14600
effective_num_earners: 1.71
saturation: 3
min_rig_cost_usd_per_day: 13
registration_cost_tao: 0.1077
mechanism_trap: winner_take_all
newcomer_friendliness: 2
edge_required: real computational-chemistry / ML molecular-optimization skill to win the single best-affinity molecule per epoch on a deterministic oracle; commodity compute alone earns ~0
ev_usd_per_month_low: -450
ev_usd_per_month_base: 3600
ev_usd_per_month_high: 25800
confidence: 2
recommendation: WATCH
composite_score: 13
one_line_thesis: Healthy positive-inflow drug-discovery subnet whose winner-take-all PSICHIC-scored molecule contest genuinely rewards a chemistry/ML edge — but the owner coldkey runs both the dominant validator and the #1 miner (72% of payout), so only a true domain expert who can repeatedly out-search the operator is +EV; everyone else earns ~0.
```

### Key evidence behind each score
- **token_health 3** — alpha 0.0220 τ (mid-tier price), market cap τ112k
  (~11th-largest subnet), and **net inflow +0.0020 τ (POSITIVE — rare)**; pool
  reserve τ42.6k is moderately deep. Source: `btcli subnet list`.
- **miner_pool $14.6k/day** — 2,950 ظ/day default × 0.0220 τ × $225; chain-observed
  emissions (~121 ظ/tempo × 20) cross-check ~$12k. Source: `btcli subnet list` +
  metagraph emissions.
- **effective_num_earners 1.71 / saturation 3** — only **3 of ~192 miner UIDs**
  earn (mech0: owner 72%, anon 28%; mech1: anon 100%); 1/Σs² = 1.71, but 71% is
  the owner's own UID 0 → ~1 independent earner. Looks open, capped by WTA +
  owner capture. Source: metagraph (both mechanisms).
- **min_rig $13/day** — validators need 2 GPUs; miners run lighter PSICHIC GNN +
  search, single RTX-4090-class viable (~$0.30–0.50/hr). Source: repo README /
  DeepWiki; Vast/RunPod rates.
- **registration_cost τ0.1077** — `btcli subnet show --netuid 68` ("Registration
  cost (recycled)"); ~$24.
- **mechanism_trap winner_take_all** — best molecule per ~1hr epoch wins;
  on-chain mech1 UID54 = 100% incentive, mech0 top-two 72/28; deterministic
  PSICHIC oracle + BTDr commit-reveal. Also owner-capture red flag (coldkey
  `5EcdJL` = top validator UID5 *and* top miner UID0). Source: DeepWiki +
  metagraph + subnet show owner field.
- **newcomer_friendliness 2** — open registration, no miner whitelist, submit
  immediately; BUT winner-take-all means $0 unless you produce the single best
  molecule (no proportional ramp), and the operator controls weights. Source:
  DeepWiki epoch workflow + metagraph.
- **confidence 2 / WATCH** — EV is bimodal and skill-gated; owner controls both
  validator and top miner; per-epoch win dynamics unobservable without a live
  test. Resolve by running a real search miner ~1–2 weeks and checking whether a
  fresh hotkey wins any epochs.
```
```
