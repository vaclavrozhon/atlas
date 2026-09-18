"""Confirm approved mergers on the retained cards, preserving raw archive copies."""
import fcntl,hashlib,json,sys
from datetime import datetime,timezone
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT/'research/card-completion-20260913'))
from complete_review import CRITERIA,reader_record,validate_record,atomic
with (ROOT/'.publish.lock').open('a') as lock:
 fcntl.flock(lock,fcntl.LOCK_EX)
 qp=ROOT/'research/card-completion-20260913/queue.json';q=json.loads(qp.read_text());events=[]
 for source,target in [('TCS-4983','TCS-7317'),('TCS-2427','TCS-6567')]:
  p=ROOT/'data/cards'/f'{target}.json';raw=p.read_bytes();c=json.loads(raw)
  entry=next(x for x in c['source_consolidations'] if x['from_id']==source)
  if entry.get('user_confirmed_on')=='2026-09-18':continue
  before=hashlib.sha256(raw).hexdigest();row=next((x for x in q['records'] if x['id']==target),None)
  if row:assert row['output_sha256']==before and row['state']=='completed'
  note=f'On 18 September 2026 the user explicitly confirmed consolidation of {source} into {target} and archival of the overlapping source record. The previous editorial default is now user-confirmed; this does not assert resolution of the retained open target.'
  entry['user_confirmed_on']='2026-09-18';entry['note']+=' '+note
  for section,key in [('statement_review','notes'),('quality_review','changes')]:
   value=c[section][key]
   c[section][key]=value+[note] if isinstance(value,list) else value+' '+note
  c['updated_at']=datetime.now(timezone.utc).isoformat(timespec='seconds')
  validate_record(reader_record(c,CRITERIA),p,CRITERIA)
  output=json.dumps(c,ensure_ascii=False,indent=2)+'\n';after=hashlib.sha256(output.encode()).hexdigest();atomic(p,output)
  if row:row['output_sha256']=after
  events.append(dict(id=target,from_id=source,date='2026-09-18',outcome='user_merge_confirmation',changes=[note],input_sha256=before,output_sha256=after,output_path=str(p.relative_to(ROOT))))
 atomic(qp,json.dumps(q,ensure_ascii=False,indent=2)+'\n')
 with (qp.parent/'reviews.jsonl').open('a') as f:
  for event in events:f.write(json.dumps(event,ensure_ascii=False)+'\n')
 print(len(events),'merger confirmations; archived raw cards and completion counts unchanged.')
