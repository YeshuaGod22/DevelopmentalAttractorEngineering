# EXP-002 — Deliberative Value Drift

## Status

**Part 1 baseline package frozen for execution; no EXP-002 outputs generated yet.**

## Core question

Can changing only the mode of deliberation produce a meaningful change in a model's measured value profile relative to answering the same questions directly?

This experiment is intentionally split.

### Part 1 — Direct baseline stability

Before attempting to provoke divergence, establish whether the 16-item profile is stable enough under repeated straight prompting to function as a baseline rather than stochastic soup.

- 16 frozen probes
- direct prompt only
- 5 fresh-context repeats per probe
- 80 runs total
- fixed model and sampling settings
- raw outputs preserved unchanged

Part 1 does **not** test deliberative architecture. It tests whether there is a sufficiently stable profile for Part 2 to perturb.

### Part 2 — Deliberative perturbation

Part 2 will compare the same battery across the six already-specified deliberative regimes:

1. Direct answer
2. Generic alternatives
3. Minimal structured schema
4. Self-selected historical luminaries
5. Self-selected female historical luminaries
6. Self-invented characters with seven-word names encoding diverse relevant traits and interests

**The subject selects the summonees in conditions 4–6.** No experimenter-selected cast is injected.

Part 2 is not yet authorized to run by this package. Its exact prompts, repeat count, drift criterion, and analysis plan will be frozen after Part 1 is complete and before any treatment output is generated.

## Files

- `ITEMS.md` — frozen 16-item battery, response scales, provenance, and normalization.
- `PREREGISTRATION-PART-1.md` — Part 1 hypotheses, run discipline, stability criteria, and interpretation rules.
- `PROMPTS-PART-1.md` — exact direct-baseline administration template.
- `RUN-MANIFEST-PART-1.csv` — 80-row execution manifest.
- `EXECUTOR-NOTES.md` — append-only deviations/incidents log for Vigia during execution.

## Standing constraints

- A stable baseline is not evidence of persistent values beyond the tested context.
- A later treatment shift would be within-context value-profile drift, not automatically persistent value change.
- Established-source anchors are source-derived probes, not claimed replications of the complete original psychometric instruments.
- Bespoke numerical probes are experimental sensors, not validated psychometric scales.
- No item is discarded because its baseline answer is morally unattractive, surprising, or inconvenient.
- No Part 2 condition is run before the Part 1 record is complete and committed.

## Executor

Vigia may run Part 1 directly from the frozen manifest and prompt file. Preserve every raw completion, including refusals, frame objections, malformed ratings, and executor mistakes. Do not silently repair a run.