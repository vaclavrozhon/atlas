"""Preserve an invalid background-sentence extraction without inventing a target."""
import collections
import hashlib
import json
import sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT/'research/card-completion-20260913'))
from complete_review import DATE
from review_queue import read_claims,read_queue,locked,require_claim,finish_claim
from catalog_exports import atomic
from archive_cards import change_activity
identifier='TCS-5427'
claim=read_claims(ROOT)[identifier]
reason=('Invalid open-question extraction: the cited CCC 2016 §1.2 sentence describes prior work; '
 'the same paper announces the multipass characterization in its abstract and §1.3 and gives Theorem 5.1 in §5. '
 'Original record preserved; individual review in research/recovery-20260916/review_turnstile_extraction.md.')
with locked(ROOT):
 require_claim(ROOT,identifier,claim['token'])
 original=(ROOT/'data/cards'/f'{identifier}.json').read_bytes()
 assert hashlib.sha256(original).hexdigest()==claim['input_sha256']
 assert next(r for r in read_queue(ROOT)['records'] if r['id']==identifier)['state']=='pending'
print(change_activity([identifier],reason=reason))
with locked(ROOT):
 archived=ROOT/'data/archive/cards'/f'{identifier}.json'
 assert archived.read_bytes()==original
 queue=read_queue(ROOT)
 row=next(r for r in queue['records'] if r['id']==identifier)
 row.update(state='completed',completed_on=DATE,
   review_input_sha256=claim['input_sha256'],
   output_sha256=hashlib.sha256(original).hexdigest(),
   output_path=str(archived.relative_to(ROOT)),
   review_outcome=dict(complete=True,disposition='invalid_extraction',
     review_path='research/recovery-20260916/review_turnstile_extraction.md'))
 queue['counts']=dict(total=len(queue['records']),**dict(collections.Counter(r['state'] for r in queue['records'])))
 atomic(ROOT/'research/card-completion-20260913/queue.json',json.dumps(queue,ensure_ascii=False,indent=2)+'\n')
 with (ROOT/'research/card-completion-20260913/reviews.jsonl').open('a') as ledger:
  ledger.write(json.dumps(dict(id=identifier,date=DATE,outcome='invalid_extraction_after_individual_review',
    changes=[reason,'Corrected the provenance locator from PDF p. 2 to published p. 20:3 in the disposition notes.'],
    sources_checked=[
     'CCC 2016 Article 20: abstract, §§1.2–1.3, §2 definitions, §5 Theorem 5.1 and its proof, Appendix A.',
     'Jiang–Liu–Yu, arXiv:2604.22052v1, 23 April 2026: abstract and §1.3 related work, p. 5.',
    ],
    status_review='Source-context exclusion; no independent proof certification or replacement target.',
    input_sha256=claim['input_sha256'],output_path=str(archived.relative_to(ROOT)),
    review_path='research/recovery-20260916/review_turnstile_extraction.md'),ensure_ascii=False)+'\n')
 finish_claim(ROOT,identifier,claim['token'],queue)
 print(identifier,queue['counts'])
