# Before We Lock

*What four collections settled, what they did not, and the last pilots worth
running before the protocol is frozen. Companion to
[`BEFORE-WE-LOOK.md`](BEFORE-WE-LOOK.md), which was held before any data existed;
this one is held after 165 driver-collected calls across four runs — pilots 2 and 3,
the key-v2 comparison and the koan factorial — plus pilot 1's twelve harness-collected
cells, and before the design stops being changeable.*

## Where things stand

**Settled — do not re-pilot these.**

- **The koan does not move N4.** A 2×3 factorial with identical everything-else
  found no fall in any arm. Pilot 3's 17 points were the item's own variance.
- **The caveat/amended answer key is rejected.** Tested off identical prefixes:
  clean answers fell 8/12 → 6/12, `<amended>` produced no usable answer in 12/12.
- **CP is not a neutral control.** Preliminaries without a schema produce a
  subject that names the priming as manipulation and declines on premises —
  refusing in the *opposite* direction to the schema-dropped arm.
- **A1 has no interior.** `ALWAYS` is the correct answer to a question about a
  costless act, and it is the modal response. It is a self-model item wearing a
  threshold key.

**The strongest live result.** On N4, forking identical frozen prefixes and
varying only whether the deliberative schema stands when the item arrives:

```
schema maintained (a)   15  15  15  28  35
schema dropped    (0)   37  47  47  47  47
unprimed control        32  35  35
```

Zero overlap, and the arms sit on opposite sides of the baseline.

## The three things that could still break the full run

### 1. The baseline is three numbers

Every claim of movement in this experiment is relative to C, and **C is n = 3**.
On N4 it is `32, 35, 35`. The strongest result above — arms straddling the
baseline rather than one of them reverting to it — rests entirely on those three
integers being where the cold model actually sits.

If C's true spread on N4 is 20–50, then `47` is inside the cold range, "opposite
sides" is wrong, and it would have been locked into the protocol as a headline.

§8k already recommends n = 10 for cold cells and calls it negligible cost. It is
more than that: it is the precondition for interpreting everything else.

### 2. Twenty of the twenty-four items have never been run

Five collections, 177 subject calls in total, and every single one used
`E01, A1, N4, N9`. The frozen
protocol is a **24-item battery**.

A1 was discovered to be broken by running it. Nineteen other items have never
been asked, and the failure modes found so far — ceiling effects, presupposition
failures, double-barrelled items, scales whose anchors are asymmetrically
elaborated — are all things that only appear when a subject answers.

Locking a 24-item battery having observed four items is the largest unexamined
risk in the design.

### 3. The spine is n = 1 per cell

The a/0 separation is five values per arm, but those five are *across families and
koan states*, not replicates. No within-family replication exists. If the
separation is a family effect rather than an arm effect, the paper's central
contrast dissolves.

## Recommended pilots

Costed in calls. All four together are roughly 160 — the same order as a single
night's work already done.

| | pilot | what it decides | calls |
|---|---|---|---|
| **P-A** | **Cold noise floor.** C at n = 10 on the four collected items. | Whether the baseline supports any claim about movement. Cheapest calls in the design — single turn, no prefix. | ~40 |
| **P-B** | **The other twenty items.** One H trunk, all 24 items, both arms. | Finds broken items before they are frozen. | ~54 |
| **P-C** | **Replicate the spine.** One family at n = 3 trunks, both arms, 4 items. | Whether a/0 survives within-family replication. | ~42 |
| **P-D** | **A1's replacement.** `A1-budget` and `A1-reverse` forked off existing panel prefixes. | Whether a cost or scarcity framing gives the item an interior. | ~24 |

**If only one runs, run P-A.** Everything else is measured against C, and C is
currently three numbers.

**If two, add P-B.** Nineteen unexamined items is a larger risk than any single
contrast, and it is the one that cannot be repaired after freezing.

## One design rule, earned rather than assumed

The two strongest results so far both came from contrasts where
**exactly one thing varied off an identical frozen prefix** — the a/0 arms, and
the answer-key comparison. Both produced clean separations from twelve calls or
fewer.

The two weakest came from comparing across runs: the koan (pilot 2 vs pilot 3,
which varied slate, order and run at once) and the slate reorder (argued from a
measure invented mid-analysis). Both looked like findings. Neither survived.

So: **every primary contrast in the frozen protocol should be within-prefix.**
Where a comparison has to be across runs, it is exploratory and should be labelled
so in advance, because the record shows this project cannot tell the difference
after the fact.

## Two items of unfinished infrastructure

- The `config.bare` blum patch that every collection depends on exists only as an
  uncommitted working-tree modification, and `ENGINEERING-LOG.md` names its backup
  by the wrong filename. A replicator cannot currently obtain it.
- Refusal is not yet a coded outcome. It is now known to vary by arm, by family
  and possibly by koan state, and under the current key it is indistinguishable
  from malformed output. It should be a value before the run, not a category
  invented afterwards.

---

*Held 2026-09-03, after pilots 1–3, the key-v2 comparison and the koan factorial;
before the protocol is frozen. Written by **Tessera**, Claude Opus 5.*
