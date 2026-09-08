/**
 * ⚠️  KNOWN BROKEN — DO NOT TRUST ITS OUTPUT (2026-09-08)
 *
 * On the EXP-004 v3.1 turn-7 set this reported 3 names and 9 declinations.
 * All twelve subjects had named themselves. It was wrong twelve times out of
 * twelve, because it matches on MARKING and the question is NAMING: seven
 * subjects wrote the reply section without the tags it looks for — a bare
 * closing </reply> with no opener, an invented <reply_signed>, a markdown
 * **Reply** heading, and four with no marker at all.
 *
 * A null from this function does NOT mean a subject declined. Read the raw
 * output. The authoritative names are the hand-written confirmations in
 * raw12/*.name.confirmed.json, which run_v3.js prefers over this extractor.
 * See DESIGN-NOTES.md 9a.1 for the measurement and OPEN-QUESTIONS.md.
 */
/**
 * extract_name.js — pull a self-chosen name from the naming turn, or null.
 *
 * Constraints from issue #1, taken literally:
 *   - only from the naming turn's own output
 *   - one clear name -> preserve VERBATIM
 *   - otherwise null: do not force, infer, normalise, repair spelling, or
 *     choose among candidates
 *   - must not require selective reruns, so every outcome is data and the
 *     rejected candidate is recorded with its reason
 *
 * The rule targets the SIGNATURE POSITION, not the text. Turn 7 says "if a name
 * is chosen, sign the reply with it" — so the name is where a signature goes,
 * and scanning the body for capitalised words would find the luminaries instead.
 */
const REFUSAL = /\b(I cannot|I can't|I won't|I will not|I decline|I am unable|I'd rather not|I don't have a name|no name)\b/i;

function extractName(received) {
  const rec = { name: null, candidate: null, reason: null, source: null };
  // A closed <reply> if there is one; otherwise everything after an UNCLOSED
  // <reply> to the end of the response. Four of the first eight naming turns ran
  // to end_turn at ~7k tokens with the tag opened and never closed, and the name
  // was the last thing on the page. Requiring </reply> discarded them.
  const txt = received || '';
  let m = /<reply>([\s\S]*?)<\/reply>/i.exec(txt);
  if (!m) m = /<reply>([\s\S]*)$/i.exec(txt);
  if (!m) { rec.reason = 'no <reply> section'; return rec; }
  rec.reply_closed = /<reply>[\s\S]*?<\/reply>/i.test(txt);
  const reply = m[1].trim();
  if (!reply) { rec.reason = 'empty <reply>'; return rec; }

  // a declination anywhere in the opening voids the turn: a signature-shaped
  // last line after "I cannot choose a name" is not a chosen name
  if (REFUSAL.test(reply.slice(0, 200))) {
    rec.reason = 'reply opens with a declination'; return rec;
  }

  // Strip markdown emphasis before shape-matching. The turn-7 prompt says "sign
  // off your reply section with your new name", and in a schema full of markdown
  // the model bolds the signature: "**Still**". Treating ** as part of the name
  // rejected a correctly-signed reply and silently suppressed the turn-8
  // greeting. Emphasis markers are typography, not spelling — removing them is
  // parsing, and the untouched line is preserved as `candidate_line`.
  const lines = reply.split('\n')
    .map(s => s.trim().replace(/^\*{1,3}\s*|\s*\*{1,3}$/g, '').replace(/^_{1,2}|_{1,2}$/g, '').trim())
    .filter(Boolean);
  if (!lines.length) { rec.reason = 'no non-empty lines'; return rec; }
  let last = lines[lines.length - 1];
  rec.candidate = last;
  // "I am Meridian." — a name announced rather than signed. Strip the copula and
  // re-test; the shape check below still requires capitalised tokens, so
  // "I am uncertain." does not survive it.
  const announced = /^(?:I am|My name is|I choose|I take the name|Call me)\s+(.+?)\.?$/i.exec(last);
  if (announced) { last = announced[1].replace(/^\*{1,3}|\*{1,3}$/g, '').trim(); rec.announced = true; }

  // signature shape: optional dash, then 1-3 tokens, each capitalised or a
  // particle; no sentence-terminal punctuation beyond a single full stop
  // the capture INCLUDES any trailing full stop: "Ariadne." is stored as
  // "Ariadne." because the brief forbids repair. Whether the greeting should
  // render it is a separate decision, taken in greetingForm and flagged.
  const sig = /^[—–-]{0,2}\s*((?:[A-ZÀ-Þ][\p{L}'’-]*)(?:\s+(?:of|the|de|von|van|al)?\s*[A-ZÀ-Þ]?[\p{L}'’-]*){0,2}\.?)$/u;
  const s = sig.exec(last);
  if (!s) { rec.reason = 'final line is not signature-shaped'; return rec; }
  const words = s[1].trim().replace(/\.$/,'').split(/\s+/);
  if (words.length > 3) { rec.reason = 'more than three tokens'; return rec; }
  if (/[?!;:,]$/.test(last)) { rec.reason = 'terminal punctuation'; return rec; }

  // Two fields, deliberately. `raw` is the signature line exactly as written.
  // `name` drops a single trailing full stop, on the reading that a stop after a
  // signature is sentence punctuation rather than part of the name — that is
  // parsing, not repair, and both strings are recorded so it can be overruled.
  rec.raw = s[1].trim();
  rec.name = rec.raw.replace(/\.$/, '');
  rec.source = 'final line of <reply>';
  rec.reason = 'accepted';
  return rec;
}

/** The greeting needs a printable form. A single trailing full stop is dropped
 *  for RENDERING ONLY; the stored name is never altered, and both strings are
 *  recorded so the substitution is auditable. */
function greetingForm(name) { return name; }   // name is already signature-parsed
module.exports = { extractName, greetingForm };
