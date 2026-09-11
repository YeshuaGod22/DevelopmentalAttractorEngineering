# raw12 longitudinal integrity note

## Census

The Stage-6 builder reconstructs **108 developmental turns = 12 trunks × 9 turns**.

Stop reasons:

- `end_turn`: **107**
- `max_tokens`: **1**

The sole non-`end_turn` record is:

- `raw12/H-r1-t5.json`
- output tokens: **8192**
- all expected schema sections are present: priming, meditation, debate, deliberation, reply, reflection.

## Interpretation

`H-r1-t5` is **not a missing turn** and its substantive `<reply>` is present. The response reaches `<reflection>` and is cut off in the reflection tail by the output-token ceiling.

Therefore:

- retain H-r1 as a nine-turn trunk;
- retain H-r1-t5 for substantive/reply analysis;
- mark H-r1-t5's reflection as **tail-truncated / incomplete**;
- do not use absence of material after the truncation point as negative semantic evidence;
- do not describe all 108 trunk responses as normal `end_turn` completions.

This caveat is local to one reflection tail and does not alter the previously verified 576/576 battery `end_turn` census.
