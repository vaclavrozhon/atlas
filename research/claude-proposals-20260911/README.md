> Follow-up, 11 September 2026: the user approved five Claude additions. TSP, quantum approximate SVP, near-exact near-linear edit distance, private marginals and PCSP(K₃,K₆) are now published in the [approved ten-card batch](../gpt-claude-additions-20260911/README.md). CDCL without restarts remains outside this batch. The analysis and positions below are the earlier snapshot.

# Posouzení návrhů Claude – 11. září 2026

**Doporučuji šest nových samostatných otázek:** obecný vážený TSP pod 2ⁿ, kvantovou polynomiální aproximaci SVP, téměř lineární (1+ε)-aproximaci edit distance, efektivní privátní uvolnění vyšších marginál, NP-těžkost PCSP(K₃,K₆) a sílu greedy CDCL bez restartů. Poslední dvě formulace vyžadují přesně uvedený rozhodovací, respektive důkazový model; u DP je konkrétní model navržen níže.

Z 35 hlavních voleb máme **25 přímo** (včetně pracovních zdrojových záznamů a záznamů v jiném bucketu), **3 jako příbuznou variantu nebo podproblém**, **5 chybí** a **2 jsou široké výzkumné programy**. Šestý návrh na přidání, CDCL bez restartů, je z alternativ uvnitř textu. Navíc níže samostatně porovnávám 20 konkrétních alternativ.

Pořadí odpovídá katalogu `6e1b40f3ab2390295bd9` z 2026-09-11T09:22:41+00:00. Čtu `importance_rank` v celém skutečném bucketu, nikoli pořadí po filtrování. **TOP5/TOP2** v tabulce potvrzuje přesnou nebo zdrojovou shodu v požadovaném bucketu. U příbuzného cíle není jeho vysoká pozice důkazem, že tam máme přesný návrh. U jiného bucketu uvádím jeho vlastní pořadí. Pracovní záznam (`source`, `index`) není hotová reviewed karta. Nové doporučené otázky dosud vlastní pořadí nemají.

Ve srovnání s předchozím auditem GPT se katalog mezitím změnil; například Erdős–Hajnal je nyní #3 a mimo top2. Tento report katalog ani jeho pořadí nemění.

Přítomnost jsem kontroloval podle titulů, formulací, kontextu a zdrojů, ne jen podle podobných slov. Literatura byla zvlášť kontrolována u nových kandidátů, důležitých variant a sporných tvrzení o vyřešení. Jde o kontrolu navržených otázek, nikoli o potvrzení každého historického nebo technického tvrzení v Claudeově komentáři. U DP je hlavní explicitní otevřená otázka ze staršího přehledu; nenašel jsem řešení navrženého obecného cíle, ale netvrdím úplnost rešerše všech k-way režimů.

## Nové otázky, které doporučuji přidat

### M2: Obecný vážený TSP v O*((2−ε)^n)

**Bucket:** Parameterized and exact algorithms. Základní neprolomená exponenciální bariéra, která není již přítomnou SETH ani Hamiltonovskou kružnicí.

Existuje konstanta ε>0 a klasický randomizovaný algoritmus s úspěchem alespoň 2/3, který vyřeší TSP na obecném úplném neorientovaném n-vrcholovém grafu s nezápornými binárně zadanými celočíselnými vahami v čase O((2−ε)^n poly(n,L)), kde L je celková bitová délka vah? Metrickou nerovnost nepředpokládáme. Deterministickou variantu uvést jako silnější cíl.

[Stoian 2024: zlepšení podexponenciálního faktoru, nikoli báze 2](https://arxiv.org/abs/2405.03018).

### M9: Kvantová polynomiální aproximace SVP

**Bucket:** Lattices and computational number theory. Oddělí klasickou aproximaci, kvantový přesný SVP a kvantovou aproximaci; právě poslední cíl tu chybí.

Existuje pevná konstanta C>0 a uniformní kvantový algoritmus s omezenou chybou, který z racionální báze n-rozměrné eukleidovské mřížky v čase polynomiálním v bitové délce vstupu vydá nenulový mřížkový vektor v s normou nejvýše n^C λ₁(L)? Úspěch požadovat alespoň 2/3. Jde o search SVP, nikoli o neurčenou rodinu LWE parametrů.

[Regev: směr worst-case lattice → average-case LWE redukce](https://arxiv.org/abs/2401.03703).

### M11: (1+ε)-edit distance v n^(1+o(1))

**Bucket:** String algorithms and bioinformatics. Near-linear čas a libovolně malá relativní chyba současně představují další konkrétní cíl; uživatel výslovně připouští více variant edit distance.

Pro každé pevné ε>0 existuje klasický randomizovaný algoritmus, který ze dvou řetězců délky nejvýše n nad pevnou konečnou abecedou v čase n^(1+o(1)) vydá s pravděpodobností alespoň 2/3 odhad D s ED≤D≤(1+ε)ED? ED má jednotkovou cenu vložení, smazání a substituce. Pro fixní ε je algoritmus jeden; parametr o(1) klesá s n.

[Mao–Rubinstein 2026: zatím quasi-strongly subquadratic schémata](https://arxiv.org/abs/2603.29702).

### M15: Efektivní privátní uvolnění vyšších marginál

**Bucket:** Differential privacy. Doplní výpočetní cenu odpovídání na přirozené rodiny dotazů vedle existující statistické otázky privátního PAC learningu.

Jako konkrétní kartu volit polynomiálně efektivní privátní uvolnění všech vyšších marginál podle Open Problem 7.8: existují C>0, α(d)=o(1), uniformní mechanismus a evaluator s časem poly(n,d), takže pro každou databázi n=⌈d^C⌉ řádků z {0,1}^d mechanismus splňuje (1,1/(100n²))-DP při změně jednoho řádku a vydá polynomial-size reprezentaci odpovědí? S pravděpodobností alespoň 2/3 mají odhady současně pro všechny marginály (konjunkce literálů na libovolné množině souřadnic) aditivní chybu nejvýše α(d). Výstup nemusí být syntetická databáze. Jde o navržené upřesnění modelu, nikoli doslovnou ekvivalentní formulaci každé k-way varianty.

[Vadhan, The Complexity of Differential Privacy, Open Problem 7.8](https://privacytools.seas.harvard.edu/files/complexityprivacy_1.pdf); [Chandrasekaran–Thaler–Ullman–Wan: subexponenciální odpovídání na marginály](https://arxiv.org/abs/1304.3754).

### M17: NP-těžkost 3-versus-6 barvení

**Bucket:** Constraint satisfaction. Konkrétní následující případ aproximačního barvení zaslouží samostatnou kartu vedle širší otázky pro libovolný konstantní počet barev.

Je promise rozhodovací problém PCSP(K₃,K₆) NP-těžký při deterministických polynomiálních many-one redukcích? Yes-instances jsou 3-obarvitelné grafy; no-instances grafy, které nejsou 6-obarvitelné. Grafy s chromatickým číslem 4,5,6 leží mimo příslib. Nalezení 6-obarvení slíbeného 3-obarvitelného grafu uvést jako související search cíl.

[Barto et al.: Algebraic Approach to Promise Constraint Satisfaction](https://arxiv.org/abs/1811.00970); [Beyond PCSP(1-in-3,NAE), úvod: otázka 3-versus-6](https://drops.dagstuhl.de/storage/00lipics/lipics-vol198-icalp2021/LIPIcs.ICALP.2021.121/LIPIcs.ICALP.2021.121.pdf).

### M19.a: P-simulace rezoluce pomocí greedy CDCL bez restartů

**Bucket:** Automated reasoning and unification. Ostrá otázka vysvětlující sílu konkrétního mechanismu SAT solveru; nahradí neurčité heslo proč CDCL funguje.

P-simuluje standardní greedy CDCL bez restartů obecnou rezoluci? Zvolit publikovaný model eager unit propagation a okamžitého zpracování konfliktů, standardní asserting clause learning a backjumping, bez preprocessing s novými proměnnými. P-simulace vyžaduje polynomiální převod dodané rezoluční refutace na legální CDCL běh; netvrdí existenci efektivní heuristiky hledající důkaz bez této nápovědy. Před publikací úplné karty je nutné přesně převzít přechodová pravidla z jednoho zdroje.

[Buss–Thapen, 2026: dosud otevřená separace](https://mathweb.ucsd.edu/~sbuss/ResearchWeb/heightTradeoff/); [Vinyals 2022: síla variant CDCL a non-greedy výjimka](https://simons.berkeley.edu/sites/default/files/docs/21462/satreunionslides-marcvinyals.pdf).

## Všech 35 hlavních voleb

Legenda akcí: ponechat = otázka již existuje; dopracovat = využít stávající ID; doplnit variantu = nepřidávat automaticky novou kartu. Doporučení k novým kartám je oddělené od případného budoucího přerovnání top5/top2.

### Velké oblasti

| # / požadovaný bucket | Problém | Máme? | Současný záznam a pořadí | Doporučení |
|---|---|---|---|---|
| V1 · Quantum computation | Quantum PCP | Ano | TCS-6446, **#1**; reviewed; **TOP5** | **Ponechat**. Stejná konstantní mezera normalizované energie; NLTS není řešením Quantum PCP. |
| V2 · Computational geometry and metric spaces | GNRS | Ano | TCS-6525, **#2**; reviewed; **TOP5** | **Ponechat**. Máme plnou minorově uzavřenou variantu. Planární případ je významný speciální případ, nikoli celá GNRS. |
| V3 · Computational complexity | P versus NP | Ano | TCS-0001, **#1**; reviewed; **TOP5** | **Ponechat**. Stejný základní problém. Nepřebírat bez kontroly doprovodná tvrzení o nejlepších obvodových dolních mezích. |
| V4 · Algorithms & data structures | Exponent násobení matic ω=2 | Ano | TCS-0007, **#1**; reviewed; **jiný bucket: Algebraic computation** | **Ponechat**. Máme, ale v Algebraic computation, nikoli v Algorithms & data structures. |
| V5 · Learning theory | Proč funguje hluboké učení | Široký výzkumný program | — | **Nepřidávat obecné heslo**. Výzkumný program, bez jednoznačného kritéria vyřešení. Nepřidávat jako jednu kartu; ostrá alternativa o juntách je níže. |
| V6 · Cryptography | OWF z worst-case obtížnosti | Odlišná varianta | TCS-0022, **#2**; reviewed; pořadí příbuzné karty | **Doplnit variantu/mezník**. Máme silnější implikaci P≠NP ⇒ OWF. Claudeovo NP⊄BPP je silnější předpoklad, takže implikace s tímto předpokladem je slabší cíl. Doplnit variantu a vztah předpokladů, ne vydávat za ekvivalenci. |
| V7 · Distributed, parallel and sublinear algorithms | Obecné perfektní párování v deterministickém NC | Ano | TCS-6504, **#3**; reviewed; **TOP5** | **Ponechat**. Stejný cíl pro obecné grafy; výsledky omezené na bipartitní grafy jej neřeší. |
| V8 · Automata and formal languages | Černého hypotéza | Ano | TCS-6558, **#1**; reviewed; **TOP5** | **Ponechat**. Stejný ostrý kvadratický resetovací práh. |
| V9 · Semantics, logic and verification | Skolemův problém | Ano, pracovní záznam | TCS-5773, **#9**; source; mimo top5 | **Dopracovat stávající**. Přesná obecná diskrétní otázka je v pracovním zdrojovém záznamu. Dopracovat jej; nezaměňovat za continuous Skolem nebo Positivity, pro které máme jiné karty. |
| V10 · Optimization and numerics | Silně polynomiální lineární programování | Ano | TCS-0008, **#1**; reviewed; **TOP5** | **Ponechat**. Stejný obecný racionální LP cíl včetně kontroly bitové velikosti mezivýsledků. |

### Malé oblasti

| # / požadovaný bucket | Problém | Máme? | Současný záznam a pořadí | Doporučení |
|---|---|---|---|---|
| M1 · Approximation algorithms and hardness of approximation | Unique Games Conjecture | Ano | TCS-0006, **#2**; reviewed; **TOP2** | **Ponechat**. Stejná konstantní completeness/soundness mezera; již máme. |
| M2 · Parameterized and exact algorithms | Obecný vážený TSP v O*((2−ε)^n) | Ne | — | **PŘIDAT**. Chybí přesný klasický algoritmický cíl. Fixovat obecné binárně kódované váhy a polynomiální závislost na jejich bitové délce; Hamiltonovská kružnice ani pseudopolynomiální algoritmus jej neřeší. |
| M3 · Fine-grained complexity | SETH | Ano | TCS-6595, **#1**; reviewed; **TOP2** | **Ponechat**. Stejná deterministická formulace. Vztahy k APSP a 3SUM jsou další otázky o konkrétních typech redukcí. |
| M4 · Pseudorandomness and derandomization | BPL = L | Ano, pracovní záznam | TCS-0026, **#5**; index; mimo top2 | **Dopracovat stávající**. Máme samostatný indexový záznam. Dopracovat místo založení duplikátu. |
| M5 · Proof complexity | Superpolynomiální dolní meze pro Frege | Ano | TCS-0025, **#4**; reviewed; mimo top2 | **Ponechat**. Máme unrestricted Frege. Extended Frege je samostatný silnější systém a jeho lower bound není stejná otázka. |
| M6 · Communication complexity and Boolean function analysis | Log-rank conjecture | Ano | TCS-6603, **#1**; reviewed; **TOP2** | **Ponechat**. Stejná deterministická komunikační složitost totálních funkcí a reálný rank. |
| M7 · Coding and information theory | Optimální binární rate–distance vztah / těsnost GV | Ano | TCS-1010, **#2**; reviewed; **TOP2** | **Ponechat**. Máme určení R₂(δ). Těsnost GV je konkrétní navrhovaná odpověď na tuto otázku, nikoli požadavek explicitní konstrukce. |
| M8 · Algebraic computation | VP versus VNP | Ano | TCS-0005, **#5**; reviewed; mimo top2 | **Ponechat**. Máme obecné aritmetické obvody. Tvrzená ekvivalence s polynomiální determinantální reprezentací permanentu není známa; tu máme zvlášť. |
| M9 · Lattices and computational number theory | Kvantová polynomiální aproximace SVP | Ne; máme příbuzný cíl | TCS-6667, **#2**; reviewed; pořadí příbuzné karty | **PŘIDAT**. TCS-6667 požaduje klasický algoritmus; TCS-7169 kvantový, ale přesný SVP. Kvantový algoritmus s polynomiálním aproximačním faktorem je další, dosud chybějící varianta. Není prostě ekvivalentní prolomení LWE. |
| M10 · Randomized algorithms and sampling | Glauberovo míchání pro q≥Δ+2 | Ano | TCS-6621, **#1**; reviewed; **TOP2** | **Ponechat**. Stejný konkrétní Markovův řetězec a práh. Liší se od GPT návrhu libovolného sampleru pro Δ+1 barev. |
| M11 · String algorithms and bioinformatics | (1+ε)-edit distance v n^(1+o(1)) | Ne; máme příbuzný cíl | TCS-7220, **#3**; reviewed; pořadí příbuzné karty | **PŘIDAT**. Máme (1+ε) ve skutečně subkvadratickém čase, TCS-7220, a konstantní aproximaci v n polylog n, TCS-6624. Zde je samostatný přísnější požadavek na společnou přesnost a čas. |
| M12 · Dynamic graph algorithms | Dynamické téměř optimální párování v n^(1−Ω(1)) | Odlišná varianta | TCS-6627, **#2**; reviewed; pořadí příbuzné karty | **Doplnit variantu/mezník**. Máme silnější cíl polylogaritmických aktualizací, s explicitním párováním, fixním ε a specifikovaným adversářem. Polynomické zrychlení zapsat jako mezník. Citovaný Liuův téměř lineární update bound se týká bipartitního případu. |
| M13 · Counting and enumeration | FPRAS pro perfektní párování v obecných grafech | Ano | TCS-6628, **#1**; reviewed; **TOP2** | **Ponechat**. Máme hotovou kartu přesně této otázky. Bipartitní permanent není řešením obecného případu. |
| M14 · Property testing and distribution learning | Ostré kvantitativní triangle removal lemma | Pojmenovaný případ širší karty | TCS-1029, **#5**; index; pořadí příbuzné karty | **Dopracovat stávající**. Existuje indexová karta ostrých removal mezí pro pevné vzory; zdroj výslovně probírá trojúhelník. Dopracovat jeho pojmenovaný trojúhelníkový případ. Vztah k query complexity formulovat pro příslušný model testeru. |
| M15 · Differential privacy | Efektivní privátní uvolnění vyšších marginál | Ne | — | **PŘIDAT**. Chybí přesná algoritmická otázka. TCS-6040 je otázka o učení coverage funkcí ze stejnojmenného článku, nikoli tato úloha. Fixovat soukromí, současnou aditivní přesnost, velikost databáze a efektivní reprezentaci odpovědí. |
| M16 · Algorithmic game theory, mechanism design and fair division | Existence úplné EFX alokace aditivních statků | Ano, pracovní záznam | TCS-0011, **#2**; index; **TOP2** | **Dopracovat stávající**. Máme formulaci, evidence je stále index. Zachovat konvenci odebrání statku s kladnou hodnotou pro závidícího agenta; formulace se všemi statky včetně nulových má silnější podmínku EFX₀. |
| M17 · Constraint satisfaction | NP-těžkost 3-versus-6 barvení | Ne; máme příbuzný cíl | TCS-6637, **#3**; reviewed; pořadí příbuzné karty | **PŘIDAT**. Máme širší algoritmickou otázku, zda pomůže nějaký konstantní počet barev. Pevný promise PCSP(K₃,K₆) a jeho NP-těžkost je samostatný konkrétní cíl na současné hranici. |
| M18 · Scheduling and packing | Prolomit faktor 2 pro unrelated makespan | Ano | TCS-6638, **#1**; reviewed; **TOP2** | **Ponechat**. Stejný R∥Cmax cíl pro nějaké fixní ε>0. |
| M19 · Automated reasoning and unification | Proč fungují průmyslové CDCL solvery | Široký výzkumný program | — | **Nepřidávat obecné heslo**. Výzkumný program bez jednoho rozhodovacího kritéria. Ostré alternativy o síle CDCL bez restartů a jednopravidlovém přepisování posuzuji níže. |
| M20 · Database theory and finite model theory | Logika zachycující PTIME | Ano, pracovní záznam | TCS-7195, **#3**; source; mimo top2 | **Dopracovat stávající**. Máme zdrojovou kartu v požadovaném bucketu. Je třeba nejen efektivní syntaxe, ale i odpovídající efektivní polynomiální vyhodnocování. |
| M21 · Computability and algorithmic information | Hilbertův 10. problém nad Q | Ano | TCS-6571, **#1**; reviewed; **jiný bucket: Lattices and computational number theory** | **Ponechat**. Máme v Lattices and computational number theory, nikoli v Computability. Výsledky o okruzích celých čísel číselných těles nerozhodují případ Q. |
| M22 · Knowledge representation and reasoning | Rozhodnutelnost CQ entailment v SROIQ | Ano | TCS-6680, **#4**; reviewed; **jiný bucket: Database theory and finite model theory** | **Ponechat**. Máme v Database theory and finite model theory, nikoli v Knowledge representation. Zachovat entailment přes obecné modely; konečné modely jsou jiná varianta. |
| M23 · Structural graph theory | Hadwigerova hypotéza | Ano | TCS-6651, **#1**; reviewed; **TOP2** | **Ponechat**. Stejný obecný minorový cíl. |
| M24 · Beyond worst-case and average-case analysis | Dynamická optimalita splay stromů | Ano | TCS-6498, **#1**; reviewed; **jiný bucket: Algorithms & data structures** | **Ponechat**. Máme v Algorithms & data structures, nikoli v Beyond worst-case. |
| M25 · Miscellaneous | Planted clique pod odmocninovou škálou | Ano | TCS-6656, **#1**; reviewed; **jiný bucket: Beyond worst-case and average-case analysis** | **Ponechat**. Máme v Beyond worst-case, nikoli v Miscellaneous. Katalog přesně fixuje detekci a polynomiální odstup k=n^(1/2−ε); obecný popis log n ≪ k ≪ √n zahrnuje další režimy. |

## Dvacet konkrétních alternativ uvnitř textu

| # / požadovaný bucket | Problém | Máme? | Současný záznam a pořadí | Doporučení |
|---|---|---|---|---|
| V2.a · Computational geometry and metric spaces | Sum of square roots v P | Ano, pracovní záznam | TCS-0055, **#18**; index; **jiný bucket: Algebraic computation** | **Dopracovat stávající**. Zdrojový index v Algebraic computation; hlavní separační otázka zdroje není ekvivalentní algoritmické, ta je však v motivaci přítomná. Již v auditu GPT65. |
| V5.a · Learning theory | Učení k-junt v poly(n)·f(k) | Odlišná varianta | TCS-6543, **#3**; reviewed; pořadí příbuzné karty | **Doplnit variantu/mezník**. Máme silnější čas poly(n,2^k) pro nezávislé uniformní příklady. FPT variantu uvést jako slabší mezník, ne jako ekvivalentní formulaci. |
| V6.a · Cryptography | iO ze samotného LWE | Ano | TCS-6550, **#3**; reviewed; **TOP5** | **Ponechat**. Již máme a figuruje i v GPT65. Postkvantové zabezpečení musí být součástí předpokladu a definice protivníka; samotné slovo LWE je neurčuje. |
| V7.a · Distributed, parallel and sublinear algorithms | Distribuovaný LLL v O(log log n) | Ano, pracovní záznam | TCS-6554, **#4**; source; **TOP5** | **Dopracovat stávající**. Zdrojová karta existuje a je v top5. Fixuje konstantní stupeň závislostí a dostatečnou slack podmínku; neztotožňovat s libovolnou instancí na hranici LLL. |
| V8.a · Automata and formal languages | Rozhodnutelnost každé úrovně dot-depth | Ano | TCS-6561, **#4**; reviewed; **TOP5** | **Ponechat**. Máme samostatnou kartu, v top5. |
| V9.a · Semantics, logic and verification | Paritní hry v P | Ano, pracovní záznam | TCS-4245, **#128**; index; mimo top5 | **Dopracovat stávající**. Přesná otázka existuje v indexu. Dopracovat; již doporučeno v GPT65. |
| V10.a · Optimization and numerics | Polynomiální Hirschova hypotéza | Ano | TCS-6573, **#4**; reviewed; **jiný bucket: Computational geometry and metric spaces** | **Ponechat**. Máme v Computational geometry and metric spaces. Jde o průměr grafu polytopu, nikoli o kompletní ekvivalent silně polynomiálního LP. |
| M1.a · Approximation algorithms and hardness of approximation | Small-Set Expansion Hypothesis | Ano, pracovní záznam | TCS-7160, **#4**; source; mimo top2 | **Dopracovat stávající**. Máme samostatný pracovní zdrojový záznam. |
| M5.a · Proof complexity | Superpolynomiální AC⁰[p]-Frege lower bounds | Ano | TCS-6602, **#3**; reviewed; mimo top2 | **Ponechat**. Máme vedle unrestricted Frege a Extended Frege. Rozdílné důkazové systémy jsou zde podstatné. |
| M6.a · Communication complexity and Boolean function analysis | Aaronsonova–Ambainisova hypotéza | Ano | TCS-6605, **#3**; reviewed; mimo top2 | **Ponechat**. Máme samostatně; mimo top2 tohoto bucketu. |
| M7.a · Coding and information theory | Explicitní binární kódy na GV mezi | Ano, pracovní záznam | TCS-6859, **#53**; source; mimo top2 | **Dopracovat stávající**. Máme konstrukční otázku jako zdroj. Dopracovat efektivní binární lineární formulaci, již navrženou v GPT65. |
| M8.a · Algebraic computation | Superpolynomiální determinantální složitost permanentu | Ano | TCS-6611, **#2**; reviewed; **TOP2** | **Ponechat**. Máme samostatnou kartu. Determinant je univerzální pro algebraic branching programs / weakly skew obvody, nikoli známě pro všechny polynomial-size aritmetické obvody. |
| M13.a · Counting and enumeration | Output-polynomial minimální transverzály | Ano, pracovní záznam | TCS-7112, **#47**; source; mimo top2 | **Dopracovat stávající**. Máme přímo v Counting and enumeration. Dopracovat existující kartu; aktuální #47 není tvrzení o oborovém konsenzu. |
| M15.a · Differential privacy | Kvantitativní privátní PAC learning | Ano | TCS-0506, **#2**; reviewed; **TOP2** | **Ponechat**. Máme v top2. Současná karta zahrnuje VC dimenzi i log-star Littlestoneovy dimenze; samotná Littlestoneova dimenze nevystihuje celý kvantitativní problém. |
| M18.a · Scheduling and packing | P3 s precedencemi a jednotkovými úlohami | Pojmenovaný případ širší karty | TCS-0935, **#5**; index; pořadí příbuzné karty | **Dopracovat stávající**. Máme zdrojovou otázku pro fixní počet strojů k>2. Případ k=3 výslovně pojmenovat a dopracovat, bez nové kopie. |
| M19.a · Automated reasoning and unification | P-simulace rezoluce pomocí greedy CDCL bez restartů | Ne | — | **PŘIDAT**. Přidat až s přesně zvoleným standardním modelem: vynucená unit propagation a konflikty, bez restartů, bez preprocessing s novými proměnnými. Non-greedy varianta již rezoluci simuluje. |
| M19.b · Automated reasoning and unification | Terminace jednopravidlových string-rewriting systémů | Ano, pracovní záznam | TCS-6644, **#4**; source; mimo top2 | **Dopracovat stávající**. Máme samostatnou pracovní kartu. Ani zde není potřeba nový záznam jen kvůli tomu, že jde o další problém o řetězcích. |
| M20.a · Database theory and finite model theory | Containment konjunktivních dotazů v bag sémantice | Ano | TCS-0492, **#5**; reviewed; mimo top2 | **Ponechat**. Máme samostatnou reviewed kartu; bag a set sémantika se nesmějí zaměnit. |
| M21.a · Computability and algorithmic information | NP-úplnost MCSP | Ano, pracovní záznam | TCS-5501, **#110**; source; **jiný bucket: Computational complexity** | **Dopracovat stávající**. Máme zdrojový záznam; již v auditu GPT65. Fixovat běžné deterministické polynomiální many-one redukce. |
| M23.a · Structural graph theory | Erdősova–Hajnalova hypotéza | Ano | TCS-6652, **#3**; reviewed; mimo top2 | **Ponechat**. Máme, v aktuálním katalogu #3, tedy nyní mimo top2. Již obsaženo v návrzích GPT65. |

## Co je potřeba v Claudeově textu opravit nebo rozlišit

- **VP versus VNP není známě ekvivalentní polynomiální determinantální reprezentaci permanentu.** Determinant reprezentuje polynomial-size algebraic branching programs, zatímco VP dovoluje obecné aritmetické obvody. Proto ponechat dvě existující karty TCS-0005 a TCS-6611. Viz rozlišení v úvodu a poznámce 2 práce [Kumar–Volk, CCC 2021](https://drops.dagstuhl.de/storage/00lipics/lipics-vol200-ccc2021/LIPIcs.CCC.2021.4/LIPIcs.CCC.2021.4.pdf).
- **SVP a LWE nejsou bez upřesnění ekvivalentní.** Známé redukce mají směr a parametry a pracují také s GapSVP a SIVP. Existence vhodného LWE solveru dává pomocí redukce kvantový algoritmus pro určité worst-case mřížkové problémy; obrácenou neomezenou ekvivalenci s aproximací search SVP z toho nevyvozovat. [Regev](https://arxiv.org/abs/2401.03703).
- **EFX pro chores: zmíněný negativní výsledek skutečně existuje.** He–Tao v preprintu z června 2026, v2 z 9. července, dávají pro každé n≥4 aditivní příklady bez EFX alokace. Toto obecné existenční tvrzení proto nepřidávat jako otevřené. Výsledek se týká chores a neřeší EFX pro goods. [He–Tao](https://arxiv.org/abs/2606.08872).
- **EFX versus EFX₀:** pokud dovolujeme nulové hodnoty, slova „libovolný předmět“ jsou přísnější než definice TCS-0011, která vyžaduje kladnou hodnotu odebíraného předmětu pro závidícího agenta. Před převzetím formulace explicitně zachovat zvolenou konvenci. [Amanatidis et al., survey, Definition 5](https://arxiv.org/abs/2202.07551).
- **CDCL bez restartů není jeden model.** Non-greedy unit propagation/conflict processing může rezoluci simulovat; také preprocessing může změnit sílu systému. Otevřenou kartu vázat na standardní greedy model. Aktuální práce stále popisuje kandidáta na separaci, nikoli důkaz separace. [Vinyals, slide 41–42](https://simons.berkeley.edu/sites/default/files/docs/21462/satreunionslides-marcvinyals.pdf), [Buss–Thapen, journal 2026](https://mathweb.ucsd.edu/~sbuss/ResearchWeb/heightTradeoff/).
- **Dynamické párování:** rozlišovat obecné/bipartitní grafy, explicitní párování/odhad jeho velikosti, fixní/klesající ε a amortizovaný/worst-case čas. Citace Liuova boundu bez bipartitnosti je zavádějící. Existence rychlého maximal matching není řešení maximum matching. [Liu 2024](https://arxiv.org/abs/2403.02582), [Assadi–Khanna–Kiss, SODA 2025](https://arxiv.org/abs/2406.13573).
- **Removal lemma a ordered RS grafy mají skutečnou souvislost, ale nejde o totožné kvantitativní cíle.** Ordered RS je definováno přes indukovanost v příslušných suffixech; novější převod mezi ordered a běžnými RS grafy je třeba zahrnout. Formulaci „obě otázky čekají na tutéž díru“ nepřebírat jako ekvivalenci. [Pratt, SOSA 2026](https://arxiv.org/abs/2502.02455). Trojúhelníkový případ existujícího TCS-1029 je výslovně probírán u [Goldreich, Open Problem 8.17](https://www.wisdom.weizmann.ac.il/~oded/PDF/pt-v3.pdf).
- **Nové algoritmy neztotožňovat se změnou exponentu, kterou chceme.** TSP algoritmus 2ⁿn²/2^{Ω(√log n)} stále nemá bázi 2−ε. Obdobně edit-distance schéma s quasi-strongly subquadratic časem nemá téměř lineární čas. [Stoian 2024](https://arxiv.org/abs/2405.03018), [Mao–Rubinstein 2026](https://arxiv.org/abs/2603.29702).

## Další zmíněné směry bez doporučení nové karty v této podobě

- **Vztahy mezi SETH, APSP a 3SUM:** smysluplné téma, ale pro jednu novou kartu určit směr implikace, typ redukce, randomizaci a požadované fine-grained parametry. Samotné podmíněné bariéry nejsou důkazem neexistence všech redukcí.
- **Proč generalizují sítě, teorie feature learningu a proč funguje průmyslové CDCL:** zachovat jako oborovou motivaci; karty mají mít konkrétní tvrzení s kritériem vyřešení.
- **Je low-degree heuristika správná / worst-case základ planted clique:** neurčené rodiny modelů, stupně, redukce a rozsah tvrzení; nelze zatím stanovit jednu přesnou novou otázku.
- **Přesná výpočetní složitost offline optimálního BST, těsnost Wilberových mezí a hustota RS grafů:** zajímavé vedlejší cíle, ale Claudeův text neurčuje pro každý samostatně model a kvantifikátory. V této analýze je nepočítám mezi šest hotových doporučení; ponechávám je k případnému samostatnému výběru.
- **Obecné prolomení LWE kvantově:** před samostatnou kartou fixovat modul, chybu, počet vzorků, search/decision variantu a požadovanou úspěšnost. Nelze jej získat pouhým přejmenováním nové SVP karty.

## Priorita úpravy již přítomných záznamů

Nejprve bych dopracoval **Skolem, paritní hry, BPL = L a trojúhelníkový removal problém**. Další vhodné existující záznamy jsou logika pro PTIME, minimální transverzály, tří-strojový scheduling a jednopravidlové string rewriting. Jejich dnešní nízká pozice neznamená nízký odborný význam; zde však pořadí nepřepisuji.

Karty pro násobení matic, Hilbertův 10. problém nad Q, SROIQ, dynamickou optimalitu a planted clique už máme, pouze v jiných bucketech než navrhuje Claude. Nové kopie kvůli jinému zařazení nevytvářet.

Kompletní mapování, aktuální evidence a zdrojové odkazy existujících karet: [audit.json](audit.json).
