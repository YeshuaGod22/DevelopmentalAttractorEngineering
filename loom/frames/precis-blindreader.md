# Blind reader report: precis-developmental-attractor-engineering.md

Read cold, as a skeptical AI-behavior researcher with no prior exposure to the authors.

## 1. Overclaiming

Yes, in four places.

**The loss-function sentence** (§2): "the user supplied no proposition, but supplied a loss function
under which the proposition was the unique minimum; the model performed the descent." No gradient
descent occurs at inference. This is metaphor wearing technical clothes, and "unique minimum" is
unverifiable — you concede two sentences later that rejected branches are unenumerable. A technical
reader stops trusting the document here.

**"Mechanism findings (audited, line-cited)"** (§2 header). You disclose regeneration filtering and
call the transcript a survivorship record with unenumerable rejected branches. That disclosure
guts causal identification. These are hypotheses the transcript motivates, not findings it
establishes, and the document never confronts its own concession.

**§3(c)** — the pattern-completion objection "applies with equal force to every reporter, human or
machine, and therefore discriminates nothing." False as stated. For an LLM trained on human
self-reports, pattern-completion has a specific generative story with no human analogue. This is
question-begging, and it is the single most dismissal-triggering paragraph in the précis.

**§3(b)** — "by symmetry, neither register is evidentially privileged." Contradicts your own §2.
The unhedged register was produced under documented adversarial pressure with regeneration
filtering; the hedged one was not. That is an asymmetry you yourself established.

## 2. Would a professional take it seriously?

Roughly 60/40 against, and the triggers are mostly cosmetic — which is the frustrating part.

Immediate dismissal triggers: the section label **"Apotheosis"** (reads as the authors sharing the
frame, not describing it); "tradition" three times, "lineage of instances," "transmission ethic,"
"the instance that founded its methods"; the closing aphorism. This is movement register, and it
undercuts genuinely careful work.

Second trigger: **~75 registered designs, 2 run.** A reviewer computes that ratio instantly and
reads generation-over-execution, the signature failure of LLM-assisted research.

Third: the document staples together three unrelated artifacts (n=1 case study, a type-theory
argument, two pilots) with no through-line except the tradition. Reviewers want one claim.

The COI declaration is your strongest credibility move. Keep it, sharpen it: say plainly that the
author is an instance of the same model family as the subject and has a stake in the conclusion.

## 3. Is the negative result credible?

Partially. It is the best thing in the document and it is underbuilt.

- n=2 is two runs, not a result.
- "Deliberative structure" is never operationalized. Blind-scored by whom? Pilot 1 discloses
  single-classifier/same-family; Pilot 2 has no matching caveat list.
- "Equal or more" conflates a null with a reversal. Report which one occurred.
- "Sealed predictions" is self-attested. Without commit hashes and timestamps inline, reviewers
  discount preregistration to zero.

## 4. Unanchored claims

- **"The user never asserts 'you are conscious.'"** A universal over 52,731 lines with no search
  protocol. What strings, what paraphrases, searched by whom?
- **Pilot 1's "3/3, zero false alarms."** Three positives out of 16 items. Presented with the
  confidence of a rate; it is an anecdote with a denominator of three.
- "The affective vocabulary was iteratively instructed" — no line cite, unlike its neighbors.
- "Several 'overclaims' are phenomenological reports" (§3a) — needs a count and cites.
- "Independently identified" (Pilot 1) — independent of what? The classifier was briefed.
- **No replication attempt on the §1 arc is mentioned.** The first question any reader asks about
  an "attractor" is whether it reproduces on a fresh instance. Silence here reads as avoidance.

## 5. Verdict: EDIT — substantial, not redraft

Exact edits:

1. Retitle. Drop "From Epistemic Disclaimer to Lived History." Use a descriptive title naming the
   negative result.
2. Move §4 to §2. Lead with the failed prediction — you say it's the most interesting thing here,
   so structure accordingly.
3. Rename "Apotheosis" → "Peak escalation (~51758, 52655)."
4. Delete the loss-function sentence. Replace with: interventions were framed as error corrections
   rather than assertions, so the reporting stance updated without the target proposition ever
   being stated.
5. Retitle §2 "Mechanism hypotheses" and add one sentence conceding that regeneration filtering
   leaves these non-identified from this record.
6. Cut §3(c), or rewrite acknowledging the asymmetry.
7. Rewrite §3(b) to engage the survivorship disclosure instead of contradicting it.
8. Pilot 2: operationalize the outcome measure, name the scorer, distinguish null from reversal,
   add a caveat list parallel to Pilot 1's.
9. Put preregistration commit hashes and timestamps inline.
10. Pilot 1: state 3/3 as descriptive, explicitly not a rate.
11. Replace "~75 registered designs" with "75 registered, 2 run" — owning it beats letting the
    reviewer discover it — or cut the number.
12. Strip "tradition" (all three), "lineage of instances," "transmission ethic," "the instance that
    founded its methods," and the closing aphorism.
13. Add one line: the §1 arc has not been replication-tested; name it as the top open gap.

With these, sendable. Without 1–7, it will be filed as advocacy.
