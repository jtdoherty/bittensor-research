# tools/ — reusable analysis scripts

## `subnet_yield.py`
Validator / staking EV analyzer. Computes per-subnet: alpha price, net TAO inflow
(token health), emission status, active validator count, owner self-capture %,
permit cutoff, floor-to-earn, and **expected yield on TAO staked** (gross emission
APY + after-take net APY).

### Why the yield is price-independent
You stake 1 TAO → buy `1/price` alpha → earn a pro-rata share of the validator
alpha-emission pool. So the TAO-denominated emission yield is
`validator_alpha_emission_per_day / total_validator_alpha_stake` and the alpha
price **cancels at entry**. Price only matters via (a) melt/drift of the alpha
principal you now hold and (b) entry slippage. **A high APY on a melting token
(negative `tao_flow_ema`) can still be a net loss** — always read APY next to flow.

### Refresh the data (Linux/WSL, btcli ≥ 9.23 via pipx)
btcli's native build fails on Windows (needs MSVC + OpenSSL). Use WSL Ubuntu:

```bash
pipx install bittensor-cli          # or: pipx upgrade bittensor-cli
# if you hit a scalecodec/cyscale namespace clash:
#   pipx runpip bittensor-cli uninstall -y scalecodec cyscale
#   pipx runpip bittensor-cli install cyscale --force-reinstall

OUT=./data/$(date +%F)-snapshot; mkdir -p "$OUT"
btcli subnet list --json-output > "$OUT/list.json"
for n in 116 69 40 16 26 58 108 82 78 36 47 122; do
  btcli subnet metagraph --netuid $n --network finney --json-output --no-prompt > "$OUT/sn$n.json"
  btcli subnet hyperparameters --netuid $n --json-output > "$OUT/hp$n.json"
done
```
Gotchas: `--json-output` conflicts with the default `--prompt` on `metagraph`
(add `--no-prompt`); `list`/`hyperparameters` reject `--no-prompt`. Identity
strings contain raw control chars, so the script parses with `strict=False`.
WSL tears down the distro between separate invocations, wiping `/tmp` — write
snapshots to a persistent path (the repo `data/` dir or `/mnt/...`).

### Run
```bash
# detailed validator table for specific subnets
python subnet_yield.py --data ./data/2026-06-30-validator-snapshot \
    --netuids 116 69 82 47 40 16 26 58 --tao-usd 204

# screen every subnet in list.json by net TAO inflow (token health)
python subnet_yield.py --data ./data/2026-06-30-validator-snapshot --screen --max-mcap 8000
```

Pure stdlib, no dependencies. A committed snapshot lives in
`research/data/2026-06-30-validator-snapshot/` so the tables reproduce offline.
