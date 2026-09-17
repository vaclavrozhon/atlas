"""Finish the individual review of the full Barnette conjecture."""
import sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT/'research/card-completion-20260913'))
from complete_review import complete,ref,block,progress,DATE
from review_queue import read_claims
identifier='TCS-7250'
claim=read_claims(ROOT)[identifier]
notes=[
 'Preserved the full finite simple 3-connected cubic bipartite planar graph target.',
 'Expanded vertex connectivity, crossing-free planarity and the spanning-cycle quantifiers into self-contained definitions.',
 'Replaced the generic proof-assistant criterion with the required complete Lean-checked theorem or finite counterexample.',
 'Separated Hamiltonicity from relaxed subhamiltonian orders, bounded-face-size results and finite-size verification.',
 'Read the original 2025 approximation theorem and February 2026 partition paper, and added the precisely scoped August 2025 bounded-face preprint.',
 'Replaced doubly escaped formula delimiters in inherited context/progress and preserved importance 94.',
]
sources=[
 'Read Bekos–Kaufmann–Pfister, GD 2025 Article 6, full official PDF, abstract, §1 pp. 6:1–6:2, §2 subhamiltonian definition and Theorem 1 p. 6:5. The result guarantees at least 5n/6 original adjacencies in a subhamiltonian order, not a cycle in the original graph.',
 'Read Cambie–Dross–Knauer–La–Valicov, Electronic Journal of Combinatorics 33(1), P1.27, full journal PDF, title-page publication date 13 February 2026 and §1 pp. 1–3, Conjectures 1–4. The general Hamiltonicity conjecture is explicitly retained, alongside its planar-dual forest partition formulation.',
 'Read Schnieders, arXiv:2508.03531v1 (posted 5 August 2025; manuscript cover dated 6 August), abstract and §1 pp. 1–2, Conjecture 1.3, Theorem 1.12 and Corollary 1.13. The Hamiltonicity result imposes face size at most eight; the computational case analysis was not rerun or independently certified.',
 f'Bounded primary-source searches through {DATE} found no verified general resolution. The September 2026 Lean-statement registration explicitly supplies no proof and was not treated as a solution; secondary research dashboards were not used as evidence of theorem correctness.',
]
status='The checked GD 2025 and February 2026 primary papers explicitly retain the full conjecture. The August 2025 face-size-eight preprint treats a restricted class, while the GD result permits missing adjacencies in a planar Hamiltonian augmentation. No general proof or counterexample was verified in the bounded review through the stated date.'
complete(identifier,dict(
 criterion='decision',question_type='yes_no',
 formal=r'''Is every finite simple undirected graph that is 3-connected, cubic, bipartite and planar Hamiltonian?

Equivalently, for every integer \(n\ge4\) and every graph \(G=([n],E)\) satisfying the four properties below, must there exist a bijection \(\pi:\{0,\ldots,n-1\}\to[n]\) such that
\[
\{\pi(j),\pi((j+1)\bmod n)\}\in E
\qquad\text{for every }j\in\{0,\ldots,n-1\}?
\]
The cyclic order must use only edges of the original graph.''',
 definitions=r'''A finite simple undirected graph consists of a finite vertex set \(V\) and a set \(E\) of unordered two-element subsets of \(V\). There are no loops, parallel edges, edge directions or weights. Relabeling the vertices as \([n]=\{1,\ldots,n\}\) imposes no restriction.

Two vertices are joined by a path if there is a finite sequence of vertices starting at one and ending at the other, with each consecutive pair an edge. A graph is connected when every pair of its vertices is joined by a path.

For a subset \(S\subseteq V\), the graph \(G-S\) retains the vertices \(V\setminus S\) and exactly the edges with both endpoints outside \(S\). The graph is 3-connected when \(|V|\ge4\) and \(G-S\) is connected for every \(S\) with \(|S|\le2\). This is vertex connectivity, not merely a condition on deleting edges.

The degree of a vertex is the number of its neighbors. Cubic means that every vertex has degree exactly three, not at most three. Bipartite means that there is a partition \(V=X\sqcup Y\) such that every edge has one endpoint in each part. The partition is not prescribed in advance.

Planar means that vertices can be assigned distinct points in \(\mathbb R^2\) and each edge \(\{u,v\}\) can be drawn as the image of an injective continuous map from \([0,1]\) to \(\mathbb R^2\), with endpoints at \(u,v\), so that no edge interior contains a vertex and different edge images intersect only at their common endpoints. Only existence of such a drawing is required. No embedding, face-size bound, geometric coordinate restriction or condition on a particular outer face is part of the hypothesis.

A Hamiltonian cycle is a cyclic order of all vertices, each appearing exactly once, whose consecutive pairs, including the last and first, are edges. The displayed bijection defines this requirement without choosing an orientation of the undirected cycle. A closed walk that repeats vertices, a set of several disjoint cycles, or a path omitting the closing edge does not satisfy it.

The assertion concerns every graph meeting all four hypotheses, without a bound on the number of vertices or the lengths of face boundaries. It asks for existence of the cycle, not an algorithm with a prescribed running time, and does not require a cycle to contain or avoid any preselected edge.

This is a universal existence proposition. The numerical \(1/100\) approximation convention does not permit a cycle to omit vertices or use added edges.''',
 answer_criterion=r'''Supply a complete Lean-checked proof that every graph satisfying the stated hypotheses has a Hamiltonian cycle, or supply one finite counterexample together with complete Lean-checked proofs of simplicity, 3-connectivity, cubic degree, bipartiteness, planarity and absence of every Hamiltonian cycle. A result for only bounded graph sizes or bounded face sizes is insufficient. A Hamiltonian cycle in a graph obtained by adding edges, or a spanning cyclic order with only some original adjacencies, does not establish the claim.''',
 source_formulation=dict(
 text='The primary source states Barnette’s conjecture as Hamiltonicity of every 3-regular, 3-connected, bipartite planar graph. The card preserves the ordinary finite simple graph convention and requires the cycle in the original graph.',
 caption='Paraphrase of Bekos–Kaufmann–Pfister, §1 p. 6:1; also explicitly Conjecture 1 in the February 2026 partition paper.',
 citation='primary',format='editorial_paraphrase'),
 why='The conjecture asks whether local degree and parity restrictions, together with planar structure and robust connectivity, force one global cycle through every vertex. It is a classical boundary problem for Hamiltonicity, with connections to graph drawing and partitions of planar dual graphs. A proof or counterexample would settle the full structural claim, beyond algorithms for individual instances or restricted families.',
 references=[
 ref('primary','Approximating Barnette’s Conjecture',
  'Michael A. Bekos; Michael Kaufmann; Maximilian Pfister',2025,
  'https://doi.org/10.4230/LIPIcs.GD.2025.6',
  'GD 2025, LIPIcs 357, Article 6; §1 pp. 6:1–6:2, §2 subhamiltonian definition, Theorem 1 p. 6:5'),
 ref('partitions','Partitions of planar (oriented) graphs into a connected acyclic and an independent set',
  'Stijn Cambie; François Dross; Kolja Knauer; Hoang La; Petru Valicov',2026,
  'https://doi.org/10.37236/13673',
  'Electronic Journal of Combinatorics 33(1), P1.27, published 13 February 2026; §1 pp. 1–3, Conjectures 1–4'),
 ref('faces','Barnette Graphs with Faces up to Size 8 are Hamiltonian',
  'Tobias Schnieders',2025,'https://arxiv.org/abs/2508.03531v1',
  'Version 1, posted 5 August 2025; manuscript dated 6 August 2025; §1 pp. 1–2, Conjecture 1.3, Theorem 1.12 and Corollary 1.13; computer-aided proof not independently rerun'),
 ],
 context_blocks=[
 block('The graph properties are jointly restrictive. The February 2026 paper recalls that removing bipartiteness or removing planarity leads to classical conjectures that have counterexamples. The present target keeps all the stated hypotheses.','partitions'),
 block(r'The GD 2025 theorem gives a planar Hamiltonian augmentation whose spanning cyclic order contains at least \(5n/6\) original edges. The remaining adjacencies may be absent from the original graph, so this is not a Hamiltonian cycle in that graph.'),
 block('Schnieders’s August 2025 preprint proves the conjecture for Barnette graphs with every face of size at most eight, as a corollary of a stronger result within that bounded-face setting. The unrestricted conjecture permits larger faces.','faces'),
 block('The planar-dual formulation concerns partitioning the vertices of an Eulerian planar triangulation into two sets, each inducing a forest. The 2026 paper studies related partition problems and explicitly distinguishes them from the unresolved general Hamiltonicity assertion.','partitions'),
 ],
 progress=[
 progress('2025-08-05','The bounded-face preprint gives Hamiltonicity when all face sizes are at most eight.','faces'),
 progress('2025','The GD theorem improves the number of guaranteed original adjacencies in a subhamiltonian cyclic order.'),
 progress('2026-02-13','The published partition paper states the full Hamiltonicity conjecture and its dual form as open.','partitions'),
 progress(DATE,'The review preserves the unrestricted finite graph target, fixes the Lean acceptance criterion and checks the scope of recent partial results.'),
 ],
),notes,sources,status,summary=[
 'Barnette’s conjecture concerns finite simple planar bipartite graphs in which every vertex has degree three and deleting any two vertices leaves the graph connected.',
 'It predicts that every such graph contains a single cycle through every vertex exactly once.',
 'Every edge of that cycle must already belong to the graph.',
 'Recent results cover bounded face sizes or allow missing adjacencies in a Hamiltonian augmentation.',
 'Those partial results do not settle the unrestricted existence claim, which the checked 2026 literature retains as open.',
],expected_sha256=claim['input_sha256'],claim_token=claim['token'])
