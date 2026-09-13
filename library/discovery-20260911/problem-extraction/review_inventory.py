"""Human-authored source questions; present-day verification is a separate layer."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent
ENTRIES = []


def add(source, locator, pages, title, question, kind='question'):
    ENTRIES.append(dict(id=f'{source}:{locator}', source_id=source, source_locator=locator,
                        source_pages=pages if isinstance(pages, list) else [pages],
                        title=title, question=question, kind=kind,
                        current_status='source_open_unchecked',
                        selection='not_imported', catalogue_ids=[]))


# Complete numbered list in Schrijver, Volume C, file pages 1491–1499.
schrijver = [
('P versus NP', 'Is P different from NP?'),
('P versus NP intersect coNP', 'Does P equal NP intersect coNP?'),
('Linear Hirsch bound', 'Does every d-dimensional polytope with m facets have edge diameter at most m-d?'),
('O(nm) maximum flow', 'Can a maximum flow be found in O(nm) time in the source network model?'),
('Berge path-partition conjecture', 'For every minimum k-truncated-size directed path partition, are there k disjoint stable sets meeting each path in min(k, its number of vertices) distinct sets?'),
('Packing common transversals', 'Determine the maximum number of common transversals of two set families whose summed incidence vectors obey a specified integral capacity vector.'),
('Small matching extended formulations', 'Does every matching polytope admit an extended linear formulation of polynomial size?'),
('Tutte five-flow conjecture', 'Does every bridgeless graph admit a nowhere-zero 5-flow?'),
('Tutte four-flow conjecture', 'Does every bridgeless graph with no Petersen minor admit a nowhere-zero 4-flow?'),
('Tutte three-flow conjecture', 'Does every 4-edge-connected graph admit a nowhere-zero 3-flow?'),
('Weak three-flow conjecture', 'Is there an absolute edge-connectivity threshold that guarantees a nowhere-zero 3-flow?'),
('Jaeger circular-flow conjecture', 'For each k at least one, does every 4k-connected graph admit an orientation with outdegree minus indegree divisible by 2k+1 at every vertex? Consult the source for its connectivity convention.'),
('Generalized Fulkerson conjecture', 'In every k-regular graph whose odd cuts have size at least k, do 2k perfect matchings cover every edge exactly twice?'),
('Fulkerson six-matchings conjecture', 'Do six perfect matchings cover every edge of every bridgeless cubic graph exactly twice?'),
('Berge five-matchings conjecture', 'Can every bridgeless cubic graph be covered by five perfect matchings?'),
('Goldberg–Seymour conjecture', 'Is the chromatic index of every multigraph at most the maximum of maximum degree plus one and the ceiling of its fractional chromatic index?'),
('Edge-colouring planar k-graphs', 'Is every planar k-regular graph with every odd cut of size at least k, k-edge-colourable?'),
('Edge-colouring Petersen-minor-free k-graphs', 'Is every Petersen-minor-free k-regular graph with every odd cut of size at least k, k-edge-colourable?'),
('Vizing planar degree-six question', 'Is there a simple planar graph with maximum degree six requiring seven edge colours?'),
('Kempe changes to an optimal edge-colouring', 'Can any edge-colouring be transformed into a minimum edge-colouring using only alternating-path or alternating-cycle colour swaps and removal of unused colours?'),
('List-edge-colouring conjecture', 'Does the list chromatic index equal the ordinary chromatic index for every graph?'),
('Total colouring of simple graphs', 'Does every simple graph have a total colouring using at most maximum degree plus two colours?'),
('Total colouring of multigraphs', 'Is the total chromatic number at most maximum degree plus maximum edge multiplicity plus one?'),
('Integral points in the circuit cone', 'Is every even integral vector in a graph circuit cone a nonnegative integral sum of circuit incidence vectors?'),
('Cycle double cover conjecture', 'Does every bridgeless graph have a multiset of circuits covering each edge exactly twice?'),
('Quarter-integrality of T-join constraints', 'Is the system of T-join constraints totally dual quarter-integral?'),
('Shortest odd paths with conservative weights', 'What is the complexity of a shortest odd s-t path when rational edge lengths give every circuit nonnegative total length?'),
('Two-factors without short circuits', 'What is the complexity of deciding whether a graph has a 2-factor with no circuit of length at most four?'),
('Weighted triangle-free two-factors', 'What is the complexity of finding a maximum-weight 2-factor with no circuit of length at most three?'),
('Five-cycle double cover conjecture', 'Can every bridgeless graph be covered exactly twice by at most five cycles, with cycle interpreted as in the source rather than necessarily a connected circuit?'),
('Duality of algebraic matroids', 'Is the dual of every algebraic matroid also algebraic?'),
('Independent spanning trees', 'If a root has k internally vertex-disjoint paths to every other vertex, do k spanning trees simultaneously realize those internally disjoint root-to-vertex paths?'),
('Computing maximum disjoint dijoins', 'Can a maximum-cardinality family of pairwise arc-disjoint directed-cut covers be computed in polynomial time?'),
('Woodall dijoin-packing conjecture', 'Does the minimum cardinality of a directed cut equal the maximum number of pairwise arc-disjoint dijoins?'),
('Four-thirds subtour integrality gap', 'Is a minimum Hamiltonian tour at most four-thirds of the subtour-elimination linear-programming optimum under the nonnegative edge costs in the source?'),
('Diameter of the TSP polytope', 'Is the edge diameter of the symmetric travelling-salesman polytope of every complete graph at most two?'),
('Augmenting acyclic digraph connectivity', 'For simple acyclic digraphs, is the minimum number of arcs needed for k-vertex-connectivity the larger of the total indegree and outdegree deficits specified by Frank?'),
('Hadwiger conjecture', 'Must every graph of chromatic number at least k contain a complete graph on k vertices as a minor?'),
('Stable sets at bounded cutting-plane rank', 'For each fixed t, is maximum stable set polynomial-time solvable when its polytope arises from the clique relaxation in at most t cutting-plane rounds?'),
('Cutting-plane proof length for stable sets', 'Is there no polynomial bound on the number of cutting-plane additions needed to derive the maximum-stable-set inequality from the edge relaxation?'),
('Chi-boundedness without odd holes', 'Is the chromatic number of every odd-hole-free graph bounded by a function of its clique number?'),
('Recognizing perfect graphs', 'Can perfect graphs be recognized in polynomial time?'),
('Berge alpha-diperfect digraph characterization', 'Are alpha-diperfect digraphs exactly those avoiding the explicitly oriented induced odd circuits specified in source conjecture (20)?'),
('Shannon capacity of odd cycles', 'Does the Shannon capacity of every odd cycle equal its Lovász theta number?'),
('Computing Haemers bound', 'Can Haemers bound on the Shannon capacity of a graph be computed in polynomial time? The underlying field convention must be taken from the source.'),
('Strong t-perfection', 'Is the stable-set description by nonnegativity, edges and odd-circuit inequalities totally dual integral whenever it is integral?'),
('Minimal obstructions to t-perfection', 'Which graphs are minimally non-t-perfect under induced-subgraph deletion and the allowed neighbourhood contractions?'),
('Connectivity forcing k-linkedness', 'Is 2k+2 the minimum vertex-connectivity that guarantees k-linkedness for every k at least two?'),
('Edge-connectivity forcing paired paths', 'Is the edge-connectivity threshold guaranteeing k specified pairwise edge-disjoint paths k for odd k and k+1 for even k?'),
('Directed planar arc-disjoint paths', 'For every fixed k at least two, what is the complexity of k specified arc-disjoint paths in a planar digraph?'),
('Half-integral multiflows for two triangles', 'For two disjoint demand triangles with integral data and the Euler condition, does fractional multiflow feasibility imply half-integral feasibility?'),
('Bounded fractionality with no three disjoint demands', 'Does every demand graph with no three disjoint edges admit a fixed denominator bounding feasible multiflow fractionality for every supply graph and integral capacities and demands?'),
('Okamura half-integral routing conjecture', 'If the supply graph is l-edge-connected and every cut of the demand graph has at most l edges, is there a half-integral routing of the demands?'),
('Mader matroids as gammoids', 'Is every Mader matroid a gammoid?'),
('Representability of Mader matroids', 'Is every Mader matroid linearly representable?'),
('Planar outer-face edge-disjoint paths', 'Is the undirected edge-disjoint paths problem polynomial-time solvable when all terminals lie on the outer face of a planar graph?'),
('Planar multiflows on finitely many faces', 'Is integer multiflow polynomial-time solvable when supply and demand graphs are jointly planar and demands span a fixed number of supply faces?'),
('Quarter-to-half-integral toroidal routing', 'When the union of supply and demand graphs embeds in the torus, does quarter-integral edge-disjoint routing imply half-integral routing?'),
('Packing cuts in planar bipartite graphs', 'Can disjoint cuts realize all required distances among outer-face vertices and a fixed boundary root in the manner stated in source Question 59?'),
('Cut Hilbert bases under minors', 'Is the class of graphs whose cut incidence vectors form a Hilbert base closed under taking minors?'),
('Weighted fractional hypergraph matching bound', 'Does every nonnegative edge-weighted hypergraph have a matching whose sum of (edge size minus one plus reciprocal edge size) times edge weight is at least the fractional matching optimum?'),
('Ideal binary hypergraph characterization', 'Is a binary hypergraph ideal exactly when it excludes the three minors O(K5), its blocker, and F7 specified by Seymour?'),
('Minor witnesses for weighted blocking inequalities', 'Can every violation of the weighted blocking inequality for a hypergraph without a Jn minor be witnessed by zero-one weights on a minor with the source covering-number bounds?'),
('Minor attainment of a nonideal covering minimum', 'For a nonideal hypergraph, is the minimum covering number among nonideal parallelizations and minors already attained by a minor?'),
('Finitely many large minimally nonideal hypergraphs', 'Are there only finitely many minimally nonideal hypergraphs having both minimum edge size and covering number greater than two?'),
('Uniform bound for minimally nonideal hypergraphs', 'Is one of minimum edge size and covering number bounded by an absolute constant in every minimally nonideal hypergraph?'),
('Lehman structure for minimal k-packing obstructions', 'Must every minor-minimal hypergraph with the source strict k-fold covering inequality contain a Jn minor or satisfy the specified Lehman regularity conditions?'),
('Conforti–Cornuéjols packing conjecture', 'Does every clutter with the packing property have the max-flow min-cut property; equivalently, is every packing hypergraph Mengerian?'),
('Minimally nonideal implies minimally nonpacking', 'If a minimally nonideal hypergraph has minimum edge size times covering number equal to ground-set size plus one, must it be minimally nonpacking?'),
('Covering number of ideal minimal nonpackers', 'Does every ideal minimally nonpacking hypergraph have covering number two?'),
('The binary ideal T30 obstruction', 'Is T30 the unique minor-minimal binary ideal hypergraph whose two-fold packing number is less than twice its covering number?'),
('Dyadic packing of ideal hypergraphs', 'Does every ideal hypergraph attain its covering number by fractional packing with denominator a power of two; does denominator four always suffice?'),
('GCD of exact fractional-packing denominators', 'For every ideal hypergraph, is the greatest common divisor of exact packing denominators either one or two?'),
('Binary hypergraph half-integral min-max characterization', 'Are the three weighted packing, half-integral packing, and excluded-minor conditions in source Question 74 equivalent?'),
('One-cycling and one-flowing binary matroids', 'Are the one-cycling and one-flowing properties equivalent for binary matroids, with exactly the three excluded minors specified in source Question 75?'),
]
assert len(schrijver) == 75
for i, (title, question) in enumerate(schrijver, 1):
    page = next(p for hi, p in [(8,1491),(13,1492),(22,1493),(32,1494),(39,1495),(49,1496),(61,1497),(69,1498),(75,1499)] if i <= hi)
    add('personal-234', f'Survey Question {i}', [page, page+1] if i in [22,32,39,61] else page, title, question)

# Complete numbered chapter of Barenboim–Elkin. These are source-era targets.
distributed = [
(147,'Distributed derandomization','Develop a general derandomization method for distributed message-passing algorithms.'),
(148,'Polylogarithmic deterministic MIS','Can maximal independent set be computed deterministically in polylogarithmic LOCAL rounds?'),
(148,'Polylogarithmic near-linear-palette colouring','Can a proper vertex colouring with Delta times polylog(Delta) colours be computed deterministically in polylogarithmic rounds?'),
(148,'Polylogarithmic deterministic edge colouring','Can a proper (2Delta-1)-edge-colouring be computed deterministically in polylogarithmic rounds?'),
(149,'MIS with bounded neighbourhood independence','Is deterministic polylogarithmic-round MIS possible when neighbourhood independence is at most two?'),
(149,'Sublinear dependence on maximum degree','Can the listed symmetry-breaking problems be solved in o(Delta)+log-star(n) deterministic rounds?'),
(149,'Efficient defective colouring','Can a (Delta/p)-defective colouring using O(p) colours be computed efficiently in the distributed model?'),
(150,'Large-arboricity deterministic symmetry breaking','Are deterministic polylogarithmic-round symmetry-breaking algorithms possible beyond polylogarithmic arboricity?'),
(150,'Sublogarithmic sparse-graph symmetry breaking','Can deterministic sublogarithmic rounds handle MIS and colouring at arboricity Omega(sqrt(log n)), and matching and edge colouring at arboricity Omega(log n)?'),
(150,'Distributed decomposition below twice the arboricity','Can a graph of arboricity a be efficiently decomposed into fewer than 2a forests in the distributed model?'),
(150,'Improving arboricity-dependent palettes','Can deterministic O(log n)-round colouring use substantially fewer than a squared colours for arboricity a?'),
(151,'Randomized MIS in square-root-logarithmic time','Is randomized O(sqrt(log n))-round MIS possible in all graphs, and what is its optimal randomized complexity?'),
(151,'Randomized MIS on low-arboricity graphs','Improve the source randomized MIS bounds for graphs of bounded arboricity.'),
(151,'Randomized maximal matching in square-root-logarithmic time','Is randomized O(sqrt(log n))-round maximal matching possible in all graphs?'),
(151,'Randomized MIS complexity on unoriented trees','Is the randomized LOCAL complexity of MIS on unoriented trees Theta(sqrt(log n))?'),
(152,'Randomized Delta-plus-one colouring complexity','Determine the optimal randomized LOCAL round complexity of proper (Delta+1)-vertex-colouring.'),
(152,'Log-star randomized colouring at small degree','Can randomized O(log-star n)-round colouring with O(Delta) colours extend to sublogarithmic maximum degree?'),
]
for i, (page,title,question) in enumerate(distributed,1):
    add('personal-283',f'Open Problem 11.{i}',page,title,question,
        'research_direction' if i in [1,7,10,11,13] else 'question')


# Further individually read passages, including related questions in different books.
other = [
('personal-270','1.1.1',40,'Physical universality of quantum computation','Can the standard universal quantum-computer model efficiently simulate every physically realizable system? The physical theory and simulation criterion remain to be specified.'),
('personal-270','1.4',74,'P versus NP','Does every polynomially verifiable decision problem have a deterministic polynomial-time algorithm?'),
('personal-270','1.4, quantum complexity',75,'NP inside BQP','Can bounded-error polynomial-time quantum computation solve every problem in NP?'),
('personal-270','5, final discussion',277,'Quantum graph isomorphism','Is graph isomorphism solvable by a polynomial-time quantum algorithm?'),
('personal-270','Chapter 5, hidden-subgroup discussion',278,'Efficient nonabelian hidden-subgroup measurements','Can the information obtainable with few hidden-subgroup oracle queries be decoded using a polynomial number of quantum operations?'),
('personal-270','12, product-state capacity',87,'Additivity of classical quantum-channel capacity','Does entanglement across channel uses fail to increase classical communication capacity beyond the product-state expression?'),
('personal-270','Problem 12.7, historical discussion',640,'Quantum channel capacity','Determine quantum-channel capacity. The source-era discussion predates the general regularized coding theorem; particular single-letter capacities are separate questions.'),
('personal-270','Appendix 3',651,'Optimal Solovay–Kitaev exponent','How small can the approximation-length exponent be in the Solovay–Kitaev setting described by the source?'),
('personal-270','Appendix 4, RSA',677,'RSA inversion versus factoring','Does hardness of integer factorization imply hardness of RSA inversion in the source key distribution?'),
('personal-274','Chapter 15, hidden variables',213,'Robustness of the Schrödinger hidden-variable theory','Does the source transition matrix vary continuously under small changes of the unitary and initial state?'),
('personal-274','Chapter 17',239,'Classical-oracle QMA versus QCMA separation','Is there a classical oracle relative to which quantum witnesses are more powerful than classical witnesses?'),
('personal-274','Chapter 23',335,'More-than-exponential certified randomness expansion','Can quantum-device protocols expand a random seed by more than an exponential factor with the source certification requirements?'),
('personal-275','Quantum walks, triangle finding',71,'Quantum triangle query complexity','What is the optimal bounded-error quantum query complexity of detecting a triangle in a graph?'),
('personal-275','Quantum walks, triangle running time',71,'Quantum triangle time complexity','What is the optimal quantum time complexity of triangle detection in the source input-access model?'),
('personal-7','34, NP-completeness',990,'P versus NP','Is P a proper subset of NP?'),
('personal-6','Complexity classes',133,'P versus NP','Does nondeterministic polynomial time exceed deterministic polynomial time?'),
('personal-5','1, exponentiation',41,'Exact shortest addition chains','Can a shortest addition chain for a binary integer n be found in time polynomial in its bit length?'),
('personal-5','Splay trees',249,'Splay-tree dynamic optimality','Are splay trees within a universal constant factor of the best offline rotation-based binary search tree on every access sequence?'),
('personal-5','Matrix multiplication',339,'Matrix multiplication exponent two','Is the matrix multiplication exponent equal to two?'),
('personal-5','30.2',417,'NP versus coNP','Does every no-instance of an NP problem have a polynomially verifiable certificate?'),
('personal-5','30.4',419,'Logspace versus polynomial reductions','Does allowing polynomial-time rather than logarithmic-space reductions change which problems are NP-hard in the specified reduction sense?'),
('personal-25','Open Problem B.2',498,'Explicit superlinear Boolean circuit lower bounds','Exhibit an explicitly computable Boolean function, or a linear-output-length Boolean map, whose unrestricted circuit size is not O(n).'),
('personal-25','B.2, multiplication example',498,'Linear-size integer multiplication circuits','Can multiplication of two n-bit integers be computed by Boolean circuits of size O(n)?'),
('personal-25','Open Problem B.6',500,'Explicit superpolynomial formula lower bounds','Exhibit an explicit Boolean function requiring superpolynomial-size Boolean formulas.'),
('personal-25','Open Problem B.7',502,'Explicit hard univariate polynomials','Exhibit an explicit degree-d polynomial whose arithmetic circuit size is not O(log d).'),
('personal-25','B.3.1',502,'Complexity of the rising-factorial polynomial','Does the polynomial (x+1)(x+2)...(x+d) require arithmetic circuits larger than every polynomial in log d?'),
('personal-25','B.3.2',503,'Unrestricted Fourier-transform circuit lower bounds','Does the discrete Fourier transform require more than linear-size arithmetic circuits when scalar constants are unrestricted?'),
('personal-25','B.3.2, Walsh transform',503,'Unrestricted Walsh-transform circuit lower bounds','Does the Walsh transform over the rationals require more than linear-size arithmetic circuits with unrestricted constants?'),
('personal-25','B, proof complexity',506,'Unrestricted Frege lower bounds','Are there propositional tautology families with no polynomial-length Frege proofs?'),
('personal-25','G.4, finite fields',613,'Deterministic construction of finite fields','Can irreducible degree-e polynomials over an arbitrary prime field be constructed in deterministic time polynomial in e and the bit length of the prime?'),
('personal-141','1.5.3',48,'Existence of one-way functions','Do computationally secure one-way functions exist?'),
('personal-141','2.2.4.2',62,'Efficient decoding of random linear codes','Can random constant-rate binary linear codes be efficiently decoded from a constant fraction of errors in the source average-case regime?'),
('personal-141','2, RSA discussion',77,'RSA inversion versus factoring','Can factoring RSA moduli be reduced to RSA inversion with the source key-generation and exponent conventions?'),
('personal-141','2.7.3',112,'Worst-case hardness and one-way functions','Does NP not contained in BPP imply the existence of one-way functions?'),
('personal-141','2.7.3, amplification',113,'Security-preserving amplification for arbitrary one-way functions','Extend the efficient hardness amplification available for one-way permutations to arbitrary weak one-way functions.'),
('personal-141','3.8.3',193,'Efficient generic PRG construction','Obtain a substantially more security-preserving construction of pseudorandom generators from arbitrary one-way functions than the source transformation.'),
('personal-141','4.3.1.5',226,'Perfect versus statistical zero knowledge','Does perfect zero knowledge have the same computational power as statistical zero knowledge?'),
('personal-141','4.12.3',344,'Strict versus expected-time perfect simulation','Does the expected-polynomial-time simulator definition of perfect zero knowledge imply the strict-polynomial-time definition with bounded failure used in this book?'),
('personal-146','8.4, RSA',335,'RSA inversion versus factoring','Does hardness of factoring imply hardness of the RSA problem?'),
('personal-280','Network decomposition, chapter notes',311,'Deterministic polylogarithmic distributed symmetry breaking','Do deterministic polylogarithmic-round algorithms exist for MIS and colouring in the LOCAL model?'),
('personal-282','Atomic objects',422,'Fast atomic shared-memory objects','Can the source atomic-object constructions be made fast enough for the intended applications? No quantitative resolution target is fixed.'),
('personal-282','GHS correctness',547,'Modular proof of the GHS algorithm','Find a decomposed proof of correctness for the GHS distributed minimum-spanning-tree algorithm while preserving its main ideas and complexity.'),
('personal-277','Atomic snapshots',224,'Optimal atomic-snapshot complexity','Can the cost of atomic snapshots be improved in the shared-memory model and cost measure of the source?'),
('personal-277','24.4.3',260,'Splitter-network renaming space','Can the source O(n to the three-halves) space bound for deterministic splitter-network renaming be improved?'),
('personal-159','6, strongly polynomial algorithms',114,'Strongly polynomial linear programming','Does general linear programming have a strongly polynomial-time algorithm?'),
('personal-138','Comb inequalities',198,'Exact separation of TSP comb inequalities','Is exact separation of comb inequalities polynomial-time solvable when the input point satisfies all subtour constraints, or is it NP-hard?'),
('personal-233','Bin packing',495,'Additive-one bin packing','Is there a polynomial-time bin-packing algorithm that uses at most one more bin than optimum?'),
('personal-55','Research Problem 9.6',290,'Randomized strongly polynomial linear programming','Is there a randomized linear-programming algorithm with expected arithmetic-operation count polynomial in the number of variables and constraints?'),
('personal-55','Research Problem 12.1',377,'Deterministic parallel maximum matching','Can a maximum matching in a general graph be found in NC?'),
('personal-55','Research Problem 12.2',377,'Parallel Delta-plus-one edge colouring','Is there an NC or RNC algorithm for (Delta+1)-edge-colouring a simple graph?'),
('personal-55','Number-theoretic algorithms',418,'Discrete logarithms versus factoring','Can the computational hardness of discrete logarithms be related by reductions to the hardness of integer factoring?'),
('personal-55','14.6',432,'NP-hardness of factoring','Is the search version of integer factoring NP-hard under the relevant reduction convention?'),
('personal-68','4, match counts',95,'Linear-time match counts','Can all pattern-versus-text alignment match counts be computed in linear time in the source model?'),
('personal-68','Chapter 4, Exercise 8',106,'Comparison-based match counts','Can match counts be computed in O(m log m) time using only character comparisons?'),
('personal-68','Suffix trees, Exercise 6',141,'Online true suffix-tree construction','Can all successive true suffix trees be maintained online in linear total time, without explicitly saving every tree?'),
('personal-68','Chapter exercises, LCS',331,'Linear-space combinatorial LCS recovery','Can the source fast combinatorial LCS method recover an actual common subsequence in linear space without increasing its running time?'),
('personal-69','12, introduction',344,'Suffix-tree-free linear repetition algorithms','Can the source repetition-enumeration bound be attained without using suffix trees?'),
('personal-15','6, open problems',34,'Deterministic polylogarithmic dynamic connectivity','Can fully dynamic connectivity and two-connectivity attain deterministic polylogarithmic update bounds in the source model?'),
('personal-185','Rational functions and recurrences',281,'Skolem problem','Is there an algorithm deciding whether a given linear recurrence sequence ever takes value zero?'),
('personal-185','Self-avoiding walks',379,'Square-lattice self-avoiding walk asymptotics','Determine the asymptotic number of self-avoiding walks of length n on the square lattice.'),
('personal-134','Open Problem 1.4.15',34,'Relational width of finite algebras','If every relation structure compatible with a finite algebra has relational width k, does the algebra have relational width k in the source sense?'),
('personal-285','Conjecture 2.27',62,'Hedetniemi product-colouring conjecture','Does the chromatic number of the categorical product equal the smaller factor chromatic number?'),
('personal-285','5, CSP dichotomy',165,'Finite-domain CSP dichotomy','Is every fixed finite-template CSP either polynomial-time solvable or NP-complete?'),
('personal-292','14, nonrepetitive colouring',351,'Bounded nonrepetitive colouring of planar graphs','Is the nonrepetitive chromatic number of planar graphs bounded by an absolute constant?'),
('personal-292','Separators and expansion',394,'Sublinear separators versus expansion','Under the source structural hypotheses, is the existence of sublinear vertex separators equivalent to subexponential omega-expansion?'),
('personal-290','Conjecture 5.30',81,'Graph reconstruction','Do homomorphism counts from all strictly smaller graphs determine every simple graph on at least three vertices?'),
('personal-290','Bounded-degree graph limits',369,'Aldous–Lyons approximation conjecture','Is every unimodular random rooted bounded-degree graph approximable by finite graphs in the source local-convergence sense?'),
('personal-218','14.1.12',475,'Duality of algebraic matroids','Is the dual of every algebraic matroid algebraic?'),
('personal-218','6.5.11 and 14.1',215,'Rota finite-field excluded-minor conjecture','For each finite field, are there finitely many excluded minors for matroid representability over that field?'),
('personal-152','Introduction',15,'Linear-time integer multiplication','Can two binary integers be multiplied in linear bit time in the source machine model? This differs from nonuniform circuit size.'),
('personal-152','5.4',130,'Parallel modular inversion','Is modular inversion in NC, or is it P-complete under the source reductions?'),
('personal-152','Polynomial algorithms',183,'Factoring over p-adic fields','Can polynomials over p-adic fields be factored in polynomial time in the representation and precision model of the source?'),
('foundations_databases','Queries and order',448,'A logic capturing polynomial time','Is there a logic capturing all polynomial-time queries on unordered finite structures?'),
('libkin_fmt','10, complement closure',212,'NP versus coNP','Is NP closed under complement?'),
('boneh_shoup','15, multilinear maps',682,'Cryptographic multilinear maps','Construct cryptographically secure multilinear maps beyond the bilinear setting with the source security properties.'),
('boneh_shoup','16, CDH',706,'Uniform discrete-log to CDH reduction','Can discrete logarithms be reduced uniformly to computational Diffie–Hellman without the auxiliary advice used by the known reduction?'),
('boneh_shoup','16, RSA',712,'RSA inversion versus factoring','Does hardness of factoring RSA moduli imply hardness of RSA inversion?'),
('boneh_shoup','18, function inversion',757,'Optimal random-function inversion time-space tradeoff','Can the source generic time-space tradeoff for inverting a random function with preprocessing be improved?'),
('boneh_shoup','Schnorr identification',776,'Active security of Schnorr identification','Is the source Schnorr identification protocol secure against active attacks under the discrete-log assumption?'),
('boneh_shoup','Encrypted and MACed ElGamal',821,'CCA security of EaMEG','Can the source EaMEG construction be proved CCA secure in the random-oracle model under a concrete group assumption?'),
]
for args in other:
    add(*args)


# Complete nine numbered open questions in Canonne's downloaded survey.
canonne = [
('2.1',90,'Bipartite collision tester assumptions','Can the minimum-sample requirement in Theorem 2.14 be relaxed, or is it necessary?','question'),
('2.2',90,'Asymmetric testing errors','Determine optimal sample complexity when Type I and Type II error probabilities are prescribed separately.','question'),
('2.3',90,'Testing with dependent samples','Which distribution testers tolerate limited independence among samples?','research_direction'),
('3.1',132,'Exact instance-optimal identity testing','Remove the truncation-factor gap between instance-dependent identity-testing bounds, or determine the correct dependence.','question'),
('3.2',132,'Testing reductions from ordinary learning','Does Theorem 3.11 have an analogue assuming an ordinary learner instead of an agnostic learner?','question'),
('3.3',132,'High-confidence instance-dependent testing','Determine tight confidence dependence in the instance-dependent lower bounds of Section 3.5.','question'),
('4.1',144,'Soft information constraints','Minimize distribution-testing cost under a general cost function for user communication or privacy.','research_direction'),
('4.2',[144,145],'Heterogeneous information constraints','Develop testing techniques for users with different privacy, bandwidth or channel constraints.','research_direction'),
('4.3',145,'Testing with an unknown domain at users','What distributed uniformity testing is possible when only the server knows the domain size?','question'),
]
for number, pages, title, question, kind in canonne:
    add('canonne_distribution_testing', f'Open Question {number}', pages, title, question, kind)


# Selected passages recovered from scanned books; page numbers are file pages.
for args in [
    ('personal-10','Introduction, derandomization',10,'P versus BPP','Can every bounded-error randomized polynomial-time decision algorithm be derandomized in polynomial time?'),
    ('personal-10','2, elliptic curves',122,'Computing the rank of rational elliptic curves','Is there an unconditional algorithm computing the rank of the group of rational points of every elliptic curve over the rationals?'),
    ('personal-10','Minimum spanning trees, notes',[444,445],'Deterministic linear-time minimum spanning tree','Can an exact minimum spanning tree be computed deterministically in linear time for arbitrary comparable edge weights?'),
    ('personal-26','4.4.2, unknot certificates',[134,135],'Polynomial Reidemeister simplification of the unknot','Can every unknot diagram be simplified to a circle with polynomially many Reidemeister moves in its crossing number?'),
    ('personal-26','11.4',556,'P versus BPP','Does randomized polynomial-time decision computation have the same power as deterministic polynomial time?'),
    ('personal-26','12, square-lattice colouring',642,'Mixing for four- and five-colour square lattices','Establish the source spatial-mixing and Glauber-mixing claims for four and five colours, with boundary conditions specified.','research_direction'),
]:
    add(*args)


def finish():
    path=ROOT/'reviewed-entries.json'
    overrides=ROOT/'decisions.json'
    patches=json.loads(overrides.read_text()) if overrides.exists() else {}
    for entry in ENTRIES:
        entry.update(patches.get(entry['id'],{}))
    assert len({e['id'] for e in ENTRIES})==len(ENTRIES)
    path.write_text(json.dumps(ENTRIES,ensure_ascii=False,indent=2)+'\n')
    print(f'{len(ENTRIES)} human-authored source entries')


if __name__=='__main__':
    finish()
