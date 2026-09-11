import concurrent.futures as cf
import hashlib, json, re, time
from pathlib import Path
from urllib.parse import urljoin
import requests
from bs4 import BeautifulSoup

ROOT = Path(__file__).resolve().parent
CACHE = ROOT / 'cache'
CACHE.mkdir(exist_ok=True)

def fetch(url):
    key = hashlib.sha256(url.encode()).hexdigest()[:20]
    path = CACHE / (key + '.json')
    if path.exists():
        old = json.loads(path.read_text())
        if old.get('code',0) != 0:
            return old
    try:
        r = requests.get(url, timeout=40, headers={'User-Agent':'TCS-research-catalog/1.0'})
        if 'text/' in r.headers.get('Content-Type','') or not r.content.startswith(b'%PDF'):
            r.encoding = 'utf-8'
            result = dict(url=url, final_url=r.url, code=r.status_code, html=r.text)
        else:
            pdf = CACHE / (key+'.pdf'); pdf.write_bytes(r.content)
            import subprocess
            subprocess.run(['pdftotext','-layout',str(pdf),str(CACHE/(key+'.txt'))],check=True)
            result = dict(url=url, final_url=r.url, code=r.status_code, text=(CACHE/(key+'.txt')).read_text(), pdf=str(pdf))
    except Exception as e:
        result = dict(url=url, code=0, error=str(e))
    path.write_text(json.dumps(result,ensure_ascii=False))
    return result

def soup(result):
    return BeautifulSoup(result.get('html',''),'html.parser')

def clean(s):
    return re.sub(r'\s+',' ',s).strip()

def txt(node):
    return clean(node.get_text(' ',strip=True)) if node else ''

def main():
    candidates=[]
    def add(collection,title,url,locator='',year='',**kw):
        candidates.append(dict(collection=collection,title=title,source_url=url,locator=locator,source_year=year,**kw))
    for name,base,pattern in [
        ('automata','https://automata.exchange/',r'^\d\d\.\d'),
        ('sublinear','https://sublinear.info/',r'^Problem \d+:'),
        ('topp','https://topp.openproblem.net/',r'\(Problem\s*\d+\)')]:
        s=BeautifulSoup((CACHE/(name+'.html')).read_text(),'html.parser')
        for a in s.select('a[href]'):
            title=txt(a)
            if re.search(pattern,title):
                url=urljoin(base,a['href'])
                if any(x['source_url']==url for x in candidates):continue
                year='20'+title[:2] if name=='automata' else ''
                add(name,title,url,year=year)
    s=BeautifulSoup((CACHE/'rta.html').read_text(),'html.parser')
    for tr in s.select('tr'):
        cells=tr.select('td');a=tr.find('a')
        if a and len(cells)>1:
            add('rta',txt(cells[1]),urljoin('https://www.cs.tau.ac.il/~nachum/rtaloop/problems/',a['href']),locator='Problem '+txt(a))
    # Read individual records, not just the lists, to capture status updates.
    def enrich(x):
        r=fetch(x['source_url']);s=soup(r)
        body=s.select_one('.post-body') or s.select_one('#mw-content-text') or s.body or s
        for el in body.select('script,style,nav,footer'):el.decompose()
        x['text']=txt(body);x['html']=str(body);x['http_status']=r['code']
        return x
    with cf.ThreadPoolExecutor(12) as pool:
        out=list(pool.map(enrich,candidates))
    (ROOT/'harvested.json').write_text(json.dumps(out,ensure_ascii=False,indent=2))
    print('harvested',len(out),flush=True)

if __name__=='__main__':main()
