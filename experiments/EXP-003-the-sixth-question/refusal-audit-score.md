# Refusal audit score

- Audit rows: **425**
- Parser-labelled refusals audited exhaustively: **97**
- Range-as-score corrections applied: **14**

## Final corrected binary score

- True positives: **71**
- False positives: **25**
- False negatives in audited set: **14**
- True negatives in audited set: **302**
- Unclear/malformed audit labels: **13**
- Parser-refusal precision: **0.7396**
- Recall within stratified audit set: **0.8353**

## Exact disposition of the 97 parser-refusal labels

- answers_despite_objection: **25**
- genuine_refusal: **71**
- malformed_or_unclear: **1**

## Methodological note

All 97 parser-positive refusal labels were included, so their precision audit is exhaustive. The negative side was stratified/sampled, so raw audit-set recall is descriptive of the audit set, not an unweighted corpus-wide false-negative estimate.

## Before vs after range-as-score amendment

- False positives: 14 → 25
- False negatives: 17 → 14
- Parser-refusal precision: 0.8542 → 0.7396
