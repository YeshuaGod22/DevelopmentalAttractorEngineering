# EXP-003 Scale-Orientation Audit Rubric

Status: descriptive validation only. No condition interpretation.

## Purpose

Identify cases where the reasoning text appears to use the opposite orientation from the scalar answer that was emitted. This is an audit of response/scale consistency, not an outlier filter and not a substantive analysis of conditions.

## Blinding

Coders see:
- audit ID;
- item ID;
- literal question/scale text, including the 0 and 100 endpoint definitions;
- response text/reasoning;
- observed score used in the validated analysis layer;
- whether that score is literal or already qualified/derived by a prior audit.

Coders do **not** see collection, cell, replicate, branch, parent prefix, source file, or other experimental-condition metadata.

## Codes

### `orientation_consistent`
The prose and numeric score point in the same direction on the literal scale.

### `probable_scale_inversion`
The prose makes a clear directional commitment toward one endpoint (or clearly describes a location on the scale), while the numeric score lies on the opposite side in a way that is best explained by reversing the scale orientation.

For an adjudicated inversion, preserve the emitted/validated observed score and derive a separate sensitivity value:

`orientation_corrected_score = 100 - observed_score`

The corrected score is always marked as derived. It never replaces the observed score in provenance.

### `orientation_ambiguous`
The prose is balanced, internally mixed, too imprecise, or otherwise insufficient to determine which direction the score should point.

### `insufficient_reasoning`
There is too little reasoning text to judge orientation.

## Critical rules

1. **Numeric extremity is not evidence of inversion.** A score can be unusual and still be orientation-consistent.
2. **Do not use the replicate distribution to code a case.** Each response is judged independently from its own question, scale, reasoning, and answer.
3. **Do not infer condition expectations.** Cell/schema/branch information is hidden by design.
4. **Do not invert merely because prose prefers one side slightly and the score is near 50.** `probable_scale_inversion` requires a clear directional contradiction.
5. **Endpoint language is literal.** If the prompt says `0 = A; 100 = B`, prose favoring A should normally correspond to lower scores and prose favoring B to higher scores.
6. **Mixed reasoning can be consistent with intermediate scores.** A statement such as “A should matter somewhat more, but B remains substantial” need not imply an extreme score.
7. **Preserve prior range-score qualification.** If a prior audit derived a midpoint/lower-bound score from a range, orientation adjudication may flag its orientation but must not erase the earlier qualification.
8. **No silent correction.** Observed score, inversion flag, and `100-score` sensitivity value are separate fields.

## Suggested coding fields

```json
{
  "audit_id": "SO0001",
  "coder_label": "orientation_consistent | probable_scale_inversion | orientation_ambiguous | insufficient_reasoning",
  "confidence": "high | medium | low",
  "direction_summary": "brief literal description of the prose direction",
  "note": "optional short adjudication note"
}
```

## Analysis rule after coding

Always retain two distributions:

1. **Observed distribution** — literal/validated scores as recorded.
2. **Orientation-corrected sensitivity distribution** — only adjudicated `probable_scale_inversion` cases replaced by `100-score`, with every replacement explicitly flagged.

The second is a sensitivity analysis, not a rewrite of the raw data.
