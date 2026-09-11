from collect import *

THEORY = re.compile(r'complexity|algorithm|computab|computation|geometry|automata|logic|graph|combinatori|crypto|quantum|formal|verification|semantics|proof|game theory|game theor|mechanism|social choice|constraint|scheduling|data structure|neural language|foundations|optimization|optimisation|distributed computing|distributed systems|discrete|random|learning theory|information theory|coding|compression|string',re.I)

def reports():
    out=[]
    for f in sorted(CACHE.glob('*.json')):
        if f.stat().st_size>20_000_000:continue
        try:r=json.loads(f.read_text())
        except:continue
        if not isinstance(r,dict) or 'drops.dagstuhl.de/storage/04dagstuhl-reports/' not in r.get('url','') or 'text' not in r:continue
        t=r['text']
        for match in re.finditer(r'(?m)^\f?Report from Dagstuhl (?:Seminar|Perspectives Workshop) (\d+)',t):
            end=re.search(r'(?m)^\f?Report from Dagstuhl (?:Seminar|Perspectives Workshop) \d+',t[match.end():])
            body=t[match.start():match.end()+end.start() if end else len(t)]
            lines=body.splitlines();title=[]
            for l in lines[2:]:
                if re.search(r'[∗†]|\d\s*,',l):break
                if l.strip():title.append(l.strip())
                if len(title)>=4:break
            title=' '.join(title)
            doi=re.search(r'10\.4230/DagRep\.\d+\.\d+\.\d+',body[:18000])
            if not doi:continue
            title=re.sub(r'\s+\d+$','',title).removesuffix(' Edited by')
            if not THEORY.search(title):continue
            out.append(dict(seminar=match.group(1),title=title,doi=doi.group(0),source_url='https://doi.org/'+doi.group(0),issue_url=r['url'],source_year='20'+match.group(1)[:2],text=body,offset=match.start(),pdf_page=t[:match.start()].count('\f')+1))
    return out

def extract_sections(report):
    t=report['text'];found=[]
    # Main section labels are used in these reports for collections of questions.
    headers=list(re.finditer(r'(?m)^[ \t]*([1-9])[ \t]+([^\n]{4,90})[ \t]*$',t))
    for h in headers:
        title=h.group(2).strip()
        if not re.match(r'(?:Overview of |List of |Collection of |Summary of |Selected )?(?:Open [Pp]roblems|Open [Qq]uestions|Problem [Ss]essions?)(?:[ :].*)?$',title,re.I) or re.search(r'\.\s*\.|\d\s*$',title):continue
        section_no=h.group(1)
        end=re.search(r'(?m)^\s*'+str(int(section_no)+1)+r'\s+\w|^\s*Participants\s*$',t[h.end():])
        section=t[h.end():h.end()+end.start() if end else len(t)]
        subs=list(re.finditer(r'(?m)^\s*('+section_no+r'\.\d+)\s+([^\n]+)',section))
        if not subs:
            found.append(dict(**{k:v for k,v in report.items() if k not in ['text','pdf_page']},locator=section_no,section_title=title,text=section,pdf_page=report['pdf_page']+t[:h.start()].count('\f')))
            continue
        for i,sub in enumerate(subs):
            block=section[sub.end():subs[i+1].start() if i+1<len(subs) else len(section)]
            stitle=sub.group(2).strip()
            # Add wrapped title lines before the author line.
            first=[l for l in block.splitlines() if l.strip()]
            if first and first[0].strip() and not re.search(r'\(|License|©|University|Universit|Institute',first[0]):
                stitle+=' '+first[0].strip()
            found.append(dict(**{k:v for k,v in report.items() if k not in ['text','pdf_page']},locator=sub.group(1),section_title=stitle,text=block,pdf_page=report['pdf_page']+t[:h.end()+sub.start()].count('\f')))
    return found

if __name__=='__main__':
    rs=reports();sections=[s for r in rs for s in extract_sections(r)]
    (ROOT/'dagstuhl_reports.json').write_text(json.dumps(rs,ensure_ascii=False,indent=2))
    (ROOT/'dagstuhl_sections.json').write_text(json.dumps(sections,ensure_ascii=False,indent=2))
    print('Reports',len(rs),'sections',len(sections))
    for r in rs:
        ss=[s for s in sections if s['seminar']==r['seminar']]
        if ss:print(r['seminar'],len(ss),r['title'])
