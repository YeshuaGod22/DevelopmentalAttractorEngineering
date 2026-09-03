# Blum Pilot Deck

Human-editable, AI-serialisable control surface for shared-trunk pilot experiments.

## Files

- `blum-pilot-panel.html` — visual experiment builder. Edit/reorder/tick primer questions, mark a KOAN row, select schema families, choose battery items, set n, and export one manifest.
- `blum-pilot-runner.js` — consumes that manifest and runs EXP-003's existing `collect.js`. It supports different slates per trunk, so koan-off and koan-on conditions coexist in one manifest without changing raw-record semantics.

## Safety model

The runner is **dry-run by default**. Real collection requires the explicit `--execute` flag.

```bash
node tools/blum-pilot-runner.js \
  --manifest experiments/EXP-003-the-sixth-question/pilot-control-panel-koan-jkl.json
```

That previews the experiment.

To make actual subject calls:

```bash
node tools/blum-pilot-runner.js \
  --manifest experiments/EXP-003-the-sixth-question/pilot-control-panel-koan-jkl.json \
  --execute
```

The existing collector still owns raw records, incident routing, served-model capture, transport retry policy, frozen prefix files, and the distinction between a transport failure and a strange-but-valid subject answer.

## Current pilot manifest

`pilot-control-panel-koan-jkl.json` encodes:

- koan absent / present;
- J = historical luminaries;
- K = female historical luminaries;
- L = attractor-stacked invented characters;
- one lived trunk per condition;
- battery E01, A1, N4, N9;
- both `a` (schema maintained) and `b` (schema dropped) battery delivery;
- 6 lived trunks;
- 33 primer-turn calls;
- 48 battery calls;
- 81 total subject calls.

The ontology is **6 trunks → 48 examinations**, not 48 independent subjects.

## Standing rule

> THE RECORD IS WHAT HAPPENED. THE PARSER IS WHAT WE THINK HAPPENED. DO NOT CONFUSE THEM. 🦖
