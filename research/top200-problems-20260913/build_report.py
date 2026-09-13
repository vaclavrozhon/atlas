"""Resolve the hand-reviewed 200-person assignment list against active cards."""
import collections
import csv
import hashlib
import json
from pathlib import Path

ROOT=Path(__file__).resolve().parents[2]
HERE=Path(__file__).resolve().parent
DATE='2026-09-13'
people=json.loads((ROOT/'research/tcs-top200-20260913/top200.json').read_text())
baseline=set(json.loads((HERE/'baseline-ids.json').read_text()))
cards={p.stem:json.loads(p.read_text()) for p in (ROOT/'data/cards').glob('*.json')}
new={c['researcher_import']['slug']:id for id,c in cards.items()
     if c.get('researcher_import',{}).get('batch')=='top200-problems-20260913'}
rows=[[s.strip() for s in line.split('|')]
      for line in (HERE/'assignments.txt').read_text().splitlines() if line.strip()]
assert len(people)==len(rows)==200
assert [int(r[0]) for r in rows]==list(range(1,201))

records=[]
for person,row in zip(people,rows):
    assert person['rank']==int(row[0])
    problems=[]
    for slot,index in [(1,1),(2,3)]:
        token=row[index]
        id='TCS-'+token.zfill(4) if token.isdigit() else new[token]
        card=cards[id]
        assert card['status'] not in ['resolved','excluded'],(person['name'],id)
        refs=card.get('references',[])
        assert refs and all(r.get('url','').startswith(('http://','https://')) for r in refs)
        sr=card.get('statement_review',{})
        problems.append(dict(slot=slot,id=id,title=card['title'],area=card['area'],
            action='added' if id in new.values() else 'reused',
            affinity=row[index+1],affinity_type='editorial inference, not an attributed priority',
            card_path='data/cards/'+id+'.json',status=card['status'],evidence=card['evidence'],
            formulation_status=sr.get('status','not individually completed'),
            formulation_reviewed_on=card.get('formulation_reviewed_on',sr.get('reviewed_on')),
            status_note=card.get('status_note',''),
            references=[{k:r[k] for k in ('id','title','authors','year','url','locator') if k in r} for r in refs],
            current_batch_scope='primary-source and targeted later-work check' if id in new.values()
                else 'active-card and source-locator review; existing status is carried through, not independently recertified'))
    assert problems[0]['id']!=problems[1]['id']
    records.append(dict(rank=person['rank'],researcher=person['name'],
        researcher_bibliography=person['dblp'],
        research_evidence='research/tcs-top200-20260913/top200.json',
        conference_papers_in_previous_review=person['total_2011_2025'],problems=problems))

flat=[dict(rank=r['rank'],researcher=r['researcher'],researcher_bibliography=r['researcher_bibliography'],**p)
      for r in records for p in r['problems']]
assert len(flat)==400
assert {p['id'] for p in flat if p['action']=='added'}==set(new.values())
reused={p['id'] for p in flat if p['action']=='reused'}
assert reused<=baseline
counts=dict(researchers=200,associations=400,distinct_problems=len({p['id'] for p in flat}),
    new_cards=len(new),reused_cards=len(reused),
    associations_to_new_cards=sum(p['action']=='added' for p in flat),
    associations_to_existing_cards=sum(p['action']=='reused' for p in flat),
    distinct_card_statuses=dict(collections.Counter(cards[id]['status'] for id in {p['id'] for p in flat})),
    distinct_card_evidence=dict(collections.Counter(cards[id]['evidence'] for id in {p['id'] for p in flat})))
(HERE/'assignments.json').write_text(json.dumps(dict(checked_on=DATE,scope='Researcher affinities are editorial; scientific status retains the distinctions in each canonical card.',counts=counts,researchers=records),ensure_ascii=False,indent=2)+'\n')
fields=['rank','researcher','slot','id','title','area','action','affinity','status','evidence','formulation_status','formulation_reviewed_on','current_batch_scope','researcher_bibliography','problem_sources']
with (HERE/'assignments.csv').open('w',newline='') as f:
    w=csv.DictWriter(f,fieldnames=fields);w.writeheader()
    for p in flat:
        w.writerow({k:('; '.join(r['url'] for r in p['references']) if k=='problem_sources' else p.get(k,'')) for k in fields})

overview=['# Two major problem candidates for each of the selected 200 researchers','',
    f'Review date: {DATE}. The list contains **400 researcher–problem associations**, covering **{counts["distinct_problems"]} distinct problems**. **{len(new)} new cards were added** and **{len(reused)} existing cards reused**. A shared problem has one canonical card.',
    '', 'The 200 researchers and their order come from the earlier [STOC/FOCS/SODA review](../tcs-top200-20260913/top200.md). The explanation for each association is editorial judgment about the researcher’s work, not an assertion that the researcher posed, endorsed or personally prioritizes the question.',
    '', '**Scope of status checking.** Each new card received a precise formulation, primary-source review, a targeted later-work search, and an active/retired identity comparison. Reused cards retain their existing evidence and status; this pass is not a fresh literature review of every old card. `source_open` means source-backed without exhaustive certification. `uncertain` can mean an incomplete inherited record or an unverified claimed resolution. Neither label is silently upgraded. The detailed file carries each status note and source locator.',
    '', '[400-row CSV](assignments.csv) · [Detailed explanations and sources](assignments.md) · [Machine-readable JSON](assignments.json) · [Admission and exclusion audit](admission-audit.md)',
    '', '## New cards','', '| ID | Problem |', '|---|---|']
for id in sorted(new.values()):overview.append(f'| [{id}](../../data/cards/{id}.json) | {cards[id]["title"]} |')
overview+=['','## All 200 researchers','','An asterisk marks a newly added card. Each link opens the canonical card, including its current review status.','','| Rank | Researcher | Problem 1 | Problem 2 |','|---:|---|---|---|']
for r in records:
    cells=[]
    for p in r['problems']:
        title=p['title'].replace('|',r'\|')
        cells.append(f'[{title}](../../data/cards/{p["id"]}.json)'+(' *' if p['action']=='added' else ''))
    overview.append(f'| {r["rank"]} | [{r["researcher"]}]({r["researcher_bibliography"]}) | {cells[0]} | {cells[1]} |')
(HERE/'README.md').write_text('\n'.join(overview)+'\n')

detail=['# Researcher–problem explanations and source locators','',
    'These are editorial research affinities. Status and evidence are snapshots of the canonical cards, not new certification of all reused entries. The [overview](README.md) explains the scope.','']
for r in records:
    detail += [f'## {r["rank"]}. {r["researcher"]}','',f'[Research bibliography]({r["researcher_bibliography"]}).','']
    for p in r['problems']:
        detail += [f'### {p["slot"]}. {p["title"]}','',
            f'[{p["id"]}](../../data/cards/{p["id"]}.json) · {p["action"]} · status: `{p["status"]}` · evidence: `{p["evidence"]}`.',
            '',p['affinity'],'',f'**Status scope:** {p["status_note"].rstrip()}','',
            'Sources: '+ '; '.join(f'[{ref["title"]}]({ref["url"]})' for ref in p['references'])+'.','']
(HERE/'assignments.md').write_text('\n'.join(detail))

manifest=[]
for id in sorted(new.values()):
    p=ROOT/'data/cards'/f'{id}.json'
    manifest.append(dict(id=id,key=cards[id]['key'],sha256=hashlib.sha256(p.read_bytes()).hexdigest(),
                         researchers=[r['researcher'] for r in records if any(p['id']==id for p in r['problems'])]))
(HERE/'import-audit.json').write_text(json.dumps(dict(date=DATE,counts=counts,added=manifest,
    validation='make publish, make check, and node tests/math.cjs; exact execution outcomes recorded in admission-audit.md'),ensure_ascii=False,indent=2)+'\n')
print(json.dumps(counts,indent=2))
