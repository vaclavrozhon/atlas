# Editorial preference ranking — 23 October 2026

The user's request was to review the problems and order them by editorial preference within each category. This pass explicitly scored all 1,120 active cards in all 35 categories, including the 135 newly imported candidates.

## How to read the order

This is subjective editorial judgment based on saved titles and statement excerpts, with expanded summaries for sparse drafts. I favor consequential mathematical barriers, reusable structural principles, and concise conceptual targets. Conceptual clarity refers to the underlying question; unfinished prose and formalization effort do not reduce a score. Age, publication date and the length of a card do not increase it. This pass did not independently verify the literature or current open status.

The first five entries in each large category and the first two in each small category form a deliberately ordered focus prefix balancing importance and topic diversity. Remaining entries follow decreasing editorial scores, with stable-ID tie-breaking. Equal scores express comparable preference, not a hidden fine-grained distinction. Scores are rough editorial bands, not probabilities of truth, tractability or eventual solution.

Scientific motivation in each importance assessment is retained from the card, with new explicit comparisons at category level. Sparse drafts received targeted motivation based on their saved summaries. Statements, definitions, citations, scientific status, evidence and formulation-review flags are unchanged. In particular, a higher score does not promote a source candidate to a reviewed problem. Both saved girth-conjecture formulations receive the same score; this ranking pass does not merge cards.

The static catalogue and exports reproduce this editorial order. The existing live reader can apply community votes on top of it; voting behavior was not changed.

## Changes

- 988 cards changed their position within a category.
- 1087 scores changed; all 1,120 now have an explicit editorial assessment.
- 27 categories have a changed focus prefix.
- The nested exports contain 100, 488 and 886 entries respectively. Existing per-category quotas remain unchanged.
- Newly imported candidates represented: 1 in Top 100 and 39 in Top 500.
- Non-ranking card content was verified unchanged by hashes for every active card.

## Audit and reproduction

decisions.json contains every individually assigned score tier, the ordered focus prefixes and the category comparisons. before.json preserves the previous assessments, ranks and focus selections. apply_ranking.py applies those choices after validating complete and unique coverage. It does not infer priority from keywords or reuse old scores to select the new tiers. After make publish, report.py verifies all 35 orders and produces this report and audit.json. validation.json records the completed checks.

## Complete ranking

Previous position refers to the local catalogue immediately before this ranking pass. Focus marks the Top 100 prefix. Every row links to its canonical card.

### Computational complexity

Favor foundational separations, concrete circuit lower bounds and meta-complexity. Keep time, space and circuits visible rather than filling the prefix with NP variants.

| Rank | Previous | Score | Focus | Problem |
| ---: | ---: | ---: | :---: | --- |
| 1 | 1 | 100 | yes | [P versus NP](../../data/cards/TCS-0001.json) (TCS-0001) |
| 2 | 9 | 96 | yes | [Superlinear Boolean circuit lower bounds](../../data/cards/TCS-0015.json) (TCS-0015) |
| 3 | 15 | 96 | yes | [L versus NL](../../data/cards/TCS-0004.json) (TCS-0004) |
| 4 | 13 | 94 | yes | [Minimum Circuit Size Problem](../../data/cards/TCS-4786.json) (TCS-4786) |
| 5 | 2 | 98 | yes | [P versus PSPACE](../../data/cards/TCS-6530.json) (TCS-6530) |
| 6 | 8 | 98 |  | [NP versus coNP](../../data/cards/TCS-0002.json) (TCS-0002) |
| 7 | 7 | 98 |  | [NP versus P/poly](../../data/cards/TCS-0021.json) (TCS-0021) |
| 8 | 6 | 98 |  | [Strictness of the polynomial hierarchy](../../data/cards/TCS-6532.json) (TCS-6532) |
| 9 | 23 | 94 |  | [Polynomial-size circuits for EXP](../../data/cards/TCS-0020.json) (TCS-0020) |
| 10 | 3 | 94 |  | [L versus P](../../data/cards/TCS-6531.json) (TCS-6531) |
| 11 | 4 | 94 |  | [Nonuniform \(\mathrm{TC}^{0}\) versus \(\mathrm{NC}^{1}\)](../../data/cards/TCS-6535.json) (TCS-6535) |
| 12 | 12 | 94 |  | [NEXP versus nonuniform \(\mathrm{TC}^{0}\)](../../data/cards/TCS-7161.json) (TCS-7161) |
| 13 | 10 | 90 |  | [Exponential circuit lower bounds for 3-SAT](../../data/cards/TCS-0016.json) (TCS-0016) |
| 14 | 41 | 90 |  | [KRW formula-size conjecture with constant loss](../../data/cards/TCS-0017.json) (TCS-0017) |
| 15 | 31 | 90 |  | [Exponential lower bounds for unrestricted threshold-of-threshold circuits](../../data/cards/TCS-1054.json) (TCS-1054) |
| 16 | 27 | 90 |  | [Majority outside constant-depth modular circuits](../../data/cards/TCS-1056.json) (TCS-1056) |
| 17 | 5 | 90 |  | [Berman–Hartmanis conjecture](../../data/cards/TCS-6534.json) (TCS-6534) |
| 18 | 29 | 90 |  | [Directed reachability in polynomial time and polylogarithmic space](../../data/cards/TCS-6817.json) (TCS-6817) |
| 19 | 17 | 90 |  | [Ruling out quasilinear-time SAT without a space restriction](../../data/cards/TCS-6977.json) (TCS-6977) |
| 20 | 11 | 90 |  | [PH versus PSPACE](../../data/cards/TCS-7158.json) (TCS-7158) |
| 21 | 30 | 86 |  | [P versus NP intersect coNP](../../data/cards/TCS-0018.json) (TCS-0018) |
| 22 | 61 | 86 |  | [Subquadratic deterministic simulation of nondeterministic space](../../data/cards/TCS-0293.json) (TCS-0293) |
| 23 | 16 | 86 |  | [Existence of TFNP-complete problems](../../data/cards/TCS-4988.json) (TCS-4988) |
| 24 | 24 | 86 |  | [Exponential depth-three \(\mathrm{AC}^{0}\) lower bounds for E](../../data/cards/TCS-6091.json) (TCS-6091) |
| 25 | 14 | 86 |  | [NL versus UL](../../data/cards/TCS-6533.json) (TCS-6533) |
| 26 | 39 | 86 |  | [Nonuniform \(\mathrm{NC}^{1}\) perfect matching](../../data/cards/TCS-6714.json) (TCS-6714) |
| 27 | 18 | 86 |  | [Sliding-scale PCP conjecture](../../data/cards/TCS-7268.json) (TCS-7268) |
| 28 | 19 | 86 |  | [\(\mathrm P_{\mathbb R}\) versus \(\mathrm{NP}_{\mathbb R}\)](../../data/cards/TCS-7321.json) (TCS-7321) |
| 29 | 20 | 86 |  | [\(\exists\mathbb{R}\) versus \(\mathrm{NP}\)](../../data/cards/TCS-7363.json) (TCS-7363) |
| 30 | 51 | 82 |  | [Polynomial formulas versus linear circuits](../../data/cards/TCS-0019.json) (TCS-0019) |
| 31 | 57 | 82 |  | [Supercubic uniform formula lower bounds for SAT](../../data/cards/TCS-0305.json) (TCS-0305) |
| 32 | 58 | 82 |  | [Depth-three lower bounds beyond the log-depth simulation threshold](../../data/cards/TCS-1052.json) (TCS-1052) |
| 33 | 59 | 82 |  | [Depth-three circuit lower bounds beyond the square-root exponent](../../data/cards/TCS-1053.json) (TCS-1053) |
| 34 | 54 | 82 |  | [Doubly efficient \(\mathrm{IP}=\mathrm{PSPACE}\)](../../data/cards/TCS-6455.json) (TCS-6455) |
| 35 | 25 | 82 |  | [Randomized evasiveness conjecture](../../data/cards/TCS-6743.json) (TCS-6743) |
| 36 | 26 | 82 |  | [Independence of P versus NP from ZFC](../../data/cards/TCS-6979.json) (TCS-6979) |
| 37 | 22 | 82 |  | [CLS versus FP](../../data/cards/TCS-7286.json) (TCS-7286) |
| 38 | 65 | 78 |  | [Nonlinear-gate advantages for binary linear operators](../../data/cards/TCS-1040.json) (TCS-1040) |
| 39 | 32 | 78 |  | [Black-Box Hypothesis](../../data/cards/TCS-5593.json) (TCS-5593) |
| 40 | 45 | 78 |  | [Is ARRIVAL solvable in polynomial time?](../../data/cards/TCS-6006.json) (TCS-6006) |
| 41 | 33 | 78 |  | [Does NP-hardness of MCSP imply circuit lower bounds for EXP?](../../data/cards/TCS-6168.json) (TCS-6168) |
| 42 | 28 | 78 |  | [Graph nonisomorphism in BPP](../../data/cards/TCS-6747.json) (TCS-6747) |
| 43 | 34 | 78 |  | [Hartmanis–Stearns conjecture](../../data/cards/TCS-7159.json) (TCS-7159) |
| 44 | 47 | 78 |  | [Reversible simulation in polynomial time and linear space](../../data/cards/TCS-7256.json) (TCS-7256) |
| 45 | 35 | 74 |  | [UNSAT multi-prover proofs with efficient SAT-oracle provers](../../data/cards/TCS-0298.json) (TCS-0298) |
| 46 | 36 | 74 |  | [Excluding one-sided randomized quasilinear-time log-space SAT](../../data/cards/TCS-0301.json) (TCS-0301) |
| 47 | 64 | 74 |  | [Cost of restricting linear circuits to depth two](../../data/cards/TCS-1035.json) (TCS-1035) |
| 48 | 38 | 74 |  | [Downward self-reducibility of PLS-complete problems](../../data/cards/TCS-2333.json) (TCS-2333) |
| 49 | 44 | 74 |  | [NEXP circuit lower bounds from uniform obfuscation](../../data/cards/TCS-2532.json) (TCS-2532) |
| 50 | 46 | 74 |  | [Closure of UL under complement](../../data/cards/TCS-6285.json) (TCS-6285) |
| 51 | 69 | 74 |  | [Unconditional exclusion of linear-time CNF satisfiability](../../data/cards/TCS-6934.json) (TCS-6934) |
| 52 | 55 | 74 |  | [Formula versus circuit noise thresholds](../../data/cards/TCS-7257.json) (TCS-7257) |
| 53 | 42 | 70 |  | [A counting characterization of P with NP access](../../data/cards/TCS-0297.json) (TCS-0297) |
| 54 | 43 | 70 |  | [Improving the log-space SAT time exponent beyond 2 cos(π/7)](../../data/cards/TCS-0303.json) (TCS-0303) |
| 55 | 66 | 70 |  | [Largest separation between SUM and OR circuits](../../data/cards/TCS-1034.json) (TCS-1034) |
| 56 | 67 | 70 |  | [Unbounded XOR-over-OR complexity separations](../../data/cards/TCS-1036.json) (TCS-1036) |
| 57 | 37 | 70 |  | [Real quantifier alternation versus summation](../../data/cards/TCS-2215.json) (TCS-2215) |
| 58 | 48 | 70 |  | [Closure of SZK under truth-table reductions](../../data/cards/TCS-2425.json) (TCS-2425) |
| 59 | 52 | 70 |  | [Complete problem for Search-SZK](../../data/cards/TCS-3862.json) (TCS-3862) |
| 60 | 53 | 70 |  | [Subexponential derandomization with two-way random-tape access](../../data/cards/TCS-6139.json) (TCS-6139) |
| 61 | 60 | 66 |  | [FBPP versus negligible-error FBPP](../../data/cards/TCS-2029.json) (TCS-2029) |
| 62 | 68 | 66 |  | [UEOPL versus EOPL](../../data/cards/TCS-2681.json) (TCS-2681) |
| 63 | 49 | 66 |  | [\(\exists\!\cdot\!\mathrm{BPP}\) versus MA](../../data/cards/TCS-3886.json) (TCS-3886) |
| 64 | 50 | 66 |  | [Effective enumeration of BPP](../../data/cards/TCS-4746.json) (TCS-4746) |
| 65 | 40 | 66 |  | [Linear-size circuits for stable ternary compaction](../../data/cards/TCS-7243.json) (TCS-7243) |
| 66 | 63 | 62 |  | [Polynomial-time weighted falsifiability of unambiguous DNFs](../../data/cards/TCS-0310.json) (TCS-0310) |
| 67 | 62 | 62 |  | [Deterministic query complexity of tournament kings](../../data/cards/TCS-1602.json) (TCS-1602) |
| 68 | 21 | 62 |  | [DNF versus d-DNNF succinctness](../../data/cards/TCS-6681.json) (TCS-6681) |
| 69 | 56 | 62 |  | [Polynomial-size closure of d-DNNF under negation](../../data/cards/TCS-7260.json) (TCS-7260) |

### Algorithms

Favor basic primitives and reusable compression principles: sorting, terminal flow representation, sparsification and output-sensitive computation, before narrow graph-class classifications.

| Rank | Previous | Score | Focus | Problem |
| ---: | ---: | ---: | :---: | --- |
| 1 | 1 | 96 | yes | [Expected linear-time integer sorting for every word length](../../data/cards/TCS-6537.json) (TCS-6537) |
| 2 | 2 | 92 | yes | [Sorting \(X + Y\)](../../data/cards/TCS-0388.json) (TCS-0388) |
| 3 | 28 | 90 | yes | [Size-bounded approximate multicommodity-flow sparsifiers](../../data/cards/TCS-7380.json) (TCS-7380) |
| 4 | 3 | 92 | yes | [Hypergraph cut sparsifiers with \(O(n/\varepsilon ^{2})\) hyperedges](../../data/cards/TCS-0946.json) (TCS-0946) |
| 5 | 5 | 90 | yes | [Near-linear output-sensitive Subset Sum](../../data/cards/TCS-7350.json) (TCS-7350) |
| 6 | 6 | 90 |  | [Small Implicit Graph Conjecture](../../data/cards/TCS-5705.json) (TCS-5705) |
| 7 | 12 | 86 |  | [Quadratic-size submodular hypergraph sparsifiers](../../data/cards/TCS-2018.json) (TCS-2018) |
| 8 | 8 | 86 |  | [Quasipolynomial dependence on vertices for hypergraph isomorphism](../../data/cards/TCS-3346.json) (TCS-3346) |
| 9 | 7 | 86 |  | [Optimal size of four-additive graph spanners](../../data/cards/TCS-6783.json) (TCS-6783) |
| 10 | 14 | 86 |  | [Optimal additive error of linear-size spanners](../../data/cards/TCS-6785.json) (TCS-6785) |
| 11 | 20 | 82 |  | [Strongly polynomial planar minimum-cost flow](../../data/cards/TCS-0809.json) (TCS-0809) |
| 12 | 11 | 82 |  | [Isomorphism dichotomy for finitely forbidden hereditary classes](../../data/cards/TCS-6421.json) (TCS-6421) |
| 13 | 27 | 82 |  | [Spanners matching Thorup–Zwick emulator tradeoffs](../../data/cards/TCS-6784.json) (TCS-6784) |
| 14 | 16 | 82 |  | [Complexity of general vertex-connectivity augmentation](../../data/cards/TCS-7075.json) (TCS-7075) |
| 15 | 18 | 82 |  | [Linear-time exact inversion counting](../../data/cards/TCS-7351.json) (TCS-7351) |
| 16 | 4 | 78 |  | [Near-linear-time approximation of reachability diameter](../../data/cards/TCS-1141.json) (TCS-1141) |
| 17 | 21 | 78 |  | [Set-system sparsifiers of size proportional to chain length](../../data/cards/TCS-1338.json) (TCS-1338) |
| 18 | 9 | 78 |  | [Complexity of planar 3-edge-colorability](../../data/cards/TCS-5969.json) (TCS-5969) |
| 19 | 13 | 78 |  | [Three disjoint directed shortest paths](../../data/cards/TCS-6173.json) (TCS-6173) |
| 20 | 15 | 78 |  | [Polynomial-time detection of fixed pivot- and vertex-minors](../../data/cards/TCS-7146.json) (TCS-7146) |
| 21 | 10 | 74 |  | [Planarity dichotomy for induced subdivision detection](../../data/cards/TCS-1617.json) (TCS-1617) |
| 22 | 23 | 74 |  | [Polynomial-time minimum-total-length disjoint paths for fixed k](../../data/cards/TCS-3263.json) (TCS-3263) |
| 23 | 25 | 74 |  | [Polynomial-time independent set under a forbidden forest](../../data/cards/TCS-6251.json) (TCS-6251) |
| 24 | 17 | 74 |  | [A dichotomy for edge deletion with finitely many forbidden induced subgraphs](../../data/cards/TCS-7061.json) (TCS-7061) |
| 25 | 19 | 70 |  | [Near-linear constant-factor minimum-degree spanning trees](../../data/cards/TCS-0538.json) (TCS-0538) |
| 26 | 22 | 70 |  | [Complexity of directed detours](../../data/cards/TCS-2822.json) (TCS-2822) |
| 27 | 24 | 70 |  | [Linear-time directed bottleneck paths and trees](../../data/cards/TCS-4417.json) (TCS-4417) |
| 28 | 26 | 70 |  | [Near-linear-query reconstruction of bounded-degree graphs](../../data/cards/TCS-6270.json) (TCS-6270) |

### Automata and formal languages

Favor canonical barriers in synchronization, nondeterminism, expressive power and equivalence. Broad characterizations outrank model-specific closure questions.

| Rank | Previous | Score | Focus | Problem |
| ---: | ---: | ---: | :---: | --- |
| 1 | 1 | 96 | yes | [Maximum reset threshold of synchronizing automata](../../data/cards/TCS-6558.json) (TCS-6558) |
| 2 | 2 | 96 | yes | [Sakoda–Sipser problem](../../data/cards/TCS-6560.json) (TCS-6560) |
| 3 | 3 | 92 | yes | [Generalized star-height problem](../../data/cards/TCS-6559.json) (TCS-6559) |
| 4 | 8 | 90 | yes | [Decidability of equivalence for unambiguous context-free grammars](../../data/cards/TCS-0164.json) (TCS-0164) |
| 5 | 7 | 90 | yes | [First-order definability of regular tree languages](../../data/cards/TCS-6564.json) (TCS-6564) |
| 6 | 4 | 90 |  | [Decidability of every level of the dot-depth hierarchy](../../data/cards/TCS-6561.json) (TCS-6561) |
| 7 | 5 | 86 |  | [Equivalence of deterministic macro tree transducers](../../data/cards/TCS-6563.json) (TCS-6563) |
| 8 | 6 | 86 |  | [Equivalence of deterministic higher-order recursion schemes](../../data/cards/TCS-6582.json) (TCS-6582) |
| 9 | 15 | 86 |  | [Linear-time minimization of deterministic finite automata](../../data/cards/TCS-7261.json) (TCS-7261) |
| 10 | 40 | 86 |  | [Decidability of the nondeterministic tree-automaton index problem](../../data/cards/TCS-7431.json) (TCS-7431) |
| 11 | 18 | 82 |  | [Separating words problem](../../data/cards/TCS-0154.json) (TCS-0154) |
| 12 | 14 | 82 |  | [Primitive words and context-freeness](../../data/cards/TCS-0167.json) (TCS-0167) |
| 13 | 17 | 82 |  | [Two-dimensional cellular-automaton limit sets](../../data/cards/TCS-6064.json) (TCS-6064) |
| 14 | 32 | 82 |  | [Complement closure of conjunctive languages](../../data/cards/TCS-7406.json) (TCS-7406) |
| 15 | 35 | 82 |  | [Dense periodic behavior in surjective one-dimensional cellular automata](../../data/cards/TCS-7409.json) (TCS-7409) |
| 16 | 28 | 78 |  | [State complexity of complementing unambiguous automata](../../data/cards/TCS-0128.json) (TCS-0128) |
| 17 | 20 | 78 |  | [Polynomial-time universality for unambiguous context-free grammars](../../data/cards/TCS-0146.json) (TCS-0146) |
| 18 | 23 | 78 |  | [A \(\mathrm{TC}^{0}/\mathrm{NC}^{1}\) dichotomy for visibly pushdown languages](../../data/cards/TCS-2243.json) (TCS-2243) |
| 19 | 13 | 78 |  | [Equivalence of discounted-sum automata](../../data/cards/TCS-5904.json) (TCS-5904) |
| 20 | 10 | 78 |  | [Complexity of the Game of Life limit set](../../data/cards/TCS-5959.json) (TCS-5959) |
| 21 | 34 | 78 |  | [Deciding pattern avoidance over a prescribed alphabet](../../data/cards/TCS-7408.json) (TCS-7408) |
| 22 | 36 | 78 |  | [Nondeterminism versus determinism with two two-way heads](../../data/cards/TCS-7410.json) (TCS-7410) |
| 23 | 22 | 74 |  | [Zeroness of rational weighted context-free grammars](../../data/cards/TCS-0135.json) (TCS-0135) |
| 24 | 27 | 74 |  | [Periodic configurations in low-complexity two-dimensional shifts of finite type](../../data/cards/TCS-3378.json) (TCS-3378) |
| 25 | 21 | 74 |  | [Decidability of discounted-sum universality over infinite words](../../data/cards/TCS-4575.json) (TCS-4575) |
| 26 | 12 | 74 |  | [Recognizing good-for-games and good-for-MDP automata](../../data/cards/TCS-5651.json) (TCS-5651) |
| 27 | 37 | 74 |  | [Isomorphism of tree-automatic ordinals without addition](../../data/cards/TCS-7412.json) (TCS-7412) |
| 28 | 25 | 70 |  | [Deterministic separability of nondeterministic timed languages](../../data/cards/TCS-0138.json) (TCS-0138) |
| 29 | 11 | 70 |  | [Containment of finitely ambiguous probabilistic automata](../../data/cards/TCS-3863.json) (TCS-3863) |
| 30 | 29 | 70 |  | [Does adding modular predicates preserve decidable first-order definability?](../../data/cards/TCS-4636.json) (TCS-4636) |
| 31 | 26 | 70 |  | [Deciding first-order definability of orbit-finite automata](../../data/cards/TCS-4677.json) (TCS-4677) |
| 32 | 19 | 70 |  | [Recognizable separability of automatic relations](../../data/cards/TCS-5738.json) (TCS-5738) |
| 33 | 16 | 70 |  | [Decidability of stochastic resolvability for \(\omega\)-automata](../../data/cards/TCS-5863.json) (TCS-5863) |
| 34 | 9 | 70 |  | [Decidability with two parametric clocks and arbitrarily many integer parameters](../../data/cards/TCS-7309.json) (TCS-7309) |
| 35 | 30 | 66 |  | [Unconditional containment of unambiguous probabilistic automata](../../data/cards/TCS-0133.json) (TCS-0133) |
| 36 | 24 | 66 |  | [Universality of unambiguous register automata over ordered integers](../../data/cards/TCS-0136.json) (TCS-0136) |
| 37 | 31 | 66 |  | [Determinacy of Wadge games for Muller tree languages](../../data/cards/TCS-4659.json) (TCS-4659) |
| 38 | 33 | 66 |  | [Greibach normal form for conjunctive grammars](../../data/cards/TCS-7407.json) (TCS-7407) |
| 39 | 38 | 62 |  | [Complement closure of deterministic finite-testable counter languages](../../data/cards/TCS-7413.json) (TCS-7413) |
| 40 | 39 | 62 |  | [Complementing unambiguous partially blind counter languages](../../data/cards/TCS-7414.json) (TCS-7414) |

### Semantics, logic and verification

Favor compact decidability boundaries, algorithmic games, and foundations of proof assistants and program logic. Represent several foundations rather than only recurrence variants.

| Rank | Previous | Score | Focus | Problem |
| ---: | ---: | ---: | :---: | --- |
| 1 | 7 | 96 | yes | [Skolem problem](../../data/cards/TCS-5773.json) (TCS-5773) |
| 2 | 6 | 94 | yes | [Parity games in polynomial time](../../data/cards/TCS-4245.json) (TCS-4245) |
| 3 | 9 | 96 | yes | [Tarski’s exponential function problem](../../data/cards/TCS-7230.json) (TCS-7230) |
| 4 | 3 | 90 | yes | [Internal semisimplicial types in ordinary HoTT](../../data/cards/TCS-6569.json) (TCS-6569) |
| 5 | 13 | 90 | yes | [Decidability of multiplicative-exponential linear logic](../../data/cards/TCS-7192.json) (TCS-7192) |
| 6 | 1 | 94 |  | [Positivity problem for linear recurrences](../../data/cards/TCS-6565.json) (TCS-6565) |
| 7 | 2 | 92 |  | [Simple stochastic games in polynomial time](../../data/cards/TCS-6567.json) (TCS-6567) |
| 8 | 8 | 92 |  | [Mean-payoff games in polynomial time](../../data/cards/TCS-6568.json) (TCS-6568) |
| 9 | 10 | 86 |  | [Continuous Skolem problem](../../data/cards/TCS-6566.json) (TCS-6566) |
| 10 | 4 | 86 |  | [Scott-continuous lambda models with theory \(\lambda \beta\)](../../data/cards/TCS-6570.json) (TCS-6570) |
| 11 | 5 | 86 |  | [Barendregt–Geuvers–Klop conjecture](../../data/cards/TCS-6583.json) (TCS-6583) |
| 12 | 11 | 86 |  | [Ultimate Positivity problem](../../data/cards/TCS-7153.json) (TCS-7153) |
| 13 | 12 | 86 |  | [Termination of linear-constraint loops](../../data/cards/TCS-7157.json) (TCS-7157) |
| 14 | 47 | 86 |  | [Commutativity of the full probabilistic powerdomain monad](../../data/cards/TCS-7428.json) (TCS-7428) |
| 15 | 26 | 82 |  | [Decidability of branching-VASS reachability](../../data/cards/TCS-1649.json) (TCS-1649) |
| 16 | 30 | 82 |  | [Consistency of excluded middle and Church’s thesis in Coq](../../data/cards/TCS-3031.json) (TCS-3031) |
| 17 | 21 | 82 |  | [Inductive-inductive types from inductive types without UIP](../../data/cards/TCS-3655.json) (TCS-3655) |
| 18 | 15 | 82 |  | [Constructive simplicial model with univalent universes](../../data/cards/TCS-5915.json) (TCS-5915) |
| 19 | 31 | 82 |  | [Univalence, impredicativity and propositional resizing](../../data/cards/TCS-6112.json) (TCS-6112) |
| 20 | 23 | 82 |  | [Decidability and completeness of concurrent Kleene algebra with parallel iteration](../../data/cards/TCS-6359.json) (TCS-6359) |
| 21 | 41 | 82 |  | [Deciding MSO-definable choice on the infinite binary tree](../../data/cards/TCS-7418.json) (TCS-7418) |
| 22 | 49 | 82 |  | [Satisfiability with two variables and one transitive relation](../../data/cards/TCS-7432.json) (TCS-7432) |
| 23 | 34 | 78 |  | [Word problem for the S-combinator](../../data/cards/TCS-0913.json) (TCS-0913) |
| 24 | 22 | 78 |  | [One-dimensional piecewise-affine reachability](../../data/cards/TCS-5682.json) (TCS-5682) |
| 25 | 18 | 78 |  | [Effective homotopy canonicity with propositional resizing](../../data/cards/TCS-5817.json) (TCS-5817) |
| 26 | 42 | 78 |  | [Continuous-time synthesis for Metric Interval Temporal Logic](../../data/cards/TCS-7419.json) (TCS-7419) |
| 27 | 43 | 78 |  | [Polynomial-time quantitative stochastic parity verification](../../data/cards/TCS-7423.json) (TCS-7423) |
| 28 | 44 | 78 |  | [Fully abstract game semantics for pure call-by-value](../../data/cards/TCS-7425.json) (TCS-7425) |
| 29 | 45 | 78 |  | [Finite algebraic axiomatization of full guarded KAT](../../data/cards/TCS-7426.json) (TCS-7426) |
| 30 | 48 | 78 |  | [Decidability of the infinite target discounted-sum problem](../../data/cards/TCS-7430.json) (TCS-7430) |
| 31 | 37 | 74 |  | [Decidability of termination for one left- and right-linear term rule](../../data/cards/TCS-0901.json) (TCS-0901) |
| 32 | 33 | 74 |  | [Relative completeness of Kleene induction for the positive calculus of relations](../../data/cards/TCS-4017.json) (TCS-4017) |
| 33 | 17 | 74 |  | [Exact multi-objective LTL achievability in stochastic games](../../data/cards/TCS-4302.json) (TCS-4302) |
| 34 | 19 | 74 |  | [Decidability of weak bisimulation for normed BPA](../../data/cards/TCS-5987.json) (TCS-5987) |
| 35 | 24 | 74 |  | [Decidability of restricted elementary real functions](../../data/cards/TCS-6036.json) (TCS-6036) |
| 36 | 20 | 74 |  | [Unconditional decidability of exact time-bounded CTMDP reachability](../../data/cards/TCS-7310.json) (TCS-7310) |
| 37 | 39 | 74 |  | [Craig interpolation for Gödel logic with function symbols](../../data/cards/TCS-7416.json) (TCS-7416) |
| 38 | 28 | 70 |  | [Linear-length witnesses for reachability in each fixed vector addition system](../../data/cards/TCS-0632.json) (TCS-0632) |
| 39 | 36 | 70 |  | [Computable one-step normalization for finite confluent term rewriting](../../data/cards/TCS-0896.json) (TCS-0896) |
| 40 | 29 | 70 |  | [Elementary-time reachability for one-dimensional grammar-controlled VAS](../../data/cards/TCS-2033.json) (TCS-2033) |
| 41 | 16 | 70 |  | [Exponential witness bounds for three-dimensional VASS](../../data/cards/TCS-6245.json) (TCS-6245) |
| 42 | 14 | 70 |  | [Effective ultimate-positivity thresholds for simple recurrences](../../data/cards/TCS-7154.json) (TCS-7154) |
| 43 | 40 | 70 |  | [Effective prenex normalization for countable Gödel truth-value sets](../../data/cards/TCS-7417.json) (TCS-7417) |
| 44 | 46 | 70 |  | [Cut elimination for \(\mu\mathrm{LK}_{p}^{+}\)](../../data/cards/TCS-7427.json) (TCS-7427) |
| 45 | 38 | 66 |  | [A coanalytic upper bound for fair almost-sure termination](../../data/cards/TCS-0092.json) (TCS-0092) |
| 46 | 25 | 66 |  | [TOWER-hard reachability with seven nonnegative counters](../../data/cards/TCS-0619.json) (TCS-0619) |
| 47 | 32 | 66 |  | [Shortest runs in 3-D VASS](../../data/cards/TCS-0640.json) (TCS-0640) |
| 48 | 35 | 66 |  | [Exact finite-iteration reachability for Bellman operators](../../data/cards/TCS-1659.json) (TCS-1659) |
| 49 | 27 | 66 |  | [Decisiveness of static probabilistic Petri nets for finite targets](../../data/cards/TCS-5975.json) (TCS-5975) |
| 50 | 50 | 66 |  | [Decidability of the full alternating uniform one-dimensional fragment](../../data/cards/TCS-7433.json) (TCS-7433) |
| 51 | 51 | 66 |  | [Uniform cut elimination with digging and fixed points](../../data/cards/TCS-7435.json) (TCS-7435) |

### Distributed, parallel and sublinear algorithms

Favor the limits of parallelism and locality, derandomization of matching, and lower bounds for powerful communication models. General primitives and streaming characterizations precede individual tradeoff improvements.

| Rank | Previous | Score | Focus | Problem |
| ---: | ---: | ---: | :---: | --- |
| 1 | 1 | 98 | yes | [P versus NC](../../data/cards/TCS-6553.json) (TCS-6553) |
| 2 | 3 | 96 | yes | [Perfect matching in NC](../../data/cards/TCS-6504.json) (TCS-6504) |
| 3 | 4 | 92 | yes | [Distributed Lovász Local Lemma in \(O(\log  \log  n)\) rounds](../../data/cards/TCS-6554.json) (TCS-6554) |
| 4 | 13 | 92 | yes | [One-cycle versus two-cycles conjecture](../../data/cards/TCS-6505.json) (TCS-6505) |
| 5 | 6 | 92 | yes | [Explicit superconstant lower bounds in the congested clique](../../data/cards/TCS-6557.json) (TCS-6557) |
| 6 | 8 | 92 |  | [Work-efficient parallel directed reachability](../../data/cards/TCS-6507.json) (TCS-6507) |
| 7 | 12 | 90 |  | [Sublogarithmic distributed MIS](../../data/cards/TCS-6499.json) (TCS-6499) |
| 8 | 14 | 90 |  | [Logarithmic-round deterministic maximal independent set](../../data/cards/TCS-6506.json) (TCS-6506) |
| 9 | 7 | 90 |  | [Almost-linear-work parallel exact maximum flow](../../data/cards/TCS-7349.json) (TCS-7349) |
| 10 | 19 | 86 |  | [Deterministic volume gap](../../data/cards/TCS-0515.json) (TCS-0515) |
| 11 | 10 | 86 |  | [Quantum 3-coloring of cycles in \(o(\log^{*}n)\) rounds](../../data/cards/TCS-0522.json) (TCS-0522) |
| 12 | 5 | 86 |  | [Optimal exact single-source shortest paths in CONGEST](../../data/cards/TCS-6555.json) (TCS-6555) |
| 13 | 2 | 86 |  | [Directed reachability with nearly linear memory and polylogarithmic passes](../../data/cards/TCS-6556.json) (TCS-6556) |
| 14 | 9 | 86 |  | [Depth-first search in NC](../../data/cards/TCS-7172.json) (TCS-7172) |
| 15 | 24 | 86 |  | [Two-dimensional sandpile prediction in NC](../../data/cards/TCS-7259.json) (TCS-7259) |
| 16 | 32 | 82 |  | [Lifting CSP sketching resistance to sublinear streaming resistance](../../data/cards/TCS-0940.json) (TCS-0940) |
| 17 | 38 | 82 |  | [Optimal measurements and near-linear decoding for universal ℓ₂/ℓ₁ sparse recovery](../../data/cards/TCS-0984.json) (TCS-0984) |
| 18 | 25 | 82 |  | [Characterizing separable distances approximable in small streaming space](../../data/cards/TCS-0986.json) (TCS-0986) |
| 19 | 17 | 82 |  | [Fast merging of summaries for symmetric streaming computations](../../data/cards/TCS-0998.json) (TCS-0998) |
| 20 | 51 | 82 |  | [Wait-free exact FIFO queues in Common\(_{2}\)](../../data/cards/TCS-3416.json) (TCS-3416) |
| 21 | 18 | 82 |  | [Common2 membership of FIFO queues](../../data/cards/TCS-7336.json) (TCS-7336) |
| 22 | 54 | 82 |  | [One-pass approximation scheme for random-order streaming matching](../../data/cards/TCS-7400.json) (TCS-7400) |
| 23 | 41 | 78 |  | [LOCAL coloring below square-root degree dependence](../../data/cards/TCS-0524.json) (TCS-0524) |
| 24 | 43 | 78 |  | [Randomized parity sketches versus one-way communication for XOR functions](../../data/cards/TCS-0950.json) (TCS-0950) |
| 25 | 11 | 78 |  | [Optimal one-pass randomized space for LIS length](../../data/cards/TCS-0969.json) (TCS-0969) |
| 26 | 16 | 78 |  | [Full random walks with near-linear streaming space](../../data/cards/TCS-0980.json) (TCS-0980) |
| 27 | 23 | 78 |  | [Local certificate size versus verification radius](../../data/cards/TCS-5797.json) (TCS-5797) |
| 28 | 26 | 78 |  | [Linear-round weighted APSP in CONGEST](../../data/cards/TCS-6080.json) (TCS-6080) |
| 29 | 39 | 78 |  | [Constant-round MIS in the congested clique](../../data/cards/TCS-6501.json) (TCS-6501) |
| 30 | 21 | 78 |  | [Linear-sketch complexity of the nuclear norm](../../data/cards/TCS-7010.json) (TCS-7010) |
| 31 | 15 | 74 |  | [Subquadratic metric TSP cost estimation below factor two](../../data/cards/TCS-0954.json) (TCS-0954) |
| 32 | 20 | 74 |  | [Factor-two graph distances in logarithmically many passes](../../data/cards/TCS-0993.json) (TCS-0993) |
| 33 | 40 | 74 |  | [Constant-pass weighted matching with O(n log n) bits](../../data/cards/TCS-0994.json) (TCS-0994) |
| 34 | 45 | 74 |  | [Classification of robust chemical computation](../../data/cards/TCS-1588.json) (TCS-1588) |
| 35 | 35 | 74 |  | [Work-efficient parallel approximate flow](../../data/cards/TCS-4763.json) (TCS-4763) |
| 36 | 22 | 74 |  | [One-pass semi-streaming depth-first search](../../data/cards/TCS-5795.json) (TCS-5795) |
| 37 | 27 | 74 |  | [Optimal clique-detection rounds in CONGEST](../../data/cards/TCS-6206.json) (TCS-6206) |
| 38 | 42 | 74 |  | [Fractional-edge-cover load for general-message parallel joins](../../data/cards/TCS-6380.json) (TCS-6380) |
| 39 | 36 | 74 |  | [Register space of obstruction-free set agreement](../../data/cards/TCS-7337.json) (TCS-7337) |
| 40 | 29 | 70 |  | [Bipartite maximal matching with polynomial-in-degree volume](../../data/cards/TCS-0519.json) (TCS-0519) |
| 41 | 30 | 70 |  | [Superlinear local certificates for hereditary graph classes](../../data/cards/TCS-2233.json) (TCS-2233) |
| 42 | 33 | 70 |  | [Parallel sampling of planar perfect matchings](../../data/cards/TCS-3075.json) (TCS-3075) |
| 43 | 47 | 70 |  | [Polynomial-in-optimum graph matching in \(\mathrm{AC}^{0}\)](../../data/cards/TCS-3384.json) (TCS-3384) |
| 44 | 52 | 70 |  | [Deterministic linearizable objects for set agreement](../../data/cards/TCS-3792.json) (TCS-3792) |
| 45 | 34 | 70 |  | [LOCAL lower bounds for 2-ruling sets](../../data/cards/TCS-4193.json) (TCS-4193) |
| 46 | 31 | 70 |  | [Linear CONGEST lower bound with logarithmic LOCAL complexity](../../data/cards/TCS-6125.json) (TCS-6125) |
| 47 | 37 | 70 |  | [Polylogarithmic-space streaming Euclidean MST estimation](../../data/cards/TCS-7376.json) (TCS-7376) |
| 48 | 28 | 66 |  | [Maximum independent set in the congested clique](../../data/cards/TCS-0469.json) (TCS-0469) |
| 49 | 48 | 66 |  | [Streaming space for additive \(L_\infty\) estimation](../../data/cards/TCS-0985.json) (TCS-0985) |
| 50 | 50 | 66 |  | [Breaking the quadratic color bound for bounded outdegree](../../data/cards/TCS-2470.json) (TCS-2470) |
| 51 | 44 | 66 |  | [Polynomial-state protocols for Presburger arithmetic](../../data/cards/TCS-3381.json) (TCS-3381) |
| 52 | 53 | 66 |  | [Subpolynomial detection of two-connected patterns](../../data/cards/TCS-4274.json) (TCS-4274) |
| 53 | 49 | 62 |  | [Query complexity of the graph degree distribution](../../data/cards/TCS-0834.json) (TCS-0834) |
| 54 | 46 | 62 |  | [Two-stage group testing with arithmetic progressions](../../data/cards/TCS-0849.json) (TCS-0849) |

### Optimization and numerical computation

Favor universal optimization and discrepancy barriers, exact feasibility, and dimension dependence. Fundamental geometric obstructions outrank refinements of one relaxation.

| Rank | Previous | Score | Focus | Problem |
| ---: | ---: | ---: | :---: | --- |
| 1 | 1 | 100 | yes | [Strongly polynomial linear programming](../../data/cards/TCS-0008.json) (TCS-0008) |
| 2 | 7 | 96 | yes | [Komlós conjecture](../../data/cards/TCS-7314.json) (TCS-7314) |
| 3 | 4 | 96 | yes | [Nearly linear-time solution of general sparse linear systems](../../data/cards/TCS-6585.json) (TCS-6585) |
| 4 | 2 | 94 | yes | [Exact semidefinite feasibility in polynomial time](../../data/cards/TCS-6574.json) (TCS-6574) |
| 5 | 10 | 92 | yes | [Single-exponential dependence on dimension for integer programming](../../data/cards/TCS-7264.json) (TCS-7264) |
| 6 | 6 | 94 |  | [Polynomial-time simplex pivot rule](../../data/cards/TCS-6572.json) (TCS-6572) |
| 7 | 9 | 92 |  | [Beck–Fiala conjecture](../../data/cards/TCS-7315.json) (TCS-7315) |
| 8 | 3 | 88 |  | [Conforti–Cornuéjols conjecture](../../data/cards/TCS-7227.json) (TCS-7227) |
| 9 | 8 | 88 |  | [P-matrix linear complementarity in polynomial time](../../data/cards/TCS-7231.json) (TCS-7231) |
| 10 | 26 | 88 |  | [Truly linear-time Laplacian solving](../../data/cards/TCS-7397.json) (TCS-7397) |
| 11 | 27 | 88 |  | [Polynomial-time integer programming with bounded subdeterminants](../../data/cards/TCS-7438.json) (TCS-7438) |
| 12 | 28 | 88 |  | [Linear bound in the flatness theorem](../../data/cards/TCS-7439.json) (TCS-7439) |
| 13 | 17 | 84 |  | [Limited-memory convex optimization](../../data/cards/TCS-0724.json) (TCS-0724) |
| 14 | 5 | 84 |  | [Smale’s seventh problem](../../data/cards/TCS-6578.json) (TCS-6578) |
| 15 | 12 | 84 |  | [Woodall’s conjecture](../../data/cards/TCS-7226.json) (TCS-7226) |
| 16 | 11 | 84 |  | [Superpolynomial semidefinite extension complexity of perfect matching](../../data/cards/TCS-7283.json) (TCS-7283) |
| 17 | 25 | 84 |  | [Nearly quadratic oracle complexity for convex-body volume](../../data/cards/TCS-7389.json) (TCS-7389) |
| 18 | 20 | 80 |  | [Polynomial-time linear convergence for geodesically convex optimization](../../data/cards/TCS-0722.json) (TCS-0722) |
| 19 | 19 | 80 |  | [Deterministic near-linear-query approximation schemes for matroid intersection](../../data/cards/TCS-5330.json) (TCS-5330) |
| 20 | 16 | 80 |  | [Superlinear randomized query lower bounds for submodular minimization](../../data/cards/TCS-6483.json) (TCS-6483) |
| 21 | 15 | 80 |  | [Input-sparsity relative spectral low-rank approximation](../../data/cards/TCS-7007.json) (TCS-7007) |
| 22 | 32 | 80 |  | [Flowing conjecture](../../data/cards/TCS-7443.json) (TCS-7443) |
| 23 | 33 | 80 |  | [Explicit matroids with exponentially large extended formulations](../../data/cards/TCS-7444.json) (TCS-7444) |
| 24 | 21 | 76 |  | [Gap-entropy conjecture](../../data/cards/TCS-0687.json) (TCS-0687) |
| 25 | 14 | 76 |  | [Constant-factor entrywise \(\ell_1\) rank-\(k\) approximation with variable \(k\)](../../data/cards/TCS-7298.json) (TCS-7298) |
| 26 | 30 | 76 |  | [Oertel’s mixed-integer centerpoint conjecture](../../data/cards/TCS-7441.json) (TCS-7441) |
| 27 | 31 | 76 |  | [Seymour’s dyadic packing conjecture](../../data/cards/TCS-7442.json) (TCS-7442) |
| 28 | 13 | 72 |  | [Log-squared query complexity of fixed-dimensional Tarski fixed points](../../data/cards/TCS-0491.json) (TCS-0491) |
| 29 | 24 | 72 |  | [First-order convergence to local minimax optima](../../data/cards/TCS-0673.json) (TCS-0673) |
| 30 | 18 | 72 |  | [Smooth convex optimization with different domain and smoothness norms](../../data/cards/TCS-0728.json) (TCS-0728) |
| 31 | 34 | 72 |  | [Polynomial-size constant-gap relaxation for minimum knapsack](../../data/cards/TCS-7445.json) (TCS-7445) |
| 32 | 35 | 72 |  | [Fully polynomial-size LP relaxation scheme for maximum knapsack](../../data/cards/TCS-7446.json) (TCS-7446) |
| 33 | 22 | 68 |  | [Second-order cone lift dimension of semialgebraic convex hulls](../../data/cards/TCS-0725.json) (TCS-0725) |
| 34 | 23 | 68 |  | [Deterministic competitive ratio for matching with delays](../../data/cards/TCS-0914.json) (TCS-0914) |
| 35 | 29 | 68 |  | [Polynomial-size split closures in fixed dimension](../../data/cards/TCS-7440.json) (TCS-7440) |

### Geometry, topology and metric spaces

Favor broad isoperimetric and embedding principles, algorithmic topology, and clean extremal geometric barriers. Representation costs follow general structural questions.

| Rank | Previous | Score | Focus | Problem |
| ---: | ---: | ---: | :---: | --- |
| 1 | 1 | 98 | yes | [Kannan–Lovász–Simonovits conjecture](../../data/cards/TCS-6523.json) (TCS-6523) |
| 2 | 2 | 94 | yes | [Gupta–Newman–Rabinovich–Sinclair conjecture](../../data/cards/TCS-6525.json) (TCS-6525) |
| 3 | 3 | 94 | yes | [Unknot recognition in polynomial time](../../data/cards/TCS-6528.json) (TCS-6528) |
| 4 | 5 | 90 | yes | [Planar k-set extremal function](../../data/cards/TCS-0318.json) (TCS-0318) |
| 5 | 4 | 94 | yes | [Polynomial Hirsch conjecture](../../data/cards/TCS-6573.json) (TCS-6573) |
| 6 | 6 | 90 |  | [Lang–Plaut problem](../../data/cards/TCS-6524.json) (TCS-6524) |
| 7 | 8 | 90 |  | [Optimal size of weak \(\varepsilon\)-nets for convex ranges](../../data/cards/TCS-6526.json) (TCS-6526) |
| 8 | 7 | 90 |  | [Decidability of PL four-sphere recognition](../../data/cards/TCS-7242.json) (TCS-7242) |
| 9 | 16 | 86 |  | [Euclidean minimum spanning tree complexity](../../data/cards/TCS-0403.json) (TCS-0403) |
| 10 | 9 | 86 |  | [Dürer’s conjecture](../../data/cards/TCS-0406.json) (TCS-0406) |
| 11 | 17 | 86 |  | [Exact planar Euclidean matching](../../data/cards/TCS-0408.json) (TCS-0408) |
| 12 | 40 | 86 |  | [Decidability of contractibility for finite two-dimensional complexes](../../data/cards/TCS-6199.json) (TCS-6199) |
| 13 | 10 | 86 |  | [Constant-distortion Steiner point removal](../../data/cards/TCS-6527.json) (TCS-6527) |
| 14 | 12 | 86 |  | [Polynomial-time recognition of the 3-sphere](../../data/cards/TCS-7292.json) (TCS-7292) |
| 15 | 33 | 82 |  | [Linear-size universal point sets for planar graphs](../../data/cards/TCS-0377.json) (TCS-0377) |
| 16 | 18 | 82 |  | [Flip graph connectivity in three dimensions](../../data/cards/TCS-0381.json) (TCS-0381) |
| 17 | 19 | 82 |  | [NP certificates for homeomorphism of three-manifolds](../../data/cards/TCS-0427.json) (TCS-0427) |
| 18 | 14 | 82 |  | [Optimal input-sparsity subspace embeddings](../../data/cards/TCS-7006.json) (TCS-7006) |
| 19 | 11 | 82 |  | [Klee’s measure problem](../../data/cards/TCS-7184.json) (TCS-7184) |
| 20 | 13 | 78 |  | [General unfolding of nonconvex polyhedra](../../data/cards/TCS-0382.json) (TCS-0382) |
| 21 | 22 | 78 |  | [Output-sensitive convex hull complexity](../../data/cards/TCS-0410.json) (TCS-0410) |
| 22 | 23 | 78 |  | [Earth mover distance sketching complexity](../../data/cards/TCS-0973.json) (TCS-0973) |
| 23 | 28 | 78 |  | [Efficient constant-distortion cut-cone approximation](../../data/cards/TCS-6880.json) (TCS-6880) |
| 24 | 15 | 78 |  | [Simultaneous embedding with fixed edges for two graphs](../../data/cards/TCS-7182.json) (TCS-7182) |
| 25 | 41 | 78 |  | [Truly subquadratic exact Euclidean bipartite matching](../../data/cards/TCS-7377.json) (TCS-7377) |
| 26 | 31 | 74 |  | [Polygon visibility graph recognition](../../data/cards/TCS-0416.json) (TCS-0416) |
| 27 | 25 | 74 |  | [Near-quadratic Voronoi complexity of lines in three dimensions](../../data/cards/TCS-0417.json) (TCS-0417) |
| 28 | 26 | 74 |  | [coNP certificates for three-manifold homeomorphism](../../data/cards/TCS-0419.json) (TCS-0419) |
| 29 | 34 | 74 |  | [Polynomial flip-distance bounds for three-manifold triangulations](../../data/cards/TCS-0432.json) (TCS-0432) |
| 30 | 37 | 74 |  | [Fast Johnson–Lindenstrauss transforms for sparse vectors](../../data/cards/TCS-0970.json) (TCS-0970) |
| 31 | 36 | 70 |  | [Efficient average-distortion embeddings of polyhedral norms](../../data/cards/TCS-0340.json) (TCS-0340) |
| 32 | 21 | 70 |  | [Exact planar Euclidean maximum TSP](../../data/cards/TCS-0398.json) (TCS-0398) |
| 33 | 27 | 70 |  | [Point location in three-dimensional subdivisions](../../data/cards/TCS-0411.json) (TCS-0411) |
| 34 | 35 | 70 |  | [NP recognition of closed hyperbolic three-manifolds](../../data/cards/TCS-0428.json) (TCS-0428) |
| 35 | 32 | 70 |  | [Constant-factor streaming approximation of planar Earth Mover Distance](../../data/cards/TCS-0990.json) (TCS-0990) |
| 36 | 39 | 70 |  | [Half-snowflake embeddings into Wasserstein p-space](../../data/cards/TCS-4454.json) (TCS-4454) |
| 37 | 20 | 70 |  | [Minimum-weight triangulation in NP](../../data/cards/TCS-7189.json) (TCS-7189) |
| 38 | 24 | 66 |  | [Counting simple polygonalizations](../../data/cards/TCS-0327.json) (TCS-0327) |
| 39 | 38 | 66 |  | [Minimum-Link Path in 2D](../../data/cards/TCS-0409.json) (TCS-0409) |
| 40 | 29 | 66 |  | [NP-hardness of three-manifold homeomorphism](../../data/cards/TCS-0430.json) (TCS-0430) |
| 41 | 42 | 66 |  | [Optimal space–query tradeoff for approximate Voronoi diagrams](../../data/cards/TCS-7403.json) (TCS-7403) |
| 42 | 30 | 62 |  | [Lower-left anchored rectangle packing constant](../../data/cards/TCS-3059.json) (TCS-3059) |

### Learning theory

Favor the relation between information and computation: compression, noise, expressive concept classes, statistical structure and cryptographic hardness. General learnability principles precede specialized models.

| Rank | Previous | Score | Focus | Problem |
| ---: | ---: | ---: | :---: | --- |
| 1 | 1 | 96 | yes | [Linear-size sample compression](../../data/cards/TCS-6541.json) (TCS-6541) |
| 2 | 2 | 96 | yes | [Learning parity with noise in polynomial time](../../data/cards/TCS-6542.json) (TCS-6542) |
| 3 | 4 | 94 | yes | [Polynomial-time distribution-free PAC learning of DNF](../../data/cards/TCS-5358.json) (TCS-5358) |
| 4 | 5 | 90 | yes | [Efficient learning of well-separated Gaussian mixtures](../../data/cards/TCS-3391.json) (TCS-3391) |
| 5 | 8 | 90 | yes | [One-way functions from hardness of learning P/poly](../../data/cards/TCS-5090.json) (TCS-5090) |
| 6 | 3 | 90 |  | [Learning Boolean juntas from uniform random examples](../../data/cards/TCS-6543.json) (TCS-6543) |
| 7 | 10 | 90 |  | [Learning decision trees from uniform random examples in polynomial time](../../data/cards/TCS-7294.json) (TCS-7294) |
| 8 | 19 | 86 |  | [NP-hardness of improper learning of \(\mathrm{P}/\mathrm{poly}\)](../../data/cards/TCS-1573.json) (TCS-1573) |
| 9 | 15 | 86 |  | [Time complexity of Gaussian agnostic halfspace learning](../../data/cards/TCS-4592.json) (TCS-4592) |
| 10 | 6 | 86 |  | [Fully polynomial learning of halfspace intersections under Gaussian and uniform inputs](../../data/cards/TCS-5088.json) (TCS-5088) |
| 11 | 7 | 86 |  | [Distribution-free learning of two margin halfspaces](../../data/cards/TCS-6544.json) (TCS-6544) |
| 12 | 12 | 86 |  | [Distribution-free improper learning of two unrestricted halfspaces](../../data/cards/TCS-7293.json) (TCS-7293) |
| 13 | 14 | 82 |  | [Optimal multiclass regret versus Littlestone dimension](../../data/cards/TCS-2336.json) (TCS-2336) |
| 14 | 25 | 82 |  | [Littlestone-dimension regret bounds for unrestricted classes](../../data/cards/TCS-5031.json) (TCS-5031) |
| 15 | 11 | 82 |  | [Sample-optimal Gaussian graphical model learning in polynomial time](../../data/cards/TCS-5119.json) (TCS-5119) |
| 16 | 9 | 82 |  | [Nontrivial agnostic membership-query learning of \(\mathrm{ACC}^{0}\)](../../data/cards/TCS-5434.json) (TCS-5434) |
| 17 | 23 | 82 |  | [Linear conditional-information bounds for VC learning](../../data/cards/TCS-5847.json) (TCS-5847) |
| 18 | 13 | 82 |  | [PAC learning of finite automata under the uniform distribution](../../data/cards/TCS-5902.json) (TCS-5902) |
| 19 | 37 | 82 |  | [Characterizing agnostic online reinforcement learning](../../data/cards/TCS-7447.json) (TCS-7447) |
| 20 | 32 | 78 |  | [Dimension complexity of distribution-independent SQ learning](../../data/cards/TCS-0664.json) (TCS-0664) |
| 21 | 18 | 78 |  | [Proper decision-tree learning in polynomial time](../../data/cards/TCS-0677.json) (TCS-0677) |
| 22 | 26 | 78 |  | [Recursive teaching dimension conjecture](../../data/cards/TCS-2339.json) (TCS-2339) |
| 23 | 16 | 78 |  | [Memory–sample tradeoffs for noisy parity learning](../../data/cards/TCS-3117.json) (TCS-3117) |
| 24 | 21 | 78 |  | [Proper unlabeled compression of ample classes](../../data/cards/TCS-3787.json) (TCS-3787) |
| 25 | 22 | 78 |  | [Multiclass sample compression from binary compression](../../data/cards/TCS-4792.json) (TCS-4792) |
| 26 | 20 | 78 |  | [Polynomial-time robust spectral estimation](../../data/cards/TCS-5087.json) (TCS-5087) |
| 27 | 30 | 74 |  | [Local regularization for multiclass learning](../../data/cards/TCS-0670.json) (TCS-0670) |
| 28 | 29 | 74 |  | [Compression overhead for adversarial robustness](../../data/cards/TCS-1539.json) (TCS-1539) |
| 29 | 17 | 74 |  | [Learning PH/poly from learning NP/poly](../../data/cards/TCS-3177.json) (TCS-3177) |
| 30 | 24 | 74 |  | [Non-clashing teaching dimension versus VC dimension](../../data/cards/TCS-3689.json) (TCS-3689) |
| 31 | 36 | 74 |  | [Learning speedups from random examples](../../data/cards/TCS-4186.json) (TCS-4186) |
| 32 | 31 | 70 |  | [Agnostic direct-sum learning rates](../../data/cards/TCS-0671.json) (TCS-0671) |
| 33 | 33 | 70 |  | [Monotone empirical risk minimization](../../data/cards/TCS-0682.json) (TCS-0682) |
| 34 | 28 | 70 |  | [Improper compression for Gaussian-mixture reconstruction](../../data/cards/TCS-0683.json) (TCS-0683) |
| 35 | 27 | 70 |  | [Statistical-query complexity of sparse halfspaces](../../data/cards/TCS-0694.json) (TCS-0694) |
| 36 | 35 | 70 |  | [Uniform convergence under Dobrushin dependence](../../data/cards/TCS-3691.json) (TCS-3691) |
| 37 | 38 | 66 |  | [Polynomial-time proper learning of Poisson binomial distributions](../../data/cards/TCS-7448.json) (TCS-7448) |
| 38 | 39 | 66 |  | [Longest-example memory for automatic learning](../../data/cards/TCS-7449.json) (TCS-7449) |
| 39 | 40 | 66 |  | [Automatic iterative learning versus hypothesis-sized memory](../../data/cards/TCS-7450.json) (TCS-7450) |
| 40 | 34 | 62 |  | [Identifiable elicitation complexity](../../data/cards/TCS-0689.json) (TCS-0689) |

### Cryptography

Favor minimal assumptions for central cryptographic capabilities and information-theoretic limits. Keep secret sharing beside computational assumptions; place specialized efficiency improvements after broad primitive separations.

| Rank | Previous | Score | Focus | Problem |
| ---: | ---: | ---: | :---: | --- |
| 1 | 2 | 98 | yes | [One-way functions from \(\mathrm{P} \ne  \mathrm{NP}\)](../../data/cards/TCS-0022.json) (TCS-0022) |
| 2 | 1 | 96 | yes | [Public-key encryption from one-way functions](../../data/cards/TCS-6545.json) (TCS-6545) |
| 3 | 3 | 94 | yes | [Circuit obfuscation from polynomial-hard LWE](../../data/cards/TCS-6550.json) (TCS-6550) |
| 4 | 4 | 94 | yes | [Unleveled fully homomorphic encryption from LWE alone](../../data/cards/TCS-6551.json) (TCS-6551) |
| 5 | 5 | 92 | yes | [Sub-square-root share-size exponents in perfect secret sharing](../../data/cards/TCS-0465.json) (TCS-0465) |
| 6 | 6 | 98 |  | [Existence of one-way functions](../../data/cards/TCS-7167.json) (TCS-7167) |
| 7 | 7 | 94 |  | [Existence of public-key encryption](../../data/cards/TCS-7168.json) (TCS-7168) |
| 8 | 9 | 92 |  | [Oblivious transfer from public-key encryption](../../data/cards/TCS-6549.json) (TCS-6549) |
| 9 | 8 | 92 |  | [Key agreement from one-way functions](../../data/cards/TCS-7229.json) (TCS-7229) |
| 10 | 11 | 90 |  | [One-way permutations from one-way functions](../../data/cards/TCS-6546.json) (TCS-6546) |
| 11 | 10 | 90 |  | [Collision-resistant hashing from one-way functions](../../data/cards/TCS-6547.json) (TCS-6547) |
| 12 | 13 | 90 |  | [Noninteractive zero knowledge from one-way functions](../../data/cards/TCS-6552.json) (TCS-6552) |
| 13 | 20 | 90 |  | [Fully homomorphic encryption from public-key encryption](../../data/cards/TCS-7277.json) (TCS-7277) |
| 14 | 38 | 90 |  | [Succinct noninteractive arguments for NP from LWE alone](../../data/cards/TCS-7458.json) (TCS-7458) |
| 15 | 12 | 86 |  | [Chosen-ciphertext security from ordinary public-key encryption](../../data/cards/TCS-6548.json) (TCS-6548) |
| 16 | 15 | 86 |  | [One-way functions from errorless average-case NP hardness](../../data/cards/TCS-6953.json) (TCS-6953) |
| 17 | 17 | 86 |  | [Average-case RSA inversion versus factoring for exponent 65537](../../data/cards/TCS-7276.json) (TCS-7276) |
| 18 | 16 | 86 |  | [Public-key quantum money from LWE alone](../../data/cards/TCS-7359.json) (TCS-7359) |
| 19 | 31 | 86 |  | [Witness encryption from plain LWE](../../data/cards/TCS-7451.json) (TCS-7451) |
| 20 | 33 | 86 |  | [General functional encryption from plain LWE](../../data/cards/TCS-7453.json) (TCS-7453) |
| 21 | 26 | 82 |  | [Pseudorandom functions from worst-case hardness of learning](../../data/cards/TCS-5793.json) (TCS-5793) |
| 22 | 22 | 82 |  | [Low-noise LPN hardness from Nearest Codeword hardness](../../data/cards/TCS-6454.json) (TCS-6454) |
| 23 | 14 | 82 |  | [Unbounded fully homomorphic encryption from polynomial-factor GapSVP](../../data/cards/TCS-6871.json) (TCS-6871) |
| 24 | 19 | 82 |  | [Noninteractive SZK versus SZK](../../data/cards/TCS-7272.json) (TCS-7272) |
| 25 | 23 | 82 |  | [One-way functions in \(\mathrm{NC}^{0}\) from one-way functions](../../data/cards/TCS-7274.json) (TCS-7274) |
| 26 | 35 | 82 |  | [Verifiable random functions from one-way functions alone](../../data/cards/TCS-7455.json) (TCS-7455) |
| 27 | 40 | 82 |  | [Blind signatures from one-way functions alone](../../data/cards/TCS-7460.json) (TCS-7460) |
| 28 | 21 | 78 |  | [PZK versus SZK](../../data/cards/TCS-7225.json) (TCS-7225) |
| 29 | 24 | 78 |  | [Identity-based encryption from arbitrary public-key encryption](../../data/cards/TCS-7278.json) (TCS-7278) |
| 30 | 32 | 78 |  | [Dual pseudorandom functions from arbitrary one-way functions](../../data/cards/TCS-7452.json) (TCS-7452) |
| 31 | 36 | 78 |  | [Compact general-circuit homomorphic secret sharing from DDH](../../data/cards/TCS-7456.json) (TCS-7456) |
| 32 | 37 | 78 |  | [Constant-round concurrent zero knowledge from LWE alone](../../data/cards/TCS-7457.json) (TCS-7457) |
| 33 | 39 | 78 |  | [Doubly efficient PIR with quasilinear server preprocessing](../../data/cards/TCS-7459.json) (TCS-7459) |
| 34 | 29 | 74 |  | [Polynomial-time computationally sound verification of \(\#\mathrm{SAT}\)](../../data/cards/TCS-1138.json) (TCS-1138) |
| 35 | 25 | 74 |  | [Exponentially hard weak versus strong one-way functions](../../data/cards/TCS-3025.json) (TCS-3025) |
| 36 | 18 | 74 |  | [Linear-seed pseudorandom generators from one-way functions](../../data/cards/TCS-6692.json) (TCS-6692) |
| 37 | 34 | 74 |  | [Efficient split-state non-malleable codes approaching capacity](../../data/cards/TCS-7454.json) (TCS-7454) |
| 38 | 27 | 70 |  | [Subpolynomial-key perfectly secure three-server DPFs](../../data/cards/TCS-2732.json) (TCS-2732) |
| 39 | 30 | 70 |  | [Unconditional zero knowledge for gap circuit complexity](../../data/cards/TCS-4754.json) (TCS-4754) |
| 40 | 28 | 70 |  | [Sublinear communication for perfectly secure two-party computation](../../data/cards/TCS-5013.json) (TCS-5013) |

### Quantum computation and information

Favor quantum computational power, local Hamiltonian complexity, entanglement and verification. Keep coding and capacity prominent without letting nearby QMA variants crowd out distinct phenomena.

| Rank | Previous | Score | Focus | Problem |
| ---: | ---: | ---: | :---: | --- |
| 1 | 1 | 98 | yes | [Quantum PCP conjecture with classical reductions](../../data/cards/TCS-6446.json) (TCS-6446) |
| 2 | 2 | 98 | yes | [BPP versus BQP](../../data/cards/TCS-0036.json) (TCS-0036) |
| 3 | 3 | 96 | yes | [Area law for gapped two-dimensional Hamiltonians](../../data/cards/TCS-6516.json) (TCS-6516) |
| 4 | 4 | 96 | yes | [Information-theoretic classical verification of quantum computation](../../data/cards/TCS-6580.json) (TCS-6580) |
| 5 | 5 | 94 | yes | [NPT bound entanglement](../../data/cards/TCS-6518.json) (TCS-6518) |
| 6 | 6 | 94 |  | [Asymptotically good quantum locally testable stabilizer codes](../../data/cards/TCS-6515.json) (TCS-6515) |
| 7 | 7 | 94 |  | [Passive quantum memory in three dimensions](../../data/cards/TCS-6517.json) (TCS-6517) |
| 8 | 9 | 92 |  | [NP outside BQP](../../data/cards/TCS-0037.json) (TCS-0037) |
| 9 | 10 | 92 |  | [QMA versus QCMA](../../data/cards/TCS-6448.json) (TCS-6448) |
| 10 | 8 | 92 |  | [Quantum capacity of the qubit depolarizing channel](../../data/cards/TCS-6519.json) (TCS-6519) |
| 11 | 11 | 92 |  | [Computability of quantum channel capacity](../../data/cards/TCS-6520.json) (TCS-6520) |
| 12 | 19 | 88 |  | [QMA versus \(\mathrm{QMA}(2)\)](../../data/cards/TCS-2229.json) (TCS-2229) |
| 13 | 20 | 88 |  | [Quantum entropy inequalities beyond strong subadditivity](../../data/cards/TCS-4615.json) (TCS-4615) |
| 14 | 52 | 88 |  | [Exponential repetition of two-player entangled games](../../data/cards/TCS-5077.json) (TCS-5077) |
| 15 | 16 | 88 |  | [Dihedral hidden subgroup problem in BQP](../../data/cards/TCS-6521.json) (TCS-6521) |
| 16 | 17 | 88 |  | [Graph isomorphism in BQP](../../data/cards/TCS-6522.json) (TCS-6522) |
| 17 | 21 | 88 |  | [Bell nonlocality from finitely many copies of every entangled state](../../data/cards/TCS-7308.json) (TCS-7308) |
| 18 | 23 | 84 |  | [Maximum randomized-versus-quantum gap for total functions](../../data/cards/TCS-0029.json) (TCS-0029) |
| 19 | 12 | 84 |  | [Quantum query-to-communication lifting](../../data/cards/TCS-3709.json) (TCS-3709) |
| 20 | 25 | 84 |  | [Locality-preserving quantum gap amplification](../../data/cards/TCS-4734.json) (TCS-4734) |
| 21 | 13 | 84 |  | [QMA versus \(\mathrm{QMA}_1\) over Clifford+T](../../data/cards/TCS-4737.json) (TCS-4737) |
| 22 | 14 | 84 |  | [Quantum–classical communication gaps for total functions](../../data/cards/TCS-4952.json) (TCS-4952) |
| 23 | 31 | 84 |  | [Quantum versus classical nonuniform advice](../../data/cards/TCS-6449.json) (TCS-6449) |
| 24 | 18 | 84 |  | [Classical hardness of approximate Boson Sampling](../../data/cards/TCS-6933.json) (TCS-6933) |
| 25 | 32 | 80 |  | [Quantum query complexity versus bounded approximate degree](../../data/cards/TCS-0033.json) (TCS-0033) |
| 26 | 24 | 80 |  | [One-way state generators versus EFI pairs](../../data/cards/TCS-1961.json) (TCS-1961) |
| 27 | 27 | 80 |  | [Remote state preparation from quantum-secure one-way functions](../../data/cards/TCS-2408.json) (TCS-2408) |
| 28 | 51 | 80 |  | [Simulation or postselection universality for algebraic two-qubit interactions](../../data/cards/TCS-4457.json) (TCS-4457) |
| 29 | 22 | 80 |  | [\(\mathrm{QMA}(2)\) versus NEXP](../../data/cards/TCS-4753.json) (TCS-4753) |
| 30 | 36 | 80 |  | [Polynomially many EPR pairs for bounded-error Boolean communication](../../data/cards/TCS-4991.json) (TCS-4991) |
| 31 | 15 | 80 |  | [Entanglement without distillable secret key](../../data/cards/TCS-6459.json) (TCS-6459) |
| 32 | 45 | 76 |  | [Black-box unitary synthesis](../../data/cards/TCS-0027.json) (TCS-0027) |
| 33 | 49 | 76 |  | [Quantum games PCP with efficient honest provers and short messages](../../data/cards/TCS-1324.json) (TCS-1324) |
| 34 | 50 | 76 |  | [Completeness and soundness amplification in StoqMA](../../data/cards/TCS-3275.json) (TCS-3275) |
| 35 | 38 | 76 |  | [Succinct entangled proofs with efficient provers](../../data/cards/TCS-4715.json) (TCS-4715) |
| 36 | 28 | 76 |  | [Efficient approximation of the optimal dihedral measurement](../../data/cards/TCS-4811.json) (TCS-4811) |
| 37 | 30 | 76 |  | [A finite quantum gate set with decision power strictly between P and BQP](../../data/cards/TCS-4927.json) (TCS-4927) |
| 38 | 37 | 76 |  | [Universal quantum stability of seeded extractors with output-linear error loss](../../data/cards/TCS-5202.json) (TCS-5202) |
| 39 | 35 | 72 |  | [\(\mathrm{QMA}(2)\) versus \(\mathrm{BQEXP}\)](../../data/cards/TCS-0861.json) (TCS-0861) |
| 40 | 44 | 72 |  | [Constant-round quantum refereed games versus \(\mathrm{PSPACE}\)](../../data/cards/TCS-0862.json) (TCS-0862) |
| 41 | 34 | 72 |  | [Optimal quantum query complexity of uniformity testing](../../data/cards/TCS-1882.json) (TCS-1882) |
| 42 | 29 | 72 |  | [Parity versus \(\mathrm{AC}^{0}\) with shallow quantum preprocessing](../../data/cards/TCS-4894.json) (TCS-4894) |
| 43 | 33 | 72 |  | [Limiting optimized QAOA energy in the SK model](../../data/cards/TCS-5021.json) (TCS-5021) |
| 44 | 40 | 72 |  | [Strong quantum IOPs with polynomial communication](../../data/cards/TCS-6447.json) (TCS-6447) |
| 45 | 26 | 72 |  | [Bosonic quantum computation in PP](../../data/cards/TCS-6481.json) (TCS-6481) |
| 46 | 47 | 68 |  | [Oracle separation of BQP from efficient-prover interactive proofs](../../data/cards/TCS-0030.json) (TCS-0030) |
| 47 | 41 | 68 |  | [Oracle separation of BQP from IP](../../data/cards/TCS-0031.json) (TCS-0031) |
| 48 | 42 | 68 |  | [Quantum query–space tradeoffs for collisions and distinctness](../../data/cards/TCS-0034.json) (TCS-0034) |
| 49 | 46 | 68 |  | [Complement of quantum approximate counting in \(\mathrm{QMA}(2)\)](../../data/cards/TCS-0860.json) (TCS-0860) |
| 50 | 48 | 68 |  | [Exact quantum fanout in constant depth with unrestricted circuit size](../../data/cards/TCS-1259.json) (TCS-1259) |
| 51 | 39 | 68 |  | [Zero-free quantum partition functions with a tensor-product perturbation](../../data/cards/TCS-2707.json) (TCS-2707) |
| 52 | 43 | 68 |  | [Sequential randomness certification against non-signaling adversaries](../../data/cards/TCS-4238.json) (TCS-4238) |

### Computability and algorithmic information theory

Favor structural laws of computation and explicit frontiers of mathematical knowledge. BB(6) supplies a concrete target alongside degree-theoretic structure; broad randomness and computable-analysis questions precede specialized definability fragments.

| Rank | Previous | Score | Focus | Problem |
| ---: | ---: | ---: | :---: | --- |
| 1 | 1 | 96 | yes | [Martin’s conjecture](../../data/cards/TCS-6646.json) (TCS-6646) |
| 2 | 4 | 92 | yes | [Busy Beaver \(\mathrm{BB}(6)\)](../../data/cards/TCS-6685.json) (TCS-6685) |
| 3 | 3 | 96 |  | [Rigidity of the Turing degrees](../../data/cards/TCS-6647.json) (TCS-6647) |
| 4 | 2 | 92 |  | [Kolmogorov–Loveland randomness versus Martin-Löf randomness](../../data/cards/TCS-6648.json) (TCS-6648) |
| 5 | 8 | 88 |  | [Computability of the Mandelbrot set](../../data/cards/TCS-6105.json) (TCS-6105) |
| 6 | 5 | 88 |  | [Reversal of Hindman’s theorem to the \(\omega\)-jump](../../data/cards/TCS-6649.json) (TCS-6649) |
| 7 | 6 | 88 |  | [Universality of Turing equivalence](../../data/cards/TCS-6679.json) (TCS-6679) |
| 8 | 9 | 84 |  | [NP-hardness of conditional polynomial-time pKt](../../data/cards/TCS-2202.json) (TCS-2202) |
| 9 | 10 | 84 |  | [Unconditional coding theorem for randomized Kolmogorov complexity](../../data/cards/TCS-5010.json) (TCS-5010) |
| 10 | 7 | 84 |  | [Mortality of \(2\times 2\) integer matrix semigroups](../../data/cards/TCS-7193.json) (TCS-7193) |
| 11 | 19 | 84 |  | [Rigidity of the computably enumerable degrees](../../data/cards/TCS-7461.json) (TCS-7461) |
| 12 | 23 | 84 |  | [Biinterpretability of computably enumerable degrees with arithmetic](../../data/cards/TCS-7465.json) (TCS-7465) |
| 13 | 15 | 80 |  | [An algorithmic Ahlswede–Körner lemma](../../data/cards/TCS-0238.json) (TCS-0238) |
| 14 | 12 | 80 |  | [Shannon feasibility from algorithmic network coding](../../data/cards/TCS-0247.json) (TCS-0247) |
| 15 | 11 | 80 |  | [Scaling joint Kolmogorov-complexity profiles](../../data/cards/TCS-0250.json) (TCS-0250) |
| 16 | 21 | 80 |  | [Low-\(n\) Boolean algebra conjecture](../../data/cards/TCS-7463.json) (TCS-7463) |
| 17 | 28 | 80 |  | [Universality of recursive isomorphism on binary sequences](../../data/cards/TCS-7470.json) (TCS-7470) |
| 18 | 16 | 76 |  | [Algorithmic networks characterized by cut inequalities](../../data/cards/TCS-0254.json) (TCS-0254) |
| 19 | 20 | 76 |  | [Deciding the two-quantifier theory of c.e. degrees](../../data/cards/TCS-7462.json) (TCS-7462) |
| 20 | 24 | 76 |  | [Deciding finite-lattice embeddability into c.e. degrees](../../data/cards/TCS-7466.json) (TCS-7466) |
| 21 | 29 | 76 |  | [Topological computable categoricity of infinite Polish spaces](../../data/cards/TCS-7471.json) (TCS-7471) |
| 22 | 30 | 76 |  | [Degree of topological categoricity of Baire space](../../data/cards/TCS-7472.json) (TCS-7472) |
| 23 | 14 | 72 |  | [Strong extractors for infinite sequences](../../data/cards/TCS-0287.json) (TCS-0287) |
| 24 | 13 | 72 |  | [Existence of strings without simple optimal hypotheses](../../data/cards/TCS-4185.json) (TCS-4185) |
| 25 | 22 | 72 |  | [Low-two supersets lattice conjecture](../../data/cards/TCS-7464.json) (TCS-7464) |
| 26 | 26 | 72 |  | [Classifying sets with countable infinite-time decision complexity](../../data/cards/TCS-7468.json) (TCS-7468) |
| 27 | 17 | 68 |  | [Communication rate for secret-key agreement at fixed Hamming distance](../../data/cards/TCS-0240.json) (TCS-0240) |
| 28 | 18 | 68 |  | [Random-oracle invariance of fully extractable common information](../../data/cards/TCS-0279.json) (TCS-0279) |
| 29 | 25 | 68 |  | [Two-quantifier theory of the local enumeration degrees](../../data/cards/TCS-7467.json) (TCS-7467) |
| 30 | 27 | 68 |  | [Admissibility of gaps in infinite-time decision times](../../data/cards/TCS-7469.json) (TCS-7469) |

### Proof complexity

Favor limits on general proof systems and the existence of a universally efficient proof formalism. Put central lower bounds and arithmetic strength before refinements of a single proof resource.

| Rank | Previous | Score | Focus | Problem |
| ---: | ---: | ---: | :---: | --- |
| 1 | 1 | 98 | yes | [Superpolynomial Extended Frege lower bounds](../../data/cards/TCS-6601.json) (TCS-6601) |
| 2 | 5 | 94 | yes | [Existence of p-optimal proof systems](../../data/cards/TCS-7162.json) (TCS-7162) |
| 3 | 4 | 98 |  | [Superpolynomial lower bounds for unrestricted Frege proofs](../../data/cards/TCS-0025.json) (TCS-0025) |
| 4 | 2 | 94 |  | [Frege versus Extended Frege](../../data/cards/TCS-6663.json) (TCS-6663) |
| 5 | 26 | 90 |  | [Weak automatability of Resolution](../../data/cards/TCS-5332.json) (TCS-5332) |
| 6 | 3 | 90 |  | [Superpolynomial \(\mathrm{AC}^{0}[p]\)-Frege lower bounds](../../data/cards/TCS-6602.json) (TCS-6602) |
| 7 | 13 | 86 |  | [Frege lower bounds from circuit hardness](../../data/cards/TCS-0024.json) (TCS-0024) |
| 8 | 17 | 86 |  | [Separating levels of bounded arithmetic](../../data/cards/TCS-1099.json) (TCS-1099) |
| 9 | 9 | 86 |  | [Superpolynomial \(\mathrm{Res}(\oplus)\) lower bounds](../../data/cards/TCS-1253.json) (TCS-1253) |
| 10 | 6 | 86 |  | [Complete disjoint NP pairs](../../data/cards/TCS-7273.json) (TCS-7273) |
| 11 | 18 | 82 |  | [Unprovability of polynomial circuit upper bounds in \(S_2^1\)](../../data/cards/TCS-1096.json) (TCS-1096) |
| 12 | 19 | 82 |  | [Unprovability of NP circuit upper bounds in \(T_2^1\)](../../data/cards/TCS-1097.json) (TCS-1097) |
| 13 | 20 | 82 |  | [\(PV_1\) nonprovability of polynomial-time SAT solvers](../../data/cards/TCS-1098.json) (TCS-1098) |
| 14 | 16 | 82 |  | [Lovász–Schrijver simulation of Cutting Planes](../../data/cards/TCS-5114.json) (TCS-5114) |
| 15 | 15 | 82 |  | [Cutting Planes versus polynomial-coefficient Cutting Planes](../../data/cards/TCS-6770.json) (TCS-6770) |
| 16 | 10 | 78 |  | [Linear-space Cutting Planes refutations](../../data/cards/TCS-5333.json) (TCS-5333) |
| 17 | 7 | 78 |  | [PSPACE-completeness of resolution clause space](../../data/cards/TCS-6759.json) (TCS-6759) |
| 18 | 12 | 78 |  | [Polynomial resolution length from logarithmic clause space](../../data/cards/TCS-6766.json) (TCS-6766) |
| 19 | 14 | 78 |  | [Simultaneous polynomial-length constant-space refutations](../../data/cards/TCS-6768.json) (TCS-6768) |
| 20 | 8 | 78 |  | [Linear versus general resolution](../../data/cards/TCS-6771.json) (TCS-6771) |
| 21 | 23 | 74 |  | [Short tree-like resolution from small proof space](../../data/cards/TCS-2889.json) (TCS-2889) |
| 22 | 25 | 74 |  | [Optimal proof systems outside NP](../../data/cards/TCS-5292.json) (TCS-5292) |
| 23 | 21 | 74 |  | [Sharp resolution length bounds at fixed width](../../data/cards/TCS-6767.json) (TCS-6767) |
| 24 | 11 | 74 |  | [Effective polynomial simulation of Extended Frege by Resolution](../../data/cards/TCS-7163.json) (TCS-7163) |
| 25 | 22 | 70 |  | [\(\mathrm{NC}^{0}\) proof systems for directed reachability](../../data/cards/TCS-0071.json) (TCS-0071) |
| 26 | 24 | 70 |  | [Does uniform randomized circuit learning imply P equals NP?](../../data/cards/TCS-4982.json) (TCS-4982) |

### Communication complexity and Boolean function analysis

Favor structural relations between algebra, information and communication. General compression, lifting and direct-sum principles precede exact costs of particular predicates.

| Rank | Previous | Score | Focus | Problem |
| ---: | ---: | ---: | :---: | --- |
| 1 | 1 | 98 | yes | [Log-rank conjecture](../../data/cards/TCS-6603.json) (TCS-6603) |
| 2 | 2 | 96 | yes | [Fourier Entropy–Influence conjecture](../../data/cards/TCS-6604.json) (TCS-6604) |
| 3 | 4 | 92 |  | [Mansour’s conjecture](../../data/cards/TCS-6581.json) (TCS-6581) |
| 4 | 3 | 92 |  | [Aaronson–Ambainis conjecture](../../data/cards/TCS-6605.json) (TCS-6605) |
| 5 | 7 | 88 |  | [Interactive compression with logarithmic input-length overhead](../../data/cards/TCS-5326.json) (TCS-5326) |
| 6 | 8 | 88 |  | [Polynomial relation between classical and quantum communication](../../data/cards/TCS-6450.json) (TCS-6450) |
| 7 | 5 | 88 |  | [Maximum influence of polynomial threshold functions](../../data/cards/TCS-6664.json) (TCS-6664) |
| 8 | 6 | 88 |  | [Aanderaa–Karp–Rosenberg conjecture](../../data/cards/TCS-7219.json) (TCS-7219) |
| 9 | 19 | 84 |  | [Formula size versus partition complexity](../../data/cards/TCS-1047.json) (TCS-1047) |
| 10 | 20 | 84 |  | [Linearization conjecture for depth-two circuits](../../data/cards/TCS-1059.json) (TCS-1059) |
| 11 | 25 | 84 |  | [Quadratic decision-tree bounds from block sensitivity](../../data/cards/TCS-1061.json) (TCS-1061) |
| 12 | 28 | 84 |  | [Constant-factor randomized direct sums for total Boolean functions](../../data/cards/TCS-5892.json) (TCS-5892) |
| 13 | 10 | 84 |  | [Number-on-forehead disjointness complexity](../../data/cards/TCS-6710.json) (TCS-6710) |
| 14 | 24 | 80 |  | [Large zero rectangles in low-rank real matrices](../../data/cards/TCS-0811.json) (TCS-0811) |
| 15 | 26 | 80 |  | [Sign-rank bounds from constant margin](../../data/cards/TCS-2658.json) (TCS-2658) |
| 16 | 27 | 80 |  | [Fourier rank versus sparsity](../../data/cards/TCS-3153.json) (TCS-3153) |
| 17 | 9 | 80 |  | [Fourier Min-Entropy–Influence conjecture](../../data/cards/TCS-6708.json) (TCS-6708) |
| 18 | 15 | 80 |  | [Deterministic communication versus monochromatic partition size](../../data/cards/TCS-6711.json) (TCS-6711) |
| 19 | 18 | 76 |  | [A randomized-communication characterization of ordinary KW games](../../data/cards/TCS-2571.json) (TCS-2571) |
| 20 | 17 | 76 |  | [Two-sided versus one-sided randomized communication](../../data/cards/TCS-4771.json) (TCS-4771) |
| 21 | 11 | 76 |  | [Multiparty Clique lower bounds in compression games](../../data/cards/TCS-5272.json) (TCS-5272) |
| 22 | 13 | 76 |  | [Sharp low-degree Fourier weight of halfspaces](../../data/cards/TCS-6705.json) (TCS-6705) |
| 23 | 12 | 76 |  | [Zero-error query complexity of recursive majority-of-three](../../data/cards/TCS-6707.json) (TCS-6707) |
| 24 | 22 | 72 |  | [Near-linear communication for exact maximum flow with local outputs](../../data/cards/TCS-0540.json) (TCS-0540) |
| 25 | 14 | 72 |  | [Removing low-influence directions from convex sets](../../data/cards/TCS-2664.json) (TCS-2664) |
| 26 | 21 | 72 |  | [PSPACE-hardness of a factor-two gap in decision-tree depth](../../data/cards/TCS-5189.json) (TCS-5189) |
| 27 | 23 | 66 |  | [Optimal one-bit cryptogenography success for every number of players](../../data/cards/TCS-0218.json) (TCS-0218) |
| 28 | 16 | 66 |  | [Optimal time exponent for truth-table decision-tree depth](../../data/cards/TCS-1845.json) (TCS-1845) |

### Fine-grained complexity

Favor the main fine-grained barriers and reductions that connect seemingly different primitives. Prefer a distinct algorithmic bottleneck to another variant of the same hypothesis.

| Rank | Previous | Score | Focus | Problem |
| ---: | ---: | ---: | :---: | --- |
| 1 | 1 | 96 | yes | [Strong Exponential Time Hypothesis](../../data/cards/TCS-6595.json) (TCS-6595) |
| 2 | 2 | 96 | yes | [Truly subcubic APSP](../../data/cards/TCS-6510.json) (TCS-6510) |
| 3 | 11 | 92 |  | [Truly subquadratic algorithms for 3SUM](../../data/cards/TCS-0557.json) (TCS-0557) |
| 4 | 9 | 92 |  | [Online matrix–vector multiplication conjecture](../../data/cards/TCS-6503.json) (TCS-6503) |
| 5 | 8 | 92 |  | [Truly subquadratic exact edit distance](../../data/cards/TCS-7179.json) (TCS-7179) |
| 6 | 5 | 88 |  | [Orthogonal Vectors Hypothesis](../../data/cards/TCS-6596.json) (TCS-6596) |
| 7 | 6 | 88 |  | [Algebraic k-Clique Hypothesis](../../data/cards/TCS-6597.json) (TCS-6597) |
| 8 | 10 | 88 |  | [Min-Plus Convolution Hypothesis](../../data/cards/TCS-6598.json) (TCS-6598) |
| 9 | 3 | 88 |  | [Randomized Strong Exponential Time Hypothesis](../../data/cards/TCS-6935.json) (TCS-6935) |
| 10 | 4 | 88 |  | [Randomized APSP hypothesis for polynomial integer weights](../../data/cards/TCS-6937.json) (TCS-6937) |
| 11 | 13 | 88 |  | [ETH versus Gap-ETH](../../data/cards/TCS-7313.json) (TCS-7313) |
| 12 | 7 | 84 |  | [Hyperclique Hypothesis](../../data/cards/TCS-6661.json) (TCS-6661) |
| 13 | 19 | 84 |  | [A fine-grained reduction from integer APSP to 3SUM](../../data/cards/TCS-6946.json) (TCS-6946) |
| 14 | 14 | 84 |  | [Disjunction of randomized SETH, integer APSP and 3SUM hypotheses](../../data/cards/TCS-6950.json) (TCS-6950) |
| 15 | 20 | 84 |  | [Linear-size Circuit-SAT below exhaustive search](../../data/cards/TCS-7270.json) (TCS-7270) |
| 16 | 25 | 80 |  | [Nondeterministic Strong Exponential Time Hypothesis](../../data/cards/TCS-0562.json) (TCS-0562) |
| 17 | 27 | 80 |  | [Fine-grained comparability of permanent and SETH](../../data/cards/TCS-0815.json) (TCS-0815) |
| 18 | 12 | 80 |  | [Hitting Set conjecture](../../data/cards/TCS-6599.json) (TCS-6599) |
| 19 | 15 | 80 |  | [Min-Weight k-Clique hypothesis](../../data/cards/TCS-6944.json) (TCS-6944) |
| 20 | 21 | 80 |  | [NC-SETH for polynomial-size, polylogarithmic-depth circuits](../../data/cards/TCS-6949.json) (TCS-6949) |
| 21 | 16 | 80 |  | [Directed unweighted APSP below \(n^{5/2}\)](../../data/cards/TCS-7347.json) (TCS-7347) |
| 22 | 18 | 76 |  | [Consequences of linear-time Orthogonal Vectors](../../data/cards/TCS-5422.json) (TCS-5422) |
| 23 | 22 | 76 |  | [Does logarithmic-dimension OV hardness imply Hitting Set hardness?](../../data/cards/TCS-6942.json) (TCS-6942) |
| 24 | 23 | 76 |  | [Exact-Weight k-Clique hypothesis](../../data/cards/TCS-6945.json) (TCS-6945) |
| 25 | 17 | 76 |  | [Balanced dense NFA Acceptance Hypothesis](../../data/cards/TCS-7373.json) (TCS-7373) |
| 26 | 26 | 72 |  | [A fine-grained reduction from logarithmic-dimension Hitting Set to 3SUM](../../data/cards/TCS-0560.json) (TCS-0560) |
| 27 | 28 | 72 |  | [Time exponents for multiple-string LCS over fixed alphabets](../../data/cards/TCS-0761.json) (TCS-0761) |
| 28 | 24 | 72 |  | [Subgraph detection with a sublinear treewidth exponent on some unbounded class](../../data/cards/TCS-6025.json) (TCS-6025) |

### Pseudorandomness and derandomization

Favor removing randomness as a general computational resource and constructing objects at their natural information limits. Broad hardness-randomness principles precede a particular seed-length improvement.

| Rank | Previous | Score | Focus | Problem |
| ---: | ---: | ---: | :---: | --- |
| 1 | 1 | 100 | yes | [P versus BPP](../../data/cards/TCS-0003.json) (TCS-0003) |
| 2 | 3 | 96 | yes | [L versus BPL](../../data/cards/TCS-0026.json) (TCS-0026) |
| 3 | 2 | 94 |  | [Optimal explicit pseudorandom generators for read-once branching programs](../../data/cards/TCS-6600.json) (TCS-6600) |
| 4 | 4 | 94 |  | [P versus RP](../../data/cards/TCS-6686.json) (TCS-6686) |
| 5 | 5 | 92 |  | [Optimal deterministic restricted-isometry matrices](../../data/cards/TCS-6662.json) (TCS-6662) |
| 6 | 6 | 92 |  | [AM versus NP](../../data/cards/TCS-6699.json) (TCS-6699) |
| 7 | 9 | 88 |  | [Unconditional subexponential simulation of BPP](../../data/cards/TCS-1005.json) (TCS-1005) |
| 8 | 10 | 88 |  | [Does arithmetic formula hardness derandomize identity testing?](../../data/cards/TCS-5287.json) (TCS-5287) |
| 9 | 12 | 88 |  | [Pseudorandom generators from hitting-set generators](../../data/cards/TCS-5341.json) (TCS-5341) |
| 10 | 7 | 88 |  | [Uniform PRGs from exponential-time hardness](../../data/cards/TCS-6696.json) (TCS-6696) |
| 11 | 11 | 88 |  | [Explicit near-optimal vertex expanders](../../data/cards/TCS-6879.json) (TCS-6879) |
| 12 | 8 | 88 |  | [Two-source extraction at log n plus constant entropy](../../data/cards/TCS-7271.json) (TCS-7271) |
| 13 | 19 | 84 |  | [Seeded extraction with constant total entropy loss](../../data/cards/TCS-1015.json) (TCS-1015) |
| 14 | 20 | 84 |  | [Extraction with log n plus constant seed length](../../data/cards/TCS-1016.json) (TCS-1016) |
| 15 | 24 | 84 |  | [Promise-BPP derandomization implying EXP circuit hardness](../../data/cards/TCS-1021.json) (TCS-1021) |
| 16 | 25 | 84 |  | [\(\mathrm{NEXP}\) circuit hardness from promise derandomization](../../data/cards/TCS-1022.json) (TCS-1022) |
| 17 | 40 | 84 |  | [Pseudodeterministic construction of primes at every length](../../data/cards/TCS-5798.json) (TCS-5798) |
| 18 | 14 | 84 |  | [Subpolynomial-seed pseudorandom generators for \(\mathrm{AC}^{0}[2]\)](../../data/cards/TCS-6693.json) (TCS-6693) |
| 19 | 13 | 84 |  | [Deterministic linear representations of transversal matroids](../../data/cards/TCS-6729.json) (TCS-6729) |
| 20 | 21 | 80 |  | [Universal determinant evaluations for bipartite matching](../../data/cards/TCS-1006.json) (TCS-1006) |
| 21 | 33 | 80 |  | [Optimal-size highly unbalanced lossless expanders](../../data/cards/TCS-1013.json) (TCS-1013) |
| 22 | 28 | 80 |  | [Lossless condensers with constant output overhead](../../data/cards/TCS-1014.json) (TCS-1014) |
| 23 | 36 | 80 |  | [Nontrivial PRGs for logarithmic-degree binary polynomials](../../data/cards/TCS-1122.json) (TCS-1122) |
| 24 | 26 | 80 |  | [Sub-log-squared seeds for width-four ordered branching programs](../../data/cards/TCS-1125.json) (TCS-1125) |
| 25 | 27 | 80 |  | [Sub-log-squared seeds for polynomial-size CNFs and DNFs](../../data/cards/TCS-1133.json) (TCS-1133) |
| 26 | 22 | 80 |  | [Simultaneously optimal averaging samplers](../../data/cards/TCS-6689.json) (TCS-6689) |
| 27 | 32 | 76 |  | [Fully explicit bipartite vertex expanders with constant additive loss](../../data/cards/TCS-1008.json) (TCS-1008) |
| 28 | 34 | 76 |  | [Optimal PRGs for high-dimensional combinatorial rectangles](../../data/cards/TCS-1124.json) (TCS-1124) |
| 29 | 37 | 76 |  | [Sublinear-seed generators for AC0 with parity gates](../../data/cards/TCS-1131.json) (TCS-1131) |
| 30 | 16 | 76 |  | [Super-bits from demi-bits](../../data/cards/TCS-1956.json) (TCS-1956) |
| 31 | 23 | 76 |  | [A general oracle conversion from two-source extractors to non-malleable extractors](../../data/cards/TCS-2201.json) (TCS-2201) |
| 32 | 17 | 76 |  | [Polynomial-stretch PRGs for depth-two threshold circuits with superlinear gate count](../../data/cards/TCS-3958.json) (TCS-3958) |
| 33 | 18 | 76 |  | [Does exponential circuit hardness derandomize amplified relational computation?](../../data/cards/TCS-4778.json) (TCS-4778) |
| 34 | 29 | 72 |  | [Promise-ZPP versus Promise-BPP derandomization](../../data/cards/TCS-0854.json) (TCS-0854) |
| 35 | 38 | 72 |  | [Universal traversal sequences under arbitrary labels](../../data/cards/TCS-1007.json) (TCS-1007) |
| 36 | 15 | 72 |  | [Linear-seed hardness-to-randomness sampling](../../data/cards/TCS-1018.json) (TCS-1018) |
| 37 | 35 | 72 |  | [Polynomial-time derandomization of randomized \(\mathrm{AC}^0\)](../../data/cards/TCS-1019.json) (TCS-1019) |
| 38 | 30 | 72 |  | [Promise-AM derandomization via targeted hitting sets](../../data/cards/TCS-1135.json) (TCS-1135) |
| 39 | 31 | 72 |  | [Derandomization from almost-all-inputs uniform hardness](../../data/cards/TCS-1137.json) (TCS-1137) |
| 40 | 39 | 72 |  | [Circuit hardness from inverse-polynomial-error BPP heuristics](../../data/cards/TCS-3986.json) (TCS-3986) |

### Parameterized complexity and algorithms

Favor whether parameterization truly enables tractability and whether iconic exact algorithms can break long-standing exponential barriers. Broad kernelization and width principles precede individual deletion variants.

| Rank | Previous | Score | Focus | Problem |
| ---: | ---: | ---: | :---: | --- |
| 1 | 1 | 98 | yes | [FPT versus \(\mathrm{W}[1]\)](../../data/cards/TCS-6592.json) (TCS-6592) |
| 2 | 3 | 94 | yes | [Breaking the \(2^{n}\) barrier for weighted TSP](../../data/cards/TCS-7233.json) (TCS-7233) |
| 3 | 2 | 94 |  | [Exponential Time Hypothesis](../../data/cards/TCS-6593.json) (TCS-6593) |
| 4 | 7 | 90 |  | [Subset Sum below the meet-in-the-middle exponent](../../data/cards/TCS-4790.json) (TCS-4790) |
| 5 | 4 | 90 |  | [Set Cover conjecture](../../data/cards/TCS-6594.json) (TCS-6594) |
| 6 | 8 | 90 |  | [Strictness of the W-hierarchy](../../data/cards/TCS-6731.json) (TCS-6731) |
| 7 | 6 | 86 |  | [Polynomial kernel for Edge Multiway Cut](../../data/cards/TCS-6660.json) (TCS-6660) |
| 8 | 14 | 86 |  | [Polynomial compression versus polynomial kernelization](../../data/cards/TCS-6734.json) (TCS-6734) |
| 9 | 9 | 86 |  | [General Formula-SAT with a fixed exponential saving](../../data/cards/TCS-6974.json) (TCS-6974) |
| 10 | 10 | 86 |  | [Single-exponential Directed Feedback Vertex Set](../../data/cards/TCS-7035.json) (TCS-7035) |
| 11 | 11 | 86 |  | [Exact recognition of bounded clique-width](../../data/cards/TCS-7181.json) (TCS-7181) |
| 12 | 5 | 86 |  | [FPT approximation of twin-width](../../data/cards/TCS-7241.json) (TCS-7241) |
| 13 | 27 | 82 |  | [Directed Hamiltonicity](../../data/cards/TCS-0801.json) (TCS-0801) |
| 14 | 36 | 82 |  | [Polynomial kernels for forbidden-minor vertex deletion](../../data/cards/TCS-4695.json) (TCS-4695) |
| 15 | 37 | 82 |  | [Polynomial kernels for Directed Feedback Vertex Set](../../data/cards/TCS-6379.json) (TCS-6379) |
| 16 | 19 | 82 |  | [Chromatic number in \(2^{n}\) time and polynomial space](../../data/cards/TCS-6728.json) (TCS-6728) |
| 17 | 22 | 82 |  | [Deterministic polynomial kernels for Almost 2-SAT](../../data/cards/TCS-6749.json) (TCS-6749) |
| 18 | 13 | 82 |  | [Fixed-parameter tractability of graph isomorphism by rank-width](../../data/cards/TCS-7312.json) (TCS-7312) |
| 19 | 26 | 78 |  | [ETH barrier to single-exponential treewidth computation](../../data/cards/TCS-0787.json) (TCS-0787) |
| 20 | 16 | 78 |  | [Does ETH rule out subexponential constant-gap Max-Clique?](../../data/cards/TCS-2662.json) (TCS-2662) |
| 21 | 17 | 78 |  | [\(\mathrm{W}[2]\)-hardness of bounded-VC-dimension Hitting Set](../../data/cards/TCS-4289.json) (TCS-4289) |
| 22 | 18 | 78 |  | [A DAG-treewidth dichotomy for homomorphism counting in degenerate graphs](../../data/cards/TCS-5374.json) (TCS-5374) |
| 23 | 25 | 78 |  | [Polynomial kernels for minor-free edge deletion](../../data/cards/TCS-7023.json) (TCS-7023) |
| 24 | 31 | 74 |  | [Fixed-parameter tractability of coloring graphs with no induced P5](../../data/cards/TCS-0597.json) (TCS-0597) |
| 25 | 28 | 74 |  | [Shortest common superstring in \(O^*(1.99^n)\) time](../../data/cards/TCS-0816.json) (TCS-0816) |
| 26 | 24 | 74 |  | [Tight ETH lower bounds for binary Nearest Codeword at every constant factor](../../data/cards/TCS-1945.json) (TCS-1945) |
| 27 | 33 | 74 |  | [Slice-wise Polynomial Space Conjecture](../../data/cards/TCS-2804.json) (TCS-2804) |
| 28 | 15 | 74 |  | [Job-shop approximation parameterized only by machines and accuracy](../../data/cards/TCS-6814.json) (TCS-6814) |
| 29 | 20 | 74 |  | [Polynomial kernel for Planar Edge Deletion](../../data/cards/TCS-7022.json) (TCS-7022) |
| 30 | 12 | 74 |  | [Independent set algorithms from tropical circuit size](../../data/cards/TCS-7247.json) (TCS-7247) |
| 31 | 32 | 70 |  | [Converting CNF to DNF](../../data/cards/TCS-0799.json) (TCS-0799) |
| 32 | 29 | 70 |  | [Cutwidth](../../data/cards/TCS-0800.json) (TCS-0800) |
| 33 | 30 | 70 |  | [Sub-base-two exact maximum acyclic subgraph](../../data/cards/TCS-0808.json) (TCS-0808) |
| 34 | 21 | 70 |  | [Polynomial exact metric sparsifiers with a crossing-edge budget](../../data/cards/TCS-3480.json) (TCS-3480) |
| 35 | 34 | 70 |  | [Disjoint-union closure of tractable forbidden patterns](../../data/cards/TCS-3917.json) (TCS-3917) |
| 36 | 35 | 70 |  | [Expected FPT delay from small-witness decision](../../data/cards/TCS-4440.json) (TCS-4440) |
| 37 | 23 | 70 |  | [Fixed-parameter tractability of Perfect Edge Deletion](../../data/cards/TCS-7027.json) (TCS-7027) |

### Approximation algorithms and inapproximability

Favor principles that organize approximation hardness and prominent problems resisting even coarse guarantees. General thresholds and integrality phenomena precede narrow ratio improvements.

| Rank | Previous | Score | Focus | Problem |
| ---: | ---: | ---: | :---: | --- |
| 1 | 2 | 98 | yes | [Unique Games Conjecture](../../data/cards/TCS-0006.json) (TCS-0006) |
| 2 | 1 | 96 | yes | [Constant-factor approximation for Densest k-Subgraph](../../data/cards/TCS-6587.json) (TCS-6587) |
| 3 | 4 | 96 |  | [Small-Set Expansion Hypothesis](../../data/cards/TCS-7160.json) (TCS-7160) |
| 4 | 3 | 92 |  | [Polylogarithmic approximation for Directed Steiner Tree](../../data/cards/TCS-6588.json) (TCS-6588) |
| 5 | 10 | 92 |  | [Constant-factor approximation for uniform Sparsest Cut](../../data/cards/TCS-7266.json) (TCS-7266) |
| 6 | 7 | 92 |  | [Vertex Cover approximation below factor two](../../data/cards/TCS-7282.json) (TCS-7282) |
| 7 | 5 | 88 |  | [Subtour-LP integrality gap for metric TSP](../../data/cards/TCS-6589.json) (TCS-6589) |
| 8 | 13 | 88 |  | [Constant-factor approximation for Directed Feedback Vertex Set](../../data/cards/TCS-6591.json) (TCS-6591) |
| 9 | 6 | 88 |  | [Optimal polynomial-time approximation ratio for metric k-Median](../../data/cards/TCS-6659.json) (TCS-6659) |
| 10 | 11 | 88 |  | [Unconditional NP-hardness at the Goemans–Williamson Max-Cut threshold](../../data/cards/TCS-7281.json) (TCS-7281) |
| 11 | 12 | 88 |  | [Optimal polynomial-time approximation ratio for metric TSP](../../data/cards/TCS-7356.json) (TCS-7356) |
| 12 | 9 | 84 |  | [Subtour-LP integrality gap for asymmetric TSP](../../data/cards/TCS-6590.json) (TCS-6590) |
| 13 | 29 | 84 |  | [Optimal general-domain CSP approximation under Unique Games hardness](../../data/cards/TCS-6756.json) (TCS-6756) |
| 14 | 21 | 84 |  | [Min-CSP approximation at the SDP integrality gap](../../data/cards/TCS-6757.json) (TCS-6757) |
| 15 | 14 | 84 |  | [Optimal polynomial-time approximation ratio for asymmetric TSP](../../data/cards/TCS-7357.json) (TCS-7357) |
| 16 | 17 | 84 |  | [Optimal polynomial-time approximation ratio for Steiner Tree](../../data/cards/TCS-7358.json) (TCS-7358) |
| 17 | 25 | 80 |  | [Parameterized Inapproximability Hypothesis from \(\mathrm{FPT} \ne  \mathrm{W}[1]\)](../../data/cards/TCS-1930.json) (TCS-1930) |
| 18 | 16 | 80 |  | [Optimal approximation for nonmonotone submodular maximization over a matroid](../../data/cards/TCS-5407.json) (TCS-5407) |
| 19 | 8 | 80 |  | [Does a fixed d-to-1 Games conjecture imply Unique Games?](../../data/cards/TCS-5544.json) (TCS-5544) |
| 20 | 20 | 80 |  | [Constant-factor approximation for Dasgupta’s hierarchical clustering objective](../../data/cards/TCS-7318.json) (TCS-7318) |
| 21 | 15 | 80 |  | [Optimal polynomial-time approximation ratio for Euclidean k-means](../../data/cards/TCS-7353.json) (TCS-7353) |
| 22 | 26 | 76 |  | [Almost 3-colorable graphs versus graphs with no large independent set](../../data/cards/TCS-2625.json) (TCS-2625) |
| 23 | 28 | 76 |  | [Constant-factor approximation of graph crossing number](../../data/cards/TCS-5787.json) (TCS-5787) |
| 24 | 18 | 76 |  | [A polynomial-time constant approximation for capacitated k-median without violations](../../data/cards/TCS-6309.json) (TCS-6309) |
| 25 | 22 | 76 |  | [Square-root logarithmic approximation for metric labeling](../../data/cards/TCS-7287.json) (TCS-7287) |
| 26 | 19 | 76 |  | [Optimal polynomial-time approximation ratio for metric k-means](../../data/cards/TCS-7354.json) (TCS-7354) |
| 27 | 23 | 72 |  | [Configuration-LP gap for maximum generalized assignment](../../data/cards/TCS-0922.json) (TCS-0922) |
| 28 | 24 | 72 |  | [Hardness of coloring 2-dicolorable digraphs with any fixed number of colors](../../data/cards/TCS-1168.json) (TCS-1168) |
| 29 | 27 | 72 |  | [Subquadratic factor-three edit-distance approximation](../../data/cards/TCS-5554.json) (TCS-5554) |

### Online algorithms, scheduling and packing

Favor canonical online-information barriers and general selection principles. Keep scheduling and packing prominent in the remainder; narrower model-specific constants come later.

| Rank | Previous | Score | Focus | Problem |
| ---: | ---: | ---: | :---: | --- |
| 1 | 1 | 96 | yes | [Deterministic competitiveness of k-server](../../data/cards/TCS-6575.json) (TCS-6575) |
| 2 | 7 | 96 | yes | [Matroid secretary conjecture](../../data/cards/TCS-7316.json) (TCS-7316) |
| 3 | 5 | 92 |  | [Optimal competitive ratio for convex body chasing](../../data/cards/TCS-6576.json) (TCS-6576) |
| 4 | 2 | 92 |  | [Optimal approximation ratio for unrelated-machine makespan](../../data/cards/TCS-6638.json) (TCS-6638) |
| 5 | 8 | 92 |  | [Randomized competitiveness of k-server](../../data/cards/TCS-7317.json) (TCS-7317) |
| 6 | 6 | 88 |  | [Minimax dimension dependence in bandit convex optimization](../../data/cards/TCS-6577.json) (TCS-6577) |
| 7 | 4 | 88 |  | [Constant additive error for one-dimensional bin packing](../../data/cards/TCS-6640.json) (TCS-6640) |
| 8 | 3 | 88 |  | [Optimal approximation ratio for precedence-constrained makespan](../../data/cards/TCS-6676.json) (TCS-6676) |
| 9 | 22 | 88 |  | [Additive-one approximation for bin packing](../../data/cards/TCS-6721.json) (TCS-6721) |
| 10 | 9 | 84 |  | [Constant-factor online contention resolution for matroids](../../data/cards/TCS-5779.json) (TCS-5779) |
| 11 | 11 | 84 |  | [Minimax rate of sequential binary calibration](../../data/cards/TCS-7319.json) (TCS-7319) |
| 12 | 23 | 84 |  | [Optimal competitive ratio of online bin packing](../../data/cards/TCS-7473.json) (TCS-7473) |
| 13 | 28 | 84 |  | [Polynomial-time constant approximation for the General Scheduling Problem](../../data/cards/TCS-7478.json) (TCS-7478) |
| 14 | 15 | 80 |  | [Polynomial-time unit-job precedence scheduling on fixed machines](../../data/cards/TCS-0935.json) (TCS-0935) |
| 15 | 12 | 80 |  | [Optimal randomized competitive ratio of weighted k-server](../../data/cards/TCS-5030.json) (TCS-5030) |
| 16 | 10 | 80 |  | [Constant-factor related-machine precedence scheduling](../../data/cards/TCS-6724.json) (TCS-6724) |
| 17 | 29 | 80 |  | [Optimal prophet-secretary constant](../../data/cards/TCS-7479.json) (TCS-7479) |
| 18 | 21 | 76 |  | [One forecaster with the optimal regret rate for every proper loss](../../data/cards/TCS-1529.json) (TCS-1529) |
| 19 | 13 | 76 |  | [Sublinear-in-q prophet inequalities for q-matroid intersection](../../data/cards/TCS-5221.json) (TCS-5221) |
| 20 | 16 | 76 |  | [Randomized competitive ratio of list update](../../data/cards/TCS-7335.json) (TCS-7335) |
| 21 | 24 | 76 |  | [Optimal stretch for online bin stretching](../../data/cards/TCS-7474.json) (TCS-7474) |
| 22 | 14 | 72 |  | [Sublogarithmic competitiveness for online metric TSP](../../data/cards/TCS-1241.json) (TCS-1241) |
| 23 | 17 | 72 |  | [Pinwheel Packing in NP](../../data/cards/TCS-6078.json) (TCS-6078) |
| 24 | 18 | 72 |  | [Adaptive regret in misspecified linear bandits](../../data/cards/TCS-6836.json) (TCS-6836) |
| 25 | 27 | 72 |  | [Three-competitive deterministic file migration](../../data/cards/TCS-7477.json) (TCS-7477) |
| 26 | 20 | 68 |  | [Exact optimal stopping for mixtures of product distributions](../../data/cards/TCS-0700.json) (TCS-0700) |
| 27 | 19 | 68 |  | [Optimal bandit regret for paths in a directed grid](../../data/cards/TCS-5252.json) (TCS-5252) |
| 28 | 25 | 68 |  | [Optimal deterministic price of obligatory testing](../../data/cards/TCS-7475.json) (TCS-7475) |
| 29 | 26 | 68 |  | [Power of randomization in scheduling with obligatory tests](../../data/cards/TCS-7476.json) (TCS-7476) |

### Beyond worst-case and average-case analysis

Favor the worst-case/average-case bridge and statistical-computational gaps over the performance of one heuristic. Random combinatorial optimization is attractive when it exposes a genuine algorithmic threshold.

| Rank | Previous | Score | Focus | Problem |
| ---: | ---: | ---: | :---: | --- |
| 1 | 2 | 98 | yes | [Average-case NP hardness from \(\mathrm{P} \ne  \mathrm{NP}\)](../../data/cards/TCS-0012.json) (TCS-0012) |
| 2 | 1 | 94 | yes | [Planted clique conjecture](../../data/cards/TCS-6656.json) (TCS-6656) |
| 3 | 3 | 90 |  | [Computational threshold for tensor PCA](../../data/cards/TCS-6657.json) (TCS-6657) |
| 4 | 4 | 90 |  | [Computational Kesten–Stigum threshold](../../data/cards/TCS-6684.json) (TCS-6684) |
| 5 | 5 | 90 |  | [Polynomial-time refutation of random 3-SAT at constant density](../../data/cards/TCS-7238.json) (TCS-7238) |
| 6 | 13 | 86 |  | [Algorithmic threshold for random k-SAT](../../data/cards/TCS-4876.json) (TCS-4876) |
| 7 | 6 | 86 |  | [Infinitely-often one-way functions from average-case NP hardness](../../data/cards/TCS-6453.json) (TCS-6453) |
| 8 | 8 | 86 |  | [Exponential worst-case hardness implies mild average-case hardness in NP](../../data/cards/TCS-6702.json) (TCS-6702) |
| 9 | 10 | 82 |  | [Algorithmic threshold for the symmetric binary perceptron](../../data/cards/TCS-5011.json) (TCS-5011) |
| 10 | 11 | 82 |  | [Optimization and certification of Max-Cut in random cubic graphs](../../data/cards/TCS-5406.json) (TCS-5406) |
| 11 | 7 | 82 |  | [Polynomial smoothed complexity of FLIP for Max-Cut](../../data/cards/TCS-6658.json) (TCS-6658) |
| 12 | 12 | 78 |  | [Optimal exponential hardness amplification for balanced NP languages](../../data/cards/TCS-6703.json) (TCS-6703) |
| 13 | 9 | 78 |  | [Polynomial simplex complexity under zero-preserving perturbations](../../data/cards/TCS-7148.json) (TCS-7148) |
| 14 | 14 | 78 |  | [Asymptotically optimal algorithms for random three-dimensional assignment](../../data/cards/TCS-7378.json) (TCS-7378) |
| 15 | 15 | 78 |  | [Polynomial-time exact optimization of random asymmetric TSP](../../data/cards/TCS-7379.json) (TCS-7379) |
| 16 | 17 | 74 |  | [Average-case optimality of standard Shellsort](../../data/cards/TCS-7388.json) (TCS-7388) |
| 17 | 18 | 74 |  | [Instance-optimal outer approximation of convex polytopes](../../data/cards/TCS-7402.json) (TCS-7402) |
| 18 | 16 | 68 |  | [Exact random-order ratio of Best Fit bin packing](../../data/cards/TCS-7381.json) (TCS-7381) |

### Sampling, Markov chains and mixing times

Favor mixing at natural uniqueness or criticality boundaries and general principles of random exploration. Critical physical dynamics and combinatorial sampling take precedence over a specialized implementation improvement.

| Rank | Previous | Score | Focus | Problem |
| ---: | ---: | ---: | :---: | --- |
| 1 | 1 | 94 | yes | [Rapid mixing of Glauber dynamics with \(\Delta +2\) colours](../../data/cards/TCS-6621.json) (TCS-6621) |
| 2 | 3 | 90 | yes | [Polynomial mixing of critical three-dimensional Ising dynamics](../../data/cards/TCS-6668.json) (TCS-6668) |
| 3 | 2 | 90 |  | [Kannan–Tetali–Vempala conjecture](../../data/cards/TCS-6622.json) (TCS-6622) |
| 4 | 5 | 86 |  | [Cutoff for bounded-degree transitive expanders](../../data/cards/TCS-6843.json) (TCS-6843) |
| 5 | 12 | 86 |  | [Stationary-start cover-time lower bound](../../data/cards/TCS-7480.json) (TCS-7480) |
| 6 | 17 | 86 |  | [Hard-core phase transition on the square lattice](../../data/cards/TCS-7485.json) (TCS-7485) |
| 7 | 4 | 82 |  | [Polynomial mixing of planar Ising dynamics with plus boundaries](../../data/cards/TCS-6839.json) (TCS-6839) |
| 8 | 7 | 82 |  | [Monotonicity of Ising spectral gaps](../../data/cards/TCS-6840.json) (TCS-6840) |
| 9 | 8 | 82 |  | [Mixing of the self-avoiding-walk pivot chain](../../data/cards/TCS-6857.json) (TCS-6857) |
| 10 | 13 | 82 |  | [Polynomial mixing at the four-state Potts critical point](../../data/cards/TCS-7481.json) (TCS-7481) |
| 11 | 15 | 82 |  | [Cluster sampling of graph colorings with \(\Delta+1\) colors](../../data/cards/TCS-7483.json) (TCS-7483) |
| 12 | 6 | 78 |  | [Weakly negatively regressive sampling of matroid bases](../../data/cards/TCS-2861.json) (TCS-2861) |
| 13 | 10 | 78 |  | [General characterization of parallel random-walk cover time](../../data/cards/TCS-7386.json) (TCS-7386) |
| 14 | 11 | 78 |  | [Exact uniform spanning-tree sampling in linear time](../../data/cards/TCS-7404.json) (TCS-7404) |
| 15 | 9 | 74 |  | [Deterministic approximation scheme for graph cover times](../../data/cards/TCS-6851.json) (TCS-6851) |
| 16 | 14 | 74 |  | [Critical Swendsen–Wang spectral-gap exponent](../../data/cards/TCS-7482.json) (TCS-7482) |
| 17 | 16 | 74 |  | [Rapid cluster sampling of three-colourings on the square torus](../../data/cards/TCS-7484.json) (TCS-7484) |

### Counting and enumeration

Favor canonical approximate-counting barriers and the decision/counting distinction. General enumeration principles come before Gray-code variants and refinements of one counting algorithm.

| Rank | Previous | Score | Focus | Problem |
| ---: | ---: | ---: | :---: | --- |
| 1 | 1 | 94 | yes | [FPRAS for counting perfect matchings](../../data/cards/TCS-6628.json) (TCS-6628) |
| 2 | 2 | 94 | yes | [FPRAS for #BIS](../../data/cards/TCS-7221.json) (TCS-7221) |
| 3 | 3 | 96 |  | [FP versus #P](../../data/cards/TCS-6820.json) (TCS-6820) |
| 4 | 4 | 90 |  | [Deterministic FPTAS for the nonnegative permanent](../../data/cards/TCS-6629.json) (TCS-6629) |
| 5 | 7 | 90 |  | [FP = #P from \(\mathrm{P} = \mathrm{NP}\)](../../data/cards/TCS-6821.json) (TCS-6821) |
| 6 | 12 | 86 |  | [Deterministic relative counting for DNF](../../data/cards/TCS-1004.json) (TCS-1004) |
| 7 | 8 | 86 |  | [Output-polynomial hypergraph transversal enumeration](../../data/cards/TCS-7112.json) (TCS-7112) |
| 8 | 5 | 86 |  | [Output-polynomial vertex enumeration](../../data/cards/TCS-7240.json) (TCS-7240) |
| 9 | 18 | 82 |  | [Decision versus approximate counting for fixed-width SAT](../../data/cards/TCS-4671.json) (TCS-4671) |
| 10 | 6 | 82 |  | [FPRAS for counting undirected Euler tours](../../data/cards/TCS-6671.json) (TCS-6671) |
| 11 | 10 | 82 |  | [#BIS-easiness of Boolean log-supermodular counting CSPs](../../data/cards/TCS-7320.json) (TCS-7320) |
| 12 | 9 | 82 |  | [Fully polynomial randomized approximation of mixed discriminants](../../data/cards/TCS-7355.json) (TCS-7355) |
| 13 | 11 | 78 |  | [Parity subgraph-counting dichotomy](../../data/cards/TCS-3037.json) (TCS-3037) |
| 14 | 17 | 78 |  | [Treewidth classification of approximate counting CSP](../../data/cards/TCS-3635.json) (TCS-3635) |
| 15 | 13 | 78 |  | [Finite-domain enumeration-CSP dichotomy](../../data/cards/TCS-7099.json) (TCS-7099) |
| 16 | 14 | 74 |  | [Does P ≠ NP imply both polynomial-space enumeration separations?](../../data/cards/TCS-7084.json) (TCS-7084) |
| 17 | 15 | 74 |  | [Incremental polynomial-time binary-matroid circuit enumeration](../../data/cards/TCS-7086.json) (TCS-7086) |
| 18 | 19 | 74 |  | [Nearly linear approximate counting for knapsack](../../data/cards/TCS-7399.json) (TCS-7399) |
| 19 | 22 | 74 |  | [Edge-exchange Gray codes for directed spanning trees](../../data/cards/TCS-7488.json) (TCS-7488) |
| 20 | 16 | 70 |  | [A natural OutputP versus IncP separation from clique-free domination](../../data/cards/TCS-7082.json) (TCS-7082) |
| 21 | 21 | 70 |  | [Pivot-exchange Gray codes for spanning trees](../../data/cards/TCS-7487.json) (TCS-7487) |
| 22 | 20 | 66 |  | [Ranking and unranking a spanning-tree Gray code](../../data/cards/TCS-7486.json) (TCS-7486) |
| 23 | 23 | 66 |  | [Polynomial-delay disjointness Gray codes for combinations](../../data/cards/TCS-7489.json) (TCS-7489) |

### Structural graph theory and graph algorithms

Favor global structural conjectures and the complexity of graph identity. Exact matching, flow and sparsity barriers lead the algorithmic remainder; close variants and specialized class restrictions follow.

| Rank | Previous | Score | Focus | Problem |
| ---: | ---: | ---: | :---: | --- |
| 1 | 1 | 98 | yes | [Hadwiger’s conjecture](../../data/cards/TCS-6651.json) (TCS-6651) |
| 2 | 5 | 96 | yes | [Graph isomorphism in polynomial time](../../data/cards/TCS-7222.json) (TCS-7222) |
| 3 | 3 | 96 |  | [Erdős–Hajnal conjecture](../../data/cards/TCS-6652.json) (TCS-6652) |
| 4 | 2 | 94 |  | [Deterministic linear-time minimum spanning tree](../../data/cards/TCS-6536.json) (TCS-6536) |
| 5 | 7 | 94 |  | [Almost-linear-time exact maximum matching in general graphs](../../data/cards/TCS-6538.json) (TCS-6538) |
| 6 | 6 | 94 |  | [Tutte’s 5-flow conjecture](../../data/cards/TCS-7248.json) (TCS-7248) |
| 7 | 47 | 90 |  | [Erdős girth conjecture](../../data/cards/TCS-2783.json) (TCS-2783) |
| 8 | 21 | 90 |  | [Erdős girth conjecture](../../data/cards/TCS-6500.json) (TCS-6500) |
| 9 | 8 | 90 |  | [Gyárfás–Sumner conjecture](../../data/cards/TCS-6653.json) (TCS-6653) |
| 10 | 4 | 90 |  | [Reed’s conjecture](../../data/cards/TCS-6682.json) (TCS-6682) |
| 11 | 15 | 90 |  | [Vertex reconstruction conjecture](../../data/cards/TCS-7216.json) (TCS-7216) |
| 12 | 22 | 90 |  | [List edge-coloring conjecture](../../data/cards/TCS-7218.json) (TCS-7218) |
| 13 | 10 | 90 |  | [Caccetta–Häggkvist conjecture](../../data/cards/TCS-7251.json) (TCS-7251) |
| 14 | 25 | 86 |  | [Deterministic Exact Matching](../../data/cards/TCS-6511.json) (TCS-6511) |
| 15 | 12 | 86 |  | [Seese’s conjecture](../../data/cards/TCS-6654.json) (TCS-6654) |
| 16 | 9 | 86 |  | [Optimal bounds in the Excluded Grid Theorem](../../data/cards/TCS-6683.json) (TCS-6683) |
| 17 | 13 | 86 |  | [Exact directed maximum flow in \(O((m+n) \operatorname{polylog} n)\) time](../../data/cards/TCS-7228.json) (TCS-7228) |
| 18 | 16 | 86 |  | [Berge–Fulkerson conjecture](../../data/cards/TCS-7249.json) (TCS-7249) |
| 19 | 17 | 86 |  | [Barnette’s conjecture](../../data/cards/TCS-7250.json) (TCS-7250) |
| 20 | 18 | 86 |  | [Seymour’s second-neighborhood conjecture](../../data/cards/TCS-7253.json) (TCS-7253) |
| 21 | 35 | 86 |  | [Lovász conjecture](../../data/cards/TCS-7289.json) (TCS-7289) |
| 22 | 48 | 84 |  | [Ramanujan graphs of every degree](../../data/cards/TCS-6874.json) (TCS-6874) |
| 23 | 49 | 84 |  | [Two-sided Ramanujan signings](../../data/cards/TCS-6875.json) (TCS-6875) |
| 24 | 45 | 82 |  | [Fat Minors](../../data/cards/TCS-0315.json) (TCS-0315) |
| 25 | 24 | 82 |  | [Sparsification conjecture](../../data/cards/TCS-1206.json) (TCS-1206) |
| 26 | 11 | 82 |  | [Almost-linear triangle detection](../../data/cards/TCS-6539.json) (TCS-6539) |
| 27 | 14 | 82 |  | [Cereceda’s conjecture](../../data/cards/TCS-6655.json) (TCS-6655) |
| 28 | 52 | 82 |  | [Well-quasi-ordering by pivot-minors](../../data/cards/TCS-7145.json) (TCS-7145) |
| 29 | 27 | 82 |  | [Graph canonization versus graph isomorphism](../../data/cards/TCS-7180.json) (TCS-7180) |
| 30 | 23 | 82 |  | [Tuza’s triangle packing–covering conjecture](../../data/cards/TCS-7252.json) (TCS-7252) |
| 31 | 39 | 82 |  | [Strongly explicit Ramanujan families for every degree](../../data/cards/TCS-7285.json) (TCS-7285) |
| 32 | 19 | 82 |  | [Strongly polynomial near-linear negative-weight shortest paths](../../data/cards/TCS-7341.json) (TCS-7341) |
| 33 | 20 | 82 |  | [Strongly polynomial maximum flow below the \(mn\) barrier](../../data/cards/TCS-7346.json) (TCS-7346) |
| 34 | 46 | 80 |  | [Linear neighborhood complexity of hereditary small graph classes](../../data/cards/TCS-1639.json) (TCS-1639) |
| 35 | 50 | 78 |  | [Bipartite circle pivot-minors from large rank-width](../../data/cards/TCS-7143.json) (TCS-7143) |
| 36 | 51 | 78 |  | [Tree vertex-minors from large linear rank-width](../../data/cards/TCS-7144.json) (TCS-7144) |
| 37 | 33 | 78 |  | [Edge reconstruction conjecture](../../data/cards/TCS-7217.json) (TCS-7217) |
| 38 | 30 | 78 |  | [Constant-factor treewidth preservation by subcubic subgraphs](../../data/cards/TCS-7245.json) (TCS-7245) |
| 39 | 26 | 78 |  | [Neumann–Lara conjecture](../../data/cards/TCS-7254.json) (TCS-7254) |
| 40 | 31 | 78 |  | [Linear-time directed shortest paths with nonnegative real weights](../../data/cards/TCS-7263.json) (TCS-7263) |
| 41 | 28 | 78 |  | [Steiner Shortcut Conjecture](../../data/cards/TCS-7342.json) (TCS-7342) |
| 42 | 29 | 78 |  | [Deterministic almost-linear vertex connectivity](../../data/cards/TCS-7343.json) (TCS-7343) |
| 43 | 32 | 78 |  | [Single-exponential exact cut mimicking networks](../../data/cards/TCS-7348.json) (TCS-7348) |
| 44 | 53 | 78 |  | [Near-linear-space exact planar distance oracles with polylogarithmic queries](../../data/cards/TCS-7394.json) (TCS-7394) |
| 45 | 40 | 74 |  | [Bipartite Exact Matching: deterministic polynomial time](../../data/cards/TCS-0611.json) (TCS-0611) |
| 46 | 41 | 74 |  | [Polynomial-time computation of planar treewidth](../../data/cards/TCS-0771.json) (TCS-0771) |
| 47 | 44 | 74 |  | [Optimal exact-distance label length for planar graphs](../../data/cards/TCS-0775.json) (TCS-0775) |
| 48 | 34 | 74 |  | [Well-quasi-ordering Eulerian digraphs by weak immersion](../../data/cards/TCS-1246.json) (TCS-1246) |
| 49 | 38 | 74 |  | [Boolean dimension of posets with planar cover graphs](../../data/cards/TCS-7244.json) (TCS-7244) |
| 50 | 36 | 74 |  | [Almost-linear exact directed global minimum cut](../../data/cards/TCS-7344.json) (TCS-7344) |
| 51 | 37 | 74 |  | [Almost-linear directed vertex connectivity](../../data/cards/TCS-7345.json) (TCS-7345) |
| 52 | 43 | 70 |  | [Polylogarithmic treewidth with forbidden induced minors](../../data/cards/TCS-0587.json) (TCS-0587) |
| 53 | 42 | 70 |  | [3-colorability of diameter-two graphs](../../data/cards/TCS-0594.json) (TCS-0594) |

### Data structures

Favor universal adaptivity and strong data-structure lower bounds, followed by deterministic basic primitives. Long-standing structural conjectures precede improvements tied to one queue or hashing implementation.

| Rank | Previous | Score | Focus | Problem |
| ---: | ---: | ---: | :---: | --- |
| 1 | 1 | 98 | yes | [Dynamic optimality conjecture](../../data/cards/TCS-6498.json) (TCS-6498) |
| 2 | 2 | 96 | yes | [Superlogarithmic static cell-probe lower bounds](../../data/cards/TCS-6540.json) (TCS-6540) |
| 3 | 3 | 90 |  | [Deterministic linear-time static dictionaries](../../data/cards/TCS-6586.json) (TCS-6586) |
| 4 | 4 | 90 |  | [Constant-time deterministic dynamic dictionaries](../../data/cards/TCS-7331.json) (TCS-7331) |
| 5 | 5 | 90 |  | [Multiphase conjecture](../../data/cards/TCS-7338.json) (TCS-7338) |
| 6 | 21 | 90 |  | [Polynomial lower bounds for adaptive dynamic data structures](../../data/cards/TCS-7398.json) (TCS-7398) |
| 7 | 6 | 86 |  | [Superlinear cell-probe lower bounds for succinct Boolean matrix-vector products](../../data/cards/TCS-0949.json) (TCS-0949) |
| 8 | 12 | 86 |  | [Superconstant word-RAM time for prefix-\(U_1\)](../../data/cards/TCS-5825.json) (TCS-5825) |
| 9 | 9 | 86 |  | [Space-query exponent curve of 3SUM indexing](../../data/cards/TCS-7333.json) (TCS-7333) |
| 10 | 10 | 86 |  | [Strong SetDisjointness conjecture](../../data/cards/TCS-7334.json) (TCS-7334) |
| 11 | 7 | 82 |  | [Randomized complexity of online labeling](../../data/cards/TCS-0300.json) (TCS-0300) |
| 12 | 11 | 82 |  | [Unified bound for binary search trees](../../data/cards/TCS-5706.json) (TCS-5706) |
| 13 | 15 | 82 |  | [Deque conjecture](../../data/cards/TCS-6508.json) (TCS-6508) |
| 14 | 8 | 82 |  | [Amortized decrease-key complexity of standard pairing heaps](../../data/cards/TCS-7328.json) (TCS-7328) |
| 15 | 25 | 82 |  | [Splay traversal conjecture](../../data/cards/TCS-7493.json) (TCS-7493) |
| 16 | 13 | 78 |  | [Logarithmic fully retroactive priority queues](../../data/cards/TCS-7329.json) (TCS-7329) |
| 17 | 19 | 78 |  | [Optimal distance oracles that also report paths](../../data/cards/TCS-7382.json) (TCS-7382) |
| 18 | 20 | 78 |  | [Truly subquadratic preprocessing for stretch-3 distance oracles](../../data/cards/TCS-7383.json) (TCS-7383) |
| 19 | 26 | 78 |  | [Sorting-bound external-memory breadth-first search](../../data/cards/TCS-7497.json) (TCS-7497) |
| 20 | 27 | 78 |  | [Sorting-bound external-memory weighted shortest paths](../../data/cards/TCS-7498.json) (TCS-7498) |
| 21 | 16 | 74 |  | [Constant-update working-set heaps on pointer machines](../../data/cards/TCS-0474.json) (TCS-0474) |
| 22 | 17 | 74 |  | [Buffered fully persistent search trees](../../data/cards/TCS-7327.json) (TCS-7327) |
| 23 | 14 | 74 |  | [Optimal randomized memory-reallocation overhead](../../data/cards/TCS-7340.json) (TCS-7340) |
| 24 | 18 | 70 |  | [Combined depth and size bounds for confluently persistent tries](../../data/cards/TCS-7330.json) (TCS-7330) |
| 25 | 22 | 70 |  | [Computing optimal generalized binary split trees](../../data/cards/TCS-7401.json) (TCS-7401) |
| 26 | 24 | 70 |  | [Fast insertion arbitrarily close to bucketized-cuckoo thresholds](../../data/cards/TCS-7491.json) (TCS-7491) |
| 27 | 23 | 64 |  | [Rank error of MultiQueues under unrestricted insertion orders](../../data/cards/TCS-7490.json) (TCS-7490) |

### Dynamic algorithms

Favor robustness under arbitrary updates for core graph primitives and general limits of dynamic expressiveness. Broader dynamic metatheorems precede improvements for a particular data representation.

| Rank | Previous | Score | Focus | Problem |
| ---: | ---: | ---: | :---: | --- |
| 1 | 1 | 94 | yes | [Deterministic fully dynamic connectivity with polylogarithmic worst-case updates](../../data/cards/TCS-6625.json) (TCS-6625) |
| 2 | 2 | 94 | yes | [Fully dynamic near-optimal matching with polylogarithmic updates](../../data/cards/TCS-6627.json) (TCS-6627) |
| 3 | 6 | 90 |  | [Dynamic APSP with edge-linear updates](../../data/cards/TCS-0478.json) (TCS-0478) |
| 4 | 3 | 90 |  | [Polylogarithmic worst-case updates for exact dynamic minimum spanning forests](../../data/cards/TCS-6626.json) (TCS-6626) |
| 5 | 4 | 90 |  | [Polylogarithmic maintenance of the exact global minimum cut](../../data/cards/TCS-6670.json) (TCS-6670) |
| 6 | 8 | 86 |  | [Near-linear incremental topological ordering](../../data/cards/TCS-7339.json) (TCS-7339) |
| 7 | 20 | 86 |  | [Polynomial-time query outside DynFO](../../data/cards/TCS-7437.json) (TCS-7437) |
| 8 | 22 | 86 |  | [Worst-case dynamic Courcelle theorem at bounded treewidth](../../data/cards/TCS-7494.json) (TCS-7494) |
| 9 | 23 | 86 |  | [Worst-case polylogarithmic fully dynamic planarity testing](../../data/cards/TCS-7495.json) (TCS-7495) |
| 10 | 10 | 82 |  | [Dynamic spanning trees with polylogarithmic average stretch](../../data/cards/TCS-0541.json) (TCS-0541) |
| 11 | 9 | 82 |  | [Polylogarithmic dynamic maximal matching against adaptive updates](../../data/cards/TCS-0543.json) (TCS-0543) |
| 12 | 5 | 82 |  | [Logarithmic Las Vegas dynamic connectivity](../../data/cards/TCS-7332.json) (TCS-7332) |
| 13 | 16 | 82 |  | [Fast constant-factor fully dynamic edit distance](../../data/cards/TCS-7387.json) (TCS-7387) |
| 14 | 18 | 82 |  | [Deterministic worst-case polylogarithmic dynamic 2-edge-connectivity](../../data/cards/TCS-7393.json) (TCS-7393) |
| 15 | 24 | 82 |  | [Polylogarithmic updates for the exact arboricity value](../../data/cards/TCS-7496.json) (TCS-7496) |
| 16 | 13 | 78 |  | [Logarithmic fully dynamic planar nearest neighbors](../../data/cards/TCS-0387.json) (TCS-0387) |
| 17 | 15 | 78 |  | [Subquadratic exact fully dynamic weighted single-source distances](../../data/cards/TCS-5209.json) (TCS-5209) |
| 18 | 7 | 78 |  | [Worst-case logarithmic dynamic planar convex hulls](../../data/cards/TCS-7326.json) (TCS-7326) |
| 19 | 19 | 78 |  | [DynProp maintenance of directed reachability](../../data/cards/TCS-7436.json) (TCS-7436) |
| 20 | 21 | 78 |  | [Polylogarithmic updates for bounded rank-width](../../data/cards/TCS-7492.json) (TCS-7492) |
| 21 | 28 | 78 |  | [Optimal-query fully dynamic text indexing](../../data/cards/TCS-7502.json) (TCS-7502) |
| 22 | 11 | 74 |  | [Dynamic edge coloring with sublinear additive slack](../../data/cards/TCS-0536.json) (TCS-0536) |
| 23 | 14 | 74 |  | [DynFO maintenance of red-predecessor parity](../../data/cards/TCS-3331.json) (TCS-3331) |
| 24 | 17 | 74 |  | [Deterministic \(\widetilde O(n^{5/2})\) worst-case dynamic APSP](../../data/cards/TCS-7392.json) (TCS-7392) |
| 25 | 27 | 74 |  | [Fast dynamic vertex colouring against adaptive updates](../../data/cards/TCS-7501.json) (TCS-7501) |
| 26 | 12 | 70 |  | [Low-loss deterministic reduction from weighted to unweighted dynamic matching](../../data/cards/TCS-0545.json) (TCS-0545) |
| 27 | 26 | 70 |  | [Fully dynamic linear programming with outliers](../../data/cards/TCS-7500.json) (TCS-7500) |
| 28 | 29 | 70 |  | [Logarithmic dynamic convex-hull line intersection queries](../../data/cards/TCS-7503.json) (TCS-7503) |
| 29 | 25 | 66 |  | [Faster approximate dynamic distances on monotone grids](../../data/cards/TCS-7499.json) (TCS-7499) |

### String algorithms and computational biology

Favor recovering strings from noise and fast comparison of sequences. General compression principles and metric structure precede specialized indexing tradeoffs.

| Rank | Previous | Score | Focus | Problem |
| ---: | ---: | ---: | :---: | --- |
| 1 | 1 | 94 | yes | [Worst-case sample complexity of trace reconstruction](../../data/cards/TCS-6623.json) (TCS-6623) |
| 2 | 2 | 94 | yes | [Constant-factor edit-distance approximation in \(O(n\operatorname{polylog} n)\) time](../../data/cards/TCS-6624.json) (TCS-6624) |
| 3 | 11 | 90 |  | [Constant-factor approximation of the smallest grammar](../../data/cards/TCS-6513.json) (TCS-6513) |
| 4 | 3 | 90 |  | [Almost-linear-time \((1+\varepsilon)\)-approximation of edit distance](../../data/cards/TCS-7235.json) (TCS-7235) |
| 5 | 13 | 90 |  | [Optimal \(\ell_{1}\) distortion of binary edit distance](../../data/cards/TCS-7297.json) (TCS-7297) |
| 6 | 5 | 86 |  | [Breaking two for sum-of-pairs multiple sequence alignment](../../data/cards/TCS-6669.json) (TCS-6669) |
| 7 | 4 | 86 |  | [Truly subquadratic \((1+\varepsilon)\)-approximation of edit distance](../../data/cards/TCS-7220.json) (TCS-7220) |
| 8 | 16 | 86 |  | [Optimal approximation ratio for shortest common superstring](../../data/cards/TCS-7322.json) (TCS-7322) |
| 9 | 6 | 86 |  | [Almost-linear constant-factor approximation of LCS](../../data/cards/TCS-7371.json) (TCS-7371) |
| 10 | 12 | 82 |  | [Linear-space encoding from smallest string attractors](../../data/cards/TCS-6928.json) (TCS-6928) |
| 11 | 7 | 82 |  | [Text-to-pattern Hamming distances below the square-root barrier](../../data/cards/TCS-7367.json) (TCS-7367) |
| 12 | 10 | 82 |  | [Almost-quadratic unweighted tree edit distance](../../data/cards/TCS-7374.json) (TCS-7374) |
| 13 | 20 | 78 |  | [Linear-space LZ77 random access](../../data/cards/TCS-0467.json) (TCS-0467) |
| 14 | 23 | 78 |  | [Linear-time LZ77 pattern matching](../../data/cards/TCS-0468.json) (TCS-0468) |
| 15 | 8 | 78 |  | [Linear-space k-mismatch indexing with fast queries](../../data/cards/TCS-7366.json) (TCS-7366) |
| 16 | 9 | 78 |  | [Space-query exponent curve of gapped string indexing](../../data/cards/TCS-7369.json) (TCS-7369) |
| 17 | 25 | 78 |  | [Fully functional suffix trees in BWT-run-linear total space](../../data/cards/TCS-7375.json) (TCS-7375) |
| 18 | 24 | 74 |  | [Grammar random access in \(O(g\log g)\) bits](../../data/cards/TCS-0470.json) (TCS-0470) |
| 19 | 17 | 74 |  | [Polyloglogarithmic suffix-array access in compact space](../../data/cards/TCS-7360.json) (TCS-7360) |
| 20 | 18 | 74 |  | [Preprocessing exponent of binary jumbled indexing](../../data/cards/TCS-7364.json) (TCS-7364) |
| 21 | 15 | 74 |  | [General-alphabet Hamming oracles with optimal preprocessing](../../data/cards/TCS-7365.json) (TCS-7365) |
| 22 | 26 | 70 |  | [Certifying Karp–Rabin fingerprints](../../data/cards/TCS-0466.json) (TCS-0466) |
| 23 | 22 | 70 |  | [Input-optimal construction of compact inverse suffix arrays](../../data/cards/TCS-7361.json) (TCS-7361) |
| 24 | 14 | 70 |  | [Optimal top-k document retrieval in compact space](../../data/cards/TCS-7362.json) (TCS-7362) |
| 25 | 19 | 70 |  | [Polynomial-time construction of minimum-density DNA minimizers](../../data/cards/TCS-7370.json) (TCS-7370) |
| 26 | 21 | 66 |  | [A fixed exponent improvement for elastic-degenerate string intersection](../../data/cards/TCS-7368.json) (TCS-7368) |

### Game theory, social choice and fair division

Favor whether fairness and truthful efficiency are achievable at all. Broad existence and black-box mechanism questions precede exact constants for specialized markets.

| Rank | Previous | Score | Focus | Problem |
| ---: | ---: | ---: | :---: | --- |
| 1 | 2 | 96 | yes | [Existence of complete EFX allocations for additive valuations](../../data/cards/TCS-0011.json) (TCS-0011) |
| 2 | 1 | 92 | yes | [Constant-factor universally truthful auctions for submodular bidders](../../data/cards/TCS-6632.json) (TCS-6632) |
| 3 | 3 | 88 |  | [Constant-factor approximation for Santa Claus](../../data/cards/TCS-6639.json) (TCS-6639) |
| 4 | 4 | 88 |  | [Randomized truthful unrelated-machine scheduling](../../data/cards/TCS-6674.json) (TCS-6674) |
| 5 | 23 | 88 |  | [Constant-factor truthful subadditive combinatorial auctions](../../data/cards/TCS-7507.json) (TCS-7507) |
| 6 | 26 | 88 |  | [Black-box conversion to dominant-strategy truthfulness without expected-welfare loss](../../data/cards/TCS-7510.json) (TCS-7510) |
| 7 | 12 | 84 |  | [Universal maximin-share approximation for additive goods](../../data/cards/TCS-0056.json) (TCS-0056) |
| 8 | 5 | 84 |  | [Polynomial query complexity of exact envy-free cake cutting](../../data/cards/TCS-6633.json) (TCS-6633) |
| 9 | 21 | 84 |  | [Constant-factor welfare from posted item prices](../../data/cards/TCS-7505.json) (TCS-7505) |
| 10 | 24 | 84 |  | [Constant price of stability for undirected network design](../../data/cards/TCS-7508.json) (TCS-7508) |
| 11 | 17 | 80 |  | [Pure positional Nash equilibria in reachability games](../../data/cards/TCS-0571.json) (TCS-0571) |
| 12 | 15 | 80 |  | [EF1 existence for arbitrary mixed-item utilities](../../data/cards/TCS-1108.json) (TCS-1108) |
| 13 | 14 | 80 |  | [EF1 and Pareto optimality for additive mixed items](../../data/cards/TCS-1109.json) (TCS-1109) |
| 14 | 13 | 80 |  | [Polynomial-time EF1 and Pareto-optimal goods allocation](../../data/cards/TCS-1115.json) (TCS-1115) |
| 15 | 10 | 80 |  | [Optimal universal approximation factor for EFX](../../data/cards/TCS-1116.json) (TCS-1116) |
| 16 | 8 | 80 |  | [Polynomial-time approximation of EFX](../../data/cards/TCS-7197.json) (TCS-7197) |
| 17 | 9 | 80 |  | [Multiplicative MMS guarantee for chores](../../data/cards/TCS-7200.json) (TCS-7200) |
| 18 | 16 | 76 |  | [Polynomial-time mixed equilibria in coordination polymatrix games](../../data/cards/TCS-0073.json) (TCS-0073) |
| 19 | 19 | 76 |  | [Nash equilibria in concurrent terminal-reward games](../../data/cards/TCS-4584.json) (TCS-4584) |
| 20 | 6 | 76 |  | [Randomized metric distortion in social choice](../../data/cards/TCS-6634.json) (TCS-6634) |
| 21 | 7 | 76 |  | [Polynomial-time EFX for three additive agents](../../data/cards/TCS-7196.json) (TCS-7196) |
| 22 | 11 | 76 |  | [Bounded protocols for connected envy-free proportional cake cutting](../../data/cards/TCS-7203.json) (TCS-7203) |
| 23 | 18 | 72 |  | [Polynomial-time stable matching in unimodular hypergraphs](../../data/cards/TCS-1714.json) (TCS-1714) |
| 24 | 20 | 72 |  | [Optimal truthful pricing from one sample](../../data/cards/TCS-7504.json) (TCS-7504) |
| 25 | 22 | 72 |  | [Optimal randomized truthful two-facility location](../../data/cards/TCS-7506.json) (TCS-7506) |
| 26 | 27 | 72 |  | [Optimal truthful approximation for multi-hospital kidney exchange](../../data/cards/TCS-7511.json) (TCS-7511) |
| 27 | 25 | 68 |  | [Sharp selfishness threshold for manipulation-resistant tournaments](../../data/cards/TCS-7509.json) (TCS-7509) |

### Algebraic computation

Favor the cost of basic algebraic computation and general lower-bound/derandomization barriers. Keep broad algebraic decidability questions high, while placing restricted circuit refinements below the central separations.

| Rank | Previous | Score | Focus | Problem |
| ---: | ---: | ---: | :---: | --- |
| 1 | 1 | 100 | yes | [Matrix multiplication exponent](../../data/cards/TCS-0007.json) (TCS-0007) |
| 2 | 5 | 100 | yes | [VP versus VNP](../../data/cards/TCS-0005.json) (TCS-0005) |
| 3 | 2 | 96 |  | [Permanent versus determinant](../../data/cards/TCS-6611.json) (TCS-6611) |
| 4 | 12 | 96 |  | [Derandomizing polynomial identity testing](../../data/cards/TCS-7113.json) (TCS-7113) |
| 5 | 4 | 92 |  | [VP versus VBP over the complex numbers](../../data/cards/TCS-6612.json) (TCS-6612) |
| 6 | 6 | 92 |  | [Polynomial-size arithmetic formulas for the determinant](../../data/cards/TCS-6613.json) (TCS-6613) |
| 7 | 9 | 92 |  | [Deterministic polynomial-time factorization over finite fields](../../data/cards/TCS-6614.json) (TCS-6614) |
| 8 | 3 | 92 |  | [Shub–Smale \(\tau\)-conjecture](../../data/cards/TCS-6666.json) (TCS-6666) |
| 9 | 8 | 92 |  | [Superpolynomial arithmetic formula lower bounds](../../data/cards/TCS-6888.json) (TCS-6888) |
| 10 | 46 | 88 |  | [Explicit univariate arithmetic circuit lower bounds](../../data/cards/TCS-0009.json) (TCS-0009) |
| 11 | 34 | 88 |  | [Superlinear constant-degree arithmetic circuit lower bounds](../../data/cards/TCS-0010.json) (TCS-0010) |
| 12 | 7 | 88 |  | [Word problem for one-relation monoids](../../data/cards/TCS-6641.json) (TCS-6641) |
| 13 | 16 | 88 |  | [Explicit three-dimensional tensors of superlinear rank](../../data/cards/TCS-6895.json) (TCS-6895) |
| 14 | 13 | 88 |  | [Bit complexity of integer multiplication](../../data/cards/TCS-7174.json) (TCS-7174) |
| 15 | 14 | 88 |  | [Strassen’s asymptotic rank conjecture](../../data/cards/TCS-7262.json) (TCS-7262) |
| 16 | 32 | 84 |  | [Sum-of-square-roots problem](../../data/cards/TCS-0055.json) (TCS-0055) |
| 17 | 28 | 84 |  | [Explicit rigidity at rank n over log log n](../../data/cards/TCS-1058.json) (TCS-1058) |
| 18 | 15 | 84 |  | [Polynomial-time finite-group isomorphism in the Cayley-table model](../../data/cards/TCS-6615.json) (TCS-6615) |
| 19 | 10 | 84 |  | [Conjugacy problem for one-relator groups](../../data/cards/TCS-6642.json) (TCS-6642) |
| 20 | 11 | 84 |  | [Isomorphism problem for one-relator groups](../../data/cards/TCS-6677.json) (TCS-6677) |
| 21 | 23 | 84 |  | [Superpolynomial noncommutative circuit lower bounds](../../data/cards/TCS-6890.json) (TCS-6890) |
| 22 | 24 | 84 |  | [Superpolynomial multilinear circuit lower bounds](../../data/cards/TCS-6893.json) (TCS-6893) |
| 23 | 17 | 84 |  | [Derandomizing black-box depth-four PIT](../../data/cards/TCS-6898.json) (TCS-6898) |
| 24 | 18 | 84 |  | [Unrestricted arithmetic lower bounds for the discrete Fourier transform](../../data/cards/TCS-7175.json) (TCS-7175) |
| 25 | 25 | 84 |  | [Linear-size circuits for integer multiplication](../../data/cards/TCS-7223.json) (TCS-7223) |
| 26 | 29 | 80 |  | [Decidability of freeness in automaton groups](../../data/cards/TCS-2039.json) (TCS-2039) |
| 27 | 56 | 80 |  | [Algebraic branching programs versus formulas](../../data/cards/TCS-2506.json) (TCS-2506) |
| 28 | 20 | 80 |  | [NP-hardness of PosSLP](../../data/cards/TCS-5520.json) (TCS-5520) |
| 29 | 43 | 80 |  | [Membership in \(2\times 2\) integer matrix semigroups](../../data/cards/TCS-5921.json) (TCS-5921) |
| 30 | 19 | 80 |  | [Uniform exact permanent circuits below base two](../../data/cards/TCS-6616.json) (TCS-6616) |
| 31 | 30 | 80 |  | [Multilinear versus general arithmetic circuits](../../data/cards/TCS-6883.json) (TCS-6883) |
| 32 | 27 | 80 |  | [Semantic versus syntactic multilinear circuits](../../data/cards/TCS-6884.json) (TCS-6884) |
| 33 | 21 | 80 |  | [Permanent lower bounds from black-box identity testing](../../data/cards/TCS-6897.json) (TCS-6897) |
| 34 | 31 | 80 |  | [Deterministic noncommutative circuit identity testing in polynomial size and degree](../../data/cards/TCS-6903.json) (TCS-6903) |
| 35 | 26 | 80 |  | [Optimal multilinear-formula size of the permanent](../../data/cards/TCS-7269.json) (TCS-7269) |
| 36 | 48 | 76 |  | [Polynomial-time feasibility of integer min-plus linear systems](../../data/cards/TCS-0046.json) (TCS-0046) |
| 37 | 22 | 76 |  | [Cubic min-plus circuit lower bounds for shortest paths](../../data/cards/TCS-0481.json) (TCS-0481) |
| 38 | 49 | 76 |  | [VP factor closure in positive characteristic](../../data/cards/TCS-1101.json) (TCS-1101) |
| 39 | 50 | 76 |  | [VBP factor closure in positive characteristic](../../data/cards/TCS-1102.json) (TCS-1102) |
| 40 | 38 | 76 |  | [Containment of presentable border VP in VNP over every field](../../data/cards/TCS-1103.json) (TCS-1103) |
| 41 | 42 | 76 |  | [Arithmetic circuit closure under pth roots](../../data/cards/TCS-3318.json) (TCS-3318) |
| 42 | 39 | 76 |  | [Explicit rigid matrices over low-degree number fields](../../data/cards/TCS-5260.json) (TCS-5260) |
| 43 | 33 | 76 |  | [Tensor orbit-closure intersection in \(\mathrm{NP}\cap\mathrm{coAM}\)](../../data/cards/TCS-6493.json) (TCS-6493) |
| 44 | 37 | 76 |  | [Homogeneous versus unrestricted arithmetic formulas](../../data/cards/TCS-6882.json) (TCS-6882) |
| 45 | 52 | 72 |  | [Exact Kronecker-polytope membership in polynomial time](../../data/cards/TCS-0047.json) (TCS-0047) |
| 46 | 47 | 72 |  | [Bounded-interval zero testing for exponential-trigonometric polynomials](../../data/cards/TCS-1151.json) (TCS-1151) |
| 47 | 44 | 72 |  | [A qAC⁰ versus NL-complete dichotomy for Cayley semigroup membership](../../data/cards/TCS-1544.json) (TCS-1544) |
| 48 | 58 | 72 |  | [Efficient equations for VP with unrestricted complex coefficients](../../data/cards/TCS-2958.json) (TCS-2958) |
| 49 | 35 | 72 |  | [Approximate polynomial satisfiability in AM under GRH](../../data/cards/TCS-3959.json) (TCS-3959) |
| 50 | 45 | 72 |  | [Polynomial-time dimension expansion over finite fields](../../data/cards/TCS-4523.json) (TCS-4523) |
| 51 | 36 | 72 |  | [Does explicit multivariate hardness imply univariate hardness over F₂?](../../data/cards/TCS-5240.json) (TCS-5240) |
| 52 | 41 | 72 |  | [Polynomial-time computation of addition-chain length](../../data/cards/TCS-7224.json) (TCS-7224) |
| 53 | 40 | 72 |  | [Linear-time unit-Monge distance multiplication](../../data/cards/TCS-7372.json) (TCS-7372) |
| 54 | 53 | 68 |  | [Efficient LRS evaluation](../../data/cards/TCS-0095.json) (TCS-0095) |
| 55 | 54 | 68 |  | [Does real Zariski-closure membership belong to ∃R?](../../data/cards/TCS-1069.json) (TCS-1069) |
| 56 | 55 | 68 |  | [Deterministic divisibility testing by a constant-degree polynomial](../../data/cards/TCS-2077.json) (TCS-2077) |
| 57 | 57 | 68 |  | [A uniform exponent saving for arbitrary generalized convolution](../../data/cards/TCS-2718.json) (TCS-2718) |
| 58 | 59 | 68 |  | [Uniform compressed word problem for graph groups](../../data/cards/TCS-4350.json) (TCS-4350) |
| 59 | 51 | 68 |  | [Polynomial-time sign testing of matrix powers in every fixed dimension](../../data/cards/TCS-4490.json) (TCS-4490) |
| 60 | 60 | 68 |  | [Collapse of rational recurrence systems to single recurrences](../../data/cards/TCS-5739.json) (TCS-5739) |

### Lattices and computational number theory

Favor computability of rational arithmetic and central number-theoretic algorithms. Broad lattice approximation and cryptographic foundations precede sharper constants in a particular reduction.

| Rank | Previous | Score | Focus | Problem |
| ---: | ---: | ---: | :---: | --- |
| 1 | 1 | 98 | yes | [Hilbert’s tenth problem over the rationals](../../data/cards/TCS-6571.json) (TCS-6571) |
| 2 | 3 | 96 | yes | [Integer factorization in randomized polynomial time](../../data/cards/TCS-6617.json) (TCS-6617) |
| 3 | 4 | 92 |  | [Prime-field discrete logarithms in randomized polynomial time](../../data/cards/TCS-6618.json) (TCS-6618) |
| 4 | 2 | 92 |  | [Polynomial-time, polynomial-factor approximation of Euclidean SVP](../../data/cards/TCS-6667.json) (TCS-6667) |
| 5 | 7 | 88 |  | [Vinogradov’s least quadratic nonresidue conjecture](../../data/cards/TCS-6620.json) (TCS-6620) |
| 6 | 8 | 88 |  | [Exact Euclidean SVP in BQP](../../data/cards/TCS-7169.json) (TCS-7169) |
| 7 | 5 | 88 |  | [Quantum polynomial-factor approximation of Euclidean SVP](../../data/cards/TCS-7234.json) (TCS-7234) |
| 8 | 12 | 88 |  | [Deterministic polynomial-time construction of a prime of a given bit length](../../data/cards/TCS-7265.json) (TCS-7265) |
| 9 | 19 | 84 |  | [Polynomial-factor Euclidean SVP hardness assuming NP is not contained in RP](../../data/cards/TCS-0655.json) (TCS-0655) |
| 10 | 9 | 84 |  | [Quantum-ETH hardness of cryptographic-factor GapSVP](../../data/cards/TCS-0658.json) (TCS-0658) |
| 11 | 6 | 84 |  | [Exact Euclidean SVP in single-exponential time and polynomial space](../../data/cards/TCS-6619.json) (TCS-6619) |
| 12 | 11 | 84 |  | [Polynomial-factor approximation of cyclotomic ideal SVP](../../data/cards/TCS-6863.json) (TCS-6863) |
| 13 | 16 | 80 |  | [A classical reduction from semiprime factoring to polynomial-gap SVP](../../data/cards/TCS-0656.json) (TCS-0656) |
| 14 | 10 | 80 |  | [A classical same-dimension reduction from SIVP to polynomial-modulus LWE](../../data/cards/TCS-6861.json) (TCS-6861) |
| 15 | 15 | 80 |  | [Classical ideal-SVP hardness of ring-LWE in power-of-two cyclotomic rings](../../data/cards/TCS-6864.json) (TCS-6864) |
| 16 | 18 | 80 |  | [Scholz–Brauer conjecture](../../data/cards/TCS-7170.json) (TCS-7170) |
| 17 | 17 | 80 |  | [Baillie–PSW pseudoprimes](../../data/cards/TCS-7171.json) (TCS-7171) |
| 18 | 22 | 76 |  | [NP-hardness of Euclidean unique SVP with a fixed gap greater than one](../../data/cards/TCS-0648.json) (TCS-0648) |
| 19 | 21 | 76 |  | [Dimension-preserving search-to-decision reductions for SVP](../../data/cards/TCS-0652.json) (TCS-0652) |
| 20 | 13 | 76 |  | [A classical SIS reduction from sublinear-factor GapSVP](../../data/cards/TCS-0659.json) (TCS-0659) |
| 21 | 14 | 76 |  | [NP-hardness of Euclidean covering radius](../../data/cards/TCS-5317.json) (TCS-5317) |
| 22 | 20 | 76 |  | [Downward self-reducibility of integer factoring](../../data/cards/TCS-5395.json) (TCS-5395) |
| 23 | 25 | 72 |  | [coNP certificates for GapSVP at the square-root n/log n scale](../../data/cards/TCS-0657.json) (TCS-0657) |
| 24 | 23 | 72 |  | [SVP hardness for fixed-rank cyclotomic modules](../../data/cards/TCS-0661.json) (TCS-0661) |
| 25 | 27 | 72 |  | [ETH hardness of constant-factor shortest-vector approximation for \(1\le p\le 2\)](../../data/cards/TCS-1170.json) (TCS-1170) |
| 26 | 26 | 68 |  | [A quantum 2^(0.2075n) lower bound for exact Euclidean SVP from QSETH](../../data/cards/TCS-0653.json) (TCS-0653) |
| 27 | 24 | 68 |  | [Unconditional exponential hardness of \(n^{1+\varepsilon}\)-GapSVP](../../data/cards/TCS-0662.json) (TCS-0662) |

### Coding and information theory

Favor fundamental coding tradeoffs and multiuser information limits. Local decoding and computability of capacity remain central; already-known approximation targets rank lower as research questions while remaining eligible formalization tasks.

| Rank | Previous | Score | Focus | Problem |
| ---: | ---: | ---: | :---: | --- |
| 1 | 2 | 98 | yes | [Optimal asymptotic binary rate–distance tradeoff](../../data/cards/TCS-1010.json) (TCS-1010) |
| 2 | 1 | 96 | yes | [Capacity of the two-user Gaussian interference channel](../../data/cards/TCS-6606.json) (TCS-6606) |
| 3 | 3 | 96 |  | [Capacity of the general broadcast channel](../../data/cards/TCS-6665.json) (TCS-6665) |
| 4 | 4 | 92 |  | [Li–Li conjecture](../../data/cards/TCS-6584.json) (TCS-6584) |
| 5 | 8 | 92 |  | [Capacity of the general two-user interference channel](../../data/cards/TCS-7210.json) (TCS-7210) |
| 6 | 6 | 92 |  | [Binary codes beyond the Gilbert–Varshamov bound](../../data/cards/TCS-7267.json) (TCS-7267) |
| 7 | 15 | 88 |  | [Polynomial-length constant-query locally decodable codes](../../data/cards/TCS-1020.json) (TCS-1020) |
| 8 | 7 | 88 |  | [Decidability of unconditional entropy inequalities](../../data/cards/TCS-6608.json) (TCS-6608) |
| 9 | 10 | 88 |  | [Constant-rate binary locally decodable codes with logarithmic query complexity](../../data/cards/TCS-6609.json) (TCS-6609) |
| 10 | 12 | 88 |  | [Shannon capacity of \(C_{7}\)](../../data/cards/TCS-6610.json) (TCS-6610) |
| 11 | 13 | 88 |  | [Capacity of the general two-way channel](../../data/cards/TCS-7211.json) (TCS-7211) |
| 12 | 14 | 88 |  | [Computability of graph Shannon capacity](../../data/cards/TCS-7215.json) (TCS-7215) |
| 13 | 16 | 84 |  | [Efficient explicit constant-rate tree codes](../../data/cards/TCS-0013.json) (TCS-0013) |
| 14 | 17 | 84 |  | [Explicit binary codes with efficient list decoding up to capacity](../../data/cards/TCS-1012.json) (TCS-1012) |
| 15 | 9 | 84 |  | [Positive-rate binary codes against adversarial deletions](../../data/cards/TCS-4524.json) (TCS-4524) |
| 16 | 20 | 84 |  | [Do nonlinear binary codes have a strictly better asymptotic rate?](../../data/cards/TCS-4968.json) (TCS-4968) |
| 17 | 18 | 84 |  | [Linear-length locally testable proofs for CircuitSAT](../../data/cards/TCS-6738.json) (TCS-6738) |
| 18 | 11 | 84 |  | [Rate–distortion tradeoff for distributed lossy source coding](../../data/cards/TCS-7214.json) (TCS-7214) |
| 19 | 22 | 80 |  | [Polyhedrality of linear-rank inequality cones](../../data/cards/TCS-0196.json) (TCS-0196) |
| 20 | 21 | 80 |  | [Full-length Reed–Solomon list decoding beyond Johnson](../../data/cards/TCS-1011.json) (TCS-1011) |
| 21 | 25 | 76 |  | [Entropic matroid approximations approaching unit ratio](../../data/cards/TCS-0184.json) (TCS-0184) |
| 22 | 19 | 76 |  | [Explicit positive-rate codes below the Plotkin point](../../data/cards/TCS-3513.json) (TCS-3513) |
| 23 | 23 | 76 |  | [The maximal error fraction for constant-rate binary two-way codes](../../data/cards/TCS-4802.json) (TCS-4802) |
| 24 | 24 | 72 |  | [Bounded-alphabet approximation of the β = 0 entropy face](../../data/cards/TCS-0178.json) (TCS-0178) |
| 25 | 26 | 72 |  | [Are characteristic sets of linear-rank inequalities finite or cofinite?](../../data/cards/TCS-0187.json) (TCS-0187) |
| 26 | 27 | 72 |  | [The infimal normalized Ingleton score](../../data/cards/TCS-0205.json) (TCS-0205) |
| 27 | 5 | 60 |  | [Capacity of the binary deletion channel](../../data/cards/TCS-6607.json) (TCS-6607) |

### Property testing and distribution learning

Favor general characterizations of what can be learned from local access and the gap between testing and estimation. Strong structural properties follow before specialized query-model refinements.

| Rank | Previous | Score | Focus | Problem |
| ---: | ---: | ---: | :---: | --- |
| 1 | 1 | 92 | yes | [Effective classification of polynomially testable hereditary graph properties](../../data/cards/TCS-6630.json) (TCS-6630) |
| 2 | 2 | 92 | yes | [Polynomial testability versus distance estimation](../../data/cards/TCS-1033.json) (TCS-1033) |
| 3 | 6 | 88 |  | [Sharp graph-removal bounds for fixed patterns](../../data/cards/TCS-1029.json) (TCS-1029) |
| 4 | 7 | 88 |  | [Polynomial-time density learning of Gaussian mixtures](../../data/cards/TCS-5443.json) (TCS-5443) |
| 5 | 11 | 84 |  | [Polynomial-query submodularity testing](../../data/cards/TCS-0848.json) (TCS-0848) |
| 6 | 5 | 84 |  | [Planar graphs from local neighborhoods](../../data/cards/TCS-4376.json) (TCS-4376) |
| 7 | 3 | 84 |  | [Sublinear testing of bounded-degree graph isomorphism](../../data/cards/TCS-6672.json) (TCS-6672) |
| 8 | 17 | 84 |  | [Complexity of tolerant monotonicity testing](../../data/cards/TCS-7384.json) (TCS-7384) |
| 9 | 4 | 80 |  | [Polynomial testing of induced four-cycle freeness](../../data/cards/TCS-1030.json) (TCS-1030) |
| 10 | 8 | 80 |  | [Query complexity of Max-CSP testing](../../data/cards/TCS-5085.json) (TCS-5085) |
| 11 | 18 | 80 |  | [Efficient black-box testing of high-dimensional convexity](../../data/cards/TCS-7385.json) (TCS-7385) |
| 12 | 20 | 80 |  | [Estimating sparse finite-field matrix rank with sublinear queries](../../data/cards/TCS-7396.json) (TCS-7396) |
| 13 | 14 | 76 |  | [Efficient characterization of instance-optimal identity testing](../../data/cards/TCS-0672.json) (TCS-0672) |
| 14 | 15 | 76 |  | [A dimension-free directed \(\mathrm{L}^{1}\) Poincaré inequality](../../data/cards/TCS-2535.json) (TCS-2535) |
| 15 | 9 | 76 |  | [Sample complexity of symmetric Markov-chain identity testing](../../data/cards/TCS-3906.json) (TCS-3906) |
| 16 | 19 | 76 |  | [Polynomial accuracy dependence for sublinear LIS estimation](../../data/cards/TCS-7395.json) (TCS-7395) |
| 17 | 12 | 72 |  | [Query complexity of conditional equivalence testing](../../data/cards/TCS-0841.json) (TCS-0841) |
| 18 | 13 | 72 |  | [Query complexity of directed acyclicity testing with bidirectional access](../../data/cards/TCS-0847.json) (TCS-0847) |
| 19 | 16 | 72 |  | [Optimal query cost of reducing testing adaptivity](../../data/cards/TCS-4259.json) (TCS-4259) |
| 20 | 10 | 72 |  | [Polylogarithmic-query pattern-freeness testing](../../data/cards/TCS-5210.json) (TCS-5210) |

### Differential privacy

Favor general private learnability and the computational limits of releasing rich statistical information. Sequential privacy costs remain important but follow these broader boundaries.

| Rank | Previous | Score | Focus | Problem |
| ---: | ---: | ---: | :---: | --- |
| 1 | 1 | 92 | yes | [Private PAC sample complexity from VC and Littlestone dimensions](../../data/cards/TCS-0506.json) (TCS-0506) |
| 2 | 3 | 88 | yes | [Polynomial-time private release of all marginals](../../data/cards/TCS-7236.json) (TCS-7236) |
| 3 | 2 | 84 |  | [Optimal error for pure-DP continual counting](../../data/cards/TCS-6673.json) (TCS-6673) |
| 4 | 5 | 84 |  | [Additive privacy cost for adversarial bandits](../../data/cards/TCS-7390.json) (TCS-7390) |
| 5 | 4 | 78 |  | [Optimal regret for private stochastic online learning](../../data/cards/TCS-0507.json) (TCS-0507) |
| 6 | 6 | 74 |  | [Optimal private sample complexity for nonsmooth nonconvex optimization](../../data/cards/TCS-7391.json) (TCS-7391) |

### Constraint satisfaction

Favor general tractability classifications and the elementary promise of coloring an already three-colorable graph. Structural explanations and search/decision equivalences precede more restricted meta-problems.

| Rank | Previous | Score | Focus | Problem |
| ---: | ---: | ---: | :---: | --- |
| 1 | 1 | 96 | yes | [Finite-domain promise CSP dichotomy](../../data/cards/TCS-6635.json) (TCS-6635) |
| 2 | 3 | 94 | yes | [Constant-colour polynomial-time colouring of 3-colourable graphs](../../data/cards/TCS-6637.json) (TCS-6637) |
| 3 | 2 | 92 |  | [Bodirsky–Pinsker conjecture](../../data/cards/TCS-6636.json) (TCS-6636) |
| 4 | 4 | 86 |  | [Search-to-decision equivalence for finite promise CSPs](../../data/cards/TCS-6675.json) (TCS-6675) |
| 5 | 5 | 86 |  | [Logarithmic-color approximation of 3-colorable graphs](../../data/cards/TCS-6725.json) (TCS-6725) |
| 6 | 6 | 86 |  | [Hardness of 6-coloring 3-colorable graphs](../../data/cards/TCS-7237.json) (TCS-7237) |
| 7 | 7 | 82 |  | [NP-intermediate \(\omega\)-categorical CSPs](../../data/cards/TCS-1173.json) (TCS-1173) |
| 8 | 13 | 82 |  | [Dichotomy for finite-domain restricted CSPs](../../data/cards/TCS-1807.json) (TCS-1807) |
| 9 | 10 | 82 |  | [Boolean decision-Holant dichotomy](../../data/cards/TCS-6748.json) (TCS-6748) |
| 10 | 12 | 82 |  | [Universal representation of NP by \(\omega\)-categorical CSPs](../../data/cards/TCS-7116.json) (TCS-7116) |
| 11 | 16 | 78 |  | [Common polynomial exponent for tractable digraph CSPs](../../data/cards/TCS-0504.json) (TCS-0504) |
| 12 | 8 | 78 |  | [VCSP tractability over the countable random graph](../../data/cards/TCS-1555.json) (TCS-1555) |
| 13 | 14 | 78 |  | [Search tractability of BLP-solvable promise CSPs](../../data/cards/TCS-1978.json) (TCS-1978) |
| 14 | 9 | 78 |  | [Super-log-logarithmic colouring hardness for two-colourable triple systems](../../data/cards/TCS-3984.json) (TCS-3984) |
| 15 | 15 | 74 |  | [Characterizing CSP languages with linear non-redundancy](../../data/cards/TCS-0441.json) (TCS-0441) |
| 16 | 17 | 74 |  | [Polynomial kernels for Boolean MinCSP](../../data/cards/TCS-0444.json) (TCS-0444) |
| 17 | 11 | 74 |  | [Exact exponential-time equivalence for nonnegative Boolean Max-CSP](../../data/cards/TCS-3585.json) (TCS-3585) |
| 18 | 18 | 74 |  | [Polynomial-time tractability testing for core crisp CSP languages](../../data/cards/TCS-3678.json) (TCS-3678) |

### Automated reasoning, rewriting and unification

Favor the basic decidability and complexity of symbolic equations. General rewriting and unification principles follow; implementation-level refinements of restricted representations come later.

| Rank | Previous | Score | Focus | Problem |
| ---: | ---: | ---: | :---: | --- |
| 1 | 1 | 94 | yes | [Word equations with linear length constraints](../../data/cards/TCS-6562.json) (TCS-6562) |
| 2 | 8 | 90 | yes | [NP membership of word-equation satisfiability](../../data/cards/TCS-0163.json) (TCS-0163) |
| 3 | 3 | 86 |  | [Decidability of Presburger arithmetic with primes](../../data/cards/TCS-1992.json) (TCS-1992) |
| 4 | 2 | 86 |  | [Decidability of unification in the basic modal logic K](../../data/cards/TCS-6643.json) (TCS-6643) |
| 5 | 6 | 86 |  | [Decidability of termination for one-rule string rewriting](../../data/cards/TCS-6644.json) (TCS-6644) |
| 6 | 7 | 82 |  | [Singly exponential shortest solutions of word equations](../../data/cards/TCS-7194.json) (TCS-7194) |
| 7 | 5 | 82 |  | [Greedy CDCL without restarts versus resolution](../../data/cards/TCS-7239.json) (TCS-7239) |
| 8 | 15 | 82 |  | [Madlener–Otto plain-group conjecture](../../data/cards/TCS-7405.json) (TCS-7405) |
| 9 | 16 | 82 |  | [NP membership of context unification](../../data/cards/TCS-7411.json) (TCS-7411) |
| 10 | 9 | 78 |  | [Decidability of fifth-order \(\beta\)-matching](../../data/cards/TCS-1595.json) (TCS-1595) |
| 11 | 4 | 78 |  | [Deterministic polynomial-time equivalence testing for d-DNNFs](../../data/cards/TCS-6650.json) (TCS-6650) |
| 12 | 11 | 78 |  | [Two-sided distributive unification with a unit](../../data/cards/TCS-7125.json) (TCS-7125) |
| 13 | 19 | 78 |  | [Probabilistic Newman lemma with ordinary local confluence](../../data/cards/TCS-7424.json) (TCS-7424) |
| 14 | 12 | 74 |  | [Decidability of subsequence constraints with regular domains](../../data/cards/TCS-0114.json) (TCS-0114) |
| 15 | 10 | 74 |  | [Polynomial-time equivalence of free binary decision diagrams](../../data/cards/TCS-7134.json) (TCS-7134) |
| 16 | 20 | 74 |  | [Perpetual reduction for the \(\lambda\sigma\) calculus](../../data/cards/TCS-7434.json) (TCS-7434) |
| 17 | 13 | 70 |  | [Polynomial-time complementation of d-DNNFs](../../data/cards/TCS-0306.json) (TCS-0306) |
| 18 | 14 | 70 |  | [Polynomial-time recognition of abelian cores](../../data/cards/TCS-5603.json) (TCS-5603) |
| 19 | 18 | 70 |  | [Near-linear equivalence testing for propositional Horn theories](../../data/cards/TCS-7421.json) (TCS-7421) |
| 20 | 17 | 66 |  | [Recognizing minimally false quantified formulas of fixed deficiency](../../data/cards/TCS-7420.json) (TCS-7420) |

### Database theory and finite model theory

Favor a syntax for efficient computation and structural characterizations of tractable model checking. General query semantics and enumeration principles precede specialized representation gaps.

| Rank | Previous | Score | Focus | Problem |
| ---: | ---: | ---: | :---: | --- |
| 1 | 3 | 98 | yes | [A logic capturing polynomial time](../../data/cards/TCS-7195.json) (TCS-7195) |
| 2 | 1 | 92 | yes | [FO model checking on hereditary monadically dependent graph classes](../../data/cards/TCS-6678.json) (TCS-6678) |
| 3 | 4 | 92 |  | [Asser’s problem](../../data/cards/TCS-7232.json) (TCS-7232) |
| 4 | 7 | 88 |  | [A logic capturing logarithmic space](../../data/cards/TCS-3631.json) (TCS-3631) |
| 5 | 2 | 88 |  | [Constant-delay conjunctive-query classification](../../data/cards/TCS-6645.json) (TCS-6645) |
| 6 | 6 | 84 |  | [Conjunctive-query containment under bag semantics](../../data/cards/TCS-0492.json) (TCS-0492) |
| 7 | 5 | 84 |  | [Decidability of conjunctive-query entailment in SROIQ](../../data/cards/TCS-6680.json) (TCS-6680) |
| 8 | 20 | 84 |  | [Fagin’s binary-relation spectrum problem](../../data/cards/TCS-7415.json) (TCS-7415) |
| 9 | 21 | 84 |  | [Effective syntax for order-invariant first-order queries](../../data/cards/TCS-7422.json) (TCS-7422) |
| 10 | 9 | 80 |  | [Computability of entropic query-size bounds](../../data/cards/TCS-0488.json) (TCS-0488) |
| 11 | 14 | 80 |  | [BDD/FC conjecture](../../data/cards/TCS-0494.json) (TCS-0494) |
| 12 | 8 | 80 |  | [Successor-invariant first-order model checking on nowhere dense graphs](../../data/cards/TCS-4458.json) (TCS-4458) |
| 13 | 19 | 80 |  | [Cai–Fürer–Immerman definability in choiceless polynomial time](../../data/cards/TCS-6372.json) (TCS-6372) |
| 14 | 22 | 80 |  | [Eliminating an invariant order on bounded-degree structures](../../data/cards/TCS-7429.json) (TCS-7429) |
| 15 | 10 | 76 |  | [Linear-round convergence over stable semirings](../../data/cards/TCS-0482.json) (TCS-0482) |
| 16 | 15 | 76 |  | [Graph homomorphism parameterized by both treewidths](../../data/cards/TCS-0499.json) (TCS-0499) |
| 17 | 17 | 76 |  | [Uniform reliability of homomorphism-closed queries](../../data/cards/TCS-0505.json) (TCS-0505) |
| 18 | 11 | 76 |  | [Entropic width versus submodular width](../../data/cards/TCS-4995.json) (TCS-4995) |
| 19 | 12 | 72 |  | [Complexity of polymatroid query-size bounds](../../data/cards/TCS-0487.json) (TCS-0487) |
| 20 | 16 | 72 |  | [Tractable probability without polynomial-size deterministic decomposable lineage](../../data/cards/TCS-0502.json) (TCS-0502) |
| 21 | 18 | 72 |  | [Does extension preservation eliminate stratified intensional negation?](../../data/cards/TCS-3557.json) (TCS-3557) |
| 22 | 13 | 72 |  | [Unconditional constant-delay lower bound for the two-step query](../../data/cards/TCS-7128.json) (TCS-7128) |

### Miscellaneous

Both are compact, striking combinatorial conjectures. Prefer the sunflower question for its broader complexity connections, followed by the balanced-comparison principle for partial orders.

| Rank | Previous | Score | Focus | Problem |
| ---: | ---: | ---: | :---: | --- |
| 1 | 2 | 94 | yes | [Sunflower conjecture](../../data/cards/TCS-7290.json) (TCS-7290) |
| 2 | 1 | 88 | yes | [\(1/3\)–\(2/3\) conjecture](../../data/cards/TCS-7177.json) (TCS-7177) |
