# How to make money on Bittensor — validating vs mining vs delegating

> Synthesis as of **2026-06-30** (TAO ≈ $204). Combines the mining EV thesis in
> `README.md` with live validator/staking data pulled via `btcli` 9.23.1. Numbers
> reproduce from `tools/subnet_yield.py` + `data/2026-06-30-validator-snapshot/`.

## TL;DR
There are four ways to earn on Bittensor. Ranked by *who they actually suit*:

1. **Delegating (staking TAO to a validator)** — passive, no skill, no ops. You
   earn the subnet's emission APY minus the validator's take, **denominated in
   alpha that usually melts.** Net result ≈ emission yield − token depreciation.
   Only positive-inflow subnets clear that bar. **Best for: capital, no time.**
2. **Validating (running your own validator)** — keep the full emission share, but
   it's a **capital game**: income is stake-weighted and you compete with a pro
   cartel + owners. Permits are nearly free on thin subnets; *income* is not.
   **Best for: large capital + uptime + willingness to hold a subnet's alpha.**
3. **Mining** — do the subnet's work for emissions. Free entry drives marginal
   EV→0; **profit requires an edge** (cheap/owned compute, domain skill, or being
   early on a thin healthy subnet). **Best for: a real, specific edge.**
4. **Speculating on alpha** — buy a subnet token early, sell higher. This is what
   actually dominates returns in 1–3 (your payout *is* alpha). **Best for: nobody
   reading a research repo for "safe" yield; it's a directional bet.**

**The single most important fact:** in every mode your payout is alpha, so
**token health (price × net inflow) dominates the emission mechanics.** Only
**25 of 129 subnets** currently have positive net TAO inflow. Start there or
don't bother.

---

## Mode 1 — Delegating (passive staking)

**Mechanics.** Stake TAO to a validator on a subnet → your TAO buys that subnet's
alpha → you earn a pro-rata share of the validator emission pool, minus the
validator's take (commission, ~18% typical). You can unstake back to TAO (subject
to slippage on the alpha/TAO pool).

**The price-independence insight.** Because you buy alpha *and* earn alpha, the
emission yield is `validator_alpha_emission_per_day / total_validator_stake` and
the alpha price **cancels at entry**. So the headline APY is real *in alpha terms*
— but your **principal is now alpha**, and:

> **Net USD return ≈ emission APY + alpha price change over the holding period.**

High APY on a melting token is a trap. This is why `tao_flow_ema` (net TAO inflow,
the demand signal) matters more than APY.

**Live yields (2026-06-30, net of ~18% take):**

| SN | Name | net APY | net inflow | Owner cap | Read |
|---|---|---|---|---|---|
| 116 | Memo | ~111% | +0.00016 | 0% | open, weak inflow |
| 69 | ain | ~104% | **+0.00114** | 39% | strongest inflow of the batch |
| 16 | Fast Thinker | ~85% | +0.00090 | 99% | owner-captured |
| 82 | Compelle | ~69% | +0.00049 | 17% | decent inflow, low capture |
| 47 | EvolAI | ~68% | +0.00002 | 0% | open but inflow ~flat |
| 122 | CookingTAO | ~156% | +0.00036 | 43% | high APY, concentrated (3 vals) |
| 58 | greevils | **0%** | 0 | 0% | **dormant — emission off** |

**Realistic expectation.** These ~70–155% alpha-APYs are gross of price drift. On
a token with *strong* inflow, you keep most of it; on a flat/melting one you can
net zero or negative. The honest framing: delegating is a **leveraged bet on the
subnet's alpha**, wrapped in a high emission carry. Pick from the positive-inflow
list, prefer stronger inflow (ain > Compelle > Memo on that axis), and size it as
risk capital, not yield.

---

## Mode 2 — Validating (run your own validator)

**What you actually do.** Register a hotkey, stake alpha to it, run the subnet's
validator code (query miners → score → `set_weights` each tempo), keep uptime, and
maintain vTrust (weights must track Yuma consensus or get clipped to ~0 dividends).

**Permit vs. income (the core trap, and the answer to "is less stake needed on new
subnets?").**
- **Permit (right to set weights):** top `max_validators` (=64) neurons by stake.
  On thin/new subnets **fewer than 64 neurons hold any stake**, so the permit is
  effectively **free** — your hypothesis is correct here.
- **Income:** dividends are **stake-weighted among validators.** You compete with
  the multi-subnet pro cartel (tao.bot, Yuma/DCG, TAO.com, tao5, Rizzo, 1T1B.AI)
  plus, on most subnets, the **owner self-staking**. Clearing the permit by 1 α
  earns ~nothing.

**Capital to earn a target share** (≈ `share/(1−share) × total_val_stake × price`):

| SN | Floor to *appear* | Capital for ~5% of val emissions | Owner cap |
|---|---|---|---|
| 116 Memo | ~$8.3k | ~$114k | 0% ✅ |
| 69 ain | ~$15.7k | ~$324k | 39% |
| 82 Compelle | ~$7.3k | ~$50k | 17% |
| 47 EvolAI | ~$6.5k | ~$45k | 0% ✅ |
| 26 Perturb | ~$2.4M | n/a (owner = 100%) | 100% ❌ |

**When validating makes money:** you have **capital you want exposed to a specific
subnet's alpha anyway**, and the emission carry (~70–135% gross, no take) pays you
to hold it while you also help secure the subnet. It is **not** an edge-light way
to out-earn delegating unless you run your own validator at scale (saving the take)
and the token holds value. Avoid owner-captured sets (26, 16, 40) — you're diluting
against the owner.

**Best open validator targets (emitting + low owner-capture + positive inflow):**
**Memo (116)**, **Compelle (82)**, **EvolAI (47)**, and **ain (69)** for inflow.

---

## Mode 3 — Mining (do the work)

Full treatment in `README.md`. The thesis: mining is a **Tullock contest**
(`share = your_score / Σ scores`), free entry drives the marginal miner's EV→0, so
**profit requires an edge.** The dominant EV-killer observed across 14 teardowns is
**owners self-mining their own subsidy** (Minos 87.5%, NOVA both sides, iota's lone
earner = owner, Harnyx 64%).

**Edge → subnet map (mine only where you hold the edge):**
- Owned/cheap datacenter GPUs → lium (51), Chutes (64) *if compute is sunk/free*
- TEE hardware (Intel TDX / SEV-SNP) → Targon (4)
- Genomics / variant-calling → Minos (107)
- Computational chemistry / molecular-ML → NOVA (68)
- Frontier ML research → Albedo (97), Affine (120)
- Pure capital + automation → Tag101 (101)

**Highest-value cheap pilot (from README):** iota (9) — cheapest rig, healthiest
inflow; the one open question (can a fresh hotkey get credited when the owner runs
the orchestrator?) is only answerable empirically.

---

## Runnable on a CPU box (e.g. Oracle Ampere ARM, 24 GB, no GPU)

Most subnets require a **GPU validator** (to run reference models for scoring), and
many "healthy" thin subnets have **no published code** (fresh re-registrations —
see `subnet-58-greevils/`). Screening the 25 positive-inflow subnets for
**published + CPU-only validator code** leaves a short, real list:

| SN | Name | Validator HW (published) | net inflow | owner cap | net APY | $100 staked → /yr* | ARM caveat |
|---|---|---|---|---|---|---|---|
| 51 | lium / Compute | **CPU 4 cores / 8 GB** (verifies miners' GPUs) | **+0.01581** (#1) | 0% | ~34% | **~$34** | pure-Python, likely OK |
| 61 | RedTeam | CPU (evaluates code-challenge submissions) | +0.00161 | 0% | ~24% | ~$24 | pure-Python, likely OK |
| 10 | Sturdy/Swap | CPU (DeFi yield simulation) | +0.00198 | 0% | ~30% | ~$30 | chain name "Swap" ≠ repo "Sturdy" — verify not re-reg |
| 107 | Minos | CPU 4 cores / 8–16 GB (re-executes variant-calling) | +0.00123 | 66% ⚠️ | ~57% | ~$57 | **Docker genomics images are amd64 — likely NOT ARM-compatible** |

Ruled out (GPU-required, confirmed): Bitsec (60), iota/Pretraining (9); and by
type: Chutes (64), NOVA (68), NicheImage/Trishool (23), Condense/EvolAI (47).

\* **$100 is a *delegation* number, not a run-your-own-node number.** At $100 you
are far below every validator floor ($2.5k–$35k), so running your own validator
earns ~nothing and the Oracle box is irrelevant. To *use the box*, you need enough
stake (thousands+) to be a non-trivial validator. The $100 figures assume you
**delegate** to an existing validator; they are **gross of alpha price drift** — on
a melting token, subtract the drop. lium (51) has by far the strongest inflow, so
the best price support of the group.

**Reality check:** the CPU-runnable subnets pay **lower APY (24–57%)** than the
ultra-thin new ones (Memo 111%, ain 104%) — because they're established with more
validator stake diluting the pool. That's the trade: real code + healthy token +
lower risk vs. higher-but-unrunnable/unverifiable yield. For a CPU box with real
capital, **lium (51)** is the standout (CPU validator, healthiest token, 0% owner
capture, published). With only $100, just **delegate** to lium or RedTeam.

## Cross-cutting: the only screen that matters first

Token health gates everything. The 2026-06-30 positive-inflow list (25 of 129),
top by `tao_flow_ema`:

```
51 lium.io   +0.01581     9 iota      +0.01301    64 Chutes    +0.00608
68 NOVA      +0.00203    10 Swap      +0.00198    61 RedTeam   +0.00161
107 Minos    +0.00123    69 ain       +0.00114    83 CliqueAI  +0.00095
16 FastThink +0.00090   110 GreenComp +0.00088    96 Verathos  +0.00079
... (full list via: python tools/subnet_yield.py --screen)
```
Everything else (104 subnets) has **flat-to-negative inflow** = a melting payout.
The mining repo independently flagged the same melters (Gradients −0.0090, Affine
−0.0051, Targon −0.0046, Quasar −0.0040) — strong cross-validation.

## Decision guide
- **I have capital, no time, want yield:** delegate to a **positive-inflow** subnet
  (start: ain 69, Compelle 82, lium 51, iota 9). Treat APY as a carry on a
  directional alpha bet, not a savings rate. Size as risk capital.
- **I have serious capital + can run infra:** validate **Memo (116) / Compelle (82)
  / EvolAI (47)** (owner doesn't capture), or any healthy subnet whose alpha you're
  willing to hold. Save the take by running your own validator.
- **I have a real edge (compute/skill):** mine the matching subnet, be early on a
  thin *healthy* one. Pilot **iota (9)** cheaply first.
- **I have none of these:** hold/stake TAO at the root level for the base emission;
  don't expect subnet alpha to beat it after melt.

## What would change these conclusions
1. A subnet appearing with **strong** positive inflow **and** low owner-capture
   **and** a low floor — re-run the screen weekly; this is the GO profile.
2. Confirmed **validator commissions** (we assumed 18%) and **max_validators** per
   subnet (confirmed 64 for the batch).
3. Real **alpha price trajectories** — the dominant term in every mode's USD return
   and the one this snapshot cannot predict.

---
*Reproduce: `tools/subnet_yield.py` over `data/2026-06-30-validator-snapshot/`.
Refresh data per `tools/README.md` (WSL + btcli).*
