# Bittensor Subnet Mining — EV Research

Goal: find the highest-EV Bittensor subnet(s) to mine. Each subnet is torn down
end-to-end (one folder each) and reduced to a comparable `SCORECARD` block.
Methodology / reusable per-subnet prompt: **`SUBNET_EV_RESEARCH_PROMPT.md`**.

## Core thesis (how to read every scorecard)
Mining = two stacked arbitrages + a contest, funded by inflation:
`resource-hours → ALPHA token (the work) → USD (liquidation)`.
- Emissions are inflation-funded and ~uniform per subnet (~2,950 alpha/day to
  miners), mostly independent of real customer demand → mining harvests a
  **subsidy**. Real demand mainly matters because it supports the token.
- You're paid in **alpha** (volatile/thin/often melting). **Token health =
  price × NET INFLOW EMA** is the most underweighted variable. Negative inflow
  = melting payout → discount hard.
- It's a **Tullock contest**: `share = your_score / Σ scores`. Free entry drives
  the marginal miner's EV → 0. **Profit requires an EDGE** (cheap/owned compute,
  efficiency, being EARLY on a thin subnet, or a structural/niche edge).
- The hunting profile: **healthy/positive-inflow token × few effective earners ×
  low barrier × no winner-take-all/cohort/gating trap.** Edges decay reflexively
  → move fast and broad.

## Ranking so far (by composite_score, then recommendation) — 14 subnets analyzed

| Rank | Netuid | Name | Work | α px (τ) | Net inflow | Token health | Eff. earners | Newcomer | Mechanism trap | Rec | Composite | Base EV $/mo |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | 107 | Minos | CPU genomics | 0.0383 | **+0.0012** | 4 | 2.05* | 3 | winner-take-all + owner 87.5% | WATCH | **16** | +5,500 |
| 2 | 51 | lium.io | GPU rental | 0.0543 | **+0.0158** | 4 | 4.25 | 3 | stake_gated + owner 44% | WATCH | **15** | +1,600 |
| 2 | 9 | iota | Training | 0.0362 | **+0.0130** | 4 | 1.39 | 3 | assignment_gated (owner=orch) | WATCH | **15** | +4,000 |
| 4 | 97 | Albedo | LLM distillation | 0.0271 | −0.0002 | 3 | 5.0 | 2 | winner-take-all (+5% moat) | WATCH | **14** | −1,000 |
| 4 | 101 | Tag101 | Social tagging | 0.0058 | +0.0004 | 2 | 220 (12 ops) | 4 | rich_get_richer (Sybil capital) | WATCH | **14** | +900 |
| 4 | 64 | Chutes | GPU inference | **0.0747** | +0.0061 | 4 | 8.4 | 3 | rich_get_richer (commodity) | NO-GO | **14** | −3,700 |
| 7 | 67 | Harnyx | Research agents | 0.0100 | +0.0002 | 2 | 2.46 | 3 | rich_get_richer + owner 64% | WATCH | **13** | +500 |
| 7 | 68 | NOVA | Drug discovery | 0.0220 | **+0.0020** | 3 | 1.71 | 2 | winner-take-all + owner both sides | WATCH | **13** | +3,600 |
| 9 | 4 | Targon | GPU TEE marketplace | 0.0524 | **−0.0046** | 2 | 1.98 | 2 | assignment_gated (demand-auction) | WATCH | **12** | +2,500 |
| 10 | 56 | Gradients | AutoML training | 0.0189 | **−0.0090** | 2 | 2.1 | 2 | rich_get_richer + champ moat | NO-GO | **11** | −150 |
| 11 | 120 | Affine | RL model contest | 0.0590 | **−0.0051** | 3 | 5.0 | 1 | winner-take-all + permanent-terminate | NO-GO | **10** | −707† |
| 12 | 24 | Quasar | Training | 0.0099 | **−0.0040** | 1 | 2.03 | 1 | synchronized cohort (triple) | NO-GO | **9** | −1,400 |
| 12 | 110 | GreenCompute | GPU inference | 0.0098 | 0.0000 | 2 | 1.0 | 1 | assignment_gated (green oracle) | NO-GO | **9** | +200 |
| — | 129 | (none) | DOES NOT EXIST | — | — | — | — | — | btcli totals-row misread | NO-GO | **0** | 0 |

\*Minos earners/pool are the *contestable* third-party slice (owner UID0 self-captures 87.5%).
†Affine base scorecard cites a contingent +$50k, but the realistic newcomer mode is −$707 (lose registration on first failed challenge).

### Read-through
- **Still no clear GO across all 14.** Every subnet lands WATCH/NO-GO — consistent with the free-entry thesis: visible pools are either commodity-saturated (Chutes, Quasar), **owner-captured** (Minos 87.5%, Harnyx 64%, NOVA owner runs both top validator + top miner, GreenCompute one earner = 100%, lium 44%, iota's lone earner = owner), or **skill-gated frontier contests** you only win with a research edge (Affine, Albedo, Gradients). The recurring pattern: *owners self-mine their own subsidy.*
- **Healthy-token shortlist (positive net inflow — the rarest, most underweighted variable):** lium (+0.0158), iota (+0.0130), NOVA (+0.0020), Minos (+0.0012). Melting outliers to discount hard: Gradients (−0.0090), Affine (−0.0051), Targon (−0.0046), Quasar (−0.0040).
- **Best leads (WATCH), each +EV only with a specific edge:**
  - **iota (9):** cheapest rig ($12/day), healthiest inflow, but the only earner is the owner who also runs the orchestrator + top validator. **Decisive unknown: can a fresh hotkey actually get credited?** Cheapest to test → highest-priority empirical pilot.
  - **Minos (107):** genuine niche — needs **variant-calling expertise** to win rounds (out-tune GATK/DeepVariant). +EV for a bioinformatics specialist, not a generic GPU renter.
  - **NOVA (68):** positive inflow + a real domain edge (computational chemistry / molecular-ML), but the owner controls both the top validator and the #1 miner.
  - **lium (51):** only +EV if you **already own in-demand H200/B200** below market + can post collateral.
- **Edge-gated map (mining EV is gated by the edge, not the subnet):** datacenter GPUs → lium (51) / Chutes (64) only if free/sunk; TEE hardware (Intel TDX / SEV-SNP) → Targon (4); genomics → Minos (107); comp-chem → NOVA (68); frontier ML lab → Albedo (97) / Affine (120); agent engineering → Harnyx (67); pure capital + automation → Tag101 (101).
- **Avoid regardless of edge (for a marginal newcomer):** Quasar (24), GreenCompute (110), Gradients (56), Chutes at market rental (64).

## Method notes / consistency
- TAO/USD varied across analyses ($218–$275). Treat cross-subnet $/day as
  **directional**; re-normalize to one TAO price before final ranking.
- `M_alpha ≈ 2,960 alpha/day` to miners was **chain-verified** on SN24/51/64
  (sum of per-tempo Emissions × ~20 tempos/day). Reuse but spot-check per subnet.
- Always separate **registered** from **earning** (incentive > 0) and report
  **effective earners = 1/Σ shareᵢ²**. Watch for **owner self-mining** — it's the
  dominant EV-killer found so far.

## Next actions
1. **Empirically pilot iota (9)** — cheapest rig + healthiest token; the one open
   question (fresh-hotkey crediting) is only answerable by registering and running.
   This is the single highest-value next move and cheap to falsify.
2. Expand the search to more thin/positive-inflow subnets per the prompt. The 14
   analyzed so far are owner-captured, commodity-saturated, or skill-gated — keep
   hunting for the GO profile: **healthy-token subnet whose owner does NOT
   self-capture and whose work matches an edge we have.** Priority screen: pull
   `btcli subnet list`, filter to **positive net inflow**, then teardown any with
   few effective earners + a non-owner-dominated incentive distribution.
3. For any edge we actually hold (datacenter GPUs / TEE hw / genomics / comp-chem),
   re-cost the matching subnet (lium / Targon / Minos / NOVA) with real numbers.

## Folders (14 teardowns complete)
- `subnet-24-quasar/` — BASELINE (NO-GO), full teardown + method origin.
- `subnet-09-iota/`, `subnet_51/`, `subnet_64/`, `subnet_68/` (NOVA), `subnet-04-targon/`.
- `subnet-97-albedo/`, `subnet-101-tag101/`, `subnet-107-minos/`, `subnet-110-greencompute/`,
  `subnet-120-affine/`, `subnet-56-gradients/`, `subnet-67-harnyx/`.
- `subnet-129-nonexistent/` — proof SN129 is a btcli totals-row misread, not a subnet.
