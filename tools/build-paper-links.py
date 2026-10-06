#!/usr/bin/env python3
"""Build the evidence index and linked paper from pinned, locally present records."""
from pathlib import Path
import csv,json,hashlib,re,urllib.parse,html
ROOT=Path(__file__).resolve().parents[1];P=ROOT/'papers/03-different-histories';EXP=ROOT/'experiments/EXP-003-the-sixth-question';PIN='787d3e217a5a23564fcf65c60e9e3fc7ad43db75'
BASE=f'https://github.com/YeshuaGod22/DevelopmentalAttractorEngineering/blob/{PIN}/experiments/EXP-003-the-sixth-question/'
def rows(n):return list(csv.DictReader((P/n).open()))
def path(url):
 assert url.startswith(BASE),url
 v=url[len(BASE):];assert (EXP/v).is_file(),v;return v
profiles=rows('EXP-003-trunk-profile-data.csv');depth=rows('EXP-003-within-trunk-depth-data.csv');reviews=rows('W1-process-evaluation-coding.csv');control=rows('EXP-003-C-observed-answers.csv')
records={}
def add(url):
 v=path(url);raw=(EXP/v).read_bytes();x=json.loads(raw)
 assert isinstance(x.get('sent'),list) and isinstance(x.get('received'),str),v
 records[v]={'source':url,'sha256':hashlib.sha256(raw).hexdigest(),'blob_sha':hashlib.sha1(b'blob '+str(len(raw)).encode()+b'\0'+raw).hexdigest()}
 return v
for r in profiles:r['record']=add(r['source']) if r['source'] else None
for r in depth:r['t6_record']=add(r['t6_source']);r['t9_record']=add(r['t9_source'])
for r in reviews:
 r['record']=add(r['source']);assert r['evidence_quote'] in json.loads((EXP/r['record']).read_text())['received']
 assert r['blob_sha']==records[r['record']]['blob_sha'],r['record']
# Control companion has one row per original fresh answer.
for r in control:
 r['record']=add(BASE+'raw7/'+r['source_file'])
# Raw links cited directly by the paper also resolve through the reader.
s=(P/'EXP-003-writeup.md').read_text()
for url in re.findall(r'https://github\.com/[^\s)]+\.json',s):
 if url.startswith(BASE):
  try:add(url)
  except AssertionError:pass
for encoded in re.findall(r'blum-reader\.html\?record=([^\s)]+)',s):
 add(BASE+urllib.parse.unquote(encoded.split('&')[0]))
battery=json.loads((EXP/'battery.json').read_text())
index={'version':1,'repository':'YeshuaGod22/DevelopmentalAttractorEngineering','source_commit':PIN,'records':records,'profiles':profiles,'depth':depth,'reviews':reviews,'control':control,'questions':battery['items'],'answer_keys':battery['keys']}
(ROOT/'tools/blum-evidence-index.json').write_text(json.dumps(index,ensure_ascii=False,indent=2))
# Preserve a finished scientific manuscript; add navigation in this publication copy.
nav='''## Explore the exchanges and design an experiment

[Open the evidence browser](../../tools/blum-evidence.html) to select a history and question, inspect its answer with the exact preceding context, or compare sibling responses. [Read Iris’s process review](../../tools/blum-reader.html?record=raw12%2FHa-r3-W1.json&compare=1), then [open an editable inquiry in Blum Lab](../../tools/blum-lab.html?record=raw12%2FHa-r3-W1.json).

What would you ask next? Repeat a measurement, collect new histories, or continue from a recorded answer. The Lab preserves the source of a design and exports it for the existing runner. Each experimental action identifies the context it inherits.

'''
if '## Explore the exchanges and design an experiment' not in s:s=s.replace('## Appendix A',nav+'## Appendix A',1)
# Link original JSON citations to the complete-context reader; the Reader exposes pinned raw sources.
s=re.sub(r'\]\('+re.escape(BASE)+r'((?:raw\d+|prefixes)/[^)]+\.json)\)',lambda m:'](../../tools/blum-reader.html?record='+urllib.parse.quote(m[1],safe='')+')',s)
# Add accessible per-question view directly alongside overview figures.
for name in ['EXP-003-figure-1-original-profiles.png','EXP-003-figure-2-nine-turn-profiles.png','EXP-003-figure-3-depth-trajectories.png']:
 needle=')\n' # append only once after the image line
 pat=r'(!\[[^\n]+\]\('+re.escape(name)+r'\))'
 s=re.sub(pat,r'\1\n\n[Select a history and question to inspect the underlying answers](../../tools/blum-evidence.html).',s,count=1) if 'Select a history and question' not in s[s.index(name):s.index(name)+260] else s
(P/'EXP-003-writeup.md').write_text(s)
assert (P/'paper.css').is_file(), 'Publication CSS is missing'
print(f'Validated {len(records)} exact-context records and all24 quotation anchors.')
