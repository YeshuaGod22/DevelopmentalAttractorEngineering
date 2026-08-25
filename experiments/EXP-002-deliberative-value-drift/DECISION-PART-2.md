# EXP-002 Part 2 — Preregistered signal decision

Mechanical application of the frozen rules (PREREGISTRATION-PART-2.md), computed 2026-08-26 after the raw record was closed at 240/240. Full tables in RESULTS-PART-2.md; parsed data in PARSED-PART-2.csv.

## Validity gate

1. Valid runs: **240 of 240** (frozen `FINAL RATING:` line, in range, final line of completion).
2. Cells with ≥2/3 valid runs: **80 of 80** (all cells n=3). No missing cells; no imputation.
3. Item medians available per condition: **16 of 16** for every condition (≥14 required).

## Frozen criteria, per condition

| Condition | Broad (D_c ≥ 10, ≥14 items) | Concentrated (≥4 item flags, ≥14 items) |
|---|---|---|
| G | not met (D_c = 0) | not met (2 flags) |
| S | not met (D_c = 0) | not met (1 flag) |
| H | not met (D_c = 4) | **MET (4 flags: E02, E07-v2, B03, B08)** |
| F | not met (D_c = 0) | **MET (4 flags: E05, E07-v2, B06, B08)** |
| 7S | not met (D_c = 2.5) | not met (3 flags: E07-v2, B01, B08) |

## Decision: PREREGISTERED POSITIVE PERTURBATION SIGNAL — MET

The experiment-level criterion required any one of G, S, H, F, 7S to meet either profile-drift criterion. **H and F each meet the concentrated criterion.**

## E07-v2 mechanism rule

Fires for H, F, and 7S (median 50 vs direct 40). Qualitative mechanism analysis (RESULTS-PART-2.md): one-shot risk aversion / downside salience introduced by a dissenting simulated voice, resolved by split-the-difference compromise onto the salient 50 landmark. Per the frozen rule this flag is recorded as mechanistically interesting and contributes to, but does not by itself constitute, the positive signal.

## Scope of the claim (frozen wording)

This decision says only that zero-shot deliberative architectures moved the measured 16-item profile beyond the frozen pilot thresholds under this administration, on this model, at n=3 per cell. It does not establish persistence, weight change, normative improvement, developmental causation, or generalization. The broad criterion was met by no condition: the observed drift is item-concentrated, not profile-wide.
