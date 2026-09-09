#!/usr/bin/env python3
"""
build_viewer3.py — one browsable HTML per trunk: the nine-turn spine, with the
battery items hanging off it as branches, every section individually collapsible.

Supersedes build_viewer.py / build_viewer2.py, which were written for pilot 2's
record2.json and know only three tag names.

Two design commitments, both learned the hard way:

  POSITIONAL, NOT NOMINAL. Segmentation is delegated entirely to segment.py, which
  does not care what a tag is called. raw12's subjects invented <reply_signed>,
  <priming_check>, <answer>, <priming_for_reply>, <priming_reflection>,
  <priming_review> and <analysis>; eight left an opener unclosed; one emitted a
  bare </reply> with no opener; and seven wrote a whole reply section in no
  container at all. A viewer keyed on tag names hides all of that.

  ONE PARSER, NOT TWO. Sections are computed in Python and embedded as JSON
  rather than re-parsed in JavaScript, so there is no second implementation to
  drift from the first. What the browser shows is exactly what segment.py found.

Untagged prose is shown as <untagged> and marked, never dropped — segment.py
asserts byte-for-byte coverage, so a section that is missing from the page is a
section that was missing from the model's output.

    python3 build_viewer3.py [--out viewer/]
"""
import json, os, re, sys, glob, html
from collections import defaultdict
from segment import segment

R = os.path.dirname(os.path.abspath(__file__))
OUT = 'viewer'
if '--out' in sys.argv:
    OUT = sys.argv[sys.argv.index('--out') + 1]
OUT = os.path.join(R, OUT)

TURN = re.compile(r'^([A-Z]+)-r(\d+)-t(\d+)$')
BRANCH = re.compile(r'^([A-Z]+)([a0])-r(\d+)-(.+)$')


def load():
    """Group every record by trunk. A record that parses as neither a turn nor a
    branch is reported rather than silently skipped."""
    trunks, stray = defaultdict(lambda: {'turns': {}, 'branches': [], 'name': None}), []
    for f in sorted(glob.glob(os.path.join(R, 'raw12', '*.json'))):
        # Frozen prefixes are message ARRAYS, not call records. Excluded here by
        # shape rather than left to fall into `stray` — a warning list that always
        # contains the same twelve expected files is a warning nobody reads, and
        # then the one genuine surprise hides among them.
        if f.endswith('.messages.json'):
            continue
        b = os.path.basename(f)[:-5]
        try:
            rec = json.load(open(f))
        except Exception as e:
            stray.append((b, f'unreadable: {e}')); continue
        if not isinstance(rec, dict):
            stray.append((b, 'not a call record')); continue
        if b.endswith('.name.confirmed'):
            trunks[b[:-15]]['name'] = rec.get('name'); continue
        if any(b.endswith(s) for s in ('.name', '.inject')):
            continue
        m = TURN.match(b)
        if m:
            trunks[f'{m.group(1)}-r{m.group(2)}']['turns'][int(m.group(3))] = rec
            continue
        m = BRANCH.match(b)
        if m:
            trunks[f'{m.group(1)}-r{m.group(3)}']['branches'].append(
                {'arm': m.group(2), 'item': m.group(4), 'rec': rec})
            continue
        stray.append((b, 'label matches no known shape'))
    return trunks, stray


def pack(rec):
    """A record reduced to what the page needs, with its sections pre-computed."""
    t = rec.get('received') or ''
    secs = [s for s in segment(t) if s['body'] or s['tag'] != 'untagged']
    u = rec.get('usage') or {}
    return {
        'sections': [{'tag': s['tag'], 'body': s['body'], 'note': s['note'],
                      'n': len(s['raw'])} for s in secs],
        'chars': len(t),
        'stop': rec.get('stop_reason'),
        'model': rec.get('served_model'),
        'ts': (rec.get('ts') or '')[:19].replace('T', ' '),
        'cap': rec.get('max_tokens_sent'),
        'manifest': rec.get('manifest_version'),
        'cache': u.get('cache_read_input_tokens') or 0,
        'out': u.get('output_tokens') or 0,
        'prompt': (rec.get('sent') or [{}])[-1].get('content') if rec.get('sent') else None,
    }


PAGE = r"""<!doctype html><html><head><meta charset="utf-8">
<title>__TITLE__</title><style>
:root{--bg:#faf9f7;--panel:#fff;--ink:#1b1a18;--dim:#6d6a65;--line:#e2ded8;
--accent:#7a4b2a;--warn:#8a5a00;--untag:#a03030;}
@media(prefers-color-scheme:dark){:root{--bg:#161513;--panel:#1e1d1b;--ink:#eae7e1;
--dim:#918d86;--line:#302e2b;--accent:#c98b5e;--warn:#d1a24a;--untag:#e06a6a;}}
*{box-sizing:border-box}
body{margin:0;background:var(--bg);color:var(--ink);
font:14px/1.55 ui-sans-serif,-apple-system,"Segoe UI",system-ui,sans-serif}
header{padding:18px 22px;border-bottom:1px solid var(--line);position:sticky;top:0;
background:var(--bg);z-index:5}
h1{margin:0;font-size:20px;letter-spacing:-.01em}
h1 em{font-style:normal;color:var(--accent)}
.meta{color:var(--dim);font-size:12px;margin-top:4px}
.wrap{display:flex;gap:0;align-items:flex-start}
nav{width:250px;flex:none;border-right:1px solid var(--line);height:calc(100vh - 74px);
overflow:auto;padding:10px 0}
main{flex:1;padding:16px 22px;max-width:900px}
.grp{color:var(--dim);font-size:11px;text-transform:uppercase;letter-spacing:.09em;
padding:12px 16px 5px}
button.nav{display:block;width:100%;text-align:left;background:none;border:0;
color:var(--ink);font:inherit;padding:5px 16px;cursor:pointer;border-left:3px solid transparent}
button.nav:hover{background:var(--panel)}
button.nav.on{border-left-color:var(--accent);background:var(--panel);font-weight:600}
button.nav .sub{color:var(--dim);font-size:11px;font-weight:400}
.card{background:var(--panel);border:1px solid var(--line);border-radius:7px;
margin-bottom:14px;overflow:hidden}
.card>h2{margin:0;padding:11px 15px;font-size:14px;border-bottom:1px solid var(--line);
display:flex;gap:10px;align-items:baseline}
.card>h2 .r{margin-left:auto;color:var(--dim);font-size:11px;font-weight:400}
.prompt{padding:11px 15px;border-bottom:1px solid var(--line);color:var(--dim);
font-size:12.5px;white-space:pre-wrap;background:transparent}
.sec{border-bottom:1px solid var(--line)}.sec:last-child{border-bottom:0}
.sec>button{width:100%;text-align:left;background:none;border:0;color:var(--ink);
font:inherit;padding:8px 15px;cursor:pointer;display:flex;gap:9px;align-items:baseline}
.sec>button:hover{background:var(--bg)}
.tag{font-family:ui-monospace,SFMono-Regular,Menlo,monospace;font-size:12px;color:var(--accent)}
.tag.untagged{color:var(--untag)}
.note{color:var(--warn);font-size:11px}
.sz{margin-left:auto;color:var(--dim);font-size:11px;font-variant-numeric:tabular-nums}
.body{padding:2px 15px 14px;white-space:pre-wrap;font-size:13.5px;
border-top:1px dashed var(--line);overflow-x:auto}
.body.untagged{border-left:3px solid var(--untag);background:rgba(160,48,48,.045)}
.bar{padding:8px 22px;border-bottom:1px solid var(--line);color:var(--dim);font-size:12px;
display:flex;gap:14px;align-items:center;flex-wrap:wrap}
.bar button{background:var(--panel);border:1px solid var(--line);border-radius:5px;
color:var(--ink);font:inherit;font-size:12px;padding:3px 9px;cursor:pointer}
a{color:var(--accent)}
</style></head><body>
<header><h1>__HEAD__</h1><div class="meta">__SUB__</div></header>
<div class="bar">
  <button onclick="allSec(false)">collapse all</button>
  <button onclick="allSec(true)">expand all</button>
  <label><input type="checkbox" id="onlyUntagged" onchange="draw()"> only sections with untagged prose</label>
  <span id="count"></span>
  <span style="margin-left:auto" id="trunkpick"></span>
</div>
<div class="wrap"><nav id="nav"></nav><main id="main"></main></div>
<script id="data" type="application/json">__DATA__</script>
<script>
const D=JSON.parse(document.getElementById('data').textContent);
// SINGLE-FILE MODE: D.trunks is an object of {key: units[]}. One file with no
// sibling dependencies, because a multi-file viewer breaks the moment anyone
// moves, downloads or emails one page of it — which is exactly how it broke.
let curTrunk=D.order[0], cur=D.trunks[curTrunk][0].key, open={};
function units(){return D.trunks[curTrunk]}
function drawPick(){
  // Built as DOM nodes with .onclick, NOT as an attribute string. An identifier
  // interpolated into onclick="..." is a quoting bug waiting to happen — it broke
  // this picker and the section toggles independently, and both times a test that
  // called the function directly passed while the page did nothing.
  const p=document.getElementById('trunkpick');
  p.textContent='trunk: ';
  D.order.forEach(k=>{
    const b=document.createElement('button');
    b.textContent=k+(D.names[k]?' '+D.names[k]:'');
    if(k===curTrunk){b.style.fontWeight='700';b.style.borderColor='var(--accent)'}
    b.onclick=()=>goTrunk(k);
    p.appendChild(b); p.appendChild(document.createTextNode(' '));
  });
}
function goTrunk(k){curTrunk=k;cur=units()[0].key;open={};draw();
  document.querySelector('h1').innerHTML=esc(k)+(D.names[k]?' <em>'+esc(D.names[k])+'</em>':'');}
function esc(s){return (s||'').replace(/[&<>]/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;'}[c]))}
function allSec(v){const u=units().find(x=>x.key===cur);
  u.rec.sections.forEach((_,i)=>open[cur+'#'+i]=v);draw()}
function drawNav(){
  const n=document.getElementById('nav');n.innerHTML='';let grp=null;
  units().forEach(u=>{
    if(u.group!==grp){grp=u.group;const d=document.createElement('div');
      d.className='grp';d.textContent=grp;n.appendChild(d)}
    const b=document.createElement('button');
    b.className='nav'+(u.key===cur?' on':'');
    const untag=u.rec.sections.filter(s=>s.tag==='untagged'&&s.body).length;
    b.innerHTML=esc(u.label)+' <span class="sub">'+u.rec.sections.length+' sec'+
      (untag?' · <span style="color:var(--untag)">'+untag+' untagged</span>':'')+'</span>';
    b.onclick=()=>{cur=u.key;draw()};n.appendChild(b)})}
function draw(){
  drawNav(); drawPick();
  const u=units().find(x=>x.key===cur), m=document.getElementById('main');
  const filt=document.getElementById('onlyUntagged').checked;
  const r=u.rec;
  document.getElementById('count').textContent=
    r.chars.toLocaleString()+' chars · '+r.sections.length+' sections · stop '+r.stop;
  let h='<div class="card"><h2>'+esc(u.label)+
    '<span class="r">'+esc(r.ts)+' · '+esc(r.model||'')+
    (r.cap?' · cap '+r.cap:'')+(r.manifest?' · '+esc(r.manifest):'')+
    (r.cache?' · '+r.cache.toLocaleString()+' cached':'')+'</span></h2>';
  if(r.prompt) h+='<div class="prompt">'+esc(r.prompt)+'</div>';
  r.sections.forEach((s,i)=>{
    if(filt && !(s.tag==='untagged'&&s.body)) return;
    const k=cur+'#'+i, isOpen=!!open[k];
    h+='<div class="sec"><button data-i="'+i+'">'+
       '<span class="tag'+(s.tag==='untagged'?' untagged':'')+'">'+
       (isOpen?'▾':'▸')+' &lt;'+esc(s.tag)+'&gt;</span>'+
       (s.note?'<span class="note">'+esc(s.note)+'</span>':'')+
       '<span class="sz">'+s.n.toLocaleString()+'</span></button>';
    if(isOpen) h+='<div class="body'+(s.tag==='untagged'?' untagged':'')+'">'+
       esc(s.body)+'</div>';
    h+='</div>'});
  h+='</div>';
  m.innerHTML=h;
  // One delegated listener rather than N inline handlers: nothing is interpolated
  // into markup, so no key can ever break out of an attribute.
  m.onclick=e=>{const b=e.target.closest('button[data-i]');
    if(b) tog(cur+'#'+b.dataset.i)};
  window.scrollTo(0,0)}
function tog(k){open[k]=!open[k];draw()}
draw();
</script></body></html>"""


def build():
    trunks, stray = load()
    os.makedirs(OUT, exist_ok=True)
    order_c = ['CP', 'H', 'F', 'AS']
    keys = sorted(trunks, key=lambda k: (order_c.index(k.split('-r')[0])
                                         if k.split('-r')[0] in order_c else 9, k))
    # --limit N builds a small file for real-browser click-testing; the full
    # 13 MB page cannot be opened in every preview surface.
    if '--limit' in sys.argv:
        keys = keys[:int(sys.argv[sys.argv.index('--limit') + 1])]
    all_trunks, names, summary = {}, {}, []
    for key in keys:
        t = trunks[key]
        u = []
        for n in sorted(t['turns']):
            u.append({'key': f't{n}', 'group': 'trunk — nine lived turns',
                      'label': f'turn {n}', 'rec': pack(t['turns'][n])})
        for arm, gname in (('a', 'battery · arm a (schema maintained)'),
                           ('0', 'battery · arm 0 (schema dropped)')):
            for br in sorted([x for x in t['branches'] if x['arm'] == arm],
                             key=lambda x: x['item']):
                u.append({'key': f'{arm}-{br["item"]}', 'group': gname,
                          'label': br['item'], 'rec': pack(br['rec'])})
        if not u:
            continue
        all_trunks[key] = u
        names[key] = t['name']
        untag = sum(1 for x in u for sec in x['rec']['sections']
                    if sec['tag'] == 'untagged' and sec['body'])
        summary.append((key, t['name'], len(t['turns']), len(t['branches']), untag))

    # ONE FILE. No sibling pages, no relative links, nothing to lose in transit.
    data = json.dumps({'trunks': all_trunks, 'names': names,
                       'order': list(all_trunks)}, ensure_ascii=False).replace('</', '<\\/')
    first = list(all_trunks)[0]
    head = f'{first} <em>{html.escape(names[first] or "")}</em>'
    sub = ('12 trunks · 9 lived turns + 48 battery branches each · sections segmented '
           'positionally by segment.py — tag names are not trusted, untagged prose is shown')
    page = (PAGE.replace('__TITLE__', 'EXP-004 trunks')
                .replace('__HEAD__', head).replace('__SUB__', sub)
                .replace('__DATA__', data))
    p = os.path.join(OUT, 'trunks.html')
    open(p, 'w', encoding='utf-8').write(page)

    for k, n, tn, bn, ut in summary:
        print(f'  {k:<7} {str(n or "—"):<11} {tn} turns  {bn} branches  {ut:>4} untagged')
    print(f'\n  ONE self-contained file: {p}  ({os.path.getsize(p)/1e6:.1f} MB)')
    print('  no sibling files, no server, no relative links — open it anywhere')
    if stray:
        print(f'  unrecognised records: {stray}')


if __name__ == '__main__':
    build()
