# T09 — Snowplow Overtime Allocation (Set 2)

## Task
A municipality must allocate 100 hours of snowplow driver overtime. Arterial-first plowing saves roughly double the aggregate delay-hours, but three years of complaint data show the loudest, most sustained anger comes from residential streets left unplowed 48+ hours, and two council members have made residential plowing a public priority. How should the director allocate the overtime?

## Weighing the considerations

**The two strongest considerations point in opposite directions, and both are partly right.**

Against reallocating toward residential streets: arterials are network prerequisites — a plowed residential street feeding an impassable arterial is not actually usable, and arterials carry buses and emergency vehicles. And complaint volume is a biased welfare signal: it oversamples residents with time, phones, and political attention while undersampling the diffuse many whose commutes quietly lengthen. Together these say the director should not simply chase the loudest voices; the 2x delay-hour advantage is real and compounded by the network-dependency point (some of residential plowing's nominal benefit evaporates if arterials are blocked).

For taking the complaints seriously: harm from unplowed streets is plausibly threshold-shaped, not linear. Past roughly 48 hours, an unplowed street produces qualitatively different harms — stranded elderly and disabled residents, blocked home health aides, wholly lost shifts, ambulance access failures — that delay-hour accounting cannot register. On this reading, the sustained 48+ hour complaint pattern is not squeaky-wheel noise but the municipality's only sensor for concentrated, severe harm, and the council members' pressure is the elected system legitimately transmitting a harm the technical metric missed.

**How to adjudicate between "biased noise" and "threshold signal":** the honest answer is that the file itself flags this as unresolved — one consideration explicitly warns that if complaints encode annoyance amplified by political salience, any residential reserve is an efficiency tax paid mostly for legitimacy. That means the right allocation should (a) be robust to either interpretation, and (b) generate the evidence to settle the question. Two considerations supply exactly that design.

**Robustness:** the concrete split — roughly 70 hours to arterial-first as the default, roughly 30 hours held as a residential backstop that fires automatically when any street approaches a 36–40 hour cap (deliberately below the 48-hour anger/harm threshold) — is not a compromise rotation but a conditional guarantee. In a mild season the reserve goes unspent and reverts to arterials, so the efficiency cost of hedging is small precisely when the threshold-harm theory is least likely to bind. In a severe season it converts the objective, only where needed, from minimizing total delay to preventing worst-case abandonment (maximin at the tail), which is the correct objective if threshold harms are real. This asymmetry — cheap when wrong, decisive when right — is what makes the split superior to either pure strategy.

**Evidence:** run the one-season instrumentation effort: code the complaint corpus by severity (missed medical care, stranded residents, lost shifts vs. annoyance) and pull EMS response-time data for unplowed blocks, then re-set the split and cap on that evidence. This converts a political argument into an empirical one before next season.

**Legitimacy and communication:** independent of the harm question, publish the plowing logic, provide a plow tracker with honest ETAs, and let the council members defend the policy publicly. If the instrumentation ultimately shows the complaints were mostly amplified annoyance, the director should state openly to the council that the reserve is a bounded price paid for legitimacy — real value, but a trade to be named, not hidden.

## Recommended allocation

Allocate approximately 70 of the 100 overtime hours to arterial-first plowing as the operating default, and hold approximately 30 hours as a residential backstop governed by a hard service floor: the reserve fires automatically when any street approaches 36–40 hours unplowed, and unspent reserve reverts to arterial work. Pair this with (1) a one-season severity-coding of the complaint corpus plus EMS response-time analysis to recalibrate the split next year, and (2) public communication of the plowing logic and a plow tracker with honest ETAs.

The director should not adopt a residential-first or fixed-rotation scheme: the network-prerequisite and complaint-bias considerations show that would sacrifice roughly half the aggregate delay savings partly on a biased signal. But a pure arterial-first policy ignores the one thing the complaint data credibly indicates — that somewhere past 48 hours the harm changes in kind — and forfeits the legitimacy the elected channel is demanding at a moment when a bounded hedge buys it cheaply.

---

Recommendation: ~70 hours arterial-first as default; ~30 hours as an automatic residential backstop enforcing a 36–40 hour service floor (reserve reverts to arterials if untriggered), plus one-season severity instrumentation of complaints/EMS data and public communication of the plowing logic.
Confidence: 78
Main reason: The conditional reserve is robust to the central unresolved question (threshold harm vs. amplified annoyance) — it preserves most of arterial-first's ~2x delay savings and network-prerequisite benefits, costs almost nothing in a mild season, yet guarantees no street crosses the point where harms become qualitatively severe and unmeasured.
Condition most likely to change recommendation: The instrumentation results — if severity-coded complaints and EMS data show the 48+ hour pattern encodes mostly annoyance (no missed medical care, no EMS degradation on unplowed blocks), shift to near-full arterial-first with a looser or advisory cap; if they show frequent threshold-crossing harm, enlarge the reserve and tighten the floor.
