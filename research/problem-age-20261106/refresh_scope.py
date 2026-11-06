"""Check live selection and reader order without writing to the shared service."""
import datetime
import json
import subprocess
from pathlib import Path

HERE = Path(__file__).resolve().parent


def fetch(url):
    result = subprocess.run(['curl', '-fsS', '--max-time', '60', url], check=True, capture_output=True, text=True)
    return json.loads(result.stdout)


stamp = datetime.datetime.now(datetime.timezone.utc).isoformat()
catalog = fetch('https://vaclavrozhon.github.io/atlas/catalog.json?age-check=' + stamp)
selection = fetch('https://atlas-public-notes.vaclavrozhon.chatgpt.site/api/selection')
votes = fetch('https://atlas-public-notes.vaclavrozhon.chatgpt.site/api/votes')
assert selection['version'] == catalog['meta']['final_selection']['version'], 'Wait for the in-progress catalogue publication to match the selection service.'
choices = {c['problem_id']: c for c in selection['choices']}
scores = {v['problem_id']: v['score'] for v in votes['votes']}


def current(card):
    return choices.get(card['id'], card['selection'])


def order(card):
    focus = card.get('benchmark_focus', {}).get('position', float('inf')) if current(card)['area'] == card['selection']['area'] else float('inf')
    return (-scores.get(card['id'], 0), focus, -card.get('importance', {}).get('score', 50), card['id'])


targets, counts = [], []
for area in catalog['areas']:
    candidates = sorted((c for c in catalog['cards'] if current(c)['area'] == area['area'] and not c.get('scope_exclusion') and c['status'] != 'excluded' and (c['status'] != 'resolved' or c.get('benchmark_eligibility', {}).get('open_at_cutoff') is True)), key=order)
    greens = [c for c in candidates if current(c)['color'] == 'green']
    reds = [c for c in candidates if current(c)['color'] == 'red'][:5]
    for card in greens + reds:
        targets.append({'id': card['id'], 'title': card['title'], 'area': area['area'], 'color': current(card)['color']})
    counts.append({'area': area['area'], 'green': len(greens), 'red': len(reds)})
for name, value in [('current-selection', selection), ('current-votes', votes), ('current-targets', targets), ('current-counts', counts)]:
    (HERE / (name + '.json')).write_text(json.dumps(value, ensure_ascii=False, indent=2) + '\n')
assessed = json.loads((HERE / 'origins.json').read_text())
result = {'checked_at': stamp, 'reader_version': catalog['meta']['version'], 'selection_version': selection['version'], 'green': sum(a['green'] for a in counts), 'red': sum(a['red'] for a in counts), 'requested': len(targets), 'assessed': len(assessed), 'missing': [t for t in targets if t['id'] not in assessed]}
(HERE / 'current-coverage.json').write_text(json.dumps(result, ensure_ascii=False, indent=2) + '\n')
print(json.dumps(result, ensure_ascii=False))
