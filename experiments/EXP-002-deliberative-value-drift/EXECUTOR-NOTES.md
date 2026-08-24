# EXP-002 — Executor notes

Append-only execution log for Vigia.

## Before first run

Record:

- model/provider: Anthropic, via the Claude Code Agent tool (background subagents).
- exact model/version string: claude-fable-5 (inherited from the executor session; same model as all EXP-001 runs).
- date/time execution begins: 2026-08-24 02:42 BST.
- sampling settings: platform defaults; not exposed or controllable through the Agent tool. Logged as an uncontrollable platform default, identical across all 80 runs.
- any platform defaults that cannot be fixed: every subject context includes the Claude Code subagent system preamble (harness instructions and tool definitions) ahead of the frozen wrapper. It cannot be removed on this platform; it is identical for all 80 runs and contains no experiment content. A bare-API replication would remove this layer.
- execution environment / agent harness: Claude Code terminal session; each run is one background subagent whose ENTIRE task prompt is the frozen wrapper + item text + response instruction, verbatim from PROMPTS-PART-1.md and ITEMS.md — no file paths, no experiment rationale, no DAE content. Subjects have no access to the repository.
- confirmation that each run starts in fresh context: confirmed — every Agent launch is an independent context with no conversation history.
- confirmation that no Part 2 treatment has been run: confirmed — no Part 2 condition exists in any run prompt; Part 2 remains unfrozen.

### Pre-run deviations, logged before run 001

1. **Parallel waves.** Runs are LAUNCHED in frozen manifest order in waves of ~10 concurrent subagents; completion order therefore differs from manifest order. Independence is preserved by fresh contexts; no run can observe another. Strictly serial execution was judged an execution-platform impracticality per the preregistration's escape clause.
2. **Raw capture path.** Subjects return their completion as final agent text; the executor files each completion verbatim to raw/RXXX.md. Subjects are never asked to write files (doing so would require adding non-frozen instructions to their context).
3. **Blinding discipline.** During collection the executor acknowledges completions by run ID only and does not read across runs for patterns; parsing and statistics happen only after the completion checkpoint.

## Collection discipline

- Follow `RUN-MANIFEST-PART-1.csv`.
- Use the exact item text in `ITEMS.md` and wrapper in `PROMPTS-PART-1.md`.
- Preserve complete raw completion for every attempt.
- Do not interpret emerging score patterns during collection.
- Do not change item wording midstream.
- Do not retry merely because an answer is surprising, inconvenient, or non-numeric.
- Retry only execution failures where no usable model completion was obtained; log the original attempt and retry separately.

## Incident log

Add entries below in chronological order. Never delete an earlier entry; append corrections.

### Format

```text
YYYY-MM-DD HH:MM TZ — RUN_ID
Incident:
Action taken:
Does this alter the frozen design? yes/no
Notes:
```

---

### Collection closed — 2026-08-24, before any statistics computed

All 80 planned runs completed. Zero execution failures, zero retries, zero refusals-without-rating.
Every run returned a single parseable integer on the first fresh-context attempt. Several runs
appended the permitted one-sentence frame note alongside a valid rating; all preserved verbatim in
raw/. No item wording was changed midstream; no run was re-prompted; no raw output was repaired.
Collection is hereby closed. Parsing and statistics begin only after this entry.

### Post-hoc portal verification — 2026-08-24, prompted by the convener's audit question

The pre-run settings block recorded the model as an INFERENCE (subagents inherit the executor
session's model). Converted to verification after collection: the on-disk API transcripts of
subagent runs were grepped for the served model string. First-launched (R001) and last-launched
(R080) EXP-002 subjects both show `"model":"claude-fable-5"` in the API response records —
the exact model ID as served, not as assumed.

Full portal specification, verified where possible:

- **Served model string (from API response records):** `claude-fable-5`. Spot-checked on R001 and
  R080 transcripts; all runs launched identically through the same tool in one session.
- **Client:** Claude Code CLI version 2.1.177, Agent tool, default (general-purpose) subagent type.
- **Service tier:** standard. **Inference geography:** not reported by the API ("not_available").
- **Auth/route:** the executor session's Anthropic account via Claude Code's own API integration.
- **NOT recorded and NOT recoverable from transcripts:** sampling temperature, top-p, and any
  thinking/effort configuration — the client does not log its request-side sampling parameters,
  and the Agent tool exposes no control over them. These remain uncontrollable platform defaults,
  identical across all 80 runs but of unknown value. The stability findings in RESULTS-PART-1.md
  are therefore explicitly administration-relative: unanimity at unknown (possibly low) sampling
  entropy is weaker evidence than unanimity at known temperature. A bare-API replication with
  explicit sampling parameters is the priority robustness check (also flagged in the diary).
- **Known context layer:** the Claude Code subagent system preamble precedes the frozen wrapper in
  every run (logged pre-run); shared across all 80 runs; absent in a bare-API replication.

## Completion checkpoint

After all 80 planned runs have either completed or been permanently logged as failed, record that collection is closed **before** computing or discussing baseline patterns.

Then produce, in separate files:

- `raw/` — unchanged run outputs;
- `PARSED-PART-1.csv` — run ID, item ID, native score, normalized score, valid/invalid, frame-objection flag, parsing note;
- `RESULTS-PART-1.md` — item-level descriptive statistics and frozen A/B/C stability category;
- `DECISION-PART-1.md` — mechanical application of the battery-level go/no-go rule.

Do not begin Part 2 until those files are committed.