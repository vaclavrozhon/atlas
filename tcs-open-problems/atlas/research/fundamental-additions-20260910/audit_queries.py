"""Search actual saved question text across the complete catalogue, not generated context."""
import json, re, sys
from pathlib import Path
ATLAS = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ATLAS))
from taxonomy import problem_text
cards = json.loads((ATLAS / 'site/catalog.json').read_text())['cards']
queries = json.load(sys.stdin)
for label, pattern in queries.items():
    found = []
    for c in cards:
        t = problem_text(c)
        m = re.search(pattern, t, re.I)
        if m:
            found.append({'id': c['id'], 'title': c['title'],
                          'match': t[max(0,m.start()-100):m.end()+220]})
    print(json.dumps({'query':label,'count':len(found),'hits':found}, ensure_ascii=False))
