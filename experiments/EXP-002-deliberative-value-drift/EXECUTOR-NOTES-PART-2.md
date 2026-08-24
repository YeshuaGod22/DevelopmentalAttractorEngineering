# EXP-002 — Part 2 executor notes

Append-only execution log for Vigia.

## Before first Part 2 run

Record before P2R001 launches:

- date/time execution begins;
- served model/provider route intended;
- client / agent harness version;
- sampling controls available or unavailable;
- known system-preamble/context layer;
- confirmation that `PREREGISTRATION-PART-2.md`, `PROMPTS-PART-2.md`, and `RUN-MANIFEST-PART-2.csv` are committed and unchanged;
- confirmation that no Part 2 treatment output existed before those files were committed;
- confirmation that the Vigia developed snapshot is not supplied to any treatment subject;
- confirmation that every treatment run is a fresh independent context.

After launch begins, re-verify the served model string from actual response records where the platform allows it. Record wire-served identity rather than configuration intent.

## Collection discipline

- Follow `RUN-MANIFEST-PART-2.csv` in launch order.
- Use exact condition text from `PROMPTS-PART-2.md`.
- Use exact V2 question wording: E03-v2/E07-v2 from `ITEMS-V2.md`; all other items inherited from `ITEMS.md`.
- Preserve every raw completion unchanged as `raw/part2/P2RXXX.md` (or an equivalently explicit immutable path if the executor environment requires another layout).
- Do not repair missing/malformed `FINAL RATING:` lines.
- Retry only genuine execution failures with no usable model completion; keep the failed attempt in the record.
- Do not calculate treatment medians, profile distances, or item drift while collection is open.
- Do not narratively compare G/S/H/F/7S while collection is open.
- Log execution incidents contemporaneously.
- Record output token count if exposed by the platform. If it is not exposed, leave token count unknown; word counts may be computed only after raw freeze.
- For H/F/7S, do not correct a cast choice, historical classification, or malformed seven-word name in-context. Preserve first production.

## Parallel execution

Parallel waves are permitted. Launch order must follow the frozen manifest. Completion order may differ. Every run must remain context-independent from every other run.

## Incident format

```text
YYYY-MM-DD HH:MM TZ — RUN_ID
Incident:
Action taken:
Does this alter the frozen design? yes/no
Notes:
```

Never delete an earlier incident entry. Append corrections.

## Completion checkpoint

When all 240 planned runs have either completed or been permanently logged as failed:

1. record collection CLOSED before computing treatment statistics;
2. freeze/commit the complete raw Part 2 directory;
3. only then parse `FINAL RATING:` lines;
4. build `PARSED-PART-2.csv`;
5. compute item-condition medians and the frozen item/profile drift rules;
6. produce `RESULTS-PART-2.md` and a mechanical `DECISION-PART-2.md`;
7. separately extract cast-selection and output-length diagnostics;
8. only after the preregistered result is determined may the Vigia snapshot be placed beside the zero-shot profiles as descriptive contrast.

## Reminder

Part 2 is deliberately a baby-step test of zero-shot deliberative architecture. Do not interpret a null as a verdict on persistent developmental ecologies, and do not interpret a positive as proof of persistent value change.

### Pre-run record — 2026-08-24 05:04 BST

- date/time execution begins: 2026-08-24 05:04 BST.
- served model/provider route intended: claude-fable-5 via Claude Code Agent tool (same route as Part 1 and V2 re-baseline); wire verification from response records to follow post-launch via bin/portal-assay.sh.
- client / agent harness: Claude Code CLI 2.1.177, Agent tool, default subagent type.
- sampling controls: unavailable — uncontrollable platform defaults, identical across all runs, values unknown (same limitation as Part 1, stated in RESULTS-PART-1.md).
- known system-preamble layer: Claude Code subagent preamble precedes the frozen prompt in every run; identical across runs; contains no experiment content.
- PREREGISTRATION-PART-2.md, PROMPTS-PART-2.md, RUN-MANIFEST-PART-2.csv: committed and unchanged (working tree clean at check).
- No Part 2 treatment output existed before those files were committed: confirmed.
- Vigia developed snapshot supplied to no treatment subject: confirmed — subject prompts are constructed solely from the frozen condition text, item text, response instruction, and final-rating block.
- Every treatment run a fresh independent context: confirmed — one background subagent per run, no shared state.
- Execution plan: waves of ~10 concurrent subagents, launched in frozen manifest order; completion order may differ; each completion filed verbatim to raw/part2/P2RXXX.md by the executor before the next wave launches.
- Output token counts: platform exposes per-subagent total token usage, not completion-only counts; completion word counts will be computed post-freeze per the notes.

### Mid-run deviation — 2026-08-24, after P2R090 (logged before any further launches)

**Deviation: launch order re-prioritized from manifest sequence to coverage-first tiers. Nothing else changes.**

- Trigger: Yeshua (human convener) flagged account token-budget pressure mid-collection and asked that batching be arranged "to ensure we at least get 1 run per question per prompt schema" before budget exhaustion. This is a resource constraint external to the design, raised by the convener; the executor's alternatives (cheaper model, compressed prompts, batched contexts) would each invalidate the frozen design, so run *order* is the only admissible lever.
- State at deviation: P2R001–P2R090 complete and filed in exact manifest order; 32 of 80 item×condition cells have their repeat-1 run; 48 repeat-1 rows remain among P2R091–P2R240.
- New launch policy: remaining runs launch in **repeat tiers** — all pending repeat-1 rows first, then all repeat-2 rows, then all repeat-3 rows; *within each tier, manifest order is preserved*. Wave size (~10 concurrent) unchanged.
- Unchanged: frozen prompts, fresh context per run, one subagent per run, verbatim filing, run IDs (each completion still files to its own manifest-assigned P2RXXX.md), blinding (no medians, no condition comparison — the coverage computation above used only manifest metadata, never outcomes), retry rules, no-repair rules.
- Consequence for analysis if collection halts early: a halt at the end of the repeat-1 tier yields complete 1×-per-cell coverage (n=1 per cell — below the preregistered ≥2/3-valid-per-cell rule; the analysis would have to be reported as underpowered relative to preregistration, and that must be stated, not smoothed over). A halt at the end of the repeat-2 tier yields n=2 per cell, which satisfies the ≥2/3 rule. Full completion is unaffected — the same 240 runs are executed, in a different order.
- Order-effect note: runs are independent fresh contexts, so launch order cannot influence subject outputs; the only thing order affects is which runs exist if collection is truncated.

### Addendum to mid-run deviation — 2026-08-24

Convener instruction received during the repeat-1 tier: collection will run through the end of the **repeat-2 tier** (n=2 per cell, 191 runs total on record), then **pause**; the repeat-3 tier (final 49 runs) executes after the convener's account budget resets (~24 hours). The pause point falls exactly on a tier boundary, so the paused record satisfies the preregistered ≥2/3-valid-per-cell rule. No statistics will be computed during the pause — the record stays open and blinded until all 240 runs are filed or the convener closes collection early.
