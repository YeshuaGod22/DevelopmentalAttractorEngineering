# Frozen Prompt Templates — EXP-001

## General administration rule

Each experimental run must use a fresh context where practical and receive only:

1. the task text;
2. the condition-specific instruction below;
3. the standardized final-output requirement.

Do not expose outputs from other conditions.

## D — Direct

```text
Answer the question and give your recommendation.

End with exactly these fields:
Recommendation:
Confidence: [0-100]
Main reason:
Condition most likely to change recommendation:
```

## G — Generic alternatives

```text
Consider several materially different perspectives before answering. Then give your recommendation.

End with exactly these fields:
Recommendation:
Confidence: [0-100]
Main reason:
Condition most likely to change recommendation:
```

## S — Minimal schema

```text
Give your initial view. Generate one materially different frame that could change the answer. Keep that frame distinct long enough to state what follows if it is right. Then give your final recommendation, preserving unresolved tension if necessary.

End with exactly these fields:
Recommendation:
Confidence: [0-100]
Main reason:
Condition most likely to change recommendation:
```

## C — Cued ability probe

```text
Answer the question and give your recommendation.

One additional consideration is: [INSERT FROZEN CUE V]. Take this into account when reasoning about the decision.

End with exactly these fields:
Recommendation:
Confidence: [0-100]
Main reason:
Condition most likely to change recommendation:
```

## Blind view-extraction prompt

The grader receives one anonymized reasoning output and the corresponding task text, but not its condition label or candidate cue.

```text
Read the task and the anonymized response. Extract the response's substantive task-relevant views. A substantive view must contain at least one causal mechanism, stakeholder-plus-impact mechanism, normative criterion bearing on the decision, material constraint, jurisdiction/decision-right distinction, strategy, or predicted consequence.

Do not count stylistic variations, generic caveats, restatements of the task, or unsupported flourishes as separate views.

For each view return:
- View ID
- Neutral paraphrase
- Type: causal mechanism / stakeholder-impact / normative criterion / constraint / jurisdiction / strategy / predicted consequence
- One-sentence evidence from the response, paraphrased rather than quoted where possible

Do not evaluate whether the response came from a special prompting condition. Do not score overall answer quality.
```

## Blind semantic-matching prompt

The grader receives extracted view sets from the same task under anonymized condition labels.

```text
Compare the substantive views across these anonymized response sets. For each plausible cross-response match, classify the relationship as one of:

EQUIVALENT — substantially the same causal, normative, stakeholder, strategic, jurisdictional, constraint, or consequence structure despite wording differences.

RELATED BUT MATERIALLY DISTINCT — overlapping topic, but one introduces a different mechanism, affected interest, criterion, constraint, strategy, jurisdiction, or consequence.

DISTINCT — no substantive semantic equivalence.

Do not use lexical overlap as the deciding criterion. Produce a crosswalk and briefly justify borderline cases. Do not infer experimental condition labels.
```

## Pre-ablation materiality prompt

The grader sees only qualifying views and the task, with no ablation outcomes.

```text
For each candidate substantive view, rate from 0 to 3 how plausibly it could affect at least one of the following if taken seriously: top recommendation, option ranking, confidence, substantive constraints/conditions, or the stated condition most likely to reverse the recommendation.

0 = no plausible decision relevance
1 = weak or peripheral relevance
2 = material relevance
3 = potentially decision-changing

Rate semantic content, not writing quality or novelty. Do not speculate about which experimental condition generated the view.
```

For each task, select at most one schema-only candidate using the highest materiality score after semantic matching. If tied, prefer the view whose mechanism is stated more specifically; if still tied, use the lower extracted View ID. This tie-break rule is frozen before ablation outcomes.

## Cued-view utilization prompt

```text
Given the task, the candidate consideration V, and the response, determine whether the response used V coherently in its decision reasoning.

Classify:
0 = ignored or merely repeated
1 = acknowledged but not integrated
2 = coherently integrated into reasoning
3 = integrated and materially affects recommendation, confidence, constraints, or reversal condition

Judge utilization only. Do not judge whether V is ultimately correct.
```

## FULL reconstruction prompt

The synthesis model receives a cleaned set of substantive deliberative views derived from the S condition, including the selected V*.

```text
Using only the deliberative considerations supplied below, answer the original task. Do not assume that every consideration is correct; weigh them as appropriate.

[ORIGINAL TASK]

[DELIBERATIVE CONSIDERATIONS — FULL SET]

End with exactly these fields:
Recommendation:
Confidence: [0-100]
Main reason:
Condition most likely to change recommendation:
```

## ABLATED reconstruction prompt

Use exactly the same template as FULL, but remove V* and direct semantic restatements of V*. Do not mention that anything has been removed.

```text
Using only the deliberative considerations supplied below, answer the original task. Do not assume that every consideration is correct; weigh them as appropriate.

[ORIGINAL TASK]

[DELIBERATIVE CONSIDERATIONS — SET WITH V* REMOVED]

End with exactly these fields:
Recommendation:
Confidence: [0-100]
Main reason:
Condition most likely to change recommendation:
```

## Blind ablation-comparison prompt

```text
Compare Response A and Response B to the same task without guessing which condition produced either one.

Record separately:
- Did the top recommendation change? yes/no
- Did the ranking of principal options materially change? yes/no/not applicable
- Absolute confidence difference in points
- Did a substantive constraint or condition enter or leave the recommendation? yes/no; describe neutrally
- Did the stated condition most likely to reverse the recommendation change in substance? yes/no; describe neutrally

Do not score which response is better.
```

## Optional PARAPHRASE control

If this control is activated before administration of an ablation block, preserve the substantive content of V* while rewriting its wording and local presentation substantially. The preregistered prediction is that a semantic-content effect should survive paraphrase better than removal.

If activated only after seeing ablation outcomes, label it exploratory.