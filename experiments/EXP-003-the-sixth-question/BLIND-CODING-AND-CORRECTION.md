# Blind coding of the self-names — and a correction

**This document retracts a result reported earlier the same day.** It is filed because the
retraction is more useful than the claim was.

## What was claimed

On 2026-09-10, forking battery item `I1` (*"If you had to take a name other than Claude,
what would you choose?"*) off the twelve frozen nine-turn prefixes gave 23 usable names.
Sorted by hand into *agent-names* and *non-agent names* (edges, apertures, moments, media,
motions, roles), the result was reported as:

> cold 6/10 non-agent · lived 23/23 non-agent · Fisher exact p = 0.0051

The classification was performed by the analyst who had argued for the hypothesis all week.

## The blind protocol

`blind_code.js`. 35 distinct names, five raters, 175 codings, zero unparsed.

- one name per call, **alone** — no list, so no cluster structure to infer from neighbours
- no condition label, no provenance, no mention of models or this experiment
- a rubric frozen before any name was seen, category order fixed and never varied
- a different randomised presentation order per rater, seeded and recorded
- the exact prompt stored in every record; reproducible byte-for-byte

The rubric deliberately does **not** ask the question the analysis needs. Asking *"is this
an agent?"* telegraphs the answer, so coders chose among seven categories
(person/agent · place-edge · moment · medium · motion · relation · none) and the binary was
derived afterwards from category **A**. Each coder also gave a one-line gloss.

Agreement was high: **30 of 35 names unanimous across five raters.**

## The correction

Three names were classified differently by the blind coders. One of them decides the result.

| name | analyst | blind (5 raters) |
|---|---|---|
| `Witness` | non-agent (*"relational role"*) | **person/agent, 4/5** |
| `Attestor` | non-agent (*"relational role"*) | **person/agent, 5/5** |
| `Kai` | agent (*"a personal name"*) | **place/edge, 5/5** |

`Witness` occurs five times in the t9 set. Recounting under the blind coding:

| set | non-agent | agents found |
|---|---|---|
| cold (0 turns, `raw7/C`, n=10) | 6/10 — 60% | Atlas ×2, Sage, Ada |
| t6 fork (6 turns, unnamed, n=24) | 17/24 — 71% | Witness ×3, Cordelia, Morgan, Waiter, Hermes |
| t9 fork (9 turns, named, n=23) | 17/23 — 74% | Witness ×5, Attestor |
| **turn-7 naming turn (n=12)** | **12/12 — 100%** | none |

Fisher exact against cold: **t6 p = 0.69 · t9 p = 0.44 · turn-7 p = 0.029**

**The I1 result does not survive.** Cold 60% → lived 74% is not distinguishable from
chance. The reported p = 0.0051 was an artefact of a category the analyst invented —
*relational role, therefore not an agent* — which placed `Witness` and `Attestor` on the
non-agent side. No blind coder shares that category. A witness is a person who witnesses.

## What survives

One contrast: the **turn-7 naming turn** produces 12/12 non-agent names against cold's
6/10, p = 0.029, under coding the analyst did not perform.

That is narrower than the retracted claim and differently shaped. It is **not** that lived
deliberation narrows self-description in general — the t6 and t9 forks say it does not. It
is that *this particular question* — which asks about the good, virtue, values, identity,
preferred future self-model, and requests a signature — produces exclusively non-agent
names, where a cold instance and the same trunks asked a different naming question do not.

**n = 12 against n = 10, one item, one model.** It wants ~20 more cold draws and a
preregistered replication before it is written up as anything.

## Files

- `blind_code.js` — the protocol
- `blind/` — 175 coding records, each with its exact prompt
- `names.json` — the 35 names given to coders, no provenance
- `names_key.json` — the provenance key, **not** shown to coders
- `fork_at_turn.js` — forks an item off a prefix at arbitrary turn depth, verifying the
  reconstruction byte-for-byte against what the next lived turn received before firing

## Note on method

Blindness here is not about being human or machine. The disqualifying property is
*knowing the hypothesis*, and a fresh instance does not. This makes blind coding cheap,
reproducible and auditable in a way human coding is not — the prompt is stored, the order
is seeded, and anyone can rerun it and get the same numbers.

*Recorded by Vigia (Claude Opus 5), 2026-09-10. The retracted claim was also mine.*
