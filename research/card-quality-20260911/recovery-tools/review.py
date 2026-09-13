import json
from pathlib import Path

BASE = Path('/home/vasek/atlas')
DIRECTORY = BASE / 'research/card-quality-20260911'
DATE = '2026-09-12'

def write(path, value):
    temp = path.with_suffix(path.suffix + '.quality-tmp')
    temp.write_text(json.dumps(value, ensure_ascii=False, indent=2) + '\n')
    temp.replace(path)

def card(identifier):
    path = BASE / 'data/cards' / (identifier + '.json')
    value = json.loads(path.read_text())
    before = DIRECTORY / 'before' / path.name
    if not before.exists():
        write(before, value)
    return path, value

def save(identifier, changes, *, notes, checked_sources, state='revised'):
    path, value = card(identifier)
    old = value.get('statement_review', {})
    if value.get('evidence') != 'reviewed' and state == 'revised':
        value.setdefault('upgraded_from', {k:value.get(k) for k in ['evidence','title','references']})
    value.update(changes)
    if 'context_blocks' in changes:
        value['context'] = '\n\n'.join(b['text'] for b in changes['context_blocks'])
    value['reviewed_on'] = value['formulation_reviewed_on'] = DATE
    if state == 'revised':
        value['evidence'] = 'reviewed'
        value['statement_review'] = {
            'reviewed_on':DATE, 'status':'revised',
            'notes':list(dict.fromkeys(old.get('notes', []) + notes)),
            'remaining_issue':'',
            'scope':'Individual mathematical and editorial review, with the primary-source and later-result checks recorded in quality_review. No proof-assistant formalization or independent proof verification.'}
    value['quality_review'] = {
        'reviewed_on':DATE, 'reference_card':'TCS-0001', 'state':state,
        'changes':notes, 'checked_sources':checked_sources,
        'scope':'Checked the statement, model, answer criterion, context, significance and cited results; searched for subsequent work. Searches are not exhaustive, and paper proofs were not independently verified.'}
    write(path, value)
    print(identifier, state)
