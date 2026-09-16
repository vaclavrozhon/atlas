"""Individual review of the user-selected four-parameter graph-query target."""
import sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT/'research/card-completion-20260913'))
from complete_review import complete,ref,block,progress
from review_queue import read_claims
identifier='TCS-0834'
claim=read_claims(ROOT)[identifier]
refs=[
 ref('primary',"Problem 98: Estimating a Graph's Degree Distribution",'C. Seshadhri',2019,
 'https://sublinear.info/index.php?title=Open_Problems:98',
 'WOLA 2019 problem; revision 1298, last edited 26 August 2019; first question on matching query bounds'),
 ref('saddles','Provable and Practical Approximations for the Degree Distribution using Sublinear Graph Samples',
 'Talya Eden; Shweta Jain; Ali Pinar; Dana Ron; C. Seshadhri',2018,
 'https://arxiv.org/abs/1710.08607v3',
 'Version 3, 28 August 2018; §1.1 and Definition 1.1, Definitions 1.4–1.5, Theorems 1.6 and 3.1, Algorithm SADDLES'),
 ref('stronger','Towards Tight Bounds for Estimating Degree Distribution in Streaming and Query Models',
 'Arijit Bishnu; Debarshi Chanda; Gopinath Mishra',2025,
 'https://arxiv.org/abs/2507.21784v1',
 'Version 1, 29 July 2025; §2.2.2 query model, Table 1, §§4.3 and 5: direct random-edge access'),
]
notes=[
 'Applied both user decisions: characterize constant-factor query complexity using n, m, h and minimum positive d*N(d), while supplying only n to the algorithm.',
 'Corrected the reversed threshold shifts in the problem-page display against Definition 1.1 of the original paper.',
 'Defined the h-index by an integer maximum, not by the possibly nonexistent equality N(h)=h; excluded zero-tail thresholds from the minimum.',
 'Specified labeled simple undirected graphs, the three original oracle types, independent random replies, expected adaptive query cost and simultaneous success.',
 'Defined a pointwise minimax envelope over algorithms that are correct on all graphs, with exact feasible parameter classes; no promise that the graph belongs to a supplied class is given.',
 'Distinguished infimum bounds from existence of one algorithm simultaneously attaining every point of the envelope.',
 'Separated the sample-budget hypotheses of the 2018 theorem and the stronger random-edge model of the 2025 preprint from the selected unknown-parameter target.',
 'Preserved the existing importance score and category; added full Lean acceptance and problem-specific context.',
]
sources=[
 'Read Sublinear.info Problem 98, revision 1298: three access primitives, the original bound and matching-bound question, and separate tail-only/testing/random-walk variants.',
 'Read Eden et al. arXiv:1710.08607v3 §1.1, Definitions 1.1, 1.4 and 1.5, and Theorem 3.1 with Algorithm SADDLES. The theorem is stated with sample budgets satisfying parameter-dependent lower bounds, and measures expected queries.',
 'Read Bishnu–Chanda–Mishra arXiv:2507.21784v1 §2.2.2, Table 1 and query implementations in §§4.3 and 5. Direct uniform random-edge queries are available; indexed-neighbor and edge-existence queries are also part of the broader model.',
 'Checked primary-source searches through 16 September 2026. Recent average-degree/moment results address different statistics. The FOCS 2026 local-node-privacy degree-distribution result concerns a privacy model, not this three-oracle query-complexity target.',
]
status=('The 2019 source asks for improved upper and matching lower bounds. Its displayed bicriteria shifts are reversed; this review uses the original 2018 Definition 1.1. '
 'The user selected all four performance parameters, fixed ten-percent error and constant-factor precision, then specified on 16 September 2026 that only n is supplied. '
 'The 2018 SADDLES theorem requires suitable parameter-dependent sample budgets. The 2025 preprint uses stronger direct random-edge access. '
 'Neither source establishes the full constant-factor, four-parameter minimax envelope for the selected information model. No matching resolution was found in the bounded current review.')
complete(identifier,dict(
 title='Query complexity of the graph degree distribution',
 criterion='resources',question_type='asymptotic_complexity',
 formal=r'''Determine, up to universal constant factors, the function
\[
Q^\star(n,m,h,w)=
\inf_{A\in\mathcal A}\ 
\max_{G\in\mathcal G(n,m,h,w)}
\mathbb E[T_A(G)]
\]
on every feasible tuple defined below. Here \(\mathcal A\) consists of uniform randomized algorithms which receive only \(n\), access the graph through the three specified query types, and correctly estimate its entire complementary cumulative degree histogram with probability at least \(2/3\). The required simultaneous accuracy is
\[
\Pr\!\left[
\forall d\in\{1,\ldots,n-1\},\
\frac9{10}N_G\!\left(\frac{11}{10}d\right)
\le \widehat N(d)\le
\frac{11}{10}N_G\!\left(\frac9{10}d\right)
\right]\ge\frac23.
\]
The parameters \(m,h,w\) describe the graph on which cost is evaluated; their values, estimates and bounds are not supplied to the algorithm.''',
 definitions=r'''The input graph \(G=([n],E)\), with \(n\ge2\) and \([n]=\{1,\ldots,n\}\), is finite, simple and undirected, with no loops or repeated edges. All labels in \([n]\) are valid query arguments; the edge set is hidden. Put
\[
m=|E|,\qquad
N_G(t)=|\{v\in[n]:\deg_G(v)\ge t\}|\quad(t\in\mathbb R).
\]
Thus a noninteger threshold means its ceiling, \(N_G(t)=n\) for \(t\le0\), and \(N_G(t)=0\) for \(t>n-1\). The output is a list of nonnegative rational estimates \(\widehat N(d)\) for integer \(1\le d\le n-1\); the value at zero is known to be \(n\). The event in the question must hold for all output thresholds together.

The h-index and the second tail parameter are
\[
h(G)=\max\bigl(\{0\}\cup\{d\in\{1,\ldots,n-1\}:N_G(d)\ge d\}\bigr),
\]
\[
w(G)=
\begin{cases}
\min\{dN_G(d):1\le d\le n-1,\ N_G(d)>0\},&m>0,\\
0,&m=0.
\end{cases}
\]
The \(z\)-index in the 2018 paper satisfies \(z=\sqrt{w}\). These are integer parameters, with the displayed empty-graph convention. A tuple \((n,m,h,w)\) is feasible precisely when some graph on \([n]\) has those values. Let \(\mathcal G(n,m,h,w)\) be the finite nonempty set of all such labeled graphs. The domain includes edgeless graphs.

Each of the following oracle calls costs one query:

- Vertex: return a uniformly random label in \([n]\).
- Degree(\(v\)): return the exact integer \(\deg_G(v)\).
- RandomNeighbor(\(v\)): return a uniformly random neighbor of \(v\), or a distinguished symbol \(\bot\) if its degree is zero.

Random replies are fresh independent samples conditional on the selected query and the fixed graph. An algorithm may adapt its calls and stopping rule to previous replies and its independent fair random bits. There is no indexed-neighbor, edge-existence or direct uniform-edge oracle. The initial input is the binary encoding of \(n\), without advice. Computation, memory, random-bit generation and output length are unrestricted and do not contribute to the query count.

An element of \(\mathcal A\) is one probabilistic Turing machine, uniform over all \(n\ge2\), which halts almost surely with finite expected query count on every input graph and meets the stated success guarantee on every such graph. Let \(T_A(G)\) count all its calls, including those on unsuccessful runs. Expectation includes both its internal randomness and the oracle randomness. The maximum in the question ranges over the exact parameter class, but membership in that class is not an input promise available to \(A\).

The infimum is taken pointwise over this same class \(\mathcal A\). A witness for an upper bound must still be a machine correct on every graph with only \(n\) supplied. The definition does not demand that one machine attain the infimum, or achieve optimal cost simultaneously for every tuple. In particular, a procedure justified only under a promised value of \(m,h,w\) is not automatically an admissible witness. Querying all \(n\) degrees provides an admissible finite baseline.''',
 answer_criterion=r'''Supply an unambiguous, noncircular description of a nonnegative function \(F\) on the feasible tuples and absolute constants \(c,C>0\), together with a complete Lean-checked proof that
\[
cF(n,m,h,w)\le Q^\star(n,m,h,w)\le CF(n,m,h,w)
\]
for every feasible tuple. Upper bounds must use admissible algorithms or an approaching family establishing the infimum bound; lower bounds must apply to all admissible algorithms. Merely repeating the optimization defining \(Q^\star\) is not a determination. Hidden logarithmic factors are not permitted in this constant-factor answer, and no additive \(1/100\) tolerance applies to the asymptotic target. Bounds for average degree alone, only the high-degree tail, a stronger query oracle, or algorithms given the hidden parameters do not settle the requested function.''',
 source_formulation=dict(text='The first question asks whether the SADDLES degree-distribution query bound can be improved and whether matching lower bounds can be proved. The user selected the full four-parameter complexity function, fixed ten-percent bicriteria error and constant-factor precision, with only n known in advance.',
 caption='Paraphrase of the first question in Problem 98; user-selected precision and information convention. Threshold shifts follow the original paper, correcting the problem-page typo.',
 citation='primary',format='editorial_paraphrase'),
 why='The degree histogram distinguishes common low-degree vertices from rare hubs. Estimating its whole cumulative profile requires guarantees in the tail as well as where most vertices lie. A sharp query bound would identify which structural features permit reliable graph summaries with limited access.',
 references=refs,
 context_blocks=[
 block('A cumulative degree histogram counts vertices above each degree threshold. Approximating only its normalization in an additive distributional distance can overlook a small but structurally important population of high-degree vertices. The bicriteria requirement controls this tail while allowing a small shift of the threshold.','saddles'),
 block('Uniform vertices and random neighbors have different sampling biases. The model makes these access costs explicit and includes degree queries. The question therefore concerns information available through local graph access, rather than the cost of reading an adjacency matrix.'),
 block(r'The 2018 paper introduces the \(z\)-index alongside the usual h-index. In its Standard Model, Theorem 3.1 gives expected cost \(O((n/h+m/w)\varepsilon^{-2}\log(n/\delta))\), for positive parameters and sample budgets meeting the theorem’s hypotheses, with simultaneous success probability at least \(1-\delta\). This is a sourced algorithmic bound, not a matching characterization.','saddles'),
 block('The sample-budget conditions in that theorem depend on graph parameters. Because this card supplies only the vertex count, an upper-bound proof must account for obtaining suitable information or otherwise justify its stopping rule. The source theorem is not silently promoted to an unknown-parameter guarantee.','saddles'),
 block(r'The 2025 preprint gives nearly matching bounds on an \(m/h\) scale in a stronger query model, using direct random-edge samples. Its general interface also includes indexed neighbors and edge-existence tests. Those guarantees do not determine the cost when an edge sample must be obtained using only the three calls in this card.','stronger'),
 block('The original entry also raises tail-only estimation, testing degree-distribution properties and replacing uniform vertex samples by other access. Those are separate variants. This card retains the full cumulative profile and the original three types of access.'),
 ],
 progress=[
 progress('2018-08-28','Version 3 states the simultaneous bicriteria guarantee and the h-index/z-index expected-query analysis of SADDLES.','saddles'),
 progress('2019-08-26','Problem 98 asks for improved upper bounds and matching lower bounds for the whole cumulative degree distribution.'),
 progress('2025-07-29','A preprint studies tighter bounds using direct random-edge access and streaming models; the stronger query interface matters.','stronger'),
 progress('2026-09-16','Individual review applies the user’s four-parameter, constant-factor target with only n supplied and corrects the source display against its cited paper.'),
 ],
),notes,sources,status,summary=[
 'A graph’s cumulative degree histogram counts vertices above each degree threshold.',
 'The task is to estimate the entire histogram with ten-percent bicriteria error and simultaneous success probability at least two thirds.',
 'The algorithm knows only the number of vertices and may sample vertices, query degrees or sample neighbors.',
 'The target is the optimal expected query complexity as a function of the vertex count, edge count, h-index and minimum positive degree-times-tail count.',
 'Known bounds and recent stronger-oracle results do not provide the full constant-factor characterization in this information model.',
],expected_sha256=claim['input_sha256'],claim_token=claim['token'])
