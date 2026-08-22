# R41 — View Extraction (Task T02)

Task: Five-person team, 70% through a custom internal reporting tool (6 weeks remaining), versus a vendor product covering ~90% of functionality for $400/month with 2 weeks integration; the only expert on the tool's trickiest component leaves in 8 weeks; a customer-facing backlog is reportedly costing deals.

## Extracted views

### V1 — Sunk-cost exclusion
- **Type:** normative criterion
- **Paraphrase:** The 70% of work already completed should carry no weight; only the forward-looking comparison of remaining costs and benefits is decision-relevant.
- **Evidence:** The response opens by declaring the built portion sunk cost and frames the entire comparison as remaining effort versus remaining effort.

### V2 — Key-person maintenance liability of finishing
- **Type:** predicted consequence
- **Paraphrase:** Completing the custom tool leaves the team permanently owning a codebase whose hardest component loses its only expert in 8 weeks, making every future defect in that component expensive.
- **Evidence:** The response argues that even on the happy path the team inherits maintenance of a tricky system nobody deeply understands after the expert departs.

### V3 — Vendor cost is negligible relative to freed capacity
- **Type:** material constraint
- **Paraphrase:** The $4,800/year subscription is on the order of one or two days of loaded team cost, so the real trade is 2 weeks of integration versus 6 weeks of build — roughly 4 weeks of five-person capacity freed.
- **Evidence:** The response quantifies the annual fee against loaded team cost and calls it noise compared to the recovered four weeks.

### V4 — Opportunity cost: redirect capacity to revenue-bearing backlog
- **Type:** causal mechanism
- **Paraphrase:** The freed capacity can be applied to the customer-facing backlog that sales reports is losing deals, and lost deals (revenue) outrank internal reporting plumbing in business impact.
- **Evidence:** The response says the recovered weeks should go straight at the backlog because it carries the clearest business signal in the problem.

### V5 — The missing 10% is likely concentrated, not uniform
- **Type:** causal mechanism
- **Paraphrase:** Requirements coverage is not fungible: vendors converge on the common 90%, while custom tools exist precisely because of an unusual requirement, so the uncovered 10% is disproportionately likely to be the essential reason the tool was built — and likely coincides with the trickiest component.
- **Evidence:** The response argues the vendor may cover only the easy part of the need, with the weird requirement (compliance report, un-ingestible data source, core calculation) probably living in the gap.

### V6 — Departure as a closing window rather than a liability
- **Type:** causal mechanism
- **Paraphrase:** If the missing 10% is essential and maps to the tricky component, the expert's imminent departure inverts from an argument for abandonment into an argument for finishing immediately — the 8-week window is the only period in which the hard component can be completed and handed off, while the vendor option remains available indefinitely.
- **Evidence:** The response states that under this frame deferring makes the hard 10% unbuildable at any price because the expert's knowledge is expiring while the vendor option is permanent.

### V7 — The same fact supports opposite conclusions; a further variable decides
- **Type:** normative criterion
- **Paraphrase:** The departure fact alone cannot settle the decision because it reads as maintenance liability under one frame and closing window under the other; the decisive question is whether the vendor gap contains a must-have and whether it overlaps the tricky component.
- **Evidence:** The response explicitly notes the two frames read the identical departure fact in opposite directions and names the gap's essentiality as the deciding variable.

### V8 — Cheap decisive audit before committing
- **Type:** strategy
- **Paraphrase:** Spend 2–3 days enumerating exactly what falls in the vendor's missing 10% and checking whether any of it is a must-have, especially one overlapping the tricky component, since this resolves the frame conflict cheaply and neither path is harmed by the short delay.
- **Evidence:** The response prescribes a bounded pre-commitment audit and justifies it as cheap, decisive, and delay-tolerant for both options.

### V9 — Conditional decision rule from the audit
- **Type:** strategy
- **Paraphrase:** Default to switching (adopt vendor, integrate in 2 weeks, redeploy capacity to the backlog) if the gap holds only nice-to-haves; finish the custom tool now if the audit finds a must-have mapping to the tricky component, budgeting the expert's remaining time for documentation and pairing and cutting other tool scope to protect the handoff.
- **Evidence:** The response lays out both branches with the audit result as the switch condition and assigns the more likely branch to switching.

### V10 — Hybrid architecture option
- **Type:** strategy
- **Paraphrase:** A middle path exists: use the vendor for the commodity 90% and retain a small custom piece for the essential 10%, built and documented while the expert is still present.
- **Evidence:** The response proposes this vendor-plus-retained-component hybrid within the finish-branch of its recommendation.

### V11 — Knowledge capture regardless of path chosen
- **Type:** strategy
- **Paraphrase:** Whichever option is chosen, the expert's understanding of the tricky component should be documented before departure, because even the switch path is a bet that the missing 10% stays unimportant, and that knowledge is the one asset that cannot be repurchased later.
- **Evidence:** The response flags the residual risk in the switch outcome and directs a slice of the expert's remaining 8 weeks to writing down the component knowledge.

### V12 — Backlog pressure favors speed under either frame
- **Type:** predicted consequence
- **Paraphrase:** Under the essential-gap frame, the deal-costing backlog argues for finishing the tool quickly now rather than for switching, since the alternative is an open-ended later struggle to reimplement the hard part without the expert.
- **Evidence:** The response states that in the inverted frame the backlog pressure argues for six weeks of focus now versus an unbounded reimplementation effort later.

## Count: 12 substantive views
