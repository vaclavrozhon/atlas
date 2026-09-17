"""Complete exact deterministic almost-linear global vertex connectivity."""
import sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];sys.path.insert(0,str(ROOT/'research/card-completion-20260913'))
from complete_review import complete,ref,block,progress,DATE
from review_queue import read_claims
identifier='TCS-7343';claim=read_claims(ROOT)[identifier]
notes=[
 'Preserved exact deterministic almost-linear time for all simple unweighted undirected graphs and all connectivity values.',
 'Specified explicit input size including isolated vertices, the separator witness and disconnected and complete-graph conventions.',
 'Made one-program, word-size and subpolynomial-overhead quantifiers explicit and retained charged initialization and output.',
 'Corrected the randomized reduction description to near-linear total flow-instance size rather than an unsupported count of flow calls.',
 'Distinguished weighted, directed, approximate and small-connectivity results; removed an unrelated background textbook reference.',
 'Preserved importance 91 and category and required a complete Lean-checked proof of either direction.',
]
sources=[
 'Read Jiang–Nalam–Saranurak–Yingchareonthawornchai, arXiv:2503.20985v1, 26 March 2025, Introduction and Theorem 1.2 pp. 1–3. It gives deterministic m*kappa*n^o(1) time for unweighted undirected graphs, while the weighted or directed theorem is different. The live history still lists only v1 on the review date; the primary author page confirms STOC 2025 publication.',
 'Read Li–Nanongkai–Panigrahi–Saranurak–Yingchareonthawornchai, arXiv:2104.00104v2, 9 April 2021, Introduction and Theorem 1.1 p. 2. The Monte Carlo reduction produces unit-capacity max-flow instances with near-linear cumulative vertices and edges and near-linear outside work. It explicitly remains randomized even with deterministic flow subroutines. The definition includes the singleton convention for complete graphs.',
 'Read Chen–Kyng–Liu–Peng–Probst Gutenberg–Sachdeva, arXiv:2203.00671v2, 22 April 2022, abstract, Theorem 1.1 and Corollary 1.2. Exact integral maximum flow with polynomially bounded capacities has almost-linear time with high probability. Combined with the 2021 reduction this supplies the randomized, not deterministic, comparison bound.',
 'Read the primary abstract and version history of Quanrud, arXiv:2512.00176v1, 28 November 2025, Approximating Directed Connectivity in Almost-Linear Time. It concerns randomized (1+epsilon) approximation and special small-connectivity exact consequences, not the deterministic exact endpoint for all connectivity values.',
 f'Bounded primary-source searches through {DATE}, including primary author publications and later connectivity papers, found no verified resolution. New results on connectivity augmentation, failure oracles and special graph classes were not treated as algorithms for this target. No independent full proof audit of the cited algorithms is claimed.',
]
complete(identifier,dict(
 title='Deterministic almost-linear vertex connectivity',criterion='resources',question_type='yes_no',
 formal=r'''Do there exist one uniform deterministic word-RAM algorithm \(A\), a real constant \(K>0\), an integer word-size constant \(d\ge4\), and a function \(h:\{2,3,\ldots\}\to[1,\infty)\) satisfying
\[
 \lim_{N\to\infty}\frac{\log h(N)}{\log N}=0
\]
such that, for every explicitly given simple unweighted undirected graph \(G=(V,E)\) with \(V=[n]\), \(n\ge2\), \(m=|E|\) and \(N=n+m\), the algorithm uses at most \(KNh(N)\) instructions and outputs both
\[
 \kappa(G)=\min\bigl\{|S|:S\subseteq V,
 G[V\setminus S]\text{ is disconnected or }|V\setminus S|\le1\bigr\}
\]
and a set \(S\) attaining this minimum?

The machine has word length \(w=d\lceil\log_2(n+2)\rceil\) and the operations and charged costs below. No randomness is allowed.''',
 definitions=r'''An edge is an unordered pair of distinct labelled vertices. Loops, parallel edges, edge weights and vertex weights are absent. The input explicitly lists all \(n\) vertices, including isolated ones, and the \(m\) edges as pairs of endpoint labels, with length headers. It occupies \(\Theta(n+m)\) words; a small binary header cannot stand for an unlisted exponentially large set of vertices. Edge order is arbitrary.

The induced graph \(G[V\setminus S]\) deletes every vertex of \(S\) and all its incident edges. A graph with at least two vertices is disconnected when some two of them have no path between them. The separate at-most-one-vertex clause defines the degenerate endpoint. In particular, \(\kappa(G)=0\) for an initially disconnected graph and \(\kappa(K_n)=n-1\) for a complete graph. There is always an attaining set. The requested output lists its vertices explicitly without repetitions, together with its integer size. Any minimum set is allowed; no canonical choice is prescribed.

This is global vertex connectivity: no distinguished source or sink is part of the input. The measure counts deleted vertices, not deleted edges. Every graph is allowed, including disconnected, dense and complete graphs, with connectivity possibly growing linearly in \(n\). A fixed-parameter running time whose hidden coefficient depends on \(\kappa(G)\) does not automatically give the stated uniform bound.

The uniform sequential word RAM is a fixed finite program with unsigned \(w\)-bit words, word-sized addresses and no advice, external oracle or free lookup table. Unit-cost operations are reads, writes, copies, comparisons, branching, Boolean operations, logical shifts, addition, subtraction and multiplication modulo \(2^w\), and integer quotient and remainder with nonzero divisor. Shifts by at least \(w\) return zero. Computation involving multiple words pays for each constituent instruction. All initialization, input access, preprocessing, constructed tables, auxiliary computation and output writes are charged. Both correctness and the instruction bound hold on every input, without random choices or error.

The function \(h\) depends only on \(N\), not on the graph or its connectivity, and is only a bound rather than an oracle supplied to the program. The same algorithm has running time \(N^{1+o(1)}\): for every real \(\eta>0\), it runs in \(O(N^{1+\eta})\) for all sufficiently large \(N\), with the constant and threshold allowed to depend on \(\eta\). A different program for each fixed \(\eta\) is not the one-program assertion here. No separate space bound is imposed beyond the stated machine and charged time.''',
 answer_criterion=r'''Give a complete Lean-checked proof of the existence of the stated algorithm, constants and bound, or a complete Lean-checked proof of their logical nonexistence in this model.

A positive answer must compute the exact value and an attaining vertex set on every allowed graph within the common worst-case time bound. A randomized algorithm, an approximation, a result for bounded connectivity or a conditional lower bound does not decide the full proposition. No numerical approximation tolerance applies to this algorithm-existence target.''',
 source_formulation=dict(text='The 2025 deterministic vertex-connectivity paper narrows the gap with randomized almost-linear algorithms, giving time m times the vertex connectivity up to subpolynomial factors on unweighted undirected graphs. The card asks for the almost-linear deterministic endpoint uniformly over all connectivity values.',caption='Editorial endpoint based on Jiang–Nalam–Saranurak–Yingchareonthawornchai, Introduction and Theorem 1.2, together with the explicit derandomization question following Theorem 1.1 of the 2021 reduction.',citation='primary',format='editorial_paraphrase'),
 why='Determine whether randomness is needed for almost-linear exact computation of a basic measure of network resilience. Finding the weakest vertex separation uniformly over sparse and dense graphs remains different from handling only small cuts.',
 references=[
 ref('primary','Deterministic Vertex Connectivity via Common-Neighborhood Clustering and Pseudorandomness','Yonggang Jiang; Chaitanya Nalam; Thatchaphol Saranurak; Sorrachai Yingchareonthawornchai',2025,'https://arxiv.org/abs/2503.20985v1','26 March 2025 version; Introduction and Theorem 1.2 pp. 1–3; STOC 2025'),
 ref('random','Vertex Connectivity in Poly-logarithmic Max-flows','Jason Li; Danupon Nanongkai; Debmalya Panigrahi; Thatchaphol Saranurak; Sorrachai Yingchareonthawornchai',2021,'https://arxiv.org/abs/2104.00104v2','9 April 2021 version; Theorem 1.1 and following derandomization question, p. 2'),
 ref('flow','Maximum Flow and Minimum-Cost Flow in Almost-Linear Time','Li Chen; Rasmus Kyng; Yang P. Liu; Richard Peng; Maximilian Probst Gutenberg; Sushant Sachdeva',2022,'https://arxiv.org/abs/2203.00671v2','22 April 2022 version; Theorem 1.1 and Corollary 1.2, polynomially bounded integral capacities'),
 ref('approx','Approximating Directed Connectivity in Almost-Linear Time','Kent Quanrud',2025,'https://arxiv.org/abs/2512.00176v1','28 November 2025; primary abstract, randomized approximation scope'),
 ],
 context_blocks=[
 block('Vertex connectivity measures the smallest number of vertex failures that disconnect a network, with the standard complete-graph convention. The algorithm must find the weakest separation without being told which two vertices it separates.'),
 block('The 2021 randomized reduction uses unit-capacity flow instances of near-linear total size. Its own randomness remains even if the supplied maximum-flow algorithm is deterministic.','random'),
 block('Almost-linear exact integral-flow algorithms transfer through that reduction to randomized almost-linear vertex connectivity. This establishes the comparison target while leaving the required derandomization open.','flow'),
 block(r'The 2025 deterministic bound is \(m\kappa(G)n^{o(1)}\) on nontrivial instances. The multiplicative connectivity factor can be polynomially large; the card asks to eliminate that loss uniformly.'),
 block('The later directed result gives randomized approximation schemes and exact consequences in small-connectivity regimes. Those results have different error, randomness and parameter guarantees.','approx'),
 ],
 progress=[progress('2021-04-09','A Monte Carlo reduction gives near-linear total size of max-flow instances and explicitly asks for derandomization.','random'),progress('2022','Exact almost-linear integral flow provides the randomized almost-linear comparison through that reduction.','flow'),progress('2025-03-26','The deterministic unweighted undirected algorithm has time m times the connectivity, up to subpolynomial factors.'),progress('2025-11-28','Randomized directed approximation schemes address a related but different endpoint.','approx')],
),notes,sources,'The 2025 deterministic bound retains a multiplicative connectivity factor, and the randomized flow reduction remains randomized even with deterministic flow subroutines. Bounded primary-source checks through 17 September 2026 found no verified resolution of the unrestricted exact deterministic almost-linear target. The cited full proofs were not independently audited.',summary=[
 'Vertex connectivity is the smallest number of vertices whose deletion disconnects a graph or leaves at most one vertex.',
 'The input is an explicit unweighted undirected graph, including all isolated vertices.',
 'The task is to output the exact value and an attaining set in deterministic almost-linear worst-case time.',
 'Randomized almost-linear time is known, while the reviewed deterministic bound retains a connectivity factor.',
 'A complete Lean-checked answer must cover every connectivity value with the same algorithm and time bound.',
],expected_sha256=claim['input_sha256'],claim_token=claim['token'])
