**Publication update — 10 September 2026:** The retained proposals below have now been added to the atlas as source-linked short drafts, following the user’s approval. The original research and novelty checks below describe the pre-publication stage. See [publication manifest](../import-fundamental-20260910/publication.json).

**Návrhy zásadních nových problémů — 10. září 2026**

Výsledek rešerše: **72 kandidátů v deseti velkých kategoriích**. Požadovaných 10–20 nových zásadních problémů v každé kategorii se mi nepodařilo doložit. Níže proto uvádím skutečný počet; seznam neobsahuje náhradní položky přidané pouze pro dosažení kvóty.

Porovnání zahrnovalo všech **6,513 uložených karet**, včetně malých kategorií. Hledal jsem v názvech, formulacích a původních výňatcích; u blízkých shod jsem posuzoval výpočetní model, kvantifikátory a podle potřeby otevřel původní pasáž. Samotná zmínka o hypotéze v motivaci článku se nepočítá jako existující karta této hypotézy; existující výňatek formulující tutéž hlavní otázku se počítá, i když je jeho název nečitelný.

Výběr významnosti je odborný úsudek: dlouhodobá ústřední otázka oboru, základní hranice výpočetního modelu nebo chybějící teorie široce používaného primitiva. Nejde o kompletní výzkumné karty ani nezávislé ověření všech důkazů v citované literatuře. U jednotlivých položek je uvedeno, co musí zůstat ve formulaci, aby byla opravdu otevřená.

| # | Velká kategorie | Noví kandidáti | Chybí do minima 10 |
|---|---|---:|---:|
| 1 | Quantum computation | **9** | 1 |
| 2 | Computational geometry and metric spaces | **7** | 3 |
| 3 | Computational complexity | **6** | 4 |
| 4 | Algorithms & data structures | **6** | 4 |
| 5 | Learning theory | **5** | 5 |
| 6 | Cryptography | **8** | 2 |
| 7 | Distributed, parallel and sublinear algorithms | **6** | 4 |
| 8 | Automata and formal languages | **8** | 2 |
| 9 | Semantics, logic and verification | **8** | 2 |
| 10 | Optimization and numerics | **9** | 1 |
| | **Celkem** | **72** | **28** |

Návrhy jsou uloženy odděleně od veřejného katalogu. [Vyřazené duplicity a nově vyřešené otázky](EXCLUSIONS.md) vysvětlují nejdůležitější odmítnutí. [JSON](candidates.json) a [CSV](shortlist.csv) obsahují strojově čitelný seznam.

---

**1. Quantum computation — 9 kandidátů**

**1. [Asymptotically good quantum locally testable codes](https://www.nature.com/articles/s41534-024-00908-8)**

Existují kvantové kódy s konstantní lokalitou a soundness a současně konstantním rate a relativní vzdáleností? Kvantová obdoba jednoho ze základních spojení mezi opravou chyb, lokálním testováním a PCP.

Nejbližší karty: TCS-6446. Quantum PCP je jiná hypotéza; existence dobrých qLDPC bez lokální testovatelnosti už byla vyřešena.

Další podklady: [zdroj 2](https://quantum-journal.org/papers/q-2024-10-18-1501/).

**2. [Area law for general gapped 2D Hamiltonians](https://arxiv.org/abs/2103.02492)**

Splňuje jedinečný základní stav obecného lokálního Hamiltoniánu na 2D mřížce s pevnou lokální dimenzí, rovnoměrně omezenými interakcemi a konstantní spektrální mezerou entanglementovou area law? Základní hranice složitosti kvantových stavů a předpoklad používaný při jejich numerickém popisu.

V prohledaných formulacích katalogu nebyla nalezena stejná otázka.

Další podklady: [zdroj 2](https://www.nature.com/articles/s41567-022-01740-7).

**3. [Self-correcting quantum memory in three dimensions](https://arxiv.org/abs/2510.05479)**

Lze v geometricky lokálním 3D systému s omezenými interakcemi pasivně uchovávat qubit při nenulové teplotě po dobu rostoucí s velikostí systému, bez dodatečného zákazu lokálních chyb? Řeší, zda může kvantová paměť dosáhnout přirozené tepelné stability klasické paměti.

Nejbližší karty: TCS-4951. TCS-4951 řeší dobu koherence konkrétní konstrukce; zde jde o obecnou existenci paměti v geometrických 3D systémech. Práce o cored product codes (2025/2026) poskytuje numerickou evidenci konečných velikostí, nikoli asymptotický důkaz; symmetry-protected model zase dodatečně omezuje povolené chyby.

Další podklady: [zdroj 2](https://arxiv.org/abs/2103.08622).

**4. [NPT bound entanglement](https://www.sciencedirect.com/science/article/pii/S0024379524004336)**

Existuje kvantový stav, jehož částečná transpozice není pozitivně semidefinitní, a přesto z něj nelze LOCC destilovat entanglement ani při použití libovolného počtu kopií? Rozhoduje základní hranici mezi existujícím a využitelným kvantovým provázáním.

Nejbližší karty: TCS-6459. Otázka NPT distilovatelnosti není totožná s distilovatelným tajným klíčem ani s pouhou existencí bound entanglement.

**5. [Quantum capacity of the qubit depolarizing channel](https://journals.aps.org/prl/abstract/10.1103/PhysRevLett.120.160503)**

Určit neasistovanou asymptotickou kvantovou kapacitu qubitového depolarizačního kanálu pro všechny hodnoty šumu. Nezodpovězená základní kapacitní otázka pro kanonický model kvantového šumu.

V prohledaných formulacích katalogu nebyla nalezena stejná otázka.

**6. [Computability of quantum channel capacity](https://doi.org/10.1016/j.physrep.2025.06.004)**

Existuje algoritmus, který z efektivního popisu libovolného konečněrozměrného bezpaměťového kvantového kanálu a ε vypočte jeho kvantovou kapacitu s chybou nejvýše ε? Ptá se, zda základní informační kapacitu vůbec lze algoritmicky určovat.

Katalog obsahuje Shannonovu kapacitu grafu, nikoli tuto kapacitu kvantového kanálu. Nezaměňovat s nerozhodnutelností jiných kapacit.

**7. [Polynomial-time quantum algorithm for the dihedral hidden subgroup problem](https://arxiv.org/abs/1112.3333)**

Lze dihedrální hidden subgroup problem s oracle přístupem řešit v kvantovém čase polynomiálním v logaritmu velikosti grupy? Jeden z hlavních nevyřešených cílů kvantových algoritmů po Shorově algoritmu, propojený s mřížkovými problémy.

Nejbližší karty: TCS-4374, TCS-4811, TCS-5170. Existující výňatky se ptají na realizaci určitého měření či využití výstupu orákula. Obecná polynomialita DHSP v nich formulována není.

**8. [Graph isomorphism in BQP](https://www.scottaaronson.com/writings/qchallenge.html)**

Existuje polynomiální kvantový algoritmus pro izomorfismus libovolných konečných grafů? Kanonický kandidát na nové kvantové zrychlení mimo abelovské hidden subgroup problémy.

Nejbližší karty: TCS-4419. Klasická GI v P je už TCS-5750. Kvantová polynomialita je odlišný výpočetní cíl a v prohledaném katalogu chybí.

Další podklady: [zdroj 2](https://arxiv.org/abs/2512.24423).

**9. [Information-theoretic classical verification of quantum computation](https://arxiv.org/abs/2604.11952)**

Má každý BQP výpočet interaktivní důkaz s klasickým polynomiálním verifikátorem, jediným efektivním kvantovým proverem a soundness proti neomezenému podvodníkovi, bez kryptografických předpokladů? Ústřední otázka, zda lze kvantovému výpočtu důvěřovat pouze na základě klasicky kontrolované komunikace.

Nejbližší karty: TCS-0030, TCS-0031. Existující karty požadují oracle separaci. Zde je cílem protokol nebo nepodmíněná nemožnost v běžném modelu. Mahadev řeší verzi s kryptografickým předpokladem.

Další podklady: [zdroj 2](https://arxiv.org/abs/1709.06984).

---

**2. Computational geometry and metric spaces — 7 kandidátů**

**1. [Kannan–Lovász–Simonovits conjecture](https://randomstrasse101.math.ethz.ch/posts/KLSConjecture/)**

Mají všechny izotropní logkonkávní míry dimenzionálně nezávislou Poincarého konstantu? Ústřední hypotéza vysokodimenzionální geometrie s přímými důsledky pro sampling a optimalizaci.

Nejbližší karty: TCS-2661. TCS-2661 se ptá na analogii pro Hessian manifolds; obecná KLS v katalogu chybí. Thin-shell a slicing už nepřidávat.

**2. [Lang–Plaut problem](https://web.math.princeton.edu/~naor/homepage%20files/assouad-N%28K%29.pdf)**

Vkládá se každá doubling podmnožina Hilbertova prostoru bi-Lipschitzovsky do konečněrozměrného eukleidovského prostoru, s parametry závislými jen na doubling konstantě? Základní otázka redukce dimenze podle vnitřní geometrie dat.

V prohledaných formulacích katalogu nebyla nalezena stejná otázka.

Další podklady: [zdroj 2](https://www.its.caltech.edu/~sryoo/teaching/Syllabus_Ma191a_2024F.pdf).

**3. [Gupta–Newman–Rabinovich–Sinclair conjecture](https://www.wisdom.weizmann.ac.il/~robi/papers/CKR-TreewidthSparsestCut-APPROX10.pdf)**

Pro každou vyloučenou minorovou strukturu H: vkládají se všechny metriky H-minor-free grafů do ℓ₁ s konstantním zkreslením závislým jen na H? Spojuje strukturu metrik se základní mezerou mezi multicommodity flow a sparsest cut.

V prohledaných formulacích katalogu nebyla nalezena stejná otázka.

Další podklady: [zdroj 2](https://courses.grainger.illinois.edu/CS583/sp2026/approx-algorithms-lecture-notes.pdf).

**4. [Optimal size of weak ε-nets for convex ranges](https://arxiv.org/abs/1808.02686)**

Jaká je asymptoticky nejmenší velikost slabé ε-sítě pro libovolnou konečnou množinu bodů v pevné dimenzi, vzhledem ke všem konvexním rozsahům? Klasický základ geometrického samplingu; velká mezera mezi známými mezemi přetrvává už v rovině.

Nejbližší karty: TCS-4428, TCS-6419. Katalog má otázku pro pohybující se body. Obecnou statickou extremální otázku je třeba odlišit od tohoto kinetického modelu.

**5. [Constant-distortion Steiner point removal](https://epubs.siam.org/doi/10.1137/1.9781611977912.191)**

Lze z každého váženého grafu s terminály vytvořit minor jen na těchto terminálech a vhodně jej převážit tak, aby D(u,v) ≤ D_minor(u,v) ≤ C·D(u,v) pro všechny terminály a univerzální C? Základní problém komprese metrik a síťových struktur při zachování vzdáleností.

Planární a obecně minor-free případ byl vyřešen; kandidátem je obecný graf.

**6. [Unknot recognition in polynomial time](https://drops.dagstuhl.de/storage/00lipics/lipics-vol332-socg2025/html/LIPIcs.SoCG.2025.55/LIPIcs.SoCG.2025.55.html)**

Lze v čase polynomiálním v délce diagramu rozhodnout, zda zadaný uzel je triviální? Jeden ze základních výpočetních problémů topologie; známé certifikáty ani praktické algoritmy zatím nedávají polynomiální algoritmus.

V prohledaných formulacích katalogu nebyla nalezena stejná otázka.

**7. [Optimal ℓ₁ distortion of planar Earth Mover Distance](https://www.weizmann.ac.il/math/gideon/sites/math.gideon/files/uploads/planar-earthmover.pdf)**

Určit optimální zkreslení při bi-Lipschitzově vnoření transportní metriky na n×n mřížce do ℓ₁. Základní otázka, jak účinně lze reprezentovat podobnost obrazů a transportní vzdálenosti.

Nejbližší karty: TCS-0973, TCS-0990. Existující otázky řeší velikost sketchů a paměť streamingu; zde jde o optimální geometrické zkreslení samotného embeddingu.

---

**3. Computational complexity — 6 kandidátů**

**1. [P versus PSPACE](https://www.math.ias.edu/files/Book-online-Aug0619.pdf)**

Platí P = PSPACE? Základní rozdíl mezi efektivním výpočtem a možností efektivně ukládat stav výpočtu.

P vs NP už je zahrnuto; rovnost P a PSPACE není ekvivalentní otázka. Další sousední separace z téže hierarchie nepřidáváme jen pro navýšení počtu.

**2. [L versus P](https://www.math.ias.edu/files/Book-online-Aug0619.pdf)**

Lze každý polynomiálně časový výpočet provést s logaritmickou pracovní pamětí? Kanonická hranice síly paměti v efektivním výpočtu.

Nejbližší karty: TCS-5150. TCS-5150 se zabývá neuniformní formulací přes branching programs a proof systems; zde jde o uniformní třídy.

**3. [Infinitude of the polynomial hierarchy](https://www.math.ias.edu/files/Book-online-Aug0619.pdf)**

Je polynomiální hierarchie striktní na všech konečných úrovních? Ptá se, zda každá další alternace existenčních a univerzálních důkazů přidává výpočetní sílu.

Jedna společná otázka pro celou hierarchii, nikoli série uměle oddělených sousedních separací.

**4. [NL versus UL](https://eccc.weizmann.ac.il/report/2025/077/download)**

Lze každý nondeterministický logspace výpočet nahradit výpočtem s nejvýše jednou přijímající větví? Základní otázka jednoznačnosti svědků a izolace cest v malém prostoru.

Nejbližší karty: TCS-0004. L vs NL je silnější derandomizační/cestová hranice; NL vs UL má odlišný cíl: jediného přijímajícího svědka.

**5. [Berman–Hartmanis isomorphism conjecture](https://eccc.weizmann.ac.il/report/2025/157/download/)**

Jsou všechny NP-úplné jazyky navzájem izomorfní bijekcí, kterou i její inverzi lze počítat v polynomiálním čase? Klasická otázka jednotné struktury NP-úplnosti.

V prohledaných formulacích katalogu nebyla nalezena stejná otázka.

**6. [TC⁰ versus NC¹](https://web.vu.lt/mif/s.jukna/boolean/index.html)**

Je NC¹ obsaženo v neuniformní TC⁰, nebo existuje funkce počitatelná logaritmicky hlubokými obvody vyžadující superpolynomiální konstantně hluboké threshold obvody? Jedna z hlavních bariér explicitních dolních mezí pro obvody s majority/threshold branami.

Nejbližší karty: TCS-2243, TCS-1054. TCS-2243 řeší dichotomii jazykové podtřídy; TCS-1054 exponenciální dolní meze pro hloubku dvě. Zde jde o všechny konstantní hloubky a superpolynomiální separaci.

Další podklady: [zdroj 2](https://drops.dagstuhl.de/storage/00lipics/lipics-vol360-fsttcs2025/LIPIcs.FSTTCS.2025.26/LIPIcs.FSTTCS.2025.26.pdf).

---

**4. Algorithms & data structures — 6 kandidátů**

**1. [Deterministic linear-time minimum spanning tree](https://people.csail.mit.edu/karger/Papers/mst.pdf)**

Existuje deterministický O(m+n) algoritmus pro MST s porovnáváním libovolných reálných vah? Zbývající základní mezera mezi deterministickým a randomizovaným řešením jedné z ústředních grafových úloh.

Nejbližší karty: TCS-0403. Euclidean MST a distributed MST jsou jiné vstupní/výpočetní modely.

**2. [Linear-time integer sorting](https://www.cs.cmu.edu/~15451-s25/slides/lecture03.pdf)**

Lze n celých čísel po jednom wbitovém slově seřadit na word RAM v očekávaném O(n) čase pro obecné w ≥ log n? Základní otázka využitelnosti bitových operací v jednom z nejdůležitějších algoritmických primitiv.

Polynomiálně omezený číselný univerzum se dá lineárně řadit radix sortem; kandidát musí výslovně připouštět obecnou délku slova.

Další podklady: [zdroj 2](https://cs.au.dk/~gerth/papers/swat14sort.pdf).

**3. [Almost-linear-time maximum matching in general graphs](https://arxiv.org/abs/2409.14849)**

Lze v obecném neorientovaném grafu nalézt přesný maximum-cardinality matching v čase m^(1+o(1))? Významná zbývající hranice rychlých algoritmů pro základní kombinatorickou optimalizaci.

Nejbližší karty: TCS-4499. TCS-4499 se ptá na kvantovou query complexity. Téměř lineární bipartitní případ neřeší obecné grafy.

**4. [Linear-time triangle detection](https://arxiv.org/abs/1402.0054)**

Lze v libovolném neorientovaném grafu rozhodnout existenci trojúhelníku v O(m+n), případně m^(1+o(1)), čase? Základní hranice rychlosti lokálních grafových výpočtů a důležitý opěrný bod jemné složitosti.

Nejbližší karty: TCS-2997, TCS-1160. CONGEST a zakázané podgrafy mají užší model; jde o běžný sekvenční algoritmus pro obecný graf. Neověřené preprinty tvrdící linearitu nelze vydávat za přijaté řešení.

**5. [Superlogarithmic static cell-probe lower bounds](https://eccc.weizmann.ac.il/report/2025/155/download/)**

Prokázat superlogaritmický počet paměťových přístupů pro explicitní statickou úlohu s O(log n)bitovým dotazem, O(log n)bitovými slovy a téměř lineární pamětí. Jedna z hlavních dosud nepřekonaných bariér nepodmíněných dolních mezí pro datové struktury.

Nejbližší karty: TCS-0949, TCS-5850. TCS-0949 se ptá na vektorový dotaz délky n a dolní mez ω(n); nejde o obecnou logaritmickou bariéru u krátkých dotazů. Výsledek 2025 pro náhodný operátor a velmi mnoho dotazů tento explicitní cíl neřeší.

**6. [Deterministic linear-time construction of static dictionaries](https://www.brics.dk/RS/99/48/BRICS-RS-99-48.pdf)**

Lze ze seznamu n různých celočíselných klíčů deterministicky v O(n) čase zkonstruovat statický slovník s O(n) slovy paměti a O(1) nejhorším časem dotazu na členství a přidružená data? Uvažujme standardní word-RAM s w = Θ(log n), aritmetikou včetně násobení a bitovými operacemi; příprava datové struktury se započítává do času. Klasická otázka, zda náhodnost přináší nezbytnou výhodu už při konstrukci jedné z nejzákladnějších datových struktur. Náhodné konstrukce optimálního očekávaného lineárního času známe; obecné deterministické konstrukce mají stále režii.

Nejbližší karty: TCS-1730, TCS-2389, TCS-4997, TCS-4910. TCS-1730 řeší praktickou rychlost MPHF blízko informační mezi; TCS-2389 learned monotone hashing v praxi; TCS-4997 explicitní konstrukce speciálních disperserů pro neadaptivní cell-probe model; TCS-4910 selhání rodin hashovacích funkcí s omezeným náhodným popisem. Žádná není obecná deterministická konstrukce statického slovníku. Předchozí návrh integer-sort požaduje třídění, nikoli O(1) dotazy slovníku. Není ani v návrhu pro malé kategorie.

Další podklady: [zdroj 2](https://doi.org/10.1007/978-3-540-70575-8_8), [zdroj 3](https://epubs.siam.org/doi/10.1137/23M1567618), [zdroj 4](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.CPM.2026.25).

---

**5. Learning theory — 5 kandidátů**

**1. [Linear-size sample compression conjecture](https://proceedings.mlr.press/v272/attias25a.html)**

Má každá binární konceptová třída s VC dimenzí d vzorkové kompresní schéma velikosti O(d), nezávisle na počtu příkladů? Základní otázka, zda se statistická složitost učení přesně odráží v možnosti komprimovat naučenou informaci.

Nejbližší karty: TCS-1539, TCS-4792, TCS-1942, TCS-4999, TCS-3787, TCS-5148. Existující otázky řeší robustní, multiclass, ample či reálné varianty. Obecná binární VC otázka není tatáž. Údajný důkaz arXiv:2603.23561 byl stažen; poslední verze uvádí chybu v Lemma 2.

Další podklady: [zdroj 2](https://arxiv.org/abs/2604.02949), [zdroj 3](https://arxiv.org/abs/2603.23561).

**2. [Efficient learning parity with noise](https://doi.org/10.4230/LIPIcs.APPROX/RANDOM.2021.60)**

Lze neznámou paritu n bitů naučit z uniformních příkladů s nezávislým konstantním šumem η∈(0,1/2) v polynomiálním čase? Kanonický test hranice výpočetní naučitelnosti a základ široké rodiny kryptografických předpokladů.

Nejbližší karty: TCS-3117, TCS-6454, TCS-0453. Paměťové dolní meze a redukce k variantám LPN nejsou obecná otázka polynomiální naučitelnosti.

**3. [Breaking the computational barrier for learning juntas](https://openreview.net/pdf?id=wszZlP1K14)**

Lze libovolnou k-juntu na n proměnných naučit z uniformních náhodných příkladů v čase poly(n,2^k,1/ε), místo prohledávání n^{Ω(k)} možností? Základní úloha identifikace malého počtu relevantních proměnných bez předpokladů o tvaru cílové funkce.

Nejbližší karty: TCS-1823, TCS-1400, TCS-3717, TCS-6043, TCS-3304. Testing junt, učení junta-distribucí a učení při dalších předpokladech jsou odlišné otázky. Uvedený čas je hlavní ambiciózní cíl; už n^{o(k)} by překonal klasickou bariéru.

**4. [Distribution-free learning of intersections of two halfspaces](https://proceedings.mlr.press/v291/diakonikolas25a.html)**

Existuje improper PAC algoritmus pro průnik dvou γ-margin halfspaces nad jednotkovou koulí, s časem poly(d,1/γ,1/ε), pro libovolné rozdělení příkladů? Jedna z nejjednodušších nelineárních tříd, u nichž stále není pochopena efektivní distribučně nezávislá naučitelnost.

Nejbližší karty: TCS-5088. TCS-5088 se výslovně ptá na plnou polynomialitu při silných distribučních předpokladech. Zde nejsou takové předpoklady a postačují dvě halfspaces; proper hardness sama tuto otázku neřeší.

**5. [Mansour’s conjecture](https://www.ias.edu/sites/default/files/math/ODonnell_Fourier.pdf)**

Je pro každé ε∈(0,1/2] Fourierovo spektrum každé s-termové DNF ε-koncentrované na nejvýše s^{O(log(1/ε))} koeficientech? Zásadní hypotéza spektrální struktury naučitelných funkcí s přímým důsledkem pro efektivní agnostické učení DNF s dotazy.

Nejbližší karty: TCS-0023, TCS-5358. Existující PAC-learning DNF otázky nejsou ekvivalentní analytické hypotéze. Patří na rozhraní learning a Boolean function analysis; zde zařazena podle důsledků pro učení.

Další podklady: [zdroj 2](https://eccc.weizmann.ac.il/report/2010/023/revision/3/download/).

---

**6. Cryptography — 8 kandidátů**

**1. [Public-key encryption from one-way functions](https://mit6875.github.io/FA23SLIDES/lec10.pdf)**

Implikuje existence jednosměrných funkcí existenci bezpečného šifrování s veřejným klíčem, pokud připustíme i non-black-box konstrukce? Základní hranice mezi soukromým a veřejným klíčem.

Nejbližší karty: TCS-0022, TCS-6453. Existence OWF z NP-hardness je jiná otázka. Známé black-box separace neřeší obecnou implikaci.

Další podklady: [zdroj 2](https://eprint.iacr.org/2017/365.pdf).

**2. [One-way permutations from one-way functions](https://eprint.iacr.org/2015/752.pdf)**

Stačí existence kryptografických jednosměrných funkcí k existenci kryptografických jednosměrných permutací? Ptá se, zda požadavek bijektivity přidává zásadní kryptografickou sílu.

Jde o average-case kryptografickou bezpečnost a obecné konstrukce; nejde o pouze worst-case jednosměrnost ekvivalentní separacím tříd.

**3. [Collision-resistant hashing from one-way functions](https://ieee-focs.org/FOCS-2018-Papers/pdfs/59f850.pdf)**

Implikují jednosměrné funkce existenci rodiny kolizně odolných hashovacích funkcí, bez omezení na black-box konstrukce? Vyjasňuje minimální předpoklady pro základní nástroj autentizace a kryptografických závazků.

Otázka je obecná implikace mezi primitivy; konkrétní hashovací konstrukce ani black-box nemožnost ji neřeší.

**4. [Chosen-ciphertext security from ordinary public-key encryption](https://theory.stanford.edu/~trevisan/cs276/projects.html)**

Lze z libovolné existence IND-CPA bezpečného PKE odvodit existenci IND-CCA2 bezpečného PKE bez dalších předpokladů? Základní otázka, zda obrana proti aktivním útokům vyžaduje silnější předpoklady než pasivní utajení.

Nejde o zesílení konkrétního schématu při dodatečných předpokladech ani pouze o black-box transformaci.

**5. [Oblivious transfer from public-key encryption](https://theory.stanford.edu/~trevisan/cs276/projects.html)**

Implikuje samotná existence PKE existenci oblivious transfer, při povolení obecných non-black-box konstrukcí? Ptá se, zda základní veřejné šifrování postačuje k obecné bezpečné dvoustranné komputaci.

Známá black-box separace ponechává obecnou implikaci otevřenou.

Další podklady: [zdroj 2](https://eprint.iacr.org/2021/882.pdf).

**6. [Indistinguishability obfuscation from LWE alone](https://eprint.iacr.org/2021/1334.pdf)**

Lze z běžného LWE předpokladu samotného sestrojit indistinguishability obfuscation pro všechny polynomiálně velké obvody? Obfuskace je univerzální kryptografický nástroj; hlavní otázkou zůstává její založení na jednom široce studovaném předpokladu.

Nejbližší karty: TCS-0450, TCS-4097. Existence iO z kombinací předpokladů je známá. Konkrétní útoky na staré obfuskátory nejsou obecná konstrukce z LWE.

Další podklady: [zdroj 2](https://doi.org/10.1145/3785007).

**7. [Unleveled FHE without circular-security assumptions](https://eprint.iacr.org/2023/1376.pdf)**

Lze z běžného LWE samotného sestrojit kompaktní fully homomorphic encryption pro neomezenou předem neurčenou polynomiální hloubku, bez dodatečného circular/KDM security předpokladu? Řeší základní mezeru mezi teoretickým předpokladem bezpečnosti a univerzální homomorfní komputací.

Leveled FHE s hloubkou určenou při generování klíče není řešením této otázky.

Další podklady: [zdroj 2](https://cseweb.ucsd.edu/classes/wi23/cse208-a/FHEorg.pdf).

**8. [Non-interactive zero knowledge from one-way functions](https://homepages.cwi.nl/~schaffne/courses/crypto/2014/papers/ComZK08.pdf)**

Stačí jednosměrné funkce pro NIZK argumenty pro všechny NP jazyky ve standardním common-reference-string modelu? Vymezuje minimální předpoklady pro odstranění interakce ze zero-knowledge důkazů.

NIZK z LWE existuje. Kandidátem je slabší předpoklad OWF a standardní CRS model, nikoli random oracle.

---

**7. Distributed, parallel and sublinear algorithms — 6 kandidátů**

**1. [P versus NC](https://www.math.ias.edu/files/Book-online-Aug0619.pdf)**

Lze každý polynomiálně časový problém řešit uniformními polynomiálně velkými obvody polylogaritmické hloubky? Ústřední otázka, zda existují efektivní výpočty, které jsou nevyhnutelně sekvenční.

Jedna otázka pro obecnou parallelizovatelnost; nepočítáme zvlášť každou dvojici sousedních paralelních tříd.

**2. [Distributed Lovász Local Lemma in O(log log n) rounds](https://arxiv.org/abs/1705.04840)**

Lze distribuovaný LLL při konstantním závislostním stupni a dostatečném konstantním polynomiálním slacku řešit v LOCAL modelu s vysokou pravděpodobností za O(log log n) kol? Kanonická bariéra distribuovaného překonávání lokálních konfliktů, s důsledky pro širokou rodinu grafových algoritmů.

Nejbližší karty: TCS-0851. Node-averaged O(log log n) z roku 2025 není požadovaná worst-case složitost všech uzlů.

Další podklady: [zdroj 2](https://arxiv.org/abs/2502.11690).

**3. [Optimal exact single-source shortest paths in CONGEST](https://link.springer.com/article/10.1007/s00446-026-00505-2)**

Lze přesné vzdálenosti od zdroje ve spojeném neorientovaném grafu s n vrcholy, nezápornými polynomiálně omezenými celočíselnými vahami a hop-diameter D spočítat randomizovaně v CONGEST za Õ(√n+D) kol s vysokou pravděpodobností? Základní distribuované grafové primitivum s neuzavřenou mezerou mezi algoritmy a komunikačními dolními mezemi.

Je nutné zachovat přesnost, omezení zpráv a závislost na průměru; aproximace ani LOCAL algoritmus nestačí.

**4. [Pass complexity of directed reachability in semi-streaming](https://par.nsf.gov/servlets/purl/10488812)**

Lze orientovanou s–t dosažitelnost v libovolném pořadí hran rozhodnout s O(n polylog n) bity paměti za polylogaritmický počet průchodů, nebo jsou nutné polynomiálně mnohé? Základní hranice možností zpracování velkých orientovaných grafů v malé paměti.

Nejbližší karty: TCS-6507, TCS-0993. TCS-6507 je paralelní work/depth otázka; TCS-0993 se ptá na aproximaci vzdáleností. Zde jde o přesnou rozhodovací dosažitelnost a počet streamingových průchodů.

**5. [Explicit superconstant lower bounds in the congested clique](https://people.csail.mit.edu/andyd/cong_clique_podc14.pdf)**

Najít explicitní, centralizovaně polynomiálně řešitelnou rozhodovací grafovou úlohu s jedním výstupním bitem, která v deterministickém unicast congested clique vyžaduje ω(1) komunikačních kol. Základní nepřekonaná bariéra nepodmíněných komunikačních dolních mezí ve velmi silném distribuovaném modelu.

Nejbližší karty: TCS-6501, TCS-0469. MIS algoritmus je konkrétní horní mez. Nejde o úlohy s velkým výstupem, kde omezení množství přenesených bitů dává přímou dolní mez.

Další podklady: [zdroj 2](https://jukkasuomela.fi/doc/clique-complexity.pdf).

**6. [The Li–Li undirected network coding conjecture](https://ics.uci.edu/~vazirani/isit.pdf)**

Zvyšuje síťové kódování dosažitelnou propustnost neorientované kapacitní sítě s několika nezávislými unicast přenosy? Li–Li conjecture tvrdí, že každou asymptoticky dosažitelnou kombinaci rychlostí lze dosáhnout také frakčním multikomoditním směrováním. Kapacita hrany je společná oběma směrům; uzly smějí při kódování zprávy obecně kombinovat. Základní otázka, zda výpočty uvnitř komunikační sítě poskytují výhodu oproti přeposílání informace. Hypotéza pochází z roku 2004 a má také aplikace v dolních mezích pro výpočet.

Nejbližší karty: TCS-0247, TCS-4610. TCS-0247 je Q13 v SIGACT sloupku o Kolmogorovově složitosti: vztah Shannonova a algoritmického informačního toku, nikoli kódování versus routing. Původní Q13 byl přečten. TCS-4610 se týká kvantových výpočtů pomocí měření. V předchozích 69 velkých ani 72 malých návrzích není Li–Li. Multicast a orientované sítě nejsou touto hypotézou pokryty. Zařazení do velké 7 je redakční volba; přirozený přesah je Coding and information theory.

Další podklady: [zdroj 2](https://ieeexplore.ieee.org/document/11195643/), [zdroj 3](https://chekuri.cs.illinois.edu/talks/DIMACS-netcoding.pdf), [zdroj 4](https://ntt-research.com/cis-elaine-shi-2020summit-transcript/).

---

**8. Automata and formal languages — 8 kandidátů**

**1. [Černý conjecture](https://arxiv.org/abs/2608.24245)**

Má každý synchronizující deterministický automat s n stavy resetovací slovo délky nejvýše (n−1)²? Jedna z nejznámějších dlouhodobých hypotéz teorie konečných automatů.

Nejbližší karty: TCS-0119, TCS-5818, TCS-6437. Dokončování částečných automatů, avoiding words a synchronizační hry nejsou obecná Černého hypotéza.

**2. [Generalized star-height problem](https://hal.science/hal-00019978)**

Existuje regulární jazyk, který nelze popsat regulárním výrazem s doplňkem a s nejvýše jednou úrovní vnoření Kleeneho hvězdy? Základní otázka vyjadřovací síly regulárních výrazů s booleovskými operacemi.

Obyčejná star-height hierarchy bez doplňku je jiný, vyřešený problém.

Další podklady: [zdroj 2](https://www.irif.fr/~jep/Problemes/starheight.html).

**3. [Sakoda–Sipser problem](https://journals.sagepub.com/doi/10.3233/FI-2013-879)**

Lze každý obousměrný nedeterministický konečný automat simulovat obousměrným deterministickým automatem s polynomiálním počtem stavů? Hlavní stavově-složitostní otázka síly nedeterminismu při obousměrném čtení vstupu.

Počítáme jednu obecnou otázku, nikoli samostatné omezené varianty simulace.

**4. [Decidability of the full concatenation hierarchy](https://arxiv.org/abs/2401.16195)**

Existuje algoritmus pro membership ve všech úrovních dot-depth/first-order alternation hierarchy regulárních jazyků, pro libovolně zadanou pevnou úroveň? Určuje, zda lze efektivně měřit logickou a algebraickou složitost regulárních jazyků v celé přirozené hierarchii.

Výsledky pro jednotlivé nízké úrovně, včetně dot-depth 3, neřeší všechny úrovně.

**5. [Word equations with linear length constraints](https://arxiv.org/abs/2406.02160)**

Je rozhodnutelná splnitelnost soustav slovních rovnic doplněných lineárními aritmetickými podmínkami na délky proměnných? Základní mezera v teorii řetězců, přímo ovlivňující SMT a verifikaci programů pracujících s textem.

Nejbližší karty: TCS-0163. NP horní mez pro samotné slovní rovnice je jiná otázka; zde není známa ani rozhodnutelnost rozšířené teorie.

Další podklady: [zdroj 2](https://www.lboro.ac.uk/departments/compsci/events/seminars/tcs/2025/word-equations/).

**6. [Equivalence of deterministic macro tree transducers](https://doi.org/10.1016/j.ipl.2022.106332)**

Je rozhodnutelná ekvivalence obecných deterministických macro tree transducerů? Ústřední otevřená otázka ekvivalence programů v expresivním, ale stále strukturovaném modelu stromových transformací.

Ekvivalence s origin informací či omezenými parametry neřeší obecný model.

**7. [First-order definability of regular tree languages](https://lmcs.episciences.org/699)**

Lze z automatu pro konečné uspořádané označené stromy rozhodnout, zda jeho jazyk definujeme first-order logikou se stromovými vztahy, včetně potomka/descendant? Stromová obdoba základní efektivní charakterizace first-order definovatelných slovních jazyků.

Signaturu je třeba fixovat: zde standardní ordered-tree/forest setting s descendant a pořadím sourozenců. Výsledek pro omezenou alternaci není plná FO charakterizace.

Další podklady: [zdroj 2](https://www.mimuw.edu.pl/~bojan/paper).

**8. [Equivalence of higher-order recursion schemes](https://www.cs.rhul.ac.uk/home/uxac009/files/papers/tocl17.pdf)**

Je rozhodnutelné, zda dvě deterministická higher-order recursion schemes generují stejný potenciálně nekonečný označený strom? Hlavní otevřená hranice ekvivalence vyšších rekurzivních programů, propojená s jazykovou ekvivalencí deterministických collapsible pushdown automatů.

Nejbližší karty: TCS-2107, TCS-5858, TCS-4644. Existující karty řeší real-time rozšíření, model checking kvantitativních vlastností nebo omezenou dosažitelnost. Obecná ekvivalence generovaných stromů je jiná otázka.

---

**9. Semantics, logic and verification — 8 kandidátů**

**1. [Decidability of Positivity for linear recurrences](https://people.mpi-sws.org/~joel/publications/skolem_and_positivity_survey26.pdf)**

Lze u libovolné celočíselné lineární rekurentní posloupnosti rozhodnout, zda jsou všechny členy nezáporné? Základní rozhodovací problém pro lineární dynamiku a bezpečnost programů s numerickým stavem.

Nejbližší karty: TCS-0637, TCS-5773. Universal Positivity Sets nejsou obecná rozhodnutelnost Positivity; Skolem se ptá na nulový člen. Ultimate Positivity nepřidáváme zvlášť jen kvůli počtu.

**2. [Unbounded Continuous Skolem Problem](https://people.mpi-sws.org/~joel/publications/skolem_and_positivity_survey26.pdf)**

Lze pro racionální A,b,c rozhodnout, zda cᵀ exp(At)b=0 pro nějaké reálné t≥0? Ústřední otázka dosažitelnosti u spojitých lineárních systémů, tedy přímý základ jejich verifikace.

Nejbližší karty: TCS-1151, TCS-5722, TCS-5773. Existující výňatky se týkají omezeného časového intervalu či diskrétní posloupnosti. Zde je čas spojitý a interval neomezený.

**3. [Simple stochastic games in polynomial time](https://drops.dagstuhl.de/storage/00lipics/lipics-vol366-fun2026/html/LIPIcs.FUN.2026.19/LIPIcs.FUN.2026.19.html)**

Lze v polynomiálním čase rozhodnout, zda optimální pravděpodobnost dosažení cíle v jednoduché stochastické hře překračuje zadaný racionální práh? Kanonická hranice efektivní syntézy při kombinaci protivníka a náhody.

Nejbližší karty: TCS-4140. Konkrétní redukce či omezené třídy arén nejsou obecná polynomiální řešitelnost.

**4. [Mean-payoff games in polynomial time](https://arxiv.org/abs/2607.23754)**

Lze vítěze celočíselně vážené dvouhráčové mean-payoff hry určit v čase polynomiálním v bitové délce vstupu? Základní otázka kvantitativní verifikace a dlouhodobého řízení; pseudopolynomiální algoritmus ji neřeší.

Nejbližší karty: TCS-3519, TCS-4245. TCS-3519 řeší hierarchii kombinovaných cílů a TCS-4245 parity games. Tyto problémy nejsou známé jako ekvivalentní v požadované složitosti.

Další podklady: [zdroj 2](https://doi.org/10.1007/BFb0030814).

**5. [Internal semisimplicial types in ordinary HoTT](https://nicolaikraus.github.io/docs/on_semisimplicial_types.pdf)**

Lze v běžné homotopy type theory interně definovat typ semisimpliciálních typů všech dimenzí, s nekonečnou koherencí a bez přidání druhé vrstvy striktní rovnosti? Základní překážka interního popisu vyšších kategorií a rozsáhlé formalizace homotopické matematiky.

Pevné konečné dimenze a řešení v two-level type theory neřeší formulaci uvnitř původní teorie.

Další podklady: [zdroj 2](https://www.cambridge.org/core/journals/mathematical-structures-in-computer-science/article/twolevel-type-theory-and-applications/4914DB4F8E8305DFC68F9CDCA9D0C8D0).

**6. [Scott-continuous model with exactly λβ equational theory](https://arxiv.org/abs/math/0701684)**

Existuje model netypovaného lambda kalkulu ve Scottově spojité sémantice, jehož rovnost termů je přesně β-konvertibilita? Klasická otázka úplnosti denotační sémantiky: zda význam může zachovat přesně syntaktickou rovnost základního modelu programování.

Syntaktická termová algebra není požadovaný Scott-continuous denotační model.

Další podklady: [zdroj 2](https://cgi.cse.unsw.edu.au/~eptcs/paper.cgi?LSFA2012.8.pdf).

**7. [Hilbert’s tenth problem over the rationals](https://math.mit.edu/~poonen/papers/aws2003.pdf)**

Existuje algoritmus rozhodující, zda polynom s celočíselnými koeficienty v libovolném počtu proměnných má racionální řešení? Jedna z hlavních otevřených hranic rozhodnutelnosti aritmetických teorií.

Nerozhodnutelnost nad celými čísly, ani nad okruhy celých čísel číselných těles, neřeší racionální těleso. Zařazení: rozhodnutelnost v logice.

Další podklady: [zdroj 2](https://math.mit.edu/~poonen/slides/sample_slides.pdf).

**8. [Barendregt–Geuvers–Klop conjecture](https://tlca.di.unito.it/opltlca/problem9.pdf)**

Je každý slabě normalizující pure type system také silně normalizující? Klasická obecná otázka základů typových systémů: zda existence ukončující redukce pro každý typovatelný term vynucuje ukončení každé redukce.

Nejbližší karty: TCS-0892. TCS-0892 žádá konkrétní formu důkazu normalizace typovaného lambda kalkulu; zde jde o obecnou implikaci pro celou rodinu PTS.

Další podklady: [zdroj 2](https://drops.dagstuhl.de/storage/00lipics/lipics-vol269-types2022/LIPIcs.TYPES.2022.7/LIPIcs.TYPES.2022.7.pdf).

---

**10. Optimization and numerics — 9 kandidátů**

**1. [A polynomial-time pivot rule for the simplex method](https://arxiv.org/abs/2502.18019)**

Existuje pivotovací pravidlo pro simplex, které každou racionální lineární úlohu vyřeší v počtu bitových operací polynomiálním v délce vstupu? Základní nevysvětlená mezera mezi mimořádným praktickým úspěchem simplexové metody a její obecnou teorií.

Nejbližší karty: TCS-0008, TCS-4088. Silně polynomiální LP je jiný cíl: zde je algoritmus omezen na simplex, ale může záviset na bitové délce čísel. Exponenciální příklady pro jednotlivá pravidla neřeší existenci vhodného pravidla.

Další podklady: [zdroj 2](https://arxiv.org/abs/2507.16648).

**2. [Polynomial Hirsch conjecture](https://ti.inf.ethz.ch/ew/courses/Geo25/lecture/gca25-10.pdf)**

Je průměr hranového grafu libovolného d-rozměrného polyedru s n fasetami omezen polynomem v n a d? Základní strukturální překážka krátkých cest po přípustných bázích lineárního programování.

Původní lineární Hirschova mez byla vyvrácena; kandidátem je polynomiální mez, nikoli stará nepravdivá hypotéza.

**3. [Polynomial-time exact semidefinite feasibility](https://epubs.siam.org/doi/full/10.1137/21M1434945)**

Lze v Turingově modelu v polynomiálním čase rozhodnout, zda racionálně zadaný afinní podprostor obsahuje pozitivně semidefinitní matici? Základní nevyjasněná výpočetní hranice semidefinitní optimalizace, včetně degenerovaných a slabě nepřípustných instancí.

Polynomiální slabá aproximace za regularitních předpokladů není přesná rozhodnutelnost feasibility.

**4. [Deterministic k-server conjecture](https://arxiv.org/abs/2211.05753)**

Existuje pro každou metriku deterministický k-kompetitivní algoritmus pro problém k serverů? Jedna z ústředních dlouhodobých hypotéz online optimalizace.

Nejbližší karty: TCS-4983, TCS-1634. TCS-4983 se ptá na randomizovaný o(k) poměr. Zde jde o optimální deterministický poměr k. Původní randomizovaná O(log k) hypotéza už je vyvrácena.

**5. [Optimal competitive ratio for convex body chasing](https://theory.epfl.ch/WinterSchool2025/slides/2025/Gupta_lec4-chasing.pdf)**

Jaký je optimální deterministický kompetitivní poměr pro convex body chasing v d-rozměrném eukleidovském prostoru; lze uzavřít mezeru mezi Ω(√d) a O(d)? Kanonický geometrický model online optimalizace s náklady na přesun.

Pouhá existence poměru závislého jen na dimenzi už byla dokázána; kandidátem je jeho optimální řád.

**6. [Minimax dimension dependence in bandit convex optimization](https://tor-lattimore.com/downloads/cvx-book/cvx.pdf)**

Jaký je optimální minimax regret jako funkce dimenze d a horizontu T pro adversarial bandit convex optimization s jedním pozorováním hodnoty za kolo? Určuje skutečnou cenu omezené zpětné vazby v základním modelu online konvexní optimalizace.

Nejbližší karty: TCS-0711. Jde o celý minimax řád, nikoli doladění konkrétního algoritmu. Contextual-bandit model selection je odlišná otázka.

Další podklady: [zdroj 2](https://www.cambridge.org/core/books/abs/bandit-convex-optimisation/outlook/FAEE9479EE720E949F7CECDADCE307D5).

**7. [Smale’s seventh problem](https://www.lebesgue.fr/sites/default/files/inline-files/Yakir.pdf)**

Lze v polynomiálním čase v N sestrojit N bodů na sféře, jejichž logaritmická energie se liší od globálního minima nejvýše o C log N pro univerzální C? Jeden ze Smaleových hlavních problémů: efektivní konstrukce téměř optimálních globálních konfigurací.

Jde o Smale 7, nikoli o Smale 17, který již byl vyřešen. Zařazení je na rozhraní numeriky a geometrie.

**8. [Crouzeix’s conjecture](https://ris.utwente.nl/ws/portalfiles/portal/171656886/17m1143757.pdf)**

Platí pro každou komplexní čtvercovou matici A a polynom p nerovnost ||p(A)||₂ ≤ 2 max{|p(z)|: z∈W(A)}, kde W(A) je numerický obor hodnot? Základní otázka maticové funkcionální kalkuly s důsledky pro analýzu numerických maticových algoritmů.

Numerická lineární algebra, tedy výslovně přijatá numerics část kategorie.

Další podklady: [zdroj 2](https://www.sciencedirect.com/science/article/pii/S0024379523004585).

**9. [Nearly linear-time solution of general sparse linear systems](https://arxiv.org/abs/2007.10254)**

Lze obecnou nesingulární soustavu Ax=b s n proměnnými a m nenulovými koeficienty řešit s relativním reziduem ||Ax-b||₂ ≤ ε||b||₂ v čase m·polylog(nκ/ε), kde κ je číslo podmíněnosti? Konkrétní cílový režim má racionální vstupy s O(log n) bity, κ ≤ poly(n) a ε = 1/poly(n); započítává se práce s konečnou přesností a výstupem je celý aproximující vektor. Ústřední hranice algoritmické numerické lineární algebry, s dopadem na optimalizaci a vědecké výpočty. Téměř lineární řešiče speciálních tříd matic neposkytují takový algoritmus pro obecné řídké soustavy.

Nejbližší karty: TCS-6120, TCS-0046. TCS-6120 po přečtení původní strany 6 řeší vliv vložitelnosti simpliciálního komplexu do R³ na rychlost řešiče; obecný problém se tím neduplikuje. TCS-0046 řeší tropické/min-plus soustavy, odlišnou algebru. Kontrolovány také oba předchozí návrhy. Překonání času násobení matic již vyřešili Peng a Vempala: není zde navrhováno jako otevřená otázka.

Další podklady: [zdroj 2](https://arxiv.org/abs/2602.05394), [zdroj 3](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.ICALP.2022.53), [zdroj 4](https://simons.berkeley.edu/workshops/linear-systems-eigenvalue-problems).

---

**Doklady kontroly**

[novelty-audit.json](novelty-audit.json) uchovává vyhledané shody a redakční závěr. Počet regex shod není počet duplicit. [Komprimovaný snímek formulací](catalog-question-snapshot.json.gz) zachovává vstup kontroly, protože katalog se souběžně mění. Zdroje jsou připojené přímo k jednotlivým otázkám.

SHA-256 původního catalog.json: `4f7649542c42d0d79694144f0714b7d84a830932b635f00900c7c572d9ddffe7`.
