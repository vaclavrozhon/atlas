"""Freeze the requested scope using the reader's shared colors and ordering."""
import json
from pathlib import Path
from datetime import datetime, timezone

ROOT = Path(__file__).resolve().parents[2]
HERE = Path(__file__).resolve().parent
catalog = json.loads((ROOT / 'build/catalog.json').read_text())
selection = json.loads(Path('/tmp/atlas-problem-age-selection.json').read_text())
votes = json.loads(Path('/tmp/atlas-problem-age-votes.json').read_text())
choices = {r['problem_id']: r for r in selection['choices']}
scores = {r['problem_id']: r['score'] for r in votes['votes']}

def active(c):
    return (not c.get('scope_exclusion') and c.get('status') != 'excluded'
            and (c.get('status') != 'resolved' or c.get('benchmark_eligibility', {}).get('open_at_cutoff') is True))

def current(c):
    return choices.get(c['id'], c['selection'])

def key(c):
    focus = (c.get('benchmark_focus', {}).get('position', float('inf'))
             if current(c)['area'] == c['selection']['area'] else float('inf'))
    return (-scores.get(c['id'], 0), focus, -c.get('importance', {}).get('score', 50), c['id'])

groups = []
targets = []
for area in catalog['areas']:
    candidates = sorted((c for c in catalog['cards'] if active(c) and current(c)['area'] == area['area']), key=key)
    greens = [c for c in candidates if current(c)['color'] == 'green']
    reds = [c for c in candidates if current(c)['color'] == 'red'][:5]
    ids = {c['id'] for c in greens + reds}
    chosen = []
    for rank, c in enumerate(candidates, 1):
        if c['id'] not in ids:
            continue
        row = {'id': c['id'], 'title': c['title'], 'area': area['area'], 'area_label': area['label'],
               'color': current(c)['color'], 'category_position': rank, 'vote_score': scores.get(c['id'], 0)}
        targets.append(row)
        chosen.append(row)
    groups.append({'id': area['id'], 'area': area['area'], 'label': area['label'],
                   'green': len(greens), 'red': len(reds), 'cards': chosen})

HERE.mkdir(exist_ok=True)
for name, value in [('selection', selection), ('votes', votes), ('targets', targets), ('categories', groups)]:
    (HERE / (name + '.json')).write_text(json.dumps(value, ensure_ascii=False, indent=2) + '\n')
scope = {'prepared_at': datetime.now(timezone.utc).isoformat(), 'as_of_year': 2026,
         'reader_version': catalog['meta']['version'], 'selection_version': selection['version'],
         'green': sum(g['green'] for g in groups), 'red': sum(g['red'] for g in groups), 'total': len(targets),
         'ordering': 'Shared vote score, then eligible focus position, importance score descending, stable ID; current shared category overrides applied.',
         'request': 'Annotate every green card and the first five red cards in each category with the origin and approximate age of its problem.',
         'dating_policy': 'Distinguish documented origin, approximate period, and latest-known origin date. Date the question, not the card or its newest source. Explain historical roots and modern variants separately. Age runs to 2026, not merely to a resolution date.',
         'excluded_actions': ['No selection or category mutations.', 'No resumption of the deferred catalogue-wide solvedness audit.'],
         'workflow': ['Individual origin assessment using saved source evidence and targeted primary-source lookup.', 'Persist evidence-backed metadata on the cards.', 'Show age in compact and full reader views.', 'Validate coverage, metadata and UI; publish and verify.']}
(HERE / 'scope.json').write_text(json.dumps(scope, ensure_ascii=False, indent=2) + '\n')
print(json.dumps({k: scope[k] for k in ['green', 'red', 'total']}))

