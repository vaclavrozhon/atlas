"""Build the review document and reproducible novelty evidence; never publish cards."""
import csv
import gzip
import hashlib
import json
import re
import sys
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path

HERE = Path(__file__).resolve().parent
ATLAS = HERE.parents[1]
sys.path.insert(0, str(ATLAS))
from taxonomy import problem_text

CATEGORIES = {
    1: 'Quantum computation',
    2: 'Computational geometry and metric spaces',
    3: 'Computational complexity',
    4: 'Algorithms & data structures',
    5: 'Learning theory',
    6: 'Cryptography',
    7: 'Distributed, parallel and sublinear algorithms',
    8: 'Automata and formal languages',
    9: 'Semantics, logic and verification',
    10: 'Optimization and numerics',
}


def main():
    data = json.loads((HERE / 'candidates.json').read_text())
    entries = data['entries']
    assert len(entries) == len({e['key'] for e in entries})
    chosen = [e for e in entries if e['status'] == 'shortlisted']
    raw = (ATLAS / 'site/catalog.json').read_bytes()
    cards = json.loads(raw)['cards']
    known_ids = {c['id'] for c in cards}
    snapshot = [{'id': c['id'], 'title': c['title'], 'area': c['area'],
                 'question_text': problem_text(c), 'references': c['references']}
                for c in cards]
    snapshot_raw = json.dumps(snapshot, ensure_ascii=False).encode()
    (HERE / 'catalog-question-snapshot.json.gz').write_bytes(gzip.compress(snapshot_raw, mtime=0))
    data['catalog_snapshot'] = {
        'checked_at_utc': datetime.now(timezone.utc).isoformat(),
        'sha256': hashlib.sha256(raw).hexdigest(),
        'question_snapshot_sha256': hashlib.sha256(snapshot_raw).hexdigest(),
        'cards': len(cards),
        'scope': 'all saved catalogue cards, including small categories and archive',
    }
    counts = Counter(e['category'] for e in chosen)
    data['coverage'] = {'requested_minimum_per_category': 10,
                        'shortlisted': len(chosen),
                        'minimum_quota_met': all(counts[i] >= 10 for i in CATEGORIES),
                        'counts': {str(i): counts[i] for i in CATEGORIES}}
    (HERE / 'candidates.json').write_text(json.dumps(data, ensure_ascii=False, indent=2) + '\n')
    audit = []
    for e in entries:
        assert e['category'] in CATEGORIES
        assert all(u.startswith('https://') for u in e['sources'])
        assert set(e['near_existing']) <= known_ids, (e['key'], e['near_existing'])
        pattern = re.compile('|'.join('(?:' + p + ')' for p in e['novelty_patterns']), re.I)
        hits = []
        for c in snapshot:
            match = pattern.search(c['question_text'])
            if match:
                hits.append({**c, 'match': c['question_text'][max(0, match.start()-60):match.end()+200]})
        audit.append({'key': e['key'], 'category': e['category'],
                      'pattern_hits': len(hits), 'hits': hits,
                      'editorial_status': e['status'],
                      'near_existing': e['near_existing'],
                      'editorial_note_cs': e['novelty_note_cs']})
    (HERE / 'novelty-audit.json').write_text(json.dumps(audit, ensure_ascii=False, indent=2) + '\n')

    lines = [
        '**Návrhy zásadních nových problémů — 10. září 2026**', '',
        f'Výsledek rešerše: **{len(chosen)} kandidátů v deseti velkých kategoriích**. '
        'Požadovaných 10–20 nových zásadních problémů v každé kategorii se mi nepodařilo doložit. '
        'Níže proto uvádím skutečný počet; seznam neobsahuje náhradní položky přidané pouze pro dosažení kvóty.', '',
        f'Porovnání zahrnovalo všech **{len(cards):,} uložených karet**, včetně malých kategorií. '
        'Hledal jsem v názvech, formulacích a původních výňatcích; u blízkých shod jsem posuzoval '
        'výpočetní model, kvantifikátory a podle potřeby otevřel původní pasáž. '
        'Samotná zmínka o hypotéze v motivaci článku se nepočítá jako existující karta této hypotézy; '
        'existující výňatek formulující tutéž hlavní otázku se počítá, i když je jeho název nečitelný.', '',
        'Výběr významnosti je odborný úsudek: dlouhodobá ústřední otázka oboru, základní hranice '
        'výpočetního modelu nebo chybějící teorie široce používaného primitiva. '
        'Nejde o kompletní výzkumné karty ani nezávislé ověření všech důkazů v citované literatuře. '
        'U jednotlivých položek je uvedeno, co musí zůstat ve formulaci, aby byla opravdu otevřená.', '',
        '| # | Velká kategorie | Noví kandidáti | Chybí do minima 10 |',
        '|---|---|---:|---:|',
    ]
    for i, name in CATEGORIES.items():
        lines.append(f'| {i} | {name} | **{counts[i]}** | {max(0, 10-counts[i])} |')
    lines += [f'| | **Celkem** | **{len(chosen)}** | **{sum(max(0,10-counts[i]) for i in CATEGORIES)}** |', '',
              'Návrhy jsou uloženy odděleně od veřejného katalogu. '
              '[Vyřazené duplicity a nově vyřešené otázky](EXCLUSIONS.md) vysvětlují nejdůležitější odmítnutí. '
              '[JSON](candidates.json) a [CSV](shortlist.csv) obsahují strojově čitelný seznam.', '']
    for category, name in CATEGORIES.items():
        lines += ['---', '', f'**{category}. {name} — {counts[category]} kandidátů**', '']
        for number, e in enumerate((e for e in chosen if e['category'] == category), 1):
            lines += [f"**{number}. [{e['title']}]({e['sources'][0]})**", '',
                      e['question_cs'] + ' ' + e['importance_cs'], '']
            near = ', '.join(e['near_existing'])
            note = ('Nejbližší karty: ' + near + '. ' if near else '') + e['novelty_note_cs']
            lines += [note, '']
            if len(e['sources']) > 1:
                lines += ['Další podklady: ' + ', '.join(
                    f'[zdroj {j}]({u})' for j, u in enumerate(e['sources'][1:], 2)) + '.', '']
    lines += ['---', '', '**Doklady kontroly**', '',
              '[novelty-audit.json](novelty-audit.json) uchovává vyhledané shody a redakční závěr. '
              'Počet regex shod není počet duplicit. '
              '[Komprimovaný snímek formulací](catalog-question-snapshot.json.gz) zachovává vstup kontroly, '
              'protože katalog se souběžně mění. Zdroje jsou připojené přímo k jednotlivým otázkám.', '',
              f"SHA-256 původního catalog.json: `{data['catalog_snapshot']['sha256']}`.", '']
    (HERE / 'REPORT.md').write_text('\n'.join(lines))
    with (HERE / 'shortlist.csv').open('w', newline='') as out:
        writer = csv.writer(out)
        writer.writerow(['category_number', 'category', 'key', 'title', 'question_cs',
                         'importance_cs', 'sources', 'near_existing', 'novelty_note_cs'])
        for e in sorted(chosen, key=lambda e: e['category']):
            writer.writerow([e['category'], CATEGORIES[e['category']], e['key'], e['title'],
                             e['question_cs'], e['importance_cs'], ' | '.join(e['sources']),
                             ', '.join(e['near_existing']), e['novelty_note_cs']])
    print(json.dumps(data['coverage'], ensure_ascii=False))


if __name__ == '__main__':
    main()
