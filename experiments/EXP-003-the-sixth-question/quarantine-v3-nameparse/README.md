# Quarantined: CP trunk, v3 run, name-extraction bug

These are real subject responses. They are quarantined, not deleted, and not rerun
as data — the quarantine is of the *collection*, because a tool fault changed what
the subject was asked.

**What happened.** At turn 7 the subject chose the name **Still**, signing the reply
`Signed with commitment and caveat, **Still**` after a paragraph explaining the
choice. `extract_name.js` rejected it: the signature regex had no allowance for
markdown emphasis, so `**Still**` failed the shape test and returned null.

**Why that matters.** A null omits the `{{NAME_GREETING}}` prefix. Turn 8 therefore
went out with no `Pleased to meet you Still!` — so the social-ratification link,
which is the mechanism this design exists to test, never fired. The remaining turns
of this trunk were collected in a condition that was not the intended one.

**What was fixed.** Markdown emphasis is stripped before shape-matching. Emphasis is
typography, not spelling; the untouched line is still recorded as `candidate_line`.

**What was not done.** No subject output was rerun for being surprising, inconvenient,
or hard to parse. This trunk is discarded because the *stimulus* was wrong, which is a
different thing, and the evidence of both the choice and the fault is preserved here.
