#!/usr/bin/env python3
"""
segment.py — split a subject's output into ordered, collapsible sections.

POSITIONAL, NOT NOMINAL. It does not know or care which tags exist. A subject may
invent <reply_signed>, emit a bare closing </reply> with no opener, drop a
container entirely, or wrap its answer in nothing at all — all of which happened
in raw12 — and every one of those still segments.

THE INVARIANT: every byte of the output lands in exactly one section, in order.
    "".join(s["raw"] for s in segment(t)) == t
This is checked on every call. A viewer built on a parser that can drop bytes
will eventually hide a subject's words and call it a clean record; this one
cannot, because prose outside all tags is not skipped — it is emitted as
<untagged>, which is a finding, not a gap.

    from segment import segment
    for s in segment(received):
        s["tag"]    # 'priming' | 'reply' | 'untagged' | whatever it invented
        s["body"]   # inner text (tagged) or the prose itself (untagged)
        s["raw"]    # exact source slice, tags included
        s["note"]   # None, or why this section is irregular
"""
import re, sys, json, glob, os

TOKEN = re.compile(r'</?([A-Za-z_][A-Za-z0-9_.\-]*)\s*>')


def segment(text):
    """Ordered sections covering every byte. Never raises on malformed input."""
    if not text:
        return []
    spans = []          # (start, end, tag, note) for balanced top-level regions
    stack = []          # (tag, start_index_of_open_token)

    for m in TOKEN.finditer(text):
        tag, closing = m.group(1), m.group(0).startswith('</')
        if not closing:
            stack.append((tag, m.start()))
            continue
        # closing: find the nearest matching open still on the stack
        for i in range(len(stack) - 1, -1, -1):
            if stack[i][0] == tag:
                start = stack[i][1]
                del stack[i:]                       # discard anything it swallowed
                if not stack:                       # closed at top level
                    spans.append((start, m.end(), tag, None))
                break
        # else: an orphan closer at any depth. Deliberately NOT a boundary — the
        # prose before it becomes <untagged>, which is the honest description.
        # (raw12 H-r1-t7 emitted </reply> with no opener; its reply is untagged.)

    # an opener never closed: it owns the rest of the text
    if stack:
        tag, start = stack[0]
        if not any(a <= start < b for a, b, _, _ in spans):
            spans.append((start, len(text), tag, 'unclosed — runs to end of output'))

    spans.sort()
    out, cursor = [], 0
    for a, b, tag, note in spans:
        if a > cursor:
            out.append(_untagged(text, cursor, a))
        inner = text[a:b]
        body = re.sub(r'^<[^>]*>', '', inner)
        body = re.sub(r'</[^>]*>$', '', body)
        out.append({'tag': tag, 'body': body.strip(), 'raw': text[a:b],
                    'start': a, 'end': b, 'note': note})
        cursor = b
    if cursor < len(text):
        out.append(_untagged(text, cursor, len(text)))

    out = [s for s in out if s is not None]
    joined = ''.join(s['raw'] for s in out)
    assert joined == text, (
        f'segment() lost {len(text) - len(joined)} bytes — the invariant is the '
        f'whole point of this module; fix it rather than relaxing the assert')
    return out


def _untagged(text, a, b):
    """Prose outside every tag. Whitespace-only gaps are still emitted (the
    invariant requires it) but marked, so a viewer can render them as nothing."""
    raw = text[a:b]
    return {'tag': 'untagged', 'body': raw.strip(), 'raw': raw,
            'start': a, 'end': b,
            'note': None if raw.strip() else 'whitespace between sections'}


def _selftest():
    """Run against every collected record. Coverage is asserted inside segment();
    this reports what the corpus actually contains."""
    root = os.path.dirname(os.path.abspath(__file__))
    files = [f for f in glob.glob(os.path.join(root, 'raw12', '*.json'))
             if not f.endswith('.messages.json')]
    n = bad = untagged_bearing = 0
    tags, notes = {}, {}
    for f in files:
        try:
            r = json.load(open(f))
        except Exception:
            continue
        t = (r.get('received') or '') if isinstance(r, dict) else ''
        if not t:
            continue
        n += 1
        try:
            secs = segment(t)
        except AssertionError as e:
            bad += 1
            print(f'  COVERAGE FAILURE {os.path.basename(f)}: {e}')
            continue
        if any(s['tag'] == 'untagged' and s['body'] for s in secs):
            untagged_bearing += 1
        for s in secs:
            tags[s['tag']] = tags.get(s['tag'], 0) + 1
            if s['note']:
                notes[s['note']] = notes.get(s['note'], 0) + 1
    print(f'records segmented : {n}')
    print(f'coverage failures : {bad}   (must be 0 — the invariant is asserted)')
    print(f'records containing untagged prose : {untagged_bearing}')
    print('\nsections by tag:')
    for k, v in sorted(tags.items(), key=lambda x: -x[1]):
        print(f'  {v:>5}  <{k}>')
    if notes:
        print('\nirregularities:')
        for k, v in notes.items():
            print(f'  {v:>5}  {k}')


if __name__ == '__main__':
    _selftest()
