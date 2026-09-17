"""Complete the fixed-k, unbounded-order Erdős girth conjecture."""
import sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];sys.path.insert(0,str(ROOT/'research/card-completion-20260913'))
from complete_review import complete,ref,block,progress,DATE
from review_queue import read_claims
identifier='TCS-6500';claim=read_claims(ROOT)[identifier]
notes=[
 'Retained all fixed integers k at least two, with a separate positive density constant for each k and graphs of unbounded order.',
 'Made the exact quantifier order explicit: no constant uniform in k, no graph at every prescribed order and no efficient explicit construction are required.',
 'Defined simple cycles and prohibited every cycle length from three through 2k, whether induced or not; distinguished this from forbidding only C_2k.',
 'Stated the correct negation as an eventual little-o bound for at least one fixed k, not failure at one graph size or of one construction.',
 'Read the August 2026 ESA source and its current lower-bound model, the 2021 cycle paper and a later restricted-family counterexample paper; preserved the distinction between girth and spanner fault models.',
 'Removed first-person admission language and solution-style derivation, preserved importance 93 and category, and required complete Lean checking.',
]
sources=[
 'Read Bodwin–Lopez, Unconditional Lower Bounds for Degree Fault Tolerant Spanners, ESA 2026 Article 31, publisher dated 25 August 2026: Section 1.1 pp. 31:1–2, Theorem 2, the girth discussion p. 31:2, and Section 1.3. The text records known parameters k in {1,2,3,5} and separates its unconditional degree-fault-tolerant lower bound from the unresolved girth conjecture. Also compared the July 8 arXiv version already cached locally.',
 'Read Conlon, Extremal Numbers of Cycles Revisited, author PDF and primary Caltech record, American Mathematical Monthly 128 (2021), pp. 464–466. Its special even-cycle constructions and discussion of possible C8 behavior do not prove either direction of the unrestricted girth statement. The distinction between a single forbidden cycle and all short cycles is material.',
 'Read Conlon–Mulrenin–Pohoata, Two Counterexamples to a Conjecture about Even Cycles, current author-hosted PDF, abstract and Theorems 1.2, 1.3 and 3.1, accessed 17 September 2026. It refutes a different claim about retaining a positive fraction of edges in C10-free graphs while removing C8, using specified host families. It does not upper-bound every C8-free graph or refute Erdős’s girth conjecture. This bounded check did not independently audit the full proof.',
 f'Bounded later-work searches through {DATE} found no verified resolution of all remaining girth parameters. The card preserves its admitted arbitrarily-large-order convention without asserting an unproved equivalence to a graph at every sufficiently large order.',
]
complete(identifier,dict(
 criterion='construction',question_type='yes_no',
 formal=r'''Is the following assertion true?
\[
 \forall k\in\mathbb Z_{\ge2}\quad
 \exists c_k\in\mathbb R_{>0}\quad
 \forall N\in\mathbb Z_{\ge1}\quad
 \exists n\in\mathbb Z_{\ge N}\quad
 \exists G:\quad
 |V(G)|=n,\qquad |E(G)|\ge c_k n^{1+1/k},\qquad
 \operatorname{girth}(G)>2k,
\]
where \(G\) ranges over finite simple undirected graphs? In words, for every fixed \(k\ge2\), there must be graphs of unbounded order with no cycle of length at most \(2k\) and with a positive constant fraction of \(n^{1+1/k}\) edges.''',
 definitions=r'''A finite simple undirected graph \(G=(V,E)\) has a finite vertex set and an edge set consisting of unordered pairs of distinct vertices. It has no loops, parallel edges, directions or edge weights. For a graph of order \(n\), one may take \(V=\{1,\ldots,n\}\) without restricting the question. Connectivity, regularity, bipartiteness and algebraic structure are not required.

A cycle of length \(\ell\ge3\) is a list of distinct vertices \(v_0,\ldots,v_{\ell-1}\) with edges between each successive pair and between \(v_{\ell-1}\) and \(v_0\). Additional edges among these vertices do not destroy the cycle: the prohibition is on ordinary cycles, not just induced cycles. The girth is the smallest cycle length, with the convention \(\operatorname{girth}(G)=+\infty\) if there is no cycle. Thus \(\operatorname{girth}(G)>2k\) means that no cycle of any length \(3,4,\ldots,2k\) occurs. Forests satisfy this girth requirement, although their edge counts need not satisfy the density requirement.

The exponent \(1+1/k\) is a real exponent with \(n\ge1\). The integer \(k\) is fixed before taking graph orders arbitrarily large. Its constant \(c_k\) must stay positive and independent of \(n\), \(N\) and the particular graph. Different values of \(k\) may use different constants and unrelated graph families. No positive lower bound on \(c_k\) uniform over all \(k\) is requested.

The quantifier \(\forall N\,\exists n\ge N\) requires an unbounded sequence of graph orders. It does not prescribe a graph at every order \(N\), a bound on gaps between successive orders, or one graph simultaneously serving all \(k\). The assertion is purely existential. There is no bound on construction time, no requirement for a uniform algorithm producing the graphs, and no separate computability requirement on the map \(k\mapsto c_k\).

For describing the negation, define \(h_k(n)\) to be the maximum number of edges in a graph on \(n\) vertices with girth greater than \(2k\). This finite maximum exists because there are only finitely many labeled simple graphs of a given order, and the edgeless graph is eligible. The conjecture says that for every fixed \(k\ge2\), the sequence \(h_k(n)/n^{1+1/k}\) stays bounded away from zero along some unbounded sequence of orders. It does not replace the constant factor by a loss that tends to zero, such as a logarithmic denominator.

For context only, a multiplicative \(t\)-spanner of an unweighted graph is a spanning subgraph whose shortest-path distance for every pair connected in the original graph is at most \(t\) times the original distance. Spanner lower bounds motivate the question, but constructing a spanner or proving a lower bound in a stronger fault-tolerance model is not the mathematical target.''',
 answer_criterion=r'''Give a complete Lean-checked proof of the displayed assertion for every integer \(k\ge2\), or a complete Lean-checked proof of its logical negation. An existential or probabilistic construction qualifies if its proof establishes actual finite graphs with all the required bounds; an efficient algorithm is not necessary.

A refutation must establish that for at least one fixed \(k\ge2\),
\[
 \forall c>0\ \exists N\ge1\ \forall n\ge N:
     h_k(n)<c n^{1+1/k},
\]
that is, \(h_k(n)=o(n^{1+1/k})\) as \(n\to\infty\) with that \(k\) fixed. Failure of a particular graph construction, nonexistence at finitely many orders, or a density bound only for a restricted graph family does not establish this negation.

Proving one new value of \(k\), including \(k=4\), is partial progress and does not prove the universal assertion. A construction that forbids only the cycle of length \(2k\), or only induced short cycles, is insufficient. Bounds for graph spanners with additional failure requirements must not be substituted for the required high-girth families. This is a binary exact assertion; no numerical acceptance tolerance applies.''',
 source_formulation=dict(text='The ESA source defines the maximum edge count when every cycle of length at most 2k is forbidden, recalls its order n^{1+1/k} upper bound and states Erdős’s conjecture that the bound is sharp for every fixed k. The card keeps its existing unbounded-order existence interpretation and spells out the constants.',caption='Paraphrase of Bodwin–Lopez, ESA 2026, Section 1.1, pp. 31:1–2.',citation='current',format='editorial_paraphrase'),
 references=[
 ref('current','Unconditional Lower Bounds for Degree Fault Tolerant Spanners','Greg Bodwin; Aleksey Lopez',2026,'https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.ESA.2026.31','Published 25 August 2026; Section 1.1 pp. 31:1–2, Theorem 2, and Section 1.3; degree-fault model distinguished from girth'),
 ref('cycles','Extremal Numbers of Cycles Revisited','David Conlon',2021,'https://authors.library.caltech.edu/records/8w53p-t0j17','American Mathematical Monthly 128, pp. 464–466; special even-cycle constructions and final discussion; author PDF at https://www.its.caltech.edu/~dconlon/Cycles-revisited.pdf'),
 ],
 why='The conjecture asks whether graphs can attain the classical density scale while avoiding all short cycles. Its resolution would clarify the extremal limits of sparse graph representations that preserve distances.',
 context_blocks=[
 block(r'The classical density upper bound is \(h_k(n)=O_k(n^{1+1/k})\). The target asks whether a positive constant fraction of this scale can be attained at unbounded orders for each fixed parameter.','current'),
 block(r'The August 2026 source lists \(k\in\{1,2,3,5\}\) as known cases. For the stated range \(k\ge2\), the first remaining case is \(k=4\): girth at least nine with order \(n^{5/4}\) edges.','current'),
 block('Avoiding a single even cycle is a different extremal condition from avoiding every cycle up to that length. The distinction is especially relevant for algebraic constructions that still contain shorter cycles.','cycles'),
 block('Some researchers have questioned whether the expected density is attainable at all remaining parameters. Limitations of incidence-based constructions give context for that doubt but do not exclude arbitrary graphs.','current'),
 block('The 2026 paper proves unconditional lower bounds for spanners that must tolerate sets of edge failures with bounded degree. Its stronger preservation requirement allows a lower-bound result without settling the original girth conjecture.','current'),
 ],
 progress=[progress('2021','The cycle-construction paper discusses both special even-cycle bounds and reasons to question extensions to further parameters.','cycles'),progress('2026-08-25','The ESA paper retains the girth conjecture and obtains unconditional lower bounds in the degree-fault-tolerant spanner model.','current')],
 related_problem_ids=[i for i in ['TCS-2783','TCS-4210','TCS-5770','TCS-6784','TCS-7305'] if (ROOT/'data/cards'/f'{i}.json').exists()],
),notes,sources,'The ESA paper published 25 August 2026 retains the general girth conjecture, with the known fixed parameters listed separately. Bounded checks through 17 September 2026 found no verified resolution of the remaining all-graph cases. Counterexamples concerning special host families or a different even-cycle conjecture, and unconditional fault-tolerant spanner bounds, do not settle this assertion.',summary=[
 'The Erdős girth conjecture asks for graphs with many edges and no short cycles.',
 'For each fixed integer k at least two, the graphs must avoid every cycle of length at most 2k.',
 'Their number of edges must be at least a positive k-dependent constant times n to the power one plus one over k, at unbounded graph orders.',
 'No efficient construction or coverage of every graph order is required.',
 'A complete Lean-checked resolution must prove all fixed parameters or refute the density scale eventually for at least one of them.',
],expected_sha256=claim['input_sha256'],claim_token=claim['token'])
