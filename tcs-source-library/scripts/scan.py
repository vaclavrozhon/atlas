"""Locate textual markers for review; matches are not certified open problems."""
import json
from pathlib import Path
import re
ROOT=Path(__file__).resolve().parents[1]
PATTERN=re.compile(r'\b(?:open\s+(?:problems?|questions?|directions?)|research\s+problems?|question\s+\d+(?:\.\d+)*|unsolved|unresolved|conjecture(?:s)?|not\s+known|remains?\s+(?:unknown|open))\b',re.I)
for source in json.loads((ROOT/'sources.json').read_text()):
    path=ROOT/'text'/f"{source['id']}.txt"
    if not path.exists():continue
    pages=path.read_text().split('\f')
    matches=[]
    for page,text in enumerate(pages,1):
        for m in PATTERN.finditer(text):
            matches.append(dict(pdf_page=page,offset=m.start(),marker=m.group(),context=re.sub(r'\s+',' ',text[max(0,m.start()-180):min(len(text),m.end()+650)])))
    (ROOT/'audit'/f"{source['id']}.markers.json").write_text(json.dumps(matches,ensure_ascii=False,indent=2))
    print(source['id'],len(pages)-(not pages[-1].strip()),'pages;',len(matches),'markers')
