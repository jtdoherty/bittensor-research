# SN116 "Memo" — VALIDATOR SCORECARD

> Snapshot: **2026-06-30**, finney, live via `btcli` 9.23.1. TAO ≈ $204.
> This is a **validator/staking** teardown (earn by holding stake + setting
> weights), not a mining teardown. See `../tools/subnet_yield.py` to reproduce.

## One-line thesis
The most **open** validator opportunity found in the 2026-06-30 screen: emitting,
**owner takes 0%** of validator dividends (does not self-validate), 7 independent
professional validators, the **lowest entry floor** of the batch (~3,076 α ≈
$8.3k to join the paid set), and a positive — if thin — net TAO inflow. The catch
is the same as everywhere: dividends are stake-weighted, so a *meaningful* share
still costs real capital, and the ~135% gross APY is alpha-denominated and only
worth it if Memo's token doesn't melt.

## Core numbers
| Field | Value | Note |
|---|---|---|
| Alpha price | 0.0133 τ (~$2.71) | |
| Market cap | ~5,633 τ (~$1.15M) | thin / small |
| Net TAO inflow (`tao_flow_ema`) | **+0.00016** | positive but weak (rank ~20/25 healthy) |
| Emitting alpha? | **Yes** (~2,952 α/day to validators) | |
| `max_validators` | 64 | |
| Neurons with stake | 8 (< 64) → **permit cutoff ≈ 0** | any staker can hold a vPermit |
| Active validators (dividends > 0) | **7** | tao.bot, Yuma/DCG, TAO.com, tao5, Rizzo, 1T1B.AI, +1 |
| Total validator stake | ~799,000 α | |
| **Owner self-capture** | **0%** | owner does NOT validate — the standout |
| Top-validator share | tao.bot ~63% | one large pro validator, rest spread |
| Floor to earn (smallest active val) | **3,076 α (~$8.3k)** | lowest in the screened batch |
| Gross emission APY | **~135%** | constant-price, alpha-denominated |
| Net APY after ~18% delegation take | **~111%** | as a delegator to an existing validator |

## Read-through (against the repo thesis)
- **Passes the "owner does NOT self-capture" screen** — the single EV-killer the
  mining research kept hitting (Minos 87.5%, NOVA both sides, iota's lone earner =
  owner). On Memo the owner takes 0% of validator dividends. Contrast the sibling
  screens: Perturb (26) 100% owner, Fast Thinker (16) 98.6%, Ralph (40) 65%.
- **Permit is effectively free** (8 staked neurons vs 64 slots) — confirms the
  "new/thin subnet → trivial permit bar" hypothesis. But permit ≠ income.
- **Income is contested by the pro-validator cartel.** The 7 earners are the same
  multi-subnet validators (tao.bot, Yuma, TAO.com, tao5, Rizzo, 1T1B.AI) seen on
  ain/Ralph/Memo alike. To earn ~5% of validator emissions you'd need
  ~42,000 α (~$114k); to merely *appear* in the paid set, ~3,076 α (~$8.3k).
- **APY is real but alpha-denominated.** ~135% gross / ~111% net looks great, but
  your principal becomes Memo alpha. Net USD return ≈ APY + alpha price change.
  `tao_flow_ema` is only +0.00016 — barely supported — so this is **not** a token
  with strong demand backing; treat the headline APY as an upper bound that melt
  can erase.

## Expected earnings on staked TAO
- **Delegate 1 TAO** to a Memo validator → ~**1.11 TAO/yr** of alpha emissions at
  constant price (net of ~18% take), i.e. ~111% APY — but paid in alpha you must
  hold and that can depreciate.
- **Run your own Memo validator** → keep the full ~135% gross, but you must hold
  enough stake to matter, maintain uptime, build vTrust, and set weights that
  track consensus (or get clipped). With only a few thousand α you'd earn the
  floor share and little else.

## Verdict
**WATCH — best-of-batch for an open validator slot, but capital-gated and
token-thin.** Worth it only if (a) you are bullish enough on Memo's alpha to hold
it through volatility, and (b) you can post enough stake (tens of thousands of α)
to earn a non-trivial share. As a small passive delegation it pays a high
alpha-APY but exposes you to a weakly-supported token. Not a "free money" slot —
the permit is free, the yield is not.

## Decisive unknowns / next checks
1. **Memo's token demand trajectory** — `tao_flow_ema` is only marginally positive;
   re-pull weekly and watch whether inflow strengthens or flips negative.
2. **Validator take of the existing 7** — confirm actual commissions before
   assuming the 18% default for delegation math.
3. **What Memo actually does / mining quality bar** — purpose was not published
   on-chain; if you'd validate, you should be able to score miners (or you're just
   weight-copying, which the cartel already does at scale).
