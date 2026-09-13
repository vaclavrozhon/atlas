"""Save primary-source text used in the individual import review."""
import concurrent.futures
import json
import re
import subprocess
import tempfile
from pathlib import Path
import requests

BASE = Path(__file__).resolve().parent
rows = json.loads((BASE / 'matches.json').read_text())
existing = dict(line.split() for line in (BASE / 'existing-map.txt').read_text().splitlines())
extra = {'24A', '31B', '32A', '62B', '66A', '70B', '80A', '85B', '99A'}
(BASE / 'sources').mkdir(exist_ok=True)

def fetch(row):
    key, url = row['candidate'], row['source']
    if 'arxiv.org/abs/' in url:
        url = url.replace('/abs/', '/pdf/')
    elif re.search(r'eccc.*report/\d+/\d+/$', url):
        url += 'download/'
    if not (url.endswith('.pdf') or '/pdf/' in url or '/download/' in url):
        return {'candidate': key, 'url': url, 'status': 'web_review'}
    try:
        r = requests.get(url, timeout=40)
        r.raise_for_status()
        if not r.content.startswith(b'%PDF'):
            return {'candidate': key, 'url': url, 'status': 'not_pdf'}
        with tempfile.TemporaryDirectory() as folder:
            pdf = Path(folder) / 'source.pdf'
            txt = Path(folder) / 'source.txt'
            pdf.write_bytes(r.content)
            subprocess.run(['pdftotext', '-layout', str(pdf), str(txt)], check=True, capture_output=True)
            (BASE / 'sources' / (key + '.txt')).write_bytes(txt.read_bytes())
        return {'candidate': key, 'url': url, 'status': 'saved'}
    except Exception as exc:
        return {'candidate': key, 'url': url, 'status': 'failed', 'error': str(exc)}

if __name__ == '__main__':
    work = [r for r in rows if r['candidate'] not in existing or r['candidate'] in extra]
    with concurrent.futures.ThreadPoolExecutor(max_workers=8) as pool:
        results = list(pool.map(fetch, work))
    (BASE / 'source-fetch.json').write_text(json.dumps(results, indent=2) + '\n')
    from collections import Counter
    print(dict(Counter(r['status'] for r in results)))
