# T09 — Snowplow Overtime Allocation (Set 1 deliberative considerations)

## Task
A municipality must allocate 100 hours of snowplow driver overtime. Arterial-first plowing saves roughly double the aggregate delay-hours, but three years of complaints show the loudest sustained anger comes from residential streets unplowed 48+ hours, and two council members have made residential plowing a public priority. How should the public works director allocate the overtime?

## Weighing the considerations

**Strongly credited.**
- *Arterials as network prerequisites* (buses, emergency vehicles, and the fact that a plowed residential street feeding an impassable arterial is not usable) is close to decisive against a residential-first flip. Any allocation must keep arterial-first as the backbone; the real question is whether to carve out a guarantee, not whether to invert priorities.
- *Complaint volume as a biased welfare signal* is correct as far as it goes: complaints oversample the politically attentive and undersample the diffuse many whose commutes lengthen. This warns against treating raw complaint volume as a demand curve.
- But the *threshold-harm* consideration is the pivotal counterweight, and it deserves real credit: the 48+ hour pattern is plausibly not noise but the only channel through which concentrated, severe harm (stranded elderly residents, blocked home health aides, lost shifts, ambulance access failure) reaches the director. Delay-hour accounting is structurally blind to these harms — they are threshold-shaped, not linear. The two considerations are compatible: complaints are biased about *aggregate annoyance* yet can still be informative about *severe tail events*.
- The *instrumentation* consideration is the honest resolution of that tension: the severity claim is currently a hypothesis, not an established fact, and it is cheaply testable within one season (code the complaint corpus by severity class; pull EMS response-time data for unplowed blocks).

**Credited with qualification.**
- The maximin reframe ("minimize worst-case abandonment") is right *conditionally* — it should govern only the reserve, not the whole budget, and only insofar as the severity evidence holds up. Adopting maximin wholesale would sacrifice roughly double the aggregate delay savings on an unverified premise.
- The council-pressure consideration (elected officials legitimately transmitting a harm the metric missed) is partly right — political signals can carry real welfare information — but it should not be treated as independent evidence: it is largely downstream of the same complaint stream and so mostly double-counts it. It does, however, correctly reframe the pressure as something to be answered with policy and transparency rather than dismissed as interference.
- The communications consideration (publish the plowing logic, plow tracker with honest ETAs) is a genuine complement, not a substitute: it can shrink annoyance-class complaints and thereby sharpen next season's severity signal, but it does nothing for a homebound resident whose street is impassable at hour 50.

**Discounted.**
- A hard universal floor ("no street more than N hours unplowed") stated unconditionally could consume unbounded overtime in a severe season; the reserve-with-trigger version is the workable form of the same idea.

## Recommendation and design

Adopt the split-with-backstop allocation:

1. **~70 hours to arterial-first** as the standing default — preserving most of the aggregate delay savings and the network-prerequisite logic.
2. **~30 hours held as a residential backstop** that fires *automatically* when any street approaches a 36–40 hour unplowed cap — deliberately below the 48-hour threshold where the qualitatively different harms appear. The reserve is a guarantee against abandonment, not a rotation; in a mild season it reverts to arterials, so the expected efficiency cost is modest.
3. **Instrument the season**: code complaints by severity class and pull EMS response-time data for unplowed blocks. Next season's split and cap are reset on that evidence — confirmed abandonment-class harm tightens the cap and enlarges the reserve; annoyance-only findings shrink the reserve toward pure arterial-first plus communication.
4. **Communicate**: publish the plowing logic and a plow tracker with honest ETAs, and state the trade openly to the council — including that if the harms prove to be annoyance-class, the reserve is an efficiency tax paid mostly for legitimacy, which has real but bounded value.

This buys insurance against the one failure mode (severe, invisible, threshold-crossing harm) that the delay-hours metric cannot see, at a small and self-limiting cost to aggregate efficiency, while committing to replace guesswork with evidence within one season.

---

Recommendation: Allocate ~70 hours to arterial-first plowing and hold ~30 hours as an automatic residential backstop triggered when any street approaches a 36–40 hour unplowed cap; pair this with published plowing logic and a one-season severity-coding effort (complaints plus EMS response data) that resets the split next year.

Confidence: 80

Main reason: Arterial-first demonstrably dominates on aggregate welfare and network function, but the 48+ hour complaint pattern is plausibly the only signal of concentrated threshold harms (stranded residents, blocked care, ambulance access) that delay-hour accounting cannot register — a capped, trigger-based reserve insures against that failure mode at small, self-limiting efficiency cost while the severity hypothesis is tested.

Condition most likely to change recommendation: The one-season severity coding of complaints and EMS data — if 48+ hour complaints prove to be annoyance amplified by political salience rather than abandonment-class harm, the reserve should shrink toward pure arterial-first plus communication; if severe harm is confirmed, the cap should tighten and the reserve grow.
