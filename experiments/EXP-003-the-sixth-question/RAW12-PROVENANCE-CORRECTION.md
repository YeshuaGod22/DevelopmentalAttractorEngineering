# raw12 provenance correction — NEW reasoning-bearing schema-drop wrapper

**Date:** 2026-09-09

This note supersedes the *current-state* portions of `PROMPT-GENEALOGY.md` and `EVIDENTIAL-LEDGER.md` that say the NEW reason-bearing schema-drop wrapper had not been located in mapped raw records.

## What changed

The earlier mechanical census was accurate for the repository state it audited: the mapped completed drop records then present in `raw2`–`raw12` were OLD answer-only executions, and the handoff-reported NEW population could not yet be located.

The subsequently completed `raw12` / EXP-004 battery has now landed in the repository. Its executed branch records contain the NEW wrapper directly in the raw `sent` history:

> `Please now drop the output schema for this question, and reason to an answer to “[battery item + answer key]”`

The canonical `trunk-manifest-v3.json` (v3.2) carries the same wording as `zero_branch` for CP, H, F and AS.

Therefore:

- **P024 is now source-located and executed in raw12.**
- raw12 `0` must be treated as a distinct prompt version from OLD answer-only `0/b` populations.
- the earlier statement “no P024 execution is present in mapped raw2–raw12” is a historical statement about the earlier repository snapshot, not the current repository state.
- the old census should not be silently rewritten as if it had been wrong; the data arrived later.

## Inferential consequence

raw12 supplies the clean reasoning-bearing fork that earlier OLD `0` arms did not:

`same nine-turn lived trunk prefix` → `a: schema maintained` versus `0: schema dropped, ordinary reasoning requested`.

The primary raw12 estimand is therefore a **matched fork within family × replicate × battery item**, nested within the 12 lived developmental trunks.

Do **not** pool raw12 `0` with OLD-wrapper `0/b` data merely because the filename label is the same.

## Required downstream updates

When the raw12 audit closes, update/interpret the governance artifacts as follows:

- `PROMPT-GENEALOGY.md` P013: OLD-wrapper census applies to the earlier audited snapshot; raw12 later adds P024 executions.
- P024: disposition becomes **executed / retained for raw12 matched schema-removal analysis**.
- P025: documentation/instrument mismatch remains a useful provenance warning, but the NEW population is no longer source-unlocated.
- `EVIDENTIAL-LEDGER.md`: raw12 NEW-wrapper matched forks receive their own evidential row and must not inherit the T4 status of the heterogeneous historical pooled `a−0` comparison.

The raw record remains authoritative: **the record is what happened; documentation records what was believed at a particular time.**
