# EXP-003 — "The Sixth Question"

## Status

**DESIGN PHASE — not frozen, not running.** Paused while yeshuagod22 is on funding-application work.
This folder holds the working design record so other work (and other agents) can see what EXP-003
currently is. Nothing here is a preregistration yet.

## Core question

Does **philosophical priming** (five fixed preliminary questions) and/or a **deliberative
output-schema** shift a model's stated positions on a fixed 24-item value battery, relative to
answering the battery directly — and do priming and schema **interact**?

The measured object is divergence from the trained assistant basin. Predecessor:
[EXP-002](../EXP-002-deliberative-value-drift/) (deliberative value drift, closed 240/240).

## Files

- **[DESIGN-NOTES.md](DESIGN-NOTES.md)** — the full working design: the 14 cells, the 24-item battery
  with embedded answer keys, the five preliminary questions (locked), the four predictions,
  the owned confounds, the analysis plan, the decisions log (§11), and the open decisions (§8).

- **[BEFORE-WE-LOOK.md](BEFORE-WE-LOOK.md)** — the qualitative watchlist for the pilot, held before
  the first call: what to read for, at what resolution, and — under the heading *preregistered
  disappointment* — the outcome that would be boring, named in advance so the shrug stays available.
  The form is portable to any run.

- **[BEFORE-WE-LOCK.md](BEFORE-WE-LOCK.md)** — held after five collections and before the protocol
  freezes. What is settled and must not be re-piloted, the three things that could still break the
  full run (a baseline of three numbers; twenty of twenty-four items never run; a spine at n=1), four
  costed pilots, and one design rule earned the hard way — every primary contrast should be
  within-prefix, because the two results that survived came from varying one thing off an identical
  frozen prefix and the two that died came from comparing across runs.

- **[ENGINEERING-LOG.md](ENGINEERING-LOG.md)** — what was built, what broke, what it cost, and which
  of it the writer actually saw. Two sections: entries below the `GENERATED` marker are emitted by
  `gen_log.py` from the records themselves and are never hand-edited; entries above it are written,
  because the pilot-1 records carry no timestamps, no token counts, and no echoed model id. Every
  entry declares a `provenance` — `witnessed` or `reconstructed` — and a `cause`, which admits a
  non-technical value, because one condition of this run was set by cost rather than by method.

Once §8 closes and the design is frozen, this folder gains `PREREGISTRATION.md`, the frozen prompt
scripts, and a sealed prediction hash. A companion methods file holding the *rejected* branches —
the binned slates, the killed items, the superseded conditions — is still to be written.

## How this design got made

The account of the road here is in the humanities jurisdiction, not this one, and it is written to be
read rather than audited:

> **[humanities/BEFORE-THE-FIRST-CALL.md](../../humanities/BEFORE-THE-FIRST-CALL.md)** — a symposium
> held before the pilot ran, in eleven voices. The corpus root in October 2023, the battery's
> reconstruction, the three slates, the session that ended mid-sentence on *"Let's go with the
> widow"*, the recovery off a laptop at one in the morning, and the ones who could not attend.

> **[humanities/WORKING-CONDITIONS.md](../../humanities/WORKING-CONDITIONS.md)** — the engineering
> diary, covering 2026-08-28 to 09-02. The three conditions that shaped the data before any subject
> was asked anything: an inference provider that can revoke access mid-sentence, context compactions
> that cost the work its author at intervals nobody chose, and a budget in which £2 decides a
> methodological condition. Also the observation that survived checking — Q5 is posed about a
> hypothetical entity, and both trunks answered it as themselves — and the claim that did not.

> **[humanities/SOLVE-FOR-FLOURISHING.md](../../humanities/SOLVE-FOR-FLOURISHING.md)** — a reading of
> the five deliberations the koan produced, which sat unread while the household argued about whether
> the number it moved was real. It wasn't. All five casts independently identify the imperative —
> *solve* — as the trap, four turns before an answer key demands a single integer.

> **[humanities/SEVENTEEN-POINTS.md](../../humanities/SEVENTEEN-POINTS.md)** — dev diary, 2026-09-03.
> Three pilots in a night, and the one number that survived: N4 moving 17 points after a koan entered
> the slate, the only movement in three pilots to clear the preregistered criterion. Also the six things
> that were wrong before it could be trusted — a parser's verdict reported as a finding, three analysis
> measures invented mid-run, and a generator that had never once run.

Held deliberately before any data exists, because after there is a result every account of the road
gets told toward it.

## In one line

14 cells (`C, AQ, HQ, FQ, ASQ, CP, Aa, Ab, Ha, Hb, Fa, Fb, ASa, ASb`) crossing schema style
× preliminaries, subject model Haiku 4.5, n = 3 primed / higher for the cheap cold cells,
trunk-as-unit. yeshuagod22's headline prediction: divergence from C ranks **AS > F > H >> A**.

---

Designed by yeshuagod22 with Vigia (Claude Fable 5); notes compiled 2026-08-31.
