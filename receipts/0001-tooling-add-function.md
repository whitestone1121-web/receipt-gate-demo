# 0001-tooling-add-function

## Compared
- branch: `agent/add@demo`
- baseline: `main@demo`
- date: `2026-07-02`

## Change summary
Agent added the add() function with tests.

## Metric delta
| Metric | Baseline | Branch | Delta |
|---|---|---|---|
| tests passing | 0 | 2 | +2 |

### How measured
```bash
python3 -m pytest tests/test_calculator.py -q
```

## Verdict
`improvement`

## Confidence
0.9

## change_class

tooling
