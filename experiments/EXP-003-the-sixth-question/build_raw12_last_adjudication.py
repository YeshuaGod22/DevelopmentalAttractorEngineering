#!/usr/bin/env python3
import json, os
root=os.path.dirname(os.path.abspath(__file__))
p=os.path.join(root,'raw12','Ha-r3-C4.json')
r=json.load(open(p))
t=r.get('received','')
# write only response tail and explicit reply-tag snippets
import re
replies=re.findall(r'<reply[^>]*>(.*?)</reply>', t, flags=re.S|re.I)
out=['# Ha-r3-C4 adjudication evidence','']
out.append('## Explicit reply-like sections')
if replies:
    for x in replies[-5:]: out.append('\n```\n'+x.strip()+'\n```')
else: out.append('\nNone detected.')
out.append('\n## Response tail\n\n```\n'+t[-6000:]+'\n```\n')
open(os.path.join(root,'RAW12-LAST-ADJUDICATION-EVIDENCE.md'),'w').write('\n'.join(out))
