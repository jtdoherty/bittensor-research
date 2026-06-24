# Subnet 64 — Chutes — Mining EV Research

_Analysis date: 2026-06-23 • Network: finney • Mechanism 0 • TAO assumed = $250 (sources showed $235–$264)_

## SCORECARD (machine-rankable)
```
SCORECARD
netuid: 64
name: Chutes
work_type: inference            # serverless GPU inference (LLM/vision/custom containers)
alpha_price_tao: 0.0747
net_inflow_ema_tao: +0.0061
token_health: 4                 # top-tier alpha price, POSITIVE inflow, real revenue + buybacks
miner_pool_usd_per_day: 55250   # 2960 alpha/day x 0.0747 tao x $250
effective_num_earners: 8.4      # 1/Sum(share^2) over incentive; 15 UIDs incentive>0
saturation: 2                   # ~4,400 H100-equiv GPUs; capital-saturated
min_rig_cost_usd_per_day: 40    # small node (e.g. mixed A5000/A10) rented; 8xH100 ~ $384/day
registration_cost_tao: 0.0005   # recycled; trivial — real barrier is the GPU fleet
mechanism_trap: rich_get_richer # 7-day rolling compute-time sum + incumbents capture routed traffic
newcomer_friendliness: 3        # no whitelist, cheap reg, BUT GraVal HW attestation + 7-day ramp + utilization risk
edge_required: sunk/idle GPUs or compute < ~$13 per H100-equiv/day (cheap power, owned HW). At market rental = -EV.
ev_usd_per_month_low: -8500     # 8xH100 rented @ ~$2/hr market
ev_usd_per_month_base: -3700    # 8xH100 owned, amortized (~$28/GPU/day)
ev_usd_per_month_high: +1800    # genuinely free/idle GPUs, power-only cost, + mild alpha appreciation
confidence: 4
recommendation: NO-GO
composite_score: 14             # 4 + 2 + 3 + (NO-GO=1) + 4
one_line_thesis: Top-revenue subnet with a healthy, appreciating token — but a commodity-GPU contest where ~4,400 H100-equiv GPUs share only ~$55k/day, so per-GPU alpha (~$12.6) is far below GPU cost; only +EV with sunk/free hardware or a bet on alpha appreciation.
```

## Key evidence (with sources)

### Phase 1 — Token economics (chain-verified, `btcli subnet list --network finney`)
- Row 64: **alpha price 0.0747 τ/α** (among the highest of any subnet), **Market Cap τ 410.53k**, **Emission (Τ) 0.0111**, **Net Inflow EMA +0.0061 τ (POSITIVE — token accreting, not melting)**, Pool **P = τ 201.35k TAO_in / 2.70m α_in** (very deep, highly liquid), Supply 5.49m / 21M, Tempo 30/360 (~360-block/72-min tempo → ~20 tempos/day).
- **Miner pool**: summed Emissions column for the 15 incentive>0 UIDs = 148.0 α/tempo × 20 = **2,960 alpha/day to miners** (matches the ~2,950 default → verified). → 2,960 × 0.0747 τ × $250 = **~$55,250/day total across ALL miners**.
- Token-health verdict: **strong (4/5)** — top-tier alpha price, positive net inflow, deep pool, and real product revenue (auto-staking buybacks). Main caveat: alpha has had large drawdowns historically and price is reflexive to the Chutes business.

### Phase 2 — What is the work? (`chutes.ai/docs`, github chutesai/chutes-miner)
- **Serverless GPU inference**: miners contribute GPUs to a permissionless pool; the network routes real LLM/vision/custom-container jobs to them. Chutes reportedly serves 50–100B+ tokens/day to 400k+ users.
- Hardware: bare-metal/VM, **RAM ≥ VRAM per GPU** (e.g. 4×A40 needs ≥192GB RAM), static unique IPs with 1:1 port mapping, big disk for model/docker cache. Supported GPUs span cheap (T4, A10, A5000) to **8×H100 nodes**.
- **EDGE TEST → commodity GPU.** Reward is for raw compute-time serving inference. No proprietary-data/model edge for a newcomer; margin compresses to the cheapest-compute operator.

### Phase 3 — Incentive mechanism (the traps)
- **Scoring = total compute time** over a **rolling 7-day sum** ("encouraging long-term stability"), plus bounties for being first to serve a new chute. (`chutes.ai/docs/miner-resources/overview`)
- **One UID per operator** — "Never register more than one UID, it just reduces your total compute time." You scale by adding GPUs under a single UID, so the ~15 earning UIDs each represent a *fleet operator*, not a single card.
- **Miner-side Gepetto** auto-selects/deploys chutes; validators don't hand-assign, BUT your GPUs only accrue compute time when the network actually routes chutes to them → **utilization/routing risk** (popular models concentrate on incumbents = rich-get-richer).
- **GraVal hardware attestation** gates earning — GPUs must pass cryptographic HW verification before deployment eligibility. Weight-setting dominated by the single primary validator (UID 1, dividends 0.585).
- Cold start: a fresh hotkey *can* register (reg cost τ0.0005) and earn, but ramps over the 7-day window and must clear HW attestation + IP/port requirements.

### Phase 4 — Saturation / competition
- `btcli subnet metagraph --netuid 64`: **15 of 256 UIDs have incentive > 0**; **effective earners ≈ 8.4** (1/Σshare²); **top UID 207 = 24.6%**, **top-2 = 38.7%**.
- Fleet size (secondary, subnetalpha.ai / ourcryptotalk): **~4,400 H100-equivalent GPUs**. → per-H100-equiv alpha revenue ≈ $55,250 / 4,400 = **~$12.6/GPU/day**.
- Registration cost (recycled): **τ 0.0005** (`btcli subnet show`) — negligible; the binding constraint is GPU capital + attestation.

### Phase 5 — EV synthesis
- Representative newcomer = an **8×H100 node** (a documented config) ≈ 8 H100-equiv → share ≈ 8/4,400 = **0.18%** → revenue ≈ **$100/day** (gross alpha). LOW (1 GPU) ≈ $12/day; HIGH (24 H100-equiv) ≈ $300/day.
- Realized-price adj: deep pool + positive inflow → **small haircut (~0.95)**, mild appreciation (~1.1) → roughly neutral on spot.
- Compute cost dominates: 8×H100 at **market rental ~$2/hr = $384/day**; **owned-amortized ~$28/GPU/day = $224/day**; **sunk/idle (power-only) ~$40/day**.
- Net EV/day: rented **≈ −$284**, owned **≈ −$124**, free/idle **≈ +$60**. → Monthly **LOW −$8.5k / BASE −$3.7k / HIGH +$1.8k**.
- **Biggest risk:** per-GPU alpha revenue (~$12.6/H100-equiv/day) is far below any market GPU cost → you're paying to accumulate alpha. **What most changes the answer:** your true marginal compute cost (free/idle hardware flips it positive) and a bullish view on the alpha token (real Chutes revenue + buybacks could make holding the alpha, not the USD harvest, the actual trade).

## Verdict
**NO-GO for a newcomer renting compute at market rates** (structurally −EV: $12.6/GPU/day revenue vs $36–72/GPU/day rental). Conditional **WATCH** only if you have *genuinely sunk/idle GPU capacity with cheap power* and want long alpha exposure — Chutes is a healthy, revenue-generating token, so the play here is "be long the alpha cheaply," not "harvest a mining subsidy." Minimum edge to be +EV: compute cost below **~$13 per H100-equivalent per day**.
