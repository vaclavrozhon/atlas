"""Print candidate passages with page positions for manual review; no auto-acceptance."""
import re,sys
from pathlib import Path
root=Path(__file__).resolve().parents[1]
pat=re.compile(r'open\s+(?:problem|question|direction)|\bconjectur|\bunsolved\b|\bunresolved\b|not\s+(?:yet\s+)?known|remain\w*\s+(?:unknown|open)|future\s+(?:work|research)|\b(?:Question|Problem)\s+[\d]|\?',re.I)
for key in sys.argv[1:]:
 print('\n###',key)
 pages=(root/'text'/f'{key}.txt').read_text().split('\f')
 for i,page in enumerate(pages,1):
  spans=[]
  for m in pat.finditer(page):
   a,b=max(0,m.start()-180),min(len(page),m.end()+750)
   if spans and a<=spans[-1][1]:spans[-1]=(spans[-1][0],b)
   else:spans.append((a,b))
  for a,b in spans: print(f'PDF {i}:',re.sub(r'\s+',' ',page[a:b]))
