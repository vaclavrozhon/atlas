# 100 výzkumníků TCS: 200 osobně přiřazených otevřených problémů

Pro každého vybírám dvě otázky v původním pořadí seznamu. Přiřazení je můj odhad podle jejich hlavních výsledků a navazujícího výzkumu; není to tvrzení o jejich současném osobním seznamu priorit. Krátká věta u jména vysvětluje vazbu.

Otázky jsou formulované jako konkrétní ano/ne problémy. Příbuzné varianty ponechávám, ale tentýž problém neopakuji. Odkazy vedou k původním pracím, odborným přehledům nebo autorským formulacím. Rešerše zachycuje dohledatelné výsledky k 11. září 2026; otevřenost je třeba číst pro uvedený model a parametry.

Některé algoritmické otázky mají známou podmíněnou zápornou odpověď, například za ETH nebo UGC. Není-li dodatečná hypotéza součástí otázky, ptám se na nepodmíněnou existenci algoritmu. U kryptografických implikací připouštím i ne-black-box konstrukce; známá black-box separace sama otázku neuzavírá.

Značení: poly znamená polynomiální závislost; Õ potlačuje polylogaritmické faktory. FPRAS je randomizované aproximační schéma s relativní chybou ε a časem polynomiálním ve vstupu a 1/ε. H₂ je binární entropie; VC a LD označují VC dimenzi a Littlestoneovu dimenzi.

**1. Donald Knuth** — Sčítací řetězce a přesná složitost algoritmů, které podrobně rozvíjí v TAOCP.

- **A.** Platí Scholzova–Brauerova domněnka ℓ(2ⁿ−1) ≤ n−1+ℓ(n), kde ℓ(n) je délka nejkratšího sčítacího řetězce pro n? [Scholzova domněnka](https://math.colgate.edu/~integers/a17Proc23/a17Proc23.pdf)
- **B.** Lze délku nejkratšího sčítacího řetězce pro binárně zadané n spočítat v čase poly(log n)? [Složitost sčítacích řetězců](https://faculty.eng.fau.edu/azarderakhsh/files/2016/11/Inscrypt2016.pdf)

**2. Robert Tarjan** — Přímé pokračování jeho práce na splay stromech a amortizované analýze.

- **A.** Jsou splay stromy dynamicky optimální: stojí každá posloupnost přístupů jen konstantní násobek optimálního offline BST, s obvyklým aditivním členem O(n)? [Splay trees are almost dynamically optimal](https://arxiv.org/abs/2607.18498)
- **B.** Platí deque conjecture: mají operace vložení a odebrání na obou koncích pomocí splay stromu celkovou cenu O(m+n)? [In pursuit of the dynamic optimality conjecture](https://arxiv.org/abs/1306.0207)

**3. John Hopcroft** — Jeho párovací algoritmy a minimalizace konečných automatů.

- **A.** Existuje algoritmus pro přesné maximální párování v obecném neorientovaném grafu v čase m^{1+o(1)}+O(n)? [Alternating paths and blossoms](https://pubsonline.informs.org/doi/abs/10.1287/moor.2020.0388)
- **B.** Lze libovolný n-stavový úplný deterministický automat nad pevnou alespoň dvoupísmennou abecedou minimalizovat v čase O(n) na word-RAM? [Minimization of Symbolic Automata](https://cseweb.ucsd.edu/~ldantoni/papers/popl14.pdf)

**4. Volker Strassen** — Exponent násobení matic a jeho asymptotická teorie tenzorů.

- **A.** Je exponent násobení matic ω roven 2? [Asymptotic tensor rank](https://arxiv.org/abs/2411.15789)
- **B.** Má každý komplexní n×n×n tenzor s plnou hodností všech tří zploštění asymptotickou tenzorovou hodnost n? [Strassenova asymptotická domněnka](https://arxiv.org/abs/2411.15789)

**5. Kurt Mehlhorn** — Spolehlivá geometrická aritmetika a optimální grafové algoritmy.

- **A.** Je v P porovnávání dvou součtů odmocnin nezáporných celých čísel zadaných binárně? [Sum of Square Roots](https://topp.openproblem.net/p33)
- **B.** Lze minimální kostru grafu s reálnými vahami najít deterministicky v O(m+n) čase v porovnávacím modelu? [Chazellův algoritmus pro MST](https://www.cs.princeton.edu/~chazelle/pubs/mst.pdf)

**6. Mikkel Thorup** — Jeho rychlé celočíselné algoritmy a výsledek pro neorientované SSSP.

- **A.** Lze n celých čísel, každé uložené v jednom w-bitovém slově, setřídit v očekávaném O(n) čase na word-RAM pro každé w≥log n? [Han–Thorup: Integer Sorting](https://doi.org/10.1109/SFCS.2002.1181890)
- **B.** Lze SSSP v orientovaném grafu s kladnými celočíselnými vahami spočítat v O(m+n) čase na word-RAM? [Breaking the Sorting Barrier for Directed SSSP](https://arxiv.org/abs/2504.17033)

**7. Monika Henzinger** — Dynamické grafy a podmíněné dolní meze, včetně její OMv práce.

- **A.** Existuje deterministická plně dynamická struktura pro neorientovanou souvislost s polylogaritmickým časem aktualizace i dotazu v nejhorším případě? [Dynamic graph connectivity](https://doi.org/10.1137/1.9781611973105.81)
- **B.** Platí OMv domněnka: vyžaduje online násobení pevné booleovské n×n matice postupně přicházejícími n vektory čas n^{3−o(1)}, i s randomizací? [OMv: Henzinger a spoluautoři](https://arxiv.org/abs/1511.06773)

**8. Virginia Vassilevska Williams** — Dvě ústřední otázky jemné složitosti, na jejímž rozvoji se podílela.

- **A.** Má přesné APSP s celočíselnými vahami o polylogaritmické bitové délce algoritmus v čase O(n^{3−ε}) pro nějaké pevné ε>0? [Subcubic Equivalences](https://doi.org/10.1109/FOCS.2010.67)
- **B.** Má 3SUM na reálném RAM algoritmus v čase O(n^{2−ε}) pro nějaké pevné ε>0? [Threesomes, Degenerates, and Love Triangles](https://arxiv.org/abs/1404.0799)

**9. Erik Demaine** — Jeho dlouhodobý program geometrického skládání a rozkládání.

- **A.** Lze povrch každého konvexního mnohostěnu rozstřihnout pouze podél hran do jediného nepřekrývajícího se rovinného dílu? [Demaine: Unfolding](https://courses.csail.mit.edu/6.849/fall12/lectures/L15.html)
- **B.** Lze povrch každého mnohostěnu homeomorfního sféře rozstřihnout do jediného nepřekrývajícího se rovinného dílu, dovolíme-li řezy i skrz stěny? [Demaine: General Unfolding](https://courses.csail.mit.edu/6.849/fall12/lectures/L15.html)

**10. Julia Chuzhoy** — Grid minors a disjunktní cesty jsou přímo jádrem jejích průlomů.

- **A.** Existuje konstanta C taková, že každý graf s treewidth alespoň Ck² log k obsahuje k×k mřížku jako minor? [Towards Tight(er) Bounds for the Excluded Grid Theorem](https://arxiv.org/abs/1901.07944)
- **B.** Má maximalizace počtu propojených dvojic hranově disjunktními cestami v neorientovaných grafech polylogaritmickou aproximaci bez povolení kongesce? [Chuzhoy–Li: Edge-Disjoint Paths](https://arxiv.org/abs/1208.1272)

**11. Ravindran Kannan** — Log-konkávní geometrie a celočíselné programování v pevné dimenzi.

- **A.** Platí KLS domněnka: má každá izotropní log-konkávní míra Poincarého konstantu omezenou univerzální konstantou nezávislou na dimenzi? [The Kannan–Lovász–Simonovits Conjecture](https://faculty.cc.gatech.edu/~vempala/papers/kls_survey.pdf)
- **B.** Lze celočíselné lineární programování v n proměnných řešit v čase 2^{O(n)}·poly(L), kde L je bitová délka vstupu? [From Approximate to Exact Integer Programming](https://pmc.ncbi.nlm.nih.gov/articles/PMC11870894/)

**12. Stephen Cook** — SAT a Cookovy–Reckhowovy důkazové systémy.

- **A.** Je P = NP? [Clay: P versus NP](https://www.claymath.org/millennium/p-vs-np/)
- **B.** Existuje rodina tautologií, jejichž nejkratší důkazy v systému Extended Frege mají superpolynomiální délku? [Cook–Reckhow: Propositional Proof Systems](https://www.cs.toronto.edu/~sacook/homepage/cook_reckhow.pdf)

**13. Richard Karp** — Jeho práce na párování, paralelismu a randomizovaných algoritmech.

- **A.** Je existence perfektního párování v obecném grafu rozhodnutelná v deterministické třídě NC? [General Matching in Quasi-NC](https://doi.org/10.1109/FOCS.2017.70)
- **B.** Existuje FPRAS pro počet perfektních párování v obecném, nikoli nutně bipartitním grafu? [Approximating the Permanent](https://doi.org/10.1137/0218077)

**14. Leonid Levin** — Průměrná složitost a univerzální pohled na inverzi výpočtů.

- **A.** Existují jednosměrné funkce, tedy polynomiálně spočitatelné funkce obtížně invertovatelné v průměru pro každý pravděpodobnostní polynomiální algoritmus? [Average-Case Complexity](https://arxiv.org/abs/cs/0606037v3)
- **B.** Implikuje P≠NP existenci distribučního problému z NP se vzorkovatelnou distribucí vstupů, který neleží v AvgP? [Average-Case Complexity](https://arxiv.org/abs/cs/0606037v3)

**15. Manuel Blum** — Jeho kryptografie založená na aritmetice a práce s pseudonáhodností.

- **A.** Existuje klasický randomizovaný algoritmus, který faktorizuje libovolné N v čase poly(log N)? [Survey of Number-Theoretic Algorithms](https://www.csa.iisc.ac.in/~chandan/research/survey_CNT.pdf)
- **B.** Lze pro každé n deterministicky sestrojit n-bitové prvočíslo v čase poly(n), bez neprokázaných číselněteoretických předpokladů? [Explicit Construction of Primes](https://eccc.weizmann.ac.il/report/2022/081/)

**16. Leslie Valiant** — Algebraická složitost a rigidita matic jako cesta k dolním mezím.

- **A.** Platí VP≠VNP nad komplexními čísly, ekvivalentně: nemá permanent aritmetické obvody polynomiální velikosti? [Completeness Classes in Algebra](https://doi.org/10.1145/800135.804419)
- **B.** Lze v poly(n) čase sestrojit racionální n×n matice, u nichž snížení hodnosti pod n/2 vyžaduje změnit alespoň n^{1+ε} položek pro nějaké pevné ε>0? [Valiantův program rigidity](https://www.wisdom.weizmann.ac.il/~oded/VO/rigid.pdf)

**17. Andrew Yao** — Komunikační složitost a základy bezpečného dvoustranného výpočtu.

- **A.** Platí log-rank conjecture: je deterministická komunikační složitost každé úplné booleovské funkce polynomiálně omezená logaritmem reálné hodnosti její komunikační matice? [The Log-Rank Conjecture](https://arxiv.org/abs/2510.02583v3)
- **B.** Implikuje existence šifrování s veřejným klíčem existenci bezpečného oblivious transfer ve standardním modelu? [Public-Key Encryption and Oblivious Transfer](https://vmahesh.cs.illinois.edu/papers/focs00.pdf)

**18. Avi Wigderson** — Hardness versus randomness a jeho algebraické metody.

- **A.** Je P = BPP, tedy lze odstranit randomizaci z každého polynomiálního rozhodovacího algoritmu s omezenou chybou? [Impagliazzo–Wigderson: Derandomization](https://www.math.ias.edu/~avi/PUBLICATIONS/MYPAPERS/IW97/proc.pdf)
- **B.** Existuje deterministický polynomiální algoritmus pro testování identity obecného aritmetického obvodu nad racionálními čísly? [Mathematics and Computation](https://www.math.ias.edu/files/Book-online-Aug0619.pdf)

**19. László Babai** — Izomorfismus grafů a výpočetní teorie konečných grup.

- **A.** Je izomorfismus obecných grafů v P? [Graph Isomorphism in Quasipolynomial Time](https://arxiv.org/abs/1512.03547)
- **B.** Lze v polynomiálním čase rozhodnout izomorfismus dvou konečných grup zadaných úplnými tabulkami násobení? [Parameterized Complexity of Graph Isomorphism](https://epub.uni-regensburg.de/78630/1/1-s2.0-S1574013726000274-main.pdf)

**20. Miklós Ajtai** — Obtížnost mřížkových problémů, která je základem jeho kryptografického programu.

- **A.** Je přesný problém nejkratšího vektoru v eukleidovské normě NP-těžký pod deterministickými polynomiálními redukcemi? [The Complexity of the Shortest Vector Problem](https://www.cs.umd.edu/~gasarch/open/svp-color.pdf)
- **B.** Je pro nějaké pevné ε>0 aproximace eukleidovského SVP v dimenzi n na faktor n^ε NP-těžká pod randomizovanými polynomiálními redukcemi? [The Complexity of the Shortest Vector Problem](https://www.cs.umd.edu/~gasarch/open/svp-color.pdf)

**21. Alexander Razborov** — Obvodové dolní meze a dolní meze pro silné důkazové systémy.

- **A.** Platí NP⊄P/poly: vyžaduje nějaký jazyk z NP booleovské obvody superpolynomiální velikosti? [Natural Proofs](https://doi.org/10.1006/jcss.1997.1494)
- **B.** Existují tautologie vyžadující superpolynomiálně dlouhé důkazy v běžném Fregeho systému? [Mathematics and Computation](https://www.math.ias.edu/files/Book-online-Aug0619.pdf)

**22. Johan Håstad** — Prahové obvody a Fourierova analýza booleovských funkcí.

- **A.** Platí TC⁰⊊NC¹ pro neuniformní obvody? [Bootstrapping Results for Threshold Circuits](https://eccc.weizmann.ac.il/report/2018/199/)
- **B.** Platí Fourier entropy–influence conjecture: je entropie čtverců Fourierových koeficientů každé booleovské funkce nejvýše konstantní násobek její celkové influence? [A New Bound for the Fourier-Entropy-Influence Conjecture](https://arxiv.org/abs/2312.08271)

**23. Sanjeev Arora** — Geometrické aproximace a algoritmické hranice učení latentní struktury.

- **A.** Existuje polynomiální aproximace uniformního Sparsest Cut s absolutně konstantním aproximačním faktorem? [Lecture Notes on the ARV Algorithm](https://arxiv.org/abs/1607.00854)
- **B.** Lze pro nějaké pevné ε>0 v polynomiálním čase s vysokou pravděpodobností odlišit G(n,1/2) od téhož grafu s vloženou klikou velikosti n^{1/2−ε}? [A Nearly Tight SoS Lower Bound for Planted Clique](https://doi.org/10.1137/17M1138236)

**24. Madhu Sudan** — List decoding a meze dosažitelných parametrů kódů.

- **A.** Existuje rodina standardních Reedových–Solomonových kódů konstantní rychlosti R, kterou lze polynomiálně list-dekódovat z podílu chyb alespoň 1−√R+ε pro pevné ε>0? [Algorithmic RS list decoding, ICALP 2026](https://drops.dagstuhl.de/storage/00lipics/lipics-vol374-icalp2026/html/LIPIcs.ICALP.2026.43/LIPIcs.ICALP.2026.43.html)
- **B.** Existují pro nějaké pevné 0<δ<1/2 binární kódy s asymptotickou rychlostí ostře větší než 1−H₂(δ) a relativní vzdáleností alespoň δ? [Guruswami: Coding Theory](https://www.cs.cmu.edu/~venkatg/teaching/codingtheory/)

**25. Irit Dinur** — Délka PCP důkazů a zesilování mezery v jejich ověřování.

- **A.** Má 3-SAT PCP s délkou důkazu O(N), konstantní abecedou, konstantním počtem dotazů a konstantní mezerou mezi úplností a korektností, pro vstupy délky N? [Dinur: Local-to-Global](https://www.wisdom.weizmann.ac.il/~dinuri/courses/25-loc2glob/)
- **B.** Platí sliding-scale conjecture: má NP polynomiálně dlouhé PCP s konstantním počtem dotazů, polynomiálně velkou abecedou a chybou korektnosti N^{-c} pro nějaké c>0? [Polynomially Low Error PCPs](https://arxiv.org/abs/1505.06362)

**26. Subhash Khot** — Jeho Unique Games program a geometrie obtížných aproximačních instancí.

- **A.** Platí UGC: je pro každé ε>0 a vhodnou konstantní abecedu NP-těžké rozlišit Unique Games s optimem alespoň 1−ε od těch s optimem nejvýše ε? [Khot: On the Unique Games Conjecture](https://cs.nyu.edu/~khot/papers/UGCSurvey.pdf)
- **B.** Platí Small-Set Expansion Hypothesis: je pro každé ε>0 a vhodné konstantní δ>0 NP-těžké odlišit existenci δn-vrcholové množiny s expanzí ≤ε od expanze ≥1−ε všech takových množin? [Reductions Between Expansion Problems](https://arxiv.org/abs/1011.2586)

**27. Russell Impagliazzo** — Dvě jeho vlastní základní hypotézy o exponenciální složitosti SAT.

- **A.** Platí ETH: nemá 3-SAT na n proměnných algoritmus v čase 2^{o(n)}·poly(vstup)? [Impagliazzo–Paturi: On the Complexity of k-SAT](https://cseweb.ucsd.edu/~paturi/myPapers/pubs/ImpagliazzoPaturi_2001_jcss.pdf)
- **B.** Platí SETH: pro každé ε>0 existuje k, pro které nelze k-SAT řešit v čase O((2−ε)^n) až na polynomiální faktor? [Impagliazzo–Paturi: On the Complexity of k-SAT](https://cseweb.ucsd.edu/~paturi/myPapers/pubs/ImpagliazzoPaturi_2001_jcss.pdf)

**28. Ran Raz** — Jeho dolní meze pro multilineární výpočty a struktura algebraických modelů.

- **A.** Platí VBP≠VP nad komplexními čísly, tedy jsou polynomiálně velké algebraické větvící programy slabší než obecné aritmetické obvody? [Closure of Algebraic Complexity Classes under Factoring](https://eccc.weizmann.ac.il/report/2025/083/revision/1/download/)
- **B.** Vyžaduje permanent n×n matice multilineární aritmetické formule velikosti 2^{Ω(n)}? [Multilineární formule a exponenciální dolní meze](https://eccc.weizmann.ac.il/report/2017/004/)

**29. Ryan Williams** — Přesun od rychlejšího SAT k silnějším obvodovým dolním mezím.

- **A.** Platí NEXP⊄TC⁰? [Bootstrapping Results for Threshold Circuits](https://eccc.weizmann.ac.il/report/2018/199/)
- **B.** Má SAT pro obecné booleovské obvody s n vstupy a nejvýše cn hradly algoritmus v čase (2−ε_c)^n·poly(n), pro každou pevnou konstantu c a nějaké ε_c>0? [Mathematics and Computation](https://www.math.ias.edu/files/Book-online-Aug0619.pdf)

**30. Omer Reingold** — Dosažitelnost v malé paměti a explicitní náhrady náhodné procházky.

- **A.** Platí L = NL, tedy lze orientovanou dosažitelnost řešit deterministicky v logaritmické paměti? [Mathematics and Computation](https://www.math.ias.edu/files/Book-online-Aug0619.pdf)
- **B.** Lze explicitně v polynomiálním čase sestrojit polynomiálně dlouhou univerzální traversal sequence pro všechny d-regulární neorientované grafy s libovolným lokálním číslováním portů? [Vadhanovy poznámky k Reingoldovu algoritmu](https://people.seas.harvard.edu/~salil/cs225/spring07/lecnotes/lec9.pdf)

**31. David Zuckerman** — Jeho dvouzdrojové extraktory a explicitní Ramseyovy konstrukce.

- **A.** Existuje polynomiálně spočitatelný dvouzdrojový extraktor pro nezávislé n-bitové zdroje s min-entropií log₂n+O(1), který vydá jeden bit s chybou nejvýše 0,01? [Gödel Prize 2025: Two-Source Extractors](https://sigact.org/prizes/g%C3%B6del/citation2025.html)
- **B.** Lze deterministicky v poly(N) čase sestrojit N-vrcholový graf bez kliky i nezávislé množiny větší než C log N, pro absolutní konstantu C? [Zuckermanův výzkum](https://www.cs.utexas.edu/~diz/)

**32. Salil Vadhan** — Optimální parametry pseudonáhodnosti a strukturální teorie zero knowledge.

- **A.** Existují explicitní silné seeded extractors s délkou seedu d=log₂n+O(log(1/ε)) a výstupem m≥k−O(log(1/ε)), současně pro všechny přípustné parametry? [Optimální parametry explicitních extraktorů](https://eccc.weizmann.ac.il/report/2024/176/revision/2/download/)
- **B.** Platí NISZK = SZK, tedy lze ze statistického zero knowledge odstranit interakci při povolení společného náhodného řetězce? [Can Statistical Zero Knowledge Be Made Non-interactive?](https://doi.org/10.1007/3-540-48405-1_30)

**33. Pavel Pudlák** — Jeho program porovnávání důkazových systémů a disjunktních NP dvojic.

- **A.** Existuje p-optimální propoziční důkazový systém, který polynomiálně simuluje každý jiný takový systém? [Pudlák: Incompleteness in the Finite Domain](https://arxiv.org/abs/1601.01487)
- **B.** Existuje disjunktní NP dvojice úplná pro všechny disjunktní NP dvojice pod polynomiálními many-one redukcemi? [Pudlák: Incompleteness in the Finite Domain](https://arxiv.org/abs/1601.01487)

**34. Shafi Goldwasser** — Minimální předpoklady pro šifrování a přesná síla zero knowledge.

- **A.** Implikuje samotná existence jednosměrných funkcí existenci šifrování s veřejným klíčem ve standardním modelu? [MIT: Foundations of Cryptography](https://mit6875.github.io/FA23SLIDES/lec10.pdf)
- **B.** Platí SZK = PZK: lze každý statistický zero-knowledge důkaz nahradit perfektním zero-knowledge důkazem? [Goldwasserové otevřená otázka](https://simons.berkeley.edu/open-problems-cryptography-summer-2015)

**35. Silvio Micali** — Neinteraktivní důkazy a základy kryptografické pseudonáhodnosti.

- **A.** Stačí jednosměrné funkce ke konstrukci neinteraktivního zero knowledge pro celé NP v modelu společného náhodného řetězce? [Commitment Schemes and Zero-Knowledge Protocols](https://homepages.cwi.nl/~schaffne/courses/crypto/2014/papers/ComZK08.pdf)
- **B.** Implikuje existence jednosměrných funkcí existenci jednosměrných permutací? [Limits on the Provable Consequences of One-Way Functions](https://www2.eecs.berkeley.edu/Pubs/TechRpts/1988/6060.html)

**36. Oded Goldreich** — Jeho lokální kryptografické konstrukce a vztahy mezi základními předpoklady.

- **A.** Implikuje existence libovolné jednosměrné funkce existenci jednosměrné funkce počitatelné v NC⁰? [Goldreich’s One-Way Function Candidate](https://www.iacr.org/archive/tcc2009/54440520/54440520.pdf)
- **B.** Implikuje existence jednosměrných funkcí existenci rodin hashovacích funkcí odolných proti hledání kolizí? [Finding Collisions on a One-Way Street](https://link.springer.com/chapter/10.1007/BFb0054137)

**37. Ronald Rivest** — Přesná bezpečnost RSA a odolnost šifrování proti aktivním útokům.

- **A.** Je inverze RSA s veřejným exponentem 65537 na náhodných šifrových textech polynomiálně ekvivalentní faktorizaci náhodných platných RSA modulů? [Boneh: Twenty Years of Attacks on RSA](https://crypto.stanford.edu/~dabo/papers/RSA-survey.pdf)
- **B.** Lze z každého IND-CPA bezpečného šifrování s veřejným klíčem sestrojit IND-CCA2 bezpečné šifrování ve standardním modelu? [Separation of Semantic and CCA Security](https://www.iacr.org/archive/tcc2007/43920433/43920433.pdf)

**38. Adi Shamir** — Secret sharing a hledání algoritmických slabin kryptografických předpokladů.

- **A.** Existují přístupové struktury pro n účastníků, které v každém perfektním secret-sharing schématu vyžadují podíl velikosti 2^{Ω(n)} násobků délky tajemství? [Secret Sharing and Share Size](https://eprint.iacr.org/2019/174.pdf)
- **B.** Lze LPN s pevnou konstantní mírou šumu 0<η<1/2 řešit v čase polynomiálním v dimenzi? [Noise-Tolerant Learning and the Parity Problem](https://www.microsoft.com/en-us/research/wp-content/uploads/2016/11/2003-Noise-Tolerant_Learning.pdf)

**39. Cynthia Dwork** — Informační a výpočetní cena diferenciálního soukromí.

- **A.** Má každá konečná booleovská třída soukromý realizovatelný PAC learner se vzorkovou složitostí poly(VC, log*LD), pro konstantní přesnost a (1,1/(100m²))-DP? [Does Differential Privacy Make PAC Learning Much Harder?](https://proceedings.mlr.press/v336/nissim26a.html)
- **B.** Lze z databáze o m=poly(d) binárních d-rozměrných záznamech v polynomiálním čase vytvořit (1,1/(100m²))-DP stručný výstup, který polynomiálně odpoví na všechny marginals s jednotnou chybou o(1)? [Vadhan: The Complexity of Differential Privacy](https://projects.iq.harvard.edu/files/privacytools/files/complexityprivacy_1_01.pdf)

**40. Oded Regev** — Jeho redukce k LWE a možnost kvantových algoritmů pro mřížky.

- **A.** Existuje klasická redukce z nejhoršího případu mřížkových problémů na LWE s polynomiálním modulem, která zachová dimenzi i aproximační sílu Regevovy kvantové redukce? [Classical Hardness of Learning with Errors](https://arxiv.org/abs/1306.0281)
- **B.** Existuje kvantový polynomiální algoritmus, který pro libovolnou n-rozměrnou mřížku najde nenulový vektor nejvýše n^C-krát delší než nejkratší, pro nějakou konstantu C? [Regev: On Lattices, LWE, and Cryptography](https://cims.nyu.edu/~regev/papers/qcrypto.pdf)

**41. Craig Gentry** — Minimální předpoklady pro výpočty nad šifrovanými daty a obfuskaci.

- **A.** Implikuje existence libovolného šifrování s veřejným klíčem existenci kompaktního plně homomorfního šifrování ve standardním modelu? [On the Power of Hierarchical IBE](https://eprint.iacr.org/2015/815.pdf)
- **B.** Lze indistinguishability obfuscation pro obecné obvody založit jen na běžné polynomiální obtížnosti LWE? [Otevřené problémy kryptografie](https://simons.berkeley.edu/open-problems-cryptography-summer-2015)

**42. Dan Boneh** — Párování, multilineární mapy a identity-based encryption.

- **A.** Existují efektivně počitatelné netriviální trilineární mapy v grupách s jednoznačným kódováním prvků a obtížným diskrétním logaritmem? [Bonehova otázka o trilineárních mapách](https://simons.berkeley.edu/open-problems-cryptography-summer-2015)
- **B.** Implikuje samotná existence šifrování s veřejným klíčem existenci identity-based encryption pro exponenciálně mnoho identit ve standardním modelu? [Generic-Group Identity-Based Encryption](https://eprint.iacr.org/2021/745.pdf)

**43. Yael Tauman Kalai** — Její succinct arguments a program doubly efficient interactive proofs.

- **A.** Lze succinct noninteractive arguments pro celé NP v CRS modelu založit pouze na standardním LWE? [SNARGs for NP from Unprovability of Mathematical Theorems](https://eccc.weizmann.ac.il/report/2026/098/)
- **B.** Má každý výpočet v čase T a prostoru S interaktivní důkaz s poctivým dokazovatelem v poly(T) čase a ověřovatelem v poly(n+S) čase? [Towards a Doubly Efficient IP=PSPACE](https://eccc.weizmann.ac.il/report/2026/102/)

**44. Vinod Vaikuntanathan** — Základní mřížkové konstrukce a jejich bezpečnostní předpoklady.

- **A.** Lze kompaktní neomezeně hluboké FHE založit pouze na LWE, bez dodatečného předpokladu kruhové či KDM bezpečnosti? [Efficient Fully Homomorphic Encryption from Standard LWE](https://epubs.siam.org/doi/10.1137/120868669)
- **B.** Implikuje standardní obtížnost LWE existenci jednosměrných permutací? [Vaikuntanathanova otázka o permutacích](https://simons.berkeley.edu/open-problems-cryptography-summer-2015)

**45. Éva Tardos** — Silná polynomiálnost a klasická aproximace plánování na nesouvisejících strojích.

- **A.** Existuje silně polynomiální algoritmus pro obecné racionální lineární programování? [Tardos: Strongly Polynomial Combinatorial LP](https://doi.org/10.1287/opre.34.2.250)
- **B.** Existuje polynomiální (2−ε)-aproximace minimalizace makespanu na nesouvisejících paralelních strojích pro nějaké pevné ε>0? [Lenstra–Shmoys–Tardos: Unrelated Parallel Machines](https://ir.cwi.nl/pub/18055)

**46. Michel Goemans** — Síla relaxací pro TSP a přesná hranice jeho aproximace Max-Cut.

- **A.** Je integrality gap subtour LP pro metrické TSP nejvýše 4/3? [Integrality Gap of the Subtour LP for TSP](https://arxiv.org/abs/2105.10043v3)
- **B.** Je pro každé ε>0 NP-těžké aproximovat Max-Cut lépe než faktorem α_GW+ε, kde α_GW≈0,87856, bez předpokladu UGC? [Goemans–Williamson: Semidefinite Approximation](https://doi.org/10.1145/227683.227684)

**47. Vijay Vazirani** — Primal-dual aproximace pokrytí a umísťování center.

- **A.** Existuje polynomiální (2−ε)-aproximace minimálního vertex cover v obecných grafech pro nějaké pevné ε>0? [Vaziraniho otázka k Vertex Cover](https://algo.inria.fr/seminars/sem00-01/vazirani.html)
- **B.** Má metrický k-median polynomiální (1+2/e+ε)-aproximaci pro každé pevné ε>0? [A (2+ε)-Approximation Algorithm for Metric k-Median](https://people.idsia.ch/~grandoni/Pubblicazioni/CGLSS25stoc.pdf)

**48. Uriel Feige** — Jeho program aproximační obtížnosti a náhodných instancí CSP.

- **A.** Má Densest k-Subgraph polynomiální aproximaci s absolutně konstantním faktorem? [Detecting High Log-Densities](https://arxiv.org/abs/1001.2891)
- **B.** Lze v polynomiálním čase korektně refutovat s vysokou pravděpodobností náhodné formule 3-SAT s Cn klauzulemi pro nějakou dostatečně velkou konstantu C? [How to Refute a Random CSP](https://www.cs.cmu.edu/~odonnell/papers/random-csp-refutation.pdf)

**49. Mihalis Yannakakis** — Extension complexity a jeho práce na výpočetní složitosti tržních mechanismů.

- **A.** Má polytop perfektních párování úplného grafu superpolynomiální semidefinitní extension complexity? [Semidefinite Extension Complexity of the Matching Polytope](https://digital.lib.washington.edu/server/api/core/bitstreams/a7ac9607-c4f8-4d56-9b29-0f5ef033975d/content)
- **B.** Je výpočet přesné Hyllandovy–Zeckhauserovy rovnováhy FIXP-těžký? [Vazirani–Yannakakis: Hylland–Zeckhauser](https://epubs.siam.org/doi/10.1137/23M157586X)

**50. Daniel Spielman** — Ramanujanovy grafy, spektrální meze a metoda interlacing polynomials.

- **A.** Má každý d-regulární graf znaménkování hran, jehož znaménková matice sousednosti má spektrální normu nejvýše 2√(d−1)? [Marcus–Spielman–Srivastava: Interlacing Families](https://www.cs.yale.edu/homes/spielman/PAPERS/Marcus_Spielman_SrivastavaIFI.pdf)
- **B.** Existují pro každý pevný stupeň d≥3 nekonečné rodiny d-regulárních Ramanujanových grafů se silně explicitním výpočtem sousedů v čase poly(log n)? [An Improved Bound for the Bilu–Linial Conjecture](https://arxiv.org/abs/2606.28797)

**51. Shang-Hua Teng** — Simplex, jeho geometrie a rozdíl mezi příznivou analýzou a nejhorším případem.

- **A.** Existuje efektivně vyčíslitelné pivotovací pravidlo simplexu, které řeší každé racionální LP v polynomiálním počtu kroků? [Spielman–Teng: Smoothed Analysis of Simplex](https://www.cs.yale.edu/homes/spielman/simplex/)
- **B.** Platí polynomiální Hirschova domněnka: je grafový průměr každého polytopu omezen polynomem v počtu jeho faset a dimenzi? [Convex Polytopes: Polynomial Hirsch Conjecture](https://ti.inf.ethz.ch/ew/courses/Geo25/lecture/gca25-10.pdf)

**52. Mark Jerrum** — Aproximační počítání a míchání lokálních Markovových řetězců.

- **A.** Existuje FPRAS pro #BIS, tedy počet nezávislých množin v bipartitním grafu? [A Fixed-Parameter Perspective on #BIS](https://link.springer.com/article/10.1007/s00453-019-00606-4)
- **B.** Míchá se jednovrcholová Glauberova dynamika pro vlastní q-obarvení libovolného grafu polynomiálně rychle vždy, když q≥Δ+2? [Glauber Dynamics for Colourings](https://arxiv.org/abs/2010.16158)

**53. Christos Papadimitriou** — Složitost rovnováh a jím spoluzavedená třída CLS.

- **A.** Existuje pro každé pevné ε>0 polynomiální algoritmus pro aditivní ε-Nashovu rovnováhu dvouhráčové bimaticové hry s výplatami v [0,1]? [Settling the Complexity of Approximate Nash Equilibria](https://arxiv.org/abs/1606.04550)
- **B.** Platí CLS = FP, tedy lze všechny celkové vyhledávací problémy spojitého lokálního hledání řešit v polynomiálním čase? [The Complexity of Gradient Descent](https://arxiv.org/abs/2011.01929)

**54. Noam Nisan** — Derandomizace výpočtů v malé paměti a pokračování Nisanova–Ronenova programu.

- **A.** Platí BPL = L? [Better Pseudodistributions and Space Derandomization](https://drops.dagstuhl.de/storage/00lipics/lipics-vol207-approx-random2021/LIPIcs.APPROX-RANDOM.2021.28/LIPIcs.APPROX-RANDOM.2021.28.pdf)
- **B.** Existuje pravdivý v očekávání randomizovaný mechanismus pro makespan na nesouvisejících strojích s aproximačním faktorem omezeným absolutní konstantou? [A Proof of the Nisan–Ronen Conjecture](https://doi.org/10.1145/3785408)

**55. Tim Roughgarden** — Meze pravdivých mechanismů a výpočetní obtížnost spravedlivého rozdělování.

- **A.** Existuje univerzálně pravdivá randomizovaná kombinatorická aukce pro submodulární ocenění s konstantní aproximací společenského blahobytu a polynomiální komunikací? [Improved Truthful Mechanisms for Submodular Bidders](https://epubs.siam.org/doi/10.1137/20M1316068)
- **B.** Lze přesné envy-free rozdělení dortu mezi n účastníků s nezápornými neatomickými hodnotami vždy najít pomocí poly(n) Robertsonových–Webbových dotazů, dovolíme-li nesouvislé díly? [Single-Exponential Envy-Free Cake Cutting](https://arxiv.org/abs/2609.05191)

**56. Jon Kleinberg** — Jeho metric labeling a šíření vlivu v informačních sítích.

- **A.** Existuje polynomiální O(√log k)-aproximace obecného metric labeling s k možnými štítky? [The Hardness of Metric Labeling](https://epubs.siam.org/doi/10.1137/06065430X)
- **B.** Je adaptivity gap maximalizace vlivu v modelu independent cascade s úplnou zpětnou vazbou po každé kaskádě omezen absolutní konstantou? [Adaptivity Gap for Influence Maximization](https://www.sciencedirect.com/science/article/abs/pii/S0004370223000413)

**57. László Lovász** — Dvě klasické otázky přímo spojené s jeho jménem a metodami.

- **A.** Má každý konečný souvislý vrcholově tranzitivní graf Hamiltonovskou cestu? [Towards the Lovász Conjecture via Sublinear Expanders](https://arxiv.org/abs/2606.09742)
- **B.** Je Shannonova kapacita sedmicyklu rovna jeho Lovászovu číslu θ(C₇)? [Lovász: On the Shannon Capacity of a Graph](https://doi.org/10.1109/TIT.1979.1055985)

**58. Noga Alon** — Extremální kombinatorika a algebraické metody s algoritmickými důsledky.

- **A.** Platí sunflower conjecture: pro každé r existuje C_r tak, že každá rodina více než C_r^k různých k-prvkových množin obsahuje r-slunečnici? [Improved Bounds for the Sunflower Lemma](https://arxiv.org/abs/1908.08483)
- **B.** Platí Alonova–Tarsiho domněnka, že pro každý sudý řád je počet sudých a lichých latinských čtverců různý? [The Alon–Tarsi Conjecture: A Perspective](https://www.sciencedirect.com/science/article/pii/S0012365X19301372)

**59. Paul Seymour** — Jeho strukturální grafová teorie, minory a toky.

- **A.** Platí Hadwigerova domněnka: má každý graf s chromatickým číslem alespoň t minor K_t? [Seymour: Hadwiger’s Conjecture](https://web.math.princeton.edu/~pds/papers/hadwiger/paper.pdf)
- **B.** Má každý graf bez mostů nikde nulový 5-tok, jak tvrdí Tutteho 5-flow conjecture? [Seymour: Nowhere-Zero 6-Flows](https://collaborate.princeton.edu/en/publications/nowhere-zero-6-flows/)

**60. Micha Sharir** — Incidenční geometrie a složitost geometrických konfigurací.

- **A.** Určuje každá množina n bodů v rovině nejvýše n^{1+o(1)} dvojic v jednotkové vzdálenosti? [TOPP: Distances among Point Sets](https://topp.openproblem.net/p39)
- **B.** Má každá množina n bodů v rovině v obecné poloze nejvýše n^{1+o(1)} půlících přímek? [TOPP: k-Sets](https://topp.openproblem.net/p7)

**61. Herbert Edelsbrunner** — Algoritmická topologie a rozpoznávání triangulovaných prostorů.

- **A.** Lze v polynomiálním čase rozhodnout, zda zadaná triangulace uzavřené 3-variety představuje 3-sféru? [Emerging Challenges in Computational Topology](https://arxiv.org/abs/cs/9909001)
- **B.** Je rozhodnutelné, zda zadaná triangulace uzavřené PL 4-variety je PL-homeomorfní standardní 4-sféře? [Rozpoznávání triangulovaných sfér](https://link.springer.com/article/10.1007/s41468-022-00092-8)

**62. Avrim Blum** — Jeho aproximace barvení a výpočetní teorie učení.

- **A.** Existuje pevná konstanta C a polynomiální algoritmus, který každý 3-obarvitelný graf správně obarví nejvýše C barvami? [Better Coloring of 3-Colorable Graphs](https://arxiv.org/abs/2406.00357)
- **B.** Lze průnik dvou poloprostorů nad {0,1}ⁿ PAC-naučit v polynomiálním čase z náhodných označených příkladů pro libovolnou distribuci, s možností improper hypotézy? [The Intersection of Two Halfspaces Has High Threshold Degree](https://web.cs.ucla.edu/~sherstov/pdf/hshs.pdf)

**63. Robert Schapire** — Slabé versus silné učení a klasické reprezentace, pro něž efektivní PAC učení stále uniká.

- **A.** Lze polynomiálně PAC-učit DNF z náhodných označených příkladů pro libovolnou distribuci, bez membership queries? [Learning DNF Expressions from Fourier Spectrum](https://proceedings.mlr.press/v23/feldman12b.html)
- **B.** Lze rozhodovací stromy velikosti s nad {0,1}ⁿ učit z příkladů podle rovnoměrné distribuce v čase poly(n,s,1/ε), bez membership queries? [Učení rozhodovacích stromů a DNF](https://eccc.weizmann.ac.il/report/1995/008/)

**64. Peter Bartlett** — Strukturální teorie generalizace a optimální online rozhodování.

- **A.** Má každá booleovská třída s VC dimenzí d vzorkové kompresní schéma celkové velikosti O(d), včetně započtené pomocné informace? [Sample Compression Schemes for VC Classes](https://arxiv.org/abs/1503.06960v2)
- **B.** Je minimax regret adversariální banditové konvexní optimalizace v dimenzi d nejvýše Õ(d^{3/2}√T), pro ztráty v [0,1] a zpětnou vazbu pouze v zahraném bodě? [Lattimore: Bandit Convex Optimisation](https://tor-lattimore.com/downloads/cvx-book/cvx.pdf)

**65. Yishay Mansour** — Jeho Fourierův přístup k učení a identifikace relevantních proměnných.

- **A.** Platí Mansourova domněnka: soustředí každá s-termová DNF alespoň 1−ε Fourierovy hmoty na s^{O(log(1/ε))} koeficientech? [Mansour’s Conjecture for Random DNF](https://eccc.weizmann.ac.il/report/2010/023/revision/3/download/)
- **B.** Lze každou booleovskou k-juntu učit z rovnoměrných náhodných označených příkladů v čase poly(n,2^k,1/ε)? [Learning Juntas](https://www.cs.cmu.edu/~odonnell/papers/juntas.pdf)

**66. Ankur Moitra** — Identifikovatelnost latentních modelů a tenzorové rozklady.

- **A.** Lze hustotu libovolné směsi k Gaussových rozdělení v ℝᵈ naučit do chyby ε v total variation v čase a počtu vzorků poly(d,k,1/ε), bez separačního předpokladu? [Moitra–Valiant: Learning Mixtures of Gaussians](https://people.csail.mit.edu/moitra/docs/mv.pdf)
- **B.** Lze v modelu přesné aritmetiky v polynomiálním čase s vysokou pravděpodobností rozložit T=Σᵢ aᵢ⊗aᵢ⊗aᵢ, kde aᵢ jsou nezávislé gaussovské d-vektory a počet složek je ⌊d²/10⌋? [Kothari–Moitra–Wein: Tensor Decomposition](https://arxiv.org/abs/2411.14344)

**67. Ilias Diakonikolas** — Výpočetní cena robustnosti a agnostického učení.

- **A.** Lze při ε-kontaminaci robustně odhadnout k-řídký průměr N(μ,I) s eukleidovskou chybou O(ε), v polynomiálním čase a z Õ(k log d/ε²) vzorků? [Diakonikolas a spoluautoři: Robust Sparse Estimation](https://proceedings.mlr.press/v178/diakonikolas22e.html)
- **B.** Lze agnosticky učit poloprostory pod standardní Gaussovou distribucí s chybou OPT+ε v čase poly(d,1/ε)? [Diakonikolas a spoluautoři: Agnostic Halfspaces](https://proceedings.mlr.press/v134/diakonikolas21b.html)

**68. Ronitt Rubinfeld** — Co lze zjistit o obrovském grafu z několika dotazů a kdy to lze systematicky rozpoznat.

- **A.** Implikuje testovatelnost grafové vlastnosti s poly(1/ε) dotazy možnost odhadnout její editační vzdálenost s aditivní chybou ε pomocí poly(1/ε) dotazů v hustém modelu? [Testing versus Estimation of Graph Properties, Revisited](https://onlinelibrary.wiley.com/doi/10.1002/rsa.21221)
- **B.** Existuje algoritmus, který z konečné rodiny zakázaných indukovaných podgrafů rozhodne, zda příslušná dědičná vlastnost má jednostranný tester s poly(1/ε) dotazy? [Polynomial Property Testing](https://arxiv.org/html/2508.16878v1)

**69. Piotr Indyk** — Aproximace vzdáleností, embeddingy a zrychlování porovnávání řetězců.

- **A.** Existuje konstantní aproximace editační vzdálenosti dvou řetězců délky n v čase O(n·polylog n)? [Edit Distance in Near-Linear Time](https://arxiv.org/abs/2005.07678)
- **B.** Lze metriku editační vzdálenosti na binárních řetězcích délky n vložit do ℓ₁ s distorzí polylog(n)? [Low Distortion Embeddings for Edit Distance](https://doi.org/10.1145/1060590.1060623)

**70. David Woodruff** — Jeho sketching a nízkohodnostní aproximace s optimální závislostí na vstupu.

- **A.** Lze nalézt hodnostně k aproximaci s chybou nejvýše (1+ε)OPT ve spektrální normě v čase Õ(nnz(A)+(m+n)·poly(k/ε)) pro m×n matici A? [Woodruff: Sketching for Numerical Linear Algebra](https://arxiv.org/abs/1411.4357)
- **B.** Má aproximace matice hodností k v součtu absolutních chyb položek konstantní aproximační faktor dosažitelný v čase poly(m,n,k), s výstupní hodností nejvýše k? [A PTAS for ℓp-Low Rank Approximation](https://epubs.siam.org/doi/10.1137/1.9781611975482.47)

**71. Venkatesan Guruswami** — Explicitní kódy a zásadní meze opravování synchronizačních chyb.

- **A.** Lze pro každé pevné δ∈(0,1/2) explicitně v polynomiálním čase konstruovat binární kódy s relativní vzdáleností δ a rychlostí alespoň 1−H₂(δ)−o(1)? [Guruswami: Coding Theory](https://www.cs.cmu.edu/~venkatg/teaching/codingtheory/)
- **B.** Existují binární kódy kladné asymptotické rychlosti, které jednoznačně opraví libovolných (√2−1+ε)n smazání pro nějaké pevné ε>0? [Guruswami–He–Li: Deletion Threshold](https://ieee-focs.org/FOCS-2021-Papers/pdfs/FOCS2021-5stbVHiOp5jRHWlSl41FkR/205500a737/205500a737.pdf)

**72. Mark Braverman** — Informační složitost komunikace a jeho práce na tree codes.

- **A.** Existují explicitní tree codes s konstantní abecedou, kladnou relativní vzdáleností a kódováním i dekódováním v polynomiálním čase? [Explicit Tree Codes](https://eccc.weizmann.ac.il/report/2018/032/revision/1/download)
- **B.** Platí randomizovaná log-rank conjecture: je komunikační složitost úplné booleovské funkce s chybou 1/3 omezena polynomem v logaritmu reálné hodnosti její matice? [The Log-Rank Conjecture](https://arxiv.org/abs/2510.02583v3)

**73. Peter Shor** — Hledání dalších strukturálních kvantových zrychlení po faktorizaci.

- **A.** Je izomorfismus grafů řešitelný v kvantovém polynomiálním čase, tedy GI∈BQP? [Ten Semi-Grand Challenges for Quantum Computing Theory](https://www.scottaaronson.com/writings/qchallenge.html)
- **B.** Má hidden subgroup problem v dihedrální grupě D_N kvantový algoritmus s celkovým časem poly(log N), nikoli pouze malým počtem dotazů? [Kuperberg: Dihedral Hidden Subgroup Problem](https://epubs.siam.org/doi/10.1137/S0097539703436345)

**74. Alexei Kitaev** — Lokální Hamiltoniány, kvantové kódy a struktura základních stavů.

- **A.** Existují kvantové lokálně testovatelné stabilizátorové kódy s konstantní rychlostí, lineární vzdáleností, omezenou vahou a stupněm kontrol a konstantní soundness? [Quantum Locally Testable Code with Constant Soundness](https://quantum-journal.org/papers/q-2024-10-18-1501/)
- **B.** Splňuje jedinečný základní stav každého lokálního Hamiltoniánu na 2D mřížce s konstantní spektrální mezerou entropický area law S(A)=O(|∂A|)? [An Area Law for 2D Frustration-Free Spin Systems](https://arxiv.org/abs/2103.02492v3)

**75. Umesh Vazirani** — Základní hranice kvantové výpočetní síly a síly kvantových svědků.

- **A.** Platí BPP⊊BQP bez použití orákula nebo neprokázaného předpokladu o obtížnosti konkrétního problému? [Shor: Polynomial-Time Quantum Algorithms](https://arxiv.org/abs/quant-ph/9508027v2)
- **B.** Platí QCMA⊊QMA, tedy existují efektivně kvantově ověřitelné úlohy, kterým polynomiálně dlouhý klasický svědek nestačí? [Separating Quantum and Classical Advice with Good Codes](https://eccc.weizmann.ac.il/report/2026/020/)

**76. Scott Aaronson** — Jeho konkrétní domněnky o kvantových dotazech a boson samplingu.

- **A.** Má každý polynom p:{−1,1}ⁿ→[0,1] stupně d≥1 a variance alespoň v>0 některou proměnnou s influencí alespoň (v/d)^C pro univerzální konstantu C? [Aaronson–Ambainis: The Need for Structure](https://arxiv.org/abs/0911.0996)
- **B.** Platí Permanent-of-Gaussians Conjecture: je relativní aproximace permanentu nezávisle komplexně gaussovské matice na převážné části vstupů #P-těžká v přesném smyslu GPE×? [Aaronson–Arkhipov: The Complexity of Linear Optics](https://www.scottaaronson.com/papers/optics-toc.pdf)

**77. Dorit Aharonov** — Její kvantový PCP program a ekvivalence adiabatických a obvodových výpočtů.

- **A.** Platí quantum PCP conjecture: zůstává QMA-těžké aproximovat základní energii součtu m lokálních členů 0≤Hᵢ≤I s aditivní chybou εm pro vhodnou konstantu ε>0? [Aharonov a spoluautoři: The Quantum PCP Conjecture](https://arxiv.org/abs/1309.7495)
- **B.** Lze každý polynomiálně dlouhý stoquastický adiabatický výpočet s inverzně polynomiální spektrální mezerou efektivně simulovat klasicky? [Stoquastická adiabatická simulace](https://journals.aps.org/prl/abstract/10.1103/PhysRevLett.125.170504)

**78. Charles Bennett** — Destilace provázání a skutečná kapacita kvantových kanálů.

- **A.** Existují bipartitní bound-entangled stavy se zápornou částečnou transpozicí, které nelze destilovat ani z libovolného počtu kopií? [Evidence for NPT Bound Entanglement](https://arxiv.org/abs/quant-ph/9910026)
- **B.** Má qubitový depolarizační kanál, který s celkovou pravděpodobností p aplikuje rovnoměrně jednu z chyb X,Y,Z, kladnou neasistovanou kvantovou kapacitu pro každé p<1/4? [Quantum Cloning and the Capacity of the Pauli Channel](https://arxiv.org/abs/quant-ph/9803058)

**79. Gilles Brassard** — Kvantová komunikace a informačně teoretické základy sdíleného tajemství.

- **A.** Jsou pro všechny úplné booleovské funkce randomizovaná klasická a kvantová komunikační složitost s předem sdíleným provázáním polynomiálně svázané? [Quantum–Classical Equivalence for AND-Functions](https://eccc.weizmann.ac.il/report/2026/013/)
- **B.** Existuje bipartitní bound information: rozdělení klasických proměnných Alice, Boba a Evy s kladnou intrinsic information, ale nulovou rychlostí destilace tajného klíče i při obousměrné veřejné komunikaci? [Acín–Gisin: Quantum Correlations and Secret Bits](https://doi.org/10.1103/PhysRevLett.94.020501)

**80. Thomas Vidick** — Entangled games a jeho současná práce na quantum interactive oracle proofs.

- **A.** Platí pro každou dvouhráčovou hru G s provázanou hodnotou ω*(G)<1 exponenciální parallel repetition, tedy ω*(G^{⊗r})≤exp(−c_G r) pro nějaké c_G>0? [Kempe–Vidick: Parallel Repetition of Entangled Games](https://arxiv.org/abs/1012.4728)
- **B.** Má celé QMA polynomiálně dlouhé strong quantum interactive oracle proofs s konstantním počtem kol i dotazů a konstantní mezerou mezi úplností a korektností? [Sun–Vidick: Quantum Interactive Oracle Proofs](https://arxiv.org/abs/2601.12874)

**81. Urmila Mahadev** — Klasické ověřování kvantových výpočtů a kryptograficky chráněné kvantové objekty.

- **A.** Lze každý BQP výpočet ověřit klasickým polynomiálním ověřovatelem komunikujícím s jediným poctivým BQP dokazovatelem, s informačně teoretickou korektností a bez kryptografických předpokladů? [Verification of Quantum Computation: An Overview](https://arxiv.org/abs/1709.06984)
- **B.** Lze veřejně ověřitelné kvantové peníze s opakovaně použitelnými bankovkami založit pouze na LWE bezpečném proti kvantovým útočníkům? [Anonymous Public-Key Quantum Money](https://arxiv.org/abs/2411.04482)

**82. Leslie Lamport** — Byzantská shoda, její informační předpoklady a optimální cena komunikace.

- **A.** Existuje perfektně bezpečná asynchronní binární byzantská shoda s očekávanou Õ(n²) bitovou komunikací pro t<n/3, jen s privátními kanály a bez důvěryhodné inicializace? [ABEL: Perfect Asynchronous Byzantine Extension](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.DISC.2025.1)
- **B.** Existuje asynchronní byzantská ε-přibližná shoda pro t<n/3 s O(n² log(2+S/ε)) zprávami a O(log(2+S/ε)) koly, kde S je rozpětí správných vstupů? [Asynchronous Approximate Agreement](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.OPODIS.2025.16)

**83. Nancy Lynch** — Co lze po FLP dosáhnout randomizací a za jakou cenu.

- **A.** Existuje asynchronní byzantská shoda ve full-information modelu s očekávanou latencí Õ(n³), polynomiální lokální prací a odolností pro všechna t<n/3 proti adaptivnímu protivníkovi? [Byzantine Agreement via Statistical Fraud Detection](https://arxiv.org/abs/2206.15335)
- **B.** Existuje randomizovaný asynchronní konsenzus tolerující t<n/2 havárií s očekávaným O(n²) počtem zpráv proti silně adaptivnímu plánovači? [Komunikační složitost asynchronního konsenzu](https://link.springer.com/article/10.1007/s00446-017-0315-1)

**84. Maurice Herlihy** — Jeho konsenzová hierarchie a otázka skutečné síly souběžných objektů.

- **A.** Je konsenzová hierarchie deterministických typů robustní: nepřekročí konsenzové číslo jejich společného použití maximum čísel jednotlivých typů? [Algorithms for Concurrent Systems](https://perso.telecom-paristech.fr/kuznetso/EFREI18-old/book.pdf)
- **B.** Patří neomezená linearizovatelná fronta do Common₂, tedy lze ji wait-free implementovat pro libovolný počet procesů z registrů a objektů dvouprocesového konsenzu? [Two-Enqueuer Queue in Common₂](https://arxiv.org/abs/0805.0444)

**85. David Peleg** — Spannery a kompromis mezi délkou cest a velikostí routovacích tabulek.

- **A.** Platí Erdősova girth conjecture: pro každé pevné k existují n-vrcholové grafy obvodu většího než 2k s Ω(n^{1+1/k}) hranami? [Erdősova domněnka a dolní meze pro spannery](https://doi.org/10.4230/LIPIcs.ESA.2026.31)
- **B.** Existuje pro každé pevné k≥2 compact routing pro všechny vážené neorientované grafy se stretchem 2k−1 a tabulkou Õ(n^{1/k}) na každém vrcholu, bez handshakingu a s volitelnými krátkými adresami? [Compact Routing Schemes with Improved Stretch](https://theory.stanford.edu/~virgi/cs267/papers/chechik-compactroute.pdf)

**86. Jukka Suomela** — Obě otázky navazují přímo na jeho aktuální seznam otevřených problémů lokálnosti.

- **A.** Je rozhodnutelné, zda zadaný LCL problém na nekořenových stromech omezeného stupně s konečnými vstupními štítky má deterministický LOCAL algoritmus v O(1) kolech? [Suomela: LOCAL open problems](https://jukkasuomela.fi/open/#local)
- **B.** Lze orientovaný n-cyklus 3-obarvit v quantum-LOCAL modelu v o(log* n) kolech s vysokou pravděpodobností, bez počátečního provázání mezi vrcholy? [Suomela: Quantum-LOCAL open problems](https://jukkasuomela.fi/open/#quantum-local)

**87. Dana Scott** — Meze doménové sémantiky netypovaného lambda kalkulu.

- **A.** Existuje Scottovsky spojitý reflexivní doménový model lambda kalkulu, jehož rovnicová teorie je přesně λβ? [TLCA: Continuously Complete CPO Models](https://tlca.di.unito.it/opltlca/opltlcasu29.html)
- **B.** Existuje efektivní Scottovsky spojitý lambda model s rekurzivně spočetnou rovnicovou teorií? [Effective Lambda-Models and Enumerable Theories](https://arxiv.org/abs/0806.2264)

**88. Gordon Plotkin** — Pravděpodobnostní domény a limity uspořádaných modelů výpočtu.

- **A.** Zachovává subpravděpodobnostní powerdomain V≤1 třídu všech pointed countably based FS-domén? [Finite-Valuation Approximable Structures, 2026](https://arxiv.org/html/2608.03073v3)
- **B.** Existuje absolutně neuspořadatelná kombinatorická algebra, která se nedá vložit do žádné netriviálně uspořádatelné kombinatorické algebry? [Selinger: Ordered Combinatory Algebras](https://www.mathstat.dal.ca/~selinger/papers/cmaa.pdf)

**89. Jean-Yves Girard** — Rozhodnutelnost lineární logiky a normalizace typovaných výpočtů.

- **A.** Je výroková multiplikativně-exponenciální lineární logika MELL rozhodnutelná? [On the Decidability of MELL](https://www.lix.polytechnique.fr/~lutz/papers/OnDeciMELL.pdf)
- **B.** Implikuje u každého pure type system slabá normalizace všech typovatelných termů jejich silnou normalizaci? [TLCA: Weak versus Strong Normalization](https://tlca.di.unito.it/opltlca/problem9.pdf)

**90. Per Martin-Löf** — Závislé typy a jeho teorie algoritmické náhodnosti.

- **A.** Lze v obyčejné intenzionální HoTT interně a uniformně definovat všechny konečné stupně semisimpliciálních typů s kompatibilními restrikcemi, bez přidání druhé úrovně teorie typů? [On the Role of Semisimplicial Types](https://nicolaikraus.github.io/docs/on_semisimplicial_types.pdf)
- **B.** Je každá Kolmogorovova–Lovelandova náhodná binární posloupnost také Martin-Löfovsky náhodná? [Kolmogorov–Loveland Betting Strategies](https://arxiv.org/abs/2403.19817)

**91. Samson Abramsky** — Strukturální vztah provázání, nelokálnosti a kvantových modelů.

- **A.** Lze z každého bipartitního provázaného stavu získat Bellovsky nelokální korelace pomocí konečně mnoha jeho kopií a lokálních filtrů, bez dalšího pomocného provázaného stavu? [All Entangled States Display Some Hidden Nonlocality](https://arxiv.org/abs/1210.0548)
- **B.** Je množina konečnědimenzionálních bipartitních kvantových korelací uzavřená už ve scénáři se třemi volbami měření a dvěma výstupy na každé straně, tedy Cq(3,2)? [An Inherently Infinite-Dimensional Quantum Correlation](https://www.nature.com/articles/s41467-020-17077-9)

**92. Patrick Cousot** — Přesné rozhodování invariantů a dosažitelnosti jednoduchých lineárních programů.

- **A.** Je Skolemův problém pro celočíselné lineární rekurence libovolného řádu rozhodnutelný: nabude posloupnost někdy hodnoty nula? [Skolem Meets Schanuel](https://doi.org/10.4230/LIPIcs.MFCS.2022.20)
- **B.** Je Positivity Problem pro celočíselné lineární rekurence libovolného řádu rozhodnutelný: jsou všechny členy nezáporné? [Survey of the Skolem and Positivity Problems, 2026](https://people.mpi-sws.org/~joel/publications/skolem_and_positivity_survey26abs.html)

**93. Moshe Vardi** — Automatová verifikace a deskriptivní složitost.

- **A.** Lze vítěze konečné paritní hry spočítat deterministicky v polynomiálním čase? [Deciding Parity Games in Quasipolynomial Time](https://www.cmap.polytechnique.fr/~gaubert/COURSM2/PARITYGAMES/paritygame.pdf)
- **B.** Jsou spektra prvořádových vět uzavřená na doplněk: je doplněk každé množiny konečných velikostí modelů opět spektrem nějaké prvořádové věty? [Fifty Years of the Spectrum Problem](https://arxiv.org/abs/0907.5495)

**94. Rajeev Alur** — Rozhodnutelnost těsně za hranicí časovaných automatů.

- **A.** Je dosažitelnost u automatů se dvěma stopkami rozhodnutelná, dovolíme-li rychlosti 0 a 1, racionální stráže a nulování? [What’s Decidable about Hybrid Automata?](https://doi.org/10.1006/jcss.1998.1581)
- **B.** Je dosažitelnost diskrétních parametrických časovaných automatů se dvěma parametrickými hodinami rozhodnutelná, dovolíme-li libovolný počet celočíselných parametrů? [Two Parametric Timed Clocks, 2023](https://link.springer.com/article/10.1007/s00224-023-10121-3)

**95. Thomas Henzinger** — Algoritmické hry a verifikace spojité dynamiky.

- **A.** Jsou mean-payoff games s binárně zadanými celočíselnými vahami řešitelné v čase polynomiálním v bitové délce vstupu? [Faster Algorithms for Mean-Payoff Games](https://lsv.ens-paris-saclay.fr/~doyen/papers/Faster_Algorithms_for_Mean-Payoff_Games.pdf)
- **B.** Je neomezený spojitý Skolemův problém rozhodnutelný: existuje t≥0 s cᵀe^{tA}b=0 pro racionální A,b,c? [The Skolem Problem for Continuous Linear Dynamical Systems](https://arxiv.org/abs/1506.00695)

**96. Marta Kwiatkowska** — Pravděpodobnostní hry a přesná kvantitativní verifikace.

- **A.** Lze hodnotu konečné simple stochastic game porovnat s racionálním prahem v deterministickém polynomiálním čase? [The Complexity of Stochastic Games](https://www.sciencedirect.com/science/article/pii/089054019290048K)
- **B.** Je přesné porovnání maximální pravděpodobnosti časově omezené dosažitelnosti v konečném CTMDP s racionálním prahem rozhodnutelné bez Schanuelovy domněnky? [CTMDP Reachability and Schanuel’s Conjecture](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.ICALP.2020.133)

**97. Mikołaj Bojańczyk** — Algebraické charakterizace jazyků a jejich logické definovatelnosti.

- **A.** Je rozhodnutelné, zda regulární jazyk konečných stromů lze definovat prvořádovou logikou s predikátem potomka a vrcholovými štítky? [Bojańczyk: Algebra for Finite Trees](https://www.mimuw.edu.pl/~bojan/paper/algebra-for-finite-trees)
- **B.** Má každý regulární jazyk zobecněnou star height nejvýše 1, dovolíme-li v regulárních výrazech také doplněk? [The Generalized Star-Height Problem](https://www.irif.fr/~jep/Problemes/starheight.html)

**98. Rod Downey** — Dvě velké osy jeho práce: parametrizovaná složitost a vyčíslitelnost.

- **A.** Platí FPT≠W[1], ekvivalentně: neexistuje algoritmus pro k-kliku v čase f(k)·n^{O(1)}? [On W[1]-Hardness as Evidence for Intractability](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.MFCS.2018.73)
- **B.** Je částečné uspořádání všech Turingových stupňů rigidní, tedy je každý jeho automorfismus identita? [Global Properties of the Turing Degrees](https://math.berkeley.edu/~slaman/papers/IMS_slaman.pdf)

**99. Martin Grohe** — Logiky pro polynomiální čas a strukturálně parametrizovaný izomorfismus.

- **A.** Zachycuje choiceless polynomial time s počítáním všechny PTIME vlastnosti konečných struktur? [Choiceless Polynomial Time](https://arxiv.org/abs/math/9705225)
- **B.** Je izomorfismus grafů fixed-parameter tractable podle rank-width k, tedy řešitelný v čase f(k)·n^{O(1)}? [Parameterized Complexity of Graph Isomorphism, 2026](https://epub.uni-regensburg.de/78630/1/1-s2.0-S1574013726000274-main.pdf)

**100. Dániel Marx** — Strukturální složitost CSP a přenos jemných dolních mezí na aproximace.

- **A.** Platí pro všechny konečné promise CSP dichotomie: každý je buď v P, nebo NP-těžký? [An Invitation to the Promise CSP](https://arxiv.org/abs/2208.13538)
- **B.** Implikuje ETH hypotézu Gap-ETH: existuje konstantní δ>0, pro kterou nelze v čase 2^{o(n)} rozlišit splnitelnou řídkou 3-CNF od formule s nejvýše (1−δ) podílem splnitelných klauzulí? [ETH a Gap-ETH](https://eccc.weizmann.ac.il/report/2024/114/)
