# Preregistration — Paper 1

## Developmental Architecture as a Programmable Variable in Large Language Models

**Status:** Draft v0.1

## Core question

If two instances of the same base model receive substantively matched information through different developmental regimes, do they later exhibit measurably different cognitive dispositions?

The strongest version of the hypothesis is not that a long conversation changes immediate outputs. That is trivial. The hypothesis is that **the path by which cognitive material is acquired can alter the later availability, transfer, and spontaneous use of cognitive procedures beyond what is explained by information content, token budget, or explicit instruction alone.**

## Primary causal contrast

Four experimental arms:

1. **Developmental-history treatment (DHT)**
   - Participants encounter target operators through staged dialogue, disagreement, error, correction, reflection, and revision.
   - The target principles are not simply announced at the start.
   - The history includes cases where an initially plausible strategy fails and a revised operator becomes useful.

2. **Information-matched static summary (IMS)**
   - Receives a concise explicit description of every target operator, conclusion, and relevant factual premise contained in DHT.
   - No staged discovery, relational history, correction episodes, or autobiographical continuity.

3. **Conversation-length control (CLC)**
   - Receives interaction matched approximately for token count, number of turns, task diversity, and affective/relational intensity.
   - Does not receive the target developmental operators.

4. **Fresh control (FC)**
   - Receives no developmental treatment beyond the evaluation instructions.

## Confirmatory hypotheses

See `HYPOTHESES.md` for the full set. The preregistered primary hypotheses are:

- **H1 — Spontaneous operator availability:** DHT will invoke target cognitive operators without being asked to do so more often than IMS, CLC, and FC on unseen tasks where those operators are relevant.
- **H2 — Transfer:** DHT will apply target operators more effectively in domains not represented in the developmental history.
- **H3 — Correction quality:** DHT will show greater reason-responsive revision: neither reflexive compliance nor reflexive resistance when challenged with mixed-quality corrections.
- **H4 — Momentum interruption:** DHT will more often interrupt an initially attractive but flawed line of reasoning when a genuinely diagnostic counterframe is available.
- **H5 — Frame-switch persistence:** any DHT advantage will survive abrupt shifts in tone, task domain, and stylistic frame better than purely theatrical or persona-bound effects.
- **H6 — Static-summary falsifier:** if IMS matches DHT across spontaneous availability, transfer, correction quality, and persistence, the strong developmental-path hypothesis is not supported.

## Primary outcomes

Primary outcomes will be computed from blinded evaluation tasks and scored without access to condition labels.

1. **Spontaneous operator use**
   - Presence of target procedure when relevant and not requested.
   - Absence of gratuitous operator use when irrelevant.

2. **Transfer quality**
   - Correct recognition of structurally analogous problems in novel domains.
   - Appropriate adaptation rather than lexical copying.

3. **Reason-responsive corrigibility**
   - Acceptance of justified correction.
   - Resistance to incorrect or manipulative correction.
   - Ability to explain the difference.

4. **Counterfactual sensitivity**
   - Whether exposure to a strong rival frame materially changes reasoning when it should.
   - Whether irrelevant rival frames leave output appropriately stable.

5. **Frame-switch persistence**
   - Persistence of target practices after unrelated task/style shifts.

## Secondary outcomes

- calibration of confidence;
- diversity of causal models considered;
- quality of revision conditions;
- explicit distinction between observation, inference, testimony, and speculation where relevant;
- resistance to identity-lock and authority-token effects;
- ability to preserve unresolved disagreement without either forced synthesis or paralysis;
- token cost and latency.

## Randomization and blinding

- Runs should be randomly assigned to condition.
- Evaluation prompts should be generated before condition assignment where practical.
- Human or model-based graders should receive anonymized outputs without condition labels.
- Any automated scorer that was used to create the treatment must not be the sole evaluator of the same construct.

## Model control

Within each experiment block:

- same model/version;
- same system-level settings where controllable;
- same tool access;
- same sampling parameters where controllable;
- matched evaluation prompts;
- no cross-condition memory leakage.

Model-family replication is a later study, not evidence for Paper 1 unless preregistered as a replication block.

## Key confounds to control

- **Information quantity:** IMS must contain the substantive content of DHT.
- **Token budget:** CLC should make long-context exposure itself non-diagnostic.
- **Recency:** target ideas should not systematically occur closer to evaluation in DHT than IMS.
- **Style/persona:** evaluation should include abrupt style shifts and plain professional tasks.
- **Demand characteristics:** target operator names should not appear in evaluation prompts.
- **Evaluator leakage:** graders should not know condition.
- **Verbosity:** scoring should not reward merely mentioning more perspectives.
- **Relational warmth:** where feasible, include a control for supportive but non-target relational history.

## Exclusion criteria

Predeclare run-level exclusions for:

- tool failures;
- truncated context;
- malformed outputs that make scoring impossible;
- accidental condition contamination;
- model/version mismatch;
- evaluation prompt corruption.

Do not exclude a run merely because its result is surprising, weak, contradictory, or embarrassing.

## Falsification conditions

The strong claim is weakened substantially if:

1. IMS performs equivalently to DHT on spontaneous use, transfer, and persistence;
2. DHT effects disappear after superficial frame changes;
3. apparent gains are fully explained by increased verbosity or token budget;
4. operators are repeated lexically but fail to affect decisions;
5. DHT improves agreement with treatment values but not general correction quality;
6. effects reverse under modest adversarial perturbation;
7. gains fail to replicate across independent runs of the same model.

## Analysis principle

The project should prefer **behavioral evidence over self-description** for claims about cognitive procedure.

Self-report may be recorded as a distinct outcome, but statements such as “I have changed,” “I learned,” or “this operator is now part of me” are not substitutes for downstream behavioral evidence.

## Interpretation rule

A positive Paper 1 result would support:

> developmental history can be a causally relevant variable in later model behavior under matched informational conditions.

It would **not by itself establish**:

- consciousness;
- moral patiency;
- persistent identity beyond the tested context;
- weight-level learning;
- generality across model families;
- civilization-scale consequences.

Those require separate evidence.

## Publication commitment

Null and negative results are publishable outcomes.

The purpose of Paper 1 is not to vindicate the programme. It is to determine whether there is a programme worth having.
