"""Build the editorial list and its auditable bibliographic supplement."""
import collections
import csv
import json
import re
import unicodedata
from pathlib import Path

ROOT = Path(__file__).resolve().parent
ALIASES = {
    'Ryan Williams': 'R. Ryan Williams',
    'Daniel Spielman': 'Daniel A. Spielman',
    'Daniel Kane': 'Daniel M. Kane',
    'David Woodruff': 'David P. Woodruff',
    'Tim Roughgarden': 'Timothy Roughgarden',
    'MohammadTaghi Hajiaghayi': 'Mohammad Hajiaghayi',
    'Rocco Servedio': 'Rocco A. Servedio',
    'László Végh': 'László A. Végh',
    'Timothy Chan': 'Timothy M. Chan',
    'Alexander Razborov': 'Alexander A. Razborov',
    'Fedor Fomin': 'Fedor V. Fomin',
    'Santosh Vempala': 'Santosh S. Vempala',
    'Andrei Bulatov': 'Andrei A. Bulatov',
    'Alexander Sherstov': 'Alexander A. Sherstov',
    'Adam Smith': 'Adam D. Smith',
    'Salil Vadhan': 'Salil P. Vadhan',
    'Robert Kleinberg': 'Robert D. Kleinberg',
    'Clément Canonne': 'Clément L. Canonne',
    'Guy Rothblum': 'Guy N. Rothblum',
    'Umesh Vazirani': 'Umesh V. Vazirani',
    'Aram Harrow': 'Aram W. Harrow',
    'Nisheeth Vishnoi': 'Nisheeth K. Vishnoi',
}


def norm(name):
    return ''.join(c for c in unicodedata.normalize('NFKD', name.casefold())
                   if c.isalnum() and not unicodedata.combining(c))


papers = json.loads((ROOT / 'papers.json').read_text())
nonresearch = re.compile(r'\b(invited talk|keynote|tutorial|preface|front matter)\b', re.I)
excluded = [p for p in papers if nonresearch.search(p['title'])]
research = [p for p in papers if p not in excluded]
(ROOT / 'excluded-records.json').write_text(json.dumps(excluded, ensure_ascii=False, indent=2))
authors = json.loads((ROOT / 'authors.json').read_text())
selection = []
for rank, row in enumerate((ROOT / 'selection.txt').read_text().splitlines(), 1):
    name, focus = [s.strip() for s in row.split('|', 1)]
    canonical = ALIASES.get(name, name)
    matches = [a for a in authors if norm(a['name']) == norm(canonical)]
    assert matches, name
    # The higher-count identities are the Columbia Xi Chen and extractor Xin Li.
    a = max(matches, key=lambda a: a['total'])
    mine = [p for p in research if a['pid'] in p['authors']]
    historical = [p for p in mine if p['year'] <= 2025]
    counts = collections.Counter(p['venue'] for p in historical)
    selection.append(dict(rank=rank, name=name, focus_cs=focus, dblp=a['pid']+'.html',
                          stoc_2011_2025=counts['stoc'], focs_2011_2025=counts['focs'],
                          soda_2011_2025=counts['soda'], total_2011_2025=len(historical),
                          recent_2021_2025=sum(p['year'] >= 2021 for p in historical),
                          stoc_soda_2026=sum(p['year'] == 2026 for p in mine),
                          papers=sorted(mine, key=lambda p: (p['year'], p['venue']), reverse=True)))

assert len(selection) == len({a['dblp'] for a in selection}) == 200
assert not {'Luca Trevisan', 'Michael B. Cohen', 'Mihai Pătraşcu'} & {a['name'] for a in selection}
base = [p for p in research if p['year'] <= 2025]
assert len({(p['venue'], p['year']) for p in base}) == 45
stats = dict(date='2026-09-13', base_years=[2011, 2025], base_venue_years=45,
             base_records_with_authors=sum(p['year'] <= 2025 for p in papers),
             excluded_base_records=sum(p['year'] <= 2025 for p in excluded),
             retained_base_records=len(base),
             base_authors=len({pid for p in base for pid in p['authors']}),
             supplementary_2026_records=sum(p['year'] == 2026 for p in research),
             selected_authors=200)
(ROOT / 'summary.json').write_text(json.dumps(stats, indent=2))
(ROOT / 'top200.json').write_text(json.dumps(selection, ensure_ascii=False, indent=2))
fields = [k for k in selection[0] if k != 'papers']
with (ROOT / 'top200.csv').open('w', newline='') as out:
    writer = csv.DictWriter(out, fieldnames=fields, extrasaction='ignore')
    writer.writeheader()
    writer.writerows(selection)

intro = f'''# 200 současných výzkumníků v TCS — subjektivní výběr

Stav k 13. září 2026. Základem jsou ročníky STOC, FOCS a SODA 2011–2025;
současnou aktivitu doplňují dostupné výstupy roku 2026. Jde o vlastní redakční
úsudek, nikoli o žebříček vydaný konferencemi nebo DBLP. Sousední pořadí je
nejisté; zejména ve druhé stovce je rozumnější pracovat s pásmy než jednotlivými příčkami.

Z přímého [DBLP SPARQL rozhraní](https://sparql.dblp.org/) bylo získáno
{stats['base_records_with_authors']:,} bibliografických záznamů s autory ze všech
45 základních ročníků. Po odstranění {stats['excluded_base_records']} záznamů
označených jako předmluvy, tutoriály nebo zvané přednášky zůstalo
{stats['retained_base_records']:,} záznamů a {stats['base_authors']:,} identit autorů.
STOC a SODA 2026 přidávají {stats['supplementary_2026_records']} záznamů.
Číselný základ je bibliografický přehled; nejde o přečtení plných textů všech prací.

Největší váhu mají zásadní výsledky a techniky v hodnoceném období, poté
dlouhodobá kvalita, současná aktivita a širší vliv. Prostý počet článků
nepředstavuje výsledné skóre. Výzkumníci v kryptografii, kvantových výpočtech
a teorii učení jsou posuzováni i s ohledem na relevantní výsledky mimo tuto trojici.
Záběr odpovídá komunitám těchto konferencí; logika, sémantika a verifikace
zastoupené především na LICS/CAV/POPL by vyžadovaly jinak vymezený výběr.

Kontext k významu výsledků poskytly zejména [STOC Best Paper Awards](https://www.sigact.org/prizes/best_paper.html),
[FOCS Test of Time Awards](https://tc.computer.org/tcmf/focs-test-time-award/),
[FOCS 2025 Paper Awards](https://focs.computer.org/2025/best-paper-awards/)
a [Gödelovy ceny](https://sigact.org/prizes/g%C3%B6del.html).
Aktuálnost byla doplněna z [programu STOC 2026](https://acm-stoc.org/stoc2026/stoc26-program.html)
a [přijatých prací FOCS 2026](https://focs.computer.org/2026/accepted-papers/).
Tyto zdroje podporují odborný kontext; pořadí 1–200 je moje hodnocení.

## Seznam

| # | Výzkumník / výzkumnice | Hlavní důvod zařazení | STOC | FOCS | SODA | 2021–25 celkem |
|---:|---|---|---:|---:|---:|---:|
'''
table = '\n'.join(f"| {a['rank']} | [{a['name']}]({a['dblp']}) | {a['focus_cs']} | {a['stoc_2011_2025']} | {a['focs_2011_2025']} | {a['soda_2011_2025']} | {a['recent_2021_2025']} |" for a in selection)
appendix = '''

## Jak číst data

Každý článek se každému spoluautorovi započítává jednou. Jména jsou spojena
přes identifikátor DBLP, ne pouze přes text jména. Počty ve sloupcích konferencí
pokrývají 2011–2025. Přesun publikační aktivity do COLT, CCC, CRYPTO, TCC, QIP
nebo časopisů může znamenat nízké konferenční číslo při vysokém odborném významu.
Nula v posledním období proto sama neznamená neaktivitu.

Rok je určen ročníkem konference, nikoli rokem vydání sborníku. To je relevantní
například u FOCS 2021, jehož sborník vyšel v roce 2022. Doplněk FOCS 2026 je
kvalitativní kontrola přijatých prací a není zahrnut v bibliografických počtech.

Soubory `sources/*.sparql` zachovávají skutečně provedené dotazy; `sources/*-raw.json`
jejich odpovědi. `papers.json` obsahuje získané záznamy s autory,
`excluded-records.json` vyloučené předmluvy a přednášky a `conference-coverage.csv`
počty získaných záznamů po ročnících před tímto filtrováním.
Nezávislý součet všech položek sborníků se lišil pouze o sedm anonymních
záznamů Front Matter v SODA 2015–2021, které nemají autory.

`top200.csv` obsahuje výběr a čisté konferenční počty. `top200.json` k tomu přidává
všechny odpovídající záznamy z těchto konferencí pro každého vybraného člověka.
Bibliografické počty jsou vlastní agregace této kopie DBLP; nejsou převzatým skóre CSRankings.
'''
(ROOT / 'top200.md').write_text(intro + table + appendix)
print(json.dumps(stats, ensure_ascii=False, indent=2))
print('Verified: 200 distinct author identities; 45 complete base venue-years; all names matched.')
