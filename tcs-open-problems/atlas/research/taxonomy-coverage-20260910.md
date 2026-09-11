# Coverage of the agreed 10 + 25 proposal against original categories

Date: 2026-09-10. Read-only taxonomy assessment; no UI categories, assignments or records were changed.
Compared with the conversation proposal, including geometry/metric spaces, ADS, Optimization and numerics (subsequent user rename), the merged string/bioinformatics category, Knowledge representation and reasoning, mechanism design, and Boolean function analysis. The UI still contains an older revision.

Input: 6,513 current records, grouped using original_area (43 categories). Baseline: 4,695 records in output/catalog.json. Current catalog SHA-256: 62d8bea3ac908f5cce947c9f07785d2c078834073e63c3da4419a3c86eeb4481.
Counts are record counts, not verified distinct open problems. Original labels are heuristic and sometimes incorrect. No fine-grained subcategory field exists; thematic subsets below were located by text signatures and inspected by saved titles/excerpts.

## Main findings

- Subsequent user decisions (2026-09-10): merge Computational social choice into Algorithmic game theory, mechanism design and fair division, and Computational topology into Computational geometry and metric spaces. Structural graph theory has now been added as a small category of 20, filling one of the two freed slots; one slot remains vacant. See [CATEGORY_PLAN.md](../CATEGORY_PLAN.md).
- General combinatorics remains largely excluded, with selected edge cases in a suitable category or Miscellaneous. The user reversed the exclusion of structural graph theory within the accepted TCS-oriented scope. See [SELECTION_POLICY.md](../SELECTION_POLICY.md). Counts below remain historical observations.
- Structural/extremal graph theory and combinatorics were the clearest uncovered scope in the initial comparison. Neither all 118 combinatorics records nor all 628 graph records should be counted as excluded: those labels also contain algorithmic work and classification errors.
- Combinatorial games/puzzles and molecular computing/self-assembly have no clearly advertised specialist home. They can be assigned to broader complexity, algorithms, verification or distributed categories if that scope is intentional.
- The user has resolved the numerical-scope naming issue by renaming large category 10 to **Optimization and numerics** (50 problems). Numerical algorithms, online algorithms and bandits remain in its agreed scope. Temporal graph algorithms remain covered broadly under ADS without an explicit specialist label.
- Current Miscellaneous contains 315 records (247 from General algorithm design; 68 from Combinatorics and graph polynomials), under the older UI classifier. This is not a count of topics uncovered by the new proposal.

## All original categories

| Original area | Current pool | 4,695-record baseline | Destination in latest proposal | Assessment |
|---|---:|---:|---|---|
| Graph theory and graph algorithms | 628 | 460 | Algorithms & data structures; Dynamic graph algorithms; Structural graph theory | Algorithmic work covered; structural bounds and characterizations now have an accepted small category within its defined scope. |
| Computational geometry | 422 | 356 | Computational geometry and metric spaces | Covered. |
| Parameterized and exact algorithms | 422 | 336 | Parameterized and exact algorithms | Covered; large original pool now has a target of 20. |
| Quantum computation | 391 | 181 | Quantum computation | Covered. |
| Learning theory | 359 | 265 | Learning theory | Covered. |
| Automata and formal languages | 298 | 239 | Automata and formal languages | Covered. |
| Computational and circuit complexity | 295 | 189 | Computational complexity; Communication complexity and Boolean function analysis | Covered; shortening the name does not remove circuits. |
| General algorithm design | 294 | 216 | Algorithms & data structures; specialist categories; Miscellaneous | An old catch-all, not one missing discipline. Inspect individual records. |
| Approximation algorithms | 274 | 195 | Approximation algorithms and hardness of approximation | Covered. |
| Distributed and local algorithms | 234 | 178 | Distributed, parallel and sublinear algorithms | Covered; programmable matter may need explicit scope. |
| Data structures and compressed data | 209 | 136 | Algorithms & data structures; String algorithms and bioinformatics | Covered; retain compression in the agreed scope. |
| Online algorithms, bandits and stochastic optimization | 196 | 124 | Optimization and numerics | Explicitly absorbed; preserved through the rename. |
| Games, synthesis and verification | 171 | 131 | Semantics, logic and verification | Verification games covered. Combinatorial games/puzzles deserve separate attention. |
| Rewriting, lambda calculus and semantics | 169 | 144 | Semantics, logic and verification | Covered. |
| Cryptography | 147 | 76 | Cryptography | Covered. |
| Streaming and sketching | 128 | 102 | Distributed, parallel and sublinear algorithms | Covered. |
| Proof complexity and logic | 123 | 78 | Proof complexity; Semantics, logic and verification; Knowledge representation and reasoning | Covered after distinguishing proof complexity from other logical topics. |
| Combinatorics and graph polynomials | 118 | 85 | Structural graph theory where in scope; selected exceptions in other categories or Miscellaneous | General combinatorics remains largely excluded. The new Structural graph theory category covers its agreed scope, not this entire noisy original label. |
| Database theory and finite model theory | 115 | 96 | Database theory and finite model theory; Knowledge representation and reasoning | Covered. |
| Algebraic and numerical computation | 111 | 75 | Algebraic computation; Optimization and numerics | Covered; the user has made numerical computation explicit in the large category name. |
| Pseudorandomness and derandomization | 108 | 78 | Pseudorandomness and derandomization | Covered. |
| Optimization and mathematical programming | 102 | 65 | Optimization and numerics | Covered. |
| Coding and information theory | 100 | 61 | Coding and information theory | Covered. |
| Algorithmic game theory and fair division | 99 | 75 | Algorithmic game theory, mechanism design and fair division | Covered, including social choice after its standalone small category was merged. |
| Computability and algorithmic information | 99 | 92 | Computability and algorithmic information | Covered. |
| Enumeration and counting | 90 | 65 | Counting and enumeration; Randomized algorithms and sampling | Covered. |
| Algorithms for biological structures | 89 | 82 | String algorithms and bioinformatics | Sequence/phylogenetic work covered; artificial self-assembly is less clearly included. Original classification also contains unrelated records. |
| Automated reasoning and unification | 85 | 70 | Automated reasoning and unification; Knowledge representation and reasoning | Covered. |
| Property testing and distribution learning | 77 | 45 | Property testing and distribution learning; Distributed, parallel and sublinear algorithms | Covered; specialist bucket can take priority. |
| Communication complexity | 76 | 47 | Communication complexity and Boolean function analysis | Covered. |
| Scheduling and packing | 76 | 60 | Scheduling and packing | Covered. |
| Computational topology | 75 | 59 | Computational geometry and metric spaces | Covered; user explicitly merged the standalone topology category into large geometry. |
| Constraint satisfaction | 66 | 46 | Constraint satisfaction | Covered. |
| Infinite-state systems and verification | 46 | 39 | Semantics, logic and verification | Covered. |
| Fine-grained complexity | 43 | 30 | Fine-grained complexity | Covered. |
| Dynamic graph algorithms | 42 | 30 | Dynamic graph algorithms | Covered. |
| Lattices and computational number theory | 36 | 29 | Lattices and computational number theory | Covered. |
| Temporal graph algorithms | 36 | 30 | Algorithms & data structures | Covered broadly, but temporal graphs are not automatically the same subject as dynamic graph data structures. |
| Average-case complexity | 25 | 4 | Computational complexity | Covered; average-case algorithms can also use Randomized algorithms and sampling. |
| Differential privacy | 22 | 10 | Differential privacy | Covered. |
| Existential theory of the reals | 12 | 11 | Computational complexity; Computational geometry and metric spaces; Algebraic computation | Covered, with cross-cutting assignments. |
| Information-based complexity and numerical algorithms | 4 | 4 | Optimization and numerics; Computability and algorithmic information | Included in the explicit numerical scope. |
| Randomized search and optimization | 1 | 1 | Optimization and numerics; Randomized algorithms and sampling | Covered. |

## Topic subsets with inspected record lists

These are non-exhaustive candidate subsets, not an authoritative reclassification or deduplication. Source-title counts collapse identical saved titles, not all bibliographic variants. Excluded game matches: TCS-4321 (Grundy graph coloring) and TCS-4521 (online experts/quantile methods).

### Molecular computing and self-assembly: 14 records, 11 distinct saved source titles

| Record | Original category | Source title |
|---|---|---|
| [TCS-0527](http://localhost:8766/?view=compact#TCS-0527) | Distributed and local algorithms | Algorithmic Foundations of Programmable Matter |
| [TCS-1330](http://localhost:8766/?view=compact#TCS-1330) | Distributed and local algorithms | No Time to Interact: Simulating Population Protocols at Scale |
| [TCS-1588](http://localhost:8766/?view=compact#TCS-1588) | Distributed and local algorithms | Robust Predicate and Function Computation in Continuous Chemical Reaction Networks |
| [TCS-1836](http://localhost:8766/?view=compact#TCS-1836) | Automata and formal languages | Fractals in Seeded Tile Automata |
| [TCS-1951](http://localhost:8766/?view=compact#TCS-1951) | Graph theory and graph algorithms | The Computational Power of Discrete Chemical Reaction Networks with Bounded Executions |
| [TCS-2755](http://localhost:8766/?view=compact#TCS-2755) | Automata and formal languages | Building Squares with Optimal State Complexity in Restricted Active Self-Assembly |
| [TCS-2893](http://localhost:8766/?view=compact#TCS-2893) | Games, synthesis and verification | Unique Assembly Verification in Two-Handed Self-Assembly |
| [TCS-3036](http://localhost:8766/?view=compact#TCS-3036) | Games, synthesis and verification | Covert Computation in Staged Self-Assembly: Verification Is PSPACE-Complete |
| [TCS-3738](http://localhost:8766/?view=compact#TCS-3738) | Cryptography | Covert Computation in Self-Assembled Circuits |
| [TCS-4066](http://localhost:8766/?view=compact#TCS-4066) | Algorithms for biological structures | Self-Assembly of Any Shape with Constant Tile Types using High Temperature |
| [TCS-4105](http://localhost:8766/?view=compact#TCS-4105) | Algorithms for biological structures | Tilt Assembly: Algorithms for Micro-Factories that Build Objects with Uniform External Forces |
| [TCS-5853](http://localhost:8766/?view=compact#TCS-5853) | Scheduling and packing | Tilt Assembly: Algorithms for Micro-Factories that Build Objects with Uniform External Forces |
| [TCS-5897](http://localhost:8766/?view=compact#TCS-5897) | Algorithms for biological structures | Building Squares with Optimal State Complexity in Restricted Active Self-Assembly |
| [TCS-6184](http://localhost:8766/?view=compact#TCS-6184) | Graph theory and graph algorithms | Robust Predicate and Function Computation in Continuous Chemical Reaction Networks |

### Combinatorial games and puzzles: 31 records, 21 distinct saved source titles

| Record | Original category | Source title |
|---|---|---|
| [TCS-1233](http://localhost:8766/?view=compact#TCS-1233) | General algorithm design | Tetris Is Hard with Just One Piece Type |
| [TCS-1332](http://localhost:8766/?view=compact#TCS-1332) | General algorithm design | Hive Is PSPACE-Hard |
| [TCS-1375](http://localhost:8766/?view=compact#TCS-1375) | Parameterized and exact algorithms | On the Complexity of the Maker-Breaker Happy Vertex Game |
| [TCS-1814](http://localhost:8766/?view=compact#TCS-1814) | Combinatorics and graph polynomials | On the Complexity of Client-Waiter and Waiter-Client Games |
| [TCS-2087](http://localhost:8766/?view=compact#TCS-2087) | Online algorithms, bandits and stochastic optimization | Tetris Is Not Competitive |
| [TCS-2123](http://localhost:8766/?view=compact#TCS-2123) | General algorithm design | Poset Positional Games |
| [TCS-2182](http://localhost:8766/?view=compact#TCS-2182) | Combinatorics and graph polynomials | PackIt!: Gamified Rectangle Packing |
| [TCS-2183](http://localhost:8766/?view=compact#TCS-2183) | General algorithm design | You Can't Solve These Super Mario Bros. Levels: Undecidable Mario Games |
| [TCS-2184](http://localhost:8766/?view=compact#TCS-2184) | General algorithm design | Tetris with Few Piece Types |
| [TCS-2261](http://localhost:8766/?view=compact#TCS-2261) | Combinatorics and graph polynomials | How Did They Design This Game? Swish: Complexity and Unplayable Positions |
| [TCS-2793](http://localhost:8766/?view=compact#TCS-2793) | Learning theory | Chess Is Hard Even for a Single Player |
| [TCS-2818](http://localhost:8766/?view=compact#TCS-2818) | Combinatorics and graph polynomials | Solving and Generating Nagareru Puzzles |
| [TCS-3046](http://localhost:8766/?view=compact#TCS-3046) | General algorithm design | Magic: The Gathering Is Turing Complete |
| [TCS-3095](http://localhost:8766/?view=compact#TCS-3095) | General algorithm design | 6-Uniform Maker-Breaker Game Is PSPACE-Complete |
| [TCS-3308](http://localhost:8766/?view=compact#TCS-3308) | General algorithm design | Strategy-Stealing Is Non-Constructive |
| [TCS-3359](http://localhost:8766/?view=compact#TCS-3359) | Automata and formal languages | Recursed Is Not Recursive: A Jarring Result |
| [TCS-4037](http://localhost:8766/?view=compact#TCS-4037) | Combinatorics and graph polynomials | SUPERSET: A (Super)Natural Variant of the Card Game SET |
| [TCS-4398](http://localhost:8766/?view=compact#TCS-4398) | General algorithm design | Super Mario Bros. is Harder/Easier Than We Thought |
| [TCS-5012](http://localhost:8766/?view=compact#TCS-5012) | Combinatorics and graph polynomials | On the Complexity of Client-Waiter and Waiter-Client Games |
| [TCS-6488](http://localhost:8766/?view=compact#TCS-6488) | Graph theory and graph algorithms | Winning the War by (Strategically) Losing Battles: Settling the Complexity of Grundy-Values in Undirected Geography |
| [TCS-5486](http://localhost:8766/?view=compact#TCS-5486) | Computational and circuit complexity | PSPACE-Hard 2D Super Mario Games: Thirteen Doors |
| [TCS-5650](http://localhost:8766/?view=compact#TCS-5650) | Computational geometry | Computational Complexity of Swish Is Solved |
| [TCS-5662](http://localhost:8766/?view=compact#TCS-5662) | Computational and circuit complexity | Tetris with Few Piece Types |
| [TCS-5790](http://localhost:8766/?view=compact#TCS-5790) | Computational and circuit complexity | Super Mario Bros. is Harder/Easier Than We Thought |
| [TCS-5805](http://localhost:8766/?view=compact#TCS-5805) | General algorithm design | Tetris Is Hard with Just One Piece Type |
| [TCS-5868](http://localhost:8766/?view=compact#TCS-5868) | General algorithm design | Recursed Is Not Recursive: A Jarring Result |
| [TCS-5996](http://localhost:8766/?view=compact#TCS-5996) | General algorithm design | Chess Is Hard Even for a Single Player |
| [TCS-6005](http://localhost:8766/?view=compact#TCS-6005) | Computational and circuit complexity | 6-Uniform Maker-Breaker Game Is PSPACE-Complete |
| [TCS-6065](http://localhost:8766/?view=compact#TCS-6065) | General algorithm design | Strategy-Stealing Is Non-Constructive |
| [TCS-6137](http://localhost:8766/?view=compact#TCS-6137) | Combinatorics and graph polynomials | How Did They Design This Game? Swish: Complexity and Unplayable Positions |
| [TCS-6438](http://localhost:8766/?view=compact#TCS-6438) | General algorithm design | Magic: The Gathering Is Turing Complete |

## Concrete checks

| Record | Saved topic | Why it matters for this audit |
|---|---|---|
| [TCS-0210](http://localhost:8766/?view=compact#TCS-0210) | Dimensions of spaces spanned by graph polynomials | Graph polynomial structure is not automatically algorithm design. |
| [TCS-0214](http://localhost:8766/?view=compact#TCS-0214) | Tutte polynomials of medial graphs | Graph polynomials were explicitly removed as a category. |
| [TCS-0644](http://localhost:8766/?view=compact#TCS-0644) | On a problem of classes of optimal information | Information needed to approximate continuous objects. |
| [TCS-0645](http://localhost:8766/?view=compact#TCS-0645) | Standard information versus linear information for Lp -approximation | Standard versus linear information for Lp approximation. |
| [TCS-1913](http://localhost:8766/?view=compact#TCS-1913) | This raises a natural question: does there exist a cache-oblivious priority queue that achieves the same amortized bounds on comparisons and I/Os? | External-memory priority queues are incorrectly labeled biological in the original taxonomy. |
| [TCS-1996](http://localhost:8766/?view=compact#TCS-1996) | Finding a corresponding lower bound for C(n, 3, 3) is an open problem. | Tournament problems are another noisy biological-label example. |
| [TCS-6473](http://localhost:8766/?view=compact#TCS-6473) | Krylov Methods are (nearly) Optimal for Low-Rank Approximation — Open Question 11 | Numerical linear algebra: Krylov low-rank approximation. |
| [TCS-5475](http://localhost:8766/?view=compact#TCS-5475) | Polynomial Bounds for the Graph Minor Structure Theorem — Conjecture 6.7 | Structural bounds in the graph minor theorem. |
