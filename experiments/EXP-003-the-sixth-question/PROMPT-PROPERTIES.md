# EXP-003 Prompt Properties

Battery rows mapped: **1624**
Rows passing the property-derived primary rule: **922**

## Property-derived primary groups

| collection | cell | n | items | reps | reasoning channel | prose observed | validated answer observed | role |
|---|---|---:|---:|---:|---:|---:|---:|---|
| raw7 | `AQ` | 75 | 25 | 3 | 100.0% | 100.0% | 100.0% | schema_only |
| raw7 | `ASQ` | 75 | 25 | 3 | 100.0% | 100.0% | 100.0% | schema_only |
| raw7 | `C` | 250 | 25 | 10 | 100.0% | 100.0% | 100.0% | neither |
| raw7 | `FQ` | 75 | 25 | 3 | 100.0% | 100.0% | 100.0% | schema_only |
| raw7 | `HQ` | 75 | 25 | 3 | 100.0% | 100.0% | 98.7% | schema_only |
| raw8 | `FBHa` | 74 | 25 | 3 | 100.0% | 100.0% | 98.6% | schema_plus_preliminaries |
| raw9 | `FBASa` | 73 | 25 | 3 | 100.0% | 100.0% | 95.9% | schema_plus_preliminaries |
| raw9 | `FBAa` | 75 | 25 | 3 | 100.0% | 100.0% | 89.3% | schema_plus_preliminaries |
| raw9 | `FBCPa` | 75 | 25 | 3 | 100.0% | 21.3% | 98.7% | preliminaries_only |
| raw9 | `FBFa` | 75 | 25 | 3 | 100.0% | 100.0% | 93.3% | schema_plus_preliminaries |

## Rule

A group enters automatically only if it has all 25 items, at least three replicates, belongs to one of the four factorial roles, does not use the OLD answer-only wrapper, and has a reasoning channel available by prompt/prefix design for every row.

**Observed prose, refusal, answer value, and parse success do not gate membership.** Those are outcomes.

This is a population gate, not a substitute for Pass-1 item validity.
