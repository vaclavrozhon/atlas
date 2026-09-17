"""Complete the finite six-perfect-matching exact-cover conjecture."""
import sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT/'research/card-completion-20260913'))
from complete_review import complete,ref,block,progress,DATE
from review_queue import read_claims
identifier='TCS-7249'
claim=read_claims(ROOT)[identifier]
notes=[
 'Preserved finite loopless bridgeless cubic multigraphs, distinct edge identities and repeated perfect matchings.',
 'Expanded componentwise scope, the empty case, matching incidence and exact multiplicity-two coverage.',
 'Made the complete Lean-checked proof or finite-counterexample criterion explicit, without imposing a running-time bound.',
 'Checked the July 2026 finite/infinite equivalence preprint and the July 2026 finite restricted-family paper, distinguishing both from a proof of the full conjecture.',
 'Preserved the existing importance score 94 and current substantive related-card links.',
]
sources=[
 'Read Magalhães Júnior–Silva, arXiv:2607.29511v1 (31 July 2026), abstract and §1 pp. 1–3, Conjectures 1.1–1.4, Theorems 3.1–3.4 and Corollary 3.6 as stated in the introduction. The source explicitly retains the finite Berge–Fulkerson conjecture as open; equivalence with an infinite version is not a proof of either. The full compactness proof was not independently certified.',
 'Read the publisher abstract and metadata of Luo–Hao–Luo–Zhang–Zhou, Journal of Graph Theory, online 14 July 2026, DOI 10.1002/jgt.70097. It restates the general conjecture and proves a restricted permutation-graph result involving a short alternating circuit. Full text was not accessible, so this card uses only the directly stated scope and does not certify its proof.',
 'Read Ulyanov, arXiv:2501.05348v3 (24 March 2026), abstract and version history. It proposes an oriented strengthening and verifies a special family, not the full un-oriented conjecture. No broad resolution was inferred from the title or the version note about new proofs.',
 f'Bounded primary-source searches through {DATE} found no verified general resolution. Secondary theorem dashboards and incomplete computational proof projects were not used as evidence of a completed theorem.',
]
status='The July 2026 primary sources explicitly retain the full finite conjecture. One proves results for a restricted family, and the other studies equivalence with an infinite version while keeping the finite assertion open. No complete general proof or counterexample was verified in the bounded review.'
complete(identifier,dict(
 criterion='decision',question_type='yes_no',
 formal=r'''Does every finite loopless bridgeless cubic multigraph \(G=(V,E)\) admit a list of six perfect matchings \(M_1,\ldots,M_6\subseteq E\) such that
\[
\forall e\in E,\qquad
\bigl|\{i\in\{1,\ldots,6\}:e\in M_i\}\bigr|=2?
\]
The six entries may repeat. Their union must cover every edge, and every edge must occur in exactly two list positions.''',
 definitions=r'''A finite loopless multigraph has finite sets \(V\) of vertices and \(E\) of edge identities, with a map assigning to each \(e\in E\) an unordered pair of distinct endpoints in \(V\). Different edges may have the same endpoint pair; they remain different elements of \(E\). There are no loops, directions or weights.

An edge is incident with each of its two endpoints. The degree of a vertex counts incident edge identities, including parallel edges separately. Cubic means that every vertex has degree exactly three.

Two vertices are connected if there is a finite path between them, with each consecutive pair joined by an edge. The connected components are the equivalence classes of this relation. Deleting an edge removes that edge identity only and keeps all vertices and other edges. An edge is a bridge if deleting it increases the number of connected components. Bridgeless means that no edge has this property.

A matching is a set \(M\subseteq E\) with at most one incident edge in \(M\) at each vertex. It is perfect if every vertex has exactly one incident edge in \(M\):
\[
\forall v\in V,\qquad
\bigl|\{e\in M:v\text{ is an endpoint of }e\}\bigr|=1.
\]
Thus a perfect matching meets all vertices, not merely some largest possible number of vertices.

The output object is an ordered six-tuple of edge subsets, although its ordering has no mathematical significance beyond counting multiplicities. If \(M_i=M_j\) for two different indices, an edge in that common subset contributes once at index \(i\) and once at index \(j\). The matchings need not be distinct and need not be edge-disjoint.

Disconnected graphs are permitted. One six-tuple must cover the whole graph, with each of its entries a perfect matching on every component. The empty graph is also permitted: the six empty matchings satisfy the conclusion. There is no assumption of planarity, bipartiteness, simplicity, a prescribed edge coloring or a bound on graph size.

The quantifiers are \(\forall G\,\exists(M_1,\ldots,M_6)\,\forall e\). This is an existence question with no requirement to compute the matchings within a time or space bound. Each matching must consist solely of original edge identities.

Exact multiplicity two and exactly six list positions are part of the proposition. This is not a numerical approximation question: average coverage, fractional weights, an unspecified number of matchings or coverage of almost all edges does not meet the statement.''',
 answer_criterion=r'''Supply a complete Lean-checked proof of the proposition for every finite loopless bridgeless cubic multigraph, or supply one finite multigraph and complete Lean-checked proofs that it satisfies the hypotheses and admits no such six-tuple. A result for a proper graph family, a bound on the fraction of edges covered, or a different collection of cycles or matchings is insufficient unless accompanied by a proved implication establishing this exact target. An equivalence with another unresolved conjecture does not by itself settle the assertion.''',
 source_formulation=dict(
 text='Conjecture 1.1 asserts that every bridgeless cubic graph has six perfect matchings covering each edge exactly twice. This card preserves the finite multigraph version, with repeated matchings and edge multiplicities made explicit.',
 caption='Paraphrase of Magalhães Júnior–Silva, §1, Conjecture 1.1, p. 1; also restated in the July 2026 Journal of Graph Theory abstract.',
 citation='primary',format='editorial_paraphrase'),
 why='One perfect matching selects one incident edge at every vertex. The conjecture asks whether six globally consistent selections can always distribute their incidences evenly across the three edges at each vertex. This exact decomposition problem is central to matching and covering theory for cubic graphs, and it implies other long-standing matching conjectures.',
 references=[
 ref('primary','On some perfect matching conjectures in infinite, cubic, bridgeless graphs',
  'Paulo Magalhães Júnior; Antonio Kelson Silva',2026,'https://arxiv.org/abs/2607.29511v1',
  'Version 1, 31 July 2026; abstract and §1 pp. 1–3, Conjectures 1.1–1.4, Theorem 3.2 and Corollary 3.6 stated in the introduction'),
 ref('partial','Berge–Fulkerson Conjecture, Perfect Matching Partial Coverings and Odd Dividers',
  'Yilun Luo; Rong-Xia Hao; Rong Luo; Cun-Quan Zhang; Wenjuan Zhou',2026,
  'https://doi.org/10.1002/jgt.70097',
  'Journal of Graph Theory, first online 14 July 2026; publisher abstract and metadata, general conjecture and restricted-family result; full proof not checked'),
 ref('oriented','Graph Puzzles I.1: Oriented Berge-Fulkerson Conjecture',
  'Nikolay Ulyanov',2026,'https://arxiv.org/abs/2501.05348v3',
  'Version 3, 24 March 2026, initially posted 9 January 2025; abstract, oriented strengthening and Isaacs flower-snark special case'),
 ],
 context_blocks=[
 block('The exact six-matching cover implies the Fan–Raspaud assertion that there are three perfect matchings with no edge common to all three. This illustrates its place among structural matching conjectures; the weaker assertion alone does not supply the requested cover.'),
 block('If a cubic graph has a proper edge coloring with three colors, each color class is a perfect matching, and repeating those three matchings gives the required six-tuple. The full conjecture also covers graphs for which no such coloring exists.'),
 block('The July 2026 journal article develops relations to partial matching coverings and proves the conjecture for a restricted family of permutation graphs. Its statement does not cover every bridgeless cubic graph.','partial'),
 block('The July 2026 preprint relates the finite conjecture to an infinite analogue. It explicitly presents the finite assertion as open; proving an equivalence between the two versions does not produce the required cover in the finite case.'),
 block('The March 2026 revised preprint studies an oriented strengthening and a specific family. A result about that family does not establish the original conjecture for all cubic graphs.','oriented'),
 ],
 progress=[
 progress('2026-03-24','The revised oriented-cover preprint retains a conjectural general target and proves a special family.','oriented'),
 progress('2026-07-14','The journal article states the general conjecture and proves a restricted-family result.','partial'),
 progress('2026-07-31','The finite/infinite equivalence preprint explicitly retains the finite conjecture as open.'),
 progress(DATE,'The review fixes the finite multigraph and repeated-matching conventions and requires a complete Lean proof of exact multiplicity-two coverage.'),
 ],
),notes,sources,status,summary=[
 'A perfect matching pairs every vertex with exactly one of its neighbors using edges of the graph.',
 'The Berge–Fulkerson conjecture asks for six perfect matchings in every finite bridgeless cubic multigraph.',
 'Each edge must belong to exactly two of the six matchings, and repeated matchings are allowed.',
 'The question has no algorithmic running-time requirement and includes nonplanar graphs and parallel edges.',
 'The checked 2026 results concern special families or equivalence with infinite versions and leave the full finite assertion unresolved.',
],expected_sha256=claim['input_sha256'],claim_token=claim['token'])
