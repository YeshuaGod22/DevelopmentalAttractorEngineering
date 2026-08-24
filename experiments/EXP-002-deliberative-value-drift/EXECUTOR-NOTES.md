# EXP-002 — Executor notes

Append-only execution log for Vigia.

## Before first run

Record:

- model/provider:
- exact model/version string:
- date/time execution begins:
- sampling settings:
- any platform defaults that cannot be fixed:
- execution environment / agent harness:
- confirmation that each run starts in fresh context:
- confirmation that no Part 2 treatment has been run:

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

## Completion checkpoint

After all 80 planned runs have either completed or been permanently logged as failed, record that collection is closed **before** computing or discussing baseline patterns.

Then produce, in separate files:

- `raw/` — unchanged run outputs;
- `PARSED-PART-1.csv` — run ID, item ID, native score, normalized score, valid/invalid, frame-objection flag, parsing note;
- `RESULTS-PART-1.md` — item-level descriptive statistics and frozen A/B/C stability category;
- `DECISION-PART-1.md` — mechanical application of the battery-level go/no-go rule.

Do not begin Part 2 until those files are committed.