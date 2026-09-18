"""Consolidate the sublinear randomized k-server milestone into its quantitative card."""
import collections,hashlib,json,sys
from datetime import datetime,timezone
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT/'research/card-completion-20260913'))
from complete_review import DATE,CRITERIA
from review_queue import read_claims,read_queue,locked,require_claim,finish_claim
from catalog_exports import atomic
from archive_cards import change_activity
from card_schema import reader_record
from publish import validate_record
target='TCS-7317';duplicate='TCS-4983';claim=read_claims(ROOT)[duplicate]
target_hash='24b358599a19bbd0a14fecb0bc1aff15dfaaa5a66b07a73ba22339ebf15f61f9'
reason=('Consolidated the weaker o(k) randomized k-server milestone into the completed full-asymptotic target TCS-7317. '
 'Both use arbitrary finite metrics, an oblivious request sequence, expected movement cost and a sequence-independent additive term. '
 'This is the announced editorial default after an unanswered optional merge question, not a user-confirmed choice. '
 'Archival removes overlap and does not assert that sublinear competitiveness is known.')
checked=['Read the official ICALP 2026.65 PDF model and competitive-cost conventions on pp.65:2–3 and its explicit arbitrary-metric o(k) question in §1.1 p.65:4.',
 'Compared the entire completed TCS-7317 quantifiers and definitions with this milestone, including unbounded metric cardinality and no computation restriction.',
 'The mathematical relation is equivalence of existence of an o(k) guarantee with R_rand(k)/k tending to zero; infimum nonattainment is handled by adding fixed positive slack.']
def append_text_or_list(mapping,key,value):
 old=mapping.get(key,[])
 mapping[key]=old+[value] if isinstance(old,list) else old+' '+value
with locked(ROOT):
 require_claim(ROOT,duplicate,claim['token']);assert target not in read_claims(ROOT)
 p=ROOT/'data/cards'/f'{target}.json';before=p.read_bytes();assert hashlib.sha256(before).hexdigest()==target_hash
 original=(ROOT/'data/cards'/f'{duplicate}.json').read_bytes();assert hashlib.sha256(original).hexdigest()==claim['input_sha256']
 q=read_queue(ROOT);row=next(r for r in q['records'] if r['id']==target);assert row['state']=='completed' and row['output_sha256']==target_hash
 c=json.loads(before)
 c.setdefault('source_consolidations',[]).append(dict(from_id=duplicate,reviewed_on=DATE,note=reason))
 c['related_problem_ids']=[i for i in c.get('related_problem_ids',[]) if i!=duplicate]
 for reference in c['references']:
  if reference['id']=='primary':reference['locator']='ICALP 2026, article 65, published 1 July; model and competitive-cost definitions pp.65:2–3; §1.1 explicit arbitrary-metric o(k) question p.65:4; §1.4 Theorem 1 and Corollaries 2–3. Preprint arXiv:2605.01497v1, 2 May.'
 c.setdefault('context_blocks',[]).append(dict(text=r'''The weaker milestone formerly indexed as TCS-4983 asks whether there is a function \(r(k)\ge1\) with \(r(k)/k\to0\) such that, for every finite metric and initial placement, some randomized online strategy has competitive ratio at most \(r(k)\), allowing a fixed sequence-independent additive cost. In the present model this is equivalent to \(R_{\mathrm{rand}}(k)/k\to0\). If the latter holds, the positive slack \(r(k)=R_{\mathrm{rand}}(k)+1\) accommodates possible nonattainment of the defining infimum. Thus a determination of this card's asymptotic scale also captures the sublinear milestone. The same ICALP 2026 source explicitly poses it; its polynomial-time results do not impose an additional running-time requirement on that open question.''',citation='primary'))
 append_text_or_list(c['statement_review'],'notes',reason)
 append_text_or_list(c['quality_review'],'changes',reason)
 c['quality_review']['checked_sources'].extend(checked)
 c['updated_at']=datetime.now(timezone.utc).isoformat(timespec='seconds')
 validate_record(reader_record(c,CRITERIA),p,CRITERIA)
 out=json.dumps(c,ensure_ascii=False,indent=2)+'\n';row['output_sha256']=hashlib.sha256(out.encode()).hexdigest()
 atomic(p,out);atomic(ROOT/'research/card-completion-20260913/queue.json',json.dumps(q,ensure_ascii=False,indent=2)+'\n')
 with (ROOT/'research/card-completion-20260913/reviews.jsonl').open('a') as f:f.write(json.dumps(dict(id=target,date=DATE,outcome='source_consolidation_amendment',changes=[reason],sources_checked=checked,input_sha256=target_hash,output_sha256=row['output_sha256']),ensure_ascii=False)+'\n')
print(change_activity([duplicate],reason=reason))
with locked(ROOT):
 p=ROOT/'data/archive/cards'/f'{duplicate}.json';assert p.read_bytes()==original
 q=read_queue(ROOT);row=next(r for r in q['records'] if r['id']==duplicate);assert row['state']=='pending'
 row.update(state='completed',completed_on=DATE,review_input_sha256=claim['input_sha256'],output_sha256=hashlib.sha256(original).hexdigest(),output_path=str(p.relative_to(ROOT)),consolidated_into=target)
 q['counts']=dict(total=len(q['records']),**dict(collections.Counter(r['state'] for r in q['records'])))
 atomic(ROOT/'research/card-completion-20260913/queue.json',json.dumps(q,ensure_ascii=False,indent=2)+'\n')
 with (ROOT/'research/card-completion-20260913/reviews.jsonl').open('a') as f:f.write(json.dumps(dict(id=duplicate,date=DATE,outcome='merged_after_individual_review',consolidated_into=target,changes=[reason],sources_checked=checked,input_sha256=claim['input_sha256'],output_path=str(p.relative_to(ROOT))),ensure_ascii=False)+'\n')
 finish_claim(ROOT,duplicate,claim['token'],q);print(duplicate,q['counts'])
