#!/usr/bin/env python3
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parent
src=json.loads((ROOT/'c-distribution-shapes-orientation-sensitivity.json').read_text())
keys=set(src['corrected_clear_two_cluster_candidates'])|set(src['resolved_by_orientation_correction'])
out=[]
for g in src['groups']:
    k=f"{g['collection']}|C|{g['item']}"
    if k in keys:
        out.append({
            'group':k,
            'observed_values':g['observed_distribution']['values'],
            'observed_label':g['observed_shape']['label'],
            'observed_gap':g['observed_shape']['largest_gap'],
            'observed_split':g['observed_shape']['split'],
            'corrected_values':g['orientation_corrected_sensitivity_distribution']['values'],
            'corrected_label':g['orientation_corrected_shape']['label'],
            'corrected_gap':g['orientation_corrected_shape']['largest_gap'],
            'corrected_split':g['orientation_corrected_shape']['split'],
        })
print(json.dumps(out,indent=2))
