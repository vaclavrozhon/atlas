# TCS: rozšířený katalog výzkumných otázek

Sestaveno 2026-09-09. **4,695 záznamů v 43 oblastech**, 4,043 zdrojových dokumentů. Přibylo 3,692 záznamů. ID původních 1 003 položek zůstala zachována.

## Co přesně znamená počet

- **1,003** záznamů z původního katalogu.
- **135** nových ručně vybraných a přeformulovaných zadání z knih, monografií a survey.
- **3,557** nových automaticky vybraných otázek ze stejných počtů různých konferenčních článků. Každá má krátký úryvek, název článku a odkaz na stránku PDF.

**Aktuální otevřenost většiny záznamů nebyla individuálně ověřena.** Automatická část je rešeršní index kandidátů: filtr hledal číslované otevřené otázky, explicitně nevyřešená tvrzení a otázky v závěrech. I po filtraci mohou zůstat chyby interpretace, neúplná matematická sazba, překryvy a otázky vyřešené po vydání zdroje. Počet záznamů proto není certifikovaný počet nezávislých problémů otevřených k 2026-09-09.

Původních 30 rodin problémů zůstává označeno `problem_family`. Automatická položka označuje jednu vybranou zdrojovou pasáž; pasáž může formulovat více souvisejících variant. Obtížnost menších úloh nebyla odhadována. `focused` neznamená snadný problém.

## Jak katalog používat

Otevřete **[catalog.html](catalog.html)**: funguje lokálně bez serveru, umožňuje hledání, filtrování podle oblasti, roku, způsobu zpracování a typu zdroje a export výběru. U automatického záznamu čtěte společně úryvek a název článku. `[…]` značí zkrácení; plná otázka, definice a kvantifikátory jsou na uvedené stránce zdroje.

- [Excel](tcs-open-problems.xlsx): listy Start, Catalog, Areas, Sources a Excluded.
- [CSV](catalog.csv) a [JSON](catalog.json): úplná strukturovaná data.
- [Markdown](catalog.md): celý seznam rozdělený podle oblastí.
- [Zdroje](sources.csv), [prohledané knihy a survey](consulted_books_surveys.csv), [prohledané sborníky](consulted_conferences.csv).
- [Vyřazené položky](excluded.csv), [automatický filtr](screening_audit.csv), [možné textové překryvy](possible_overlaps.csv), [validace](validation.json).

## Rozsah rešerše a výběr

Prohledáno 328 konferenčních svazků a 16,492 dostupných textů článků, dále 111 knih, monografií, survey a sbírek. Ručně zpracované doplnění čerpá ze 14 z těchto zdrojů; ne každý prohledaný zdroj přinesl použitelný záznam. Výběr zvýhodňuje veřejně dostupné zdroje LIPIcs, PMLR, ECCC a autorské kopie. Není to úplná ani rovnoměrná bibliografie TCS; sborníky STOC, FOCS, SODA a kryptografických konferencí nebyly plošně vytěženy.

Zachyceny konferenční řady: ALT, APPROX/RANDOM, CALCO, CCC, COLT, CONCUR, CPM, CSL, DISC, ESA, FSCD, FSTTCS, FUN, GD, ICALP, ICDT, IPEC, ISAAC, ITC, ITCS, MFCS, OPODIS, SAND, SAT, SEA, STACS, SWAT, SoCG, TIME, TQC, TYPES, WABI, WADS.

Z jednoho konferenčního článku se automaticky přidává nejvýše jedna položka, bez rozdělování parametrů na umělé varianty. Krátké citace mají nejvýše 25 slov na článek. Automaticky se odstraňují zjevné důkazy, řešené otázky, pouhé odkazy na otázky, obecné agendy a přesná opakování; 0 téměř shodných formulací bylo sloučeno. Matematická deduplikace napříč odlišnými formulacemi není dokončena. `possible_overlaps.csv` zaznamenává zbývající silnější textové podobnosti.

## Evidence a data

`review_level` rozlišuje převzatý index, ruční práci se zadáním a automatický výběr. Žádná z těchto hodnot sama nepotvrzuje dnešní otevřenost. `status` a `status_note` tuto nejistotu zachovávají. Rok znamená rok citované verze nebo sborníku, nikoli nutně rok položení otázky. U nedatovaného rukopisu zůstává prázdný.

`source_locator` uvádí číslo otázky nebo umístění pasáže a stránku PDF; PDF stránka se může lišit od tištěného číslování. `selection_method` a `extraction_flags` umožňují audit automatického výběru. Zařazení automatických položek do oblastí je heuristické; článek může zasahovat do více oblastí.

Při dílčí kontrole aktualizací byly vyřazeny mimo jiné některé staré otázky o citlivosti booleovských funkcí, faktorizaci formulí, property testingu a férovém rozdělování. Audit rozlišuje vyřešené položky od duplicit a nedostatečně určitých kandidátů. Nová správná bibliografická adresa ještě neznamená ověření současného stavu matematické otázky.

Zdrojové PDF a úplné vytěžené texty jsou v místní pracovní cache, nejsou součástí exportního ZIP. Skripty v sousedním adresáři `expand/` zachovávají postup sběru, výběru, ruční rozhodnutí a tvorbu výstupu. Původní katalog je v `output-v1-1003/`.
