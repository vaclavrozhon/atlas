"""Download the independent source library; never imports or writes atlas data."""
import concurrent.futures as cf
import datetime
import hashlib
import json
from pathlib import Path
import subprocess
import sys
import requests

ROOT = Path(__file__).resolve().parents[1]

def fetch(source):
    key = source['id']
    path = ROOT / 'pdf' / (key + '.pdf')
    audit = dict(id=key, requested_url=source['pdf_url'])
    try:
        if not path.exists():
            r = requests.get(source['pdf_url'], timeout=(20, 100), headers={'User-Agent': 'TCS-Source-Library/1.0 (personal scholarly reading)'})
            audit.update(http_status=r.status_code, final_url=r.url)
            r.raise_for_status()
            if not r.content[:1024].lstrip().startswith(b'%PDF-'):
                raise ValueError('Response is not a PDF')
            tmp = path.with_suffix('.part')
            tmp.write_bytes(r.content)
            tmp.replace(path)
        else:
            prior = ROOT / 'audit' / (key + '.json')
            if prior.exists(): audit.update(json.loads(prior.read_text()))
        data = path.read_bytes()
        info = subprocess.run(['pdfinfo', str(path)], capture_output=True, text=True, check=True).stdout
        (ROOT / 'audit' / (key + '.pdfinfo.txt')).write_text(info)
        subprocess.run(['pdftotext', '-layout', str(path), str(ROOT / 'text' / (key + '.txt'))], check=True, capture_output=True)
        pages = (ROOT / 'text' / (key + '.txt')).read_text().split('\f')
        if not pages[-1].strip(): pages.pop()
        audit.update(status='downloaded', bytes=len(data), sha256=hashlib.sha256(data).hexdigest(), pages=len(pages), retrieved_at=audit.get('retrieved_at',datetime.datetime.now(datetime.timezone.utc).isoformat()), extracted_characters=sum(map(len,pages)))
    except Exception as e:
        audit.update(status='failed', error=str(e))
    (ROOT / 'audit' / (key + '.json')).write_text(json.dumps(audit, ensure_ascii=False, indent=2))
    return audit

if __name__ == '__main__':
    sources = json.loads((ROOT / 'sources.json').read_text())
    if len(sys.argv)>1: sources=[s for s in sources if s['id'] in sys.argv[1:]]
    with cf.ThreadPoolExecutor(max_workers=5) as pool:
        for result in pool.map(fetch, sources):
            print(json.dumps(result, ensure_ascii=False), flush=True)
