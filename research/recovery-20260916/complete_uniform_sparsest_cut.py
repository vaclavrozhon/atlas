"""Complete the all-graph, unweighted uniform Sparsest Cut target."""
import sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];sys.path.insert(0,str(ROOT/'research/card-completion-20260913'))
from complete_review import complete,ref,block,progress,DATE
from review_queue import read_claims
identifier='TCS-7266';claim=read_claims(ROOT)[identifier]
notes=[
 'Retained simple unweighted graphs and unit demand on every unordered vertex pair, with no balance, regularity, connectivity or group-structure promise.',
 'Made the universal constant factor, one uniform classical randomized bit algorithm, worst-case polynomial time on every random tape and per-input success probability explicit.',
 'Required an explicit nonempty proper cut on every execution; approximation is the probabilistic guarantee, including exact zero boundary when the optimum is zero.',
 'Separated cut construction from value estimation, general algorithm lower bounds from gaps of a particular relaxation, and uniform from nonuniform pair demands.',
 'Read the source definition and ARV presentation, checked the 2025 general and special-class advances and the 4 September 2026 Cayley-graph preprint; no general constant approximation was established by these checks.',
 'Preserved importance 94 and category, removed an inactive related link without reviewing its archive, and required a complete Lean-checked resolution.',
]
sources=[
 'Read Rothvoss, arXiv:1607.00854v1, submitted 4 July 2016: Section 1 p. 1 defines uniform and nonuniform demands; Sections 2–5 give the ARV approximation presentation. The source allows weighted capacities; the existing card intentionally selects its simple unweighted graph case.',
 'Read Kolmogorov, ACM Transactions on Algorithms 21(4), published 1 October 2025, primary author-repository abstract at ISTA record 21007 (uploaded 21 January 2026). It simplifies and parallelizes the square-root-logarithmic approximation with a runtime/quality tradeoff, not a constant-factor general approximation.',
 'Read d’Orsi–Jones–Ruotolo–Vadhan–Zhang, APPROX/RANDOM 2025 Article 16, publisher abstract dated 15 September 2025. The near-optimal approximation is for low-degree Abelian Cayley graphs with an exponential degree/error dependence. It still explicitly frames general constant approximation as a fundamental open question.',
 'Read Stamoulis, arXiv:2609.05368v1, submitted 4 September 2026, primary abstract. Its exactness and bounded-gap statements impose finite Abelian Cayley structure and restrictions on characters or generator orders. Its stated 16/15 integrality-gap family concerns a particular SDP; neither direction settles unrestricted polynomial-time algorithms. Full proof not independently audited.',
 'Read Chang–Naor–Ren, Optimal Rounding for Sparsest Cut, STOC 2025, abstract and Section 1/Theorem 1: the sharp square-root-logarithmic Goemans–Linial gap is for general capacities and demands. This is not an impossibility theorem for the uniform all-algorithm target.',
 f'Bounded later-work searches through {DATE} found no verified unconditional resolution of the selected all-graph target. The inactive related ID was checked only for active-file absence.',
]
complete(identifier,dict(
 criterion='tightness',question_type='yes_no',
 formal=r'''Do there exist real constants \(C\ge1\) and \(K>0\), an integer constant \(d\ge1\), and one uniform classical randomized Turing machine \(A\) with the following property? For every finite simple undirected graph \(G\) on \(n\ge2\) vertices, every execution halts within \(K(n+1)^d\) bit operations and outputs a nonempty proper vertex set \(S\). For each fixed input graph,
\[
 \Pr\!\left[\varphi_G(S)\le C\operatorname{OPT}(G)\right]\ge\frac23,
 \qquad
 \operatorname{OPT}(G)=\min_{\varnothing\ne T\subsetneq V(G)}\varphi_G(T),
 \qquad
 \varphi_G(T)=\frac{|E(T,V(G)\setminus T)|}{|T|\,|V(G)\setminus T|}.
\]
The same machine and constants must work for all these graphs.''',
 definitions=r'''The vertex set is \(V(G)=\{1,\ldots,n\}\). The input consists of \(n\) in binary and the explicit symmetric \(n\times n\) Boolean adjacency matrix with zero diagonal. Each edge is an unordered pair of distinct vertices and has unit capacity; there are no parallel edges, additional weights or demand inputs. All finite simple undirected graphs with \(n\ge2\) are allowed, including disconnected graphs, isolated vertices and graphs with no edges.

For a set \(T\), the boundary \(E(T,V(G)\setminus T)\) consists of the edges with exactly one endpoint in \(T\). Every edge is counted once. The denominator counts unordered vertex pairs separated by the cut, each with demand one. It is positive for every allowed nonempty proper set. Thus all objective values and the minimum are well-defined nonnegative rational numbers. The word uniform refers to these equal pair demands, not to equal degrees or to a random input graph.

The output is the length-\(n\) Boolean membership vector of \(S\). On every execution it must encode a nonempty proper subset. The approximation guarantee, which may fail with probability at most \(1/3\), is required separately for each input graph; it is not an average over graphs. Since every output is feasible, its value is automatically at least the optimum. If the graph is disconnected, the optimum is zero, so success requires an output cut with no crossing edge, not merely an additive approximation. There is no balance requirement on the sizes of the two sides, and either a set or its complement represents the same cut value.

The machine uses independent unbiased random bits and otherwise has a fixed finite deterministic program. The total bit-operation bound holds on every possible random tape and includes reading the input, generating and processing random bits, all numerical computations and preprocessing, and writing the membership vector. There is no advice, oracle, uncharged preprocessing, exact real-arithmetic primitive or quantum computation. Intermediate numbers must have finite encodings and their manipulation is charged. The polynomial bound in \(n\) is equivalent to a polynomial bound in the specified explicit input length. All constants are absolute and independent of the input; the target does not prescribe their numerical values.

The output requirement is a cut, not merely an estimate of its optimum value. The denominator is the product of cardinalities above; replacing it by degree volumes gives a different objective. General unequal pair demands, a promised balanced cut and restrictions to regular, dense or algebraically structured graph families are not part of this input model.''',
 answer_criterion=r'''Give a complete Lean-checked proof that such a machine and constants exist, including output feasibility, the per-input approximation probability and the worst-case bit-time bound, or a complete Lean-checked proof of their logical negation.

A negative answer must rule out every fixed finite approximation factor and every uniform randomized polynomial-time algorithm in this model. A growing integrality gap for one linear or semidefinite relaxation does not by itself do this. Conditional inapproximability under an unproved complexity hypothesis establishes only that conditional assertion, with its assumptions and randomized-algorithm implications stated explicitly.

A factor growing with \(n\), an additive-error estimate, a number without a cut, or a result only on a special graph class does not establish the positive target. Results for arbitrary weighted capacities or demands must be shown to cover the selected unweighted uniform instances; hardness for a broader class alone is insufficient.''',
 source_formulation=dict(text='The notes define the uniform cut objective as boundary capacity divided by the number of separated vertex pairs and present the square-root-logarithmic ARV approximation. This card asks whether a constant factor is possible on all simple unweighted graphs, retaining the input restriction of the admitted card.',caption='Paraphrase of Rothvoss (2016), Section 1; explicit unweighted specialization and algorithmic conventions.',citation='primary',format='editorial_paraphrase'),
 references=[
 ref('primary','Lecture Notes on the ARV Algorithm for Sparsest Cut','Thomas Rothvoss',2016,'https://arxiv.org/abs/1607.00854v1','4 July 2016; Section 1 p. 1, uniform versus nonuniform demands; Sections 2–5, approximation presentation'),
 ref('parallel','A simpler and parallelizable O(√log n)-approximation algorithm for SPARSEST CUT','Vladimir Kolmogorov',2025,'https://research-explorer.ista.ac.at/record/21007','ACM Transactions on Algorithms 21(4), 1 October 2025; primary abstract and publication metadata'),
 ref('cayley','Sparsest Cut and Eigenvalue Multiplicities on Low Degree Abelian Cayley Graphs',"Tommaso d’Orsi; Chris Jones; Jake Ruotolo; Salil Vadhan; Jiyu Zhang",2025,'https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.APPROX/RANDOM.2025.16','APPROX/RANDOM 2025 Article 16, 15 September 2025; abstract, graph-class and degree-dependent running time'),
 ref('recent','Integrality Gap Bounds for the Goemans-Linial SDP on Finite Abelian Cayley Graphs','Georgios Stamoulis',2026,'https://arxiv.org/abs/2609.05368v1','4 September 2026; abstract, restricted graph classes and integrality-gap claims; full proof not independently audited'),
 ref('nonuniform','Optimal Rounding for Sparsest Cut','Alan Chang; Assaf Naor; Kevin Ren',2025,'https://doi.org/10.1145/3717823.3718285','STOC 2025; abstract and Section 1, Theorem 1, general capacities and demands'),
 ],
 why='A constant approximation would bound the quality loss for finding sparse graph separations independently of graph size, addressing a central question connecting approximation algorithms and metric geometry.',
 context_blocks=[
 block(r'The ARV approximation gives a factor \(O(\sqrt{\log n})\). The target asks whether the dependence on graph size can be removed entirely, while retaining polynomial running time and an explicit cut output.'),
 block('The 2025 algorithm simplifies and parallelizes the existing approximation framework; the stated quality guarantee still grows with graph size.','parallel'),
 block('Near-optimal approximation is known for low-degree Abelian Cayley graphs with a running-time dependence on degree and accuracy. The algebraic and degree restrictions prevent that statement from covering all input graphs here.','cayley'),
 block('The September 2026 preprint states new exactness and gap bounds for the Goemans–Linial relaxation on finite Abelian Cayley graphs. These are recent restricted-model claims, not a verified general constant-factor algorithm or impossibility theorem.','recent'),
 block('The sharp 2025 rounding result concerns arbitrary capacities and demands and the performance of a particular SDP. Its tight relaxation gap does not characterize the best possible algorithm for unweighted uniform Sparsest Cut.','nonuniform'),
 ],
 progress=[progress('2016-07-04','The source notes present the uniform objective and the ARV approximation.'),progress('2025-09-15','A near-optimal approximation is obtained for low-degree Abelian Cayley graphs.','cayley'),progress('2025-10-01','A simpler, parallelizable algorithm retains a square-root-logarithmic approximation factor.','parallel'),progress('2026-09-04','A new preprint studies integrality gaps on finite Abelian Cayley graphs; its scope does not settle general constant approximation.','recent')],
 related_problem_ids=['TCS-7287'],
),notes,sources,'The bounded primary-source check through 17 September 2026 found no verified resolution of general constant-factor approximation for the selected simple unweighted uniform objective. The 2025 improvements and September 2026 preprint retain graph-class, approximation-factor or relaxation restrictions. The full proof of the recent preprint was not independently audited.',summary=[
 'Uniform Sparsest Cut minimizes the number of crossing edges divided by the number of separated vertex pairs.',
 'The input is an arbitrary explicitly given simple unweighted undirected graph.',
 'The question asks for one randomized polynomial-time algorithm returning a cut within an absolute constant factor of optimum.',
 'Success is required separately on every graph, including finding a zero-boundary cut with the required probability when the optimum is zero.',
 'A complete Lean-checked resolution must settle the all-graph algorithmic target rather than the performance of one relaxation or a special graph class.',
],expected_sha256=claim['input_sha256'],claim_token=claim['token'])
