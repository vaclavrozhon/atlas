"""Render the proposal and record a reproducible novelty audit; never publish cards."""
import collections, csv, gzip, hashlib, json, pathlib, re

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[1]

def read(path):
    return json.loads(path.read_text())

def normalize(s):
    return re.sub(r'[^\w]+', ' ', s.casefold()).strip()

def main():
    entries = read(HERE / 'candidates.json')
    catalog_raw = (ROOT / 'site/catalog.json').read_bytes()
    catalog = json.loads(catalog_raw)
    old_small = read(ROOT / 'research/fundamental-small-20260910/shortlist.json')
    old_large = read(ROOT / 'research/fundamental-additions-20260910/candidates.json')['entries']
    plan = (ROOT / 'CATEGORY_PLAN.md').read_text().split('## Agreed small categories — 20 each')[1].split('\n## ')[0]
    categories = {int(n): name for n, name in re.findall(r'^(\d+)\. (.+)$', plan, re.M)}
    assert len(categories) == 25
    assert len({e['key'] for e in entries}) == len(entries)
    assert all(e['category'] in categories and e['sources'] and e['question'] and e['importance_cs'] for e in entries)
    assert all(s['url'].startswith('https://') for e in entries for s in e['sources'])
    prior_titles = {normalize(e['title']) for e in old_small + old_large}
    assert not prior_titles.intersection(normalize(e['title']) for e in entries)
    counts = collections.Counter(e['category'] for e in entries)
    assert max(counts.values()) <= 2
    ranks = collections.Counter()
    for e in entries:
        ranks[e['category']] += 1
        e['rank_in_category'] = ranks[e['category']]
        e['category_name'] = categories[e['category']]
        e['ranking_method'] = 'Editorial importance among THIS pass only; previous proposals are not re-ranked.'
    (HERE / 'candidates.json').write_text(json.dumps(entries, ensure_ascii=False, indent=2) + '\n')

    pool = []
    for c in catalog['cards']:
        record = {k: c.get(k) for k in ['id','title','area','formal','source_formulation','legacy','references']}
        record['origin'] = 'catalog'
        pool.append(record)
    for origin, prior in [('prior-small', old_small), ('prior-large', old_large)]:
        for c in prior:
            pool.append({'id': c.get('key') or c.get('slug'), 'origin': origin, 'title': c['title'],
                         'question': c.get('question') or c.get('question_cs'), 'sources': c.get('sources'),
                         'novelty_note': c.get('novelty_note') or c.get('novelty_note_cs')})
    with gzip.open(HERE / 'comparison-pool.json.gz', 'wt', encoding='utf-8') as f:
        json.dump(pool, f, ensure_ascii=False)
    audit = []
    for e in entries:
        rx = re.compile('|'.join(e['patterns']), re.I)
        hits = []
        for c in pool:
            matches = list(rx.finditer(json.dumps(c, ensure_ascii=False)))
            if matches:
                hits.append({'id': c['id'], 'origin': c['origin'], 'title': c['title'],
                             'matched_terms': sorted({m.group() for m in matches})})
        audit.append({'key': e['key'], 'patterns': e['patterns'], 'hits': hits,
                      'manual_resolution': e['novelty_note'], 'near_existing': e['near_existing']})
    (HERE / 'novelty-audit.json').write_text(json.dumps(audit, ensure_ascii=False, indent=2) + '\n')
    meta = {'as_of': '2026-09-10', 'catalog_count': len(catalog['cards']),
            'catalog_version': catalog['meta'].get('version'),
            'catalog_sha256': hashlib.sha256(catalog_raw).hexdigest(),
            'prior_small_count': len(old_small), 'prior_large_count': len(old_large),
            'prior_large_shortlisted_count': sum(e.get('status') == 'shortlisted' for e in old_large),
            'new_count': len(entries), 'category_counts': dict(sorted(counts.items())),
            'unfilled_categories': [n for n in categories if not counts[n]],
            'publication_status': 'Proposal only; no catalogue cards created.',
            'audit_limit': 'Lexical search plus manual reading of close matches; no automatic proof of semantic uniqueness.'}
    (HERE / 'final-audit.json').write_text(json.dumps(meta, ensure_ascii=False, indent=2) + '\n')
    with (HERE / 'candidates.csv').open('w', newline='', encoding='utf-8') as f:
        fields = ['category','category_name','rank_in_category','key','title','question','importance_cs','novelty_note','status_note','sources']
        writer = csv.DictWriter(f, fieldnames=fields, extrasaction='ignore')
        writer.writeheader()
        for e in entries:
            writer.writerow({**e, 'sources': ' | '.join(s['url'] for s in e['sources'])})

    lines = ['# Druhý průchod: další zásadní problémy pro malé kategorie', '',
             '**26 dalších návrhů ve 24 z 25 současných malých kategorií.** Ve 22 kategoriích je jeden nový problém; v Knowledge representation a Structural graph theory dva. Miscellaneous zůstává bez dalšího návrhu.', '',
             'Stav rešerše: 10. září 2026. Jde o doplnění předchozího výběru, s formulacemi a podklady k redakčnímu posouzení. Nové karty nebyly publikovány.', '',
             '## Změna přístupu', '',
             'Vycházel jsem z hlavních mezer popsaných autory přehledů, přednášek a výzkumných programů: hranice výpočetních modelů, úplné charakterizace a optimální dosažitelnost. U každé otázky jsem kontroloval, zda jde o samostatný hlavní problém, a rozlišoval jej od už vyřešených speciálních případů.', '',
             f"Porovnání zahrnuje {len(catalog['cards']):,} záznamů katalogu, {len(old_small)} předchozích návrhů pro malé kategorie a {len(old_large)} položek velkého návrhu (včetně vyřazené duplicity). Li–Li network coding přibylo mezitím do velkého návrhu, a proto zde není započítáno znovu. Blízké záznamy jsem posuzoval podle vybrané otázky a v nejasných případech podle plného zdroje, nikoli jen názvu článku.", '',
             'Hodnocení významu je redakční úsudek. Pořadí uvnitř každé kategorie se týká pouze těchto nových návrhů; starší seznam nepřerovnává. Otevřenost je závěr z uvedených primárních zdrojů a kontrol pozdějších výsledků, nikoli záruka úplnosti literatury.', '',
             '## Přehled', '', '| # | Současná malá kategorie | Další problém(y) |', '|---:|---|---|']
    for n, name in categories.items():
        titles = '<br>'.join(e['title'] for e in entries if e['category'] == n) or 'Bez návrhu splňujícího přísný výběr.'
        lines.append(f'| {n} | {name} | {titles} |')
    for n, name in categories.items():
        lines.extend(['', f'## {n}. {name}', ''])
        selected = [e for e in entries if e['category'] == n]
        if not selected:
            lines.extend(['Nebyl nalezen dostatečně silný samostatný kandidát bez přirozeného domova v jiné kategorii. Zvažované otázky tile assembly vyžadují opatrné rozlišení již omezených nebo vyřešených modelů; do počtu je nepřidávám. Ani obecné kombinatorické hypotézy sem nepřesouvám jen pro zaplnění místa.', ''])
        for e in selected:
            lines.extend([f"### {e['rank_in_category']}. {e['title']}", '',
                          f"**Otázka:** {e['question']}", '',
                          f"**Význam:** {e['importance_cs']}", '',
                          f"**Odlišení od dosavadního seznamu:** {e['novelty_note']}", '',
                          f"**Stav a přesný rozsah:** {e['status_note']}", '', '**Primární podklady:**', ''])
            for s in e['sources']:
                lines.append(f"- [{s['title']}]({s['url']}) — {s['locator']}.")
    lines.extend(['', '## Vyřazené a odložené směry', '',
                  'Viz [rejections.json](rejections.json). Zahrnuje duplicity, staré otázky vyřešené pozdějšími pracemi a nejasné formulace. Vyřazení z tohoto průchodu samo o sobě nemění stav starších karet.', '',
                  '## Audit a data', '',
                  '- [Strojový seznam](candidates.json) a [CSV](candidates.csv).',
                  '- [Lexikální shody a ruční rozlišení](novelty-audit.json).',
                  '- [Počty, otisk a omezení kontroly](final-audit.json).',
                  '- [Snapshot porovnávaných otázek](comparison-pool.json.gz).',
                  '- [Předchozích 72 malých návrhů](../fundamental-small-20260910/proposal.md).', ''])
    (HERE / 'proposal.md').write_text('\n'.join(lines))
    print(json.dumps(meta, ensure_ascii=False, indent=2))
    for item in audit:
        print(item['key'], len(item['hits']), 'lexical hits:', ', '.join(h['id'] for h in item['hits'][:10]))

if __name__ == '__main__':
    main()
