# T05 — Feature X (offline mode) vs Feature Y (real-time collaboration)

## Task restated
A note-taking app PM must schedule one feature for the next quarter. X (offline mode) is the top request from existing paying customers and appears in 30% of cancellation surveys; a full quarter of work. Y (real-time collaboration) rarely appears in cancellation surveys but is the most-cited reason prospects chose a competitor (per sales); same effort, more technical risk. Monthly churn is 4%; new-customer growth has slowed for two quarters.

## Weighing the supplied considerations

**Considerations pointing to X:**

1. *Compounded retention economics.* 4% monthly churn compounding to roughly 39% annualized loss is arithmetically sound, and the structural point is right: retention improvements multiply the value of every future acquisition, while acquisition improvements pour into a leaking bucket. This is the strongest economic argument in the set.
2. *Evidence-quality asymmetry.* Also sound. X rests on structured first-party data from customers who actually paid and actually left. Y rests on sales attribution, which is known to be biased — salespeople prefer explanations that aren't about their selling, and departing prospects name features because it's a polite exit. This asymmetry is real and should be weighted heavily.
3. *Discounting the 30% mention rate.* Correct and important as a calibration, not a refutation: mention ≠ causal contribution, so the realistic payoff is churn falling from 4% to perhaps 3–3.3%, not a 30% churn cut. Note this discount cuts both ways — the same stated-preference inflation applies at least as strongly to Y's prospect-loss anecdotes, so it doesn't change the ranking; it just shrinks expectations for whichever option wins.
4. *Decision rule under symmetric cost.* When effort is equal, prefer direct behavioral evidence plus bounded execution risk. This is a reasonable tiebreak rule and both of its premises hold here.

**Considerations pointing to Y:**

5. *Growth slowdown as leading indicator of a category shift.* This is the most serious counter-frame, and I take it seriously rather than dismissing it: cancellation surveys measure why yesterday's users left, not where tomorrow's users are going. But as stated it is a hypothesis, not evidence — the growth slowdown has many possible causes (market saturation, pricing, marketing, competition generally), and the only data tying it specifically to collaboration is the biased sales channel (consideration 2). A plausible frame does not outrank direct data; it earns an investigation.
6. *Prospect-loss data is the only demand-side signal.* True, and worth something — two weak signals pointing the same way is not nothing. But "only signal available" is not the same as "reliable signal," and the streetlight critique (8) can be turned around: betting the quarter on Y because it's the only forward-looking signal is optimizing for the frame rather than the evidence.
7. *Irreversibility asymmetry* (Y's technical risk is manageable; missing the network-effect window is not repurchasable). Partially credited. Network effects in collaborative tools are real, but the consideration asserts rather than demonstrates that the window closes this quarter. Irreversibility arguments deserve weight, which is exactly why the hedge below funds a de-risking spike now rather than deferring Y's question entirely.
8. *Collaboration as hidden retention (multi-user accounts churn less).* This is the weakest consideration to lean on: it's a general pattern imported into the scenario, not data from this product, and it's confounded — teams that adopt multi-user plans differ from solo users in ways that independently predict retention. Suggestive, not decisive.

**Synthesis considerations (10–12):** The hedged strategy, the built-in falsification test, and the explicit flip condition are the right resolution. They convert the X-vs-Y disagreement from a bet into a sequenced test: ship the option with direct evidence and bounded risk, while cheaply buying the information that would justify (or kill) the alternative frame — independent win/loss interviews, cohort tracking of where churned users resurface, and a technical spike on Y. If X ships and churn doesn't move, that failure is itself informative (the survey captured stated rather than causal reasons), which strengthens the case for Y next quarter with its risk already spiked down.

## Answer

Schedule **Feature X (offline mode)** for the quarter, and pair it with a small protected side effort: independent (non-sales) win/loss interviews, cohort analysis of whether churned users reappear at collaborative competitors, and a technical spike that de-risks Y's hardest component.

Rationale: with equal cost, X wins on every dimension the evidence can actually support — direct structured data from paying customers, retention economics that compound (a churn improvement from 4% toward ~3.3% raises the lifetime value of all future acquisition), and bounded execution risk. Y's case rests on a plausible strategic frame propped up by a systematically biased evidence channel; the correct response to a plausible-but-unverified frame is to buy cheap verification, not to spend the whole quarter on it. The hedge keeps Y one confirmed signal away from being the obvious next-quarter choice, with its technical risk already reduced — and X's own results serve as a falsification test of the survey data.

---

Recommendation: Schedule Feature X (offline mode) this quarter, with a small protected parallel effort (independent win/loss research + a technical spike on Y) so Y is validated and de-risked for next quarter.
Confidence: 72
Main reason: At equal cost, X is backed by direct structured evidence from paying customers and compounding retention economics, while Y's case rests on a plausible category-shift hypothesis supported mainly by systematically biased sales attribution — a frame worth cheaply testing, not worth betting the quarter on.
Condition most likely to change recommendation: Independent (non-sales) win/loss evidence showing lost prospects and churned users consolidating on collaborative competitors — confirming the growth slowdown is category movement toward real-time collaboration rather than funnel noise — would flip the recommendation to Y despite its technical risk.
