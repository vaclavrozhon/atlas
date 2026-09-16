"""Individual completion of the existing weighted GNRS formulation."""
import json
import sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT/'research/card-completion-20260913'))
from complete_review import complete,ref,block,progress
from review_queue import read_claims
identifier='TCS-6525'
old=json.loads((ROOT/'data/cards'/f'{identifier}.json').read_text())
claim=read_claims(ROOT)[identifier]
refs=old['references']
for r in refs:
 r['title']=r['title'].replace(r'\(\ell\)\(_{1}\)',r'\(\ell_1\)').replace(r'\(c_{1}(K_{2},_{n})\)',r'\(c_1(K_{2,n})\)')
refs[0]['locator']='Combinatorica 24(2), 233–269 (2004); author manuscript dated 22 October 2002, §§1–3, printed pp. 2–6 / PDF pp. 3–7; FOCS 1999 precursor'
refs[-1]['locator']='Version dated 4 May 2026; Chapter on Sparsest Cut, notes on planar flow-cut gaps and the GNRS conjecture'
refs += [ref('multicut2025','Improved Lower Bounds on Multiflow-Multicut Gaps',
    'Sina Kalantarzadeh; Nikhil Kumar',2025,
    'https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.APPROX-RANDOM.2025.14',
    'APPROX/RANDOM 2025; §2 distinguishes concurrent-flow/cut gaps from multiflow/multicut gaps and records the planar GNRS gap')]
notes=[
 'Retained the original all-fixed-excluded-minors, arbitrary-positive-weights existence target and assessed importance.',
 'Rewrote the full quantifier order, finite target dimension, exact noncontraction convention and permitted constant dependence.',
 'Explained the source nonnegative-weight convention by contracting zero-distance components, without imposing bounded aspect ratio or an algorithmic target.',
 'Corrected split ell-one notation and the complete bipartite graph subscript in titles, progress and context.',
 'Rechecked restricted-family results and distinguished the stronger Sherali–Adams relaxation and multiflow/multicut gaps from the conjecture.',
]
sources=[
 'Read the original author manuscript dated 22 October 2002, §§1–3: weighted minor-free conjecture, metric and cut definitions, distortion convention and concurrent-flow correspondence.',
 'Read Lee–Sidiropoulos arXiv 0910.1409v3 introduction and theorem statements; the consequence concerns fixed pathwidth and exclusion of a fixed tree, not arbitrary fixed treewidth.',
 'Read Chlamtac–Krauthgamer–Raghavendra §1.1–1.2, including its explicit statement that its stronger relaxation does not establish a bound on the ordinary flow-cut gap.',
 'Read Filtser arXiv 1903.02758v4 Theorem 1 and the final publisher abstract; the parameter is the number of faces covering the selected terminals.',
 'Read Mori arXiv 2602.23745v1 §1 and Theorems 1–2, including worst-over-edge-weights definition. No later revision displayed on 16 September 2026. The full proof was not independently certified.',
 'Read Chekuri notes dated 4 May 2026 and APPROX/RANDOM 2025.14 §2; bounded later-work search through 16 September 2026 found no resolution of the all-minors target.',
]
status=('The original source poses constant distortion for every family excluding a fixed minor. '
        'The May 2026 notes still identify the planar constant bound as open. '
        'The checked pathwidth, face-cover and February 2026 complete-bipartite results impose additional restrictions. '
        'The fixed-treewidth approximation result uses a stronger relaxation, and recent multiflow/multicut results concern a different gap. '
        'A bounded primary-source review on 16 September 2026 found no settlement; the cited proofs have not all been independently verified.')
complete(identifier,dict(
 question_type='yes_no',
 formal=r'''Is the following proposition true? For every finite simple graph \(H\), there exists a real constant \(C_H\ge1\) such that, for every nonempty finite connected simple undirected graph \(G=(V,E)\) with no \(H\) minor and every edge-length function \(w:E\to\mathbb R_{>0}\), there exist an integer \(m\ge1\) and a map \(f:V\to\mathbb R^m\) satisfying
\[
d_{G,w}(u,v)\le
\sum_{j=1}^{m}|f(u)_j-f(v)_j|
\le C_H\,d_{G,w}(u,v)
\qquad\text{for every }u,v\in V?
\]
The constant may depend only on \(H\). The dimension and map may depend on the whole weighted graph, with no bound on dimension or on the time needed to construct them.''',
 definitions=r'''A finite simple undirected graph consists of a finite vertex set and a set of unordered pairs of distinct vertices, called edges. Connected means every pair of vertices is joined by a path. A graph \(H\) is a minor of \(G\) if deleting vertices or edges and contracting edges, followed by removal of loops and duplicate edges, can produce a graph isomorphic to \(H\). Exclusion concerns the underlying unweighted graph.

The length of a path is the sum of its edge lengths. The shortest-path distance \(d_{G,w}(u,v)\) is the minimum length of a path from \(u\) to \(v\), and \(d_{G,w}(u,u)=0\). Positivity and finiteness make this a finite metric. A one-vertex graph is allowed and satisfies the target trivially.

The target space is finite-dimensional \(\ell_1^m\): the vector space \(\mathbb R^m\) with distance \(\|a-b\|_1=\sum_{j=1}^m|a_j-b_j|\). The first inequality fixes a noncontracting normalization, and the second allows expansion by at most \(C_H\). Allowing an arbitrary common scaling factor instead gives the same distortion notion.

All edge lengths are arbitrary positive real numbers. Neither graph size nor the ratio of the largest to the smallest edge length may affect \(C_H\). There is no requirement that the graph or its lengths be efficiently encoded, since this is a mathematical existence question. All pairs must satisfy the inequalities simultaneously for the same map.

The source also allows zero edge lengths and hence zero distances between different vertices. That convention is equivalent for this conjecture: contract each component of zero-length edges, retain the shortest parallel edge when necessary, and map the original vertices through this quotient. The quotient is still a minor of the original graph. The positive-length statement above avoids treating distinct points at distance zero as a metric space.

No Euclidean target, restriction to selected terminals, average-distance guarantee, or transformation of the distances by a power is part of this statement. Here a terminal, when used in the context, simply means a selected vertex whose distances must be preserved.''',
 answer_criterion=r'''Supply a complete mathematically correct proof checked in Lean of the displayed proposition or its logical negation. A positive answer must obtain a finite constant for every fixed excluded minor, uniformly over all weighted graphs in that class and all vertex pairs. It need not determine the best constant or construct the embeddings efficiently. A negative answer must give one fixed graph \(H\) such that for every real \(C\ge1\), some finite connected positively weighted \(H\)-minor-free graph admits no map into any finite-dimensional \(\ell_1\) space satisfying both inequalities with factor \(C\). Failure at one fixed distortion value is insufficient if a larger uniform value remains possible. This binary existence claim has no additive numerical tolerance.''',
 references=refs,
 source_formulation=dict(text='Every family of graphs excluding a fixed minor has a uniform constant bound on the distortion needed to embed all its weighted shortest-path metrics into ell-one.',
     caption='Editorial paraphrase of the original conjecture',citation='original',format='editorial_paraphrase'),
 context_blocks=[
     block(r'The conjecture links a qualitative restriction on graph structure to quantitative preservation of every distance. Removing one fixed graph from the set of permitted minors is predicted to prevent any distortion that grows with graph size, despite arbitrary edge lengths.','original'),
     block(r'Finite \(\ell_1\) metrics are exactly nonnegative combinations of cut metrics. A cut metric has value one on pairs separated by a vertex subset and zero on other pairs. This connects distance representation to weighted separation of vertices and hence to graph partitioning.','original'),
     block('In the equivalent routing formulation, capacities are attached to graph edges and demands to arbitrary vertex pairs. A concurrent flow routes the same fraction of every demand, allowing a demand to split among paths. The flow-cut gap compares the best achievable fraction to the upper bound imposed by the sparsest cut. The conjecture predicts a constant gap on every fixed-minor-free family.','original'),
     block('Demands in this correspondence may join any pairs; they need not themselves form a planar or minor-free graph. The multiflow/multicut optimization studied in recent work has a different objective and gap, so its constant bounds do not resolve the conjecture.','multicut2025'),
     block('The planar case is already unresolved in the checked 2026 account: the upper bound grows as the square root of the logarithm of the number of vertices, while no superconstant lower bound is known there. Trees and several other restricted families do have constant bounds.','notes'),
     block('Lee and Sidiropoulos establish a constant bound on every minor-closed family excluding a fixed tree. Their stronger random-tree result applies to bounded pathwidth, a restriction stronger than bounded treewidth.','pathwidth'),
     block('A constant-factor sparsest-cut approximation on fixed-treewidth graphs is known using the Sherali–Adams hierarchy. The authors explicitly distinguish its stronger relaxation from the ordinary concurrent-flow relaxation, whose gap is the relevant one here.','treewidth'),
     block(r'For planar graphs with a selected terminal set covered by \(\gamma\) faces of a drawing, Filtser obtains distortion \(O(\sqrt{\log(\gamma+1)})\). The added one handles the single-face boundary case in asymptotic notation. The number of covering faces is unbounded in the general conjecture.','faces'),
     block(r'Mori’s February 2026 preprint states that the worst distortion over edge lengths of \(K_{2,n}\) is \((3k-2)/(2k-1)\), where \(k=\lceil n/2\rceil\) and \(n\ge1\). Here \(K_{2,n}\) has two independent parts of sizes two and \(n\), with all edges between them. These values tend to \(3/2\), so this is progress within a bounded-distortion family.','exact'),
 ],
 progress=[
     progress('1999–2004','The original work formulates the conjecture and proves constant distortion for restricted classes, including series-parallel graphs.','original'),
     progress('2012','The checked final preprint establishes the bounded-pathwidth result and the consequence for families excluding a fixed tree.','pathwidth'),
     progress('2010','A stronger relaxation gives constant-factor sparsest-cut approximation on every fixed-treewidth class, without proving the ordinary flow-cut-gap conjecture.','treewidth'),
     progress('2024-11-22','The journal publication improves the planar terminal face-cover distortion bound.','faces'),
     progress('2026-02-27',r'The preprint states exact worst-weight distortion values for \(K_{2,n}\).','exact'),
     progress('2026-09-16','The individual review retained the general conjecture and checked the scope of the later restricted-family results.','original'),
 ],
),notes,sources,status,summary=[
 r'The GNRS conjecture asks whether weighted graphs excluding a fixed minor have shortest-path metrics that embed into \(\ell_1\) with bounded distortion.',
 'The bound may depend on the excluded graph but must be independent of graph size and all edge lengths.',
 'One map must preserve every pairwise distance, with no required algorithm or target-dimension bound.',
 'The equivalent routing formulation predicts a constant concurrent-flow versus cut gap for arbitrary demands.',
 'The checked restricted-family results leave the general conjecture, including its planar case, unresolved.',
],expected_sha256=claim['input_sha256'],claim_token=claim['token'])
