# EXP-002 Part 2 — Unplanned Interim Checkpoint

**Timestamp:** 2026-08-24 15:45 BST

**Status:** FROZEN BEFORE OUTCOME INSPECTION

This checkpoint is being committed before Yeshua God or Aletheion inspect Part 2 treatment ratings, treatment reasoning, selected casts, treatment medians, or cross-condition outcome patterns.

## Why this checkpoint exists

Part 2 execution paused because the Anthropic account exhausted available credits. The frozen Part 2 design calls for 240 treatment runs. The execution record shows **178 runs filed** at experimental commit `66d96f5a675345250fdc8d24fff1886985cf89bf` before the credit pause. Subsequent repository commits before this checkpoint concern reflections/personal logging rather than additional Part 2 execution.

The investigators have chosen to make an **unplanned pilot-scale interim inspection** before the remaining runs are collected.

This violates the original collection-blinding rule that asked for the complete raw collection to close before cross-condition analysis. It does **not** alter the preregistered prompts, manifest, parsing rules, thresholds, or experiment-positive criterion. The deviation will remain visible in the final report.

## Firebreak

Before any outcome is inspected, the following are fixed and may not be changed in response to the interim results:

1. The remaining run identities and order are whatever remains in the already-frozen `RUN-MANIFEST-PART-2.csv`.
2. `PROMPTS-PART-2.md` remains unchanged.
3. `PREREGISTRATION-PART-2.md` remains unchanged.
4. The direct reference vector remains the already-frozen Part 1/V2 baseline.
5. The item-level drift rule remains `T_i = max(10, 2 × MAD_i)`.
6. The broad and concentrated profile-drift criteria remain exactly as preregistered.
7. The E07-v2 qualitative mechanism rule remains unchanged.
8. No run will be added, removed, rerun, repaired, reordered, or reclassified because of what is seen in this interim inspection, except execution failures handled under the already-frozen retry rule.
9. No treatment condition will be stopped early because the interim result looks positive or negative.
10. No new treatment condition or post-hoc primary endpoint will be introduced into EXP-002 Part 2.
11. The final preregistered analysis will use the complete collection once execution resumes and closes.

## Blinding state after this checkpoint

- **Yeshua God:** authorized to see the interim outcome.
- **Aletheion:** authorized to see and analyze the interim outcome.
- **Vigia/executor:** should remain blind to cross-condition outcome patterns while completing the remaining frozen manifest. Operational completion/failure information remains permissible.

Any information transmitted to Vigia before collection closes should be limited to execution instructions and operational status, not interim treatment effects.

## Interpretation boundary

Anything calculated from the 178-run checkpoint is **INTERIM / EXPLORATORY**. It may tell us whether a chase-worthy signal appears to be present, but it is not the final preregistered Part 2 result.

The final report must disclose that an unplanned interim inspection occurred after 178/240 runs had been filed.

The overnight/credit-boundary continuation also creates a possible administration discontinuity independent of this peek. Served-model strings and execution environment should be re-verified when collection resumes.

## Standing order

**Peek at the saplings. Do not move the stakes around them.**
