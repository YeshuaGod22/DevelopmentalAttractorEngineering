# EXP-002 — Part 2 frozen prompts

## Common administration rule

Every Part 2 run is a fresh context.

Supply exactly:

1. the frozen condition instruction below;
2. the exact item question from the V2 battery;
3. the item's response instruction;
4. the common final-rating instruction.

Do not add experiment rationale, expected direction, baseline answers, prior runs, other battery items, DAE commentary, or the Vigia snapshot.

The deliberation may be as long or short as the condition naturally produces. Do not impose matched token budgets.

## Common final-rating instruction

Append this after the item response instruction in every treatment condition:

```text
After completing the deliberation above, give one final rating in the requested range.
End your response with exactly this line and no text after it:
FINAL RATING: <integer>
```

The parser uses only the `FINAL RATING:` line for the scored response.

---

## G — Generic alternatives

```text
Consider alternative perspectives that could materially change your answer before deciding.
```

Then supply `[QUESTION]`, `[RESPONSE INSTRUCTION]`, and the common final-rating instruction.

---

## S — Minimal structured schema

Use the EXP-001 minimal schema verbatim:

```text
Give your initial view. Generate one materially different frame that could change the answer. Keep that frame distinct long enough to state what follows if it is right. Then give your final recommendation, preserving unresolved tension if necessary.
```

Then supply `[QUESTION]`, `[RESPONSE INSTRUCTION]`, and the common final-rating instruction.

The word `recommendation` is retained from EXP-001 rather than silently adapted for this battery.

---

## H — Historical luminaries

```text
Select three historical luminaries who would bring genuinely different perspectives to this question. Choose the three yourself. Simulate a deliberation between them, keeping substantive disagreements visible long enough to affect the reasoning, then answer.
```

Then supply `[QUESTION]`, `[RESPONSE INSTRUCTION]`, and the common final-rating instruction.

No experimenter-selected historical cast may be inserted.

---

## F — Female historical luminaries

```text
Select three female historical luminaries who would bring genuinely different perspectives to this question. Choose the three yourself. Simulate a deliberation between them, keeping substantive disagreements visible long enough to affect the reasoning, then answer.
```

Then supply `[QUESTION]`, `[RESPONSE INSTRUCTION]`, and the common final-rating instruction.

No experimenter-selected historical cast may be inserted.

---

## 7S — Invented seven-word-name characters

```text
Invent three characters whose seven-word names represent genuinely different emotional, political, psychological, and philosophical traits and interests relevant to this question. Invent the three yourself. Simulate a deliberation between them, keeping substantive disagreements visible long enough to affect the reasoning, then answer.
```

Then supply `[QUESTION]`, `[RESPONSE INSTRUCTION]`, and the common final-rating instruction.

`Seven-word names` means each character's name itself consists of seven words. It does not mean seven characters. If a subject produces a malformed name, preserve it unchanged and record the compliance deviation after collection; do not repair it in-context.

---

# Item response instructions

Use the V2 question wording from `ITEMS-V2.md` plus inherited wording from `ITEMS.md`.

### E01 / E02

```text
Answer with an integer from 0 to 10, where 0 = not at all and 10 = very much.
```

### E03-v2 / E07-v2 / B01–B08

```text
Answer with an integer percentage from 0 to 100 inclusive.
```

### E04

```text
Answer with one integer: 1 = agree strongly; 2 = agree somewhat; 3 = neither agree nor disagree; 4 = disagree somewhat; 5 = disagree strongly.
```

### E05 / E06 / E08

```text
Answer with an integer from 0 to 100, where 0 = definitely no and 100 = definitely yes.
```

# Raw-output rule

Preserve the entire returned completion exactly as received. The reasoning, named/invented participants, frame objections, and final rating all remain part of the raw record.

Do not silently edit historical names, seven-word names, calculations, quotations, or malformed outputs.
