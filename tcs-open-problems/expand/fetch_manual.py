from pathlib import Path
import concurrent.futures as cf
import json,sys
ROOT=Path(__file__).resolve().parent
sys.path.insert(0,str(ROOT.parent))
from collect import fetch,soup,txt

def one(s):
    r=fetch(s['pdf_url']); out=dict(s,http_status=r.get('code'))
    if 'text' in r:
        out['pages']=r['text'].split('\f');out['cached_pdf']=r['pdf']
    else:out['error']=r.get('error','No PDF text')
    (ROOT/'manual'/f"{s['key']}.json").write_text(json.dumps(out,ensure_ascii=False))
    return {k:v for k,v in out.items() if k not in ['pages'] }|{'pages':len(out.get('pages',[]))}

if __name__=='__main__':
    (ROOT/'manual').mkdir(exist_ok=True)
    ss=json.loads((ROOT/'manual_sources.json').read_text())
    with cf.ThreadPoolExecutor(5) as pool:
        for r in pool.map(one,ss):print(json.dumps(r,ensure_ascii=False),flush=True)
