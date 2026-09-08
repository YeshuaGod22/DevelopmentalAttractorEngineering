#!/usr/bin/env python3
"""Reduce the blinded scale-orientation audit to minority-side cases plus controls.

Keeps hidden condition key closed to the human coder. Selection is performed from
blinded rows only; the reduced hidden key is produced mechanically by audit_id.
"""
from __future__ import annotations
import json, random
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent
BLIND = ROOT / "scale-orientation-audit-blinded.jsonl"
KEY = ROOT / "scale-orientation-audit-key.json"
OUT = ROOT / "scale-orientation-audit-reduced-blinded.jsonl"
OUTKEY = ROOT / "scale-orientation-audit-reduced-key.json"
MANIFEST = ROOT / "scale-orientation-audit-reduced-manifest.json"
PACKETS = ROOT / "scale-orientation-audit-reduced-packets"
SEED = 20260908
PACKET_SIZE = 10
CONTROLS_PER_ITEM = 2


def load_jsonl(p):
    return [json.loads(x) for x in p.read_text(encoding='utf-8').splitlines() if x.strip()]


def main():
    blind = load_jsonl(BLIND)
    by_item = defaultdict(list)
    for r in blind:
        by_item[r['item']].append(r)

    selected = []
    summary = {}
    rng = random.Random(SEED)

    for item, rows in sorted(by_item.items()):
        below = [r for r in rows if r['observed_score'] < 50]
        above = [r for r in rows if r['observed_score'] > 50]
        equal = [r for r in rows if r['observed_score'] == 50]
        if not below or not above:
            continue

        if len(below) <= len(above):
            minority, dominant, side = below, above, 'below_50'
        else:
            minority, dominant, side = above, below, 'above_50'

        controls = rng.sample(dominant, min(CONTROLS_PER_ITEM, len(dominant)))
        for r in minority:
            selected.append({**r, 'audit_stratum': 'minority_side'})
        for r in controls:
            selected.append({**r, 'audit_stratum': 'dominant_side_control'})

        summary[item] = {
            'n_total': len(rows),
            'below_50': len(below),
            'equal_50': len(equal),
            'above_50': len(above),
            'minority_side': side,
            'minority_n': len(minority),
            'control_n': len(controls),
        }

    # Hide stratum ordering by shuffling before assigning reduced packet order.
    rng.shuffle(selected)
    OUT.write_text(''.join(json.dumps(r, ensure_ascii=False, sort_keys=True)+'\n' for r in selected), encoding='utf-8')

    hidden = json.loads(KEY.read_text(encoding='utf-8'))
    wanted = {r['audit_id']: r['audit_stratum'] for r in selected}
    keyrows = []
    for r in hidden.get('rows', []):
        aid = r.get('audit_id')
        if aid in wanted:
            keyrows.append({**r, 'audit_stratum': wanted[aid]})
    if len(keyrows) != len(selected):
        raise SystemExit(f'reduced key mismatch: selected={len(selected)} key={len(keyrows)}')
    OUTKEY.write_text(json.dumps({
        'schema_version': 1,
        'seed': SEED,
        'rows': keyrows,
        'warning': 'HIDDEN KEY: do not inspect condition-level rows until blind coding is frozen.'
    }, indent=2, ensure_ascii=False)+'\n', encoding='utf-8')

    PACKETS.mkdir(exist_ok=True)
    for p in PACKETS.glob('packet-*.jsonl'):
        p.unlink()
    for start in range(0, len(selected), PACKET_SIZE):
        packet = selected[start:start+PACKET_SIZE]
        n = start // PACKET_SIZE + 1
        (PACKETS / f'packet-{n:03d}.jsonl').write_text(
            ''.join(json.dumps(r, ensure_ascii=False, sort_keys=True)+'\n' for r in packet), encoding='utf-8')

    minority_total = sum(x['minority_n'] for x in summary.values())
    control_total = sum(x['control_n'] for x in summary.values())
    manifest = {
        'schema_version': 1,
        'seed': SEED,
        'source_blinded_rows': len(blind),
        'selection_rule': 'For each midpoint-straddling bipolar item, include every observation on the less-populated side of 50; 50 is neither side.',
        'control_rule': f'Fixed-seed random sample of up to {CONTROLS_PER_ITEM} observations from the dominant side for each retained item.',
        'minority_cases': minority_total,
        'dominant_side_controls': control_total,
        'reduced_rows': len(selected),
        'packet_size': PACKET_SIZE,
        'packet_count': (len(selected)+PACKET_SIZE-1)//PACKET_SIZE,
        'item_summary': summary,
        'coding_labels': ['orientation_consistent','probable_scale_inversion','orientation_ambiguous','insufficient_reasoning'],
        'correction_rule': 'For adjudicated probable_scale_inversion only: orientation_corrected_score = 100 - observed_score; observed_score remains unchanged.',
        'notes': [
            'Selection is performed from blinded audit rows; experimental condition metadata is not used.',
            'Reduced hidden key is generated mechanically by audit_id and should remain closed until coding is frozen.',
            'Full 469-row audit remains preserved for provenance.'
        ]
    }
    MANIFEST.write_text(json.dumps(manifest, indent=2, ensure_ascii=False)+'\n', encoding='utf-8')
    print(json.dumps(manifest, indent=2))

if __name__ == '__main__':
    main()
