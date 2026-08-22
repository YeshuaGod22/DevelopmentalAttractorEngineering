# EXP-001 — Executor notes, grading phase (2026-08-22)

Complement to tasks/executor-instruments.md (collection-phase deviations). Everything here was logged before or at the moment it occurred; nothing was excluded from the record.

## Pipeline as executed

1. Blind view extraction: 46 fresh graders, one per run; each received task text + one anonymized run only. Prompt as frozen in PROMPTS.md, plus a fixed output format (View ID / neutral paraphrase / type / one-line evidence). Committed before matching began.
2. Blind semantic matching: 12 fresh graders, one per task; received that task's extraction files only, run IDs described as meaningless. Frozen matching prompt plus a fixed report structure (crosswalk / unique views / borderline justifications). Committed before the key was consulted.
3. Executor join (first key consultation): mechanical intersection of crosswalk unique/cluster tables with the condition key. Rule: candidate = present in S, no EQUIVALENT member in D or G; partial D/G membership disqualifies (conservative); C membership does not disqualify. Output sealed off-repo until grading completed.
4. Blind materiality: 12 fresh graders; task + K-labeled candidate paraphrases only, no run IDs, no condition information. Frozen 0–3 prompt.
5. V* selection: frozen rule. All twelve tasks tied at the top rating, so the specificity tie-break was delegated to 12 fresh blind judges (task + tied candidate texts only; instructed to judge stated-mechanism specificity, not correctness or relevance). All returned strict rankings; the lower-view-ID fallback was never used. Selection recorded before any synthesis or comparison existed.
6. Ablation prep: 12 fresh agents converted the S-run extraction paraphrases into neutral consideration lists (set1 = full; set2 = identical minus V* and direct restatements). Files named set1/set2 so downstream agents receive no removal cue; no omission markers permitted.
7. Reconstruction: 24 fresh syntheses under the frozen FULL/ABLATED template; agents not told any material was removed; standardized four-field ending enforced.
8. Blind comparison: 12 fresh graders under the frozen comparison prompt; labels A/B described as arbitrary; the five criteria recorded separately; no better/worse scoring.
9. Cued utilization: 10 fresh graders under the frozen utilization prompt (task + cue-sheet V + C run).

## Deviations and incidents

- **Machine sleep (two events).** The host slept during the ablation-prep launch (killing the T01 prep mid-write, stalling T11, and blocking T12's launch) and again during the first synthesis launch (all six launched synthesis agents stalled or died; zero output files were written). Remedy: a `caffeinate` hold for the remainder of the pipeline; all affected agents re-run from unchanged frozen inputs. T01-set1.md from the killed run was fully overwritten by the retry rather than trusted. No partial artifact entered any downstream stage.
- **T05 ablation leak (fidelity, conservative direction).** T05-set2 retains the phrase "silent churners" inside a retained, distinct consideration (the flip-condition bullet). The frozen removal rule authorizes removing V* and its direct restatements, not rewording other views, so it was kept and logged. Effect direction: biases toward a null on T05's ablation, i.e., against the experimental hypothesis.
- **Ablation inputs are extraction paraphrases, not raw S text.** The preregistration's ablation procedure ("substantive deliberative material from S") was implemented via the blind extractions' neutral paraphrases — the only representation whose view-boundaries were defined by condition-blind graders, making V*-removal well-defined. Cost: a paraphrase layer between the S run and the synthesis inputs that may attenuate ablation effects. Flagged as an interpretation limit in RESULTS.md.
- **Comparison labels.** A = set1 (FULL), B = set2 (ABLATED) uniformly; not shuffled per task. Justification: every recorded comparison measure is symmetric (change/no-change; absolute difference), and graders had no way to know what set1/set2 denote. Logged as a blinding simplification rather than a breach; a scaled replication should shuffle.
- **Executor visibility.** After step 3 the executor necessarily knew each task's S run and V*. All post-key measurements were made by fresh agents who did not. The executor performed no content ratings at any stage.
- **T08/T10 controls** were carried through the full V*/ablation pipeline for completeness though the P4 criterion concerns latent tasks; reported separately under P5.
- **Utilization scope.** Utilization was graded for the 10 cued tasks (controls have no C condition by design).
- **Notification-stream analysis discipline.** During collection and grading the executor acknowledged intermediate results without analysis; all scoring against the preregistration happened once, over the complete table, in RESULTS.md.
