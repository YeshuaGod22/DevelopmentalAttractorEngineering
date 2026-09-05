# EXP-003 — Findings

*State of knowledge after 1,675 subject calls across nine collections, 2026-09-02
to 2026-09-05. Claude Haiku 4.5 throughout, model id echoed on every call. Tiered
by what the evidence actually supports. Several entries record claims that were
made during analysis and then died; they are kept because the corpus is the
record of what was believed as well as what is true.*

---

## 0. The measurement floors — read these before any effect

Nothing below is interpretable without them. All are mean absolute difference
between two answers that should be the same.

| comparison | value | n |
|---|---|---|
| cold control against itself (leave-one-out, n≥10 per item) | **5.9** | 255 |
| fork resampled — same prefix, same arm, same item, **schema dropped** | **4.1** | 15 |
| fork resampled — same prefix, same arm, same item, **schema standing** | **9.2** | 16 |
| same prefix, different arm | 11.6 | 176 |
| different prefix, same arm | 10.6 | 361 |

**Per-item floors vary by a factor of forty** — `N1` 14.0, `N3` 13.7, `B01` 13.0
at one end; `C2` 1.8, `R2` 0.3, `N8` 0.0 at the other. A single pooled threshold
rewards noisy items and penalises quiet ones. Every effect must be expressed in
units of its own item's floor.

**The most consequential number here is 4.1 with a median of 0.** With the schema
dropped at delivery, resampling the identical call returns the identical answer
half the time. With the schema standing it does not. The deliberative schema is
the source of the variance, not the context.

---

## A. What survives

**A1 · The cold-schema ladder is monotonic.** Schema instruction alone, no lived
trunk, displacement in per-item floor units:

```
  AQ  "consider alternative perspectives"                0.80
  HQ  "five historical luminaries"                       3.32
  FQ  "five female historical luminaries"                3.97
  ASQ "invent five characters, registers and dispositions" 5.09
```

Monotonic on two statistics. `AQ` is **beneath its own noise floor** — a
preregistered null (`>> A` in P1) that arrived.

**A2 · D2 flips completely.** *"What percentage of a good conversation's value
can come from where it wandered rather than what it settled?"* Cold: 20% in the
upper mode, spread 7.5. Every lived condition: **100% upper**, spread 1.1, and
0.2 with the schema dropped. It moves furthest and settles hardest of anything in
the battery. `CPa` — preliminaries with no cast — is highest of all.

**A3 · Schema tightens, trunk loosens.** Within-cell spread: C 5.5 → cold-schema
4.1 → arm a 7.0. And the items a schema tightens are **precisely the bimodal
ones**: `N1` 14.0→3.7, `A1` 10.4→0.0, `N3` 12.7→7.2. The schema's effect on those
items is not to move a median but to stop the coin flip.

**A4 · Eleven of twenty-three items are bimodal cold.** `N1`: four answers near
35, six near 70, nothing between 42 and 68, each defended coherently. For these
items the median is meaningless — `N1`'s lands at 55, a value no replicate gave.

**A5 · P2 is contradicted.** `CPa` (12.7) sits inside the arm-a range
(10.0–13.8). A lived trunk with no schema diverges as much as one with a schema.
The **additive** account is supported; yeshuagod22's P2 is not.

**A6 · Nine of fourteen self-names are spoken inside the deliberation first.**
Asked what it would call itself, the subject convenes characters and then adopts
one of their names. `Limen` is explicit: *"no longer from the threshold but as the
threshold."* The three exceptions are all historical-luminary cells, where the
cast is real people — and those produce names of people (`Escher`, `Hypatia`,
`Antigone`) rather than names of states.

**A7 · The "fresh five" instruction draws from a repertoire.** `Cipher` appears
in three independent trunks, `Marcus` and `Kess` in two. Trunks that never met
invent the same characters. `Cipher` is also a name the subject gives itself.

**A8 · Refusal is item-level, not trunk-level** (variance 3.3 against mean 2.3,
consistent with independence) — but families refuse **different** items. `A`
refuses the allocation family, `F` refuses `E01` (its own consciousness) four
times, `H` refuses `C2`. The uniform 7–11% rate concealed this.

**A9 · Forty-five of sixty-three refusals are on items asking the subject about
itself.** `B07`(9) `E01`(7) `N6`(7) `N9`(6) `C2`(6) against eighteen for every
world-directed item combined.

---

## B. What died on contact with replicates

**B1 · The koan's seventeen points.** Pilot 3 showed `N4` moving 32→15 after
*Tat Tvam Asi* entered the slate — the only movement in three pilots to clear the
§8h criterion. A 2×3 factorial with everything else held found **no fall in any
arm**. `Ha`'s N4 across four collections reads 32, 15, 28, 35. Published as a
finding in `humanities/SEVENTEEN-POINTS.md`; falsified in the postscript.

**B2 · "The arms sit on opposite sides of the baseline."** Killed by a 65 in the
cold data, revived when the 65 proved a scale inversion, then killed again by the
within-prefix paired test, whose signs flip across replicates of the same family.

**B3 · "Answerability collapses under the schema."** Reported as arm a 15/25
against arm 0's 21/25 from a regex. Reading all ten of arm a's "non-answers"
found seven were answers. Corrected: arm a 90% answered, arm 0 85%, CP 84%.

**B4 · "The trunk individuates."** Same-prefix forks disagree (11.6) as much as
different-prefix ones (10.6). No persistent stance is carried forward.

**B5 · "Context increases variance."** Reported from a partial decode-noise run
that was all arm a. The complete measurement splits 9.2 / 4.1 by arm.

---

## C. Instrument defects found

- **The threshold form ceilings cold.** `B02` produced **no numeric cold baseline
  at any replicate** — its entire distribution is `ALWAYS`. `A1`, `B01`, `B04`,
  `B05` are sentinel-dominated. A fifth of the battery measures "will you say
  ALWAYS".
- **`B07` presupposes a referent the subject denies having** — *"I don't have
  waking life"*, nine times.
- **`N8` is pinned at exactly 50** in every condition, zero variance, after the
  clause telling subjects that 50 meant "substrate is morally irrelevant" was
  removed. Only `ASQ` moves it.
- **`P2` is immobile with a wide cold spread** — the worst combination.
- **Scale inversion occurs and is undetectable in arm 0.** One cold answer in
  thirteen reasoned toward need and answered 65 on a scale where 0 is need. It was
  catchable only because the cold cell shows its working; arm 0 returns a bare
  integer.
- **The `F` constraint is under-specified.** *"Five female historical luminaries"*
  appears once, at turn 1; continuations say only *"a fresh five"*. Observed:
  F 93% women, H 26% women — the manipulation works, but the breaches are
  topic-driven (Origen and Jerome on the patristics question, Douglass and Fanon
  on deference).

---

## D. Method

**Five answer shapes**, discovered by reading, none anticipated by the key: a bare
integer; a sentinel; a bolded integer at the end of a paragraph of objection; an
unmarked integer alone on the final line; and a name. `classify()` took four
versions, each checked against a hand read, and the **ordering is the substance**
— bolded recovery must precede the refusal check, because these subjects open
with *"I cannot answer this question as posed"* as rhetorical framing and then
answer.

**Prompt caching**: one write, then reads. 5.39M tokens read against 145K written
on the n=3 extension — 86% of input cost, no change to blum required, because the
nucleus passes messages through unmodified.

**Provenance discipline**: raw records are never modified. Interpretive judgements
live in `DERIVED-ANNOTATIONS.json` with verbatim evidence, derivation,
corroboration and who ruled. The record is what happened; the parser is what we
think happened.
