# Druhý průchod: další zásadní problémy pro malé kategorie

**26 dalších návrhů ve 24 z 25 současných malých kategorií.** Ve 22 kategoriích je jeden nový problém; v Knowledge representation a Structural graph theory dva. Miscellaneous zůstává bez dalšího návrhu.

Stav rešerše: 10. září 2026. Jde o doplnění předchozího výběru, s formulacemi a podklady k redakčnímu posouzení. Po následném souhlasu uživatele bylo všech 26 návrhů přidáno do atlasu jako krátké karty: [přehled publikovaných problémů](../../web/fundamental-small-second-additions.md). Původní audit níže zachycuje stav před publikací.

## Změna přístupu

Vycházel jsem z hlavních mezer popsaných autory přehledů, přednášek a výzkumných programů: hranice výpočetních modelů, úplné charakterizace a optimální dosažitelnost. U každé otázky jsem kontroloval, zda jde o samostatný hlavní problém, a rozlišoval jej od už vyřešených speciálních případů.

Porovnání zahrnuje 6,657 záznamů katalogu, 72 předchozích návrhů pro malé kategorie a 73 položek velkého návrhu (včetně vyřazené duplicity). Li–Li network coding přibylo mezitím do velkého návrhu, a proto zde není započítáno znovu. Blízké záznamy jsem posuzoval podle vybrané otázky a v nejasných případech podle plného zdroje, nikoli jen názvu článku.

Hodnocení významu je redakční úsudek. Pořadí uvnitř každé kategorie se týká pouze těchto nových návrhů; starší seznam nepřerovnává. Otevřenost je závěr z uvedených primárních zdrojů a kontrol pozdějších výsledků, nikoli záruka úplnosti literatury.

## Přehled

| # | Současná malá kategorie | Další problém(y) |
|---:|---|---|
| 1 | Approximation algorithms and hardness of approximation | The optimal approximation threshold for metric k-Median |
| 2 | Parameterized and exact algorithms | A polynomial kernel for Edge Multiway Cut |
| 3 | Fine-grained complexity | The Hyperclique Hypothesis |
| 4 | Pseudorandomness and derandomization | Optimal deterministic restricted-isometry matrices |
| 5 | Proof complexity | Frege versus Extended Frege |
| 6 | Communication complexity and Boolean function analysis | The asymptotic Gotsman–Linial conjecture |
| 7 | Coding and information theory | The capacity region of the general two-receiver broadcast channel |
| 8 | Algebraic computation | The Shub–Smale τ-conjecture |
| 9 | Lattices and computational number theory | Polynomial-time, polynomial-factor approximation of Euclidean SVP |
| 10 | Randomized algorithms and sampling | Polynomial mixing of critical three-dimensional Ising dynamics |
| 11 | String algorithms and bioinformatics | Breaking factor two for sum-of-pairs multiple sequence alignment |
| 12 | Dynamic graph algorithms | Polylogarithmic maintenance of the exact global minimum cut |
| 13 | Counting and enumeration | An FPRAS for counting undirected Euler tours |
| 14 | Property testing and distribution learning | Sublinear testing of bounded-degree graph isomorphism |
| 15 | Differential privacy | Optimal error for pure-DP continual counting |
| 16 | Algorithmic game theory, mechanism design and fair division | The power of randomization in truthful unrelated-machine scheduling |
| 17 | Constraint satisfaction | Search-to-decision equivalence for finite promise CSPs |
| 18 | Scheduling and packing | Breaking factor two for precedence-constrained makespan |
| 19 | Automated reasoning and unification | The isomorphism problem for one-relator groups |
| 20 | Database theory and finite model theory | FO model checking on hereditary monadically dependent graph classes |
| 21 | Computability and algorithmic information | Universality of Turing equivalence |
| 22 | Knowledge representation and reasoning | Decidability of conjunctive-query entailment in SROIQ<br>DNF versus d-DNNF succinctness |
| 23 | Structural graph theory | Reed's χ–ω–Δ conjecture<br>The optimal quantitative Excluded Grid Theorem |
| 24 | Beyond worst-case and average-case analysis | The computational Kesten–Stigum threshold for sparse community recovery |
| 25 | Miscellaneous | Bez návrhu splňujícího přísný výběr. |

## 1. Approximation algorithms and hardness of approximation

### 1. The optimal approximation threshold for metric k-Median

**Otázka:** For general finite metrics, does every fixed ε>0 admit a polynomial-time (1+2/e+ε)-approximation for k-Median, opening at most k facilities? If not, determine the stronger inapproximability threshold.

**Význam:** Základní otevřená mezera v aproximaci shlukování: jde o konečný dosažitelný poměr, nikoli o další malé zlepšení algoritmu.

**Odlišení od dosavadního seznamu:** TCS-6059 asks about FPT approximation of MATROID median; its full source p. 2 was read. The other k-median records concern capacities, anonymity, local or universal variants.

**Stav a přesný rozsah:** The STOC 2025 paper gives 2+ε and explicitly identifies the remaining gap to 1+2/e. Polynomial time is required for variable k; an FPT algorithm is insufficient.

**Primární podklady:**

- [A (2+ε)-Approximation Algorithm for Metric k-Median (STOC 2025)](https://people.idsia.ch/~grandoni/Pubblicazioni/CGLSS25stoc.pdf) — Introduction, paragraph beginning 'However, a major open problem remains'.

## 2. Parameterized and exact algorithms

### 1. A polynomial kernel for Edge Multiway Cut

**Otázka:** Can an undirected Edge Multiway Cut instance with cut budget k be reduced in polynomial time to an equivalent instance whose total encoding length is k^O(1), independently of the number of terminals? A randomized polynomial kernel would already resolve the size question.

**Význam:** Jedna z hlavních otevřených otázek kernelizace grafových řezů: zda lze velký vstup stlačit na velikost polynomiální v počtu mazaných hran.

**Odlišení od dosavadního seznamu:** Existing TCS-5901 selects Vertex Planarization, despite Multiway Cut appearing in its source title. TCS-5945 is Multiway Near-Separator with deletable terminals. Neither is the general edge-cut kernel question.

**Stav a přesný rozsah:** Keep arbitrary terminal sets and edge deletions. Polynomial kernels for fixed terminal count or for vertex deletion with deletable terminals do not settle it.

**Primární podklady:**

- [Quasipolynomial multicut-mimicking networks and kernelization of multiway cut problems](https://arxiv.org/abs/2002.08825) — Introduction and kernelization consequences.

## 3. Fine-grained complexity

### 1. The Hyperclique Hypothesis

**Otázka:** For every fixed uniformity h≥3 and clique size k>h, is detecting a k-vertex clique in an n-vertex h-uniform hypergraph impossible in O(n^(k−ε)) time for every fixed ε>0?

**Význam:** Samostatný hlavní předpoklad fine-grained complexity pro problémy s vazbami mezi více než dvěma prvky; nese jinou síť podmíněných dolních mezí než hypotézy o obyčejné klice.

**Odlišení od dosavadního seznamu:** No Hyperclique question identified. Prior small-pass algebraic k-Clique concerns ordinary graphs and matrix-multiplication exponents.

**Stav a přesný rozsah:** This is a conjectured running-time barrier, not a proven lower bound. Fix h and k; the statement excludes the trivial k=h input-reading case.

**Primární podklady:**

- [The Role of Regularity in (Hyper-)Clique Detection and Implications for Optimizing Boolean CSPs](https://arxiv.org/abs/2505.17314) — Hyperclique hypothesis; ICALP 2025.

## 4. Pseudorandomness and derandomization

### 1. Optimal deterministic restricted-isometry matrices

**Otázka:** For a fixed distortion δ=1/3, can a deterministic algorithm running in poly(N) time construct an m×N rational matrix A with m=O(s log(eN/s)) such that (1−δ)||x||²≤||Ax||²≤(1+δ)||x||² for every s-sparse real vector x? Require polynomial encoding length.

**Význam:** Výrazná mezera mezi náhodnými a explicitními konstrukcemi: optimální komprimované měření řídkých signálů bez náhody.

**Odlišení od dosavadního seznamu:** No restricted-isometry or RIP question found in the saved catalogue or earlier proposals.

**Stav a přesný rozsah:** Random matrices achieve this row count. Explicit constructions for weaker sparsity regimes or with more rows do not meet the target.

**Primární podklady:**

- [Doubly transitive equiangular tight frames that contain regular simplices](https://www.sciencedirect.com/science/article/pii/S0024379525003143) — Introduction, deterministic RIP construction problem.

## 5. Proof complexity

### 1. Frege versus Extended Frege

**Otázka:** Does Frege polynomially simulate Extended Frege in proof size? Equivalently, is there a fixed polynomial p such that every tautology with an Extended Frege proof of size s has a Frege proof of size at most p(s)?

**Význam:** Ptá se, zda zavádění jmen pro pomocné formule zásadně zkracuje důkazy. Jde o porovnání síly dvou ústředních důkazových systémů.

**Odlišení od dosavadního seznamu:** Prior small-pass candidate asks for superpolynomial Extended Frege lower bounds; this asks for a separation or simulation between systems. TCS-5332 concerns automation of Resolution.

**Stav a přesný rozsah:** Proof-size simulation is the target. Do not silently strengthen this to an efficiently computable proof translation.

**Primární podklady:**

- [Proof Complexity Mini-tutorial — Samuel Buss](https://mathweb.ucsd.edu/~sbuss/ResearchWeb/Stanford_February2014/) — Frege systems versus Extended Frege.

## 6. Communication complexity and Boolean function analysis

### 1. The asymptotic Gotsman–Linial conjecture

**Otázka:** Is there a universal C such that every Boolean polynomial threshold function f=sign(p) on {−1,1}^n, with degree(p)≤d, has total influence I(f)≤C d√n?

**Význam:** Základní otázka o citlivosti prahových funkcí nízkého stupně, která propojuje analýzu booleovských funkcí, učení a obvodovou složitost.

**Odlišení od dosavadního seznamu:** No corresponding selected question identified; broad Linial-name matches were unrelated.

**Stav a přesný rozsah:** The original exact extremal conjecture is false. Kane proved a weaker bound with polylogarithmic factors; neither fact settles the O(d√n) statement.

**Primární podklady:**

- [The Gotsman–Linial Conjecture is False](https://arxiv.org/abs/2108.02288) — Conjecture 1.2 (asymptotic version).
- [A Dual Perspective on Computational Complexity](https://dspace.mit.edu/server/api/core/bitstreams/7f2e32fd-d615-4dba-97be-f26cd30ca234/content) — Conjectures 6.1.2 and 6.1.3.

## 7. Coding and information theory

### 1. The capacity region of the general two-receiver broadcast channel

**Otázka:** Give an exact, effectively evaluable characterization of the capacity region of every finite-alphabet discrete memoryless broadcast channel p(y,z|x), for two independent private messages and vanishing average decoding error, without feedback.

**Význam:** Jeden ze základních nevyřešených modelů síťové teorie informace: jeden vysílač posílá různé zprávy dvěma příjemcům.

**Odlišení od dosavadního seznamu:** No broadcast-channel capacity question identified. Earlier Gaussian interference-channel capacity has two transmitters; it is a different network model. Li–Li network coding has meanwhile been added in the parallel large-category pass and is not counted here.

**Stav a přesný rozsah:** The proposal asks for the general capacity region, not for the tightness of Marton's bound; a recent counterexample claim concerning that bound is not a full capacity characterization.

**Primární podklady:**

- [Chandra Nair — Research: Multiuser Information Theory](https://chandra.ie.cuhk.edu.hk/research.html) — Two-receiver discrete memoryless broadcast channels.
- [Sub-optimality of Marton's Inner Bound for the Two-Receiver Broadcast Channel](https://arxiv.org/abs/2608.19869) — August 2026 preprint; narrower conjecture claimed refuted, not a full capacity characterization.

## 8. Algebraic computation

### 1. The Shub–Smale τ-conjecture

**Otázka:** Is there a universal C such that every nonzero f∈Z[x] has at most (1+τ(f))^C distinct integer roots, where τ(f) is its constant-free straight-line complexity from 1 and x using addition, subtraction and multiplication?

**Význam:** Jedna z hlavních algebraických hypotéz o složitosti výpočtu; její důkaz by mimo jiné oddělil P a NP v modelu výpočtu nad komplexními čísly.

**Odlišení od dosavadního seznamu:** No τ-conjecture or integer-root versus straight-line-complexity question identified. Prior determinant/permanent questions ask about different resources.

**Stav a přesný rozsah:** Count distinct INTEGER roots and forbid arbitrary free constants. Real-root versions and additive-complexity variants are different conjectures.

**Primární podklady:**

- [A Direct Ultrametric Approach to Additive Complexity and the Shub-Smale Tau Conjecture](https://arxiv.org/abs/math/0304100) — Definition of τ and the conjecture.

## 9. Lattices and computational number theory

### 1. Polynomial-time, polynomial-factor approximation of Euclidean SVP

**Otázka:** Is there a constant C and a classical polynomial-time algorithm that, given a rank-n rational lattice basis, returns a nonzero lattice vector of Euclidean length at most n^C λ1(L)?

**Význam:** Určuje, zda lze nejkratší vektor efektivně aproximovat aspoň do polynomiálního faktoru; je to ústřední mezera mezi algoritmy pro mříže a kryptografickými předpoklady.

**Odlišení od dosavadního seznamu:** TCS-0655 asks to rule out n^ε-GapSVP under a standard assumption for SOME small ε; this is not equivalent to finding a vector within n^C for SOME possibly large C. TCS-0652 concerns dimension-preserving reductions, not this algorithm. TCS-0658 asks for conditional hardness at n^(3/2+ε) for some ε, including quantum algorithms; it likewise does not settle the existence of a classical algorithm at some arbitrarily larger fixed polynomial factor.

**Stav a přesný rozsah:** Classical search SVP in the Euclidean norm. A hardness result at a smaller polynomial approximation factor does not rule out an algorithm at a larger one.

**Primární podklady:**

- [The Complexity of the Shortest Vector Problem — Huck Bennett](https://www.cs.umd.edu/~gasarch/open/svp-color.pdf) — Figure 1 and Section 4.1, polynomial approximation regime.

## 10. Randomized algorithms and sampling

### 1. Polynomial mixing of critical three-dimensional Ising dynamics

**Otázka:** On the L×L×L box with free boundary, zero external field and inverse temperature βc(Z³), does single-site heat-bath Glauber dynamics for the nearest-neighbour ferromagnetic Ising model have total-variation mixing time L^O(1)?

**Význam:** Zásadní otázka účinného vzorkování při fázovém přechodu v nejběžnějším prostorovém modelu magnetismu.

**Odlišení od dosavadního seznamu:** No critical Z³ Ising mixing question identified; existing Ising records concern learning and different graph/model settings.

**Stav a přesný rozsah:** High-dimensional lattice results and the 2024 result at the tree uniqueness threshold do not resolve the three-dimensional lattice critical point. Status is assessed from these primary results and later-result searches.

**Primární podklady:**

- [Log-Sobolev inequality for near critical Ising models](https://arxiv.org/abs/2202.02301) — Critical-temperature discussion; polynomial bound for d>4.
- [Polynomial Mixing of the critical Glauber Dynamics for the Ising Model](https://arxiv.org/abs/2411.10318) — Tree-uniqueness threshold; not the Z³ critical point.

## 11. String algorithms and bioinformatics

### 1. Breaking factor two for sum-of-pairs multiple sequence alignment

**Otázka:** Does some universal ε>0 admit a polynomial-time (2−ε)-approximation for minimum sum-of-pairs multiple sequence alignment with an arbitrary number of input strings and metric substitution/gap costs?

**Význam:** Centrální optimalizační úloha bioinformatiky; otevřená je zásadní hranice kvality společného zarovnání mnoha sekvencí.

**Odlišení od dosavadního seznamu:** No sum-of-pairs MSA approximation question identified. Prior edit distance concerns TWO strings and running time.

**Stav a přesný rozsah:** The constant ε must not shrink with the number k of strings. Bounds 2−q/k for fixed q do not settle it. Distinguish sum-of-pairs from column scores and local alignment.

**Primární podklady:**

- [Multiple Sequence Alignment — encyclopedia article](https://i.cs.hku.hk/~chin/paper/encycl_msa-1.pdf) — Open Problems.
- [Some Open Problems in Computational Molecular Biology](https://profs.sci.univr.it/~rrizzi/classes/BioComp2003/homeworks/openProblems.pdf) — Open problem 1.

## 12. Dynamic graph algorithms

### 1. Polylogarithmic maintenance of the exact global minimum cut

**Otázka:** Can a fully dynamic simple undirected n-vertex graph maintain its exact global minimum-cut VALUE under edge insertions and deletions with polylog(n) amortized update time and polylog(n) query time, using polynomial space? Randomization against an oblivious update sequence is allowed.

**Význam:** Základní nezodpovězená otázka o udržování odolnosti celé sítě při změnách; cílem je přesný globální řez pro libovolnou hodnotu konektivity.

**Odlišení od dosavadního seznamu:** No selected exact fully dynamic global min-cut question identified. The previous small pass added connectivity, MSF and approximate matching.

**Stav a přesný rozsah:** The 2026 exact algorithm requires a bounded min-cut value; its general-graph consequence is approximate. Reporting every edge of the cut is not required.

**Primární podklady:**

- [Deterministic and Exact Fully-dynamic Minimum Cut of Superpolylogarithmic Size in Subpolynomial Time](https://arxiv.org/abs/2512.13105) — SODA 2026 results and minimum-cut-size restriction.
- [Unifying and Strengthening Hardness for Dynamic Problems via the Online Matrix-Vector Multiplication Conjecture](https://people.csail.mit.edu/virgi/6.s078/papers/omv.pdf) — Section 5.2, Minimum Cut open problem; distinguish global cuts from s–t cuts.

## 13. Counting and enumeration

### 1. An FPRAS for counting undirected Euler tours

**Otázka:** Is there an FPRAS for the number of Euler tours of an arbitrary connected Eulerian undirected graph, with running time polynomial in the input length and 1/ε and multiplicative error 1±ε with probability at least 3/4?

**Význam:** Základní dosud nevyřešený případ aproximovaného počítání kombinatorických objektů: ani pro tyto přirozené průchody grafem neznáme obecné efektivní vzorkování a počítání.

**Odlišení od dosavadního seznamu:** TCS-4537 asks to extend EXACT bounded-treewidth counting to bounded clique-width or chordal graphs (full conclusion read). TCS-6022 asks about PARALLEL sampling in Eulerian DIGRAPHS.

**Stav a přesný rozsah:** Do not confuse Euler tours with Eulerian orientations: approximate counting of the latter has an FPRAS. Fix a tour-counting convention; standard rotation/reversal factors do not affect FPRAS existence.

**Primární podklady:**

- [Mary Cryan — Euler-tours of low-height toroidal grids (SCM 2024)](https://sites.cs.st-andrews.ac.uk/scm2024/abstracts.html) — Invited talk abstract on Euler tours.

## 14. Property testing and distribution learning

### 1. Sublinear testing of bounded-degree graph isomorphism

**Otázka:** Given adjacency-list oracle access to two bounded-degree n-vertex graphs, can one distinguish isomorphism from requiring at least εdn edge changes to become isomorphic using o(n) queries, for every fixed degree bound d and fixed ε>0? Allow two-sided error with success probability at least 2/3.

**Význam:** Ptá se, zda lze přibližnou shodu dvou řídkých sítí rozhodnout bez přečtení celého vstupu; jde o základní hranici síly property testingu.

**Odlišení od dosavadního seznamu:** TCS-5459 concerns communication complexity of tolerant graph isomorphism testing. This is the ordinary adjacency-list QUERY model for bounded-degree graphs.

**Stav a přesný rozsah:** The source asks for the full query complexity and gives an n^(2/3) lower bound up to logarithmic factors for two unknown graphs. The first decisive target here is any truly sublinear tester.

**Primární podklady:**

- [Open Problems in Testing Graph Properties — Oded Goldreich](https://eccc.weizmann.ac.il/report/2021/088/) — Open Problem 2.4; PDF pp. 6–7.

## 15. Differential privacy

### 1. Optimal error for pure-DP continual counting

**Otázka:** For causal release of all prefix sums of a binary stream of length T, determine the asymptotic minimum of sup_x E[max_t |M_t(x)−sum_{i≤t}x_i|] over (1/2,0)-differentially private mechanisms, with neighbouring streams differing in one bit.

**Význam:** Průběžné počítání je základní stavební úloha privátní analýzy dat. Hledáme optimální cenu soukromí v celém časovém průběhu.

**Odlišení od dosavadního seznamu:** TCS-5198 selects a different online-learning model modification, verified in full p. 6. The first-pass DP question concerns offline arbitrary query release with normalized Euclidean error.

**Stav a přesný rozsah:** Pure privacy (δ=0), expected maximum error. The July 2026 paper resolves the approximate-DP dependence and leaves pure DP between log^(3/2)T and log²T for constant ε.

**Primární podklady:**

- [The Binary Tree Mechanism is Optimal for Approximate Differentially Private Continual Counting](https://arxiv.org/abs/2607.00876) — Table 1: remaining PURE-DP ℓ∞ gap.

## 16. Algorithmic game theory, mechanism design and fair division

### 1. The power of randomization in truthful unrelated-machine scheduling

**Otázka:** What is the asymptotically optimal approximation ratio, as a function of the number m of machines, achievable by truthful-in-expectation randomized mechanisms with payments for makespan minimization on unrelated machines? In particular, can the ratio be bounded by a universal constant?

**Význam:** Základní otázka mechanism designu: dokáže náhoda odstranit ztrátu, kterou způsobuje požadavek, aby účastníci pravdivě hlásili své náklady?

**Odlišení od dosavadního seznamu:** TCS-4944 selects the original deterministic Nisan–Ronen conjecture, now resolved. The randomized optimum remains a separate central question.

**Stav a přesný rozsah:** Fix truthfulness in expectation, indivisible jobs and expected makespan. The deterministic m lower bound does not extend automatically to randomized mechanisms. No computational restriction is needed for the core incentive-theoretic question.

**Primární podklady:**

- [A proof of the Nisan–Ronen conjecture](https://ora.ox.ac.uk/objects/uuid%3A814fc511-99e2-47cb-b06a-f472630996dc/files/r9593tw016) — Theorem 1 and Section 1.1.

## 17. Constraint satisfaction

### 1. Search-to-decision equivalence for finite promise CSPs

**Otázka:** For every fixed finite template pair A→B, does a polynomial-time algorithm distinguishing X→A from X↛B imply a polynomial-time algorithm which, on inputs promised to satisfy X→A, outputs a homomorphism X→B?

**Význam:** Rozhodnout, že relaxované řešení existuje, nemusí znamenat umět je najít. Vyřešení by stanovilo vztah dvou základních podob celé teorie promise CSP.

**Odlišení od dosavadního seznamu:** TCS-1978 only asks about templates solvable by BLP. This is the full search/decision equivalence, across all finite templates and all polynomial-time decision algorithms. The prior PCSP dichotomy proposal classifies decision complexity rather than asking for constructive solutions.

**Stav a přesný rozsah:** The FOCS 2025 result establishes obstacles to rounding relaxation witnesses; it explicitly leaves the general equivalence open. Count one general problem, not separate BLP/AIP follow-ups.

**Primární podklady:**

- [Ineffectiveness for Search and Undecidability of PCSP Meta-Problems (FOCS 2025) — author's summary](https://albertolarrauri.github.io/publications/) — First publication and summary.
- [An invitation to the promise constraint satisfaction problem](https://arxiv.org/abs/2208.13538) — Search and decision definitions.

## 18. Scheduling and packing

### 1. Breaking factor two for precedence-constrained makespan

**Otázka:** For precedence-constrained jobs on an input number m of identical parallel machines, does there exist a universal ε>0 and a polynomial-time (2−ε)-approximation for makespan P|prec|Cmax?

**Význam:** Jedna z klasických hlavních otázek scheduling theory: zda lze zásadně překonat jednoduchý list scheduling pro obecné precedence.

**Odlišení od dosavadního seznamu:** TCS-0924 concerns weighted completion time, while TCS-0935 fixes a small number of machines and unit jobs. Previous additions concern unrelated machines without precedences, Santa Claus and bin packing.

**Stav a přesný rozsah:** The number of machines belongs to the input. Known conditional hardness uses stronger assumptions; do not state a proven unconditional 2−ε impossibility.

**Primární podklady:**

- [Hardness of Precedence Constrained Scheduling on Identical Machines — Ola Svensson](https://theory.epfl.ch/osven/Ola%20Svensson_publications/SICOMP11b.pdf) — Abstract and introduction.

## 19. Automated reasoning and unification

### 1. The isomorphism problem for one-relator groups

**Otázka:** Is there an algorithm that, given two finite group presentations each with a single defining relator, decides whether the presented groups are isomorphic?

**Význam:** Jeden z klasických rozhodovacích problémů teorie grup pro zásadní a přirozenou třídu konečných prezentací; určujeme samotnou hranici algoritmické rozhodnutelnosti.

**Odlišení od dosavadního seznamu:** The earlier pass added conjugacy INSIDE a one-relator group, not isomorphism BETWEEN two presented groups. No catalogue isomorphism question for this class was identified.

**Stav a přesný rozsah:** Retain arbitrary one-relator groups; decidability for torsion, hyperbolic or generic subclasses is insufficient. Do not substitute the false general Magnus isomorphism conjecture.

**Primární podklady:**

- [The theory of one-relator groups: history and recent progress](https://arxiv.org/abs/2501.18306) — Introduction and section on decision problems.

## 20. Database theory and finite model theory

### 1. FO model checking on hereditary monadically dependent graph classes

**Otázka:** Under the usual effectiveness assumptions on the graph class, for every hereditary monadically dependent class C of finite graphs, is first-order model checking fixed-parameter tractable with parameter the formula length? Monadic dependence means that unary colouring and a fixed FO transduction cannot generate all finite graphs from C.

**Význam:** Ústřední pokus o charakterizaci tříd grafů, na nichž lze efektivně vyhodnocovat logické dotazy; propojuje databázovou teorii, konečné modely a strukturu grafů.

**Odlišení od dosavadního seznamu:** TCS-6082 selects footnote 3 on whether structurally bounded local clique-width implies almost bounded flip-width. Full source read: the overarching model-checking Conjecture I.1 is a different question. TCS-2401 asks for an indiscernible/flatness characterization, not an FO evaluation algorithm.

**Stav a přesný rozsah:** Use the standard class-wise/effective formulation of the FPT conjecture. Results for monadically STABLE classes do not establish it for all monadically DEPENDENT classes.

**Primární podklady:**

- [Rose McCarty — Oberwolfach 2025](https://mccarty.math.gatech.edu/McCarty-2025-Oberwolfach.pdf) — Model-checking conjecture.
- [Flip-Width: Cops and Robber on Dense Graphs](https://ieee-focs.org/FOCS-2023-Papers/pdfs/FOCS2023-35YPEGokY3iqqos5xlCDsn/189400a663/189400a663.pdf) — Conjecture I.1.

## 21. Computability and algorithmic information

### 1. Universality of Turing equivalence

**Otázka:** Is Turing equivalence on 2^N universal among countable Borel equivalence relations: for every countable Borel E on a standard Borel space X, is there a Borel f:X→2^N with xEy iff f(x)≡T f(y)?

**Význam:** Ptá se, zda struktura stejné výpočetní síly dokáže reprezentovat všechny spočetné borelovské klasifikační problémy; jde o klasickou otázku na rozhraní vyčíslitelnosti a deskriptivní teorie množin.

**Odlišení od dosavadního seznamu:** No universality question for Turing equivalence identified. Prior Martin's conjecture concerns degree-invariant functions and would imply a negative answer, but is not equivalent to this named classification problem.

**Stav a přesný rozsah:** Distinguish Turing equivalence from arithmetic equivalence, whose universality is known, and from uniform universality, which is a different restriction.

**Primární podklady:**

- [The Fourteen Victoria Delfino Problems and Their Status in the Year 2019](https://preprint.math.uni-hamburg.de/public/papers/hbm/hbm770.pdf) — Question 6 (Turing-equivalence universality), printed p. 16.
- [The Theory of Countable Borel Equivalence Relations — Alexander Kechris](https://www.pma.caltech.edu/documents/5921/CBER.pdf) — Problem 12.5.

## 22. Knowledge representation and reasoning

### 1. Decidability of conjunctive-query entailment in SROIQ

**Otázka:** Is Boolean conjunctive-query entailment decidable for arbitrary finite SROIQ knowledge bases, under the standard semantics over all models?

**Význam:** Základní neuzavřená hranice dotazování nad expresivními ontologiemi: ani rozhodnutelnost satisfiability sama o sobě neposkytuje rozhodnutelnost odpovědí na dotazy.

**Odlišení od dosavadního seznamu:** No SROIQ conjunctive-query entailment question identified. Existing database containment and finite-controllability questions use different formalisms and decision problems.

**Stav a přesný rozsah:** All-model semantics, not finite-model-only reasoning. Known Horn/sublogic algorithms or practical procedures with restricted queries do not settle full SROIQ.

**Primární podklady:**

- [Absorption-Based Query Entailment Checking for Expressive Description Logics](https://ceur-ws.org/Vol-2373/paper-25.pdf) — Introduction, general SROIQ decidability problem.
### 2. DNF versus d-DNNF succinctness

**Otázka:** Is there a family of polynomial-size DNF formulas for which every equivalent deterministic decomposable negation-normal-form circuit has superpolynomial size?

**Význam:** Určuje základní cenu determinismu při kompilaci znalostí do reprezentace, která umožňuje přesné počítání modelů.

**Odlišení od dosavadního seznamu:** Prior addition asks about deterministic equivalence testing of d-DNNF. TCS-0306 concerns complementation, and TCS-0496 concerns database lineages. None is the DNF versus d-DNNF size separation. TCS-0308 is the general Boolean formula-versus-circuit size gap (full linked section read); it does not require either DNF inputs or d-DNNF outputs.

**Stav a přesný rozsah:** This is a SIZE lower bound, not a polynomial-time conversion question; #P-hardness already rules out a generic efficient conversion under standard assumptions. DNNF versus d-DNNF separation alone does not settle it.

**Primární podklady:**

- [Florent Capelli — Habilitation manuscript](https://capelli.me/publi/hdr.pdf) — Open question 1, printed pp. 17–18.

## 23. Structural graph theory

### 1. Reed's χ–ω–Δ conjecture

**Otázka:** Does every finite graph satisfy χ(G)≤ceil((Δ(G)+1+ω(G))/2), where χ is chromatic number, Δ maximum degree and ω maximum clique size?

**Význam:** Jedna z hlavních strukturálních hypotéz o barvení; hledá univerzální vztah mezi lokální hustotou, klikami a počtem potřebných barev.

**Odlišení od dosavadního seznamu:** No selected Reed colouring conjecture identified. Prior Hadwiger, Erdős–Hajnal and Gyárfás–Sumner questions impose different structural relationships.

**Stav a přesný rozsah:** Fits the approved structural-colouring scope. General graphs are required; results for special classes or asymptotic relaxations do not prove this exact inequality.

**Primární podklady:**

- [Bounding χ by a fraction of Δ for graphs without large cliques](https://www.sciencedirect.com/science/article/abs/pii/S009589562200065X) — Introduction, Reed's 1998 conjecture.
### 2. The optimal quantitative Excluded Grid Theorem

**Otázka:** Let f(r) be the least treewidth threshold forcing an r×r grid minor in every graph. Is f(r)=O(r² polylog r), and what is its tight asymptotic order?

**Význam:** Základní kvantitativní otázka graph minor theory, která určuje sílu grid minorů jako překážek malé stromové šířky a nástroje algoritmických metateorémů.

**Odlišení od dosavadního seznamu:** TCS-4404 concerns a cylindrical/directed grid question. TCS-5475 concerns parameters in the graph-minor STRUCTURE theorem; it is not the treewidth threshold for an undirected grid minor.

**Stav a přesný rozsah:** The target is the optimal order, not a modest exponent improvement. Do not claim O(r²): the known lower bound includes log r. The cited literature records competing near-quadratic and cubic conjectures; the universally agreed open target is the tight threshold, not a consensus on the answer.

**Primární podklady:**

- [Towards Tight(er) Bounds for the Excluded Grid Theorem](https://arxiv.org/abs/1901.07944) — Introduction: Ω(r² log r) versus O(r⁹ polylog r).
- [Grid Minor Theorem Revisited](https://link.springer.com/article/10.1007/s00493-025-00168-w) — Quantitative grid-minor discussion.

## 24. Beyond worst-case and average-case analysis

### 1. The computational Kesten–Stigum threshold for sparse community recovery

**Otázka:** In the balanced symmetric sparse stochastic block model with a fixed q≥5 groups and edge probabilities a/n within groups and b/n between groups (a>b>0), can any polynomial-time algorithm achieve nonvanishing correlation with the planted labels below (a−b)²=q(a+(q−1)b), in the regime where recovery is information-theoretically possible?

**Význam:** Kanonický problém rozdílu mezi statistickou možností a efektivním výpočtem: zda skutečná výpočetní bariéra nastává na Kestenově–Stigumově prahu.

**Odlišení od dosavadního seznamu:** TCS-5248 addresses bipartite SBM spectral algorithms; TCS-5744 addresses SDP/Bayes-error behavior. Prior planted clique and tensor PCA concern other planted models. TCS-1187 is the distinct growing-number-of-communities regime q>sqrt(n), whereas this target fixes q.

**Stav a přesný rozsah:** The 2025 result is conditional on the extended low-degree conjecture. The proposed unrestricted polynomial-time barrier is not a proved theorem.

**Primární podklady:**

- [Low degree conjecture implies sharp computational thresholds in stochastic block model](https://arxiv.org/abs/2502.15024) — Abstract and main recovery theorem.

## 25. Miscellaneous

Nebyl nalezen dostatečně silný samostatný kandidát bez přirozeného domova v jiné kategorii. Zvažované otázky tile assembly vyžadují opatrné rozlišení již omezených nebo vyřešených modelů; do počtu je nepřidávám. Ani obecné kombinatorické hypotézy sem nepřesouvám jen pro zaplnění místa.


## Vyřazené a odložené směry

Viz [rejections.json](rejections.json). Zahrnuje duplicity, staré otázky vyřešené pozdějšími pracemi a nejasné formulace. Vyřazení z tohoto průchodu samo o sobě nemění stav starších karet.

## Audit a data

- [Strojový seznam](candidates.json) a CSV.
- [Lexikální shody a ruční rozlišení](novelty-audit.json).
- [Počty, otisk a omezení kontroly](final-audit.json).
- Snapshot porovnávaných otázek.
- [Předchozích 72 malých návrhů](../fundamental-small-20260910/proposal.md).
