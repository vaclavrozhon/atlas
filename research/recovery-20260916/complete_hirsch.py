"""Complete the unrestricted edge-diameter review, including July 2026 work."""
import json
import sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT/'research/card-completion-20260913'))
from complete_review import complete,ref,block,progress
from review_queue import read_claims
identifier='TCS-6573'
old=json.loads((ROOT/'data/cards'/f'{identifier}.json').read_text())
claim=read_claims(ROOT)[identifier]
refs=old['references']
refs[2].update(url='https://arxiv.org/abs/1402.3579v2',
 locator='arXiv v2, submitted 20 March 2014; §1 definitions and §2 Theorem 1, pp. 1–2; the generated PDF displays a later typesetting date')
refs[3]['locator']='Discrete & Computational Geometry 62, 690–699 (2019); online 19 June 2018; publisher abstract states the asymptotic improvement'
refs += [ref('coherent','Any Proof of Polynomial Hirsch Must be Completely Incoherent',
 'Alexander E. Black; Lei Xue',2026,'https://arxiv.org/abs/2607.11628v1',
 'Version 1, 13 July 2026; introduction and Theorem 1.1, pp. 1–3; coherent monotone paths only')]
notes=[
 'Retained bounded and pointed unbounded polyhedra, arbitrary real coordinates, unrestricted undirected edge paths and the assessed importance.',
 'Specified supporting faces, affine dimension, facets, bounded edges, graph distances and the universal order of constants.',
 'Added a complete Lean proof criterion for the statement or its full superpolynomial negation.',
 'Checked the 2026 circuit upper bound and July coherent-path lower bound as different path models.',
 'Separated geometric existence from diameter computation and objective-improving algorithmic navigation.',
]
sources=[
 'Read Todd arXiv 1402.3579v2 §1 definitions and Theorem 1, including n=d and dimension-one boundary cases; it covers pointed unbounded polyhedra.',
 'Checked Santos’s Annals publisher account of the 43-dimensional, 86-facet counterexample to the linear bound.',
 'Read the publisher abstract and publication metadata for Sukegawa’s 2019 asymptotic improvement. The locally saved 2016 paper is a different result and was not substituted for this reference; full 2019 proof not audited.',
 'Read Wulf arXiv 2502.16398v3 abstract and introduction on diameter computation for bipartite perfect-matching polytopes.',
 'Read Natura arXiv 2602.06958v2 introduction, circuit definitions and Theorem 1.1; checked the revision history through 16 September 2026.',
 'Read Black–Xue arXiv 2607.11628v1 introduction and Theorem 1.1, including the definition via a parametric linear objective; the lower bound restricts to coherent monotone paths.',
 'The inherited ETH reference could not be retrieved during this pass; the checked papers independently support the retained general target and status.',
]
status=('The reviewed July 2026 paper still poses the polynomial edge-diameter conjecture and proves a lower bound only for coherent monotone paths. '
 'Natura’s February 2026 preprint states a polynomial circuit-diameter bound, with moves beyond edges. '
 'Neither changes the unrestricted edge-path target, which includes pointed unbounded polyhedra. '
 'A bounded primary-source review through 16 September 2026 found no polynomial upper bound or superpolynomial counterexample for this target; recent cited proofs were not independently certified in full.')
complete(identifier,dict(
 formal=r'''Is the following proposition true? There exist a real constant \(C>0\) and an integer \(k\ge1\) such that for every integer \(d\ge1\) and every nonempty, full-dimensional, pointed convex polyhedron \(P\subseteq\mathbb R^d\), writing \(n\) for its number of facets,
\[
\operatorname{diam}G(P)\le C(n+d)^k?
\]
The same \(C\) and \(k\) must work for all dimensions, all facet counts and all real coefficients defining \(P\). Both bounded and unbounded polyhedra are included.''',
 definitions=r'''A polyhedron is a set \(P=\{x\in\mathbb R^d:Ax\le b\}\), where \(A\) is a real matrix with finitely many rows, \(b\) is a real vector of matching length and inequalities are coordinatewise. Its affine hull is the smallest affine subspace containing it. Full-dimensional means this affine hull is \(\mathbb R^d\); a polyhedron in a larger ambient space is considered in its own affine hull.

Pointed means that there are no \(x\in P\) and nonzero \(v\in\mathbb R^d\) for which \(x+tv\in P\) for every \(t\in\mathbb R\). A nonempty pointed polyhedron has at least one vertex. A bounded polyhedron is called a polytope.

A nonempty proper face is a set \(P\cap\{x:a\cdot x=\beta\}\), where \(a\ne0\), the dot denotes the usual real inner product and \(a\cdot x\le\beta\) for all \(x\in P\). Face dimension means the dimension of its affine hull. A facet is a face of dimension \(d-1\); \(n\) counts the distinct geometric facets, not duplicate or redundant rows of a chosen inequality description. A vertex is a face consisting of one point.

The undirected graph \(G(P)\) has the vertices of \(P\) as its graph vertices. Two distinct vertices are adjacent exactly when the segment joining them is a one-dimensional face. Such a segment is a bounded edge. An unbounded one-dimensional face contributes no new graph vertex and no edge to infinity.

A graph path is a finite sequence of vertices with successive terms adjacent, and its length is its number of edges. Distance is the minimum path length between a pair of vertices, and diameter is the largest such distance. These polyhedral graphs are finite, nonempty and connected; a graph with one vertex has diameter zero. Distances count edges of unit cost, not their Euclidean lengths.

The coefficients may be arbitrary real numbers, and no simplicity, general-position or nondegeneracy hypothesis is imposed. The constants cannot depend on coordinate values or an encoding length. Paths may use edges in either direction; no objective function, monotonicity condition or algorithm for finding a path is specified. Polynomiality requires one exponent independent of dimension.''',
 answer_criterion=r'''Give a complete mathematically correct proof checked in Lean of the displayed proposition or its logical negation. A positive proof must supply universal \(C>0\) and integer \(k\ge1\) and cover every permitted polyhedron and vertex pair. A negative proof must show that for every real \(C>0\) and every integer \(k\ge1\), some permitted \(d\)-dimensional polyhedron with \(n\) facets has a pair of vertices at graph distance greater than \(C(n+d)^k\). Refuting one fixed linear expression, requiring a long path under one pivot rule, or bounding a different notion of distance is insufficient. This binary existence question has no numerical approximation tolerance.''',
 references=refs,
 source_formulation=dict(text='Is the diameter of a polyhedron bounded by a polynomial in its dimension and number of facets?',
 caption='Editorial paraphrase of the polynomial Hirsch question',citation='todd',format='editorial_paraphrase'),
 context_blocks=[
 block('A linear program optimizes a linear function over a polyhedron. Moving between adjacent vertices is the geometric operation behind simplex pivots. The conjecture asks whether every pair of feasible vertices is joined by a short sequence of these moves, before any navigation rule or objective is chosen.','complexity'),
 block(r'The facet count measures the number of essential inequalities. It can be much smaller than the number of vertices: the cube \([0,1]^d\) has \(2d\) facets and \(2^d\) vertices, but diameter only \(d\). Merely bounding distance by the number of vertices therefore does not give the desired polynomial.','todd'),
 block(r'A bound such as \(n^d\) allows the exponent to increase with the dimension. The conjecture demands one fixed exponent, and allows neither the multiplicative constant nor that exponent to depend on the particular polyhedron.','todd'),
 block(r'Santos’s 43-dimensional polytope with 86 facets has diameter greater than 43, refuting the original Hirsch bound \(n-d\) for bounded polytopes. This leaves open all sufficiently large polynomial bounds. The bounded counterexample does not itself show superpolynomial growth.','santos'),
 block(r'Todd proves the general bound \((n-d)^{\log_2 d}\), with the single-vertex boundary cases treated separately. The earlier Kalai–Kleitman bound was \(n^{2+\log_2 d}\). These estimates are quasipolynomial when both parameters vary.','todd'),
 block(r'Sukegawa’s later asymptotic refinement has exponent \(\log_2 d-\log_2\log d+O(1)\) for large \(d\). The exponent still grows without bound, so this improvement does not establish the conjecture.','sukegawa'),
 block('The length of the best available path is different from the length of a path selected by a particular pivot rule. A positive answer would give geometric existence, without supplying a fast procedure for choosing the next edge or guaranteeing objective improvement.','complexity'),
 block(r'Wulf proves that computing diameter is \(\Pi_2^p\)-hard even for bipartite perfect-matching polytopes, the convex hulls of incidence vectors of perfect matchings in bipartite graphs. This is a hardness classification at the second level of the polynomial hierarchy. It concerns finding the value, and is compatible with a polynomial upper bound on that value.','complexity'),
 block(r'Natura’s February 2026 preprint states a circuit-diameter bound \(O(r^2\log r)\) for standard-form polyhedra \(\{x\in\mathbb R^N:Ax=b,\ x\ge0\}\), where \(A\) has full row rank \(r\ge2\). A circuit direction is a nonzero kernel vector whose set of nonzero coordinates contains no smaller support of another nonzero kernel vector. A circuit step moves maximally in a feasible circuit direction and may pass through a higher-dimensional face. Such a walk need not follow graph edges.','circuit'),
 block('A monotone path increases a chosen linear objective. A coherent monotone path is more restricted: it traces optimizers as a second linear objective varies along a line in objective space. Black and Xue’s July 2026 preprint gives polytopes for which every coherent monotone path for the chosen orientation is long. Their restriction is absent from ordinary graph distance.','coherent'),
 block(r'More precisely, their Theorem 1.1 gives, for each \(q\ge3\), a polytope of dimension \(q+1\) with \((2q+1)(q+1)+1\) facets and an objective for which every coherent monotone path has length at least \(2^{q-1}-1\). The paper continues to list the unrestricted polynomial Hirsch question as open.','coherent'),
 ],
 progress=[
 progress('1992','Kalai and Kleitman establish a quasipolynomial general diameter bound.','todd'),
 progress('2010–2012','Santos announces and publishes a bounded counterexample to the original linear Hirsch inequality.','santos'),
 progress('2014-03-20',r'Todd’s revised preprint proves the bound \((n-d)^{\log_2 d}\).','todd'),
 progress('2018–2019','Sukegawa publishes an asymptotic exponent improvement, still outside a uniform polynomial bound.','sukegawa'),
 progress('2025-11-03','Wulf’s revised FOCS paper establishes stronger hardness of computing diameters.','complexity'),
 progress('2026-02-10','Natura’s revised preprint states a polynomial bound for circuit walks, including monotone circuit walks.','circuit'),
 progress('2026-07-13','Black and Xue state exponential lower bounds for coherent monotone paths, while retaining the unrestricted conjecture.','coherent'),
 progress('2026-09-16','The individual review retains the full edge-diameter target and distinguishes these three path models.','coherent'),
 ],
),notes,sources,status,summary=[
 'The polynomial Hirsch conjecture asks for a universal polynomial bound on the edge-graph diameter of every pointed polyhedron.',
 'The parameters are dimension and number of facets, with arbitrary real coordinates and both bounded and unbounded regions allowed.',
 'The original linear bound is false, while known general upper bounds remain quasipolynomial.',
 'Recent results give short circuit walks and long coherent monotone paths, neither of which settles unrestricted edge distance.',
 'The target concerns the existence of short paths and does not require an algorithm to find them.',
],expected_sha256=claim['input_sha256'],claim_token=claim['token'])
