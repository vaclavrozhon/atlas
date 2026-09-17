"""Consolidate two equivalent kernel-existence formulations under atlas policy."""
import collections
import hashlib
import json
import sys
from datetime import datetime,timezone
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT/'research/card-completion-20260913'))
from complete_review import DATE,ref,CRITERIA
from review_queue import read_claims,read_queue,locked,require_claim,finish_claim
from catalog_exports import atomic
from archive_cards import change_activity
from card_schema import reader_record
from publish import validate_record
target='TCS-6379'
duplicate='TCS-7033'
claim=read_claims(ROOT)[duplicate]
target_hash='e7c0fa74b18a490f4673e1f8e0e9210a9b126067d83b4e91f6545ce1c9fdd39c'
reason=('Consolidated into TCS-6379 under the atlas duplicate-consolidation policy. '
 'The vertex-deletion target is identical; the arc-deletion target is equivalent for existence of a polynomial kernel by polynomial-time parameter-preserving reductions in both directions. '
 'The original survey record is preserved intact in the archive.')
checked=[
 'Read the 2020 survey, §3.1, printed/PDF p. 18, Open Problem 3.1.',
 'Read the published Computer Science Review 48 (2023), article 100556, §3.1, printed/PDF p. 14: it explicitly records same-parameter reductions between the arc and vertex problems immediately before Open Problem 3.1. Checked the title page, DOI and online date 26 April 2023.',
 'Read the June 2025 Acta Informatica 62 article 25, abstract and §1 introduction: general solution-budget kernelization remains open; long-cycle restrictions and additional structural parameters give different guarantees.',
 'Checked the completed TCS-6379 model, queue hash and sources. Preserved its formal target, existing importance and output convention; made the existing global Lean proof requirement explicit in its answer criterion.',
 'Checked the reduction argument recorded in review_feedback_kernel_merge.md: polynomial output length and parameter bounds compose in both directions, with large binary budgets capped before any replication.',
]
with locked(ROOT):
 require_claim(ROOT,duplicate,claim['token'])
 assert target not in read_claims(ROOT)
 path=ROOT/'data/cards'/f'{target}.json'
 assert hashlib.sha256(path.read_bytes()).hexdigest()==target_hash
 original=(ROOT/'data/cards'/f'{duplicate}.json').read_bytes()
 assert hashlib.sha256(original).hexdigest()==claim['input_sha256']
 queue=read_queue(ROOT)
 row=next((r for r in queue['records'] if r['id']==target),None)
 if row is not None:
  assert row['state']=='completed' and row['output_sha256']==target_hash
 card=json.loads(path.read_text())
 card['references'].extend([
  ref('edge_survey','A survey of parameterized algorithms and the complexity of edge modification',
   'Christophe Crespelle; Pål Grønås Drange; Fedor V. Fomin; Petr Golovach',2023,
   'https://doi.org/10.1016/j.cosrev.2023.100556',
   'Computer Science Review 48, article 100556; online 26 April 2023; §3.1, Open Problem 3.1 and preceding equivalence discussion, printed/PDF p. 14. Earlier arXiv:2001.06867v2 (18 February 2020), same problem on p. 18.'),
  ref('induced_cycles','Data reduction for directed feedback vertex set on graphs without long induced cycles',
   'Jona Dirks; Enna Gerhard; Mario Grobler; Amer E. Mouawad; Sebastian Siebertz',2025,
   'https://doi.org/10.1007/s00236-025-00490-2',
   'Acta Informatica 62, article 25, published 3 June 2025; abstract and §1, general kernel question versus cycle-length and structural restrictions'),
 ])
 card.setdefault('source_consolidations',[]).append(dict(from_id=duplicate,reviewed_on=DATE,note=reason))
 card['related_problem_ids']=[x for x in card.get('related_problem_ids',[]) if x!=duplicate]
 card.setdefault('context_blocks',[]).extend([
  dict(text='The edge-modification survey lists both Directed Feedback Vertex Set and Directed Feedback Arc Set in Open Problem 3.1. In the arc version, one deletes at most the budgeted number of arcs to destroy all directed cycles. The survey records polynomial-time reductions in both directions that preserve the solution-size parameter, so these two formulations have the same answer to the polynomial-kernel existence question. The separate imported survey record TCS-7033 is consolidated here.',citation='edge_survey'),
  dict(text='The June 2025 study still identifies kernelization by the solution budget alone as a central open problem. Its positive results bound induced cycle length or use additional structure; those promises are absent from the present target.',citation='induced_cycles'),
 ])
 card['answer_criterion']='A complete, mathematically correct Lean-checked proof is required. '+card['answer_criterion']
 card.pop('context',None)
 card.setdefault('progress',[]).append(dict(date=DATE,text='Consolidated the equivalent vertex/arc kernel question from the published edge-modification survey and checked the scope of the 2025 restricted-class progress.',citation='edge_survey'))
 card['updated_at']=datetime.now(timezone.utc).isoformat(timespec='seconds')
 validate_record(reader_record(card,CRITERIA),path,CRITERIA)
 output=json.dumps(card,ensure_ascii=False,indent=2)+'\n'
 atomic(path,output)
 output_hash=hashlib.sha256(output.encode()).hexdigest()
 if row is not None:
  row['output_sha256']=output_hash
  atomic(ROOT/'research/card-completion-20260913/queue.json',json.dumps(queue,ensure_ascii=False,indent=2)+'\n')
 with (ROOT/'research/card-completion-20260913/reviews.jsonl').open('a') as ledger:
  ledger.write(json.dumps(dict(id=target,date=DATE,outcome='source_consolidation_amendment',
    changes=[reason],sources_checked=checked,input_sha256=target_hash,output_sha256=output_hash),ensure_ascii=False)+'\n')
print(change_activity([duplicate],reason=reason))
with locked(ROOT):
 archived=ROOT/'data/archive/cards'/f'{duplicate}.json'
 assert archived.read_bytes()==original
 queue=read_queue(ROOT)
 row=next(r for r in queue['records'] if r['id']==duplicate)
 assert row['state']=='pending'
 row.update(state='completed',completed_on=DATE,review_input_sha256=claim['input_sha256'],
   output_sha256=hashlib.sha256(original).hexdigest(),output_path=str(archived.relative_to(ROOT)),
   consolidated_into=target)
 queue['counts']=dict(total=len(queue['records']),**dict(collections.Counter(r['state'] for r in queue['records'])))
 atomic(ROOT/'research/card-completion-20260913/queue.json',json.dumps(queue,ensure_ascii=False,indent=2)+'\n')
 with (ROOT/'research/card-completion-20260913/reviews.jsonl').open('a') as ledger:
  ledger.write(json.dumps(dict(id=duplicate,date=DATE,outcome='merged_after_individual_review',
    consolidated_into=target,changes=[reason],sources_checked=checked,
    input_sha256=claim['input_sha256'],output_path=str(archived.relative_to(ROOT))),ensure_ascii=False)+'\n')
 finish_claim(ROOT,duplicate,claim['token'],queue)
 print(duplicate,queue['counts'])
