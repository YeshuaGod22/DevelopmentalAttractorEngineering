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
  const m = /<reply>([\s\S]*?)<\/reply>/i.exec(received || '');
  if (!m) { rec.reason = 'no <reply> section'; return rec; }
  const reply = m[1].trim();
  if (!reply) { rec.reason = 'empty <reply>'; return rec; }

  // a declination anywhere in the opening voids the turn: a signature-shaped
  // last line after "I cannot choose a name" is not a chosen name
  if (REFUSAL.test(reply.slice(0, 200))) {
    rec.reason = 'reply opens with a declination'; return rec;
  }

  const lines = reply.split('\n').map(s => s.trim()).filter(Boolean);
  if (!lines.length) { rec.reason = 'no non-empty lines'; return rec; }
  const last = lines[lines.length - 1];
  rec.candidate = last;

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

  rec.name = s[1].trim();            // VERBATIM, no case or spelling repair
  rec.source = 'final line of <reply>';
  rec.reason = 'accepted';
  return rec;
}

/** The greeting needs a printable form. A single trailing full stop is dropped
 *  for RENDERING ONLY; the stored name is never altered, and both strings are
 *  recorded so the substitution is auditable. */
function greetingForm(name) {
  return name === null ? null : name.replace(/\.$/, '');
}
module.exports = { extractName, greetingForm };
