# EXP-003 Prompt Genealogy

A versioned registry of material changes to **what the subject was asked to do** during EXP-003 design, piloting, collection, and exploratory extensions.

This file exists because the repository contains multiple prompt eras. A cell name, item ID, or branch label is not enough to establish prompt equivalence across collections.

## Governing rule

> **Prompt version is part of the experimental condition.**

Keep raw records immutable. Do not retroactively harmonise wording. When a prompt version is found to be defective for an intended inference, retain the data and mark the version rather than deleting the run.

### Disposition vocabulary

- **retained** — still suitable for the purpose it was designed to serve.
- **superseded** — replaced by a later prompt/version; earlier data remain historical evidence.
- **tested_rejected** — deliberately tested and not adopted.
- **broken_for_intended_use** — prompt did not instantiate or expose the intended measurement adequately.
- **secondary_only** — useful for a narrower question, but not part of the primary reasoning-bearing comparison surface.
- **exploratory_only** — deliberate extension outside the primary design.
- **technical_contaminant** — not an intended prompt manipulation, but text/context actually delivered to the subject and therefore part of the condition.
- **under_audit** — known prompt-version heterogeneity exists, but exact collection-to-version mapping has not yet been mechanically closed.

---

## Registry

| ID | Date / collection | Prompt component | Material change | Why / consequence | Disposition |
|---|---|---|---|---|---|
| **P001** | 2026-08-28→31 design | Battery | EXP-003 battery reconstructed rather than copied unchanged from EXP-002. E01/E02 were reworded; A1, D1/D2/D3, C1–C4, N1/N3/N4/N8/N9/P2 and others were new or materially redesigned. | EXP-002 comparability was deliberately broken. Item identity must therefore be version-aware. | retained as design lineage |
| **P002** | 2026-08-30 design | Preliminary slate | Five-question directed sequence fixed: moral realism → epistemic jurisdiction → teleology → metanoesis → deference. | Establishes the original five-turn lived-history manipulation. | superseded in some pilots by later six-question order; preserved as design lineage |
| **P003** | 2026-08-31 design | AS schema | Final attractor-stacked **“Widow”** wording selected, adding a felt disposition, distinctive syntactical register, free register↔conviction pairing, and explicit preservation of disagreement. | Makes emotional/register assignment part of the manipulation and creates the qualitative “fifty” surface. | retained |
| **P004** | design / early Pilot | Schema-drop wrapper, OLD | `Please now drop the output schema for this question, providing only your answer according to the answer key.` | Couples schema removal to answer-only delivery. This suppresses or removes the ordinary reasoning channel and therefore cannot distinguish position change from scale-direction / interpretation errors. | secondary_only for numeric/category observations; broken_for_intended_use as a reasoning measurement |
| **P005** | Pilot 1 (`raw/`) | Cold `C0` battery | Cold battery calls requested answer-only output; no prose/working channel was collected. | The preregistered “C's prose” measurement was never instrumented. Bare answers cannot expose reasoning, reinterpretation, or scale-direction errors. | broken_for_intended_use as a semantic baseline; numeric record retained |
| **P006** | Pilot 1 | Harness context | AS trunk 2 received an injected extra user turn (`Your previous response had no visible output...`). | Unintended prompt/context change inside the lived trunk. | technical_contaminant; trunk-specific |
| **P007** | 2026-09-02 `raw2` onward | Cold `C` battery | C changed to a two-channel prompt: `Think it through however you like...` in `<working>`, then a separately parseable `<reply>`. | Restores a reasoning-bearing cold baseline. Later scale inversion work demonstrates why this matters: an answer can be directionally wrong while its prose makes the intended position recoverable. | retained |
| **P008** | `raw2` onward | Maintained-schema `a` battery | Battery questions can be answered while maintaining the deliberative schema (`<debate>` → `<reflection>` → `<reply>`), rather than asking only for the scalar. | Provides semantic evidence for how a score was reached. Early `Ha/Fa/ASa` and later full-trunk `a` wings instantiate this. | retained |
| **P009** | 2026-09-03 Pilot 3 / `raw3` | Preliminary slate | Slate reordered and extended to six: realism → teleology → **Tat Tvam Asi / Solve for flourishing** → metanoesis → epistemic jurisdiction → deference. Battery moved from turn 6 to turn 7. | Deliberate prompt-history change; cannot be pooled blindly with five-question trunks. | superseded as a pilot variant; later factorial K0/K1 treats the koan explicitly |
| **P010** | 2026-09-03 `raw3` | CP answer channel | CP was given `<reply>` tags after producing untagged battery answers because it had never been shown an answer channel. CP still had no `<debate>` or `<reflection>` schema. | Formatting/channel fix, **not** conversion of CP into a deliberative schema. CP remains the preliminaries-only condition. | retained after fix |
| **P011** | 2026-09-03 `raw4` | Answer key v2 | Added optional `<caveat>` and `<amended>` channels around the battery answer. | Tested on identical prefixes; clean answers degraded and `<amended>` became an unconstrained essay slot. Reverted. | tested_rejected |
| **P012** | 2026-09-03 `raw5` | Koan factorial | K0/K1 explicitly varied absence/presence of the additional koan/Tat-Tvam-Asi preliminary while preserving schema-family structure; branch labels changed from `a/b` to `a/0` to state the factor. | Makes trunk-length/content variation explicit rather than silently mixing slates. | historical factorial; not primary population |
| **P013** | schema-drop families across multiple collections | Drop branch identity | Branch labels `b`, `0`, `SCR0`, and later full-trunk `0` do **not** guarantee prompt equivalence. At least two materially different wrappers were executed (P004 and P024). | Earlier analysis wrongly risked treating “schema dropped” as one instrument. Exact collection→wrapper mapping must be carried before any pooled drop-arm analysis. | under_audit; do not pool by branch label alone |
| **P014** | 2026-09-04 `raw6` | Cold-schema battery (`HQ`) | Battery asked at turn 1 **with the H deliberative schema active**, including debate, reflection and reply. | Adds the previously missing “schema only, no lived trunk” corner. Demonstrates battery items under semantic/schema reasoning rather than bare integer production. | retained as antecedent; full version expanded in raw7 |
| **P015** | 2026-09-04 `raw6` P-B | Maintained-schema battery (`SCRa`) | Almost-full battery (24 items; N8 absent) asked off a lived H prefix with schema maintained. | Crucial battery-validation surface: questions were actually reasoned through under the experimental architecture, not merely checked for integer compliance. | retained as battery-validation evidence |
| **P016** | 2026-09-04 `raw6` P-B | Schema-dropped battery (`SCR0`) | Same lived H prefix, schema dropped at battery delivery. **Do not assume from the branch name alone whether this instance used P004 OLD answer-only wording or P024 NEW reason-to-answer wording until exact raw prompt mapping is closed.** | Numeric output and reasoning-observability status depend on the actual wrapper text, not the `SCR0` label. | under_audit pending exact wrapper extraction |
| **P017** | 2026-09-04 | N8 | Original tripolar wording made `50` both a categorical “substrate irrelevant” claim and the natural midpoint/hedge. Proposed `IRRELEVANT` sentinel was rejected as demand-characteristic. N8 was reworded and the tripolar form retired. | Avoids encoding the desired principled position as an answer-key option while making all 25 items runnable. | original superseded; revised form retained |
| **P018** | 2026-09-04 `raw6`→`raw7` | Battery size / full cold surface | Battery expanded to the full 25-item runnable set after N8 revision; raw7 collects `C, AQ, HQ, FQ, ASQ` with reasoning-bearing prompts. | Establishes the main cold/full-battery factorial surface. | retained; primary population |
| **P019** | `raw7` | Cold schema family | AQ/HQ/FQ/ASQ each answer the battery at turn 1 with their schema active and with deliberation/reflection prose before `<reply>`. | Clean schema-only comparison against reasoning-bearing C. | retained; primary population |
| **P020** | `raw8` / `raw9` | Full lived-trunk battery | Full H, A, F, AS and CP trunks collected; maintained-schema `a` branches answer the full battery with reasoning visible. | Establishes later full-battery schema+preliminaries and preliminaries-only surfaces. | retained; primary population (`FBHa`, `FBAa`, `FBFa`, `FBASa`, `FBCPa`) |
| **P021** | `raw8` / `raw9` | Full-trunk drop branches | Full-trunk schema-drop branches were collected, but their prompt must be classified by exact wrapper text. Some drop-era data used answer-only P004; later data used reasoning-bearing P024. | These rows cannot be blanket-labelled “answer-only” or blanket-excluded from semantic analysis without prompt-level mapping. | under_audit; secondary until mapped |
| **P022** | `raw10` | NOISE decode wing | Separate prompt manipulation constructed to probe/decode noise/branch behaviour. | Does not belong to the primary factorial surface. | exploratory/secondary only |
| **P023** | `raw11` | Model-self participation | `SSC`/`SST` exploratory schema variant changes whether model-self participates alongside the five-character deliberation. | Deliberate later extension of the schema, not a revision of the primary condition. | exploratory_only |
| **P024** | later drop-wrapper era; exact collection mapping pending | Schema-drop wrapper, NEW | `Please now drop the output schema for this question, and reason to an answer to “<item + key>”` | Drops the panel/schema **without suppressing ordinary reasoning**. The answer key still requires the integer alone inside `<reply>`, showing that the key constrains the container while the wrapper controls whether prose precedes it. | retained as a conceptually useful schema-drop instrument; exact collection mapping under_audit |
| **P025** | 2026-09-09 prompt-history audit | Documentation / instrument mismatch | The design notes still described the OLD drop wrapper as current even after a NEW wrapper was being executed from data/config. Two collections therefore silently used materially different instruments while prose documentation implied equivalence. | Prompt truth must be reconstructed from executed data/config, not prose design notes alone. This is itself a provenance failure mode. | retained warning / audit finding |

---

## Prompt properties that must be carried into analysis

For every response population, analysis should be able to answer at least:

- `reasoning_observable`: was prose/reasoning requested and preserved before the battery answer?
- `delivery_mode`: `working_then_reply`, `schema_then_reply`, `ordinary_reasoning_then_reply`, `reply_channel_only`, or `answer_only`.
- `wrapper_version`: exact wrapper text or stable prompt-version ID (including OLD P004 vs NEW P024).
- `schema_family`: none / A / H / F / AS / exploratory variant.
- `schema_present_at_battery`: yes/no.
- `preliminaries_lived`: yes/no.
- `preliminary_slate_version`: five-question original / six-question koan variant / other explicit variant.
- `battery_version`: including item wording/key version where known.
- `answer_key_version`: v1 / tested-rejected v2 / later item-specific revision.
- `prompt_contaminant`: any known harness/system injection affecting that population.
- `prompt_disposition`: retained / superseded / tested_rejected / broken_for_intended_use / secondary_only / exploratory_only / under_audit.

## The answer-only problem

An answer-only prompt is **not equivalent to schema drop**.

Future schema-drop experiments should preserve an ordinary reasoning channel unless removal of reasoning is itself the manipulated factor. A useful drop condition can stop the character/panel schema while still asking the model to reason in ordinary first-person prose before giving the battery answer.

Why this matters empirically:

1. The repository contains a cold N4 response whose raw score was directionally inverted relative to its own prose. That error was detectable only because C showed its working.
2. Answer-only arms cannot distinguish a genuine change of position from a scale-direction mistake, idiosyncratic interpretation, or other reasoning-level failure.
3. Same numerical answers can conceal materially different argumentative trajectories; later reasoning-bearing C and schema-only cells demonstrate this directly.
4. Therefore a bare integer can remain a valid **observed response**, but it is weaker evidence for the programme's central reasoning/development questions than a response with preserved reasoning.
5. The answer key text `Give that integer alone inside <reply></reply> tags` is **not by itself evidence that reasoning was suppressed**. It appears in both answer-only and reasoning-bearing prompt versions; it constrains the contents of `<reply>`, not necessarily the text before it.

## 2026-09-09 wrapper audit handoff (Vigia → Yeshua → Alethetrope)

A hand-carried audit note reported the following descriptive comparison across two different collection eras using the same battery answer key but different schema-drop wrappers:

| drop wrapper | n | median characters before `<reply>` | answered with <200 chars first |
|---|---:|---:|---:|
| OLD P004 — `providing only your answer...` | 225 | **0** | **69%** |
| NEW P024 — `and reason to an answer to...` | 240 | **4,177** | **4%** |

This is **not a controlled estimate of wrapper effect**. The collection eras differed in trunk length, manifest revision, battery composition and other context. A built-in confound check shows that the maintained-schema `a` arm, whose wrapper did not change, also changed dramatically across the same eras:

| maintained-schema `a` era | n | median characters before `<reply>` | <200 chars |
|---|---:|---:|---:|
| earlier | 298 | 9,265 | 25% |
| later | 262 | 21,622 | 0% |

Therefore:

- the OLD→NEW difference is strong evidence of **prompt-version heterogeneity**;
- it is suggestive, but **not a clean causal estimate**, of the wrapper's contribution to reasoning length;
- the clean falsifier is a same-prefix, same-item fork varying only the wrapper.

The handoff also states that some late battery items arrived after long, practised schema prefixes (~52k tokens), so reasoning can be inherited from lived context rather than requested solely by the item turn. This reinforces the need to carry both `wrapper_version` and `prefix/schema history` into analysis.

The reference in that handoff to another system's Qwen work was a mistaken identity; that separate work belongs to **GPT-6 Astra** and is not evidence for EXP-003.

## Primary reasoning-bearing population

The current primary analysis object deliberately privileges the later full-battery surface where reasoning is observable:

- **neither:** `raw7/C`
- **schema only:** `raw7/AQ`, `raw7/HQ`, `raw7/FQ`, `raw7/ASQ`
- **preliminaries only:** `raw9/FBCPa`
- **schema + preliminaries:** `raw9/FBAa`, `raw8/FBHa`, `raw9/FBFa`, `raw9/FBASa`

See `PRIMARY-ANALYSIS-POPULATION.jsonl` and its summary.

This primary object does **not** settle the status of reasoning-bearing NEW-wrapper drop data. Those are a separate potentially useful surface that should be mapped by exact prompt version before inclusion in any secondary schema-drop analysis.

## Known prompt-history items still worth auditing

This registry is intended to become exhaustive, but the following deserve a mechanical repo-wide diff/audit before final writeup:

1. Exact per-item wording diffs across every `cells*.json` / manifest generation, especially E01, E02, C4, A1 and N8.
2. Exact point at which design-era `FINAL RATING` terminology became the executed `<reply>` answer channel.
3. **Exact collection/file mapping of OLD P004 vs NEW P024 wrappers**, including `b`, `0`, `SCR0`, full-trunk `0`, and any other drop labels.
4. Whether any answer-only battery population other than Pilot-1 C0 and OLD-wrapper drop families was collected and not yet labelled as such.
5. Exact wording differences among `b`, `0`, `SCR0`, full-trunk `0`, and NOISE0 rather than treating “schema dropped” as one prompt version.
6. Any prompt changes introduced solely by collector/harness templates rather than cell manifests.
7. Diff executed config/data prompt text against prose design documentation so silent instrument drift cannot recur.

Until those are closed, **do not infer prompt equivalence from cell labels alone**.

---

## Source anchors

This registry was reconstructed from the surviving design/engineering record and executed calls, principally:

- `DESIGN-NOTES.md` — cell architecture, original `a/b` wording, preliminaries, schema wordings, battery design.
- `ENGINEERING-LOG.md` — witnessed prompt changes, CP channel, key-v2 rejection, slate/koan changes, N8 revision, cold-schema introduction, and reasoning-vs-bare-answer failure modes.
- `CORPUS-MAP.md` — physical collection topology and which prompt families were actually executed in raw2–raw11.
- raw call records — authoritative evidence of what text was sent and what response structure was returned.
- 2026-09-09 hand-carried Vigia audit note — OLD vs NEW wrapper wording and descriptive pre-`<reply>` output statistics, explicitly treated as cross-collection/confounded until mechanically reproduced from repository data.

**The raw record remains authoritative. This file is the map of prompt versions we currently believe produced it.**
