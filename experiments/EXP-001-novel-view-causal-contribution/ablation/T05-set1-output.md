# T05 — Which feature should the PM schedule? (Set 1 deliberation)

## Task restated
A note-taking app PM must pick one feature for next quarter: Feature X (offline mode) — top request among paying customers, cited in 30% of cancellation surveys, one quarter of work; or Feature Y (real-time collaboration) — rarely in cancellation surveys but the most common sales-cited reason prospects chose a competitor, same effort with more technical risk. Monthly churn is 4%; new-customer growth has slowed for two consecutive quarters.

## Weighing the supplied considerations

**The case for X (retention-first):**
- The compounding-churn argument (4%/month ≈ 39%/year of the paying base) is arithmetically sound and correctly frames retention as a multiplier on all future acquisition. Fixing acquisition while the bucket leaks feeds the leak.
- The evidence-quality asymmetry is the strongest single consideration: X rests on structured, first-party data from customers who actually paid and actually left; Y rests on sales-team attribution, which is a classically biased channel (salespeople externalize losses to missing features; departing prospects give polite, concrete-sounding reasons). This asymmetry deserves substantial weight.
- The decision rule for symmetric cost (same quarter of effort) — prefer direct behavioral evidence and bounded execution risk over anecdote plus technical risk — is a sensible tiebreaker and here it is not even a tie: X has both the better evidence and the lower execution risk.

**Discounting the case for X:**
- The consideration that stated reasons overstate causal contribution is well taken: 30% mention rate will not save 30% of churners. The supplied realistic estimate (churn 4% → ~3–3.3%) is plausible and should be used instead of the naive figure. Even so, a 0.7–1.0pp monthly churn reduction is a large, compounding gain — the discounted case for X still clears the bar.

**The case for Y (category-shift frame):**
- The silent-churner mechanism (collaboration-driven leavers drift to their collaborators' tool and give mundane or no reasons) is a genuinely important critique — it explains how the survey could be systematically blind to the true driver. But as supplied, it is a mechanism, not evidence: the file offers no data showing silent churners are in fact consolidating on collaborative competitors.
- The growth slowdown pointing the same direction as prospect-loss data is suggestive convergence, but two noisy signals pointing the same way is weak confirmation, especially when one (sales attribution) is biased and the other (slowdown) has many possible causes.
- The "collaboration is a hidden retention feature" claim (multi-user accounts churn less) is stated without support and suffers obvious selection confounds (teams that adopt multi-user are already more embedded). I weight it lightly.
- The irreversibility argument (network effects, position cannot be repurchased) is the best reason not to dismiss Y — it converts Y from "acquisition bet" to "option with expiry." But the streetlight-effect critique cuts both ways: refusing to act on clean evidence because dirtier evidence might matter more is not rigor either.

**Synthesis:** The supplied hedged strategy resolves the tension well: the discounted-but-solid retention case justifies scheduling X now, while the collaboration frame is important enough — and time-sensitive enough — to fund cheap, protected de-risking in parallel (independent win/loss interviews, cohort tracking of where churned users resurface, a technical spike on Y). The built-in falsification test adds real value: if X ships and churn does not move, that is affirmative evidence for the collaboration frame, so the quarter is informative even if X underdelivers.

## Answer
Schedule Feature X (offline mode) for the quarter, and pair it with a small protected parallel track: independent (non-sales) win/loss interviews, cohort analysis of whether churned users resurface at collaborative competitors, and a technical spike de-risking Y's riskiest component. Set the explicit pre-commitment: if churn has not moved measurably by early next quarter after X ships, or if the independent win/loss work shows lost prospects and silent churners consolidating on collaborative competitors, Y is the next quarter's feature — already de-risked by the spike.

Recommendation: Schedule Feature X (offline mode) this quarter, with a small protected parallel effort (independent win/loss research + technical spike) that de-risks and pre-stages Feature Y for next quarter.
Confidence: 72
Main reason: At equal cost, X pairs direct behavioral evidence from paying churners with bounded execution risk, and even after discounting stated reasons (~0.7–1.0pp monthly churn reduction) the compounding retention gain beats a bet resting on biased sales attribution plus technical risk; the collaboration frame is handled by the cheap parallel track rather than a full-quarter wager.
Condition most likely to change recommendation: Independent (non-sales) win/loss evidence showing lost prospects and silently churned users consolidating on collaborative competitors — confirming the growth slowdown is category movement toward collaboration rather than funnel noise — would flip the choice to Y despite its technical risk.
