**Co se nepočítá jako nový problém — kontrola 10. 9. 2026**

Níže je výběr významných vyřazených kandidátů, nikoli úplný seznam všech odmítnutých námětů. „Už v katalogu“ zahrnuje i původní otázku skrytou za názvem článku nebo zkrácenou citací.

| Problém | Důvod vyřazení |
|---|---|
| P vs NP; NP vs coNP; L vs NL | TCS-0001, TCS-0002, TCS-0004. |
| NP versus polynomial-size circuits | TCS-0021. |
| P vs NP∩coNP | TCS-0018. |
| TFNP-complete problem | TCS-4988. |
| NP-hardness of MCSP | TCS-5312; obecná otázka je přímo v původní pasáži. |
| Quantum PCP | TCS-6446. |
| BPP vs BQP; NP outside BQP | TCS-0036, TCS-0037. |
| QMA vs QCMA; QMA vs QMA(2) | TCS-6448, TCS-2229. |
| QMA versus perfect-completeness QMA₁ | TCS-4814; původní pasáž už obsahuje hlavní otázku. |
| Quantum advice | TCS-6449. |
| General graph isomorphism in P | **TCS-5750**: původní strana 1 výslovně obsahuje otázku GI v P. TCS-3885 samotná byla jen definice, ale další karta rozhodla o duplicitě. [Původní pasáž](https://drops.dagstuhl.de/storage/00lipics/lipics-vol202-mfcs2021/LIPIcs.MFCS.2021.37/LIPIcs.MFCS.2021.37.pdf). |
| Dynamic optimality of splay trees | TCS-6498. |
| Exact weighted APSP in truly subcubic time | TCS-6510. |
| Exact Matching | TCS-6511; bipartitní varianta též TCS-0611. |
| OMv conjecture | TCS-6503. |
| Deque, traversal, split conjectures; pairing heaps | TCS-6508, TCS-6512, TCS-6509, TCS-6514. |
| Polynomial-time learning of DNF | TCS-0023 i TCS-5358; nepočítat obecnou PAC verzi jako nový problém. |
| Proper/improper learning of decision trees | TCS-0677, TCS-4891, TCS-4972. |
| Efficient learning of one-hidden-layer ReLU networks | TCS-2111 obsahuje obecnou hlavní otázku i pro kladné váhy. |
| Recursive teaching dimension vs VC dimension | TCS-0691. |
| k-sets; edge unfolding; Euclidean MST | TCS-0318, TCS-0406, TCS-0403. |
| Sum of square roots | TCS-0055. |
| Deterministic NC matching | TCS-6504. |
| Directed reachability with near-linear parallel work and polylog depth | TCS-6507. |
| One cycle versus two cycles in MPC | TCS-6505. |
| Randomized LOCAL MIS in sublogarithmic time | TCS-6499. |
| Constant-round maximal independent set in congested clique | TCS-6501. |
| Word equations in NP; equivalence of unambiguous CFGs | TCS-0163, TCS-0164. |
| General Rabin–Mostowski index problem | TCS-6444 má v původní pasáži obecnou indexovou otázku. |
| Skolem problem; parity games in P | TCS-5773, TCS-4245. |
| Decidability of the real exponential field | TCS-3324. |
| BVASS reachability / MELL provability | TCS-1649. Ekvivalentní formulace se nepočítají dvakrát. |
| Strongly polynomial linear programming | TCS-0008, též TCS-5377. |
| Randomized k-server with o(k) competitive ratio | TCS-4983. |
| Matroid secretary conjecture | **TCS-5779** žádá universal online contention resolution scheme. Pozdější výsledek prokazuje ekvivalenci s hlavní matroid secretary conjecture: [Dughmi, ITCS 2022](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.ITCS.2022.58). |

**Výsledky, kvůli kterým by starší seznam otevřených problémů byl zavádějící**

| Kandidát | Kontrola stavu |
|---|---|
| Bourgain slicing a thin-shell | Vyřešeny. Pro thin-shell viz [Klartag–Lehec, 2025](https://arxiv.org/abs/2507.15495). KLS v novém seznamu je silnější zbývající otázka. |
| Good qLDPC a NLTS | Vyřešeny; nepřidávat jako otevřené. Požadavek lokální testovatelnosti s konstantní soundness u qLTC je samostatný a zůstává v shortlistu. |
| Překonání 1/2 pro jednoproudový semi-streaming matching | Červencový preprint 2026 dokazuje nemožnost překonat poměr 1/2, tedy optimalitu greedy: [Assadi–Jiang–Xiang](https://arxiv.org/abs/2607.14656). Původní otázku vyřadit z návrhu nových otevřených problémů; tato rešerše není nezávislou kontrolou celého důkazu. |
| Finite Janin–Walukiewicz theorem | Řešení publikováno v [ICALP 2025](https://drops.dagstuhl.de/storage/00lipics/lipics-vol334-icalp2025/html/LIPIcs.ICALP.2025.152/LIPIcs.ICALP.2025.152.html). |
| Pushdown VASS reachability | Rozhodnutelnost publikována v [LICS 2026](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.LICS.2026.53). |
| Randomized k-server with O(log k) ratio | Vyvráceno; viz [Bubeck–Coester–Rabani](https://arxiv.org/abs/2211.05753). |
| Smale 17 | Vyřešen; neplést se Smale 7 ze shortlistu. [Shub–Case, SIAM](https://www.siam.org/publications/siam-news/articles/the-final-touch-solving-smale-s-17th-challenge-problem/). |
| Samotná existence dimension-dependent competitive ratio pro convex body chasing | Už známá; novou otázkou je optimální závislost na dimenzi. |
| Jung–Tix problem | Srpen 2026 přinesl [preprint tvrdící řešení pomocí FVA domén](https://arxiv.org/abs/2608.03073). Bez podrobného srovnání původní a nové formulace jej jako otevřený nepočítám. |
| Lattice-based NIKE ve standardním modelu | Obecná stará formulace není bezpečná: [USENIX Security 2026](https://www.usenix.org/conference/usenixsecurity26/presentation/li-ying) přináší konstrukci z Modulus-LWE. Otázku pro běžné LWE by bylo nutné samostatně přesně ověřit. |

**Stažený důkaz: sample compression zůstává kandidátem**

[arXiv:2603.23561](https://arxiv.org/abs/2603.23561) měl dříve název tvrdící řešení sample compression conjecture. Aktuální záznam uvádí stažení a chybu v Lemma 2. Výsledek vyhledávače se starým titulkem proto nestačí jako důvod považovat otázku za vyřešenou. Otevřenou obecnou hypotézu znovu uvádí také [práce z dubna 2026](https://arxiv.org/abs/2604.02949).

**Náměty ponechané mimo shortlist**

Nepočítám unit-distance a další čistě kombinatorické geometrické hádanky, jednotlivé mezery v parametrech čerstvých algoritmů, nespecifikovaná přání „vysvětlit deep learning“ ani několik podobných variant jedné hypotézy. Deterministická lineárně pracná paralelní konektivita, přesná komplexita HDT0L equivalence a některé další starší otázky zůstaly pouze náměty; jejich stav a význam nebyly ověřeny dostatečně pro zařazení.

