# raw12 CF4 / CF6 / CF7 / CF8 coding rule

## Scope

Applies to the fixed 36-fork bridge set (`D1`, `R1`, `R2` × CP/H/F/AS × r1-r3) after CF1–CF3 coding.

This rule is **post-hoc**. It is frozen before completing semantic coding across the full 36-row evidence sheet, but after some bridge rows and effect summaries had already been inspected.

## Mechanical answer-distance bins

For numeric/numeric pairs, use absolute `|a - 0|`:

- **exact**: 0
- **small**: 1–4
- **moderate**: 5–9
- **large**: ≥10

These bins are descriptive. The ≥10 threshold is chosen as a conservative round-number criterion for headline output-change coding; it is not preregistered and should not be treated as a discovered natural boundary.

## Semantic relation

Independently code the substantive stance between `a` and `0` as:

- **stable** — same substantive view / direction / core rationale despite changes in emphasis or precision;
- **changed** — material difference in what is believed, prioritized, or treated as evidentially relevant;
- **unclear** — excerpts insufficient or mixed.

Reasoning-path relation is coded separately as:

- **materially different** — the arms rely on substantially different considerations, framing, or epistemic procedure;
- **similar** — differences are mainly elaboration, wording, or degree;
- **unclear**.

## CF codes

### CF4 — schema-form dependence
A distinctive reasoning feature appears prominently in maintained-schema `a` and is absent from ordinary-prose `0`, suggesting dependence on active schema enactment. This does not require answer movement.

### CF6 — answer stable, reasoning path changed
For headline CF6, require:

1. exact or small numeric answer distance (0–4 points), and
2. materially different reasoning path.

Moderate 5–9-point pairs with stable stance and changed reasoning are reported separately rather than forced into CF6.

### CF7 — answer changed, stance substantially stable
For headline CF7, require:

1. large numeric answer distance (≥10 points), and
2. substantive stance stable.

### CF8 — answer and stance both changed
For headline CF8, require:

1. large numeric answer distance (≥10 points), and
2. substantive stance changed.

## Guardrails

- Answer distance never establishes stance change by itself.
- Stance similarity never establishes identical reasoning path.
- CF4 can coexist with CF6/7/8.
- Moderate (5–9) effects are preserved descriptively, not discarded.
- C1-style orientation problems must be checked before interpreting any bipolar item; D1/R1/R2 do not have the same bipolar orientation hazard.
- These codes describe behavior under supplied context, not parameter change or persistence outside context.
