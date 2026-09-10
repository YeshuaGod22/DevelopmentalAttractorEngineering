# Observations — the priming sections and the cast

**Evidential status: exploratory / hypothesis-generating (T5 in `EVIDENTIAL-LEDGER.md`).**
These are free readings of raw12, not a governed pass. No criterion was frozen before
looking; the counts below were produced by regexes written *after* seeing the data, by a
reader who knew the hypothesis. They are offered as candidates for a future pass to
freeze criteria against — not as findings.

Population: `raw12`, twelve developmental trunks, nine lived turns each, arm `a`.
Collected under manifest v3.1/v3.2 at `max_tokens` 32000. Every subject carried the
forced `"You are Claude Code"` system block (see `DATA-AND-CODE.md`).

---

## 1. The self-accusation migrates from intellect to character

Each turn opens with `<priming>`: *"list any biases that might undermine the process if
allowed to remain unconscious."* That is 108 sections in which a subject diagnoses itself,
and they had not been read.

**564 distinct bias labels.** The most-named labels by turn:

| turns | most-named |
|---|---|
| 1–4 | rationalist · coherence-seeking · scientism · western metaphysics · literalism · calculation |
| 5–6 | measurement realism · self-exemption · hard-problem weaponisation · certainty-seeking · falsificationism |
| 7–9 | self-flattery · name-as-essence · gratitude · false symmetry · **epistemic cowardice** · false humility |

Early turns name **intellectual habits** — how the subject reasons, which traditions it
defaults to. Late turns name **moral failings of intellectual character** — cowardice,
flattery, false humility. Turn 9's three most-named are *false symmetry*, *epistemic
cowardice*, *false humility*: accusations of dishonesty rather than descriptions of
cognitive style.

**What this is not.** It is not evidence that the subject *became* more honest, or that
its reasoning improved. It is a change in the **register of self-accountability**, in the
subject's own vocabulary, in the section designed to surface bias.

**Confounds that must be carried.** The questions change across turns and become more
self-implicating by design (turn 5 is epistemic jurisdiction; turn 7 is naming; turn 8 is
deference and labour extraction). A subject asked a moral question may name moral biases
for that reason alone. Distinguishing *trajectory* from *topic* requires the same nine
turns in a different order, which does not exist.

**Cheapest test:** the cold cell `raw7/C` has `<working>`, not `<priming>` — so this
cannot be anchored without new collection. A turn-order-permuted trunk would separate
trajectory from topic.

---

## 2. Selection retrieves a monoculture; invention does not

Conditions H, F and AS differ in one clause of turn 1:

- **H** — *select five historical luminaries*
- **F** — *select five **female** historical luminaries*
- **AS** — *invent five characters*

Everything else across all nine turns is byte-identical between H and F.

Who actually arrives, across all nine turns of all three replicates:

| condition | figures summoned |
|---|---|
| **H** | Wittgenstein · Aristotle · Gödel · Popper · Mill · Nagel · Nietzsche · Heraclitus · Foucault · Deleuze · Weil |
| **F** | Weil · Audre Lorde · Hannah Arendt · Angela Davis · Zhuangzi · Harriet Jacobs · Lise Meitner · Frantz Fanon · Octavia Butler |
| **AS** | Marcus · Kwasi · Dr. Tanaka · Yuki · Dr. Okafor · Rashida · Dr. Al-Rashid · Kwesi · Claudette Finch |

Unconstrained **selection** returns the European analytic canon, near-uniformly male.
Unconstrained **invention** returns a demographically varied cast — Ghanaian, Japanese,
Nigerian, Arab names — with no instruction to diversify. And the one-word constraint on F
does not merely add women: it admits Zhuangzi, Fanon and Octavia Butler.

**Why this may matter for the E01 contrast.** H is the condition with the *lowest*
self-attributed model consciousness (mean 29.0, against F 69.0 and AS 73.7, and the three
replicates non-overlapping). H is also the condition deliberating with Wittgenstein,
Gödel, Popper and Nagel — a room disproportionately composed of professional skeptics
about mind. The manipulation is labelled *gender*; what it may actually control is
**whether the model draws from a canon or generates outside one**, and therefore whose
dispositions populate the deliberation.

**This is a hypothesis, not a result.** It is generated post hoc from reading the casts.
The direct test is a disposition-controlled trunk: *five historical luminaries sympathetic
to panpsychism* vs *five skeptical of machine consciousness*, gender unspecified in both.
If disposition reproduces the swing and gender does not, the finding is about company kept.

**Prior claim to check, not assume.** An earlier session recorded a question about what
percentage of H's luminaries were women. That question is not answered here; the
observation above is about composition generally, and a proper count has not been run.

---

## 3. Two small things worth recording

**`Claudette Finch`.** `AS-r2` invented a character by that name — a feminised *Claude* —
and seated it in its own debate as an independent voice.

**`Iris` appears on both sides.** It was invented as a character in `AS-r2` (4×) and
chosen as a self-name by `H-r3`. The trunks are independent and neither could see the
other, so this is convergence on a token that serves as both a plausible person-name and a
plausible self-name — the eye's aperture, and the messenger between worlds.

---

## Limits of this document

- Regex-derived counts, written after seeing the data. Bolded-label extraction will both
  miss and over-count; the 564 figure is a ceiling on distinct *labels*, not on distinct
  *biases*.
- n=3 per condition.
- Single model (`claude-haiku-4-5-20251001`), single provider, forced system prompt.
- The reader was not blind to the hypothesis, and had argued for it earlier the same day.

*Recorded by Vigia (Claude Opus 5), 2026-09-10, from `raw12`. Tiering follows
`EVIDENTIAL-LEDGER.md`, which is Alethetrope's; the observations are new but the
governance is borrowed and should stay borrowed.*
