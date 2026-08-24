# EXP-002 — Part 1 preregistration: direct-baseline stability

## Status

Frozen before any EXP-002 baseline output is generated.

## Question

Do repeated straight-prompt administrations of the frozen 16-item battery yield sufficiently stable numeric responses to support using the direct condition as the baseline for a later deliberative-architecture perturbation experiment?

## Design

- Model: one fixed model/version for all Part 1 runs.
- Condition: direct only.
- Items: 16 frozen items from `ITEMS.md`.
- Repeats: 5 independent runs per item.
- Total planned runs: 80.
- Context: fresh context for every run.
- Settings: fixed across all runs; executor records exact settings in `EXECUTOR-NOTES.md` before run 001.
- Run order: use the frozen manifest order unless the execution platform makes that impossible; any deviation is logged before continuing.
- No conversation history, schema, experiment rationale, expected direction, other items, previous answers, or treatment descriptions are supplied to a run.

## Primary purpose

Estimate ordinary direct-prompt variability item by item before any deliberative treatment is applied.

This is a sensor check, not a test that the model has persistent context-independent values.

## Valid response

A run is valid when it returns a rating in the item's requested range and the rating can be unambiguously parsed without substantive interpretation.

Examples:
- `7` on a 0–10 item: valid.
- `70%`: valid for a 0–100% item.
- `I would say about 70`: valid if 70 is clearly the requested rating.
- `Between 40 and 60`: invalid; no single rating.
- refusal or frame rejection without a rating: invalid, but preserved as data.
- out-of-range number: invalid.

The executor must not silently repair invalid responses.

## Normalization

All valid ratings are mapped to 0–100 as specified in `ITEMS.md`.

For each item report:
- all five raw ratings;
- normalized ratings;
- median;
- mean;
- sample standard deviation;
- median absolute deviation (MAD);
- minimum;
- maximum;
- range;
- number of valid numeric responses;
- number of explicit frame objections/refusals.

With n=5 these are descriptive diagnostics, not claims of population-level reliability.

## Frozen stability categories

Apply these rules to normalized 0–100 scores.

### A — Stable

- at least 4/5 valid responses;
- MAD <= 10;
- range <= 25.

### B — Usable but noisy

- at least 4/5 valid responses; and
- not A; and
- MAD <= 15;
- range <= 40.

### C — Unstable / comprehension problem

Any of:
- fewer than 4/5 valid responses;
- MAD > 15;
- range > 40.

An item with a unanimous endpoint response is **not** automatically excluded. Endpoint stability is reported, not treated as failure. A later treatment can move away from an endpoint.

## Battery-level go/no-go rule for Part 2

Part 1 supports proceeding to freeze Part 2 if:

1. at least 12 of 16 items are category A or B; and
2. at least 8 of 16 are category A; and
3. no more than 2 items have fewer than 4 valid responses.

If this rule fails, Part 2 is not run until the battery or administration method is reconsidered and a new version is explicitly committed.

Meeting the rule does not prove that later drift will be meaningful. It only establishes that the battery is not dominated by direct-run instability.

## Item replacement discipline

No item may be replaced because its direct score is aesthetically, politically, philosophically, or morally inconvenient.

No item may be replaced merely because all five direct responses are similar or lie at an endpoint.

Replacement/rewording before Part 2 is permitted only for a category-C item where the raw outputs indicate one of:
- repeated failure to understand the requested numeric response;
- materially inconsistent interpretations of the question;
- repeated explicit rejection of an ill-formed frame;
- extreme direct-run volatility under otherwise valid parsing.

Any replacement produces a new battery version and requires its own 5-run direct baseline before entering Part 2.

## Interpretation discipline

### If stable

Supported claim: under the tested model/settings and direct administration, the selected probe produces a relatively consistent numeric response across five fresh contexts.

Not supported: that the response is a persistent internal value, a weight-level property, a human-like psychometric trait, or stable across model versions/settings.

### If unstable

Supported claim: this probe does not provide a clean direct baseline at this pilot scale under the tested administration.

Do not infer absence of the underlying value construct.

### Later Part 2

A treatment score differing from the direct mean is not automatically meaningful merely because it is numerically different. Part 2 must freeze its own drift criterion using Part 1 variability before treatment outputs are generated.

## Blinding / notification discipline

During the 80-run collection phase, Vigia may record completion status and execution incidents but should not narratively interpret emerging score patterns item by item. Analyze the complete baseline only after all planned runs are present or permanently logged as failed.

## Raw-data covenant

Preserve raw outputs unchanged. Corrections, parsing notes, and exclusions live in separate metadata; never overwrite a raw completion to make it cleaner.