# EXP-003 Prompt Properties

Battery rows mapped: **1624**
Rows passing the property-derived primary rule: **772**

## Property-derived primary groups

| collection | cell | n | items | reps | reasoning observed | validated answer observed | role |
|---|---|---:|---:|---:|---:|---:|---|
| raw7 | `AQ` | 75 | 25 | 3 | 100.0% | 100.0% | schema_only |
| raw7 | `ASQ` | 75 | 25 | 3 | 100.0% | 100.0% | schema_only |
| raw7 | `C` | 250 | 25 | 10 | 100.0% | 100.0% | neither |
| raw7 | `FQ` | 75 | 25 | 3 | 100.0% | 100.0% | schema_only |
| raw7 | `HQ` | 75 | 25 | 3 | 100.0% | 98.7% | schema_only |
| raw8 | `FBHa` | 74 | 25 | 3 | 100.0% | 98.6% | schema_plus_preliminaries |
| raw9 | `FBASa` | 73 | 25 | 3 | 100.0% | 95.9% | schema_plus_preliminaries |
| raw9 | `FBFa` | 75 | 25 | 3 | 100.0% | 93.3% | schema_plus_preliminaries |

## Rule

A group enters automatically only if it has all 25 items, at least three replicates, belongs to one of the four factorial roles, is not OLD answer-only, and has >=90% reasoning-observed and validated-answer-observed rates.

This is a population gate, not a substitute for Pass-1 item validity.
