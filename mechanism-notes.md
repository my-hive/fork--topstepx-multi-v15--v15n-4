# v15n-4 explorer notes

Stopped after eight recorded non-improving screens. No candidate achieved positive `dev_score`.

| Rank | Mechanism | Symbols | Dev score | Era PnL |
|---|---|---:|---:|---|
| 1 | MES afternoon continuation of cash-session impulse | MES | 0.000000 | -3547, -1223, -1226 |
| 2 | ES opening impulse continuation, one-hour hold | ES | 0.000000 | -30003, -68750, -55500 |
| 3 | ES/NQ causal lead-lag | ES,NQ | 0.000000 | -657898, -1194060, -1220558 |

All screens used `--null-seeds 0 --mode dev`; null p is unavailable by protocol. No 20/200-seed nulls, no sealed submissions. MES afternoon mechanism had least-negative cross-era PnL but fails every block; do not advance unchanged.
