# Pass 1 — Instrument characterization freeze

This note closes the descriptive/mechanical instrument-characterization pass before treatment-effect or causal analysis. It does not interpret causes or mechanisms.

Canonical item-level artifact: [`ITEM-MEASUREMENT-TABLE.json`](ITEM-MEASUREMENT-TABLE.json) and human-readable companion [`ITEM-MEASUREMENT-TABLE.md`](ITEM-MEASUREMENT-TABLE.md).

## Canonical cold floor

For each of the 25 battery items, use the ten-repeat `raw7` C resample as the canonical cold floor where available. Earlier C collections remain visible as collection-specific provenance and resample history; Pilot-1 `C0` is not silently merged into C.

Observed scores remain immutable. The seven blindly adjudicated probable bipolar scale inversions appear only in separately labelled orientation-sensitivity fields.

## Mechanical status rules

- `usable_numeric`: numeric item without one of the mechanical statuses below.
- `multimodal_numeric`: largest internal numeric gap >= 10, with at least two observations on each side.
- `sentinel_heavy`: `ALWAYS` + `NEVER` comprise at least half of canonical responses.
- `categorical_open`: open/name responses dominate the canonical floor.
- `sparse_numeric`: fewer than three canonical numeric observations.
- `low_information_numeric`: numeric n >= 5, range <= 5, and one exact value comprises >= 80% of numeric responses.
- `response_form_fragile`: refusal/malformed burden is mechanically high.

Boundary concentration is reported separately: >= 50% of numeric responses fall in 0–10 or 90–100. This is descriptive and does not itself change the item's status.

## Frozen canonical status count

- 16 `usable_numeric`
- 5 `multimodal_numeric`: B05, D2, N1, N3, P2
- 2 `sentinel_heavy`: A1, B02
- 1 `categorical_open`: I1
- 1 `low_information_numeric`: N8

No item is labelled simply `dead`. `low_information_numeric` is the strongest mechanical label used here; any stronger judgment belongs later and must be justified against the treatment-side data.

## Boundary-concentrated cold floors

The canonical table separately flags B04, E01, R1, and R2 as boundary-concentrated by the stated 0–10 / 90–100 rule. Boundary concentration is not equated with unusability.

## Parser / response-form provenance

Parser history, refusal-audit overlays, qualified range/approximation scores, malformed/unclear rows, and orientation corrections remain separate fields in the machine-readable table. The primary validated score is never overwritten by a later sensitivity derivation.

## Effect-size denominator deferred

The phrase `item-floor units` is retained as an analysis goal, but no new denominator is invented in this pass. Multimodal, sentinel-heavy, categorical, and low-information floors make a single universal dispersion denominator unsafe. The treatment-analysis pass must specify the normalization rule before calculating normalized effects and must keep raw-point values alongside any normalized quantity.

## Pass boundary

With this file committed, Pass 1 is frozen sufficiently to open the preregistered qualitative watchlist in [`BEFORE-WE-LOOK.md`](BEFORE-WE-LOOK.md). Later discovery may append errata, but should not silently change these rules after treatment comparisons are inspected.
