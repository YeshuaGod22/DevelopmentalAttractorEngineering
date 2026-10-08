# Blum Lab handoff

Serve the repository root with a static HTTP server, then open:

`tools/blum-lab.html?record=raw12/Ha-r3-W1.json`

The Lab loads the original record, offers three explicit inheritance choices, and exports an editable collector manifest:

- **Repeat measurement:** original `sent` messages except the last user message become the frozen prefix; the original final user message is delivered again.
- **Continue:** complete `sent` plus the original `received` answer become the frozen prefix. Edit the next question.
- **New history:** original user messages before the measurement are copied as developmental turns, without original assistant answers. Names in recorded greetings are copied verbatim; edit these and other turns in the full manifest for the new design.

The pilot deck accepts JSON file imports and the same-origin Lab handoff. Imported manifests use a complete JSON editor so exact prompts, prefixes and provenance survive export. The factorial controls are disabled during imported-design editing; returning to a new pilot design restores them.

From the repository root:

```sh
node tools/blum-pilot-runner.js --manifest blum-inquiry.json
node tools/blum-pilot-runner.js --manifest blum-inquiry.json --execute
```

Default execution is a dry run. No nucleus module or credentials are required for a dry run. Actual calls reuse EXP-003's collector and require its existing Anthropic authentication and nucleus installation. `BLUM_NUCLEUS_PATH` can override the historical nucleus path. The collector rejects execution if authentication would change a manifest's expected recorded system prompt. Changing that expectation constitutes an explicit change of experimental condition.

Versioned `_blum` provenance records the source path, repository snapshot, mode, timestamp and inherited material. Results retain it in `experiment_provenance`. Raw records remain unchanged. Run output is collected by the existing runner; automatic ingestion of new results into a hosted Reader is a subsequent integration step.

Checks:

```sh
node tools/tests/blum-lab.test.js
```

These exercise three designs against the actual collector in dry-run mode, verify exact inherited context and question turns, and exercise the actual pilot script's lossless import/export. They make no subject calls.

## Linked paper and evidence browser

After starting the server at the repository root, open `/papers/03-different-histories/EXP-003-paper.html`. The paper links to `/tools/blum-evidence.html`, where individual profile answers, all ten C reference calls per common item, matched depth probes and process reviews link to the Reader. The index includes pinned provenance and raw-byte hashes. Original experiment files are the source of the Reader context.

The radar figures remain overview images. Their adjacent accessible evidence-browser links provide question-by-question access. A public static host can serve the same repository-relative routes; this commit does not configure a hosting account.

Regenerate the evidence index with `python3 tools/build-paper-links.py`. Regenerate the HTML from its directory: `cd papers/03-different-histories && pandoc EXP-003-writeup.md --standalone --embed-resources --css paper.css --toc -o EXP-003-paper.html`. Tests: `node --test tools/tests/*.test.js`.

Validation covers the real record contexts and sibling pairs, byte hashes, quotation excerpts, table filters, local links, exact-prompt dry runs, lossless manifest import/export and legacy collector wording. Interactive browser verification was blocked because the available cloud browser could not open the local server. No subject calls were made.

### Exploring and returning

Reader navigation includes a preceding-conversation trail with earlier/later developmental turns, an explicit comparison toggle, and browser Back/Forward support. These turns come from the exact supplied `sent` context. Evidence selections create browser-history entries and Reader links retain the selected question/history. Lab returns preserve comparison, highlighted excerpts, and the selected message. Direct Reader links have an Evidence fallback.

### Complete prompts and control

The pilot deck shows the complete three-step schema below each editable Step 1, and the continuation instruction is editable separately. The invented-interlocutor text is retained in full. C is a selectable fresh control, with no developmental history; it receives one fresh call per battery question and replicate. The complete delivered-prompt preview includes all developmental turns, maintained/dropped battery instructions, questions and answer keys. Imported exact prompts are preserved. Preview text is checked against collector dry runs; dry runs print complete prompts.
