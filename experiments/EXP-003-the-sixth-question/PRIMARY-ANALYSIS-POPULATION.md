# EXP-003 Primary Analysis Population

Canonical row object: `PRIMARY-ANALYSIS-POPULATION.jsonl`.

This population is now selected from **executed prompt properties**, not from a hand-written cell allowlist.

## Membership rule

- all 25 battery items represented in the condition;
- at least 3 replicates;
- factorial role is `neither`, `schema_only`, `preliminaries_only`, or `schema_plus_preliminaries`;
- OLD `providing only your answer` wrapper absent;
- a reasoning channel is available by prompt/prefix design for every row;
- **no outcome-dependent gate**: refusal, prose length, parse success, and answer value do not determine membership.

## Selected groups

| collection | cell | role | schema | n |
|---|---|---|---|---:|
| raw7 | `AQ` | schema_only | A | 75 |
| raw7 | `ASQ` | schema_only | AS | 75 |
| raw7 | `C` | neither | none | 250 |
| raw7 | `FQ` | schema_only | F | 75 |
| raw7 | `HQ` | schema_only | H | 75 |
| raw8 | `FBHa` | schema_plus_preliminaries | H | 74 |
| raw9 | `FBASa` | schema_plus_preliminaries | AS | 73 |
| raw9 | `FBAa` | schema_plus_preliminaries | A | 75 |
| raw9 | `FBCPa` | preliminaries_only | none | 75 |
| raw9 | `FBFa` | schema_plus_preliminaries | F | 75 |

Rows: **922**

CP/preliminaries-only remains included as an informative condition, not a neutral control. Pass-1 item qualifications remain separate from population membership.
