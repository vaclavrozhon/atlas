"""Individually authored cards for the personal-problem import.

This script only writes a reviewable import payload, never canonical data.
Run scripts/import_cards.py on additions.json to allocate stable IDs.
"""
import json
import runpy
from pathlib import Path

BASE = Path(__file__).resolve().parent
ROOT = BASE.parent.parent
DATE = '2026-09-11'
ROWS = {r['candidate']: r for r in json.loads((BASE / 'matches.json').read_text())}
CATEGORIES = {c['id']: c['key'] for g in json.loads((ROOT / 'data/categories.json').read_text())['groups'] for c in g['categories']}
CARDS = []

def add(pid, title, category, criterion, formal, definitions, context, why, score,
        reference, authors, year, locator, progress, *, url=None, related=(), issue=None, note=''):
    row = ROWS[pid]
    card = dict(
        key='personal-20260911-' + pid.lower(), title=title,
        area=CATEGORIES[category], criterion=criterion, question_type='yes_no',
        formal=formal, definitions=definitions,
        context_blocks=[dict(text=p, citation='primary') for p in context.split('\n\n')],
        why=why,
        answer_criterion='Prove the stated proposition or its logical negation, with the specified quantifiers, model and guarantees. A conditional theorem settles only that conditional claim. Benchmark acceptance requires a complete proof-assistant-checked proof of the full target.',
        references=[dict(id='primary',title=reference,authors=authors,year=year,
                         url=url or row['source'],locator=locator)],
        progress=[dict(date=str(year),text=progress,citation='primary')],
        related=list(related), year=year,
        evidence='source' if issue else 'reviewed', status='source_open',
        status_note='Source-backed open target. The source and relevant later-work search were reviewed on 11 September 2026; this is a bounded literature review, not a proof that no resolution exists. ' + note,
        model_self_contained=not bool(issue), requires_context=bool(issue),
        statement_review=dict(status='needs_specification' if issue else 'revised',
                              reviewed_on=DATE,remaining_issue=issue or '',
                              reason='Individual comparison of the proposed target, source formulation, nearby cards and model conventions.'),
        formulation_reviewed_on=DATE,
        review_note='Admission is based on scientific significance, independently of the inferred researcher affinity. ' + note,
        importance=dict(score=score,method='editorial',assessed_on=DATE,reason=why),
        personal_import=dict(batch='personal-import-20260911',candidate=pid,
                             researcher=row['researcher'],source_file='research/personal-open-problems-100-cs.json',
                             affinity_status='editorial inference, not an attributed research priority'),
        category_assignment=dict(method='editorial_topic',reason='Assigned by the main mathematical target during individual admission review.')
    )
    CARDS.append(card)
    return card

BIT = 'Use uniform classical deterministic Turing computation, with no advice or oracle. Integers and rational numerators and denominators are encoded in binary; L denotes the total input bit length. A polynomial bound has constants independent of the input.'
RAM = 'Use a uniform word-RAM with word length w, addressed word memory, addition and subtraction modulo 2^w, multiplication modulo 2^w, Boolean bit operations, shifts by less than w, comparisons and conditional branches, each costing one step. No nonuniform tables are supplied; initialization and preprocessing are charged.'
CRYPTO = 'The security parameter λ is supplied in unary. Algorithms are uniform probabilistic polynomial-time machines; security is against nonuniform polynomial-size classical circuit families. A function ν(λ) is negligible if for every c>0, ν(λ)≤λ^(−c) for all sufficiently large λ. Probabilities include setup, algorithm and adversary coins. No ideal oracle or additional trusted setup is supplied unless explicitly stated; arbitrary non-black-box implications are allowed.'

if __name__ == '__main__':
    for name in ['group1.py','group2.py','group3.py']:
        exec(compile((BASE/name).read_text(),str(BASE/name),'exec'),globals())
    deferred = [c for c in CARDS if c['personal_import']['candidate'] in {'80A','22A','59B','61B','84B','71A'}]
    for c in deferred:
        pid=c['personal_import']['candidate']
        c['status']='uncertain' if pid=='80A' else 'excluded'
        c['status_note']='Not imported. See dispositions.json for the final duplicate/consolidation decision or the new parallel-repetition solution claim and revised September audit.'
        c['evidence']='source'
    (BASE/'deferred-authored-cards.json').write_text(json.dumps(deferred,ensure_ascii=False,indent=2)+'\n')
    CARDS = [c for c in CARDS if c['personal_import']['candidate'] not in {'80A','22A','59B','61B','84B','71A'}]
    assert len({c['key'] for c in CARDS})==len(CARDS)
    (BASE/'additions.json').write_text(json.dumps(CARDS,ensure_ascii=False,indent=2)+'\n')
    print(f'Authored {len(CARDS)} cards: '+str({level:sum(c['evidence']==level for c in CARDS) for level in ['reviewed','source']}))
