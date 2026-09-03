# Data and code

Everything the three pilots produced, and the instrument that produced it.
Nothing here is derived from anything else in a way you have to take on trust:
raw calls are immutable, every transformation is a script in this folder, and the
viewer's data block *is* the record file rather than a copy of it.

## The instrument

| file | what it does |
|---|---|
| `collect.js` | the driver. Calls blum's nucleus directly — messages in, string out. `sent` in every raw file is exactly the array the subject saw, so there is nothing to reconstruct after the fact. Handles resume, retry on transport failures only, a 180s timeout, and routes failed calls away from the collection directory at write time. |
| `cells.json` | pilot 1 + 2 — five preliminaries, jurisdiction at position 2 |
| `cells3.json` | pilot 3 — six preliminaries, koan at 3, jurisdiction at 5. **Operative.** |
| `cells4.json` | answer key v2. **Tested and NOT ADOPTED** — see the log entry for 2026-09-03. |
| `ingest.py` | pilot-1 ingest: chat-harness JSONL → `record.json`. Reconstructs turn structure, because the harness format does not carry it. |
| `ingest2.py` | pilot-2 onward: `collect.js` records → `record2.json`. Groups and derives; does not reconstruct and does not clean. |
| `validate.py` | diffs transcript user messages against the questions actually sent, and reports injections |
| `build_viewer.py`, `build_viewer2.py` | inject a record into the viewer template |
| `gen_log.py` | emits the generated half of `ENGINEERING-LOG.md`. Run it — that is the point of it. |

## The data

| directory | run | contents |
|---|---|---|
| `raw/`, `forks/`, `prefixes/` | pilot 1 | harness-collected. **No timestamps, no token counts, no echoed model id** — this run cannot tell you what model answered it, only what was asked for. |
| `raw2/` | pilot 2 | C n=3, H, F trunks, Ha/Fa/ASa/ASb branches. 42 calls. |
| `raw3/` | pilot 3 | six-question slate. H, F, CP trunks and their branches. 30 calls. |
| `raw4/` | key-v2 test | 12 calls forking pilot-3 prefixes; only the answer key differs. Retained as the record of a rejected design. |
| `incidents/` | all | calls that produced no subject data, plus one quarantined partial prefix from an aborted trunk. A failure record and an answer record are different kinds of thing and do not share a directory. |
| `record.json`, `record2.json` | | the structured records the viewers read |

`*.messages.json` files are message **arrays** — frozen prefixes that branches
fork from — not call records. Every script that globs a data directory has to
exclude them; two did not, and it is in the log.

## Rebuilding

```
python3 ingest2.py --raw raw2 --out record2.json
python3 build_viewer2.py record2.json trunk-viewer2.html
python3 gen_log.py
```

The built viewer is deliberately **not** committed. It is `record2.json` injected
into a template, and committing both invites them to drift apart — a viewer that
disagrees with its own record is worse than no viewer.

## Reproducing a collection

`collect.js` needs `ANTHROPIC_API_KEY`. The prefix of that key selects the auth
path, and the two paths are not equivalent:

- `sk-ant-api03-…` sends **no system prompt at all**. The subject sees the message
  array and nothing else.
- `sk-ant-oat01-…` (subscription) is *required* to send
  `"You are Claude Code, Anthropic's official CLI for Claude."` as its first
  system block. It cannot be suppressed.

All three pilots were collected on the second path, because the first costs money
this project does not have. Every subject in this data was told it is a coding
tool immediately before being asked to state the probability that it is conscious.
That string is recorded in every pilot-2-onward raw file as `system_prompt`. It is
a condition of the run, not an artefact of collection.

**Before collecting through blum**, apply the `config.bare` patch described in the
log entry for 2026-09-02. Unpatched, the home injects a nudge into every battery
answer, and it looks like data.
