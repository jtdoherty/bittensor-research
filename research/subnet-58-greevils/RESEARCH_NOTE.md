# SN58 "greevils" — RESEARCH NOTE

> Snapshot: **2026-06-30**, finney, live via `btcli` 9.23.1. Verdict: **NO-GO / skip.**

## One-line
Netuid 58 currently resolves on-chain to **"greevils"**, a **dormant, freshly
re-registered** subnet with **emission disabled** (burn mode) — nothing to mine,
nothing to validate, nothing to earn. Public registries/repos still point to the
*previous* occupants of the slot, so there is also **no discoverable code**.

## On-chain facts (authoritative)
| Field | Value |
|---|---|
| Name | greevils |
| Registered | ~block 8,511,017 → **~2026-06-29** (≈1 day old at snapshot) |
| Emission | **0** — `emission_enabled = false`, recycle = **Burn** |
| Alpha price | ~0.0069 τ (~$1.40) on ~0 volume (illiquid) |
| Alpha staked | **0** (`total_staked_alpha = 0`); everything still in AMM reserve |
| Neurons | ~50 (mostly empty) |
| "Validators" (dividends>0) | 2 (1T1B.AI, Rizzo) — earning ~0 because emission is off |
| Owner self-capture | 0% (owner not validating) |
| Net TAO inflow | ~0 |

## The identity problem (why you can't find its code)
Netuid 58 has been **recycled**. Depending on the source you get a different
subnet, because they lag the chain:
- **Live chain (today):** "greevils" — no published repo, empty on-chain identity.
- **taostat registry:** "Dippy Speech" (impel-intelligence/dippy-speech-subnet) — a
  GPU speech-model subnet; the *previous* occupant.
- **Older web index:** "HS58 / DRAIN Protocol" (Handshake58/HS58-subnet) — an even
  earlier occupant, a CPU HTTP-probe/consensus scorer.

None of these match the current on-chain occupant. There is **no verifiable
validator or miner code for "greevils"** in public sources as of the snapshot.

## Why it's a skip (all four hold)
1. **No published code = flying blind.** Can't run a validator/miner whose scoring
   logic, deps, and requirements you can't find. Likely private/unpublished.
2. **Dormant — emission is OFF (burn mode), 0 alpha staked.** Even with the code,
   payout is zero right now.
3. **Lineage is GPU-heavy.** Prior occupants (Dippy Speech = speech model, and the
   Condense-AI-style workloads seen in neighboring recycled slots) require GPU
   validators — a CPU-only box couldn't validate that class anyway.
4. **Re-registration is a red flag.** High churn + elevated deregistration risk: a
   recycled slot can be recycled again, taking your registration/stake with it.

## Decision
**Do not mine or validate SN58.** Revisit only if it (a) turns emission on, (b)
publishes code, and (c) survives long enough to shed the churn risk. Until then it
is a name on an empty pool. For a CPU box, see the runnable alternatives in
`../HOW_TO_MAKE_MONEY_ON_BITTENSOR.md` (CPU-only validator shortlist: lium 51,
RedTeam 61, Sturdy/Swap 10).

*Data: `../data/2026-06-30-validator-snapshot/sn58.json`.*
