"""Read-only helpers for the related-problem editorial review."""
import json, pathlib, sys, re
ROOT=pathlib.Path(__file__).resolve().parents[2]
DELETED=json.loads((ROOT/'data/deleted_records.json').read_text())
CARDS={c['id']:c for p in sorted((ROOT/'data/cards').glob('*.json')) if (c:=json.loads(p.read_text()))['id'] not in DELETED and not c.get('scope_exclusion') and c['status'] not in ('resolved','excluded')}
def normid(s):return f'TCS-{int(s):04d}' if s.isdigit() else s
def compact(c):
    title=re.sub(r'\s+',' ',c['title'])
    
    source=c.get('source_formulation',{}).get('text','')
    extra=(' | '+re.sub(r'\s+',' ',source)) if source and source!=title else ''
    return f"{c['id'][4:]} {title}{extra}"
if __name__=='__main__':
    op=sys.argv[1]
    if op=='areas':
        for a in dict.fromkeys(c['area'] for c in CARDS.values()):print(a)
    elif op=='list':
        for a in sys.argv[2:]:
            cs=[c for c in CARDS.values() if a.lower() in c['area'].lower()]
            print('\nAREA',a,'COUNT',len(cs))
            for c in cs:print(compact(c))
    elif op=='read':
        for id in sys.argv[2:]:
            c=CARDS.get(normid(id))
            if not c:print(id,'INACTIVE');continue
            print('\n'+compact(c))
            for k in ('formal','definitions','answer_criterion','working_summary'):
                if c.get(k):print(k+':',c[k])
    elif op=='search':
        pat=re.compile('|'.join(sys.argv[2:]),re.I)
        for c in CARDS.values():
            if pat.search(' '.join(str(c.get(k,'')) for k in ('title','formal'))):print(compact(c))
    elif op=='legacy':
        for c in CARDS.values():
            ts=[r for r in c.get('related',[]) if isinstance(r,str)]+c.get('related_catalogue_ids',[])+[r['id'] for r in c.get('problem_relations',[])]
            for t in ts:print(compact(c),'→',compact(CARDS[t]) if t in CARDS else t+' INACTIVE')
