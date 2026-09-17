"""Complete deterministic polynomial-time Exact Matching on general graphs."""
import sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];sys.path.insert(0,str(ROOT/'research/card-completion-20260913'))
from complete_review import complete,ref,block,progress,DATE
from review_queue import read_claims
identifier='TCS-6511';claim=read_claims(ROOT)[identifier]
notes=[
 'Preserved sequential deterministic polynomial-time decision for all simple undirected red/blue graphs, without a bipartite promise.',
 'Expanded the uniform bit-complexity quantifiers, explicit vertex encoding, matching condition, all red counts and empty-graph convention.',
 'Separated exact count from extremal counts, parity and approximate matching, and separated sequential polynomial time from deterministic parallel complexity.',
 'Read the August 2026 randomized-algorithm revision and the April 2026 bipartite preprint’s explicit formalization hypotheses.',
 'Retained cautious attribution of the bipartite claim without accepting its advertised complete formal verification or treating it as a general-graph theorem.',
 'Removed first-person admission language, preserved importance 92 and category and required a complete Lean proof of either direction.',
]
sources=[
 'Read El Maalouly, STACS 2023 Article 29, Introduction and Section 1.1 pp. 29:1–3: the exact decision problem, RP/RNC history, deterministic general-graph question, restricted positive results and distinction from almost-perfect or weighted variants.',
 'Read Sato–Yamaguchi, arXiv:2508.04081v2, 10 August 2026: Introduction and Theorem 1.3 p. 1, Remark 1.7 p. 2 and Section 3. The all-count decision procedure is randomized, with O(n^omega) field operations. The introduction expressly keeps deterministic polynomial time open. The live arXiv history still lists v2 as the latest version on 17 September 2026.',
 'Read Du, arXiv:2604.01571v3, 9 April 2026: stated bipartite scope and Appendix A. The formalization remains conditional on eight structural hypotheses, grouped into McCuaig family visible ASNC, narrow-pair closure, full-state base/propagation and graph-theoretic prerequisites. The review did not execute the Lean project or independently verify the mathematical arguments for those hypotheses. The live history still lists v3 as latest.',
 'Read the primary ETH repository abstract of El Maalouly–Lakis, SOFSEM 2026, Exact Matching and Top-k Perfect Matching Parameterized by Neighborhood Diversity or Bandwidth. It describes restricted parameterized progress and still distinguishes the general deterministic problem; the accepted manuscript is embargoed until 12 February 2027 and was not read.',
 'The Mulmuley–Vazirani–Vazirani 1987 randomized history is supported by the directly read 2023 and 2026 primary papers; no independent audit of the original proof is claimed.',
 f'Bounded primary-source searches through {DATE} found no verified deterministic polynomial-time decision algorithm for all graphs, or unconditional proof that none exists. Generic phrase matches about record linkage, online matching and other optimization objectives were excluded.',
]
complete(identifier,dict(
 title='Deterministic Exact Matching',criterion='models',question_type='yes_no',
 formal=r'''Do there exist a deterministic Turing machine \(A\), a real constant \(K>0\) and an integer \(d\ge1\) such that, for every explicitly given finite simple undirected graph \(G=(V,E)\) with an even number \(n\ge0\) of vertices, every red-edge subset \(R\subseteq E\), and every integer \(0\le k\le n/2\), the machine halts within \(K(L+1)^d\) steps and outputs YES exactly when
\[
 \exists M\subseteq E:\qquad
 \bigl(\forall v\in V,\ |\{e\in M:v\in e\}|=1\bigr)
 \quad\text{and}\quad |M\cap R|=k?
\]
Here \(L\) is the input bit length under the explicit encoding below. No bipartition is promised.''',
 definitions=r'''Vertices are labelled \(1,\ldots,n\), and an edge is an unordered pair of distinct vertices. Loops and parallel edges are excluded. Every edge is either red, meaning it belongs to \(R\), or blue, meaning it belongs to \(E\setminus R\). The graph, all its edges and their colours are given explicitly, not through an oracle or a succinct circuit. One fixed encoding uses a length-prefixed binary header and a list of adjacency records, one for each vertex including isolated vertices, with neighbour labels and colour bits; each undirected edge has consistent entries at both endpoints. The integer \(k\) is in binary. The encoding contains all \(n\) vertex records, so its length is at least \(n\); a binary header alone does not describe exponentially many unlisted vertices.

A matching is a subset of edges no two of which share a vertex. It is perfect if every vertex belongs to one of its edges, equivalently the degree condition in the formula. Every perfect matching then has \(n/2\) edges. The requested count is exactly \(k\) red edges, rather than at least \(k\), at most \(k\) or a count congruent to \(k\) modulo an integer. On the empty graph, the empty matching is perfect and the allowed input \(k=0\) has answer YES.

The machine is one uniform finite classical multitape Turing program; all bit operations, reading, auxiliary computation and output count toward its running time. It has no random bits, nonuniform advice or external oracle. The same \(A,K,d\) must work on every input size, colour pattern and allowed \(k\), with no error. Malformed encodings, odd vertex counts and out-of-range values of \(k\) can be rejected as invalid inputs in polynomial time. The graph may be disconnected, nonplanar and nonbipartite, with arbitrary degrees.

The required output is a decision bit; computing the number of matchings is not requested. Polynomial time means membership of this explicitly encoded decision language in the class \(\mathrm P\). Only sequential polynomial time is sought; a polylogarithmic-depth parallel algorithm is not required. The statement is unconditional: no computational hardness or derandomization assumption is supplied.''',
 answer_criterion=r'''Give a complete Lean-checked proof that the stated deterministic algorithm and common polynomial bound exist, or a complete Lean-checked proof that this decision language does not belong to \(\mathrm P\).

A positive answer must cover both YES and NO instances on all finite simple graphs. A randomized polynomial-time procedure, nonuniform circuit family, special graph class, exact-parity test or algorithm with a small red-count or matching-size error does not by itself suffice. A conditional lower bound or a barrier to one algebraic approach is not an unconditional negative answer. No numerical approximation tolerance applies.''',
 source_formulation=dict(text='Exact Matching asks whether a red/blue graph has a perfect matching with a prescribed number of red edges. Randomized polynomial-time algorithms are known, while the general deterministic polynomial-time question remains open in the 2023 survey and August 2026 algorithm paper.',caption='Paraphrase of El Maalouly’s STACS 2023 problem box and Sato–Yamaguchi, August 2026 revision, Introduction p. 1.',citation='primary',format='editorial_paraphrase'),
 why='Determine whether randomness can be removed from a basic exact constraint on perfect matching. The problem connects combinatorial derandomization with algebraic algorithms while keeping a short, directly checkable input and feasibility condition.',
 references=[
 ref('primary','Exact Matching: Algorithms and Related Problems','Nicolas El Maalouly',2023,'https://doi.org/10.4230/LIPIcs.STACS.2023.29','Introduction and Section 1.1, pp. 29:1–3; exact problem box and deterministic general-graph question'),
 ref('classical','Matching is as easy as matrix inversion','Ketan Mulmuley; Umesh V. Vazirani; Vijay V. Vazirani',1987,'https://doi.org/10.1145/28395.383347','STOC 1987; randomized history as discussed in the 2023 and 2026 primary sources'),
 ref('fast','Exact Matching in Matrix Multiplication Time','Ryotaro Sato; Yutaro Yamaguchi',2026,'https://arxiv.org/abs/2508.04081v2','10 August 2026 revision; Introduction and Theorem 1.3 p. 1, Remark 1.7 p. 2, Section 3'),
 ref('bipartite','Bipartite Exact Matching in P','Yuefeng Du',2026,'https://arxiv.org/abs/2604.01571v3','9 April 2026 revision; bipartite scope of Theorem 1.1 and Appendix A, eight explicit structural hypotheses in the formalization'),
 ],
 context_blocks=[
 block('An ordinary perfect matching covers every vertex once. The exact colour constraint asks for one specified attainable count, which is not determined merely by optimizing the count upward or downward.'),
 block('On a six-cycle whose edge colours alternate red and blue, the two perfect matchings have zero and three red edges. Counts one and two are absent even though they lie between the minimum and maximum. This elementary obstruction already occurs on bipartite inputs.'),
 block('Randomized methods place the problem among natural candidates for studying the power of randomness in efficient computation. A matching witnesses a YES answer, but the target requires a deterministic polynomial-time decision on NO instances as well.'),
 block('The August 2026 revision tests all red counts simultaneously in matrix-multiplication time measured in finite-field operations. Its decision algorithm still uses randomness, and the introduction explicitly leaves derandomization open.','fast'),
 block('The April 2026 preprint claims a deterministic algorithm only for bipartite graphs. Its Appendix A records eight unproved structural inputs in the Lean formalization. This review does not certify those inputs or the full proof; even a verified bipartite theorem would require a further general-graph argument to settle this card.','bipartite'),
 ],
 progress=[progress('1987','Randomized algebraic methods yield efficient Exact Matching algorithms, as recorded by the later primary sources.','classical'),progress('2023','The STACS survey retains deterministic polynomial time for general graphs as open.','primary'),progress('2026-04-09','The bipartite preprint’s third version records eight structural hypotheses in its formalization.','bipartite'),progress('2026-08-10','The revised simultaneous all-count algorithm achieves O(n^omega) field operations and remains randomized.','fast')],
),notes,sources,'The primary randomized-algorithm revision of 10 August 2026 explicitly retains the general deterministic polynomial-time question. The April preprint is restricted to bipartite graphs and its formalization has explicit structural hypotheses. Bounded primary-source checks through 17 September 2026 found no verified resolution for unrestricted graphs; no independent full proof or Lean audit of the bipartite claim was performed.',summary=[
 'Exact Matching asks whether a red/blue graph has a perfect matching with exactly the requested number of red edges.',
 'The target is one deterministic polynomial-time decision algorithm for all simple undirected graphs.',
 'Knowing only the minimum and maximum red counts does not determine which intermediate counts are attainable.',
 'The recent faster general algorithm remains randomized, while a separate claimed deterministic result is restricted to bipartite graphs.',
 'A complete Lean-checked solution must establish membership in P or prove its unconditional negation.',
],expected_sha256=claim['input_sha256'],claim_token=claim['token'])
