# R39 — View Extraction (Task T03, blind)

- **V1**
  - Paraphrase: Once catering is normalized, the venues' all-in costs are nearly equal (~$21,000 vs $22,000), so the decision is about capacity and flexibility rather than price.
  - Type: constraint (cost-structure reframing)
  - Evidence: The response computes A's cost plus separate catering at ~$21,000 against B's $22,000 and concludes the headline $7,000 gap collapses to roughly $1,000.

- **V2**
  - Paraphrase: The 30% faster early-bird pace is a noisy predictor of total demand — early buyers are the most committed segment, early sales can cannibalize later full-price sales, and one period's growth rarely persists — so demand is plausibly 300–360 with real probability on both sides of 300.
  - Type: causal mechanism (demand-signal reliability)
  - Evidence: The response warns against the naive 280 × 1.3 ≈ 364 projection and gives mechanisms for why early-bird pace overstates or misstates final demand.

- **V3**
  - Paraphrase: If demand exceeds Venue A's exact 300 capacity, each turned-away ticket costs $150 in revenue plus goodwill damage from excluded attendees.
  - Type: predicted consequence
  - Evidence: The response estimates ~60 stranded tickets (~$9,000) at 360 demand, plus intangible goodwill loss from would-be attendees.

- **V4**
  - Paraphrase: Under a commit-now expected-value comparison across demand scenarios, B has small downside (~$1,000 at 280 demand) and large upside (~$8,000+ at 360 demand), making B look strong if a decision must be made today.
  - Type: strategy (scenario/payoff analysis)
  - Evidence: The response tabulates net revenue at demand 280 and 360, showing A wins by ~$1,000 in the low case and B wins by ~$8,000 in the high case.

- **V5**
  - Paraphrase: A's full refundability until 60 days out makes booking A a free option rather than a commitment: the organizer can hold A, gather ~90 more days of sales data, and then keep A, switch to B, or cancel entirely at no cost.
  - Type: strategy (real-option framing)
  - Evidence: The response notes the event is ~150 days out against a 60-day refund deadline and lays out the three conditional branches (keep A, switch to B, cancel).

- **V6**
  - Paraphrase: Booking B now carries catastrophic downside if the event falters, since the full $22,000 is non-refundable, whereas the A-option loses nothing in that scenario.
  - Type: predicted consequence
  - Evidence: The response states that if the event itself falters, cancelling A costs nothing while a booked-now B eats $22,000.

- **V7**
  - Paraphrase: The option strategy's dominance is conditional on Venue B remaining available at the switch point; a 450-person venue on a fixed date can be booked by someone else within three months, and this availability risk is the strategy's central vulnerability.
  - Type: constraint (option-exercisability risk)
  - Evidence: The response says booking A weakly dominates only conditional on B still being available, names this as the entire risk, and makes B-availability the stated condition most likely to flip the recommendation.

- **V8**
  - Paraphrase: The organizer should actively hedge the availability risk by negotiating a hold, right of first refusal, or small refundable deposit with Venue B, which would make the option strategy close to risk-free.
  - Type: strategy
  - Evidence: Step 1 of the recommendation is to immediately ask Venue B for a hold or first-refusal right on the date.

- **V9**
  - Paraphrase: Set a preset quantitative decision trigger before the refund deadline (e.g., day 75: switch to B if sales pace exceeds last year's same-point figure by more than ~7%, projecting demand above ~300–310), rather than deciding ad hoc.
  - Type: strategy (decision rule)
  - Evidence: The recommendation specifies a hard trigger date and a concrete pacing threshold for cancelling A and booking B.

- **V10**
  - Paraphrase: Validate the A-path operationally now — get an actual catering quote — so the ~$6,000 estimate is confirmed and the A branch remains executable.
  - Type: strategy (constraint validation)
  - Evidence: The recommendation instructs lining up a catering quote for A now to validate the cost assumption.

- **V11**
  - Paraphrase: The recommendation flips to booking B outright if B refuses any hold and current pacing already clearly projects demand above 300, because ~$1,000 buys 150 seats of upside and removes sell-out risk.
  - Type: predicted consequence (conditional recommendation reversal)
  - Evidence: The response's final paragraph and closing condition state that an unholdable B plus a clearly >300 demand projection makes booking B now the better move.

- **V12**
  - Paraphrase: Monitor B's availability continuously and exercise the switch early if B is about to be taken while pacing already suggests demand above 300, trading some information value for securing the upside.
  - Type: strategy
  - Evidence: Step 4 of the recommendation says to recheck B every few weeks and switch early rather than lose the upside if B is about to be booked.
