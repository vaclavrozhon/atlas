# Questions found in the expanded library

Source-era questions and research directions, with separate present-day checks. These are paraphrases, not quotations or a claim that every listed question remains open. File page numbers are one-based; printed page numbers may differ.

The three complete numbered lists are Schrijver (75), Barenboim–Elkin (17), and Canonne (9). Other books have selected passages. An unchecked entry is a research lead and was not imported as a reviewed problem.

## Quantum Computation and Quantum Information

Michael A. Nielsen; Isaac L. Chuang · source `personal-270`

- **Physical universality of quantum computation** — Can the standard universal quantum-computer model efficiently simulate every physically realizable system? The physical theory and simulation criterion remain to be specified.
  Source: 1.1.1; file p. 40. Status: `source_open_unchecked`. Selection: `not_imported_direction`.
  Decision: A physical modelling programme; the passage does not specify one mathematical proposition.

- **P versus NP** — Does every polynomially verifiable decision problem have a deterministic polynomial-time algorithm?
  Source: 1.4; file p. 74. Status: `source_open_unchecked`. Selection: `existing_record`. Catalogue: TCS-0001.
  Decision: Same target is already represented; retain its existing identifier.

- **NP inside BQP** — Can bounded-error polynomial-time quantum computation solve every problem in NP?
  Source: 1.4, quantum complexity; file p. 75. Status: `source_open_unchecked`. Selection: `existing_record`. Catalogue: TCS-0037.
  Decision: Same target is already represented; retain its existing identifier.

- **Quantum graph isomorphism** — Is graph isomorphism solvable by a polynomial-time quantum algorithm?
  Source: 5, final discussion; file p. 277. Status: `source_open_unchecked`. Selection: `existing_record`. Catalogue: TCS-6522.
  Decision: Same target is already represented; retain its existing identifier.

- **Efficient nonabelian hidden-subgroup measurements** — Can the information obtainable with few hidden-subgroup oracle queries be decoded using a polynomial number of quantum operations?
  Source: Chapter 5, hidden-subgroup discussion; file p. 278. Status: `source_open_unchecked`. Selection: `related_existing_record`. Catalogue: TCS-7166.
  Decision: Efficient decoding of the hidden-subgroup information is part of the existing general hidden-subgroup goal; source representation details remain necessary.

- **Additivity of classical quantum-channel capacity** — Does entanglement across channel uses fail to increase classical communication capacity beyond the product-state expression?
  Source: 12, product-state capacity; file p. 87. Status: `resolved_negative`. Selection: `not_imported_resolved`.
  Verification: Hastings disproves general additivity. The anniversary-edition preface itself notes this development; the older chapter passage is historical.
  Sources: [primary 1](https://arxiv.org/abs/0809.3972).

- **Quantum channel capacity** — Determine quantum-channel capacity. The source-era discussion predates the general regularized coding theorem; particular single-letter capacities are separate questions.
  Source: Problem 12.7, historical discussion; file p. 640. Status: `partially_resolved_direction`. Selection: `not_imported_needs_formulation`.
  Verification: The quantum channel coding theorem gives the regularized coherent-information characterization. A general effective single-letter formula or exact computation is not supplied by that theorem. The broad source question needs this distinction before reuse.
  Sources: [primary 1](https://arxiv.org/abs/quant-ph/0304127).

- **Optimal Solovay–Kitaev exponent** — How small can the approximation-length exponent be in the Solovay–Kitaev setting described by the source?
  Source: Appendix 3; file p. 651. Status: `source_open_unchecked`. Selection: `not_imported`.

- **RSA inversion versus factoring** — Does hardness of integer factorization imply hardness of RSA inversion in the source key distribution?
  Source: Appendix 4, RSA; file p. 677. Status: `source_open_unchecked`. Selection: `not_imported`.

## Quantum Computing since Democritus

Scott Aaronson · source `personal-274`

- **Robustness of the Schrödinger hidden-variable theory** — Does the source transition matrix vary continuously under small changes of the unitary and initial state?
  Source: Chapter 15, hidden variables; file p. 213. Status: `source_open_unchecked`. Selection: `not_imported`.

- **Classical-oracle QMA versus QCMA separation** — Is there a classical oracle relative to which quantum witnesses are more powerful than classical witnesses?
  Source: Chapter 17; file p. 239. Status: `resolved_positive`. Selection: `not_imported_resolved`.
  Verification: The classical-oracle separation was announced by Bostanci–Haferkamp–Nirkhe–Zhandry in November 2025. Bostanci–Huang–Vaikuntanathan give another proof in February 2026. Neither separates unrelativized QMA from QCMA.
  Sources: [primary 1](https://eccc.weizmann.ac.il/report/2025/176/), [primary 2](https://eccc.weizmann.ac.il/report/2026/020/).

- **More-than-exponential certified randomness expansion** — Can quantum-device protocols expand a random seed by more than an exponential factor with the source certification requirements?
  Source: Chapter 23; file p. 335. Status: `resolved_positive`. Selection: `not_imported_resolved`.
  Verification: Unbounded randomness-expansion protocols exceed the historical exponential target. Gross–Aaronson explicitly analyze the seed requirement for such a protocol.
  Sources: [primary 1](https://arxiv.org/abs/1410.8019), [primary 2](https://arxiv.org/abs/1402.4797).

## Quantum Computing: Lecture Notes

Ronald de Wolf · source `personal-275`

- **Quantum triangle query complexity** — What is the optimal bounded-error quantum query complexity of detecting a triangle in a graph?
  Source: Quantum walks, triangle finding; file p. 71. Status: `source_open_unchecked`. Selection: `not_imported`.

- **Quantum triangle time complexity** — What is the optimal quantum time complexity of triangle detection in the source input-access model?
  Source: Quantum walks, triangle running time; file p. 71. Status: `source_open_unchecked`. Selection: `not_imported`.

## The Discrepancy Method: Randomness and Complexity

Bernard Chazelle · source `personal-10`

- **P versus BPP** — Can every bounded-error randomized polynomial-time decision algorithm be derandomized in polynomial time?
  Source: Introduction, derandomization; file p. 10. Status: `source_open_unchecked`. Selection: `existing_record`. Catalogue: TCS-0003.
  Decision: Same target is already represented; retain its existing identifier.

- **Computing the rank of rational elliptic curves** — Is there an unconditional algorithm computing the rank of the group of rational points of every elliptic curve over the rationals?
  Source: 2, elliptic curves; file p. 122. Status: `source_open_unchecked`. Selection: `not_imported`.

- **Deterministic linear-time minimum spanning tree** — Can an exact minimum spanning tree be computed deterministically in linear time for arbitrary comparable edge weights?
  Source: Minimum spanning trees, notes; file p. 444, 445. Status: `source_open_unchecked`. Selection: `existing_record`. Catalogue: TCS-6536.
  Decision: Same target is already represented; retain its existing identifier.

## Computational Complexity: A Conceptual Perspective

Oded Goldreich · source `personal-25`

- **Explicit superlinear Boolean circuit lower bounds** — Exhibit an explicitly computable Boolean function, or a linear-output-length Boolean map, whose unrestricted circuit size is not O(n).
  Source: Open Problem B.2; file p. 498. Status: `source_open_unchecked`. Selection: `related_existing_record`. Catalogue: TCS-6887.
  Decision: The generic explicit-circuit-lower-bound programme already has a source record. The concrete multiplication threshold was reviewed separately.

- **Linear-size integer multiplication circuits** — Can multiplication of two n-bit integers be computed by Boolean circuits of size O(n)?
  Source: B.2, multiplication example; file p. 498. Status: `open_checked`. Selection: `added_reviewed_card`. Catalogue: TCS-7223.
  Verification: No resolution was identified in the primary-source review through 11 September 2026. The checked 2026 author manuscript explicitly retains this circuit-size question. Its revision year is not a claim that the problem was first posed in 2026.
  Decision: A basic arithmetic operation supplies a concrete candidate for a central circuit-lower-bound barrier. The question is explicitly highlighted in Goldreich’s textbook and retained in Viola’s current manuscript; its nonuniform target is distinct from the catalogue’s machine-time question.
  Sources: [primary 1](https://www.wisdom.weizmann.ac.il/~oded/cc-book.html), [primary 2](https://www.ccs.neu.edu/home/viola/papers/moti.pdf).

- **Explicit superpolynomial formula lower bounds** — Exhibit an explicit Boolean function requiring superpolynomial-size Boolean formulas.
  Source: Open Problem B.6; file p. 500. Status: `source_open_unchecked`. Selection: `not_imported`.

- **Explicit hard univariate polynomials** — Exhibit an explicit degree-d polynomial whose arithmetic circuit size is not O(log d).
  Source: Open Problem B.7; file p. 502. Status: `source_open_unchecked`. Selection: `not_imported`.

- **Complexity of the rising-factorial polynomial** — Does the polynomial (x+1)(x+2)...(x+d) require arithmetic circuits larger than every polynomial in log d?
  Source: B.3.1; file p. 502. Status: `source_open_unchecked`. Selection: `not_imported`.

- **Unrestricted Fourier-transform circuit lower bounds** — Does the discrete Fourier transform require more than linear-size arithmetic circuits when scalar constants are unrestricted?
  Source: B.3.2; file p. 503. Status: `open_checked`. Selection: `existing_record`. Catalogue: TCS-7175.
  Verification: The unrestricted linear-circuit lower-bound barrier is retained in the checked primary literature. Bounded-coefficient FFT lower bounds do not settle it. TCS-7175 already covers the stronger Fourier-transform lower-bound goal, so no second record is added.
  Decision: Same target is already represented; retain its existing identifier.
  Sources: [primary 1](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.STACS.2023.31), [primary 2](https://www3.nd.edu/~jhauenst/preprints/ghilRigidity.pdf).

- **Unrestricted Walsh-transform circuit lower bounds** — Does the Walsh transform over the rationals require more than linear-size arithmetic circuits with unrestricted constants?
  Source: B.3.2, Walsh transform; file p. 503. Status: `source_open_unchecked`. Selection: `not_imported`.

- **Unrestricted Frege lower bounds** — Are there propositional tautology families with no polynomial-length Frege proofs?
  Source: B, proof complexity; file p. 506. Status: `source_open_unchecked`. Selection: `existing_record`. Catalogue: TCS-0025.
  Decision: Same target is already represented; retain its existing identifier.

- **Deterministic construction of finite fields** — Can irreducible degree-e polynomials over an arbitrary prime field be constructed in deterministic time polynomial in e and the bit length of the prime?
  Source: G.4, finite fields; file p. 613. Status: `source_open_unchecked`. Selection: `not_imported`.

## The Nature of Computation

Cristopher Moore; Stephan Mertens · source `personal-26`

- **Polynomial Reidemeister simplification of the unknot** — Can every unknot diagram be simplified to a circle with polynomially many Reidemeister moves in its crossing number?
  Source: 4.4.2, unknot certificates; file p. 134, 135. Status: `resolved_positive`. Selection: `not_imported_resolved`.
  Verification: Lackenby proves a polynomial upper bound on moves needed to simplify an unknot diagram. This certificate-length theorem does not itself yield polynomial-time unknot recognition.
  Sources: [primary 1](https://arxiv.org/abs/1302.0180).

- **P versus BPP** — Does randomized polynomial-time decision computation have the same power as deterministic polynomial time?
  Source: 11.4; file p. 556. Status: `source_open_unchecked`. Selection: `existing_record`. Catalogue: TCS-0003.
  Decision: Same target is already represented; retain its existing identifier.

- **Mixing for four- and five-colour square lattices** — Establish the source spatial-mixing and Glauber-mixing claims for four and five colours, with boundary conditions specified.
  Source: 12, square-lattice colouring; file p. 642. Status: `source_open_unchecked`. Selection: `not_imported`.

## Introduction to Algorithms

Thomas H. Cormen; Charles E. Leiserson; Ronald L. Rivest; Clifford Stein · source `personal-7`

- **P versus NP** — Is P a proper subset of NP?
  Source: 34, NP-completeness; file p. 990. Status: `source_open_unchecked`. Selection: `existing_record`. Catalogue: TCS-0001.
  Decision: Same target is already represented; retain its existing identifier.

## Algorithms

Jeff Erickson · source `personal-5`

- **Exact shortest addition chains** — Can a shortest addition chain for a binary integer n be found in time polynomial in its bit length?
  Source: 1, exponentiation; file p. 41. Status: `open_checked`. Selection: `added_reviewed_card`. Catalogue: TCS-7224.
  Verification: The single-target polynomial-time question remains unresolved in the checked sources through 11 September 2026. The review does not accept claims of NP-completeness that merely cite the generalized multiple-target theorem.
  Decision: A longstanding exact optimization problem at the intersection of arithmetic algorithms, circuit reuse and cryptographic exponentiation. Its single-target complexity is repeatedly distinguished from the solved hardness of the generalized problem; it is not a numerical special case of Scholz–Brauer.
  Sources: [primary 1](https://jeffe.cs.illinois.edu/teaching/algorithms/), [primary 2](https://faculty.eng.fau.edu/azarderakhsh/files/2016/11/Inscrypt2016.pdf), [primary 3](https://www.nature.com/articles/s44260-025-00049-9).

- **Splay-tree dynamic optimality** — Are splay trees within a universal constant factor of the best offline rotation-based binary search tree on every access sequence?
  Source: Splay trees; file p. 249. Status: `source_open_unchecked`. Selection: `existing_record`. Catalogue: TCS-6498.
  Decision: Same target is already represented; retain its existing identifier.

- **Matrix multiplication exponent two** — Is the matrix multiplication exponent equal to two?
  Source: Matrix multiplication; file p. 339. Status: `source_open_unchecked`. Selection: `existing_record`. Catalogue: TCS-0007.
  Decision: Same target is already represented; retain its existing identifier.

- **NP versus coNP** — Does every no-instance of an NP problem have a polynomially verifiable certificate?
  Source: 30.2; file p. 417. Status: `source_open_unchecked`. Selection: `not_imported`.

- **Logspace versus polynomial reductions** — Does allowing polynomial-time rather than logarithmic-space reductions change which problems are NP-hard in the specified reduction sense?
  Source: 30.4; file p. 419. Status: `source_open_unchecked`. Selection: `not_imported`.

## The Design and Analysis of Algorithms

Dexter C. Kozen · source `personal-6`

- **P versus NP** — Does nondeterministic polynomial time exceed deterministic polynomial time?
  Source: Complexity classes; file p. 133. Status: `source_open_unchecked`. Selection: `existing_record`. Catalogue: TCS-0001.
  Decision: Same target is already represented; retain its existing identifier.

## Foundations of Cryptography, Volume 1: Basic Tools

Oded Goldreich · source `personal-141`

- **Existence of one-way functions** — Do computationally secure one-way functions exist?
  Source: 1.5.3; file p. 48. Status: `source_open_unchecked`. Selection: `existing_record`. Catalogue: TCS-7167.
  Decision: Same target is already represented; retain its existing identifier.

- **Efficient decoding of random linear codes** — Can random constant-rate binary linear codes be efficiently decoded from a constant fraction of errors in the source average-case regime?
  Source: 2.2.4.2; file p. 62. Status: `source_open_unchecked`. Selection: `not_imported`.

- **RSA inversion versus factoring** — Can factoring RSA moduli be reduced to RSA inversion with the source key-generation and exponent conventions?
  Source: 2, RSA discussion; file p. 77. Status: `source_open_unchecked`. Selection: `not_imported`.

- **Worst-case hardness and one-way functions** — Does NP not contained in BPP imply the existence of one-way functions?
  Source: 2.7.3; file p. 112. Status: `source_open_unchecked`. Selection: `existing_record`. Catalogue: TCS-0022.
  Decision: Same target is already represented; retain its existing identifier.

- **Security-preserving amplification for arbitrary one-way functions** — Extend the efficient hardness amplification available for one-way permutations to arbitrary weak one-way functions.
  Source: 2.7.3, amplification; file p. 113. Status: `source_open_unchecked`. Selection: `not_imported`.

- **Efficient generic PRG construction** — Obtain a substantially more security-preserving construction of pseudorandom generators from arbitrary one-way functions than the source transformation.
  Source: 3.8.3; file p. 193. Status: `source_open_unchecked`. Selection: `not_imported`.

- **Perfect versus statistical zero knowledge** — Does perfect zero knowledge have the same computational power as statistical zero knowledge?
  Source: 4.3.1.5; file p. 226. Status: `open_checked`. Selection: `added_reviewed_card`. Catalogue: TCS-7225.
  Verification: No unrelativized resolution was found through 11 September 2026. The 2024 paper explicitly retains the equality as open. Oracle separations and perfect-zero-knowledge results in PCP or multiprover models do not settle this target.
  Decision: A foundational comparison between two information-theoretic privacy notions, posed in a standard cryptography textbook, supported by a nontrivial oracle separation and explicitly retained in recent work on perfect zero knowledge.
  Sources: [primary 1](https://www.wisdom.weizmann.ac.il/~oded/foc-vol1.html), [primary 2](https://epubs.siam.org/doi/10.1137/17M1161749), [primary 3](https://arxiv.org/abs/2403.11941).

- **Strict versus expected-time perfect simulation** — Does the expected-polynomial-time simulator definition of perfect zero knowledge imply the strict-polynomial-time definition with bounded failure used in this book?
  Source: 4.12.3; file p. 344. Status: `source_open_unchecked`. Selection: `not_imported`.

## Introduction to Modern Cryptography

Jonathan Katz; Yehuda Lindell · source `personal-146`

- **RSA inversion versus factoring** — Does hardness of factoring imply hardness of the RSA problem?
  Source: 8.4, RSA; file p. 335. Status: `source_open_unchecked`. Selection: `not_imported`.

## Distributed Algorithms

Nancy A. Lynch · source `personal-282`

- **Fast atomic shared-memory objects** — Can the source atomic-object constructions be made fast enough for the intended applications? No quantitative resolution target is fixed.
  Source: Atomic objects; file p. 422. Status: `source_open_unchecked`. Selection: `not_imported_direction`.
  Decision: The object, operation set and resource target need to be fixed before a card can be completed.

- **Modular proof of the GHS algorithm** — Find a decomposed proof of correctness for the GHS distributed minimum-spanning-tree algorithm while preserving its main ideas and complexity.
  Source: GHS correctness; file p. 547. Status: `source_open_unchecked`. Selection: `not_imported_not_open_mathematical_problem`.
  Decision: A request for a better proof organization is not itself a new unresolved mathematical proposition.

## Distributed Computing: A Locality-Sensitive Approach

David Peleg · source `personal-280`

- **Deterministic polylogarithmic distributed symmetry breaking** — Do deterministic polylogarithmic-round algorithms exist for MIS and colouring in the LOCAL model?
  Source: Network decomposition, chapter notes; file p. 311. Status: `resolved_positive`. Selection: `not_imported_resolved`.
  Verification: The historical deterministic polylogarithmic symmetry-breaking barrier is resolved by Rozhon–Ghaffari. Sharper round bounds remain separate questions.
  Sources: [primary 1](https://arxiv.org/abs/1907.10937).

## Distributed Graph Coloring: Fundamentals and Recent Developments

Leonid Barenboim; Michael Elkin · source `personal-283`

- **Distributed derandomization** — Develop a general derandomization method for distributed message-passing algorithms.
  Source: Open Problem 11.1; file p. 147. Status: `partially_resolved_direction`. Selection: `not_imported_direction`.
  Verification: Rozhon–Ghaffari give polylogarithmic derandomization for locally checkable problems. This resolves the central polylogarithmic case, but the source’s unrestricted request for a general method is broader than a single theorem.
  Sources: [primary 1](https://arxiv.org/abs/1907.10937).

- **Polylogarithmic deterministic MIS** — Can maximal independent set be computed deterministically in polylogarithmic LOCAL rounds?
  Source: Open Problem 11.2; file p. 148. Status: `resolved_positive`. Selection: `not_imported_resolved`.
  Verification: Rozhon–Ghaffari’s deterministic polylogarithmic LOCAL network decomposition resolves this polylogarithmic target. General MIS covers the neighbourhood-independence restriction; proper vertex colouring also applies to the line graph for the stated edge palette.
  Sources: [primary 1](https://arxiv.org/abs/1907.10937).

- **Polylogarithmic near-linear-palette colouring** — Can a proper vertex colouring with Delta times polylog(Delta) colours be computed deterministically in polylogarithmic rounds?
  Source: Open Problem 11.3; file p. 148. Status: `resolved_positive`. Selection: `not_imported_resolved`.
  Verification: Rozhon–Ghaffari’s deterministic polylogarithmic LOCAL network decomposition resolves this polylogarithmic target. General MIS covers the neighbourhood-independence restriction; proper vertex colouring also applies to the line graph for the stated edge palette.
  Sources: [primary 1](https://arxiv.org/abs/1907.10937).

- **Polylogarithmic deterministic edge colouring** — Can a proper (2Delta-1)-edge-colouring be computed deterministically in polylogarithmic rounds?
  Source: Open Problem 11.4; file p. 148. Status: `resolved_positive`. Selection: `not_imported_resolved`.
  Verification: Rozhon–Ghaffari’s deterministic polylogarithmic LOCAL network decomposition resolves this polylogarithmic target. General MIS covers the neighbourhood-independence restriction; proper vertex colouring also applies to the line graph for the stated edge palette.
  Sources: [primary 1](https://arxiv.org/abs/1907.10937).

- **MIS with bounded neighbourhood independence** — Is deterministic polylogarithmic-round MIS possible when neighbourhood independence is at most two?
  Source: Open Problem 11.5; file p. 149. Status: `resolved_positive`. Selection: `not_imported_resolved`.
  Verification: Rozhon–Ghaffari’s deterministic polylogarithmic LOCAL network decomposition resolves this polylogarithmic target. General MIS covers the neighbourhood-independence restriction; proper vertex colouring also applies to the line graph for the stated edge palette.
  Sources: [primary 1](https://arxiv.org/abs/1907.10937).

- **Sublinear dependence on maximum degree** — Can the listed symmetry-breaking problems be solved in o(Delta)+log-star(n) deterministic rounds?
  Source: Open Problem 11.6; file p. 149. Status: `source_open_unchecked`. Selection: `not_imported`.

- **Efficient defective colouring** — Can a (Delta/p)-defective colouring using O(p) colours be computed efficiently in the distributed model?
  Source: Open Problem 11.7; file p. 149. Status: `source_open_unchecked`. Selection: `not_imported`.

- **Large-arboricity deterministic symmetry breaking** — Are deterministic polylogarithmic-round symmetry-breaking algorithms possible beyond polylogarithmic arboricity?
  Source: Open Problem 11.8; file p. 150. Status: `source_open_unchecked`. Selection: `not_imported`.

- **Sublogarithmic sparse-graph symmetry breaking** — Can deterministic sublogarithmic rounds handle MIS and colouring at arboricity Omega(sqrt(log n)), and matching and edge colouring at arboricity Omega(log n)?
  Source: Open Problem 11.9; file p. 150. Status: `source_open_unchecked`. Selection: `not_imported`.

- **Distributed decomposition below twice the arboricity** — Can a graph of arboricity a be efficiently decomposed into fewer than 2a forests in the distributed model?
  Source: Open Problem 11.10; file p. 150. Status: `source_open_unchecked`. Selection: `not_imported`.

- **Improving arboricity-dependent palettes** — Can deterministic O(log n)-round colouring use substantially fewer than a squared colours for arboricity a?
  Source: Open Problem 11.11; file p. 150. Status: `source_open_unchecked`. Selection: `not_imported`.

- **Randomized MIS in square-root-logarithmic time** — Is randomized O(sqrt(log n))-round MIS possible in all graphs, and what is its optimal randomized complexity?
  Source: Open Problem 11.12; file p. 151. Status: `source_open_unchecked`. Selection: `not_imported`.

- **Randomized MIS on low-arboricity graphs** — Improve the source randomized MIS bounds for graphs of bounded arboricity.
  Source: Open Problem 11.13; file p. 151. Status: `source_open_unchecked`. Selection: `not_imported`.

- **Randomized maximal matching in square-root-logarithmic time** — Is randomized O(sqrt(log n))-round maximal matching possible in all graphs?
  Source: Open Problem 11.14; file p. 151. Status: `source_open_unchecked`. Selection: `not_imported`.

- **Randomized MIS complexity on unoriented trees** — Is the randomized LOCAL complexity of MIS on unoriented trees Theta(sqrt(log n))?
  Source: Open Problem 11.15; file p. 151. Status: `source_open_unchecked`. Selection: `not_imported`.

- **Randomized Delta-plus-one colouring complexity** — Determine the optimal randomized LOCAL round complexity of proper (Delta+1)-vertex-colouring.
  Source: Open Problem 11.16; file p. 152. Status: `source_open_unchecked`. Selection: `not_imported`.

- **Log-star randomized colouring at small degree** — Can randomized O(log-star n)-round colouring with O(Delta) colours extend to sublogarithmic maximum degree?
  Source: Open Problem 11.17; file p. 152. Status: `source_open_unchecked`. Selection: `not_imported`.

## Notes on Theory of Distributed Systems

James Aspnes · source `personal-277`

- **Optimal atomic-snapshot complexity** — Can the cost of atomic snapshots be improved in the shared-memory model and cost measure of the source?
  Source: Atomic snapshots; file p. 224. Status: `source_open_unchecked`. Selection: `not_imported`.

- **Splitter-network renaming space** — Can the source O(n to the three-halves) space bound for deterministic splitter-network renaming be improved?
  Source: 24.4.3; file p. 260. Status: `source_open_unchecked`. Selection: `not_imported`.

## Combinatorial Optimization: Polyhedra and Efficiency

Alexander Schrijver · source `personal-234`

- **P versus NP** — Is P different from NP?
  Source: Survey Question 1; file p. 1491. Status: `source_open_unchecked`. Selection: `existing_record`. Catalogue: TCS-0001.
  Decision: Same target is already represented; retain its existing identifier.

- **P versus NP intersect coNP** — Does P equal NP intersect coNP?
  Source: Survey Question 2; file p. 1491. Status: `source_open_unchecked`. Selection: `existing_record`. Catalogue: TCS-0018.
  Decision: Same target is already represented; retain its existing identifier.

- **Linear Hirsch bound** — Does every d-dimensional polytope with m facets have edge diameter at most m-d?
  Source: Survey Question 3; file p. 1491. Status: `resolved_negative`. Selection: `not_imported_resolved`.
  Verification: Santos disproved the Hirsch diameter bound; the author’s errata also records the correction.
  Sources: [primary 1](https://arxiv.org/abs/1006.2814), [primary 2](https://homepages.cwi.nl/~lex/co/).

- **O(nm) maximum flow** — Can a maximum flow be found in O(nm) time in the source network model?
  Source: Survey Question 4; file p. 1491. Status: `resolved_positive`. Selection: `not_imported_resolved`.
  Verification: Orlin obtained O(nm) maximum flow; Schrijver explicitly marks Survey Question 4 answered.
  Sources: [primary 1](https://homepages.cwi.nl/~lex/co/).

- **Berge path-partition conjecture** — For every minimum k-truncated-size directed path partition, are there k disjoint stable sets meeting each path in min(k, its number of vertices) distinct sets?
  Source: Survey Question 5; file p. 1491. Status: `source_open_unchecked`. Selection: `not_imported`.

- **Packing common transversals** — Determine the maximum number of common transversals of two set families whose summed incidence vectors obey a specified integral capacity vector.
  Source: Survey Question 6; file p. 1491. Status: `resolved_reported`. Selection: `not_imported_resolved`.
  Verification: Schrijver’s author errata says this question was already solved by Weinberger (1976). The original proof was not reread.
  Sources: [primary 1](https://homepages.cwi.nl/~lex/co/).

- **Small matching extended formulations** — Does every matching polytope admit an extended linear formulation of polynomial size?
  Source: Survey Question 7; file p. 1491. Status: `resolved_negative`. Selection: `not_imported_resolved`.
  Verification: Rothvoss proves exponential extension complexity for the perfect-matching polytope. This rules out the proposed polynomial extended formulation.
  Sources: [primary 1](https://arxiv.org/abs/1311.2369).

- **Tutte five-flow conjecture** — Does every bridgeless graph admit a nowhere-zero 5-flow?
  Source: Survey Question 8; file p. 1491. Status: `source_open_unchecked`. Selection: `not_imported`.

- **Tutte four-flow conjecture** — Does every bridgeless graph with no Petersen minor admit a nowhere-zero 4-flow?
  Source: Survey Question 9; file p. 1492. Status: `source_open_unchecked`. Selection: `not_imported`.

- **Tutte three-flow conjecture** — Does every 4-edge-connected graph admit a nowhere-zero 3-flow?
  Source: Survey Question 10; file p. 1492. Status: `source_open_unchecked`. Selection: `not_imported`.

- **Weak three-flow conjecture** — Is there an absolute edge-connectivity threshold that guarantees a nowhere-zero 3-flow?
  Source: Survey Question 11; file p. 1492. Status: `resolved_positive`. Selection: `not_imported_resolved`.
  Verification: Thomassen proves a fixed edge-connectivity threshold, settling the weak three-flow conjecture; this does not settle Tutte’s exact four-edge-connectivity conjecture.
  Sources: [primary 1](https://orbit.dtu.dk/en/publications/the-weak-3-flow-conjecture-and-the-weak-circular-flow/).

- **Jaeger circular-flow conjecture** — For each k at least one, does every 4k-connected graph admit an orientation with outdegree minus indegree divisible by 2k+1 at every vertex? Consult the source for its connectivity convention.
  Source: Survey Question 12; file p. 1492. Status: `source_open_unchecked`. Selection: `not_imported`.

- **Generalized Fulkerson conjecture** — In every k-regular graph whose odd cuts have size at least k, do 2k perfect matchings cover every edge exactly twice?
  Source: Survey Question 13; file p. 1492. Status: `source_open_unchecked`. Selection: `not_imported`.

- **Fulkerson six-matchings conjecture** — Do six perfect matchings cover every edge of every bridgeless cubic graph exactly twice?
  Source: Survey Question 14; file p. 1493. Status: `source_open_unchecked`. Selection: `not_imported`.

- **Berge five-matchings conjecture** — Can every bridgeless cubic graph be covered by five perfect matchings?
  Source: Survey Question 15; file p. 1493. Status: `source_open_unchecked`. Selection: `not_imported`.

- **Goldberg–Seymour conjecture** — Is the chromatic index of every multigraph at most the maximum of maximum degree plus one and the ceiling of its fractional chromatic index?
  Source: Survey Question 16; file p. 1493. Status: `resolved_positive`. Selection: `not_imported_resolved`.
  Verification: The Goldberg–Seymour bound was proved by Chen–Jing–Zang; the 2024 short proof supplies a further primary reference.
  Sources: [primary 1](https://arxiv.org/abs/1901.10316), [primary 2](https://arxiv.org/abs/2407.09403).

- **Edge-colouring planar k-graphs** — Is every planar k-regular graph with every odd cut of size at least k, k-edge-colourable?
  Source: Survey Question 17; file p. 1493. Status: `source_open_unchecked`. Selection: `not_imported`.

- **Edge-colouring Petersen-minor-free k-graphs** — Is every Petersen-minor-free k-regular graph with every odd cut of size at least k, k-edge-colourable?
  Source: Survey Question 18; file p. 1493. Status: `source_open_unchecked`. Selection: `not_imported`.

- **Vizing planar degree-six question** — Is there a simple planar graph with maximum degree six requiring seven edge colours?
  Source: Survey Question 19; file p. 1493. Status: `source_open_unchecked`. Selection: `not_imported`.

- **Kempe changes to an optimal edge-colouring** — Can any edge-colouring be transformed into a minimum edge-colouring using only alternating-path or alternating-cycle colour swaps and removal of unused colours?
  Source: Survey Question 20; file p. 1493. Status: `source_open_unchecked`. Selection: `not_imported`.

- **List-edge-colouring conjecture** — Does the list chromatic index equal the ordinary chromatic index for every graph?
  Source: Survey Question 21; file p. 1493. Status: `source_open_unchecked`. Selection: `not_imported`.

- **Total colouring of simple graphs** — Does every simple graph have a total colouring using at most maximum degree plus two colours?
  Source: Survey Question 22; file p. 1493, 1494. Status: `source_open_unchecked`. Selection: `not_imported`.

- **Total colouring of multigraphs** — Is the total chromatic number at most maximum degree plus maximum edge multiplicity plus one?
  Source: Survey Question 23; file p. 1494. Status: `source_open_unchecked`. Selection: `not_imported`.

- **Integral points in the circuit cone** — Is every even integral vector in a graph circuit cone a nonnegative integral sum of circuit incidence vectors?
  Source: Survey Question 24; file p. 1494. Status: `source_open_unchecked`. Selection: `not_imported`.

- **Cycle double cover conjecture** — Does every bridgeless graph have a multiset of circuits covering each edge exactly twice?
  Source: Survey Question 25; file p. 1494. Status: `source_open_unchecked`. Selection: `not_imported`.

- **Quarter-integrality of T-join constraints** — Is the system of T-join constraints totally dual quarter-integral?
  Source: Survey Question 26; file p. 1494. Status: `source_open_unchecked`. Selection: `not_imported`.

- **Shortest odd paths with conservative weights** — What is the complexity of a shortest odd s-t path when rational edge lengths give every circuit nonnegative total length?
  Source: Survey Question 27; file p. 1494. Status: `source_open_unchecked`. Selection: `not_imported`.

- **Two-factors without short circuits** — What is the complexity of deciding whether a graph has a 2-factor with no circuit of length at most four?
  Source: Survey Question 28; file p. 1494. Status: `source_open_unchecked`. Selection: `not_imported`.

- **Weighted triangle-free two-factors** — What is the complexity of finding a maximum-weight 2-factor with no circuit of length at most three?
  Source: Survey Question 29; file p. 1494. Status: `source_open_unchecked`. Selection: `not_imported`.

- **Five-cycle double cover conjecture** — Can every bridgeless graph be covered exactly twice by at most five cycles, with cycle interpreted as in the source rather than necessarily a connected circuit?
  Source: Survey Question 30; file p. 1494. Status: `source_open_unchecked`. Selection: `not_imported`.

- **Duality of algebraic matroids** — Is the dual of every algebraic matroid also algebraic?
  Source: Survey Question 31; file p. 1494. Status: `source_open_unchecked`. Selection: `not_imported`.

- **Independent spanning trees** — If a root has k internally vertex-disjoint paths to every other vertex, do k spanning trees simultaneously realize those internally disjoint root-to-vertex paths?
  Source: Survey Question 32; file p. 1494, 1495. Status: `source_open_unchecked`. Selection: `not_imported`.

- **Computing maximum disjoint dijoins** — Can a maximum-cardinality family of pairwise arc-disjoint directed-cut covers be computed in polynomial time?
  Source: Survey Question 33; file p. 1495. Status: `source_open_unchecked`. Selection: `not_imported`.

- **Woodall dijoin-packing conjecture** — Does the minimum cardinality of a directed cut equal the maximum number of pairwise arc-disjoint dijoins?
  Source: Survey Question 34; file p. 1495. Status: `open_checked`. Selection: `added_reviewed_card`. Catalogue: TCS-7226.
  Verification: The unweighted general conjecture remains open in the primary sources checked through 11 September 2026. The false weighted Edmonds–Giles conjecture is a different statement. The checked 2025 constant-factor packing theorem does not imply equality.
  Decision: A longstanding min–max conjecture in combinatorial optimization, singled out in Schrijver’s survey and the focus of recent approximation and integrality research. The direct packing/covering and algorithmic connections justify inclusion within optimization.
  Sources: [primary 1](https://homepages.cwi.nl/~lex/co/), [primary 2](https://doi.org/10.1007/s00493-025-00159-x).

- **Four-thirds subtour integrality gap** — Is a minimum Hamiltonian tour at most four-thirds of the subtour-elimination linear-programming optimum under the nonnegative edge costs in the source?
  Source: Survey Question 35; file p. 1495. Status: `source_formulation_corrected`. Selection: `existing_record`. Catalogue: TCS-6589.
  Corrected target: Does the metric symmetric TSP subtour relaxation have integrality gap at most 4/3?
  Verification: Schrijver’s official errata explicitly adds the triangle inequality. The uncorrected source passage must not become a new nonmetric conjecture. The corrected metric target already has TCS-6589.
  Sources: [primary 1](https://homepages.cwi.nl/~lex/co/).

- **Diameter of the TSP polytope** — Is the edge diameter of the symmetric travelling-salesman polytope of every complete graph at most two?
  Source: Survey Question 36; file p. 1495. Status: `source_open_unchecked`. Selection: `not_imported`.

- **Augmenting acyclic digraph connectivity** — For simple acyclic digraphs, is the minimum number of arcs needed for k-vertex-connectivity the larger of the total indegree and outdegree deficits specified by Frank?
  Source: Survey Question 37; file p. 1495. Status: `source_open_unchecked`. Selection: `not_imported`.

- **Hadwiger conjecture** — Must every graph of chromatic number at least k contain a complete graph on k vertices as a minor?
  Source: Survey Question 38; file p. 1495. Status: `source_open_unchecked`. Selection: `existing_record`. Catalogue: TCS-6651.
  Decision: Same target is already represented; retain its existing identifier.

- **Stable sets at bounded cutting-plane rank** — For each fixed t, is maximum stable set polynomial-time solvable when its polytope arises from the clique relaxation in at most t cutting-plane rounds?
  Source: Survey Question 39; file p. 1495, 1496. Status: `source_open_unchecked`. Selection: `not_imported`.

- **Cutting-plane proof length for stable sets** — Is there no polynomial bound on the number of cutting-plane additions needed to derive the maximum-stable-set inequality from the edge relaxation?
  Source: Survey Question 40; file p. 1496. Status: `source_open_unchecked`. Selection: `not_imported`.

- **Chi-boundedness without odd holes** — Is the chromatic number of every odd-hole-free graph bounded by a function of its clique number?
  Source: Survey Question 41; file p. 1496. Status: `resolved_positive`. Selection: `not_imported_resolved`.
  Verification: Scott–Seymour prove chi-boundedness of graphs with no odd hole.
  Sources: [primary 1](https://arxiv.org/abs/1410.4118).

- **Recognizing perfect graphs** — Can perfect graphs be recognized in polynomial time?
  Source: Survey Question 42; file p. 1496. Status: `resolved_positive`. Selection: `not_imported_resolved`.
  Verification: Polynomial recognition was obtained by Chudnovsky and coauthors. Schrijver’s errata explicitly marks Question 42 answered.
  Sources: [primary 1](https://homepages.cwi.nl/~lex/co/), [primary 2](https://algorithms.leeds.ac.uk/wp-content/uploads/sites/117/2017/09/FOCS03final.pdf).

- **Berge alpha-diperfect digraph characterization** — Are alpha-diperfect digraphs exactly those avoiding the explicitly oriented induced odd circuits specified in source conjecture (20)?
  Source: Survey Question 43; file p. 1496. Status: `source_open_unchecked`. Selection: `not_imported`.

- **Shannon capacity of odd cycles** — Does the Shannon capacity of every odd cycle equal its Lovász theta number?
  Source: Survey Question 44; file p. 1496. Status: `source_open_unchecked`. Selection: `existing_record`. Catalogue: TCS-6610.
  Decision: The existing C7 question is a prominent unsolved member of the source family. No additional generalization is imported without a separate significance review.

- **Computing Haemers bound** — Can Haemers bound on the Shannon capacity of a graph be computed in polynomial time? The underlying field convention must be taken from the source.
  Source: Survey Question 45; file p. 1496. Status: `source_open_unchecked`. Selection: `not_imported`.

- **Strong t-perfection** — Is the stable-set description by nonnegativity, edges and odd-circuit inequalities totally dual integral whenever it is integral?
  Source: Survey Question 46; file p. 1496. Status: `source_open_unchecked`. Selection: `not_imported`.

- **Minimal obstructions to t-perfection** — Which graphs are minimally non-t-perfect under induced-subgraph deletion and the allowed neighbourhood contractions?
  Source: Survey Question 47; file p. 1496. Status: `source_open_unchecked`. Selection: `not_imported`.

- **Connectivity forcing k-linkedness** — Is 2k+2 the minimum vertex-connectivity that guarantees k-linkedness for every k at least two?
  Source: Survey Question 48; file p. 1496. Status: `source_open_unchecked`. Selection: `not_imported`.

- **Edge-connectivity forcing paired paths** — Is the edge-connectivity threshold guaranteeing k specified pairwise edge-disjoint paths k for odd k and k+1 for even k?
  Source: Survey Question 49; file p. 1496. Status: `source_open_unchecked`. Selection: `not_imported`.

- **Directed planar arc-disjoint paths** — For every fixed k at least two, what is the complexity of k specified arc-disjoint paths in a planar digraph?
  Source: Survey Question 50; file p. 1497. Status: `source_open_unchecked`. Selection: `not_imported`.

- **Half-integral multiflows for two triangles** — For two disjoint demand triangles with integral data and the Euler condition, does fractional multiflow feasibility imply half-integral feasibility?
  Source: Survey Question 51; file p. 1497. Status: `source_open_unchecked`. Selection: `not_imported`.

- **Bounded fractionality with no three disjoint demands** — Does every demand graph with no three disjoint edges admit a fixed denominator bounding feasible multiflow fractionality for every supply graph and integral capacities and demands?
  Source: Survey Question 52; file p. 1497. Status: `source_open_unchecked`. Selection: `not_imported`.

- **Okamura half-integral routing conjecture** — If the supply graph is l-edge-connected and every cut of the demand graph has at most l edges, is there a half-integral routing of the demands?
  Source: Survey Question 53; file p. 1497. Status: `source_open_unchecked`. Selection: `not_imported`.

- **Mader matroids as gammoids** — Is every Mader matroid a gammoid?
  Source: Survey Question 54; file p. 1497. Status: `resolved_reported`. Selection: `not_imported_resolved`.
  Verification: The author’s errata records a positive resolution by G. Pap in February 2006; no independent proof check was performed.
  Sources: [primary 1](https://homepages.cwi.nl/~lex/co/).

- **Representability of Mader matroids** — Is every Mader matroid linearly representable?
  Source: Survey Question 55; file p. 1497. Status: `resolved_reported`. Selection: `not_imported_resolved`.
  Verification: The author’s errata records a positive resolution by G. Pap in February 2006; no independent proof check was performed.
  Sources: [primary 1](https://homepages.cwi.nl/~lex/co/).

- **Planar outer-face edge-disjoint paths** — Is the undirected edge-disjoint paths problem polynomial-time solvable when all terminals lie on the outer face of a planar graph?
  Source: Survey Question 56; file p. 1497. Status: `resolved_complexity`. Selection: `not_imported_resolved`.
  Verification: Schrijver records NP-completeness proved by W. Schwaerzler, published in Combinatorica 29 (2009), 121–126. This settles the classification; it does not unconditionally prove absence of a polynomial algorithm.
  Sources: [primary 1](https://homepages.cwi.nl/~lex/co/).

- **Planar multiflows on finitely many faces** — Is integer multiflow polynomial-time solvable when supply and demand graphs are jointly planar and demands span a fixed number of supply faces?
  Source: Survey Question 57; file p. 1497. Status: `source_open_unchecked`. Selection: `not_imported`.

- **Quarter-to-half-integral toroidal routing** — When the union of supply and demand graphs embeds in the torus, does quarter-integral edge-disjoint routing imply half-integral routing?
  Source: Survey Question 58; file p. 1497. Status: `source_open_unchecked`. Selection: `not_imported`.

- **Packing cuts in planar bipartite graphs** — Can disjoint cuts realize all required distances among outer-face vertices and a fixed boundary root in the manner stated in source Question 59?
  Source: Survey Question 59; file p. 1497. Status: `source_open_unchecked`. Selection: `not_imported`.

- **Cut Hilbert bases under minors** — Is the class of graphs whose cut incidence vectors form a Hilbert base closed under taking minors?
  Source: Survey Question 60; file p. 1497. Status: `source_open_unchecked`. Selection: `not_imported`.

- **Weighted fractional hypergraph matching bound** — Does every nonnegative edge-weighted hypergraph have a matching whose sum of (edge size minus one plus reciprocal edge size) times edge weight is at least the fractional matching optimum?
  Source: Survey Question 61; file p. 1497, 1498. Status: `source_open_unchecked`. Selection: `not_imported`.

- **Ideal binary hypergraph characterization** — Is a binary hypergraph ideal exactly when it excludes the three minors O(K5), its blocker, and F7 specified by Seymour?
  Source: Survey Question 62; file p. 1498. Status: `source_open_unchecked`. Selection: `not_imported`.

- **Minor witnesses for weighted blocking inequalities** — Can every violation of the weighted blocking inequality for a hypergraph without a Jn minor be witnessed by zero-one weights on a minor with the source covering-number bounds?
  Source: Survey Question 63; file p. 1498. Status: `source_open_unchecked`. Selection: `not_imported`.

- **Minor attainment of a nonideal covering minimum** — For a nonideal hypergraph, is the minimum covering number among nonideal parallelizations and minors already attained by a minor?
  Source: Survey Question 64; file p. 1498. Status: `source_open_unchecked`. Selection: `not_imported`.

- **Finitely many large minimally nonideal hypergraphs** — Are there only finitely many minimally nonideal hypergraphs having both minimum edge size and covering number greater than two?
  Source: Survey Question 65; file p. 1498. Status: `source_open_unchecked`. Selection: `not_imported`.

- **Uniform bound for minimally nonideal hypergraphs** — Is one of minimum edge size and covering number bounded by an absolute constant in every minimally nonideal hypergraph?
  Source: Survey Question 66; file p. 1498. Status: `source_open_unchecked`. Selection: `not_imported`.

- **Lehman structure for minimal k-packing obstructions** — Must every minor-minimal hypergraph with the source strict k-fold covering inequality contain a Jn minor or satisfy the specified Lehman regularity conditions?
  Source: Survey Question 67; file p. 1498. Status: `source_open_unchecked`. Selection: `not_imported`.

- **Conforti–Cornuéjols packing conjecture** — Does every clutter with the packing property have the max-flow min-cut property; equivalently, is every packing hypergraph Mengerian?
  Source: Survey Question 68; file p. 1498. Status: `open_checked`. Selection: `added_reviewed_card`. Catalogue: TCS-7227.
  Verification: No general resolution was found through 11 September 2026. The checked July 2026 manuscript explicitly retains the conjecture. Its reported finite computations and subclass results are recorded as progress; their proof artifacts were not independently rechecked in this editorial review.
  Decision: A central conjecture connecting minor obstructions, integral linear programming and packing–covering duality. Schrijver treats it as a major survey question, and a July 2026 primary paper develops both theoretical and computational methods around it.
  Sources: [primary 1](https://homepages.cwi.nl/~lex/co/), [primary 2](https://arxiv.org/abs/2606.16543v2).

- **Minimally nonideal implies minimally nonpacking** — If a minimally nonideal hypergraph has minimum edge size times covering number equal to ground-set size plus one, must it be minimally nonpacking?
  Source: Survey Question 69; file p. 1498. Status: `source_open_unchecked`. Selection: `not_imported`.

- **Covering number of ideal minimal nonpackers** — Does every ideal minimally nonpacking hypergraph have covering number two?
  Source: Survey Question 70; file p. 1499. Status: `source_open_unchecked`. Selection: `not_imported`.

- **The binary ideal T30 obstruction** — Is T30 the unique minor-minimal binary ideal hypergraph whose two-fold packing number is less than twice its covering number?
  Source: Survey Question 71; file p. 1499. Status: `source_open_unchecked`. Selection: `not_imported`.

- **Dyadic packing of ideal hypergraphs** — Does every ideal hypergraph attain its covering number by fractional packing with denominator a power of two; does denominator four always suffice?
  Source: Survey Question 72; file p. 1499. Status: `source_open_unchecked`. Selection: `not_imported`.

- **GCD of exact fractional-packing denominators** — For every ideal hypergraph, is the greatest common divisor of exact packing denominators either one or two?
  Source: Survey Question 73; file p. 1499. Status: `source_open_unchecked`. Selection: `not_imported`.

- **Binary hypergraph half-integral min-max characterization** — Are the three weighted packing, half-integral packing, and excluded-minor conditions in source Question 74 equivalent?
  Source: Survey Question 74; file p. 1499. Status: `source_open_unchecked`. Selection: `not_imported`.

- **One-cycling and one-flowing binary matroids** — Are the one-cycling and one-flowing properties equivalent for binary matroids, with exactly the three excluded minors specified in source Question 75?
  Source: Survey Question 75; file p. 1499. Status: `source_open_unchecked`. Selection: `not_imported`.

## Combinatorial Optimization: Theory and Algorithms

Bernhard Korte; Jens Vygen · source `personal-233`

- **Additive-one bin packing** — Is there a polynomial-time bin-packing algorithm that uses at most one more bin than optimum?
  Source: Bin packing; file p. 495. Status: `source_open_unchecked`. Selection: `related_existing_record`. Catalogue: TCS-6640.
  Decision: Additive one is stronger than the existing constant-additive-error target. No separate numerical strengthening is imported in this pass.

## Understanding and Using Linear Programming

Jiří Matoušek; Bernd Gärtner · source `personal-159`

- **Strongly polynomial linear programming** — Does general linear programming have a strongly polynomial-time algorithm?
  Source: 6, strongly polynomial algorithms; file p. 114. Status: `source_open_unchecked`. Selection: `existing_record`. Catalogue: TCS-0008.
  Decision: Same target is already represented; retain its existing identifier.

## The Traveling Salesman Problem: A Computational Study

David L. Applegate; Robert E. Bixby; Vašek Chvátal; William J. Cook · source `personal-138`

- **Exact separation of TSP comb inequalities** — Is exact separation of comb inequalities polynomial-time solvable when the input point satisfies all subtour constraints, or is it NP-hard?
  Source: Comb inequalities; file p. 198. Status: `source_open_unchecked`. Selection: `not_imported`.

## Algorithmic Number Theory, Volume 1: Efficient Algorithms

Eric Bach; Jeffrey Shallit · source `personal-152`

- **Linear-time integer multiplication** — Can two binary integers be multiplied in linear bit time in the source machine model? This differs from nonuniform circuit size.
  Source: Introduction; file p. 15. Status: `source_open_unchecked`. Selection: `existing_record`. Catalogue: TCS-7174.
  Decision: Same target is already represented; retain its existing identifier.

- **Parallel modular inversion** — Is modular inversion in NC, or is it P-complete under the source reductions?
  Source: 5.4; file p. 130. Status: `source_open_unchecked`. Selection: `not_imported`.

- **Factoring over p-adic fields** — Can polynomials over p-adic fields be factored in polynomial time in the representation and precision model of the source?
  Source: Polynomial algorithms; file p. 183. Status: `source_open_unchecked`. Selection: `not_imported`.

## Randomized Algorithms

Rajeev Motwani; Prabhakar Raghavan · source `personal-55`

- **Randomized strongly polynomial linear programming** — Is there a randomized linear-programming algorithm with expected arithmetic-operation count polynomial in the number of variables and constraints?
  Source: Research Problem 9.6; file p. 290. Status: `source_open_unchecked`. Selection: `not_imported`.

- **Deterministic parallel maximum matching** — Can a maximum matching in a general graph be found in NC?
  Source: Research Problem 12.1; file p. 377. Status: `source_open_unchecked`. Selection: `related_existing_record`. Catalogue: TCS-6504.
  Decision: Existing deterministic parallel matching target; consult the canonical general-perfect-matching card to distinguish matching variants.

- **Parallel Delta-plus-one edge colouring** — Is there an NC or RNC algorithm for (Delta+1)-edge-colouring a simple graph?
  Source: Research Problem 12.2; file p. 377. Status: `source_open_unchecked`. Selection: `not_imported`.

- **Discrete logarithms versus factoring** — Can the computational hardness of discrete logarithms be related by reductions to the hardness of integer factoring?
  Source: Number-theoretic algorithms; file p. 418. Status: `source_open_unchecked`. Selection: `not_imported`.

- **NP-hardness of factoring** — Is the search version of integer factoring NP-hard under the relevant reduction convention?
  Source: 14.6; file p. 432. Status: `source_open_unchecked`. Selection: `not_imported`.

## Algorithms on Strings, Trees, and Sequences

Dan Gusfield · source `personal-68`

- **Linear-time match counts** — Can all pattern-versus-text alignment match counts be computed in linear time in the source model?
  Source: 4, match counts; file p. 95. Status: `source_open_unchecked`. Selection: `not_imported`.

- **Comparison-based match counts** — Can match counts be computed in O(m log m) time using only character comparisons?
  Source: Chapter 4, Exercise 8; file p. 106. Status: `source_open_unchecked`. Selection: `not_imported`.

- **Online true suffix-tree construction** — Can all successive true suffix trees be maintained online in linear total time, without explicitly saving every tree?
  Source: Suffix trees, Exercise 6; file p. 141. Status: `source_open_unchecked`. Selection: `not_imported`.

- **Linear-space combinatorial LCS recovery** — Can the source fast combinatorial LCS method recover an actual common subsequence in linear space without increasing its running time?
  Source: Chapter exercises, LCS; file p. 331. Status: `source_open_unchecked`. Selection: `not_imported`.

## Computing Patterns in Strings

Bill Smyth · source `personal-69`

- **Suffix-tree-free linear repetition algorithms** — Can the source repetition-enumeration bound be attained without using suffix trees?
  Source: 12, introduction; file p. 344. Status: `source_open_unchecked`. Selection: `not_imported`.

## Dynamic Graph Algorithms

David Eppstein; Zvi Galil; Giuseppe F. Italiano · source `personal-15`

- **Deterministic polylogarithmic dynamic connectivity** — Can fully dynamic connectivity and two-connectivity attain deterministic polylogarithmic update bounds in the source model?
  Source: 6, open problems; file p. 34. Status: `source_open_unchecked`. Selection: `not_imported`.

## Analytic Combinatorics

Philippe Flajolet; Robert Sedgewick · source `personal-185`

- **Skolem problem** — Is there an algorithm deciding whether a given linear recurrence sequence ever takes value zero?
  Source: Rational functions and recurrences; file p. 281. Status: `source_open_unchecked`. Selection: `not_imported`.

- **Square-lattice self-avoiding walk asymptotics** — Determine the asymptotic number of self-avoiding walks of length n on the square lattice.
  Source: Self-avoiding walks; file p. 379. Status: `source_open_unchecked`. Selection: `not_imported_scope`.
  Decision: A general enumeration/statistical-physics asymptotic problem; no sufficient computational consequence was established for this catalogue’s selection policy.

## Constraint Satisfaction Problem – Lecture Notes

Alexandr Kazda; Miklós Maróti · source `personal-134`

- **Relational width of finite algebras** — If every relation structure compatible with a finite algebra has relational width k, does the algebra have relational width k in the source sense?
  Source: Open Problem 1.4.15; file p. 34. Status: `source_open_unchecked`. Selection: `not_imported`.

## Graphs and Homomorphisms

Pavol Hell; Jaroslav Nešetřil · source `personal-285`

- **Hedetniemi product-colouring conjecture** — Does the chromatic number of the categorical product equal the smaller factor chromatic number?
  Source: Conjecture 2.27; file p. 62. Status: `resolved_negative`. Selection: `not_imported_resolved`.
  Verification: Shitov gives counterexamples to the claimed equality for chromatic number under graph products.
  Sources: [primary 1](https://annals.math.princeton.edu/wp-content/uploads/annals-v190-n2-p06-s.pdf).

- **Finite-domain CSP dichotomy** — Is every fixed finite-template CSP either polynomial-time solvable or NP-complete?
  Source: 5, CSP dichotomy; file p. 165. Status: `resolved_positive`. Selection: `not_imported_resolved`.
  Verification: Bulatov’s dichotomy theorem settles the finite-template classification. Infinite-domain and promise variants remain different questions.
  Sources: [primary 1](https://arxiv.org/abs/1703.03021).

## Sparsity: Graphs, Structures, and Algorithms

Jaroslav Nešetřil; Patrice Ossona de Mendez · source `personal-292`

- **Bounded nonrepetitive colouring of planar graphs** — Is the nonrepetitive chromatic number of planar graphs bounded by an absolute constant?
  Source: 14, nonrepetitive colouring; file p. 351. Status: `resolved_positive`. Selection: `not_imported_resolved`.
  Verification: Dujmovic, Esperet, Joret, Walczak and Wood prove an absolute bound for planar graphs.
  Sources: [primary 1](https://arxiv.org/abs/1904.05269).

- **Sublinear separators versus expansion** — Under the source structural hypotheses, is the existence of sublinear vertex separators equivalent to subexponential omega-expansion?
  Source: Separators and expansion; file p. 394. Status: `source_open_unchecked`. Selection: `not_imported`.

## Large Networks and Graph Limits

László Lovász · source `personal-290`

- **Graph reconstruction** — Do homomorphism counts from all strictly smaller graphs determine every simple graph on at least three vertices?
  Source: Conjecture 5.30; file p. 81. Status: `source_open_unchecked`. Selection: `not_imported`.

- **Aldous–Lyons approximation conjecture** — Is every unimodular random rooted bounded-degree graph approximable by finite graphs in the source local-convergence sense?
  Source: Bounded-degree graph limits; file p. 369. Status: `reported_negative_resolution`. Selection: `not_imported_resolved`.
  Verification: The two Aldous–Lyons papers give a negative resolution. Their claims were checked in the primary abstracts; the long proofs were not independently verified.
  Sources: [primary 1](https://arxiv.org/abs/2408.00110), [primary 2](https://arxiv.org/abs/2501.00173).

## Matroid Theory

James G. Oxley · source `personal-218`

- **Duality of algebraic matroids** — Is the dual of every algebraic matroid algebraic?
  Source: 14.1.12; file p. 475. Status: `source_open_unchecked`. Selection: `not_imported`.

- **Rota finite-field excluded-minor conjecture** — For each finite field, are there finitely many excluded minors for matroid representability over that field?
  Source: 6.5.11 and 14.1; file p. 215. Status: `source_open_unchecked`. Selection: `not_imported`.

## A Graduate Course in Applied Cryptography

Dan Boneh; Victor Shoup · source `boneh_shoup`

- **Cryptographic multilinear maps** — Construct cryptographically secure multilinear maps beyond the bilinear setting with the source security properties.
  Source: 15, multilinear maps; file p. 682. Status: `source_open_unchecked`. Selection: `not_imported`.

- **Uniform discrete-log to CDH reduction** — Can discrete logarithms be reduced uniformly to computational Diffie–Hellman without the auxiliary advice used by the known reduction?
  Source: 16, CDH; file p. 706. Status: `source_open_unchecked`. Selection: `not_imported`.

- **RSA inversion versus factoring** — Does hardness of factoring RSA moduli imply hardness of RSA inversion?
  Source: 16, RSA; file p. 712. Status: `source_open_unchecked`. Selection: `not_imported`.

- **Optimal random-function inversion time-space tradeoff** — Can the source generic time-space tradeoff for inverting a random function with preprocessing be improved?
  Source: 18, function inversion; file p. 757. Status: `source_open_unchecked`. Selection: `not_imported`.

- **Active security of Schnorr identification** — Is the source Schnorr identification protocol secure against active attacks under the discrete-log assumption?
  Source: Schnorr identification; file p. 776. Status: `source_open_unchecked`. Selection: `not_imported`.

- **CCA security of EaMEG** — Can the source EaMEG construction be proved CCA secure in the random-oracle model under a concrete group assumption?
  Source: Encrypted and MACed ElGamal; file p. 821. Status: `source_open_unchecked`. Selection: `not_imported`.

## Foundations of Databases

Serge Abiteboul; Richard Hull; Victor Vianu · source `foundations_databases`

- **A logic capturing polynomial time** — Is there a logic capturing all polynomial-time queries on unordered finite structures?
  Source: Queries and order; file p. 448. Status: `source_open_unchecked`. Selection: `existing_record`. Catalogue: TCS-7195.
  Decision: Same target is already represented; retain its existing identifier.

## Elements of Finite Model Theory

Leonid Libkin · source `libkin_fmt`

- **NP versus coNP** — Is NP closed under complement?
  Source: 10, complement closure; file p. 212. Status: `source_open_unchecked`. Selection: `not_imported`.

## Topics and Techniques in Distribution Testing: A Biased but Representative Sample

Clément L. Canonne · source `canonne_distribution_testing`

- **Bipartite collision tester assumptions** — Can the minimum-sample requirement in Theorem 2.14 be relaxed, or is it necessary?
  Source: Open Question 2.1; file p. 90. Status: `source_open_unchecked`. Selection: `not_imported`.

- **Asymmetric testing errors** — Determine optimal sample complexity when Type I and Type II error probabilities are prescribed separately.
  Source: Open Question 2.2; file p. 90. Status: `source_open_unchecked`. Selection: `not_imported`.

- **Testing with dependent samples** — Which distribution testers tolerate limited independence among samples?
  Source: Open Question 2.3; file p. 90. Status: `source_open_unchecked`. Selection: `not_imported`.

- **Exact instance-optimal identity testing** — Remove the truncation-factor gap between instance-dependent identity-testing bounds, or determine the correct dependence.
  Source: Open Question 3.1; file p. 132. Status: `source_open_unchecked`. Selection: `not_imported`.

- **Testing reductions from ordinary learning** — Does Theorem 3.11 have an analogue assuming an ordinary learner instead of an agnostic learner?
  Source: Open Question 3.2; file p. 132. Status: `source_open_unchecked`. Selection: `not_imported`.

- **High-confidence instance-dependent testing** — Determine tight confidence dependence in the instance-dependent lower bounds of Section 3.5.
  Source: Open Question 3.3; file p. 132. Status: `source_open_unchecked`. Selection: `not_imported`.

- **Soft information constraints** — Minimize distribution-testing cost under a general cost function for user communication or privacy.
  Source: Open Question 4.1; file p. 144. Status: `source_open_unchecked`. Selection: `not_imported`.

- **Heterogeneous information constraints** — Develop testing techniques for users with different privacy, bandwidth or channel constraints.
  Source: Open Question 4.2; file p. 144, 145. Status: `source_open_unchecked`. Selection: `not_imported`.

- **Testing with an unknown domain at users** — What distributed uniformity testing is possible when only the server knows the domain size?
  Source: Open Question 4.3; file p. 145. Status: `source_open_unchecked`. Selection: `not_imported`.
