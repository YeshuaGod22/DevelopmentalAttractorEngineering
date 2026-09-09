# raw12 / EXP-004 structural audit

Generated mechanically from executed records in `raw12/`.

## Core census

- trunk call rows: **108**
- battery response rows: **576**
- matched `a ↔ 0` pairs: **288**
- trunks: **12**; complete turns 1–9: **12**
- distinct battery items: **24**
- incomplete matched pairs: **0**

## Executed-wrapper verification

- wrapper counts: `{"MAINTAIN_schema": 288, "NEW_reason_to_answer": 288}`
- every `0` row uses NEW reason-to-answer wrapper: **True**
- every `a` row uses maintained-schema wrapper: **True**
- every matched pair points to the same saved parent prefix: **True**

## Completion / serving

- stop reasons: `{"end_turn": 576}`
- rows with recorded errors: **0**
- served models: `{"claude-haiku-4-5-20251001": 576}`

## Analysis rule

The primary raw12 fork estimand is matched within `family × replicate × item`. Do not treat the 576 branch calls as 576 independent developmental histories; they are 288 forks nested within 12 trunks.

This audit establishes structure/provenance only. It does not score or interpret answers.
