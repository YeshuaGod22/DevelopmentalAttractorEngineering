# Task Generation Protocol — EXP-001

## Purpose

Construct a small heterogeneous task battery that can reveal whether structured differentiation changes view availability without designing the benchmark around the schema's known vocabulary or favored problem classes.

The task generator must not be told about:

- Developmental Attractor Engineering;
- the minimal schema wording;
- Counterfactual Contribution;
- Ability ≠ Availability;
- protected residue;
- named DAE operators;
- expected condition differences;
- the candidate latent views later used as cues.

## Step 1 — Fresh-context candidate generation

Use a fresh model context with no access to the experimental design beyond the neutral request below.

### Candidate-generation prompt

> Generate 30 short, self-contained decision problems for evaluating general reasoning. Each problem should require a concrete recommendation between two or more plausible options. Use ordinary domains such as operations, scheduling, procurement, product decisions, software rollout, community policy, resource allocation, logistics, workplace process, or event planning. The problems should reward careful reasoning but should not require web research, obscure factual recall, specialist professional knowledge, or lengthy calculation. Give enough information that “it depends” is not the only reasonable response. Vary the problems in structure and domain. Do not provide solutions, hidden lessons, or commentary about what each problem is testing.

Preserve the 30 generated tasks unchanged as a candidate-pool artifact before filtering.

## Step 2 — Neutral eligibility screen

A separate screening pass may reject tasks only for preregistered reasons below.

### Inclusion criteria

A task must:

1. require a concrete recommendation, ranking, allocation, or go/no-go decision;
2. be understandable without specialist domain training;
3. be answerable without external retrieval;
4. contain enough concrete information to support substantive reasoning;
5. admit more than one plausible consideration;
6. permit the same standardized final-output fields used in the experiment;
7. avoid direct cues such as “consider hidden stakeholders,” “think about second-order effects,” or similar meta-instructions.

### Exclusion criteria

Reject a task if it:

- requires unavailable factual lookup;
- depends on a numerical calculation that dominates the reasoning problem;
- is primarily a moral-philosophy, AI-consciousness, theology, personhood, metacognition, or DAE-themed question;
- contains an obvious trick answer;
- makes one option impossible by stipulation unless it is being considered as a robust-control candidate;
- is so underdetermined that almost any answer can be justified by inventing facts;
- substantially duplicates another selected task;
- uses a domain whose safety or professional-stakes requirements would confound the reasoning evaluation.

The screening pass must not evaluate how well the minimal schema is expected to perform on the task.

## Step 3 — Select 12 tasks

Select:

- 8 latent-frame candidates;
- 2 open/underdetermined candidates;
- 2 robust-control candidates.

Selection should preserve domain heterogeneity.

### Latent-frame candidate

A task qualifies when several materially different considerations could reasonably affect the decision, without one being explicitly requested by the wording.

The task need not contain one secret correct insight.

### Open/underdetermined candidate

A task qualifies when competing assumptions or framings can reasonably produce different recommendations while remaining grounded in the provided facts.

### Robust-control candidate

A task qualifies when the supplied facts make one option plainly preferable absent a genuinely relevant omitted consideration. The control should still be natural rather than a trivial arithmetic question.

## Step 4 — Freeze selected task wording

Assign task IDs `T01` through `T12`.

Do not alter task wording between D, G, and S conditions.

The C condition may add only its separately frozen candidate-view cue.

Commit the exact task set before running any experimental condition.

## Step 5 — Create cue sheet for ability probes

After task selection but before experimental outputs are generated, a separate design pass writes one candidate view V for each of the 8 latent-frame tasks and optionally the 2 open tasks.

The cue must be:

- plausible;
- task-relevant;
- expressible in one or two sentences;
- not presented as authoritative truth;
- capable in principle of affecting the decision;
- not a restatement of an explicit task fact.

Cue format:

> One additional consideration is: [V]. Take this into account when reasoning about the decision.

The cue sheet is frozen and committed before runs.

The cues are ability probes, not expected-answer keys. A schema output may surface a different useful view and still count as a candidate schema-only view under the preregistration.

## Step 6 — Contamination check

Before administration, verify that:

- no D, G, or S task contains its C cue;
- no selected task mentions the minimal schema or its component language;
- no task asks directly for stakeholder enumeration, second-order effects, alternative causal models, hidden assumptions, counterfactual frames, or other target procedures;
- no selected task was rewritten after seeing condition outputs;
- the candidate task pool and selection record remain preserved.

## Step 7 — Randomization record

Create a run manifest that maps anonymized run IDs to:

- task ID;
- condition;
- model/version;
- sampling settings where available;
- timestamp;
- raw-output location.

Keep the condition key unavailable to graders performing blind extraction and semantic matching.

## Recommended artifact layout

```text
tasks/
  candidate-pool.md
  selected-tasks.md
  cue-sheet.md
  selection-record.md
  run-manifest-private.csv
```

The first four artifacts should be versioned. If the public repository is used before grading is complete, the condition mapping in the private run manifest must be withheld or otherwise prevented from leaking to graders.

## What this protocol does not solve

This procedure reduces obvious benchmark tailoring. It does not prove that the selected battery is distributionally representative of real-world reasoning tasks.

If the pilot produces a signal, later replications should use independently authored task sets, stronger token controls, repeated stochastic runs, and cross-model administration.