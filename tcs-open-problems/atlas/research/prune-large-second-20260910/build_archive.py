"""Install individually written, reversible second-pass decisions under the writer lock."""
import collections
import csv
import datetime
import fcntl
import gzip
import hashlib
import io
import json
import re
import shutil
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
BASE = HERE.parents[1]
sys.path.insert(0, str(BASE))
from publish import _publish, atomic
from taxonomy import BIG

ARCHIVE = BASE / 'to_delete/large-buckets-second-20260910'
REVIEW_ID = ARCHIVE.name
DUPLICATES = {
    '5489': '3105', '5370': '1664', '4777': '1961',
    '5167': '0664', '5531': '0681', '5547': '0669',
    '6177': '1559', '5920': '3636', '6032': '4461', '6253': '2815',
    '5066': '2336', '5080': '0701', '5185': '3690',
    '5301': '5158', '5535': '0711', '6136': '2070',
}
DUPLICATES = {'TCS-' + a: 'TCS-' + b for a, b in DUPLICATES.items()}


def dump(path, value):
    atomic(path, json.dumps(value, ensure_ascii=False, indent=2) + '\n')


def csv_dump(path, rows, fields):
    stream = io.StringIO(newline='')
    writer = csv.DictWriter(stream, fieldnames=fields)
    writer.writeheader()
    writer.writerows(rows)
    atomic(path, stream.getvalue())


def main():
    decisions = json.loads((HERE / 'decisions.json').read_text())
    assert len(decisions) == 543
    ids = {d['id'] for d in decisions}
    assert len(ids) == len(decisions)
    assert [d['sequence'] for d in decisions] == list(range(1, 544))
    with (BASE / '.publish.lock').open('a') as lock:
        fcntl.flock(lock, fcntl.LOCK_EX)
        assert not (ARCHIVE / 'manifest.json').exists(), 'Do not overwrite an existing review'
        _publish()  # incorporate other authors' canonical work before freezing records
        data = json.loads((BASE / 'site/catalog.json').read_text())
        cards = {c['id']: c for c in data['cards']}
        prior_paths = [BASE / 'to_delete' / p / 'manifest.json' for p in
                       ['large-buckets-20260910', 'small-buckets-20260910']]
        prior_hashes = {str(p.relative_to(BASE)): hashlib.sha256(p.read_bytes()).hexdigest()
                        for p in prior_paths}
        for path in prior_paths:
            assert not ids.intersection(json.loads(path.read_text())['records'])
        for d in decisions:
            c = cards[d['id']]
            assert c['selection_group'] == 'large' and c['area'] == d['category'], d['id']
            assert c['evidence'] != 'reviewed' and not c.get('review_outcome', {}).get('complete'), d['id']
            assert not c.get('proposal_import'), d['id']
        for duplicate, retained in DUPLICATES.items():
            assert duplicate in ids and retained not in ids
            assert not cards[retained].get('scope_exclusion'), (duplicate, retained)
        before = collections.Counter(c['area'] for c in data['cards'] if c['selection_group'] == 'large')
        removed = collections.Counter(d['category'] for d in decisions)
        counts = [dict(category=a, before=before[a], removed=removed[a], remaining=before[a]-removed[a]) for a in BIG]
        assert all(r['remaining'] >= 50 for r in counts)
        ARCHIVE.mkdir(parents=True, exist_ok=True)
        with gzip.open(ARCHIVE / 'catalog-before.json.gz', 'wt', encoding='utf-8') as out:
            json.dump(data, out, ensure_ascii=False)
        dump(ARCHIVE / 'records.json', [cards[d['id']] for d in decisions])
        entries, csv_rows = {}, []
        for d in decisions:
            identifier = d['id']
            c = cards[identifier]
            related = sorted({i for i in re.findall(r'TCS-\d{4}', d['reason'])
                              if i in cards and i not in ids and not cards[i].get('scope_exclusion')})
            entry = dict(state='quarantined', category=d['category'], name=d['name'],
                         sequence=d['sequence'], reason=d['reason'], reason_language='cs',
                         reason_code='duplicate' if identifier in DUPLICATES else 'individual_review',
                         decided_on='2026-09-10', related_retained_ids=related,
                         decision_basis='Individually written editorial judgment of saved question, '
                         'source topic, scope and relationship to stronger retained goals. '
                         'Not a new open-status or full-paper review; no score or equal-share cutoff.')
            if identifier in DUPLICATES:
                entry['duplicate_of'] = DUPLICATES[identifier]
            entries[identifier] = entry
            source = c.get('references', [{}])[0]
            sf = c.get('source_formulation', {})
            question = sf.get('text') or c.get('legacy', {}).get('question_excerpt') or c.get('formal', '')
            csv_rows.append(dict(sequence=d['sequence'], id=identifier, name=d['name'],
                                 original_title=c['title'], category=d['category'], state='quarantined',
                                 reason_code=entry['reason_code'], reason=d['reason'],
                                 duplicate_of=entry.get('duplicate_of', ''),
                                 related_retained_ids=' | '.join(related),
                                 saved_question=question, source=source.get('title', ''), url=source.get('url', '')))
        manifest = dict(schema_version=1, review_id=REVIEW_ID, date='2026-09-10',
                        created_at=datetime.datetime.now(datetime.timezone.utc).isoformat(timespec='seconds'),
                        source_version=data['meta']['version'], source_total=len(cards),
                        reviewed_large_count=sum(before.values()), provisional_removed=len(ids),
                        large_remaining=sum(before.values())-len(ids), category_counts=counts,
                        previous_manifest_hashes=prior_hashes, archive_file='records.json',
                        archive_sha256=hashlib.sha256((ARCHIVE/'records.json').read_bytes()).hexdigest(),
                        records=entries)
        csv_dump(ARCHIVE/'decisions.csv', csv_rows, list(csv_rows[0]))
        csv_dump(ARCHIVE/'all-reviewed.csv', [dict(id=c['id'], title=c['title'], category=c['area'],
                 decision='quarantined' if c['id'] in ids else 'retained',
                 reason=entries.get(c['id'], {}).get('reason', 'Not selected for removal in this pass.'))
                 for c in data['cards'] if c['selection_group']=='large'],
                 ['id', 'title', 'category', 'decision', 'reason'])
        report = ['# Druhý průchod velkých kategorií: všech 543 rozhodnutí', '',
                  'Číslování odpovídá seznamu vypsanému v konverzaci. Anglické názvy jsou stručné redakční popisky; '
                  'původní názvy, celé uložené otázky a zdroje jsou v decisions.csv a records.json. '
                  'Každý důvod byl napsán jednotlivě. Jde o předběžný výběr podle významu, ne ověření aktuální otevřenosti.', '']
        report += [f"{d['sequence']}. **{d['id']} — {d['name']}** ({d['category']}). {d['reason']}" for d in decisions]
        atomic(ARCHIVE/'DECISIONS.md', '\n\n'.join(report)+'\n')
        table = ['| Kategorie | Před | Vyřazeno | Zbývá |', '|---|---:|---:|---:|']
        table += [f"| {r['category']} | {r['before']} | {r['removed']} | {r['remaining']} |" for r in counts]
        table.append(f"| **Celkem** | **{sum(before.values())}** | **{len(ids)}** | **{sum(before.values())-len(ids)}** |")
        readme = ('# Druhý průchod velkých kategorií — 10. září 2026\n\n'
                  '**2 134 → 1 591 kandidátů; dalších 543 předběžných vyřazení.**\n\n'
                  'Uživatel požadoval dalších 500–1000 vyřazení a každou položku jednotlivě vysvětlit v konverzaci. '
                  'Všech 543 položek bylo postupně vypsáno s vlastním konkrétním důvodem. '
                  'Trvalý úplný seznam je v [DECISIONS.md](DECISIONS.md).\n\n'
                  'Průchod znovu přečetl uložené otázky a zdrojová témata všech 2 134 zbývajících velkých kandidátů. '
                  'Rozhoduje samostatný význam cíle: hlavní bariéra versus pomocná míra, konkrétní metoda, '
                  'restrikční varianta, neurčený program nebo další formulace již zastoupené otázky. '
                  'Není použit automatický bodový práh ani kvóta vyřazení v kategorii. '
                  'Neúplný zápis sám není důvodem odmítnout rozpoznatelný zásadní problém. '
                  'Jde o redakční úsudky a předběžné přesuny; nejde o čerstvé čtení každého článku, '
                  'kontrolu současné otevřenosti ani konečný výběr 50 položek na kategorii.\n\n'
                  + '\n'.join(table) + '\n\n'
                  'Předchozí velký archiv (2 069) a malý archiv (1 835) zůstávají samostatně aktivní. '
                  'Malých aktivních kandidátů zůstává 1 104, všech aktivních kandidátů 2 695. '
                  'Všech 7 156 uložených ID, formulace, zdroje, stavové informace a poznámky zůstávají zachované. '
                  'Žádná individuálně dokončená karta ani schválený fundamentální návrh nebyl tímto průchodem vyřazen.\n\n'
                  '- `records.json`: úplné aktuální karty těsně před aplikací tohoto průchodu.\n'
                  '- `catalog-before.json.gz`: úplný katalog před přesunem, včetně starších archivů.\n'
                  '- `manifest.json`: živé rozhodnutí, důvod, původní bucket, pořadí a vazby na ponechané cíle.\n'
                  '- `decisions.csv`: všechna jednotlivá rozhodnutí, původní otázka i zdroj.\n'
                  '- `all-reviewed.csv`: všech 2 134 vstupních kandidátů a výsledek tohoto průchodu.\n'
                  '- `validation.json`: kontrola zachování, obnovy, publikace a prohlížeče.\n\n'
                  '## Obnovení\n\nSpouštějte z adresáře atlasu:\n\n```bash\n'
                  f'python3 to_delete/{REVIEW_ID}/restore.py --dry-run TCS-0032\n'
                  f'python3 to_delete/{REVIEW_ID}/restore.py TCS-0032\n'
                  f'python3 to_delete/{REVIEW_ID}/restore.py --all\n```\n\n'
                  'Obnova mění stav na `retained` a publikuje pod společným zámkem. '
                  'Nepřepisuje novější text starým snapshotem a neobnovuje jiné vyřazovací průchody. '
                  'Ve čtečce jsou položky nadále dostupné přes Archive a přímá stabilní ID.\n')
        atomic(ARCHIVE/'README.md', readme)
        shutil.copy2(BASE/'to_delete/large-buckets-20260910/restore.py', ARCHIVE/'restore.py')
        dump(ARCHIVE/'manifest.json', manifest)  # activate only after all review artifacts exist
        _publish()
        for path in prior_paths:
            assert hashlib.sha256(path.read_bytes()).hexdigest() == prior_hashes[str(path.relative_to(BASE))]
        result = json.loads((BASE/'site/catalog.json').read_text())
        assert sum(a['count'] for a in result['areas'] if a['group']=='large') == sum(before.values())-len(ids)
        print(json.dumps(dict(version=result['meta']['version'],removed=len(ids),
                              large_remaining=manifest['large_remaining'],taxonomy=result['meta']['taxonomy']),indent=2))


if __name__ == '__main__':
    main()
