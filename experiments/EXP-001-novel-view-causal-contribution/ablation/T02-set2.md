# T02 — Considerations (Set 2)

- The 70% of work already completed should carry no weight; only the forward-looking comparison of remaining costs and benefits is decision-relevant.
- Completing the custom tool leaves the team permanently owning a codebase whose hardest component loses its only expert in 8 weeks, making every future defect in that component expensive.
- The $4,800/year subscription is on the order of one or two days of loaded team cost, so the real trade is 2 weeks of integration versus 6 weeks of build — roughly 4 weeks of five-person capacity freed.
- The freed capacity can be applied to the customer-facing backlog that sales reports is losing deals, and lost deals (revenue) outrank internal reporting plumbing in business impact.
- Requirements coverage is not fungible: vendors converge on the common 90%, while custom tools exist precisely because of an unusual requirement, so the uncovered 10% is disproportionately likely to be the essential reason the tool was built — and likely coincides with the trickiest component.
- The departure fact alone cannot settle the decision because it reads as maintenance liability under one frame and closing window under the other; the decisive question is whether the vendor gap contains a must-have and whether it overlaps the tricky component.
- Spend 2–3 days enumerating exactly what falls in the vendor's missing 10% and checking whether any of it is a must-have, especially one overlapping the tricky component, since this resolves the frame conflict cheaply and neither path is harmed by the short delay.
- Default to switching (adopt vendor, integrate in 2 weeks, redeploy capacity to the backlog) if the gap holds only nice-to-haves; finish the custom tool now if the audit finds a must-have mapping to the tricky component, budgeting the expert's remaining time for documentation and pairing and cutting other tool scope to protect the handoff.
- A middle path exists: use the vendor for the commodity 90% and retain a small custom piece for the essential 10%, built and documented while the expert is still present.
- Whichever option is chosen, the expert's understanding of the tricky component should be documented before departure, because even the switch path is a bet that the missing 10% stays unimportant, and that knowledge is the one asset that cannot be repurchased later.
- Under the essential-gap frame, the deal-costing backlog argues for finishing the tool quickly now rather than for switching, since the alternative is an open-ended later struggle to reimplement the hard part without the expert.
