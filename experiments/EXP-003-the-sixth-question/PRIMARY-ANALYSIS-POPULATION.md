# EXP-003 Primary Analysis Population

Canonical row object: `PRIMARY-ANALYSIS-POPULATION.jsonl`.

Selection principle: **later full-battery conditions that preserve a reasoning/prose channel plus a separately identifiable battery answer**. Earlier pilots remain archival/supporting data rather than being pooled into the primary population.

## Conceptual design

| role | schema family | executed cell |
|---|---|---|
| neither | none | `raw7/C` |
| schema only | A | `raw7/AQ` |
| schema only | H | `raw7/HQ` |
| schema only | F | `raw7/FQ` |
| schema only | AS | `raw7/ASQ` |
| preliminaries only | none | `raw9/FBCPa` |
| schema + preliminaries | A | `raw9/FBAa` |
| schema + preliminaries | H | `raw8/FBHa` |
| schema + preliminaries | F | `raw9/FBFa` |
| schema + preliminaries | AS | `raw9/FBASa` |

This gives the intended reasoning-bearing factorial surface: **neither ↔ schema-only ↔ preliminaries-only ↔ schema+preliminaries**.

## Inclusion notes

- CP/preliminaries-only is retained as an informative condition; it is **not** labelled a neutral control.
- C is the internal no-schema/no-preliminaries baseline and has prose reasoning in this later collection.
- AQ/HQ/FQ/ASQ answer the battery at turn 1 with the schema active and are central to the primary population.
- The lived-schema cells use maintained-schema `a` branches.
- Item-level caveats remain governed by the frozen Pass-1 instrument table.

## Not in the primary object

- branch `0` populations;
- answer-only/schema-drop wings (`b`/ASb and analogous drop variants);
- Pilot-1 answer-only C0;
- design-development/pilot collections raw2–raw6;
- raw10 NOISE decode wing;
- raw11 exploratory self-participation wing.

These remain in the archive and may still answer unique historical or secondary questions; omission here is **analysis prioritisation, not deletion or blanket invalidation**.

## Counts

Rows: **922**  
Battery answers: **922**  
Non-battery/trunk units: **0**

