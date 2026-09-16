"""Apply the user's consolidation into the already reviewed EFI/OWSG target."""
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
target='TCS-1961'
duplicate='TCS-5015'
claim=read_claims(ROOT)[duplicate]
target_hash='296f6691ee98a2946c882c58eb86aa16f1d0678f76be98584d169fefceacf3e3'
reason=('Merged into TCS-1961 by explicit user decision on 16 September 2026. '
 'The generic EFI-foundations record is replaced in the active atlas by the already reviewed ordinary-model EFI-to-efficiently-verifiable-OWSG question; '
 'its ITCS 2023 source and broader provenance are preserved.')
with locked(ROOT):
 require_claim(ROOT,duplicate,claim['token'])
 assert target not in read_claims(ROOT)
 path=ROOT/'data/cards'/f'{target}.json'
 assert hashlib.sha256(path.read_bytes()).hexdigest()==target_hash
 original=(ROOT/'data/cards'/f'{duplicate}.json').read_bytes()
 assert hashlib.sha256(original).hexdigest()==claim['input_sha256']
 queue=read_queue(ROOT)
 row=next(r for r in queue['records'] if r['id']==target)
 assert row['state']=='completed' and row['output_sha256']==target_hash
 card=json.loads(path.read_text())
 card['references'].append(ref('efi_foundations',
   'On the Computational Hardness Needed for Quantum Cryptography',
   'Zvika Brakerski; Ran Canetti; Luowen Qian',2023,
   'https://doi.org/10.4230/LIPIcs.ITCS.2023.24',
   'ITCS 2023, Article 24; abstract and §1.2, pp. 24:9–24:10, especially Quantum unforgeability'))
 card.setdefault('source_consolidations',[]).append(dict(from_id=duplicate,
   reviewed_on=DATE,note=reason+' The original broad minimal-primitive discussion is not claimed equivalent to every specialized implication in that paper.'))
 card['related_problem_ids']=[x for x in card.get('related_problem_ids',[]) if x!=duplicate]
 card.setdefault('context_blocks',[]).append(dict(
   text='The earlier ITCS 2023 EFI-foundations paper asks how quantum unforgeability and one-way state generators relate to EFI pairs. Its broad minimal-primitive discussion was separately imported as TCS-5015. The user consolidated that general record here, selecting this card’s precise ordinary-model implication; other pseudorandomness and complexity questions in the 2023 paper are not additional benchmark targets.',
   citation='efi_foundations'))
 card['updated_at']=datetime.now(timezone.utc).isoformat(timespec='seconds')
 validate_record(reader_record(card,CRITERIA),path,CRITERIA)
 output=json.dumps(card,ensure_ascii=False,indent=2)+'\n'
 atomic(path,output)
 row['output_sha256']=hashlib.sha256(output.encode()).hexdigest()
 atomic(ROOT/'research/card-completion-20260913/queue.json',json.dumps(queue,ensure_ascii=False,indent=2)+'\n')
 with (ROOT/'research/card-completion-20260913/reviews.jsonl').open('a') as ledger:
  ledger.write(json.dumps(dict(id=target,date=DATE,outcome='source_consolidation_amendment',
    changes=[reason],sources_checked=['ITCS 2023 Article 24: abstract, introduction and §1.2, especially Quantum unforgeability on p. 24:10.'],
    input_sha256=target_hash,output_sha256=row['output_sha256']),ensure_ascii=False)+'\n')
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
    consolidated_into=target,changes=[reason],sources_checked=[
     'Read ITCS 2023 Article 24 abstract, introduction and §1.2 open questions.',
     'Inspected the completed active TCS-1961 formulation and its 2024–2026 sources; preserved its selected security conventions and assessed importance.',
    ],input_sha256=claim['input_sha256'],output_path=str(archived.relative_to(ROOT))),ensure_ascii=False)+'\n')
 finish_claim(ROOT,duplicate,claim['token'],queue)
 print(duplicate,queue['counts'])
