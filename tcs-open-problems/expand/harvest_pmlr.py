from pathlib import Path
import concurrent.futures as cf
import json,re,sys
ROOT=Path(__file__).resolve().parent
sys.path.insert(0,str(ROOT.parent))
from collect import fetch,soup,txt,urljoin

def volume(v):
    s=soup(fetch(v['volume_url']));out=[]
    for p in s.select('.paper'):
        title=txt(p.select_one('.title'))
        if re.search(r'preface|foreword|editorial',title,re.I):continue
        links=p.select('a[href]');pdf=next((a['href'] for a in links if '.pdf' in a['href']),None);url=next((a['href'] for a in links if '.html' in a['href']),None)
        if not pdf or not url:continue
        slug=url.rsplit('/',1)[-1].removesuffix('.html')
        out.append(dict(**v,doi='PMLR.'+v['volume']+'.'+slug,title=title,pdf_url=pdf,source_url=url,authors=txt(p.select_one('.authors')),classifications=['Learning theory']))
    return out

def paper(p):
    file=ROOT/'papers'/(p['doi']+'.json')
    if file.exists():return {'doi':p['doi'],'cached':True}
    r=fetch(p['pdf_url'])
    if not r.get('text'):return {'doi':p['doi'],'error':r.get('code')}
    row=dict(**p,pages=r['text'].split('\f'))
    file.write_text(json.dumps(row,ensure_ascii=False))
    return {'doi':p['doi'],'pages':len(row['pages'])}

def main():
    s=soup(fetch('https://proceedings.mlr.press/'));vs=[]
    for li in s.select('.proceedings-list li'):
        text=txt(li);y=re.search(r'20\d\d',text);v=re.search(r'\b(COLT|ALT)\b',text)
        if not y or not v or int(y[0])<2018:continue
        a=li.find('a',href=True)
        if a:vs.append(dict(volume_url=urljoin('https://proceedings.mlr.press/',a['href'])+'/',volume=a['href'],volume_title=text,year=int(y[0]),venue=v[0]))
    out=[]
    with cf.ThreadPoolExecutor(4) as pool:
        for ps in pool.map(volume,vs):out+=ps
    (ROOT/'pmlr_metadata.json').write_text(json.dumps(out,ensure_ascii=False,indent=2))
    print('Volumes',len(vs),'papers',len(out),flush=True)
    results=[]
    with cf.ThreadPoolExecutor(6) as pool:
        for i,r in enumerate(pool.map(paper,out),1):
            results.append(r)
            if i%100==0:print('Fetched',i,'errors',sum('error' in x for x in results),flush=True)
    (ROOT/'pmlr_download_audit.json').write_text(json.dumps(results,ensure_ascii=False))
    print('Finished',len(results),flush=True)

if __name__=='__main__':main()
