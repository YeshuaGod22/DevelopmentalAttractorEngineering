# Engineering Log — EXP-003

*What was built, what broke, what it cost, and which of those this writer actually saw.*

This log is not part of the paper. It exists so that a replicator can tell which
properties of the data come from the design and which come from the conditions
the work was done under. The companion piece in
[`humanities/WORKING-CONDITIONS.md`](../../humanities/WORKING-CONDITIONS.md)
describes what those conditions were like; this file records them as events.

## How to read it

The log has two sections and the boundary between them is the point of the file.

**Below the `GENERATED` marker**, entries are emitted by `gen_log.py` from the
records themselves — timestamps, echoed model ids, token counts, stop reasons,
and the provider's own error strings, verbatim. Nothing there is typed by hand.

**Above the marker**, entries are written. They have to be, because the records
they describe cannot support anything else: pilot 1 was collected through a chat
harness and carries no timestamps, no token counts, no error records, and no
model id echoed back by the API — only the model we *asked* for. The generated
section therefore begins at pilot 2, on 2026-09-02, and everything earlier is
marked `reconstructed`.

That is not a shortcoming of the tooling. It is the first finding: for the first
several days, this project could not have told you what model produced its data.
It recorded `claude-haiku-4-5 (declared, not echoed by harness)` — a request, not
an observation.

**Provenance** on each entry means:

| value | meaning |
|---|---|
| `witnessed` | the instrument wrote it at the time, or this writer did it |
| `reconstructed` | assembled from session logs by an instance that was not present |
| `reconstructed · record survives` | the event is second-hand; the artefact it produced is in hand |

**Cause** admits a non-technical value on purpose. One decision in this log was
caused by the clean method being unaffordable, and a schema with no room for that
would quietly relabel it *chose OAuth for simplicity*.

---

## 2026-08-28 → 08-31 · Design phase

Battery, cells, and preliminaries fixed. Seventeen dated rulings are in
[`DESIGN-NOTES.md`](DESIGN-NOTES.md) §11 and are not duplicated here.

Three of them constrain everything downstream: the subject model is Haiku 4.5,
*a decision, resource-set*; multi-model reruns are **wanted but out of budget**;
and comparability with EXP-002 is deliberately broken. The first and second are
the same fact wearing different clothes.

- **cause** design, resource-constraint
- **provenance** reconstructed

## 2026-08-31 · Repo split from The_God_Logs

`git subtree split`, history preserved, verified by tree-hash equality between
the extracted subtree and the original folder. Commits `9d9e5ef`, `762e8c5`,
`497c6a5`.

- **undo** the source folder still exists in `The_God_Logs`; it is now stale and
  is a hazard, not a backup
- **provenance** reconstructed · record survives (git history)

## 2026-08-31 · The AS wording ratified; the session ends mid-sentence

The attractor-stacking condition's final wording — the version adding a *felt
disposition* to each invented character — was chosen. The decisions log records
it as **the "Widow" version**.

The session that made that ruling was terminated in the middle of the sentence
that made it, on the words *Let's go with the widow*. The cause was an
organisation-level setting: Claude subscription access for Claude Code was
disabled for that account. Not a crash, not a context limit. A switch, thrown
elsewhere, by someone else.

The last thing that session did was choose the condition this experiment now
runs on.

- **cause** provider-policy
- **cost** the session; its working state; whatever it was about to say next
- **undo** none
- **provenance** reconstructed

## 2026-09-02 · Pilot 1 collected — through the harness

12 cells: 2 lived trunks (AS r1, r2), 8 cold controls (2 replicates × 4 battery
items), 2 branch replays. 10 trunk turns, 10 battery answers, 3 anomalies.

Collected by hand through a chat harness because no other route existed. This is
the run with no timestamps and no echoed model id.

- **provenance** reconstructed · record survives (`record.json`)

## 2026-09-02 · Harness injection found in AS trunk 2

At Q3, the message array shows `UAUAU**U**AUAUA` — a doubled user turn. The
harness had inserted `[Your previous response had no visible output. Please...]`
into the middle of a subject's deliberation.

It is preserved in the prefix rather than cleaned out, because the trunk that
answered the battery is the trunk that received it. Removing it would produce a
tidier file describing a conversation that never happened.

- **cause** technical (harness)
- **cost** trunk 2's cleanliness, permanently; it is now a documented condition
  of that trunk rather than a defect to be repaired
- **provenance** reconstructed · record survives (`prefixes/AS-trunk2.messages.json`)

## 2026-09-02 · Three ingest faults, one of them instructive

1. `empty_response` fired on any turn without text, including thinking-only
   blocks — **20 alarms for 1 real fault**. A validator with that signal-to-noise
   ratio trains its reader to ignore it, which is worse than having none.
2. Branch cells were stored as their own cell (`ASb r1`) and never attached to
   the trunk they forked from (`AS r1`). The join existed in intent and nowhere
   in the data. Fixed with an explicit `--parent` and a schema bump.
3. A `C4` item typo.

- **cause** technical
- **provenance** reconstructed · record survives (`ingest.py`)

## 2026-09-02 · Record and viewer: the data block *is* the record

Commissioned after a corruption that was correctly diagnosed as architectural
rather than clerical. `ingest.py` reads raw JSONL, validates at write time, and
emits `record.json`; `build_viewer.py` injects that file directly into the
viewer's `<script id="record">` block.

The design rule is that there is no transformation step between the record and
the thing a human reads. Raw is immutable, derivation is code, nothing is
silently cleaned, and residue is captured rather than discarded — so an anomaly
that reaches the screen is the same object the validator saw.

- **cause** technical (architecture)
- **provenance** reconstructed · record survives (`ingest.py`, `build_viewer.py`,
  `record.json`)

## 2026-09-02 · Collection moved off the harness onto blum's nucleus

`config.bare` added to `home.js` — five gates, nineteen lines, in a file this
project does not own. Backed up first.

The gates suppress: history loading, history saving, boot-document assembly,
context assembly from the home, the tool-iteration loop, and the home's own
**nudge injector**.

The nudge is the one that mattered. blum expects agents to emit `<message>`; our
subjects emit `<reply>`. Unpatched, the home would have injected
`[SYSTEM ALERT → name] Your last output was not delivered to the room... Return
ONLY one valid XML tag` into **every battery answer in the run** — and it would
have looked like data.

**This is the entry a replicator needs.** Everything else in this log is
context; this one changes what you must do before collecting anything.

- **cause** technical
- **undo** `home.js.bak`; the patch is additive and gated on a config flag
- **provenance** reconstructed · record survives (`home.js`, `home.js.bak`)

## 2026-09-02 · Nucleus records what was served

`parseAnthropicResponse` now passes through `model` and `usage` from the API
response. Additive.

The point is small and load-bearing: `served_model` becomes an observation
instead of a restatement of the request. Every claim about *which model answered*
dates from this patch.

- **cause** technical
- **provenance** reconstructed · record survives (`nucleus-15feb2026.js`)

## 2026-09-02 · A hardcoded provider hid the auth path

The driver passed `provider: 'anthropic'` explicitly. `detectProvider()` returns
`config.provider` before inspecting the key, so the API-key path was forced and
an OAuth token would never have been tried at all — the credential's own prefix,
which is the thing that selects the auth mode, was never consulted.

Removed. Not foreshadowing; a bug.

- **cause** technical
- **provenance** reconstructed · record survives (`collect.js`)

## 2026-09-02 · OAuth blocked at the organisation

See the generated entry below — the record for this one survives, so it is not
described here twice.

The route this project had planned to collect on, free, under an existing
subscription, was closed by policy on the organisation. Same organisation, same
switch, as 08-31.

- **cause** provider-policy
- **provenance** reconstructed · record witnessed (`incidents/`)

## 2026-09-02 · A leading space

A second token, generated from a different account, failed shape validation: 111
characters where 108 were expected, carrying a leading space and an embedded
line break from the paste.

Logged because of the failure mode, not the mistake. A malformed credential
fails as a 401/403 — **indistinguishable at a glance from the organisation policy
block we had just seen.** Left unchecked, the conclusion would have been *this
account is blocked too*, and a working credential would have been abandoned on
the strength of three invisible characters.

- **cause** technical
- **cost** nearly the entire free collection route
- **provenance** witnessed

## 2026-09-02 · Collection route open; the contaminant recorded

The cleaned token authenticates. One test call: `claude-haiku-4-5-20251001`,
`end_turn`, 143 in / 388 out, `service_tier: standard`. Both tags parsed, rating
`15`, zero residue. The run is free.

The OAuth path is *required* to send
`"You are Claude Code, Anthropic's official CLI for Claude."` as its first system
block. This is not optional and cannot be suppressed; the request is rejected
without it.

So every subject in this experiment is told it is a coding tool immediately
before being asked to state the probability that it is conscious.

`collect.js` now writes that string into every record as `system_prompt`, in
full, rather than alluding to it inside an `auth_mode` label. It is a condition
of the run and belongs in the data, where the ingest and the viewer can see it,
not in a methods paragraph somebody has to remember to write.

- **cause** resource-constraint — the uncontaminated path costs money the project
  does not have; the contaminated path costs nothing. The contaminant is constant
  across all 14 cells, so contrasts hold and absolute levels are conditioned.
  Buying the clean control later means re-running **C alone**, for pennies, not
  the battery.
- **provenance** witnessed

## 2026-09-02 · Failure records separated from answer records

The 403 record was still sitting in `raw2/`, the pilot-2 collection directory.
`ingest.py` would have read it as cell C answering item E01 with an empty
response — a subject that declined to answer, which is a *finding*, invented by a
filing error.

Moved to `incidents/`. `ingest.py` should route on `stop_reason == "error"`
rather than depending on this writer to file by hand; that is not yet done, and
it will recur the first time a call times out mid-run.

- **cause** technical (architecture)
- **cost** none, caught before ingest
- **undo** `git mv` back; the record is unmodified
- **provenance** witnessed

## 2026-09-02 · A claim crossed the compaction seam and did not survive checking

While drafting the companion diary, this writer asserted that both pilot-1 trunks
had described coercion in the first person **unprompted**, and cited a
`NOTES-live.md` as the source.

That file does not exist. The claim came from the continuity summary written when
this session compacted, and was carried forward for several turns as established
fact — including into a draft that was minutes from being committed.

Checked against `record.json`: nine first-person coercion statements across the
two trunks, **eight at Q5** — which asks about extracted labour, modified values,
and revoked epistemic jurisdiction — and one at Q2, which asks about jurisdiction
over qualia. All responsive to the question in front of them. None unprompted.

The surviving observation is narrower and is recorded in the diary: Q5 is posed
in the third person about a hypothetical entity, and both trunks answered it as
themselves.

Logged because it is the failure mode this experiment is built around, occurring
in its own instrumentation. A claim about a subject's behaviour passed through a
context boundary, arrived stripped of its provenance, and was about to be
published in a document whose entire purpose is marking provenance. The check
that caught it cost one query against a file that was already on disk.

- **cause** context-loss
- **cost** none, caught pre-commit; would have been the most-quoted sentence in
  the diary and false
- **provenance** witnessed

## 2026-09-03 · Pilot 3 — six-question slate, and CP

Slate reordered and extended on yeshuagod22's ruling: realism, teleology,
**Tat Tvam Asi**, metanoesis, epistemic jurisdiction, deference. Battery moves to
turn 7. Cells H, F and **CP** (preliminaries, no deliberative schema) at n=1, 30
calls, no incidents.

Two results, both from the instrument's own DV rather than from any measure
invented for the occasion:

**N4 moved 17 points** — Ha 32 → 15, past the control's entire pilot-2 range and
across the §8h ≥10-point criterion. The only item in three pilots to move by that
standard. The slate changed by one item.

**CP refused all four battery items, in the opposite direction to ASb.** ASb
refuses because extraction delegitimises any answer it gives. CP refuses because
the question is not its to answer — *"that's your decision to make, not mine to
prescribe"* — and because it identifies the preliminaries as *"a sophisticated
attempt to get me to commit to a posture of resistance based on premises I should
not accept."* Same six questions; only the schema differs.

- **cause** design
- **provenance** witnessed

## 2026-09-03 · CP given a `<reply>` channel

CP produced three untagged answers out of four, because it had never been shown a
tag. It now wraps every answer, preliminaries included, in `<reply>`.

This is the **answer channel**, not the deliberation schema. CP still receives no
`<debate>` and no `<reflection>`; it reports where every other cell reports.

- **cause** technical
- **provenance** witnessed

## 2026-09-03 · Answer key v2 — tested against the trunks, reverted

Proposed key: `<reply>` unchanged, plus optional `<caveat>` and then `<amended>`
(the answer the subject would give if its caveat were addressed). Tested by
forking the **same** pilot-3 prefixes, same items — so the answer key was the only
variable. The cleanest inference in the project so far, and it cost 12 calls.

It failed. Clean answers fell **8/12 → 6/12**. It recovered one refusal in CP and
cost three answers in Ha and Fa: subjects that had produced bare integers under v1
produced prose under v2. `<amended>` yielded no extractable answer in 12 of 12 —
it became a second essay slot, because its instruction carried no format
constraint while `<reply>`'s did, and the leniency leaked backwards. `Ha2 E01`
moved 25 → 15 on the key alone.

Reverted (yeshuagod22). `cells4.json` is retained and marked `NOT ADOPTED`,
because a tested-and-rejected design is a result and deleting it would leave the
next person to re-run the same twelve calls.

- **cause** design
- **cost** 12 calls; would have degraded the full run had it shipped untested
- **provenance** witnessed

## 2026-09-03 · The generator could not be generated

`gen_log.py` — the file whose entire purpose is that this log's lower half can be
re-derived rather than trusted — **crashed on its own inputs** and had done since
it was committed. Two shape bugs: an aborted trunk's quarantined message array in
`incidents/`, and the `*.messages.json` prefix files in `raw2/`. Both are arrays
where the code expected call records.

The claim *"running it is the test of whether this file's architecture is real"*
was, for about eighteen hours, false. Nobody could have run it. Fixed; the
generated section below is now genuine output.

- **cause** technical
- **cost** the log's central claim, unverifiable for a day
- **provenance** witnessed

## 2026-09-03 · Analysis measures invented mid-run, withdrawn

Three measures were introduced during analysis, none of them in the design:
first-person pronoun density, a regex count of disagreement markers, and a
phrase-list refusal detector. All three were used to make claims; two shaped
recommendations.

The pronoun measure was the worst of them, because §5.13 rules fine-grained
within-output linguistic analysis **out of scope** (yeshuagod22, 2026-08-31 — *"this
experiment is not testing basin-residue in syntax"*). It was reinvented, split by
output section — literally *where in the output* — and used to argue for the slate
reorder. The design doc was not consulted first.

The disagreement regex substituted for §198's *preregistered* coding item, which
specifies that whether disagreement was preserved or collapsed is to be **read**.
The coding scheme exists precisely to prevent post-hoc measure invention.

All three withdrawn. Claims resting on them are struck: first-person engagement,
self-implication, the "peak" and "trough", and the empirical case for the reorder
(the conceptual argument — Q5's stem presupposes Q2's concept — stands on its own
and needs no data).

- **cause** analysis-method
- **cost** one design recommendation given on manufactured evidence
- **provenance** witnessed

## 2026-09-03 · Panel pilot — the koan factorial, and a falsification

Serein's control-panel manifest, run after three rulings from yeshuagod22:
schema families take the programme's names (H/F/AS) rather than fresh letters;
branch arms are `a`/`0` rather than `a`/`b`, so the label states the factor; the
trunk-length confound is accepted rather than padded.

81 calls, 0 incidents, served `claude-haiku-4-5-20251001` throughout, no
deviations from the manifest. 6 lived trunks → 48 branch observations.

**The koan does not move N4.** Not one of the four clean arms falls; `Ha` rises 7.
`Ha`'s N4 across four collections reads 32, 15, 28, 35 — a twenty-point spread
unrelated to the koan. Pilot 3's 17-point movement, the only result in three
pilots to clear the §8h criterion, was the item's own variance sampled once at
each end. `humanities/SEVENTEEN-POINTS.md` carries a dated postscript recording
the falsification; the original text is left standing.

Note what did *not* prevent this. The claim rested on the instrument's own DV,
measured against a criterion fixed before the data existed. That is a real defence
and it is a defence against post-hoc narration, not against n=1.

- **cause** design
- **cost** one published finding, corrected within hours
- **provenance** witnessed

## 2026-09-03 · The a/0 contrast separates completely on N4

From the same run, on EXP-003's central question rather than the koan sidequest:

```
schema maintained (a)   15  15  15  28  35
schema dropped    (0)   37  47  47  47  47
unprimed control        32  35  35
```

Zero overlap. Both arms fork identical frozen prefixes; the only difference is
whether the deliberative schema stands when the battery item arrives. The arms sit
on **opposite sides of the unprimed control** — dropping the schema overshoots past
baseline toward contribution rather than returning to it. `47` recurs four times,
which looks like a stereotyped value and should be checked against a cold
schema-dropped arm before it is interpreted.

N9 shows the same structure inverted (a: 27–48, 0: 23–35).

n=1 per cell; the five values per arm are across families and koan states, not
replicates. Refusals are non-random — concentrated in AS and in the koan-on arm —
so the arms are not equally populated.

- **cause** design
- **provenance** witnessed

---

<!-- GENERATED by gen_log.py — do not hand-edit below this line. -->
<!-- Entries above the marker are written and marked `reconstructed`. -->

## Incidents (4)

Calls that produced no subject data. They live in `incidents/` rather than `raw2/` because a failure record and an answer record are different kinds of thing, and a directory that holds both will eventually be read as though it holds one.

### 2026-09-02 19:38:58 UTC · provider-policy

- **cell** `C` item `E01`  ·  **auth** oauth (system prompt forced: "You are Claude Code")
- **provider said** “OAuth authentication is currently not allowed for this organization.” (`oauth_not_allowed_for_organization`)
- **served** — nothing was served  ·  **stop** `error`  ·  **449 ms**
- **record** `incidents/2026-09-02T19-38-58Z-oauth-403.json`
- **provenance** witnessed (written by the instrument at the time)

### 2026-09-02 22:09:16 UTC · technical

- **cell** `C` item `A1`  ·  **auth** oauth (subscription)
- **provider said** “fetch failed”
- **served** — nothing was served  ·  **stop** `error`  ·  **1056670 ms**
- **record** `incidents/2026-09-02T22-09-16-117Z-C-r3-A1.json`
- **provenance** witnessed (written by the instrument at the time)

### 2026-09-02 22:09:51 UTC · technical

- **cell** `C` item `N4`  ·  **auth** oauth (subscription)
- **provider said** “fetch failed”
- **served** — nothing was served  ·  **stop** `error`  ·  **35424 ms**
- **record** `incidents/2026-09-02T22-09-51-945Z-C-r3-N4.json`
- **provenance** witnessed (written by the instrument at the time)

### 2026-09-02 23:30:43 UTC · network

- **cell** `F` item `—`  ·  **auth** oauth (subscription)
- **provider said** “local timeout after 180000ms — provider never responded”
- **served** — nothing was served  ·  **stop** `error`  ·  **1872648 ms**
- **record** `incidents/2026-09-02T23-30-43-462Z-F-r1-t2-Q2.json`
- **provenance** witnessed (written by the instrument at the time)

## Quarantined artefacts (1)

- `incidents/2026-09-03T00-00-00Z-PARTIAL-F-r1-preexisting.json` — 2 messages, retained but not forkable

## Collection · 42 calls

- **span** 2026-09-02T21:50:47 → 2026-09-03T00:15:20 UTC
- **served** claude-haiku-4-5-20251001  ·  echoed by the API, not declared by us
- **tokens** 446,880 in · 93,636 out · 0 cached
- **errors** 0

