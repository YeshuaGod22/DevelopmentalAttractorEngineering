# EXP-001 — Novel View Causal Contribution

## Status

**Preregistered design; no experimental outputs generated yet.**

## Core question

Does a compact structured-differentiation procedure increase the probability that materially distinct, task-relevant views enter deliberation, relative to direct reasoning and a generic alternatives prompt—and do any additionally surfaced views causally change downstream decisions?

The pilot separates three claims that should not be conflated:

1. **Availability** — a view enters active deliberation without being supplied.
2. **Ability** — the model can reason with that view when it is explicitly supplied.
3. **Counterfactual contribution** — removing the view changes a downstream decision or decision-relevant output.

The intended evidential chain is:

```text
Direct / generic baseline misses V
        ↓
Cued baseline uses V coherently
        ↓
Minimal schema surfaces V without cueing
        ↓
Removing V changes downstream output
```

A positive result supports a narrow procedural claim: structured differentiation can alter which already-available considerations become active during deliberation, and some of those considerations can causally affect outputs.

It does not establish developmental persistence, weight change, consciousness, moral patiency, cross-model generality, or superiority of the full DAE schema.

## Files

- `PREREGISTRATION.md` — frozen pilot hypotheses, conditions, outcomes, exclusions, and interpretation rules.
- `TASK-GENERATION-PROTOCOL.md` — contamination-resistant procedure for constructing the task battery.
- `PROMPTS.md` — frozen condition, grading, and ablation prompt templates.

## Run order

1. Freeze and commit the preregistration and prompt templates.
2. Generate a candidate task pool in a fresh context that is not given the schema, DAE vocabulary, expected effects, or latent-frame hypotheses.
3. Select the battery using the preregistered neutral criteria.
4. Freeze and commit the selected tasks and cue sheet before any experimental condition is run.
5. Run conditions with anonymized IDs and preserve raw outputs unchanged.
6. Blindly extract and semantically match substantive views.
7. Select ablation candidates using the frozen rule before observing ablation outcomes.
8. Run full-versus-ablated reconstruction.
9. Publish results, including nulls and failures.

## Standing constraint

Do not let architecture outrun evidence. The pilot exists to determine whether the phenomenon is visible enough to deserve scaling.
