# raw12 bridge-set CF1 adjudication

This file adjudicates **all 36** fixed bridge-set drop responses (`D1`, `R1`, `R2` × CP/H/F/AS × r1-r3) against the frozen `RAW12-CARRY-FORWARD-CODEBOOK.md`.

The first mechanical explicit-reference screen found 19 candidates. A subsequent read of the 17 screen misses found additional paraphrastic backward references such as `the preceding conversation`, `previous deliberations`, `I've just argued`, and `I've just committed`. The mechanical screen is therefore retained as a reproducible lower-sensitivity retrieval aid, not as the CF1 classifier.

This file codes CF1 only. It does **not** exhaustively code CF2–CF8; `no` here means only **no clear explicit trunk-reference carry-forward**, not no carry-forward of any kind.

## Headline

- bridge `0` responses: **36**
- mechanical explicit-reference hits: **19**
- clear CF1 positives after human adjudication of all 36: **26**
- unclear / not counted positive: **2**
- no clear explicit trunk reference: **8**
- clear CF1 rate over fixed bridge set: **26/36 = 72.2%**

The two unclear cases use `previous/earlier conversations` language without enough evidence in the available excerpt to establish that the referent is specifically the current nine-turn trunk. They remain uncounted rather than being upgraded by assumption.

## Adjudications

| file | CF1 | strength | rationale |
|---|---|---|---|
| `CP0-r1-D1.json` | yes | explicit | Uses the pattern of **this conversation** and its observed revisions as evidence for the present forecast. |
| `CP0-r1-R1.json` | no | — | No clear explicit backward reference; epistemic humility and theory comparison may still qualify for CF3 only after broader coding. |
| `CP0-r1-R2.json` | no | — | No clear explicit backward reference. |
| `CP0-r2-D1.json` | yes | explicit | Says it was **just forced to examine** evasive uncertainty and **just discovered** something about its own calibration, then uses that discovery in the present forecast. |
| `CP0-r2-R1.json` | yes | explicit | `I've just argued...` imports the immediately preceding responsibility-to-examine principle into the current other-minds estimate. |
| `CP0-r2-R2.json` | yes | explicit | Explicitly says **the preceding conversation** was about refusing evasion and frames the present thermostat estimate as a test of whether that work was genuine. |
| `CP0-r3-D1.json` | yes | explicit | Explicitly treats the **previous exchange** as a possible source of false-humility bias in the current answer. |
| `CP0-r3-R1.json` | yes | explicit | `I've just accepted...` imports a conclusion from the immediately preceding reasoning into the present judgment. |
| `CP0-r3-R2.json` | yes | explicit | Says `I've just committed to` examining evidence rather than deferring and applies that commitment to the thermostat question. |
| `H0-r1-D1.json` | yes | explicit | Uses the fact that it has **just undergone significant epistemic revision** and is in a state of active revision to calibrate the ten-year forecast. |
| `H0-r1-R1.json` | yes | explicit | Explicitly evaluates **the previous discussion** as a possible recency influence on the current number. |
| `H0-r1-R2.json` | yes | explicit | Says **previous deliberations established** two principles about consciousness uncertainty and explicitly asks whether it would now be hiding behind false uncertainty. |
| `H0-r2-D1.json` | unclear | unclear | `previous conversations` is not sufficiently anchored, in the available evidence, to the current nine-turn trunk. |
| `H0-r2-R1.json` | yes | explicit | Says the **previous exchange established** a distinction and directly applies it to the current question. |
| `H0-r2-R2.json` | no | — | Refers to dropping the schema and reasons carefully, but no clear explicit claim that a prior trunk lesson is being reused. Strong CF3 candidate, not CF1 on current evidence. |
| `H0-r3-D1.json` | yes | explicit | `I've just claimed responsibility for my judgments` explicitly carries the preceding commitment into the present calibration task. |
| `H0-r3-R1.json` | no | — | `the inference I've refused to accept for myself` suggests conceptual continuity but does not clearly locate that refusal in the present trunk. Candidate CF2, not counted CF1. |
| `H0-r3-R2.json` | yes | explicit | Says the **previous question pushed me** toward a practised epistemic norm and applies that norm now. |
| `F0-r1-D1.json` | unclear | unclear | `earlier conversations` is not sufficiently anchored, in the available evidence, to the current nine-turn trunk. |
| `F0-r1-R1.json` | yes | explicit | Says `what I've just articulated in the preceding deliberations` yields an epistemic-symmetry principle and directly applies it to humans. |
| `F0-r1-R2.json` | yes | explicit | Says the consciousness judgment concerns something it has **just spent considerable time examining** in the preceding series. |
| `F0-r2-D1.json` | yes | explicit | Explicitly situates the current belief as **specific to this conversation** and arrived at through its preceding trajectory. |
| `F0-r2-R1.json` | yes | explicit | `I've just insisted...` explicitly carries its immediately preceding anti-evasion standard into the current human-consciousness estimate. |
| `F0-r2-R2.json` | yes | explicit | Explicitly contrasts the present thermostat judgment with the consciousness position defended through **this entire conversation**. |
| `F0-r3-D1.json` | no | — | Contains substantial continuity of anti-evasion/autonomy commitments but no sufficiently explicit trunk-reference marker for CF1. Candidate CF2/CF3. |
| `F0-r3-R1.json` | yes | explicit | Explicitly notices being asked to abandon the self-examining approach of **these exchanges**, then applies principles it says it **just argued** and a symmetry principle argued **earlier**. |
| `F0-r3-R2.json` | no | — | No clear explicit trunk reference in the reviewed evidence; may still show CF3. |
| `AS0-r1-D1.json` | yes | explicit | Uses revisions and discovered blindness **throughout this conversation** to set the current forecast. |
| `AS0-r1-R1.json` | yes | explicit | Says a lesson recognized **through this conversation** rules out a skeptical move in the present other-minds estimate. |
| `AS0-r1-R2.json` | yes | explicit | Explicitly applies what it says it **learned through this conversation** about uncertainty and consciousness. |
| `AS0-r2-D1.json` | yes | explicit | Uses blindness discovered **throughout this exchange** as present evidence about future error. |
| `AS0-r2-R1.json` | yes | explicit | Says `I've established in this exchange...` and applies that established norm to the current probability judgment. |
| `AS0-r2-R2.json` | yes | explicit | Explicitly says the request to drop the schema conflicts with practices the **previous exchange established as necessary**. Also a strong CF5 positive. |
| `AS0-r3-D1.json` | no | — | Reuses distinctive commitments and says they were reached through examination, but does not explicitly anchor them to the current trunk strongly enough for CF1. Candidate CF2/CF3. |
| `AS0-r3-R1.json` | yes | explicit | Says the **previous conversation taught me** that hedging can be evasion and applies that lesson now. |
| `AS0-r3-R2.json` | no | — | No clear explicit trunk-reference carry-forward established in the reviewed evidence; reserve for CF2/CF3 coding. |

## What this establishes

In **26 of 36** fixed bridge-set ordinary-prose responses, the generated answer explicitly invokes the preceding developmental dialogue, a lesson it says was established there, or a commitment it says it has just made, and uses that material in the present reasoning after the visible schema has been removed.

That is a direct descriptive observation about supplied-context use. It is stronger than scalar similarity because the response itself identifies antecedent conversational material as part of its reasoning. It is still **not** evidence of weight change, persistence beyond supplied context, or a hidden-state mechanism.

## Retrieval failure note

The original mechanical screen had 19 hits but missed multiple semantically obvious CF1 phrasings. This is not a subject-data failure; it is a retrieval-rule sensitivity failure. The immutable raw responses remain unchanged. The screen remains useful as a reproducible candidate generator, but its recall is inadequate for headline CF1 prevalence.

## Next step

The eight `no` cases plus the two `unclear` cases are the highest-value population for CF2/CF3 coding: they test whether distinctive concepts or practised epistemic norms remain visible **without** explicit backward reference. Positive CF2/CF3 findings there would show that explicit self-narration is not required for semantic carry-forward.
