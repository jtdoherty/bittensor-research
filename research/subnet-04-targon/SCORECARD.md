# Subnet 4 — Targon (Manifold Labs) — Mining EV Research

_Analysis date: 2026-06-23 • Network: finney • Mechanism 0 • TAO ≈ $220 (range $216–$235 across sources)_

> Methodology: `../SUBNET_EV_RESEARCH_PROMPT.md`. Calibration baseline = SN24 Quasar
> (`../subnet-24-quasar/SCORECARD.md`). Targon is a different animal from Quasar:
> it is one of the few subnets with **real organic revenue** (a sold-out
> confidential-compute GPU marketplace) — but the token is still **melting** and
> the work requires **non-commodity TEE hardware**.

## SCORECARD (machine-rankable)
```
SCORECARD
netuid: 4
name: Targon
work_type: inference              # confidential-compute (TEE) GPU rental marketplace + verified LLM inference
alpha_price_tao: 0.0524
net_inflow_ema_tao: -0.0046
token_health: 2                  # strong-ish price tier BUT negative inflow (melting) + TAO -18.8%/7d
miner_pool_usd_per_day: 34100    # 2960 alpha/day x 0.0524 tao x $220
effective_num_earners: 1.98      # 1/Sum(share^2); only 5 UIDs earn, UID89 alone = 68.4%
saturation: 2                    # very concentrated (top-2 = 85%) but demand > supply (high tiers sold out)
min_rig_cost_usd_per_day: 90     # 1x TEE-capable H200 node IF rentable (~$3-4/hr); realistically own ~$30k+ hw
registration_cost_tao: 0.0005    # recycled, ~$0.10 — entry cost is irrelevant; hardware is the barrier
mechanism_trap: assignment_gated # demand-auction + remote-attestation gated (NOT cohort/winner-take-all)
newcomer_friendliness: 2         # no cohort/rich-get-richer lock, but steep TEE hw + attestation barrier
edge_required: cheap access to TEE-capable Hopper/Blackwell (H100/H200/B200 + Intel TDX or AMD SEV-SNP + Xeon 6th-gen + 3TB) that you can attest and price below incumbents — this hardware is NOT on Vast/RunPod, so owning/colocating it IS the edge
ev_usd_per_month_low: -900       # 1 TEE H200, poor utilization, alpha melts faster than you sell
ev_usd_per_month_base: 2500      # 1-2 TEE H200 reaching a small-earner tier into real demand
ev_usd_per_month_high: 9000      # well-priced multi-GPU TEE fleet capturing unmet (sold-out) demand
confidence: 3                    # emission-from-demand math under-documented; newcomer utilization uncertain
recommendation: WATCH
composite_score: 12              # token_health 2 + saturation 2 + newcomer_friendliness 2 + (WATCH=3) + confidence 3
one_line_thesis: A real-revenue confidential-compute GPU marketplace where emission is auctioned to genuine customer demand (high tiers sold out) — so it is NOT pure subsidy-harvesting and a newcomer CAN cold-start — but the token is melting (-inflow), 2 operators take 85% of pool, and earning requires non-commodity TEE hardware (Intel TDX / SEV-SNP H100/H200/B200) you cannot rent on Vast; +EV only if you already have cheap attestable TEE GPUs.
```

## Key evidence (with sources)

### Phase 1 — Token economics (`btcli subnet list --network finney`, row 4)
- alpha price **0.0524 τ/δ** — upper-mid tier, ~5× Quasar (0.0099), comparable to the stronger subnets.
- **Net Inflow EMA = −0.0046 τ (NEGATIVE / melting)** — capital is leaving the pool despite real revenue. Dominant token risk.
- Market Cap τ **289.0k**; Pool P = τ **128.73k / 2.46m δ**; Stake (α_out) **3.06m δ**; Supply **5.51m / 21M**; Tempo **95–96/360** (~20 tempos/day).
- **Miner pool**: incentive-bearing emissions = **148.0 δ/tempo × 20 = 2,960 δ/day** (computed from metagraph emissions of the 5 earning UIDs; matches the ~2,950 heuristic exactly) → 2,960 × 0.0524 × $220 ≈ **$34,100/day total across ALL miners**.
- TAO −5.8%/24h, **−18.8%/7d** (CoinGecko/CMC). Token-health verdict: **2/5** — decent price tier, but negative inflow + a falling base asset = you're paid in a melting token.

### Phase 2 — What is the work? (`manifold-inc/targon` repo, `docs/miner/miner.md`)
- **Confidential-compute GPU rental marketplace** + verified LLM inference. Original SN4 mechanism = *deterministic verification* of OpenAI-compatible endpoints (ground-truth tokens regenerated from query+seed and matched). It has since pivoted to a **TEE GPU marketplace**: miners list attested GPUs; customers rent them; emission tracks that demand.
- **Hardware (steep, non-commodity):** NVIDIA Hopper (**H100/H200**) or Blackwell (**B200**) with **confidential-compute / GPU TEE**; **Intel Xeon 6th-gen** for GPU passthrough; **Intel TDX** *or* **AMD EPYC 9xx4 (Genoa/Bergamo) SEV-SNP**; **≥3 TB storage** (under-reporting storage stops emission). Remote attestation required to earn.
- **EDGE TEST → this is the crux.** Reward is for *commodity GPU-hours*, **but the confidential-compute requirement makes the supply non-commodity**: you cannot rent a TDX/SEV-SNP-attested H200 on Vast/RunPod/Lambda. So the edge = *access to attestable TEE hardware at low cost*. If you have it, the work rewards real demand; if you don't, there is no entry.

### Phase 3 — Incentive mechanism teardown (`docs/miner/miner.md`)
- **Distribution shape: demand-proportional auction.** "Miner emissions are currently split proportionally to public demand." Miners set price in `config.json` (`"price": 120` = cents/hr/GPU); bids are capped (Hopper auction `"max_bid": 300` c/hr). **"The remainder of emissions not allocated to auctions is burned."** → emission is gated by *real customer demand*, not pure subsidy.
- **Not winner-take-all, not a synchronized cohort, not rich-get-richer** in the Quasar sense — meaningfully less trap-y than SN24.
- **Assignment / attestation gating:** you must pass **remote attestation** of the TEE config, run the TVM installer, and be matched to demand. Demand for your GPU class at your price is the real gate. Mis-declared storage → "machine will stop earning emission."
- **Newcomer cold-start:** a fresh hotkey with an attested, competitively-priced TEE node *can* earn within days IF there is unmet demand for its tier — no structural lock-out. This is the key contrast with Quasar.

### Phase 4 — Saturation / competition (`btcli subnet metagraph --netuid 4`)
- Only **5 UIDs have incentive > 0**: **UID89 = 0.684 (68.4%)**, UID7 = 0.166, UID57 = 0.071, UID32 = 0.046, UID74 = 0.033. **Top-2 = 85.1%. Effective earners = 1/Σshare² ≈ 1.98.**
- Per-tempo emissions of earners: UID89 **101.2 δ** (≈$1.16k/day gross alpha), UID7 24.6 δ, down to UID74 4.9 δ (≈$1.1k/day gross — even the smallest earner is sizeable). One operator clearly runs a large TEE fleet.
- **Counter-signal (bullish for a newcomer):** Targon's high-end tiers (**B200, H100 XL, 4090**) are reported **sold out — "demand is eating supply."** Targon H200 pricing (Mar 2026): ~$2.40 / $4.80 / $9.60 per hr vs AWS p5e ~$10.60/hr (4–5× cheaper, full TEE). So unlike a saturated subsidy contest, *adding attested supply can capture real unmet demand.*
- Owner UID28 holds dividends **0.809** (validator/owner capture of the dividend side) — normal for SN4's owner-run validator; does not block miner incentive.
- Registration (recycled): **τ0.0005 ≈ $0.10** — entry cost is a non-issue; the barrier is TEE hardware + attestation.

### Phase 5 — EV synthesis
Assumptions: 1× TEE-capable H200 node, TAO $220, alpha 0.0524 τ, **liquidation haircut ~0.5–0.6** (thin pool: 128k τ / 2.46m δ + negative inflow + falling TAO), ops ~$20/day.
- **LOW (−$900/mo):** node passes attestation but gets low utilization (demand for your tier/price soft), gross alpha ~$100–200/day × 0.5 haircut ≈ $50–100/day − $90 rent − ops → roughly −$30/day.
- **BASE (+$2,500/mo):** node reaches a small-earner tier into real demand, gross ~$300–500/day × 0.55 ≈ $165–275/day − $90 − $20 ≈ +$55–165/day. Ramp takes weeks.
- **HIGH (+$9,000/mo):** well-priced multi-GPU TEE fleet capturing sold-out high-end demand, matching mid earners at ~$1k/day net.
- **Biggest risk:** the **melting token (−inflow) + falling TAO** — your alpha can depreciate faster than you can liquidate, turning paper gross into thin/negative realized. Secondary: utilization/attestation friction.
- **Single thing that would most change the answer:** whether you can source **attestable TEE H100/H200/B200 cheaply** (own/colocate vs rare confidential-compute cloud). With it, real demand makes this plausibly +EV; without it, there is no entry → NO-GO.
- **Verdict: WATCH.** Not a NO-GO like Quasar — it has genuine demand, a non-trap demand-auction mechanism, and a true cold-start path. But it fails the token-health screen (melting) and demands non-commodity hardware. Minimum edge to be +EV: **cheap, attestable TEE Hopper/Blackwell capacity priced under incumbents.**

## Sources
- `btcli 9.20.0`: `subnet list`, `subnet show --netuid 4`, `subnet metagraph --netuid 4` (finney, 2026-06-23).
- Repo `github.com/manifold-inc/targon`: `README.md`, `docs/miner/miner.md` (auction/emission, hardware, attestation).
- TAO price: CoinGecko / CoinMarketCap (TAO ≈ $216–235, −18.8%/7d).
- Targon pricing & demand: ownyourmind.ai Targon SN4 review; community report of sold-out B200/H100-XL/4090 tiers and H200 $2.40–9.60/hr (Mar 2026).
- Calibration baseline: `../subnet-24-quasar/SCORECARD.md`.
