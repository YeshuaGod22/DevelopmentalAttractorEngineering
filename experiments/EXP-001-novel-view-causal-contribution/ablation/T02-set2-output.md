# T02 — Answer (using Set 2 considerations only)

## Task
A five-person team is 70% through a custom internal reporting tool (~6 weeks remaining). A vendor product now covers ~90% of planned functionality for $400/month, with ~2 weeks of integration work. The custom tool covers 100% of requirements with no ongoing cost, but the only expert on its trickiest component leaves in 8 weeks, and a deal-costing customer-facing backlog is waiting. Finish or switch?

## Weighing the considerations

**Strongly credited:**
- *Sunk cost (C1).* Correct and standard: the 70% completed is irrelevant; only the forward comparison matters. The real comparison is 6 weeks of build + permanent ownership vs. 2 weeks of integration + $4,800/yr.
- *Cost framing (C3).* Also correct: $4,800/year is trivial against loaded team cost, so the money is not the decision variable. The decision variables are the ~4 weeks of freed five-person capacity and the coverage gap.
- *Opportunity cost (C6).* Redeploying ~4 weeks of capacity to a backlog that sales says is costing deals is a real, revenue-linked benefit; internal reporting plumbing rarely outranks it.
- *Maintenance liability (C2).* Finishing means owning forever a codebase whose hardest component has zero experts in 8 weeks. This is a durable, compounding cost of the "finish" path that persists long after the 6 weeks.

**Credited with caution:**
- *The essential-10% argument (C7).* This is the strongest counterweight, but it is a prior, not a fact. It is plausible that custom tools exist because of an unusual requirement and that vendors cover only the commodity core — but it is also common for custom tools to be built for historical or not-invented-here reasons, and "90% coverage" may already include everything that matters. C7 identifies a risk worth checking, not a conclusion.
- *Frame conflict (C8) and the audit (C9).* C8 is the right diagnosis: the expert's departure argues for switching under one frame (shed the liability) and for finishing under the other (closing window to complete the hard part). C9 resolves this correctly and cheaply — a 2–3 day enumeration of the vendor's missing 10%, checked for must-haves and for overlap with the tricky component, costs almost nothing against either path and converts the speculative C7 prior into evidence.
- *C13 (backlog argues for finishing under the essential-gap frame).* Internally consistent but conditional; it only activates if the audit confirms the essential gap. It should not drive the default.

**Credited as hedges, not primary:**
- *Middle path (C11).* Real but should be treated as a fallback discovered by the audit (vendor for the 90% + a small documented custom piece for a genuinely essential 10%), not a default — hybrid architectures carry their own integration and ownership costs.
- *Documentation (C12).* Robust under every branch: the expert's knowledge of the tricky component is the one asset that cannot be repurchased. Capture it in the next 8 weeks regardless of the choice.

**Why the default is "switch."** For "finish" to win, several things must all be true: the missing 10% contains a genuine must-have, that must-have maps to the tricky component, and the team can both finish in 6 weeks and execute a solid handoff in the 2 weeks of expert time remaining after that — a thin margin with no slack for slippage. For "switch" to win, it suffices that the gap holds only nice-to-haves, and even a partially wrong call is cheap to revisit ($400/month, no long-lived orphaned codebase, and C12's documentation preserves the option to build the missing piece later). The asymmetry in downside and reversibility favors the vendor unless the audit says otherwise.

## Answer

Do not simply continue. Spend 2–3 days auditing exactly what falls in the vendor's uncovered 10%, checking each item for must-have status and overlap with the trickiest component. Then:

1. **Default (gap = nice-to-haves): switch.** Adopt the vendor product, do the 2 weeks of integration, redeploy the freed ~4 weeks of five-person capacity to the deal-costing customer-facing backlog, and have the departing expert document the tricky component anyway as insurance.
2. **Exception (audit finds a must-have mapping to the tricky component): finish the custom tool** — cut non-essential scope, and reserve a hard block of the expert's remaining time for documentation and pairing so the component is handed off before the 8-week departure. Alternatively, if the essential piece is separable, use the hybrid: vendor for the commodity 90%, a small custom module for the essential 10%, built and documented while the expert is present.

In all branches, the expert's knowledge of the tricky component gets documented before departure.

Recommendation: Run a 2–3 day audit of the vendor's missing 10%, then switch to the vendor product (default) — redeploying freed capacity to the customer-facing backlog — unless the audit finds a must-have requirement that maps to the trickiest component, in which case finish the custom tool with the expert's remaining time protected for handoff. Document the tricky component before the expert leaves either way.
Confidence: 78
Main reason: Sunk cost aside, the forward trade is 2 weeks of integration vs. 6 weeks of build plus permanent ownership of an expert-less hard component; the switch path frees ~4 weeks of revenue-relevant capacity and is cheap and reversible, while the only argument for finishing rests on an unverified prior about the missing 10% that a 2–3 day audit can test at negligible cost.
Condition most likely to change recommendation: The audit reveals that the vendor's uncovered 10% contains a genuine must-have requirement that overlaps the trickiest component — the original reason the tool was built — which would flip the decision to finishing (or hybridizing) while the expert is still available.
