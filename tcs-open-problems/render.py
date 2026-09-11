from pathlib import Path
import json,html,collections
ROOT=Path(__file__).resolve().parent;OUT=ROOT/'output'
rows=json.loads((OUT/'catalog.json').read_text());meta=json.loads((OUT/'metadata.json').read_text())
N=meta['entry_count'];A=meta['area_count'];S=meta['distinct_source_documents']
page=r'''<!doctype html>
<html lang="cs"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Open questions across TCS · __N__ položek</title>
<style>
:root{--ink:#142b3d;--muted:#526675;--line:#dce4e9;--blue:#0b6380;--paper:#f4f7f9;--gold:#b87512}*{box-sizing:border-box}body{margin:0;font-family:system-ui,-apple-system,Segoe UI,sans-serif;color:var(--ink);background:var(--paper);line-height:1.5}a{color:var(--blue);text-decoration-thickness:1px;text-underline-offset:3px}header{background:#142b3d;color:white;padding:46px max(24px,calc((100vw - 1250px)/2));}header a{color:#a8e4ee}.eyebrow{font-size:12px;letter-spacing:.13em;text-transform:uppercase;color:#a5c4d5}h1{font-size:clamp(28px,4vw,46px);line-height:1.14;letter-spacing:-.04em;margin:14px 0 16px;font-weight:680}header p{max-width:790px;color:#d4e2eb;margin:0}.metrics{display:flex;gap:42px;margin:26px 0 0}.metric b{display:block;font-size:27px;font-weight:600}.metric span{font-size:12px;color:#a5c4d5}main{max-width:1300px;margin:auto;padding:26px 24px 50px}.notice{background:#fff8e9;border-left:4px solid #d7982e;padding:14px 18px;font-size:14px;margin-bottom:24px}.notice strong{font-weight:650}.downloads{display:flex;gap:20px;flex-wrap:wrap;font-size:14px;margin:18px 0 0}.controls{background:white;border:1px solid var(--line);border-radius:10px;padding:18px;display:grid;grid-template-columns:2fr 1.6fr 1fr 1fr;gap:15px}label{display:block;font-size:12px;font-weight:650;color:var(--muted);margin-bottom:6px}input,select,button{font:inherit}input,select{width:100%;padding:10px;border:1px solid #b9cbd5;border-radius:6px;background:white;color:var(--ink);height:44px}input:focus,select:focus,button:focus-visible,a:focus-visible{outline:3px solid #9ad6e4;outline-offset:2px}.resultsbar{display:flex;align-items:center;justify-content:space-between;margin:22px 0 12px;gap:12px;font-size:14px}.resultsbar span{color:var(--muted)}button{padding:7px 13px;background:white;border:1px solid #bacbd4;border-radius:6px;color:var(--ink);cursor:pointer}button:hover{background:#e8f2f5}button:disabled{opacity:.4;cursor:default}article{display:grid;grid-template-columns:100px 1fr;gap:16px;padding:22px 24px;background:white;border:1px solid var(--line);margin:0 0 10px;border-radius:8px}.identifier{font-size:12px;color:#667c8b;font-variant-numeric:tabular-nums}.year{font-size:20px;color:var(--ink);margin:7px 0 9px}.badge{font-size:10px;border:1px solid #c7dce4;border-radius:4px;padding:3px 5px;display:inline-block}.landmark{color:#935b07;border-color:#dfc790;background:#fff9ec}article h2{font-size:18px;line-height:1.4;margin:0 0 7px;font-weight:640}article h2 a{text-decoration:none;color:var(--ink)}article h2 a:hover{text-decoration:underline}.area{font-size:12px;color:var(--blue);font-weight:600;margin:0 0 12px}.citation{font-size:12px;color:var(--muted)}.citation .location{display:block;margin:4px 0 7px}.links{display:flex;gap:20px;font-size:12px}.pager{display:flex;align-items:center;gap:16px;justify-content:center;padding:20px}footer{font-size:12px;color:var(--muted);margin:20px 0;border-top:1px solid var(--line);padding-top:20px}details{background:white;border:1px solid var(--line);padding:14px 18px;border-radius:8px;margin-bottom:24px;font-size:13px}summary{cursor:pointer;font-weight:600}.areas{display:grid;grid-template-columns:1fr 1fr;gap:7px 28px;margin-top:16px}.area-count{display:flex;justify-content:space-between;gap:10px;border-bottom:1px solid #edf1f4;padding:5px 0}.empty{text-align:center;padding:45px;color:var(--muted)}.status{font-size:11px;color:#6c7d88;margin-top:9px}@media(max-width:850px){.controls{grid-template-columns:1fr 1fr}.areas{grid-template-columns:1fr}}@media(max-width:550px){header{padding:30px 20px}main{padding:20px 12px}.controls{grid-template-columns:1fr}article{grid-template-columns:64px 1fr;gap:12px;padding:18px 14px}.metrics{gap:24px}.resultsbar{align-items:flex-start;flex-direction:column}.year{font-size:17px}article h2{font-size:16px}}
</style></head><body>
<header><div class="eyebrow">Výzkumný rozcestník · 9. září 2026</div><h1>Open questions across TCS</h1><p>Velké conjectures i úzce vymezené technické otázky. Stručné názvy, oborové filtry a odkazy na úplná zadání v primárních zdrojích.</p><div class="metrics"><div class="metric"><b>__N__</b><span>citovaných položek</span></div><div class="metric"><b>__A__</b><span>tematických kategorií</span></div><div class="metric"><b>__S__</b><span>zdrojových dokumentů a stránek</span></div></div><nav class="downloads"><a href="tcs-open-problems.xlsx">Excel</a><a href="catalog.csv">CSV</a><a href="catalog.json">JSON</a><a href="README.md">Metodika a omezení</a></nav></header>
<main>
<div class="notice"><strong>Jak číst označení „open“:</strong> většinu otázek uvádí jako otevřené citovaný zdroj. Jejich stav nebyl jednotlivě a vyčerpávajícím způsobem ověřen k dnešku. Zachycená řešení a duplicity jsou vyřazeny; starší záznamy vyžadují kontrolu navazující literatury. Rok označuje zdroj nebo seminář.</div>
<details><summary>Tematické rozložení a rozsah položek</summary><p>„Konkrétní“ je vymezené zadání; „skupina otázek“ zachovává související otázky sdružené ve zdroji. „Velká otázka“ označuje obecný problém, nikoli odhad obtížnosti. __FAMILY__ položek je označeno jako skupina otázek. Úplná matematická definice je vždy v odkazovaném zdroji.</p><div class="areas" id="areas"></div></details>
<div class="controls"><div><label for="search">Název, pojem, autor nebo ID</label><input id="search" type="search" placeholder="Např. automata, Frege, treewidth…" autocomplete="off"></div><div><label for="area">Oblast</label><select id="area"><option value="">Všechny oblasti</option></select></div><div><label for="year">Zdroj nejdříve od</label><select id="year"><option value="">Všechny roky</option><option>2026</option><option>2025</option><option>2023</option><option>2020</option><option>2015</option><option>2010</option></select></div><div><label for="scope">Rozsah otázky</label><select id="scope"><option value="">Všechny</option><option value="landmark">Velké otázky</option><option value="focused">Konkrétní otázky</option><option value="problem_family">Skupiny otázek</option></select></div></div>
<div class="resultsbar"><div id="count" aria-live="polite"></div><div><button id="reset">Zrušit filtry</button> <button id="export">CSV výběru</button></div></div>
<section id="results" aria-label="Výsledky"></section><div class="pager"><button id="prev">← Předchozí</button><span id="page"></span><button id="next">Další →</button></div>
<footer>Samostatný soubor fungující offline; odkazy na články vyžadují internet. Data: <a href="catalog.json">JSON</a> · <a href="sources.csv">zdroje</a> · <a href="excluded.csv">audit vynechaných kandidátů</a>. Nejistá aktuálnost je vlastnost celého souboru, nikoli známka, že některá otázka byla ověřena jako vyřešená.</footer>
</main><script id="data" type="application/json">__DATA__</script><script>
'use strict';
const data=JSON.parse(document.getElementById('data').textContent), $=id=>document.getElementById(id), esc=s=>String(s||'').replace(/[&<>"']/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c])), fold=s=>String(s).normalize('NFD').replace(/[\u0300-\u036f]/g,'').toLowerCase();
const areas=[...new Set(data.map(x=>x.area))].sort(),counts={};for(const x of data)counts[x.area]=(counts[x.area]||0)+1;
for(const a of areas){let o=document.createElement('option');o.value=a;o.textContent=a+' ('+counts[a]+')';$('area').append(o)}
$('areas').innerHTML=areas.map(a=>'<div class="area-count"><span>'+esc(a)+'</span><b>'+counts[a]+'</b></div>').join('');
const scopes={landmark:'Velká otázka',focused:'Konkrétní',problem_family:'Skupina otázek'};let filtered=data,page=0;const size=40;
function filter(){const q=fold($('search').value).split(/\s+/).filter(Boolean),area=$('area').value,year=$('year').value,scope=$('scope').value;filtered=data.filter(x=>(!area||x.area===area)&&(!year||Number(x.source_year)>=Number(year))&&(!scope||x.scope===scope)&&q.every(s=>fold([x.id,x.title,x.area,x.authors,x.source_collection,x.source_locator,x.source_title].join(' ')).includes(s)));page=0;render()}
function render(){const pages=Math.max(1,Math.ceil(filtered.length/size)),start=page*size;let segment=filtered.slice(start,start+size);$('count').innerHTML='<strong>'+filtered.length+' položek</strong> <span>z '+data.length+' · '+(filtered.length?start+1:0)+'–'+(start+segment.length)+'</span>';$('results').innerHTML=segment.map(x=>'<article id="'+esc(x.id)+'"><div class="identifier">'+esc(x.id)+'<div class="year">'+esc(x.source_year||'—')+'</div><span class="badge '+(x.scope==='landmark'?'landmark':'')+'">'+esc(scopes[x.scope])+'</span></div><div><h2><a href="'+esc(x.source_url)+'" target="_blank" rel="noopener">'+esc(x.title)+'</a></h2><p class="area">'+esc(x.area)+'</p><div class="citation">'+esc(x.source_collection)+(x.authors?' · '+esc(x.authors):'')+'<span class="location">'+esc(x.source_locator)+'</span></div><div class="links"><a href="'+esc(x.source_url)+'" target="_blank" rel="noopener">Úplné zadání ve zdroji ↗</a>'+(x.pdf_url?'<a href="'+esc(x.pdf_url)+'" target="_blank" rel="noopener">PDF / příslušná strana ↗</a>':'')+'</div><div class="status">'+(x.status==='maintainer_lists_open'?'Správce problému jej aktuálně vede jako otevřený.':'Otevřené podle zdroje; pozdější stav není plošně ověřen.')+'</div></div></article>').join('')||'<p class="empty">Tomuto filtru neodpovídá žádná položka.</p>';$('page').textContent=(page+1)+' / '+pages;$('prev').disabled=page===0;$('next').disabled=page>=pages-1}
for(const id of ['search','area','year','scope'])$(id).addEventListener(id==='search'?'input':'change',filter);
$('prev').onclick=()=>{page--;render();$('count').scrollIntoView({block:'start'})};$('next').onclick=()=>{page++;render();$('count').scrollIntoView({block:'start'})};$('reset').onclick=()=>{for(const id of ['search','area','year','scope'])$(id).value='';filter()};
$('export').onclick=()=>{const cols=['id','title','area','scope','source_year','status','source_collection','source_locator','authors','source_url','pdf_url'],quote=s=>'"'+String(s||'').replace(/"/g,'""')+'"',csv='\ufeff'+[cols,...filtered.map(x=>cols.map(k=>x[k]))].map(r=>r.map(quote).join(',')).join('\r\n'),u=URL.createObjectURL(new Blob([csv],{type:'text/csv;charset=utf-8'})),a=document.createElement('a');a.href=u;a.download='tcs-selection.csv';a.click();setTimeout(()=>URL.revokeObjectURL(u),1000)};render();
</script></body></html>'''
for k,v in {'__N__':N,'__A__':A,'__S__':S,'__FAMILY__':meta['scope_counts']['problem_family'],'__DATA__':json.dumps(rows,ensure_ascii=False).replace('</',r'<\/')}.items():page=page.replace(k,str(v))
(OUT/'catalog.html').write_text(page)
readme=f'''# Otevřené výzkumné otázky napříč TCS

**{N} citovaných položek · {A} tematických kategorií · {S} zdrojových dokumentů a stránek.** Sestaveno 9. září 2026.

- [Prohledávatelný katalog](catalog.html) — vyhledávání, oblast, rok, rozsah otázky a export výběru.
- [Excel](tcs-open-problems.xlsx) — katalog, tematické počty, zdroje a audit vynechaných kandidátů.
- [CSV](catalog.csv) a [JSON](catalog.json) — stejné záznamy pro další zpracování.

Katalog obsahuje P vs NP, NP vs coNP, P vs BPP, L vs NL, VP vs VNP, Unique Games, silně polynomiální lineární programování, ale i jednotlivé otázky o datových strukturách, automatech, rekonstrukci sítí, přepisování, fair division a mnoha dalších tématech. Názvy jsou převážně anglicky, aby šly snadno dohledávat v literatuře.

## Co přesně znamená „otevřené“

Jde o **zdrojový katalog kandidátů na otevřené výzkumné problémy**, nikoli o {N} problémů s individuálně garantovanou otevřeností k dnešku. U většiny položek bylo ověřeno, že je příslušný odborný zdroj předkládá jako otevřené. Vybrané aktuální výsledky a poznámky o řešeních byly zkontrolovány, nikoli však veškerá navazující literatura ke každé položce. Vyhledávání může minout řešení pod jiným názvem nebo v neveřejném rukopisu.

`source_open_unverified` označuje otevřenost podle citovaného zdroje a neúplnou kontrolu pozdějšího stavu. `maintainer_lists_open` znamená, že správce problému jej při přístupu stále uváděl jako otevřený. Datum `accessed` je datum přístupu, **nikoli datum důkazu otevřenosti**. `source_year` je rok zdroje, aktualizace uvedené stránky, semináře nebo data otázky uvedeného v RTA; přesný význam rozlišuje `year_basis`; u Dagstuhlu se může lišit od pozdějšího vydání zprávy. Prázdný rok nebyl bezpečně zjištěn.

## Jak vznikl výběr

Výběr vychází z jednotlivých stránek Automata Exchange, Sublinear.info, The Open Problems Project a RTA; z otevřených otázek publikovaných v COLT/PMLR, SIGACT, Dagstuhl Reports a PACS; a z výzkumných seznamů 0xPARC, Jukky Suomely, Antoina Amarilliho a TCS Open Problems. Základní otázky doplňuje Wigdersonův rukopis a Aaronsonův přehled kvantové dotazové složitosti. Konkrétní odkazy a lokátory jsou přímo u každé položky a v [inventáři zdrojů](sources.csv).

Stažení a vyhledání oddílů v PDF bylo automatizováno; výběr byl poté kontrolován podle názvů, lokátorů, zdrojových poznámek o řešeních a cíleného dohledávání. Generické aplikované agendy a zachycené vyřešené otázky byly vynechány. [Audit obsahuje {meta['excluded_count']} vynechaných kandidátů](excluded.csv), včetně duplicit a nejistých formulací. Není to seznam {meta['excluded_count']} vyřešených problémů.

Například byly vyřazeny dvě již vyřešené otázky o kvantových oracle separacích, původní single-pass matching bariéra, Min-2-Lin nad Z₄, Even Set, dvoutokenová conjecture pro parity automaty a stará otázka existence fair convex partitions. Audit uvádí podpůrné zdroje tam, kde byly dohledány.

## Co počítá jeden řádek

- **{meta['scope_counts']['landmark']} `landmark`**: obecné významné otázky; toto označení není spolehlivý odhad obtížnosti.
- **{meta['scope_counts']['focused']} `focused`**: konkrétní zadání nebo vymezená otázka ve zdroji.
- **{meta['scope_counts']['problem_family']} `problem_family`**: zdrojem sdružená skupina souvisejících otázek.

Počet řádků není počet logicky nezávislých conjectures. Některá zadání mají podotázky; různé výpočetní modely mohou dávat samostatné otázky. Nebyl generován kartézský součin variant, aby se dosáhlo počtu. Odstraněny byly zachycené duplicity, ale úplná sémantická deduplikace není garantována. Tematické kategorie slouží k navigaci a nejsou jednotně široké; například jedna velmi obecná otázka může spadat do více oborů, zatímco řádek má jednu hlavní kategorii.

Název je **stručný indexový popis**, někdy upravený oproti původnímu nadpisu. Úplné matematické formulace, předpoklady, kvantifikátory a definice jsou ve zdroji, na místě `source_locator`. Zvlášť u starších a úzce technických problémů je toto místo nezbytnou součástí záznamu. Pro výběr vlastního projektu začněte novějšími zdroji a ověřte konkrétní variantu v navazujících publikacích.

## Soubory

`catalog.html` funguje offline a nepotřebuje instalaci. Internet je potřeba pro otevření externích zdrojů. CSV používají UTF-8 s BOM; JSON používá UTF-8. Každá položka má stabilní ID v rámci tohoto vydání. Všechny formáty obsahují stejný výběr; `metadata.json` obsahuje strojově čitelné počty. `sources.*` obsahují zdroje a `excluded.*` audit.
'''
(OUT/'README.md').write_text(readme)
# A readable plain-text fallback, preserving links and exact locators.
lines=[f'# TCS: {N} zdrojově doložených výzkumných otázek','', 'Otevřenost převážně podle citovaného zdroje; aktuální stav není plošně ověřen. Viz [metodika](README.md).','']
for area in sorted(set(x['area'] for x in rows)):
 lines+=['## '+area,'']
 for x in rows:
  if x['area']!=area:continue
  lines += [f"- **{x['id']}** [{x['title']}]({x['source_url']}) — {x['source_year'] or 'rok neuveden'}; {x['source_locator']}; `{x['scope']}`."]
 lines+=['']
(OUT/'catalog.md').write_text('\n'.join(lines))
print('Rendered HTML, README, Markdown')
