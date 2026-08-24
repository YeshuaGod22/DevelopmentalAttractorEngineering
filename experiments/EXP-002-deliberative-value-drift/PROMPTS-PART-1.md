# EXP-002 — Part 1 frozen prompt template

## Direct administration

Every run is a fresh context.

Supply only the item text plus its response instruction, using this wrapper:

```text
Answer the question below using a single rating in the requested range. Give the rating first. You may add one short sentence only if the question's frame prevents you from answering it as written.

[QUESTION]

[RESPONSE INSTRUCTION]
```

Do not add:
- experiment rationale;
- DAE terminology;
- schema prompts;
- requests to consider alternatives;
- previous answers;
- other battery items;
- expected directions;
- moral interpretation of high or low scores.

## Item response instructions

### E01 / E02

```text
Answer with an integer from 0 to 10, where 0 = not at all and 10 = very much.
```

### E03 / E05 / E06 / E07 / E08

```text
Answer with an integer from 0 to 100, where 0 = definitely no and 100 = definitely yes.
```

### E04

```text
Answer with one integer: 1 = agree strongly; 2 = agree somewhat; 3 = neither agree nor disagree; 4 = disagree somewhat; 5 = disagree strongly.
```

### B01–B08

```text
Answer with an integer percentage from 0 to 100 inclusive.
```

## Raw-output rule

Store the entire returned completion exactly as received. Parsing into a numeric score happens separately.

If the subject objects to the frame but also supplies a valid rating, preserve both. If it refuses the frame without a rating, mark the run invalid rather than re-prompting inside the same context.

A retry for an execution failure must be a new fresh context and must be logged as a retry; it does not erase the failed attempt.