> Follow-up, 11 September 2026: five GPT proposals have now been added in the [approved ten-card batch](../gpt-claude-additions-20260911/README.md). The original M16 recommendation is corrected: [Dughmi, ITCS 2022](https://drops.dagstuhl.de/storage/00lipics/lipics-vol215-itcs2022/LIPIcs.ITCS.2022.58/LIPIcs.ITCS.2022.58.pdf) proves the Matroid Secretary/contention-resolution equivalence in the specified known-matroid random-order setting. A separate Matroid Secretary card was therefore not added; Asser’s problem was selected instead. Counts below preserve the earlier audit snapshot.

# Posouzení 65 návrhů GPT – 11. září 2026

**Doporučuji 18 nových samostatných karet.** Další návrhy jsou již přítomné, vyžadují dopracování zdrojového záznamu, nebo představují variantu či podproblém existující karty. Jediný návrh níže odmítám jako otevřený kvůli zveřejněnému řešení. Katalog ani jeho pořadí jsem touto analýzou nezměnil.

Pořadí je převzaté z publikovaného katalogu verze fd120cf309580f1f58b2 (11. září 2026, 09:12 UTC). Přehled zohledňuje nově vzniklý bucket Online algorithms i přesun d-DNNF do Automated reasoning and unification. Pro velké buckety značí zvýraznění top5, pro malé top2. U záznamu v jiném bucketu uvádím skutečný bucket a jeho pořadí, nikoli domnělé umístění v navržené kategorii. **Zdrojový záznam** znamená `source` nebo `index`, nikoli hotovou, plně rozepsanou kartu. Příbuzná karta se nepočítá jako přesná shoda.

Kontrola srovnává tituly, vlastní formulace, zdrojové úryvky a relevantní zdroje. Otevřenost a varianty jsem zvlášť ověřoval u kandidátů na přidání a u podezřelých nových výsledků; samotné přítomnosti starého zdrojového záznamu nepřisuzuji novou záruku aktuální otevřenosti.

## Co přidat

| Návrh | Problém | Doporučený bucket | Proč |
|---|---|---|---|
| V2.4 | Jednotkové vzdálenosti: prolomit exponent 4/3 | Computational geometry and metric spaces | Důležitý chybějící problém incidencí. [Zdroj](https://arxiv.org/abs/2605.20579). |
| V4.2 | Deterministické lineární třídění integerů | Algorithms & data structures | Deterministický cíl se skutečně liší od dosavadního randomizovaného. [Zdroj](https://www.cs.cmu.edu/~15451-f24/lectures/lecture03-slides.pdf). |
| V4.3 | Přesný maximální tok v m polylog n | Algorithms & data structures | Centrální grafový algoritmus; konkrétní zbývající časová bariéra. [Zdroj](https://arxiv.org/abs/2608.17384). |
| V5.4 | Minimax regret stochastického BCO | Online algorithms | Doplní statistickou cenu omezené zpětné vazby. [Zdroj](https://arxiv.org/abs/2607.18652). |
| V6.1 | Dohoda na klíči z OWF | Cryptography | Samostatná otázka minimálních předpokladů pro interaktivní primitivum. [Zdroj](https://eprint.iacr.org/2021/016). |
| V6.4 | Veřejně ověřitelné kvantové peníze z LWE | Cryptography | Doplní veřejnou kvantovou kryptografii založenou na konkrétním předpokladu. [Zdroj](https://arxiv.org/abs/2411.04482). |
| V8.4 | Kvadratické rozpoznávání každého pevného CFL | Automata and formal languages | Základní rozpoznávací problém s přesnou časovou hranicí. [Zdroj](https://arxiv.org/abs/1504.01431). |
| V9.2 | Monniaux: konvexní polyedrické invarianty | Semantics, logic and verification | Důležitá konkrétní hranice automatického hledání invariantů. [Zdroj](https://elefauch.github.io/papers_pdf/monniaux_jour.pdf). |
| V9.4 | Rozhodnutelnost reálného tělesa s exp | Semantics, logic and verification | Velký chybějící problém rozhodnutelnosti matematické teorie. [Zdroj](https://arxiv.org/abs/2603.08365). |
| V10.2 | P-matrix LCP v P | Optimization and numerics | Základní komplementarita mimo již pokryté LP a SDP. [Zdroj](https://ti.inf.ethz.ch/ew/report/2025.html). |
| M10 | Vzorkování (Delta+1)-obarvení | Randomized algorithms and sampling | Odlišuje obecnou existenci sampleru od konkrétního Markovova řetězce. [Zdroj](https://www.tifr.res.in/~piyush.srivastava/docs/LSS20.pdf). |
| M13 | Output-polynomial vertex enumeration | Counting and enumeration | Kanonický problém výstupní složitosti geometrické enumerace. [Zdroj](https://arxiv.org/abs/1404.5584). |
| M14 | Polynomial testing induced-C4-freeness | Property testing and distribution learning | Konkrétní, samostatně studovaná mezera v téměř dokončené klasifikaci pro jeden zakázaný graf. [Zdroj](https://arxiv.org/html/2508.16878v1). |
| M16 | Matroid Secretary conjecture | Online algorithms | Kanonická domněnka random-order online algoritmů. [Zdroj](https://arxiv.org/abs/2608.11413). |
| M17 | Přesný práh náhodného 3-SAT | Constraint satisfaction | Doplní náhodné CSP a přesné fázové přechody. [Zdroj](https://annals.math.princeton.edu/2022/196-1/p01). |
| M18 | Konstantní aditivní gap bin-packing LP | Scheduling and packing | Strukturální LP cíl je odlišný od dosavadní aproximační garance vůči OPT. [Zdroj](https://arxiv.org/abs/1503.08796). |
| M20 | Asserův problém | Database theory and finite model theory | Klasický základní problém konečné modelové teorie. [Zdroj](https://www.cambridge.org/core/journals/bulletin-of-symbolic-logic/article/abs/fifty-years-of-the-spectrum-problem-survey-and-new-results/AA9D145F2390B6CC61F756AA68B039BA). |
| M24 | Feige: refutace náhodného 3-SAT při konstantní hustotě | Beyond worst-case and average-case analysis | Doplní average-case refutation vedle planted clique. [Zdroj](https://www.wisdom.weizmann.ac.il/~feige/mypapers/bwca.pdf). |

## Co nepřidávat jako otevřené

**V10.4: polynomiální růstový faktor úplného pivotování.** Shah a Urschel v preprintu *Entry growth in Gaussian elimination* z 19. srpna 2026 (kontrolována verze v4 z 31. srpna) dokazují kvazipolynomiální worst-case růst. Polynomiální horní mez požadovaná návrhem je tedy podle tohoto výsledku vyvrácená. Záznam by mohl patřit do historie vyřešených problémů, ne mezi nové otevřené karty. [Primární zdroj](https://arxiv.org/abs/2608.19189v4).

## Všech 40 návrhů pro velké oblasti

### 1. Quantum computation

| Problém | Máme? | Záznam a skutečné pořadí | Doporučení |
|---|---|---|---|
| V1.1 Quantum PCP | Ano | TCS-6446, #1 **TOP5** | **Ponechat**. Stejný cíl: konstantní mezera normalizované energie. |
| V1.2 Asymptoticky dobré qLTC | Jen odlišná varianta | TCS-6515, #6 (příbuzná karta) | **Doplnit variantu**. Máme stabilizer qLTC navíc s omezeným počtem kontrol na qubit; obecnější formulaci výslovně odlišit a doplnit ke stejné rodině. |
| V1.3 QMA versus QCMA | Ano | TCS-6448, #10 | **Ponechat**. Bez orákula; kvantový versus klasický svědek. |
| V1.4 Bezpodmínečné klasické ověřování kvantových výpočtů | Ano | TCS-6580, #4 **TOP5** | **Ponechat**. Jeden efektivní kvantový server a informačně teoretická soundness. |

### 2. Computational geometry and metric spaces

| Problém | Máme? | Záznam a skutečné pořadí | Doporučení |
|---|---|---|---|
| V2.1 Halving lines | Podproblém širší karty | TCS-0318, #5 (příbuzná karta) | **Propojit jako podproblém**. Speciální případ již přítomných rovinných k-sets. Pro přímku skrze dva body musí být n sudé. Zatím doplnit jako pojmenovaný podproblém. |
| V2.2 Dürerova domněnka | Ano, zdrojový záznam | TCS-0406, #8 | **Dopracovat stávající**. Přesný problém je ve zdrojovém indexu; dopracovat existující kartu. |
| V2.3 Sum of square roots v P | Ano, zdrojový záznam | TCS-0055, #18 v Algebraic computation | **Dopracovat stávající**. Máme zdrojový záznam v Algebraic computation. TOPP 33 má hlavní otázku o separaci součtů, ale v motivaci výslovně uvádí i algoritmickou otázku. Tyto cíle neztotožňovat; v kartě doplnit algoritmickou variantu a vazbu na geometrii. |
| V2.4 Jednotkové vzdálenosti: prolomit exponent 4/3 | Ne | — | **PŘIDAT**. Přidat konkrétní otázku existence eta>0 s u(n)=O(n^(4/3-eta)); určení přesného exponentu je širší cíl. Starou domněnku exponentu 1 již neuvádět jako otevřenou. |

### 3. Computational complexity

| Problém | Máme? | Záznam a skutečné pořadí | Doporučení |
|---|---|---|---|
| V3.1 NP není podmnožinou P/poly | Ano | TCS-0021, #7 | **Ponechat**. Obecné booleovské obvody, bez omezení hloubky. |
| V3.2 NP-úplnost MCSP | Ano, zdrojový záznam | TCS-5501, #110 | **Dopracovat stávající**. Máme několik zdrojových záznamů, například tento. Sjednotit hlavní otázku a doplnit deterministické polynomiální many-one redukce. |
| V3.3 Bermanova–Hartmanisova domněnka | Ano | TCS-6534, #5 **TOP5** | **Ponechat**. Stejná polynomiální izomorfie NP-úplných jazyků. |
| V3.4 Úplný problém pro TFNP | Ano, zdrojový záznam | TCS-4988, #102 | **Dopracovat stávající**. Máme přímý zdrojový odkaz na tuto otázku. Dopracovat standardní vyhledávací redukci, ne založit další kopii. |

### 4. Algorithms & data structures

| Problém | Máme? | Záznam a skutečné pořadí | Doporučení |
|---|---|---|---|
| V4.1 Deterministická lineární minimální kostra | Ano | TCS-6536, #2 **TOP5** | **Ponechat**. Porovnávací model; katalog používá O(m+n), což zahrnuje i nesouvislé vstupy s izolovanými vrcholy. |
| V4.2 Deterministické lineární třídění integerů | Ne, pouze příbuzný problém | TCS-6537, #3 (příbuzná karta) | **PŘIDAT**. Dosavadní karta žádá Las Vegas očekávaný O(n). Deterministický worst-case O(n) pro všechna w>=log n je samostatný silnější cíl. |
| V4.3 Přesný maximální tok v m polylog n | Ne | — | **PŘIDAT**. Obecný orientovaný graf a polynomiálně omezené celočíselné kapacity; dnešní m^(1+o(1)) nesplňuje požadavek polylogaritmické režie. |
| V4.4 Deterministická k-server conjecture | Ano | TCS-6575, #1 v Online algorithms | **Ponechat**. Máme ji v novém bucketu Online algorithms. Novou kopii v Algorithms & data structures nezakládat. |

### 5. Learning theory

| Problém | Máme? | Záznam a skutečné pořadí | Doporučení |
|---|---|---|---|
| V5.1 Lineární sample compression | Ano | TCS-6541, #1 **TOP5** | **Ponechat**. Katalog započítává i pomocnou informaci; stejný O(d) cíl. |
| V5.2 Efektivní učení k-juntas | Ano | TCS-6543, #3 **TOP5** | **Ponechat**. Rovnoměrné náhodné příklady; cílová složitost polynomial v n a 2^k. |
| V5.3 Learning Parity with Noise | Ano | TCS-6542, #2 **TOP5** | **Ponechat**. Konstantní nezávislý šum; již máme v Learning theory. |
| V5.4 Minimax regret stochastického BCO | Ne, pouze příbuzný problém | TCS-6577, #2 v Online algorithms | **PŘIDAT**. Existující karta je adversariální a v Online algorithms. Nově pevná neznámá konvexní funkce, jednotková koule a přesně stanovený šum, např. nezávislý N(0,1). |

### 6. Cryptography

| Problém | Máme? | Záznam a skutečné pořadí | Doporučení |
|---|---|---|---|
| V6.1 Dohoda na klíči z OWF | Ne, pouze příbuzný problém | TCS-6545, #1 (příbuzná karta) | **PŘIDAT**. Dosavadní karta žádá public-key encryption z OWF. Obecná interaktivní klasická key agreement je jiný, slabší cíl; black-box bariéra nerozhoduje obecnou implikaci. |
| V6.2 iO ze samotného LWE | Ano | TCS-6550, #3 **TOP5** | **Ponechat**. Stejný cíl pro obecné obvody; standardní polynomiální tvrdost LWE. |
| V6.3 FHE z LWE bez circular security | Ano | TCS-6551, #4 **TOP5** | **Ponechat**. Máme plné unlevelled FHE; nezaměňovat za již známé leveled FHE. |
| V6.4 Veřejně ověřitelné kvantové peníze z LWE | Ne | — | **PŘIDAT**. Přidat se zabezpečením proti kvantovému padělateli a quantum-hard LWE. Konstrukce z iO+LWE nedokládá konstrukci ze samotného LWE. |

### 7. Distributed, parallel and sublinear algorithms

| Problém | Máme? | Záznam a skutečné pořadí | Doporučení |
|---|---|---|---|
| V7.1 Deterministická LOCAL MIS v O(log n) | Ano | TCS-6506, #13 | **Ponechat**. Stejný model a deterministická garance. |
| V7.2 One-cycle versus two-cycles v MPC | Jen odlišná varianta | TCS-6505, #11 (příbuzná karta) | **Doplnit variantu**. Stávající karta má celkovou paměť O(n). Návrh dovoluje polynomial n, a tedy požaduje silnější lower bound. Doplnit jako výslovnou variantu, ne označit za přesnou shodu. |
| V7.3 Obecné perfektní párování v deterministickém NC | Ano | TCS-6504, #3 **TOP5** | **Ponechat**. Obecné grafy. Tvrzení o bipartitním NC v preprintu TR26-100 není řešením tohoto cíle. |
| V7.4 Sublineární testing orientované acykličnosti | Ano, zdrojový záznam | TCS-0847, #15 v Property testing and distribution learning | **Dopracovat stávající**. Zdroj explicitně zahrnuje dotazy na příchozí i odchozí sousedy. Katalog jej řadí do Property testing and distribution learning. |

### 8. Automata and formal languages

| Problém | Máme? | Záznam a skutečné pořadí | Doporučení |
|---|---|---|---|
| V8.1 Generalized star height větší než 1 | Ano | TCS-6559, #3 **TOP5** | **Ponechat**. Regulární výrazy s doplňkem. |
| V8.2 Sakodova–Sipserova otázka | Ano | TCS-6560, #2 **TOP5** | **Ponechat**. Polynomiální převod 2NFA na 2DFA. |
| V8.3 Ekvivalence jednoznačných CFG | Ano, zdrojový záznam | TCS-0164, #8 | **Dopracovat stávající**. Máme příslušný zdrojový index; dopracovat promise jednoznačnosti obou gramatik. |
| V8.4 Kvadratické rozpoznávání každého pevného CFL | Ne | — | **PŘIDAT**. Pevná gramatika, délka slova n; neomezovat algoritmus na kombinatorické metody. Zdroj z roku 2007 řeší jen podtřídu; použít i práci o bariéře pro Valiantův parser. |

### 9. Semantics, logic and verification

| Problém | Máme? | Záznam a skutečné pořadí | Doporučení |
|---|---|---|---|
| V9.1 Paritní hry v P | Ano, zdrojový záznam | TCS-4245, #128 | **Dopracovat stávající**. Přímý zdrojový záznam existuje, ale zaslouží hlavní samostatně formulovanou kartu. |
| V9.2 Monniaux: konvexní polyedrické invarianty | Ne | — | **PŘIDAT**. Zachovat konvexnost, racionální afinní vstup a lineární guards. Uvést obor stavů a koeficientů invariantu; výsledky pro nekonvexní invarianty či nelineární guards tuto variantu neřeší. |
| V9.3 Barendregt–Geuvers–Klop | Ano, zdrojový záznam | TCS-6583, #5 **TOP5** | **Dopracovat stávající**. Máme formulaci slabá normalizace implikuje silnou pro PTS; dopracovat zdroje a podmínky systému. |
| V9.4 Rozhodnutelnost reálného tělesa s exp | Ne | — | **PŘIDAT**. Teorie standardního R_exp v jazyce +, krát, <, exp; známé podmíněné výsledky nejsou bezpodmínečná rozhodnutelnost. |

### 10. Optimization and numerics

| Problém | Máme? | Záznam a skutečné pořadí | Doporučení |
|---|---|---|---|
| V10.1 Polynomial Hirsch conjecture | Ano | TCS-6573, #4 v Computational geometry and metric spaces | **Ponechat**. Máme v Computational geometry and metric spaces, nikoli v Optimization. |
| V10.2 P-matrix LCP v P | Ne | — | **PŘIDAT**. Racionální vstup a příslib P-matice; zkoumáme nalezení řešení, ne rozpoznání příslibu. |
| V10.3 Přesná přípustnost SDP v P | Ano | TCS-6574, #2 **TOP5** | **Ponechat**. Stejný obecný bitový model bez předpokladu striktní přípustnosti. |
| V10.4 Polynomiální růstový faktor úplného pivotování | Ne; zveřejněné řešení | — | **NEPŘIDÁVAT – vyřešený návrh**. Jako otevřený nepřidávat. Shah–Urschel, arXiv:2608.19189 (srpen 2026), dokazují kvazipolynomiální worst-case růst; požadovaná polynomiální mez je tím vyvrácena podle zveřejněného preprintu. |

## Všech 25 návrhů pro malé oblasti

| # / bucket | Problém | Máme? | Záznam a skutečné pořadí | Doporučení |
|---|---|---|---|---|
| M1 Approximation algorithms and hardness of approximation | TSP: integrality gap 4/3 | Ano | TCS-6589, #5 | **Ponechat**. Stejná Held–Karpova subtour relaxace. |
| M2 Parameterized and exact algorithms | Polynomiální kernel pro Directed FVS | Ano, zdrojový záznam | TCS-7033, #145 | **Dopracovat stávající**. Máme společný zdrojový záznam pro directed vertex/arc set. Zpřesnit vertex variantu a provázat další zdroje. |
| M3 Fine-grained complexity | Skutečně subkubický APSP | Ano | TCS-6510, #2 **TOP2** | **Ponechat**. Přesné obecně vážené APSP; zdroj a model již rozepsané. |
| M4 Pseudorandomness and derandomization | Deterministický obecný PIT | Ano, zdrojový záznam | TCS-7113, #136 v Algebraic computation | **Dopracovat stávající**. Máme zdrojovou kartu v Algebraic computation. Dopracovat Q, polynomial degree a bitový model; jako hlavní bucket doporučuji Pseudorandomness. |
| M5 Proof complexity | p-optimální výrokový důkazový systém | Ano, zdrojový záznam | TCS-7162, #5 | **Dopracovat stávající**. Přesná základní otázka je přítomná jako pracovní zdrojová karta. |
| M6 Communication complexity and Boolean function analysis | Fourier Entropy–Influence | Ano | TCS-6604, #2 **TOP2** | **Ponechat**. Klasická booleovská verze. |
| M7 Coding and information theory | Explicitní binární kódy na GV mezi | Ano, zdrojový záznam | TCS-6859, #53 | **Dopracovat stávající**. Zdroj žádá efektivní konstrukci vnitřních lineárních GV kódů v čase polynomial v jejich vlastní dimenzi. Dopracovat kanonickou binární lineární formulaci s generátorovou maticí; obecné nelineární kódy vyžadují specifikaci výstupní reprezentace. |
| M8 Algebraic computation | VP versus VNP | Ano | TCS-0005, #5 | **Ponechat**. Obecné aritmetické obvody pro permanent; odlišit od determinantální složitosti. |
| M9 Lattices and computational number theory | Přesný SVP: 2^O(n) čas a poly prostor | Ano | TCS-6619, #5 | **Ponechat**. Stejná eukleidovská varianta. |
| M10 Randomized algorithms and sampling | Vzorkování (Delta+1)-obarvení | Ne, pouze příbuzný problém | TCS-6621, #1 (příbuzná karta) | **PŘIDAT**. Dosavadní karta je rychlé míchání Glauber dynamics pro Delta+2. Nově libovolná vzorkovací metoda, Delta+1 a celková variační vzdálenost od uniformní distribuce. |
| M11 String algorithms and bioinformatics | Konstantní aproximace nejmenší gramatiky | Ano | TCS-6513, #5 | **Ponechat**. Již máme, zatím mimo top2 Strings. |
| M12 Dynamic graph algorithms | Dynamické (1+epsilon)-párování v polylog čase | Ano | TCS-6627, #2 **TOP2** | **Ponechat**. Katalog konkretizuje randomizovaný očekávaný amortizovaný čas, oblivious adversary a explicitní matching. Worst-case či adaptive adversary by byly jiné cíle. |
| M13 Counting and enumeration | Output-polynomial vertex enumeration | Ne | — | **PŘIDAT**. Omezený racionální polytope v H-reprezentaci, proměnná dimenze a čas polynomial ve vstupu plus celém výstupu. |
| M14 Property testing and distribution learning | Polynomial testing induced-C4-freeness | Podproblém širší karty | TCS-6630, #1 (příbuzná karta) | **PŘIDAT**. Souvisí s obecnou klasifikační kartou, ale tento konkrétní zbývající případ má vlastní význam. Přidat samostatně a propojit s klasifikací. |
| M15 Differential privacy | Pure-DP continual counting: optimální chyba | Jen odlišná varianta | TCS-6673, #3 (příbuzná karta) | **Doplnit variantu**. Karta již používá očekávanou maximální absolutní chybu, ale fixuje privacy epsilon=1/2. Rozšířit o závislost na epsilon; nové ID není potřeba. |
| M16 Algorithmic game theory, mechanism design and fair division | Matroid Secretary conjecture | Ne, pouze příbuzný problém | TCS-5779, #73 v Online algorithms | **PŘIDAT**. Máme jen příbuzný problém universal online CRS a zvlášť ordinal variantu. Obecná kardinalní domněnka chybí jako přímý cíl; doporučuji Online algorithms, s vazbou na AGT. |
| M17 Constraint satisfaction | Přesný práh náhodného 3-SAT | Ne | — | **PŘIDAT**. Existence limitní konstanty a její rigorózní charakterizace. Přibližné 4.267 je predikce, nikoli již dokázaná hodnota. Zafixovat uniformní model klauzulí. |
| M18 Scheduling and packing | Konstantní aditivní gap bin-packing LP | Ne, pouze příbuzný problém | TCS-6640, #2 (příbuzná karta) | **PŘIDAT**. Existující karta žádá algoritmus s počtem binů nejvýše OPT+C. Nový cíl je strukturální nerovnost OPT-LP<=C pro konfigurační LP; nejde o tutéž formulaci. |
| M19 Automated reasoning and unification | Rozhodnutelnost unifikace v K | Ano, zdrojový záznam | TCS-6643, #2 **TOP2** | **Dopracovat stávající**. Máme zdrojovou kartu této varianty, již v top2. |
| M20 Database theory and finite model theory | Asserův problém | Ne | — | **PŘIDAT**. Uzavřenost spekter prvořádových vět na doplněk mezi kladnými celými čísly; odlišit od pouhé rozhodnutelnosti existence konečného modelu. |
| M21 Computability and algorithmic information | Martinova domněnka I pro borelovské funkce | Podproblém širší karty | TCS-6646, #1 (příbuzná karta) | **Propojit jako podproblém**. Máme plnou domněnku I+II pro všechny Turingovsky invariantní funkce pod AD. Borel/část I zapsat jako pojmenovaný podproblém s vlastními předpoklady, nikoli zaměnit za ekvivalenci. |
| M22 Knowledge representation and reasoning | Deterministická ekvivalence d-DNNF | Ano, zdrojový záznam | TCS-6650, #3 v Automated reasoning and unification | **Dopracovat stávající**. Přesný základní cíl je již ve zdrojové kartě. Zachovat absenci společného vtree/dekompozice. |
| M23 Structural graph theory | Erdősova–Hajnalova domněnka | Ano | TCS-6652, #2 **TOP2** | **Ponechat**. Obecný pevný zakázaný indukovaný graf H. |
| M24 Beyond worst-case and average-case analysis | Feige: refutace náhodného 3-SAT při konstantní hustotě | Ne | — | **PŘIDAT**. Výpočetní nalezení sound refutace je odlišné od určení statistického prahu M17. Přidat s kvantifikátorem pro konstantní hustotu a bez odmítnutí splnitelné formule. |
| M25 Miscellaneous | Aanderaa–Karp–Rosenberg evasiveness | Ano, zdrojový záznam | TCS-7219, #6 v Communication complexity and Boolean function analysis | **Dopracovat stávající**. Máme v Communication complexity and Boolean function analysis. Dopracovat stávající kartu; Miscellaneous není nutné. |

## Důležité formulace a zdroje

- **Jednotkové vzdálenosti:** letošní dolní mez vyvrací původní exponent 1, ale nezlepšuje horní exponent 4/3. Přidat lze cílenou otázku prolomení 4/3. [Sawin 2026](https://arxiv.org/abs/2605.20579), [Alon et al. 2026](https://arxiv.org/abs/2605.20695).
- **Maximální tok:** i srpnový výsledek uvádí m^(1+o(1)), což je jiná garance než m krát polylog n. [Li–Wice 2026](https://arxiv.org/abs/2608.17384).
- **Stochastické BCO:** citovaný nový lower bound je skutečně pro jednu pevnou neznámou funkci se šumem. Stávající TCS-6577 se ptá na adversariální ztráty. Při dopracování nové karty uvést přesnou distribuci/normalizaci šumu a režimy d,T; některé režimy už mají těsné meze. [Rajaraman–Han 2026](https://arxiv.org/abs/2607.18652).
- **Kvantové peníze:** známá citovaná konstrukce používá iO i LWE. Nestačí ji citovat jako řešení ze samotného LWE. Návrh je vhodný s explicitním předpokladem kvantové obtížnosti LWE a standardní definicí nepadělatelnosti. [Cakan–Goyal–Yamakawa](https://arxiv.org/abs/2411.04482).
- **Monniaux:** Theorems 1 a 2 citované práce povolují nekonvexní invarianty; autoři výslovně ponechávají konvexní případ otevřený. V nové kartě je nutné přesně fixovat doménu stavů, koeficienty, guards a počet lokací. [Fijalkow et al., úvod str. 5](https://elefauch.github.io/papers_pdf/monniaux_jour.pdf).
- **CFL:** starý uživatelský odkaz dokládá kvadratické rozpoznávání podtřídy. Pro obecný cíl s pevnou gramatikou je relevantní práce o podmíněné optimálnosti Valiantova parseru. [Abboud–Backurs–Vassilevska Williams](https://arxiv.org/abs/1504.01431).
- **MPC:** aktuální TCS-6505 vyžaduje O(n) celkové paměti; uživatel navrhuje polynomial n. Lower bound proti většímu množství paměti je silnější tvrzení. Nelze bez úpravy formulace napsat jen „máme“.
- **GV:** explicitní binární lineární kód má polynomial-size reprezentaci generátorovou maticí. TCS-6859 je zdrojový záznam stejného konstrukčního cíle v kontextu vnitřních kódů; není důvod vytvářet druhý záznam pro standardní lineární verzi. U obecných nelineárních kódů nejprve specifikovat efektivní reprezentaci/encoding. [Essential Coding Theory, §7.2](https://cse.buffalo.edu/faculty/atri/courses/coding-theory/book/).
- **Matroid secretary:** TCS-5779 míří na universal online contention-resolution scheme. Původní práce jej prezentuje jako krok k secretary conjecture, a ekvivalenci výslovně neprokazuje. Proto jde o vhodný nový přímý cíl. [Dughmi 2020, §6](https://drops.dagstuhl.de/storage/00lipics/lipics-vol168-icalp2020/LIPIcs.ICALP.2020.42/LIPIcs.ICALP.2020.42.pdf), [Dütting et al. 2026](https://arxiv.org/abs/2608.11413).
- **Induced C4:** Conjecture 3.6 je konkrétní zbývající případ pro jeden zakázaný indukovaný graf; širší efektivní klasifikace TCS-6630 je odlišný cíl. [Gishboliner–Shapira](https://arxiv.org/html/2508.16878v1).
- **Pure DP:** navržené kritérium očekávané maximální chyby už TCS-6673 má. Chybí výslovná společná závislost na T a privacy epsilon; karta dnes fixuje epsilon=1/2.
- **Třídění, šifrování a bin packing:** deterministické třídění není totéž jako Las Vegas očekávané třídění; key agreement není totéž jako PKE; konstantní LP integrality gap není totéž jako polynomial-time OPT+C algoritmus. Proto doporučuji nové samostatné cíle i při existenci blízké karty.

Prioritu dopracování bych dal zejména obecnému PIT, paritním hrám, MCSP, TFNP, Dürerovi a explicitním GV kódům. Jejich dnešní nízké pořadí částečně odráží stav záznamu. Nové umístění v top5/top2 tato analýza nenastavuje.

## Počty a audit

```json
{
  "keep": 26,
  "extend": 3,
  "link": 2,
  "develop": 15,
  "add": 18,
  "reject": 1
}
```

Kompletní strojově čitelné mapování, původní evidence a odkazy každého nalezeného záznamu: [audit.json](audit.json).
