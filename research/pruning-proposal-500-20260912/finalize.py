"""Build and validate the explicitly selected proposal; never edit catalogue cards."""
import hashlib
import json
import re
from datetime import datetime, timezone
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]


def read(name):
    return json.loads((HERE / name).read_text())


draft = read('decisions-draft.json')
reconsidered = read('reconsidered.json')
ledger = read('read-ledger.json')
sources = read('source-checks.json')
overrides = {
    'TCS-4867': 'The AC0 slice of semigroup membership is a finer component of the full finite-semigroup complexity classification retained in TCS-1544. Its separate target concerns the shallowest circuit regime.',
    'TCS-5005': 'The paper itself answers the motivating adaptive-scaling question with an asymptotic guarantee. The saved question should not remain an open existence target; further finite-time refinements would be separate, less central algorithm-analysis questions.',
    'TCS-5247': 'The source already gives adaptive and nonadaptive learners with corresponding lower bounds. The remaining accuracy and logarithmic factors are a specialized estimation refinement; this is not a claim that the complete quantitative problem is solved.',
    'TCS-5399': 'The source proves PPAD-hardness for tree polymatrix Nash equilibrium with twenty actions per player. The general tree-complexity question extracted from its introduction has already received the advertised hardness answer.',
    'TCS-5701': 'The paper labels the universal block-schedule complexity transfer false, with an explicit complexity-collapse caveat. The saved conjecture is used to explain a failure of the principle, not presented as a surviving open target.',
    'TCS-5750': 'The source introduction asks for polynomial-time general graph isomorphism, already represented by TCS-7222. Consolidate the introductory orbit-partition equivalence and reference there; do not discard the underlying important GI problem.',
    'TCS-6299': 'The source already proves different tractability classes for regular trail and simple-path queries. The extracted introductory comparison is answered by the paper itself.',
    'TCS-7088': 'Strong-delay lower bounds for DNF-model enumeration concern a particularly demanding timing convention for one elementary enumeration family. This specialized witness has less independent significance than the main output-sensitive enumeration barriers.'
}
secondary = set('0308 0856 1046 1178 2103 3324 3484 3865 4867 4972 5034 5314 5453 5697 5737 5750 5768 5770 5845 5926 5930 5961 6319 7135'.split())
answered = {'TCS-5005', 'TCS-5399', 'TCS-5701', 'TCS-6299'}
cards = {}
snapshot = []
for path in sorted((ROOT / 'data/cards').glob('*.json')):
    raw = path.read_bytes()
    card = json.loads(raw)
    identifier = card['id']
    digest = hashlib.sha256(raw).hexdigest()
    active = card['status'] not in ('resolved', 'excluded') and not card.get('scope_exclusion')
    cards[identifier] = card
    reads = [entry for entry in ledger.get(identifier, []) if entry['sha256'] == digest]
    if active:
        assert reads, f'Changed or unread active card: {identifier}'
    snapshot.append({'id': identifier, 'sha256': digest, 'status': card['status'],
                     'active': active, 'fields_displayed': sorted({field for entry in reads for field in entry['fields']})})
active_ids = {entry['id'] for entry in snapshot if entry['active']}
selected = sorted(set(draft) & active_ids - set(reconsidered))
assert len(selected) == 500, f'Expected 500 active proposals, found {len(selected)}'
decisions = []
for identifier in selected:
    card = cards[identifier]
    reason = overrides.get(identifier, draft[identifier]['reason'])
    refs = re.findall(r'TCS-\d{4}', reason)
    assert all(ref in active_ids and ref not in selected for ref in refs), (identifier, refs)
    primary = ('source_answered_or_rejected' if identifier in answered else
               'secondary_consolidation' if identifier[4:] in secondary else 'lower_independent_significance')
    decisions.append({'id': identifier,
                      'problem': 'Worst-case updates for indexed lists' if identifier == 'TCS-2730' else card['title'],
                      'reason': reason, 'primary_basis': primary,
                      'previous_proposal_reaffirmed': draft[identifier]['previous_proposal_reaffirmed'],
                      'source_check': sources.get(identifier)})
counts = {basis: sum(d['primary_basis'] == basis for d in decisions) for basis in sorted({d['primary_basis'] for d in decisions})}
metadata = {
    'created_at_utc': datetime.now(timezone.utc).isoformat(),
    'reviewed_active_cards': len(active_ids), 'proposed_removals': len(decisions),
    'active_cards_remaining_if_accepted': len(active_ids) - len(decisions),
    'initial_candidates': len(draft), 'reconsidered_and_retained': len(reconsidered),
    'candidates_now_inactive': sorted(set(draft) - active_ids),
    'decision_basis_counts': counts,
    'scope': 'Proposal only. No canonical cards, manifest, generated site, or exclusion state changed.',
    'priority': 'Independent scientific importance first; overlap second. No category quotas, score cutoffs, or formalization-cost filter.',
    'review_basis': 'Every active card was displayed and editorially assessed using its question or source-grounded summary and motivation. Initial candidates received a second pass over remaining summary sentences and substantive significance notes; selected borderline cases received fuller record and primary-source checks. This is not a fresh full-paper or current-status certification of every card.',
    'quantitative_policy': 'Numerical and function-valued targets are valid; lack of a simple closed form or difficulty of Lean formalization is not a removal reason.',
    'ordering': 'Ascending identifier for review, not a ranking of weakness.'
}
(HERE / 'decisions.json').write_text(json.dumps({'metadata': metadata, 'decisions': decisions}, ensure_ascii=False, indent=2) + '\n')
(HERE / 'input-snapshot.json').write_text(json.dumps(snapshot, indent=2) + '\n')
lines = [f'# Proposal to remove 500 cards — 2026-09-12', '',
         f'Reviewed all {len(active_ids)} currently active records. This is a proposal only; no catalogue cards were removed. Accepting this batch would leave {len(active_ids)-500} active records, so it does not by itself finish selection of Top500.', '',
         metadata['priority'], '', metadata['review_basis'], '', metadata['quantitative_policy'], '',
         f'The first pass produced {len(draft)} candidates. The second pass retained {len(reconsidered)} on substantive importance grounds; {len(set(draft)-active_ids)} other candidates had been marked resolved by concurrent catalogue work and are not counted among these 500.', '',
         'The per-card basis labels distinguish scientific selection, secondary consolidation, and questions already answered or rejected in their source. Consolidation proposals require preserving relevant references and checking any explicitly noted model conventions before implementation. No such implementation is performed here.', '',
         'See `decisions.json`, `input-snapshot.json`, `read-ledger.json`, `reconsidered.json`, and `source-checks.json` for the selection, current hashes, displayed-field log, second-pass retentions, and targeted source checks.', '',
         'Listed by identifier, not ranked by weakness.', '']
for n, d in enumerate(decisions, 1):
    link = f"../../data/cards/{d['id']}.json"
    source = f" [Source check]({d['source_check']['url']})." if d['source_check'] else ''
    lines.append(f"{n}. **[{d['id']}]({link}) — {d['problem']}.** {d['reason']}{source}")
(HERE / 'proposal.md').write_text('\n'.join(lines) + '\n')
print(json.dumps(metadata, ensure_ascii=False, indent=2))
