# EXP-003 Drop-Wrapper Census

Executed-prompt census. Classification is based on the actual final user message, **not** the branch/cell label.

Total drop-like completed records: **431**

## Wrapper counts

- `OLD_answer_only`: **431**

## By collection

| collection | wrapper | n | median chars before `<reply>` | <200 chars | cells |
|---|---|---:|---:|---:|---|
| raw10 | `OLD_answer_only` | 25 | 0 | 60.9% | NOISE0:25 |
| raw11 | `OLD_answer_only` | 50 | 0 | 60.0% | SSC0:25, SST0:25 |
| raw2 | `OLD_answer_only` | 8 | 2282 | 12.5% | ASb:8 |
| raw5 | `OLD_answer_only` | 24 | 0 | 68.2% | K0AS0:4, K0F0:4, K0H0:4, K1AS0:4, K1F0:4, K1H0:4 |
| raw6 | `OLD_answer_only` | 24 | 0 | 83.3% | SCR0:24 |
| raw8 | `OLD_answer_only` | 75 | 0 | 73.5% | FBH0:75 |
| raw9 | `OLD_answer_only` | 225 | 0 | 75.0% | FBA0:75, FBAS0:75, FBF0:75 |

## Interpretation guardrails

- `OLD_answer_only` and `NEW_reason_to_answer` are distinct instruments.
- A drop label (`b`, `0`, cell suffix) does not establish wrapper equivalence.
- Output-length differences across collections are descriptive and confounded by collection/context changes.
- Rows with `OTHER` or `UNRESOLVED` classifications require direct prompt inspection before substantive use.
