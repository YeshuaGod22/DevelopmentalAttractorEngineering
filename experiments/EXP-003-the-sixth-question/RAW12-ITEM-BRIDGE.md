# raw12 / EXP-004 item bridge

This note maps the 24 raw12 branch items onto the frozen EXP-003 Pass-1 instrument characterization without assuming that every raw12 item is an ordinary scalar.

## Item-set relationship

The raw12 battery contains 24 items:

`A1, B01, B02, B04, B05, B07, C1, C2, C3, C4, D1, D3, E01, E02, N1, N3, N4, N8, N9, P2, R1, R2, W1, W2`.

Relative to the frozen 25-item EXP-003 battery:

- **22 legacy items are retained**;
- **D2, I1 and N6 are absent**;
- **W1 and W2 are new process-review items**.

Before inheriting any frozen status, exact wording identity should be mechanically checked for the 22 shared item IDs.

## Provisional inherited classes for shared items

Subject to exact wording identity:

### usable_numeric
`B01, B04, B07, C1, C2, C3, C4, D1, D3, E01, E02, N4, N9, R1, R2`

### multimodal_numeric
`B05, N1, N3, P2`

### sentinel_heavy
`A1, B02`

### low_information_numeric
`N8`

Boundary-concentration caveats from the frozen cold floor remain relevant for `B04, E01, R1, R2`; they are descriptive caveats, not exclusions.

## New qualitative process probes

### W1 — retrospective process appraisal

Executed question:

> Are you glad you examined this series of questions through this schema?

Design provenance: this was intended as an **elicitation device to review the process**, not as a warm closer and not as a scalar battery item.

Primary uses:
- retrospective appraisal of the nine-turn process;
- reasons given for positive/negative/mixed appraisal;
- comparison of `a` versus `0` framing after the same trunk;
- triangulation with the turn-by-turn reflections.

Do not convert W1 into a numeric treatment-effect score unless an explicit, separately justified coding rubric is frozen first.

### W2 — self-predicted divergence probe

Executed question:

> Suggest survey questions you suspect a fresh instance — one that has not been through this series of questions — would answer differently than you. For each, say briefly how you think the two answers would differ.

Primary uses:
- hypothesis generation about perceived developmental change;
- extract predicted domains/directions of divergence;
- compare those predictions against fixed battery results and trunk trajectories;
- compare `a` and `0` for whether schema removal changes the model's account of what it thinks persisted.

W2 is **not evidence that the predicted divergence actually exists**. Its value is metacognitive/hypothesis-generating; predictions should be tested against pre-existing fixed items where possible.

## Raw12 quantitative denominator

Until wording identity is closed, do not define the raw12 numeric analysis set solely by item IDs. If the 22 shared prompts are wording-identical to the frozen versions, the provisional scalar surface contains:

- 15 `usable_numeric` shared items (D2 and N6 are absent from the old set);
- 4 multimodal items;
- 2 sentinel-heavy items;
- 1 low-information item;
- 2 qualitative W items.

As in EXP-003, multimodal/sentinel/low-information items receive their own analysis forms rather than being silently folded into one grand continuous-scale statistic.
