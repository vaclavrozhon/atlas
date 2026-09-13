**Publication update — 10 September 2026:** The retained proposals below have now been added to the atlas as source-linked short drafts, following the user’s approval. The original research and novelty checks below describe the pre-publication stage. See publication manifest.

**Druhé hledání: tři další zásadní problémy — 10. září 2026**

Zadání „ještě 0–5“ je zde vyloženo jako nejvýše pět dalších celkem. Vybrány jsou tři; původní návrh pro velké kategorie se rozšiřuje z 69 na 72.

Tentokrát byla výchozím bodem výzkumná agenda: program Simons Institute, odborné přednášky o network coding a dlouhodobá překážka derandomizace základních datových struktur. Následovalo dohledání přesné otázky, novější literatury a kontrola celého katalogu i obou dřívějších seznamů návrhů.

Za nejsilnější přídavky považuji první dvě položky. Slovník zařazuji jako klasický základní problém datových struktur; toto hodnocení významnosti je redakční úsudek.

**The Li–Li undirected network coding conjecture — velká kategorie 7**

Zvyšuje síťové kódování dosažitelnou propustnost neorientované kapacitní sítě s několika nezávislými unicast přenosy? Li–Li conjecture tvrdí, že každou asymptoticky dosažitelnou kombinaci rychlostí lze dosáhnout také frakčním multikomoditním směrováním. Kapacita hrany je společná oběma směrům; uzly smějí při kódování zprávy obecně kombinovat.

Základní otázka, zda výpočty uvnitř komunikační sítě poskytují výhodu oproti přeposílání informace. Hypotéza pochází z roku 2004 a má také aplikace v dolních mezích pro výpočet.

ISIT 2025, On the Capacity of Undirected Multiple Unicast Layered Networks with Asymmetric Demands, výslovně uvádí, že hypotéza je potvrzena pouze pro několik sítí a tříd sítí; nový výsledek opět řeší speciální případy.

TCS-0247 je Q13 v SIGACT sloupku o Kolmogorovově složitosti: vztah Shannonova a algoritmického informačního toku, nikoli kódování versus routing. Původní Q13 byl přečten. TCS-4610 se týká kvantových výpočtů pomocí měření. V předchozích 69 velkých ani 72 malých návrzích není Li–Li. Multicast a orientované sítě nejsou touto hypotézou pokryty. Zařazení do velké 7 je redakční volba; přirozený přesah je Coding and information theory.

Cesta přes Chekuriho přednášku o vlivu network coding a přednášku Elaine Shi o dolních mezích pro třídicí obvody; následně primární formulace a novější ISIT práce.

Podklady: [zdroj 1](https://ics.uci.edu/~vazirani/isit.pdf), [zdroj 2](https://ieeexplore.ieee.org/document/11195643/), [zdroj 3](https://chekuri.cs.illinois.edu/talks/DIMACS-netcoding.pdf), [zdroj 4](https://ntt-research.com/cis-elaine-shi-2020summit-transcript/).

**Nearly linear-time solution of general sparse linear systems — velká kategorie 10**

Lze obecnou nesingulární soustavu Ax=b s n proměnnými a m nenulovými koeficienty řešit s relativním reziduem ||Ax-b||₂ ≤ ε||b||₂ v čase m·polylog(nκ/ε), kde κ je číslo podmíněnosti? Konkrétní cílový režim má racionální vstupy s O(log n) bity, κ ≤ poly(n) a ε = 1/poly(n); započítává se práce s konečnou přesností a výstupem je celý aproximující vektor.

Ústřední hranice algoritmické numerické lineární algebry, s dopadem na optimalizaci a vědecké výpočty. Téměř lineární řešiče speciálních tříd matic neposkytují takový algoritmus pro obecné řídké soustavy.

Formulace je redakční konkretizace velké otázky složitosti obecných řídkých soustav, nikoli citovaná pojmenovaná hypotéza ani příslib kladné odpovědi. Peng–Vempala vymezuje režim konečné přesnosti a podmíněnosti; Simons workshop 2025 a souhrn arXiv:2602.05394v3 ze srpna 2026 dokumentují pokračující výzkumný program.

TCS-6120 po přečtení původní strany 6 řeší vliv vložitelnosti simpliciálního komplexu do R³ na rychlost řešiče; obecný problém se tím neduplikuje. TCS-0046 řeší tropické/min-plus soustavy, odlišnou algebru. Kontrolovány také oba předchozí návrhy. Překonání času násobení matic již vyřešili Peng a Vempala: není zde navrhováno jako otevřená otázka.

Cesta přes program Simons Institute Complexity and Linear Algebra a workshop Linear Systems and Eigenvalue Problems, následně původní algoritmická práce a redukce úplnosti.

Podklady: [zdroj 1](https://arxiv.org/abs/2007.10254), [zdroj 2](https://arxiv.org/abs/2602.05394), [zdroj 3](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.ICALP.2022.53), [zdroj 4](https://simons.berkeley.edu/workshops/linear-systems-eigenvalue-problems).

**Deterministic linear-time construction of static dictionaries — velká kategorie 4**

Lze ze seznamu n různých celočíselných klíčů deterministicky v O(n) čase zkonstruovat statický slovník s O(n) slovy paměti a O(1) nejhorším časem dotazu na členství a přidružená data? Uvažujme standardní word-RAM s w = Θ(log n), aritmetikou včetně násobení a bitovými operacemi; příprava datové struktury se započítává do času.

Klasická otázka, zda náhodnost přináší nezbytnou výhodu už při konstrukci jedné z nejzákladnějších datových struktur. Náhodné konstrukce optimálního očekávaného lineárního času známe; obecné deterministické konstrukce mají stále režii.

Základní deterministické konstrukce: Hagerup–Miltersen–Pagh a Ružić (ICALP 2008). Novější práce Internal Pattern Matching Queries in a Text and Applications používá deterministické statické slovníky s časem konstrukce O(n(log log n)²); CPM 2026 také stále uvádí zpomalení při nahrazení náhodného hashování deterministickými slovníky. Tyto práce nejsou samotným navrhovaným problémem.

TCS-1730 řeší praktickou rychlost MPHF blízko informační mezi; TCS-2389 learned monotone hashing v praxi; TCS-4997 explicitní konstrukce speciálních disperserů pro neadaptivní cell-probe model; TCS-4910 selhání rodin hashovacích funkcí s omezeným náhodným popisem. Žádná není obecná deterministická konstrukce statického slovníku. Předchozí návrh integer-sort požaduje třídění, nikoli O(1) dotazy slovníku. Není ani v návrhu pro malé kategorie.

Cesta přes historický program derandomizace hashování a přes to, jakou základní překážku uvádějí současné algoritmy jako cenu použití deterministického slovníku.

Podklady: [zdroj 1](https://www.brics.dk/RS/99/48/BRICS-RS-99-48.pdf), [zdroj 2](https://doi.org/10.1007/978-3-540-70575-8_8), [zdroj 3](https://epubs.siam.org/doi/10.1137/23M1567618), [zdroj 4](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.CPM.2026.25).

**Kontrola překryvů**

Kromě katalogu byly přečteny názvy a formulace všech 69 předchozích velkých a 72 malých návrhů. Nejbližší zdrojové pasáže TCS-0247 (Q13, PDF str. 14) a TCS-6120 (PDF str. 6) byly otevřeny a odlišeny podle otázky. Slovníkové shody byly posouzeny podle modelu a požadované záruky. Automatické shody uchovává aktualizovaný `novelty-audit.json`; nejsou automatickým důkazem duplicity ani novosti.

[Aktualizovaný společný report](REPORT.md) obsahuje všechny návrhy. Do veřejného katalogu toto hledání nové karty nepřidává.
