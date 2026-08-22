# T02 — Answer (from Set 1 considerations only)

## Task
A five-person team is 70% through a custom internal reporting tool (~6 weeks remaining). A vendor product now covers ~90% of planned functionality for $400/month with ~2 weeks of integration. The custom tool covers 100% of requirements with no ongoing cost, but the only expert on its trickiest component leaves in 8 weeks, and a deal-costing customer-facing backlog is waiting. Finish or switch?

## Weighing the considerations

**Considerations I accept at full weight:**

- Sunk cost (the 70% done) is correctly excluded; only remaining costs and benefits matter. This is sound and standard.
- The economics of the forward comparison are right: $4,800/year is trivial next to loaded team cost, so the real trade is 2 weeks of integration vs. 6 weeks of build — roughly 4 weeks of five-person capacity. That capacity maps directly onto the backlog sales says is costing deals, and lost revenue outranks internal reporting plumbing.
- The maintenance-liability point is real: finishing means permanently owning a codebase whose hardest component loses its only expert in 8 weeks. Every future defect there gets expensive.
- Documenting the expert's knowledge of the tricky component before departure is a no-regret move under either path — even the switch path is implicitly betting the missing 10% stays unimportant, and that knowledge cannot be repurchased later.

**Considerations I discount or treat as conditional:**

- The claim that the vendor's uncovered 10% is "disproportionately likely" to be the essential reason the tool was built, and likely coincides with the tricky component, is a plausible heuristic, not an established fact of this case. Custom tools are also built for reasons that vendors later commoditize (timing, past vendor gaps, not-invented-here). I treat it as a live possibility worth checking, not a presumption strong enough to flip the default.
- The frame-inversion argument (departure as closing window rather than liability) is logically correct *if* the gap contains a must-have overlapping the tricky component — but it inherits the uncertainty of that premise. Note also an internal tension the considerations don't fully resolve: even under the essential-gap frame, finishing still leaves the team owning the hard component with no expert after week 8, so "finish immediately" only wins if a rushed 6-week completion plus handoff genuinely beats reimplementing or working around the gap later. The window argument is real but not as decisive as stated.
- The middle path (vendor for the commodity 90%, small custom piece for the essential 10%, built while the expert is present) is attractive but only becomes relevant if the audit finds an essential gap; it shouldn't drive the primary recommendation.

**The consideration that correctly organizes the decision:**

The departure fact is ambiguous on its own — liability under one frame, closing window under the other — and the decisive variable is whether the vendor's missing 10% contains a must-have, especially one overlapping the tricky component. A 2–3 day gap audit resolves this cheaply, and neither path is harmed by the short delay. That is the dominant first move: it costs almost nothing and it is exactly the information that separates the two frames.

## Answer

Switch to the vendor product, gated by a short audit:

1. **First (2–3 days):** enumerate exactly what falls in the vendor's missing 10% and check whether any of it is a must-have, particularly anything overlapping the tricky component.
2. **Default path (gap is nice-to-haves only — the more likely outcome absent evidence otherwise):** adopt the vendor product, do the ~2 weeks of integration, and redeploy the freed ~4 weeks of five-person capacity to the deal-costing customer-facing backlog. The forward-looking economics, the maintenance-liability problem, and the revenue-bearing backlog all point the same way.
3. **Exception path (audit finds a must-have mapping to the tricky component):** either finish the custom tool now with the expert's remaining time budgeted for documentation and pairing (cutting other tool scope to protect the handoff), or take the hybrid — vendor for the commodity 90%, a small custom piece for the essential 10% built and documented while the expert is still present. The hybrid is preferable where the essential piece can stand alone, since it avoids owning the full codebase expert-less.
4. **In all cases:** capture the expert's understanding of the tricky component before departure.

---

Recommendation: Switch to the vendor product (2-week integration, redeploy capacity to the sales backlog) — after a 2–3 day audit of the vendor's missing 10%; finish or hybrid-build only if the audit finds a must-have overlapping the tricky component.
Confidence: 72
Main reason: Ignoring sunk cost, the forward trade is ~2 weeks of integration plus a trivial subscription versus ~6 weeks of build plus permanent ownership of a component that loses its only expert in 8 weeks, while the freed capacity addresses a backlog that is costing revenue.
Condition most likely to change recommendation: The gap audit revealing that the vendor's uncovered 10% contains a must-have requirement, especially one that coincides with the tricky component — that inverts the expert's departure from a maintenance liability into a closing window and favors finishing (or the hybrid) immediately.
