"""Refresh only the ten primary source caches used by parse.py.
Run in the repository root; requires requests. Existing catalog is never changed.
"""
import hashlib,json
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor
import requests
BASE=Path(__file__).resolve().parent
ROOT=BASE.parents[1]
def fetch(url):
    r=requests.get(url,timeout=90);r.raise_for_status()
    path=BASE/'cache'/(hashlib.sha256(url.encode()).hexdigest()[:20]+('.js' if url.endswith('.js') else '.html'))
    path.parent.mkdir(exist_ok=True);path.write_text(r.text)
    return dict(url=url,file=str(path.relative_to(ROOT)),status=r.status_code,bytes=len(r.content))
urls=[f'https://acm-stoc.org/stoc{y}/toc.html' for y in range(2022,2027)]
urls += [f'https://ieee-focs.org/FOCS-{y}-Papers/data/data.js' for y in range(2021,2026)]
with ThreadPoolExecutor(max_workers=5) as pool: results=list(pool.map(fetch,urls))
(BASE/'discovery.json').write_text(json.dumps(results[:5],indent=2))
(BASE/'discovery_data.json').write_text(json.dumps(results[5:],indent=2))
(BASE/'discovery_data_more.json').write_text('[]')
print('Refreshed',len(results),'primary sources; rerun parsing and review scripts.')
