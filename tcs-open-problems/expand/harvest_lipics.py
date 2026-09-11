"""Collect publisher metadata and openly available LIPIcs proceedings.

Discovery and extraction only. This script never promotes a passage to the catalog.
"""
from pathlib import Path
import concurrent.futures as cf
import hashlib, json, re, subprocess, sys, time
import requests
from bs4 import BeautifulSoup

ROOT = Path(__file__).resolve().parent
CACHE = ROOT / 'cache'
PAPERS = ROOT / 'papers'
for p in (CACHE, PAPERS): p.mkdir(parents=True, exist_ok=True)
BASE = 'https://drops.dagstuhl.de'
VENUES = set('APPROX/RANDOM CONCUR WABI TQC ESA DNA MFCS ITC TYPES CCC STACS ICALP ITCS CSL FSCD SAT ICDT CPM SoCG SOCG IPEC DISC ISAAC FSTTCS SWAT WADS GD SEA SAND FUN CVIT CALCO TIME OPODIS FCT'.split())
MIN_YEAR = 2018

def get(url):
    key = hashlib.sha256(url.encode()).hexdigest()[:24]
    path = CACHE / (key + '.html')
    if path.exists(): return path.read_text()
    for attempt in range(3):
        try:
            r = requests.get(url, timeout=75, headers={'User-Agent':'TCS-literature-catalog/2.0 (academic open-problem indexing)'})
            r.raise_for_status();break
        except requests.RequestException:
            if attempt==2:raise
            time.sleep(1+attempt)
    r.encoding='utf-8'; path.write_text(r.text)
    return r.text

def discover(page):
    url = BASE + '/entities/series/LIPIcs' + (f'?page={page}' if page>1 else '')
    s=BeautifulSoup(get(url),'html.parser'); out=[]
    for a in s.select('a[href]'):
        if '/entities/volume/LIPIcs-volume-' not in a['href']: continue
        title=a.get_text(' ',strip=True)
        y=re.search(r'20\d\d',title)
        if not y: continue
        year=int(y.group())
        if not MIN_YEAR<=year<=2026: continue
        venue=next((v for v in sorted(VENUES,key=len,reverse=True) if re.search(r'\b'+re.escape(v)+r'\b',title)),None)
        if venue: out.append(dict(volume_url=a['href'],volume_title=title,year=year,venue=venue))
    return out

def metadata(v):
    s=BeautifulSoup(get(v['volume_url']),'html.parser'); papers=[]; complete=None
    for card in s.select('.entity-list-item.document'):
        title=card.select_one('.card-title'); pdf=card.select_one('a[title="View PDF"]')
        category=card.select_one('.category'); category=category.get_text(' ',strip=True) if category else ''
        if not title or not pdf: continue
        doi=card.get('data-permanent-id','').removeprefix('document/')
        row=dict(**v,doi=doi,title=title.get_text(' ',strip=True),pdf_url=pdf['href'],source_url='https://doi.org/'+doi,category=category)
        if category=='Complete Volume': complete=row
        elif category!='Front Matter':
            row['authors']=[n.get('data-value') for n in card.select('[data-key="dagstuhl.contributor.author"]')]
            row['classifications']=[n.get('data-value') for n in card.select('[data-key="dagstuhl.subject.classification"]')]
            a=card.select_one('.abstract');row['abstract']=a.get_text(' ',strip=True) if a else ''
            papers.append(row)
    return dict(**v,complete=complete,papers=papers)

def download(v):
    if not v['complete']: return dict(volume=v['volume_url'],error='No complete volume')
    url=v['complete']['pdf_url']; key=hashlib.sha256(url.encode()).hexdigest()[:24]
    pdf=CACHE/(key+'.pdf'); txt=CACHE/(key+'.txt')
    try:
        if not pdf.exists():
            r=requests.get(url,timeout=180,headers={'User-Agent':'TCS-literature-catalog/2.0'})
            r.raise_for_status()
            if not r.content.startswith(b'%PDF'): raise ValueError('Not a PDF')
            temp=pdf.with_suffix('.part');temp.write_bytes(r.content);temp.replace(pdf)
        if not txt.exists():subprocess.run(['pdftotext','-layout',str(pdf),str(txt)],check=True,timeout=180,stderr=subprocess.DEVNULL)
        pages=txt.read_text().split('\f'); bydoi={p['doi']:p for p in v['papers']}; groups={}; current=None
        for page_num,page in enumerate(pages,1):
            m=re.search(r'Digital Object Identifier\s+(10\.4230/LIPIcs\.[A-Za-z0-9./-]+)',page)
            if m:
                current=m.group(1).rstrip('.')
                if current in bydoi: groups[current]=dict(**bydoi[current],volume_pdf=url,volume_pdf_start_page=page_num,pages=[])
            if current in groups:groups[current]['pages'].append(page)
        for doi,p in groups.items():
            (PAPERS/(doi.replace('/','_')+'.json')).write_text(json.dumps(p,ensure_ascii=False))
        return dict(volume=v['volume_title'],found=len(groups),expected=len(bydoi),pages=len(pages),pdf_bytes=pdf.stat().st_size)
    except Exception as e:return dict(volume=v['volume_title'],error=str(e))

def main():
    mode=sys.argv[1] if len(sys.argv)>1 else 'all'
    if mode in ('all','discover'):
        volumes=[]
        with cf.ThreadPoolExecutor(6) as pool:
            for items in pool.map(discover,range(1,26)):volumes+=items
        volumes=list({v['volume_url']:v for v in volumes}.values())
        (ROOT/'lipics_volumes.json').write_text(json.dumps(volumes,ensure_ascii=False,indent=2))
        print('Discovered',len(volumes),'volumes',flush=True)
        meta=[]
        with cf.ThreadPoolExecutor(6) as pool:
            for v in pool.map(metadata,volumes):
                meta.append(v)
                if len(meta)%20==0:print('Metadata',len(meta),flush=True)
        (ROOT/'lipics_metadata.json').write_text(json.dumps(meta,ensure_ascii=False))
        print('Metadata complete',len(meta),'volumes',sum(len(v['papers']) for v in meta),'papers',flush=True)
    if mode in ('all','download'):
        meta=json.loads((ROOT/'lipics_metadata.json').read_text()); results=[]
        with cf.ThreadPoolExecutor(4) as pool:
            for result in pool.map(download,meta):
                results.append(result);print(json.dumps(result,ensure_ascii=False),flush=True)
                (ROOT/'lipics_download_audit.json').write_text(json.dumps(results,ensure_ascii=False,indent=2))

if __name__=='__main__':main()
