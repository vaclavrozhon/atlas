"""Source evidence for questions; pending candidates are not certified open problems."""
import collections, hashlib, json, re, subprocess, sys, unicodedata
from pathlib import Path
BASE=Path(__file__).resolve().parent
sys.path.insert(0,str(BASE.parent/'expand'))
from extract_candidates import extract,blocks,normalize,EXPLICIT,NAMED,RESOLVED
from select_expansion import choose,norm

def fix_columns(r):
    if r['venue'] not in ['FOCS','Quantum'] or r.get('reading_order_fixed'):return r
    cp=BASE/'cache'/(hashlib.sha256(r['pdf_url'].encode()).hexdigest()[:24]+'.pdf')
    if not cp.exists():return r
    run=subprocess.run(['pdftotext','-','-'],input=cp.read_bytes(),stdout=subprocess.PIPE,stderr=subprocess.PIPE,timeout=90)
    if run.returncode==0:
        r['pages']=run.stdout.decode('utf-8',errors='replace').split('\f')
        if r['pages'] and not r['pages'][-1].strip():r['pages'].pop()
        r['reading_order_fixed']=True
    return r

def enhanced_extract(r):
    found=extract(r);seen={norm(x['statement']) for x in found};bs=blocks(r['pages'])
    end=next((i for i,b in enumerate(bs) if re.match(r'^(?:\d+\s+)?References\b',b['text']) and i>5),len(bs))
    for i,b in enumerate(bs[:end]):
        t=b['text']
        if not EXPLICIT.search(t):continue
        # Require a complete mathematical question, not a reference to a question.
        if not re.search(r'\b(?:whether|if|how|can|does|exist|conjecture that)\b',t,re.I):continue
        if not 12<=len(t.split())<=240:continue
        if re.search(r'\b(?:we (?:resolve|settle|answer|prove|disprove)|has been (?:resolved|settled|proved)|we show that)\b',t,re.I):continue
        after=' '.join(x['text'] for x in bs[i+1:i+3])
        if re.search(r'\b(?:we (?:resolve|settle|answer|disprove)|answer(?:s)? (?:this|the) (?:question|problem))\b',after,re.I):continue
        key=norm(t)
        if key in seen:continue
        seen.add(key)
        found.append(dict(candidate_id=hashlib.sha256((r['doi']+'|'+key).encode()).hexdigest()[:16],doi=r['doi'],paper_title=r['title'],authors=r.get('authors',[]),year=r['year'],venue=r['venue'],classifications=r.get('classifications',[]),source_url=r['source_url'],pdf_url=r['pdf_url']+f'#page={b["page"]}',source_locator=f'Explicit open question on PDF page {b["page"]}',page=b['page'],extraction_kind='explicit_unresolved_passage',statement=t,context=' '.join(x['text'] for x in bs[max(0,i-1):min(end,i+3)]),flags=['introductory_claim_requires_review'] if i<.5*end else [],source_file=r.get('source_file','')))
    return found

def main():
    out=[];newpapers=list((BASE/'papers').glob('*.json'))
    cache=BASE/'research/extractions';cache.mkdir(exist_ok=True)
    fs=list((BASE.parent/'expand/papers').glob('*.json'))+newpapers
    for i,f in enumerate(fs,1):
        p=cache/f.name
        if p.exists():out+=json.loads(p.read_text());continue
        try:
            r=json.loads(f.read_text());r['source_file']=str(f);r=fix_columns(r)
            items=enhanced_extract(r)
            # Keep paper reading-order fixes in this research cache only.
            if r.get('reading_order_fixed'):(BASE/'research'/('fixed-'+f.name)).write_text(json.dumps(r,ensure_ascii=False))
            p.write_text(json.dumps(items,ensure_ascii=False));out+=items
        except Exception as e:print('failed',f.name,str(e)[:120],flush=True)
        if i%500==0:print('extracted',i,'/',len(fs),len(out),'candidates',flush=True)
    old=json.loads((BASE.parent/'output/catalog.json').read_text());ids={x.get('candidate_id') for x in old};selected=[]
    for x in out:
        if x['candidate_id'] in ids:continue
        y=choose(x)
        if y:selected.append(y)
    (BASE/'research/all_candidates.json').write_text(json.dumps(out,ensure_ascii=False,indent=2))
    (BASE/'research/screened_candidates.json').write_text(json.dumps(selected,ensure_ascii=False,indent=2))
    print('all',len(out),'new screened',len(selected),'venues',collections.Counter(x['venue'] for x in selected),flush=True)
if __name__=='__main__':main()
