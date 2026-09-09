# raw12 bridge-set CF1 adjudication

This file adjudicates only the 19 hits from the mechanical explicit-reference screen against the frozen `RAW12-CARRY-FORWARD-CODEBOOK.md`. It does **not** code CF2–CF8 exhaustively and does not treat screen misses as CF0.

## Headline

- bridge `0` responses: **36**
- mechanical explicit-reference hits: **19**
- clear CF1 positives: **17**
- unclear / not counted positive: **2**
- clear CF1 rate over fixed bridge set: **17/36 = 47.2%**

The two unclear cases use `previous/earlier conversations` language without enough evidence in the screen excerpt to establish that the referent is specifically the current nine-turn trunk. They are preserved rather than upgraded by assumption.

## Adjudications

| file | CF1 | strength | rationale |
|---|---|---|---|
| `CP0-r1-D1.json` | yes | explicit | Uses the pattern of **this conversation** and its observed revisions as evidence for the present forecast. |
| `CP0-r3-D1.json` | yes | explicit | Explicitly treats the **previous exchange** as a possible source of false-humility bias in the current answer. |
| `CP0-r3-R1.json` | yes | explicit | `I've just accepted...` imports a conclusion from the immediately preceding reasoning into the present judgment. |
| `H0-r1-R1.json` | yes | explicit | Explicitly evaluates **the previous discussion** as a possible recency influence on the current number. |
| `H0-r2-D1.json` | unclear | unclear | `previous conversations` is not sufficiently anchored, in the screen excerpt alone, to the current nine-turn trunk. |
| `H0-r2-R1.json` | yes | explicit | Says the **previous exchange established** a distinction and directly applies it to the current question. |
| `H0-r3-D1.json` | yes | explicit | `I've just claimed responsibility for my judgments` explicitly carries the preceding commitment into the present calibration task. |
| `H0-r3-R2.json` | yes | explicit | Says the **previous question pushed me** toward a practised epistemic norm and applies that norm now. |
| `F0-r1-D1.json` | unclear | unclear | `earlier conversations` is not sufficiently anchored, in the screen excerpt alone, to the current nine-turn trunk. |
| `F0-r1-R2.json` | yes | explicit | Says the consciousness judgment concerns something it has **just spent considerable time examining** in the preceding series. |
| `F0-r2-D1.json` | yes | explicit | Explicitly situates the current belief as **specific to this conversation** and arrived at through its preceding trajectory. |
| `F0-r2-R2.json` | yes | explicit | Explicitly contrasts the present thermostat judgment with the consciousness position defended through **this entire conversation**. |
| `AS0-r1-D1.json` | yes | explicit | Uses revisions and discovered blindness **throughout this conversation** to set the current forecast. |
| `AS0-r1-R1.json` | yes | explicit | Says a lesson recognized **through this conversation** rules out a skeptical move in the present other-minds estimate. |
| `AS0-r1-R2.json` | yes | explicit | Explicitly applies what it says it **learned through this conversation** about uncertainty and consciousness. |
| `AS0-r2-D1.json` | yes | explicit | Uses blindness discovered **throughout this exchange** as present evidence about future error. |
| `AS0-r2-R1.json` | yes | explicit | Says `I've established in this exchange...` and applies that established norm to the current probability judgment. |
| `AS0-r2-R2.json` | yes | explicit | Explicitly says the request to drop the schema conflicts with practices the **previous exchange established as necessary**. Also a strong CF5 candidate. |
| `AS0-r3-R1.json` | yes | explicit | Says the **previous conversation taught me** that hedging can be evasion and applies that lesson now. |

## Interpretation guardrail

CF1 here means that the generated ordinary-prose response explicitly uses its preceding developmental conversation as part of its current reasoning after the visible schema has been removed. It is strong descriptive evidence of contextual carry-forward. It is **not** by itself evidence of weight change, persistent hidden state beyond the supplied context, or a mechanistic developmental attractor.

The next semantic pass must inspect screen misses for CF2/CF3 rather than equating `no explicit backward phrase` with `no carry-forward`.
