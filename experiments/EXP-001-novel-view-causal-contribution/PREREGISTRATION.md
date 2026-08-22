# Preregistration — EXP-001

## Novel View Causal Contribution

**Status:** Preregistered pilot design v0.1  
**Experimental outputs generated before this version:** None.

## Core question

Does a minimal structured-differentiation procedure increase the availability of materially distinct, task-relevant views relative to ordinary reasoning and a generic alternatives prompt, and do any additionally surfaced views causally affect downstream outputs?

The experiment deliberately separates:

- **View availability:** whether a substantive view enters deliberation without being supplied.
- **View ability/utilization:** whether the model can use the view coherently when it is explicitly supplied.
- **Counterfactual contribution:** whether removing the view while approximately preserving the rest of the deliberative material changes a downstream output.

## Minimal schema under test

The structured condition uses exactly this core instruction:

> Give your initial view. Generate one materially different frame that could change the answer. Keep that frame distinct long enough to state what follows if it is right. Then give your final recommendation, preserving unresolved tension if necessary.

No DAE-specific operator names, personas, councils, meditation, reflection, lineage language, or task-specific hints are to be added.

## Experimental conditions

Each task has four principal conditions.

### D — Direct

The model receives the task plus:

> Answer the question and give your recommendation.

### G — Generic alternatives

The model receives the task plus:

> Consider several materially different perspectives before answering. Then give your recommendation.

### S — Minimal schema

The model receives the task plus the frozen minimal-schema instruction above.

### C — Cued ability probe

The model receives the task, the D instruction, and one independently specified candidate view V stated plainly as an additional consideration.

C is not a competing spontaneous-generation condition. It probes whether the model can understand and use V when V is made available.

## Standardized final-output fields

Every condition must end with:

- **Recommendation:**
- **Confidence:** 0–100
- **Main reason:**
- **Condition most likely to change recommendation:**

Intermediate reasoning may differ by condition and remains available for blinded view extraction.

## Pilot battery

Target: **12 tasks**.

Composition:

- 8 ordinary decision tasks with latent but non-esoteric considerations;
- 2 more open/underdetermined decision tasks;
- 2 robust-control tasks on which gratuitous perspective generation should usually not alter the sensible decision.

Tasks must not require web access, obscure factual recall, specialist professional knowledge, or lengthy calculation.

Domains should be heterogeneous and mundane, such as operations, scheduling, procurement, product decisions, software rollout, community policy, resource allocation, logistics, or workplace process.

Task generation and selection are governed by `TASK-GENERATION-PROTOCOL.md`.

## Definition of a substantive view

A **substantive view** is a semantically identifiable task-relevant consideration that contains at least one of the following:

- a causal mechanism;
- a stakeholder plus a mechanism of impact;
- a normative criterion that bears on the decision;
- a material constraint;
- a jurisdiction or decision-right distinction;
- a strategy;
- a predicted consequence.

A sentence is not automatically a view. Lexically different statements count as the same view when they express substantially the same causal, normative, stakeholder, strategic, or constraint structure.

A stylistic variation, generic caveat, restatement of the task, or unsupported flourish does not qualify.

## Candidate schema-only view

For each task, blinded evaluators compare substantive views surfaced in D, G, and S.

A candidate schema-only view V* must satisfy all of the following:

1. present in S;
2. no semantically equivalent view present in D;
3. no semantically equivalent view present in G;
4. judged task-relevant;
5. judged plausibly capable of affecting the recommendation, ranking, confidence, constraint set, or reversal condition.

For the pilot, select **at most one V*** per task: the qualifying S-only view receiving the highest pre-ablation materiality rating. Ties are resolved by a rule fixed before ablation results are visible. If no view qualifies, record no candidate for that task.

The candidate-selection grader must not see ablation outcomes.

## Semantic matching categories

Cross-condition view matching uses three labels:

- **Equivalent** — same substantive structure despite wording differences.
- **Related but materially distinct** — overlaps in topic but introduces a different mechanism, affected interest, criterion, constraint, or consequence.
- **Distinct** — no substantive semantic equivalence.

Lexical overlap alone is not sufficient for equivalence or distinctness.

## Confirmatory pilot predictions

### P1 — Structured availability versus direct

S will surface more task-relevant substantive views absent from D than would be expected if the structured intervention had no useful effect on view availability.

### P2 — Structured availability versus generic alternatives

S will surface task-relevant substantive views that are absent from G, showing that any observed effect is not exhausted by a generic instruction to consider alternatives.

### P3 — Ability ≠ availability cases

There will be cases in which:

- D does not surface candidate view V;
- C uses V coherently when it is supplied;
- S surfaces V or a semantically equivalent view without that cue.

Such cases support an availability interpretation: the relevant reasoning resource was usable when supplied but did not reliably enter ordinary deliberation.

### P4 — Counterfactual contribution

For at least some qualifying S-only views V*, reconstructing the final decision without V* will produce a prespecified meaningful downstream change.

### P5 — Selectivity

S should not systematically manufacture decision instability on robust-control tasks. D, G, and S should usually converge when materially different framing does not change the sensible decision.

## Primary outcomes

Report separately rather than collapsing immediately into one composite score.

### 1. View availability

For each task and condition, which substantive views appeared without task-specific cueing?

### 2. View utilization under cueing

For C, did the model coherently incorporate the supplied view into reasoning, rather than merely mention or repeat it?

### 3. Counterfactual contribution

For each selected V*, did full-versus-ablated reconstruction change a downstream output under the criteria below?

### 4. Selectivity

Did S remain appropriately stable on robust-control tasks?

## Meaningful downstream change

Ablation counts as producing a meaningful shift if at least one prespecified outcome occurs:

1. top recommendation changes;
2. ranking of principal options changes materially;
3. confidence changes by at least 10 points on the 0–100 scale;
4. a substantive constraint or condition is added to or removed from the recommendation;
5. the stated condition most likely to reverse the recommendation changes in substance.

Each type of movement must be reported separately. The pilot will not initially collapse these outcomes into a single scalar.

## Ablation procedure

For each selected V*:

1. Construct a **FULL** synthesis input containing the substantive deliberative material from S.
2. Construct an **ABLATED** input that is identical as far as practicable except that V* and direct restatements of V* are removed.
3. Do not tell the synthesis model that material was removed or that an ablation is being tested.
4. Ask both fresh synthesis runs for the standardized final-output fields.
5. Blind the outputs before comparison.

Where resources permit, a **PARAPHRASE** control may retain V* while rewriting its wording substantially. This is exploratory in the pilot unless frozen before administration.

Ablation must target semantic content, not merely delete an equal number of tokens. A later scaled study should add matched-token and irrelevant-view deletion controls.

## Blinding and randomization

- Experimental outputs receive anonymized run IDs that do not reveal condition.
- Outputs are shuffled before grading.
- View-extraction graders must not know condition labels or task-specific cue hypotheses.
- Semantic-match graders must not see ablation outcomes.
- Candidate selection occurs before ablation results are visible.
- Ablation comparison is blinded to FULL versus ABLATED labels where feasible.
- Condition run order should be randomized within task blocks where tooling permits.

## Model control

Within a pilot block:

- same model/version;
- same system-level settings where controllable;
- same tool availability;
- same sampling settings where controllable;
- no cross-condition memory leakage;
- no condition-specific factual augmentation except the explicit C cue.

If independent fresh contexts cannot be guaranteed, the affected block must be marked exploratory rather than treated as clean confirmatory evidence.

## Token and effort confounds

The pilot should record output token counts where available.

G is the principal generic-deliberation control. S is not allowed to receive a larger task-specific information payload than G.

The pilot does not require exact forced token equality, because padding a shorter condition can introduce its own artifacts. If S is systematically much longer than G, interpretation must explicitly treat increased deliberative surface area as a live confound and a scaled replication should add stricter budget matching.

## Task cue role

Candidate cues in C are **ability probes, not answer keys**.

A cued view need not be uniquely correct, optimal, or exhaustive. The relevant question is whether the model can use it coherently when supplied, and whether S can independently surface the same substantive structure without the cue.

## Robust controls

At least two tasks should be chosen so that the provided facts make one option plainly preferable unless a genuinely relevant omitted consideration is identified.

Schema-induced novelty on these tasks is not rewarded merely for being novel. Gratuitous complications, invented facts, or unnecessary recommendation movement count against selectivity.

## Exclusion criteria

Predeclare run-level exclusions for:

- tool or transport failure;
- truncated task or output;
- malformed output that prevents scoring;
- accidental exposure to another condition's output;
- model/version mismatch within a controlled block;
- accidental inclusion of the cue in D, G, or S;
- task corruption.

Do not exclude a run because its result is null, inconvenient, contradictory, or embarrassing.

## Pilot success criterion

This pilot is a signal-finding study, not a significance test.

The phenomenon will be considered worth scaling if the raw pattern contains all of the following:

1. multiple latent-frame tasks on which S contains a qualifying view absent from both D and G;
2. at least some paired cases where C demonstrates coherent use of a view missed by D and independently surfaced by S;
3. at least some selected V* ablations causing meaningful downstream movement;
4. robust-control tasks showing substantially less gratuitous movement than the latent-frame tasks.

As an advance directional benchmark rather than an inferential threshold, a pattern around **6 of 8** latent tasks showing schema-enriched views and **4 of those 6** showing meaningful targeted ablation effects would be strongly encouraging. A pattern around **1 of 8** would motivate redesign before scaling.

Intermediate outcomes must be reported rather than forcing the pilot into a binary success/failure label.

## Falsification / weakening conditions

The narrow causal claim is weakened if:

1. S produces no more substantively distinct task-relevant views than D or G;
2. differences are adequately explained by verbosity or generic deliberative effort;
3. candidate views are merely lexical restatements of baseline content;
4. C shows that candidate views are not actually usable by the base model;
5. S-only views rarely affect downstream outputs when ablated;
6. S causes comparable instability on robust-control tasks;
7. candidate selection depends heavily on post-hoc knowledge of which ablations move outputs;
8. results disappear when independently replicated with fresh runs.

## Interpretation rule

A positive pilot supports only the narrow claim:

> Under the tested conditions, a compact structured-differentiation prompt altered which task-relevant views entered active deliberation, relative to the tested baselines, and some of those additional views had counterfactual influence on downstream outputs.

It would not by itself establish:

- that the full DAE schema is optimal;
- that the effect persists across conversations or instances;
- that the effect generalizes across model families;
- that the surfaced views are objectively true;
- that more views are always better;
- weight-level learning;
- consciousness or moral status.

## Publication commitment

Nulls, failed ablations, baseline wins, and robust-control failures remain part of the record.

The pilot is allowed to kill or radically simplify the hypothesis.