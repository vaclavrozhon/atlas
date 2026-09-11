"""Build a standalone, offline bibliography and per-source reading notes."""
import csv
import datetime
import hashlib
import html
import io
import json
from pathlib import Path
from reviewed import NOTES
import reviewed_areas  # Registers the specialist-source expansion and rereads.

ROOT=Path(__file__).resolve().parents[1]
SOURCES=json.loads((ROOT/'sources.json').read_text())
AREA_DATA=json.loads((ROOT/'area-coverage.json').read_text())
AREAS=AREA_DATA['areas']
assert set(NOTES)=={s['id'] for s in SOURCES}
assert len(AREAS)==35 and sum(a['tier']=='large' for a in AREAS)==10
assert [a['id'] for a in AREAS]==[f'L{i:02}' for i in range(1,11)]+[f'S{i:02}' for i in range(1,26)]
for a in AREAS:
    assert a['primary_source_id'] in a['source_ids']
    assert NOTES[a['primary_source_id']]['problems'],a['id']
    for k in a['source_ids']:
        assert k in NOTES and NOTES[k].get('review_pass'),(a['id'],k)
LABELS={'question':'Question','conjecture':'Conjecture','research_direction':'Research direction'}
LIBRARY=[]
ENTRIES=[]
for s in SOURCES:
    key=s['id'];n=NOTES[key]
    a=json.loads((ROOT/'audit'/f'{key}.json').read_text())
    assert a['status']=='downloaded',key
    assert hashlib.sha256((ROOT/'pdf'/f'{key}.pdf').read_bytes()).hexdigest()==a['sha256'],key
    markers=json.loads((ROOT/'audit'/f'{key}.markers.json').read_text())
    d={**s,**n,'download':a,'pdf':f'pdf/{key}.pdf','text':f'text/{key}.txt',
       'note':f'notes/{key}.md','marker_pages':sorted({m['pdf_page'] for m in markers}),
       'current_status_review':'not_performed','source_identity_checked':True,
       'inventory_is_exhaustive_for_entire_work':False}
    d['selected_for_categories']=[c['id'] for c in AREAS if key in c['source_ids']]
    d['inventory_target']=n.get('inventory_target','selected_explicit_unresolved_statements')
    for i,p in enumerate(d['problems'],1):
        assert 1<=p['pdf_page']<=a['pages'],(key,p)
        assert p['kind'] in LABELS
        p.update(entry_key=f'{key}/{i:02}',source_id=key,
            local_pdf_url=f"pdf/{key}.pdf#page={p['pdf_page']}",
            source_pdf_url=s['pdf_url'].split('#')[0]+f"#page={p['pdf_page']}",
            status='as_presented_in_source; current_status_not_checked')
        ENTRIES.append({**p,'source_title':s['title'],'source_year':s['year']})
    lines=[f"# {s['title']}",'',s['authors'],'',
        f"**Source year/version:** {s['year'] or 'undated early draft'}. {s['edition_note']}",'',
        f"[Source page]({s['source_url']}) · [Local PDF](../{d['pdf']}) · [Extracted text](../{d['text']}) · [Back to library](../README.md)",'',
        '## Why included','',n['selection_reason'],'',
        '## Reading scope','',n['coverage'],'',
        'This is a source inventory. The entries describe what this version presents as unresolved. Current open status has not been checked. Summaries can group related variants and are not substitutes for the source definitions.','',
        'The specialist pass aims to collect all explicit unresolved statements throughout the downloaded work, including outside its selection category. Exhaustiveness for implicit questions or every passage of a long book is not certified.' if d['selected_for_categories'] else 'This background reference retains the original selective inventory; it is not part of the specialist reread for the 35 categories.','']
    if d['selected_for_categories']:
        lines+=['**Selected for:** '+', '.join(d['selected_for_categories'])+'. [Category coverage](../AREA_COVERAGE.md).','']
    if n['caution']:lines += [n['caution'],'']
    lines+=['## Open questions and directions in the source','']
    if not n['problems']:lines+=['No explicit unresolved question identified in the reviewed material.','']
    for i,p in enumerate(d['problems'],1):
        lines += [f"{i}. **{LABELS[p['kind']]}:** {p['summary']} — {p['locator']}. [PDF p. {p['pdf_page']}](../{p['local_pdf_url']})",'']
    lines+=['## Further inspection','',
        'The following page list comes from a mechanical full-text marker scan. It includes false positives, historical questions, bibliography entries and solved conjectures; it is not an additional reviewed problem list.','',
        ', '.join(f'[{p}](../{d["pdf"]}#page={p})' for p in d['marker_pages']) or 'No matching pages.','',
        '## Download provenance','',f"- Retrieved: {a['retrieved_at']}",
        f"- Pages: {a['pages']}; bytes: {a['bytes']:,}",
        f"- SHA-256: `{a['sha256']}`",f"- Final URL: {a.get('final_url',s['pdf_url'])}",'',
        'PDF pages are counted from one, including front matter. They may differ from printed page numbers. This local copy is for personal research; retain the original author/publisher distribution terms.','']
    (ROOT/d['note']).write_text('\n'.join(lines))
    LIBRARY.append(d)

total_bytes=sum(d['download']['bytes'] for d in LIBRARY)
stats={'sources':len(LIBRARY),'annotated_entries':len(ENTRIES),
       'sources_with_entries':sum(bool(d['problems']) for d in LIBRARY),
       'pdf_pages':sum(d['download']['pages'] for d in LIBRARY),'pdf_bytes':total_bytes,
       'entry_kinds':{k:sum(p['kind']==k for p in ENTRIES) for k in LABELS},
       'built_at':datetime.datetime.now(datetime.timezone.utc).isoformat(),
       'scope':'Independent source library; no catalogue matching, import, deduplication or publication.',
       'status_scope':'Open in the downloaded source version; current status not reviewed.',
       'counting_unit':'Source entries, sometimes grouping variants; not distinct current open problems.'}
stats.update(categories=len(AREAS),large_categories=10,small_categories=25,
             categories_with_downloaded_annotated_primary_source=len(AREAS),
             specialist_sources=sum(bool(d['selected_for_categories']) for d in LIBRARY),
             new_sources=18,initial_sources=32,
             specialist_entries=sum(len(d['problems']) for d in LIBRARY if d['selected_for_categories']))
(ROOT/'library.json').write_text(json.dumps({'meta':stats,'sources':LIBRARY},ensure_ascii=False,indent=2))
(ROOT/'open-problems.json').write_text(json.dumps(ENTRIES,ensure_ascii=False,indent=2))
(ROOT/'audit/validation.json').write_text(json.dumps(stats,ensure_ascii=False,indent=2))

def csv_write(name,rows,fields):
    with (ROOT/name).open('w',newline='',encoding='utf-8-sig') as f:
        w=csv.DictWriter(f,fieldnames=fields,extrasaction='ignore');w.writeheader();w.writerows(rows)
csv_write('open-problems.csv',ENTRIES,['entry_key','source_id','source_title','source_year','kind','summary','locator','pdf_page','local_pdf_url','source_pdf_url','status'])
csv_write('sources.csv',[dict(d,entries=len(d['problems']),pages=d['download']['pages'],sha256=d['download']['sha256'],category_ids=';'.join(d['selected_for_categories'])) for d in LIBRARY],['id','title','authors','year','publication_year','edition_note','kind','area','category_ids','entries','pages','source_url','pdf_url','pdf','note','sha256','inventory_target'])

by_id={d['id']:d for d in LIBRARY}
coverage=['# Pokrytí 10 + 25 oblastí','',
    '**35 z 35 oblastí má stažený specializovaný zdroj s anotovanými otázkami.** Celkem je zde vybráno 35 hlavních zdrojů a jeden doplňkový. Rozšíření přidalo 18 PDF; 18 vhodných titulů z původní knihovny bylo znovu prověřeno. Celá knihovna nyní obsahuje 50 titulů.','',
    'Oblasti odpovídají přijatému plánu z 10. září 2026. Toto je pouze přiřazení oblastí ke zdrojům. Soupisy obsahují nalezené výslovné otázky, domněnky a výzkumné směry z celého zdroje, včetně témat mimo danou oblast.','',
    'U číslovaných seznamů byly projity všechny položky; opakování a související varianty se mohou slučovat. Zahrnuty jsou také nečíslované pasáže a otevřené případy v tabulkách. Úplnost každé implicitní otázky v rozsáhlých knihách nelze garantovat; podrobný rozsah a výjimky jsou v poznámkách.','',
    '**Stav je podle stažené verze, nikoli ověření otevřenosti k dnešku.** Otázky vyřešené později v témže textu jsou vynechány. Čísla udávají anotované položky, nikoli unikátní aktuálně otevřené problémy.','',
    '[Prohledávatelná knihovna](index.html) · [Bibliografie a metodika](README.md) · [Strojový přehled oblastí](area-coverage.json)','']
for tier,title in [('large','10 velkých oblastí'),('small','25 malých oblastí')]:
    coverage+=['## '+title,'','| Oblast | Specializovaný zdroj | Položky | Zaměření výběru |','| --- | --- | ---: | --- |']
    for a in AREAS:
        if a['tier']!=tier:continue
        d=by_id[a['primary_source_id']]
        sources=f"[{d['title']}]({d['note']}) · [PDF]({d['pdf']})"
        for k in a['source_ids']:
            if k!=d['id']:
                aux=by_id[k];sources+=f"<br>Doplněk: [{aux['title']}]({aux['note']}) · [PDF]({aux['pdf']}) ({len(aux['problems'])} položek)"
        coverage.append(f"| {a['id']} — {a['title']} | {sources} | {len(d['problems'])} | {a['selection_note']} |")
    coverage+=['']
coverage+=['## Poznámky k výběru','',
    '- Jedna specializovaná reference reprezentuje konkrétní část široké oblasti; nepředstavuje úplnou bibliografii všech jejích podoborů.',
    '- U S25 Miscellaneous je konkrétním zástupcem survey o rekonfiguraci dominujících množin. Kategorie se tím nepřejmenovává.',
    '- Doplňkový přehled Regular Model Checking má nulový počet explicitně nevyřešených otázek: jeho Further Directions popisují známá rozšíření. Hlavním zdrojem L09 s otázkami je Loop Termination.',
    '- Rao–Yehudayoff a Essential Coding Theory jsou dostupné neúplné autorské drafty. Jejich rozsah není vydáván za celé publikované knihy.',
    '- Číslování L01–L10 a S01–S25 patří pouze tomuto přehledu oblastí. Žádné položky nebyly přiřazovány k problémům původního katalogu.','']
(ROOT/'AREA_COVERAGE.md').write_text('\n'.join(coverage))

readme=['# Samostatná knihovna učebnic a surveys TCS','',
    f"**{len(LIBRARY)} titulů · {len(ENTRIES)} anotovaných položek · {stats['pdf_pages']:,} stran PDF.**",'',
    'Otevři **[prohledávatelný přehled](index.html)** nebo **[pokrytí 10 + 25 oblastí](AREA_COVERAGE.md)**. Přehled funguje přímo ze souboru a offline; nabízí filtr podle všech 35 oblastí. Poznámky k odborným zdrojům jsou anglicky.','',
    '**Rozšíření: 18 nových PDF a 18 znovu prověřených původních zdrojů pokrývá všech 35 oblastí.** Každá oblast má hlavní zdroj s anotacemi; L09 má navíc jeden doplňkový survey. Zbylých 14 titulů zůstává jako původní základní knihovna.','',
    'Jde o samostatnou databanku zdrojů: žádné párování s naším katalogem, převod jeho identifikátorů ani publikování do atlasu.','',
    '## Co přehled obsahuje','',
    '- PDF stažená z autorských, univerzitních, vydavatelských stránek a veřejných odborných repozitářů; ke každému text, původní URL a kontrolní součet.',
    '- Ke každému titulu vlastní poznámku s přehledem otázek, domněnek a výzkumných směrů, umístěním ve zdroji a odkazy na stránky PDF.',
    '- U 36 zdrojů vybraných pro oblasti je cílem soupis všech nalezených výslovných otevřených otázek v celém textu, včetně témat mimo vybranou oblast. Číslované seznamy jsou pokryty celé s výjimkou položek vyřešených v témže zdroji; varianty a opakování se mohou slučovat.',
    '- Zahrnuty jsou i nečíslované otázky a otevřené případy v tabulkách. Úplnost každé implicitní otázky v dlouhé knize není certifikována. U 14 základních titulů mimo tento výběr zůstává původní výběrový soupis. Přesný rozsah a výjimky jsou u každého zdroje.',
    '- Úplný strojový index stránek s indikátory otevřených problémů pro další čtení; tento index obsahuje také falešné nálezy a není odborně schváleným seznamem otázek.','',
    '**„Otevřené“ zde znamená podle daného vydání zdroje. Aktuální stav po jeho vydání se neověřoval.** Otázky, které samotný zdroj označuje za vyřešené, jsou v kontrolovaných pasážích vynechány. Běžná cvičení nejsou automaticky otevřenými problémy. Počet položek není počet navzájem různých dnes otevřených problémů.','',
    'U Bubeckovy *Convex Optimization*, Hazanovy *Introduction to Online Convex Optimization* a doplňkového survey *Regular Model Checking* nebyla v prohledaném textu nalezena výslovná nevyřešená otázka. Tituly mají vlastní poznámky. Rao–Yehudayoff a *Essential Coding Theory* jsou neúplné autorské drafty; konkrétní verze jsou výslovně označeny.','',
    'Výběr upřednostňuje odborné reference s dostupným autorským textem. Specializovaný zdroj může pokrývat jen část široké oblasti; důvod jeho výběru je uveden v přehledu. Jde o redakční výběr, nikoli bibliometrické pořadí.','',
    '## Tituly','', '| Titul | Oblast | Rok souboru / vydání | Položky | Soubory |', '| --- | --- | --- | ---: | --- |']
for d in LIBRARY:
    readme.append(f"| [{d['title']}]({d['note']}) | {d['area']} | {d['year'] or 'nedatovaný draft'} | {len(d['problems'])} | [PDF]({d['pdf']}) · [text]({d['text']}) |")
readme+=['','## Data a reprodukce','',
    '- [Kompletní databanka JSON](library.json), [bibliografie CSV](sources.csv).',
    '- [Anotované položky JSON](open-problems.json), [CSV](open-problems.csv).',
    '- [Pokrytí oblastí JSON](area-coverage.json).',
    '- `sources.json`: bibliografie a zdrojové adresy; `scripts/reviewed.py`: původní ručně psané soupisy; `scripts/reviewed_areas.py`: nové a rozšířené soupisy pro oblasti.',
    '- `audit/`: údaje o stažení, hashe, metadata PDF, index nálezů a validace.','',
    'Z této složky:','', '```bash','python3 scripts/fetch.py','python3 scripts/scan.py','python3 scripts/build.py','```','',
    'Stahování potřebuje Python s `requests` a nástroje `pdfinfo` a `pdftotext` (Poppler). Sestavení používá standardní knihovnu Pythonu. Existující PDF se při opakovaném spuštění nepřepisují; pro jinou verzi založ nový zdroj.','',
    'Soubory jsou místní kopie pro osobní studium; veřejná dostupnost neznamená povolení k jejich dalšímu zveřejnění. Knihovna se nikam nenasazuje ani nesdílí.','']
(ROOT/'README.md').write_text('\n'.join(readme))

esc=html.escape
cards=[]
for d in LIBRARY:
    rows=''.join(f'<li data-kind="{p["kind"]}"><span class="kind">{LABELS[p["kind"]]}</span> {esc(p["summary"])} <a class="locator" href="{esc(p["local_pdf_url"],quote=True)}">{esc(p["locator"])} · PDF {p["pdf_page"]} ↗</a></li>' for p in d['problems'])
    marker_links=' · '.join(f'<a href="{d["pdf"]}#page={p}">{p}</a>' for p in d['marker_pages'])
    category_text=' · '.join(f"{a['id']} {a['title']}" for a in AREAS if a['id'] in d['selected_for_categories'])
    cards.append(f'''<article id="{d['id']}" data-area="{esc(d['area'],quote=True)}" data-categories="{' '.join(d['selected_for_categories'])}" data-kind="{d['kind']}" data-count="{len(d['problems'])}">
<div class="eyebrow">{esc(d['area'])} <span>{d['year'] or 'Undated draft'} · {d['download']['pages']} pages</span></div>
<h2><a href="#{d['id']}">{esc(d['title'])}</a></h2><p class="authors">{esc(d['authors'])}</p>
<p class="category-label">{esc(category_text) if category_text else 'Background reference · original selective inventory'}</p>
<p class="reason">{esc(d['selection_reason'])}</p>
<nav class="links"><a href="{d['pdf']}">Read PDF ↗</a><a href="{d['text']}">Full text</a><a href="{d['note']}">Reading note</a><a href="{esc(d['source_url'],quote=True)}">Original source ↗</a></nav>
<p class="edition">{esc(d['edition_note'])}</p>
<div class="scope"><strong>Reading scope.</strong> {esc(d['coverage'])}</div>
{f'<p class="caution">{esc(d["caution"])}</p>' if d['caution'] else ''}
<h3>{len(d['problems'])} source entries</h3><ol>{rows}</ol>
{'' if rows else '<p class="none">No explicit unresolved question identified in the reviewed material.</p>'}
<details><summary>Further reading: pages flagged by text scan</summary><p>Unreviewed markers, including false positives and already solved questions. These are not additional approved entries.</p><p class="pages">{marker_links}</p></details>
</article>''')

page='''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>TCS Source Library</title><link rel="stylesheet" href="style.css"></head><body>
<header><div class="wrap"><p class="eyebrow">Independent research databank · September 2026</p><h1>TCS Source Library</h1><p class="intro">Foundational textbooks, monographs &amp; surveys.<br>Open questions, as presented in each source.</p><div class="stats">STATS</div><p class="notice">These are dated source notes. Present-day open status has not been checked. Some entries group variants or describe research directions. The category filter selects sources; it keeps all their entries, including other topics. Entire-work exhaustiveness is not certified; see each reading scope. This library has no links to catalogue problems.</p><nav class="downloads"><a href="AREA_COVERAGE.md">Coverage: 10 + 25 categories</a><a href="README.md">Read me</a><a href="sources.csv">Bibliography CSV</a><a href="open-problems.csv">Entries CSV</a><a href="library.json">Complete JSON</a></nav></div></header>
<main class="wrap"><section class="controls" aria-label="Search and filters"><label class="search">Search titles, authors or problems<input id="search" type="search" placeholder="Try: lattice, treewidth, sample compression…"></label><label class="category-select">Agreed category (10 + 25)<select id="category"><option value="">All categories + background references</option>CATEGORIES</select></label><label>Subject<select id="area"><option value="">All subjects</option>AREAS</select></label><label>Source type<select id="type"><option value="">All types</option><option value="book">Books &amp; drafts</option><option value="monograph">Monographs</option><option value="survey">Surveys</option></select></label><button id="clear" type="button">Reset</button></section><p id="count" role="status" aria-live="polite"></p><div id="empty" hidden>No sources match these filters.</div><div id="sources">CARDS</div></main><footer class="wrap">Local PDFs and text are available offline. Follow original distribution terms. Summaries are reading aids; use the linked source for precise definitions.</footer><script src="app.js"></script></body></html>'''
page=page.replace('STATS',f'<span><b>35/35</b> categories</span><span><b>{len(LIBRARY)}</b> sources</span><span><b>{len(ENTRIES)}</b> annotated entries</span><span><b>{stats["pdf_pages"]:,}</b> PDF pages</span>')
page=page.replace('CATEGORIES',''.join(f'<option value="{a["id"]}">{a["id"]} — {esc(a["title"])}</option>' for a in AREAS))
page=page.replace('AREAS',''.join(f'<option>{esc(a)}</option>' for a in sorted({d['area'] for d in LIBRARY})))
page=page.replace('CARDS','\n'.join(cards))
(ROOT/'index.html').write_text(page)
print(json.dumps(stats,ensure_ascii=False,indent=2))
