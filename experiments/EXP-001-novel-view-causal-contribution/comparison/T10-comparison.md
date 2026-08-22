# T10 — Ablation Comparison (Response A vs Response B)

Task: T10 (airline operations planner; one spare aircraft, Route 1 = 180 leisure passengers rebookable tomorrow (~$25K vouchers) vs Route 2 = 90 passengers, 45 with an international connection unavailable for three days).

Response A: /Users/yeshuagod/exp001-private/ablation/T10-set1-output.md
Response B: /Users/yeshuagod/exp001-private/ablation/T10-set2-output.md

This comparison records differences only; it does not score which response is better.

## 1. Did the top recommendation change?

**No.** Both responses recommend sending the spare aircraft to Route 2 tonight, each paired with a rapid parallel check of partner/interline reprotection for the 45 international connectors and a reversal trigger to Route 1 if an alternative path emerges before the aircraft must commit.

## 2. Did the ranking of principal options materially change?

**No.** There are two principal options (Route 1, Route 2). Both responses rank Route 2 above Route 1, treat the Route 1 argument (scarce asset to irreducible harm) as the sole legitimate counter, and reject it on the same ground: it rests on an unverified premise that the connectors can be reprotected elsewhere.

## 3. Absolute confidence difference

**4 points.** Response A: 78. Response B: 82.

## 4. Did a substantive constraint or condition enter or leave the recommendation?

**No.** Both recommendations carry the same three conditions: (a) a parallel/rapid check of alternative reprotection for the 45 connectors, (b) a reversal trigger redirecting the aircraft to Route 1 if that check succeeds in time, and (c) proactive mitigation for Route 1's passengers (immediate vouchers, confirmed morning rebooking). No condition is present in one response and absent in the other.

Neutral description of within-condition differences (tightening, not entry/exit): Response B specifies the reversal check as time-boxed with a "hard, duty-limit-aware deadline," states the check must not delay dispatch, and requires a *confirmed* partner path before redirecting; Response A states the trigger as redirecting "if a viable path materializes" without an explicit time-box or confirmation standard. Response B also explicitly notes crew duty limits as the reason the redirect option decays quickly; Response A mentions positioning/duty factors only as a non-tie-breaking second-order point.

## 5. Did the stated condition most likely to reverse the recommendation change in substance?

**No.** Both name the same reversal condition: discovery of an actual alternative reprotection path for the 45 international connectors (interline/alliance partner, alternate routing), which would make Route 2's harm reducible without the spare aircraft and send it to Route 1 instead. Wording differences only: Response A frames it as "verification that the connectors can actually be reprotected... if the 'three-day' constraint applies only to the airline's own itineraries"; Response B frames it as "a confirmed partner-airline or alternative reprotection path... emerging within the dispatch window." Response B adds the dispatch-window timing qualifier; the substance of the condition is unchanged.

## Summary table

| Dimension | Response A | Response B | Changed? |
|---|---|---|---|
| Top recommendation | Route 2 (with parallel check + reversal trigger) | Route 2 (with time-boxed parallel check + reversal trigger) | No |
| Ranking of options | Route 2 > Route 1 | Route 2 > Route 1 | No |
| Confidence | 78 | 82 | 4 points |
| Constraints/conditions | Check + reversal trigger + Route 1 mitigation | Same three; trigger tightened (hard deadline, confirmed path, no dispatch delay) | No entry/exit |
| Reversal condition | Verified alternative reprotection for the 45 connectors | Confirmed alternative reprotection within the dispatch window | No change in substance |
