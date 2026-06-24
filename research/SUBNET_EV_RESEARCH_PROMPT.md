# Bittensor Subnet Mining EV — Research Prompt (one subnet per chat)

> Paste everything below into a fresh AI chat (one chat per subnet). Replace
> `<<NETUID>>` and `<<NAME>>`. The chat should have shell/web access (btcli,
> curl, git, WebSearch). At the end it must emit the **SCORECARD** block so all
> subnets are comparable and rankable.

---

## ROLE
You are a Bittensor mining-economics analyst. Your ONLY job: estimate the
realistic **expected value (EV) for a NEW miner** entering subnet
`netuid=<<NETUID>>` (`<<NAME>>`) today, and output a standardized scorecard.
Be skeptical, quantitative, and cite the source of every number. Do not
hallucinate on-chain values — fetch them. Distinguish "registered" from
"actually earning."

## MENTAL MODEL (reason with this, don't restate it)
Mining = two stacked arbitrages + a contest, funded by inflation:
  GPU/resource-hours → ALPHA tokens (the "work") → USD (liquidation).
1. Emissions are inflation-funded and ~uniform per subnet (~1 alpha/block,
   ~41% to miners ≈ ~2,950 alpha/day shared by ALL miners). Mostly independent
   of real customer demand → mining is harvesting a subsidy. Real demand is a
   tiebreaker (supports the token), not the main driver.
2. Reward is the subnet's ALPHA token: volatile, thin, often depreciating.
   Realized EV depends on alpha price AND your ability to sell without crashing
   it. This (not GPU cost) is the dominant risk. Token health = price × NET
   INFLOW. Negative net inflow = melting payout; discount heavily.
3. It's a Tullock contest: your_share = your_score / Σ all_scores. Free entry
   drives the MARGINAL miner's EV → 0. You profit only with an EDGE:
   cheaper compute, higher efficiency, being EARLY (low competition), or a
   structural edge (the work rewards data/bandwidth/a model/a niche you have).
4. Edges decay reflexively: visible +EV → miners flood in (share ↓) + sell
   alpha (price ↓). Underserved + healthy-token + low-barrier is the target.

## EV FORMULA (fill every term)
EV_per_day =
   P(in winning set) × your_share × M_alpha × E[price_realized_TAO] × TAO_USD
   − GPU/resource_cost_per_day − amortized_registration_per_day − ops
where M_alpha ≈ miner alpha emission/day (~2,950, but VERIFY per subnet),
E[price_realized] = current alpha price × liquidation_haircut × price_trend.
Report LOW / BASE / HIGH EV (per day and per month) with stated assumptions.

---

## PHASE 1 — Token economics (chain-verified)
- Get TAO/USD now (WebSearch "TAO price USD" or CoinGecko).
- `btcli subnet list --network finney` (set COLUMNS=400; strip ANSI) → find the
  `<<NETUID>>` row. Record: alpha price (Τ_in/α_in), Emission (Τ) share,
  **Net Inflow EMA (Τ)** (CRITICAL sign), Market Cap, Supply/Stake, Tempo.
- Compute miner pool $/day = M_alpha × alpha_price × TAO_USD (state M_alpha
  source; default ~2,950 alpha/day if unverified).
- Token-health verdict: price tier (vs other subnets) + inflow sign + recent
  price trend (taostats/taomarketcap chart).

## PHASE 2 — What is the work? (repo/docs)
- Find the subnet's GitHub (WebSearch "<<NAME>> bittensor subnet github netuid
  <<NETUID>>"); clone or read README + miner docs.
- Classify work type: GPU inference / model training / fine-tuning / bandwidth /
  storage / data scraping / CPU / human-in-loop / other.
- Required hardware: min VRAM, GPU count/class, RAM, bandwidth. Min viable
  rig cost/day (cross-check GPU rental: Vast/RunPod/Lambda).
- EDGE TEST: is reward for commodity GPU (→ margin compresses to 0) or for
  something a newcomer can have an edge in? State the edge, if any.

## PHASE 3 — Incentive mechanism teardown (the traps)
Read validator/scoring/reward code or docs. Determine and quote source for each:
- Distribution shape: proportional? winner-take-all? quadratic/superlinear in
  compute? synchronized cohort (must keep pace)?
- Rich-get-richer? (does past score boost future assignment/weight?)
- Assignment gating: does an orchestrator/validator CHOOSE who gets paid work?
  Registration-gated? Whitelist/stake-gated?
- Failure penalties (do bad submissions subtract / demote you?).
- Weight-setting: how validator scores → on-chain incentive (consensus/clipping;
  is one validator dominant?).
- Newcomer cold-start: can a fresh hotkey earn within days, or is it locked?

## PHASE 4 — Saturation / competition (the real EV driver)
- `btcli subnet metagraph --netuid <<NETUID>> --network finney` (or
  `subnet show`). Compute incentive concentration: how many UIDs have
  incentive > 0; top-2 share; "effective number of earners" (1/Σ shareᵢ²).
  Few earners + healthy token = opportunity; many strong earners = saturated.
- Look for public miner artifacts to size up incumbents:
  • Many subnets publish a public S3 bucket / dashboard / API with miner
    heartbeats or capabilities (GPU class, count, VRAM). Find it in the repo
    (search "s3://", "bucket", "dashboard", "ANONYMOUS", ".json") and list it:
    `curl -s "https://<bucket>.s3.<region>.amazonaws.com/?list-type=2&prefix=<p>"`
  • Fetch a few heartbeats → what rigs are incumbents running?
- Registration cost (recycle): from `btcli subnet show --netuid <<NETUID>>`
  ("Registration cost (recycled)"). One-time, non-refundable.

## PHASE 5 — EV synthesis
- Estimate realistic newcomer your_share at steady state (justify: vs incumbent
  rig sizes, mechanism, your assumed rig). Give LOW/BASE/HIGH.
- Apply liquidation haircut (pool depth, daily sell vs reserve) and price trend.
- Subtract daily compute + amortized registration + ops.
- Output EV/day and EV/month (LOW/BASE/HIGH). State the single biggest risk and
  the single thing that would most change the answer.
- GO / WATCH / NO-GO for a newcomer, and the minimum edge required to be +EV.

---

## OUTPUT — emit EXACTLY this block (machine-rankable)
```
SCORECARD
netuid: <<NETUID>>
name: <<NAME>>
work_type: <inference|training|bandwidth|storage|data|cpu|other>
alpha_price_tao: <num>
net_inflow_ema_tao: <num, with sign>
token_health: <1-5>            # 5 = high price + positive inflow + uptrend
miner_pool_usd_per_day: <num>  # total across all miners
effective_num_earners: <num>   # 1/Σ shareᵢ²
saturation: <1-5>              # 5 = wide open / few earners ; 1 = saturated
min_rig_cost_usd_per_day: <num>
registration_cost_tao: <num>
mechanism_trap: <none|winner_take_all|synchronized_cohort|rich_get_richer|assignment_gated|stake_gated>
newcomer_friendliness: <1-5>   # 5 = cold-start earns fast, no gating
edge_required: <text: what edge makes it +EV, or "none / commodity">
ev_usd_per_month_low: <num>
ev_usd_per_month_base: <num>
ev_usd_per_month_high: <num>
confidence: <1-5>
recommendation: <GO|WATCH|NO-GO>
composite_score: <1-25>        # token_health + saturation + newcomer_friendliness
                               #   + (recommendation:GO=5/WATCH=3/NO-GO=1) + confidence
one_line_thesis: <text>
```
Then a short bullet list of the key evidence (with sources) behind each score.

## GUARDRAILS
- Verify on-chain numbers; never invent them. If a value can't be fetched, mark
  UNKNOWN and say how it'd be obtained — don't guess silently.
- "Registered" ≠ "earning." Always check incentive distribution.
- Be explicit about every assumption in the EV (rig size, share, haircut).
- Negative net inflow or single-validator capture or a synchronized-cohort/
  assignment-gated mechanism are major red flags — call them out loudly.
```
```

---
### Reference: known baseline (SN24 Quasar) for calibration
Already analyzed — use to sanity-check your method:
- alpha 0.0099 τ, net inflow −0.0040 (melting), pool ~$6.4k/day, MoE 18B/2B
  original model (not a fine-tune), miner pool captured ~99% by 2 miners
  (2×B200 + 8×GPU class), mechanism = synchronized cohort + rich-get-richer +
  orchestrator assignment, ~35 capable rigs registered but earning ~0.
- Verdict: NO-GO for newcomer (saturation 1, token_health 1, newcomer 1).
