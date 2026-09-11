# Otevřené výzkumné otázky napříč TCS

**1003 citovaných položek · 41 tematických kategorií · 472 zdrojových dokumentů a stránek.** Sestaveno 9. září 2026.

- [Prohledávatelný katalog](catalog.html) — vyhledávání, oblast, rok, rozsah otázky a export výběru.
- [Excel](tcs-open-problems.xlsx) — katalog, tematické počty, zdroje a audit vynechaných kandidátů.
- [CSV](catalog.csv) a [JSON](catalog.json) — stejné záznamy pro další zpracování.

Katalog obsahuje P vs NP, NP vs coNP, P vs BPP, L vs NL, VP vs VNP, Unique Games, silně polynomiální lineární programování, ale i jednotlivé otázky o datových strukturách, automatech, rekonstrukci sítí, přepisování, fair division a mnoha dalších tématech. Názvy jsou převážně anglicky, aby šly snadno dohledávat v literatuře.

## Co přesně znamená „otevřené“

Jde o **zdrojový katalog kandidátů na otevřené výzkumné problémy**, nikoli o 1003 problémů s individuálně garantovanou otevřeností k dnešku. U většiny položek bylo ověřeno, že je příslušný odborný zdroj předkládá jako otevřené. Vybrané aktuální výsledky a poznámky o řešeních byly zkontrolovány, nikoli však veškerá navazující literatura ke každé položce. Vyhledávání může minout řešení pod jiným názvem nebo v neveřejném rukopisu.

`source_open_unverified` označuje otevřenost podle citovaného zdroje a neúplnou kontrolu pozdějšího stavu. `maintainer_lists_open` znamená, že správce problému jej při přístupu stále uváděl jako otevřený. Datum `accessed` je datum přístupu, **nikoli datum důkazu otevřenosti**. `source_year` je rok zdroje, aktualizace uvedené stránky, semináře nebo data otázky uvedeného v RTA; přesný význam rozlišuje `year_basis`; u Dagstuhlu se může lišit od pozdějšího vydání zprávy. Prázdný rok nebyl bezpečně zjištěn.

## Jak vznikl výběr

Výběr vychází z jednotlivých stránek Automata Exchange, Sublinear.info, The Open Problems Project a RTA; z otevřených otázek publikovaných v COLT/PMLR, SIGACT, Dagstuhl Reports a PACS; a z výzkumných seznamů 0xPARC, Jukky Suomely, Antoina Amarilliho a TCS Open Problems. Základní otázky doplňuje Wigdersonův rukopis a Aaronsonův přehled kvantové dotazové složitosti. Konkrétní odkazy a lokátory jsou přímo u každé položky a v [inventáři zdrojů](sources.csv).

Stažení a vyhledání oddílů v PDF bylo automatizováno; výběr byl poté kontrolován podle názvů, lokátorů, zdrojových poznámek o řešeních a cíleného dohledávání. Generické aplikované agendy a zachycené vyřešené otázky byly vynechány. [Audit obsahuje 146 vynechaných kandidátů](excluded.csv), včetně duplicit a nejistých formulací. Není to seznam 146 vyřešených problémů.

Například byly vyřazeny dvě již vyřešené otázky o kvantových oracle separacích, původní single-pass matching bariéra, Min-2-Lin nad Z₄, Even Set, dvoutokenová conjecture pro parity automaty a stará otázka existence fair convex partitions. Audit uvádí podpůrné zdroje tam, kde byly dohledány.

## Co počítá jeden řádek

- **37 `landmark`**: obecné významné otázky; toto označení není spolehlivý odhad obtížnosti.
- **936 `focused`**: konkrétní zadání nebo vymezená otázka ve zdroji.
- **30 `problem_family`**: zdrojem sdružená skupina souvisejících otázek.

Počet řádků není počet logicky nezávislých conjectures. Některá zadání mají podotázky; různé výpočetní modely mohou dávat samostatné otázky. Nebyl generován kartézský součin variant, aby se dosáhlo počtu. Odstraněny byly zachycené duplicity, ale úplná sémantická deduplikace není garantována. Tematické kategorie slouží k navigaci a nejsou jednotně široké; například jedna velmi obecná otázka může spadat do více oborů, zatímco řádek má jednu hlavní kategorii.

Název je **stručný indexový popis**, někdy upravený oproti původnímu nadpisu. Úplné matematické formulace, předpoklady, kvantifikátory a definice jsou ve zdroji, na místě `source_locator`. Zvlášť u starších a úzce technických problémů je toto místo nezbytnou součástí záznamu. Pro výběr vlastního projektu začněte novějšími zdroji a ověřte konkrétní variantu v navazujících publikacích.

## Soubory

`catalog.html` funguje offline a nepotřebuje instalaci. Internet je potřeba pro otevření externích zdrojů. CSV používají UTF-8 s BOM; JSON používá UTF-8. Každá položka má stabilní ID v rámci tohoto vydání. Všechny formáty obsahují stejný výběr; `metadata.json` obsahuje strojově čitelné počty. `sources.*` obsahují zdroje a `excluded.*` audit.
