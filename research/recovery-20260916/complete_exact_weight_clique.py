"""Review the all-fixed-k randomized exact-edge-weight clique hypothesis."""
import sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT/'research/card-completion-20260913'))
from complete_review import complete,ref,block,progress
from review_queue import read_claims
identifier='TCS-6945'
claim=read_claims(ROOT)[identifier]
notes=[
 'Recovered Hypothesis 8 with signed integer edge weights bounded by n^(100k), exact zero target and fixed clique size k>=3.',
 'Expanded n^(k-o(1)) into exclusion of every fixed positive polynomial exponent saving, for every fixed k.',
 'Specified decision output, two-sided error at most one third on each graph, worst-case time over random outcomes and a uniform logarithmic-word RAM.',
 'Matched the already reviewed Min-Weight k-Clique card’s explicit word operations and input representation, while retaining the different exact-sum decision target.',
 'Separated arbitrary simple graphs from k-partite reductions, ordinary clique detection, vertex-weighted problems and restricted numerical ranges.',
 'Individually assessed importance and checked later exact-clique-based listing results as conditional consequences rather than proofs of the hypothesis.',
]
sources=[
 'Read Vassilevska Williams, author-hosted ICM 2018 survey On Some Fine-Grained Questions in Algorithms and Complexity: computational model pp. 3–4; §5 p. 16 definitions and Hypotheses 6–8; p. 17 consequences. The edge-weight interval is explicitly [-n^(100k),n^(100k)] and Hypothesis 8 explicitly includes randomization.',
 'Read Dalirrooyfard–Mathialagan–Vassilevska Williams–Xu, arXiv:2307.15871v2, revised 21 March 2024: abstract, §1.1 Hypothesis 1.3 printed p. 4/PDF p. 6 and Theorem 1.4, plus the §4 reduction setup. This version repeats the exact numerical range and word-RAM model; later bibliographic versions can renumber the hypothesis.',
 'Read Kirkpatrick–Mathialagan, arXiv:2407.08562v1, submitted 11 July 2024: introduction Hypothesis 1.5, §2.3 Definition 2.7 and Hypothesis 2.8, and §4 statement of the clique-listing consequence. It uses the same zero-sum edge-weight predicate. Full reduction proofs were not independently audited.',
 'Read the active reviewed TCS-6944 model to maintain compatible RAM and encoding conventions; its minimum-weight witness objective is distinct and remains unchanged.',
 'Bounded later primary-source searches through 16 September 2026 found uses of the exact-weight hypothesis and faster unweighted or restricted problems, without a fixed-power randomized speedup or unconditional proof for the full stated model. This is a bounded status check, not an exhaustive certification.',
]
status=('The survey and the checked 2024 primary sources explicitly retain the exact-weight hypothesis with the same signed edge-weight range. '
 'Their clique-listing results are conditional consequences, not proofs of the hypothesis. No resolution for the full randomized word-RAM model was found in the bounded later-source search.')
complete(identifier,dict(
 title='Exact-Weight k-Clique hypothesis',
 criterion='resources',question_type='yes_no',
 formal=r'''Is the following hypothesis true?

For every fixed integer \(k\ge3\) and every fixed real \(\varepsilon\in(0,1]\), there is no bounded-error randomized word-RAM algorithm that decides Exact-Weight \(k\)-Clique on all \(n\)-vertex inputs in worst-case time \(O(n^{k-\varepsilon})\).

An input is a simple undirected graph \(G=([n],E)\), with \(n\ge k\) and integer edge weights
\[
w:E\longrightarrow\{-n^{100k},\ldots,n^{100k}\}.
\]
The required output is YES exactly when there is a set \(S\subseteq[n]\) of \(k\) distinct vertices such that
\[
\binom S2\subseteq E,\qquad
\sum_{e\in\binom S2}w(e)=0.
\]
The algorithm must return the correct decision with probability at least \(2/3\) separately on every input. Its time bound applies to every random outcome. The explicit machine and input conventions are given below.''',
 definitions=r'''A simple undirected graph has no self-loops or parallel edges. Every unordered pair of distinct labelled vertices is either an edge or absent. A \(k\)-clique is a set of exactly \(k\) distinct vertices with all its \(\binom k2\) edges present. Its weight is the ordinary integer sum of those edge weights, counting each edge once. Positive, negative and zero weights are permitted. An absent edge cannot be used, regardless of how its unused weight field is encoded. The target sum is exactly zero. There is no approximation, modular interpretation or promise about a gap from zero.

The input is a read-only array containing \(n\), followed in lexicographic order for every unordered vertex pair by its adjacency flag, sign bit and unsigned weight magnitude, each in its own word. A sign bit zero denotes a nonnegative value and one a negative value; a zero magnitude denotes zero. An absent edge has zero sign and magnitude. Inputs obey the displayed weight bound. The output is a single decision bit; a witness clique or its list of vertices is not required. No sparsity, partiteness or input-distribution promise is imposed.

For each fixed \(k\), an algorithm is one finite word-RAM program independent of \(n\). For some fixed integer \(d\ge100k+4\), the word length is
\[
W(n)=\lceil d\log_2(n+2)\rceil.
\]
The factor \(d\) may depend on the program and \(k\), but not on \(n\) or the input. Addresses and memory cells each occupy one word. This suffices for an input weight; larger quantities can use several words, with every operation charged.

One operation accesses a constant number of addressed words or registers, copies, compares or branches, applies a word-level Boolean operation or shift, adds, subtracts or multiplies modulo \(2^W\), computes unsigned quotient or remainder by a nonzero word, or obtains one fresh independent uniformly distributed \(W\)-bit word. Shifts by at least \(W\) positions produce zero; division by zero is invalid. All accessed addresses fit in a word. Work memory is initially zero. Input access, preprocessing, table construction, memory access and output writing all count toward runtime. No tables depending on \(n\), advice, oracle, real-number instruction or quantum operation are supplied in advance. Arithmetic used to test the clique's sum must correctly implement integer equality, accounting for signs and any necessary multiple-word representation.

A randomized algorithm halts on every valid graph and every random sequence. It may err on either YES or NO instances, but on each individual graph the probability of the correct output is at least \(2/3\). The input is fixed before the independent random words are drawn. A deterministic algorithm is included by ignoring randomness.

Precisely, the excluded faster algorithm would consist of a program \(A\), a word factor \(d\), and constants \(C\ge1,n_0\ge k\) such that, for every \(n\ge n_0\), every valid graph and every random sequence, the runtime is at most \(Cn^{k-\varepsilon}\), while \(A\) is correct with probability at least \(2/3\) on every valid graph at every length. These choices may depend on \(k,\varepsilon\), but not on \(n\) or on the graph. Separate programs are allowed for separate fixed clique sizes. The hypothesis quantifies over all such programs.

The phrase \(n^{k-o(1)}\) means the exclusion of every fixed positive exponent saving just stated. It does not rule out logarithmic or other subpolynomial improvements over \(n^k\), and it does not posit one pointwise lower-bound formula for every algorithm at every input length. Restricting \(\varepsilon\) to \((0,1]\) loses no possible fixed-power refutation, since any larger saving implies a smaller positive saving.

The parameter \(k\) is fixed for each problem, not part of the growing input. The exponent \(100k\) is fixed with it. Replacing that exponent by an unquantified polynomial weight range, or replacing signed edge weights by nonnegative or vertex weights, would change the precise hypothesis.''',
 answer_criterion=r'''Give a complete Lean-checked proof or refutation of the displayed universal randomized time-barrier hypothesis in the specified word-RAM model. To refute it, one fixed \(k\ge3\), one fixed \(\varepsilon>0\), and a correct algorithm with the required worst-case runtime on all valid graphs suffice. To prove it, exclude every such algorithm for every fixed \(k\). A conditional hardness reduction, a restricted-model lower bound, a speedup only for a weight or graph promise, or a subpolynomial improvement is insufficient. This is a binary exact-decision hypothesis with an asymptotic time threshold; numerical \(1/100\) tolerance does not relax the zero-sum predicate or exponent.''',
 source_formulation=dict(
 text='Hypothesis 8 states that exact zero-weight clique detection needs essentially the enumeration exponent, including randomized algorithms, when the signed integer edge weights have the specified polynomial magnitude.',
 caption='Paraphrase of the ICM 2018 author survey, §5, p. 16, Hypothesis 8 and its immediately preceding definitions.',
 citation='primary',format='editorial_paraphrase'),
 importance=dict(score=85,method='editorial',
 reason='The hypothesis provides a common exact-weight hardness foundation for clique listing, weighted graph problems and database queries, and its triangle case connects major fine-grained assumptions.',
 basis='Individual assessment of the breadth of conditional consequences and the gap between weighted equality constraints and fast unweighted clique detection; not a claim that the hypothesis is proved.'),
 why='Requiring the edge weights of a clique to cancel exactly couples all its edges in a way that ordinary clique detection does not capture. The hypothesis asks whether this numerical constraint prevents a fixed polynomial improvement over enumeration. Its consequences connect the cost of finding weighted structures with output-sensitive enumeration and other fine-grained lower bounds.',
 references=[
 ref('primary','On Some Fine-Grained Questions in Algorithms and Complexity','Virginia Vassilevska Williams',2018,
 'https://people.csail.mit.edu/virgi/eccentri.pdf',
 'Author-hosted ICM 2018 survey; computational model pp. 3–4, §5 p. 16 Hypothesis 8 and definitions, p. 17 consequences; proceedings chapter DOI 10.1142/9789813272880_0188'),
 ref('listing','Towards Optimal Output-Sensitive Clique Listing or: Listing Cliques from Smaller Cliques',
 'Mina Dalirrooyfard; Surya Mathialagan; Virginia Vassilevska Williams; Yinzhan Xu',2024,
 'https://arxiv.org/abs/2307.15871v2',
 'Version 2, 21 March 2024; §1.1 Hypothesis 1.3 and Theorem 1.4, printed p. 4/PDF p. 6; §4 reduction setup'),
 ref('arboricity',"A Note on the Conditional Optimality of Chiba and Nishizeki's Algorithms",
 'Yael Kirkpatrick; Surya Mathialagan',2024,'https://arxiv.org/abs/2407.08562v1',
 'Version 1, 11 July 2024; Hypothesis 1.5, §2.3 Definition 2.7 and Hypothesis 2.8, §4 conditional clique-listing result'),
 ],
 context_blocks=[
 block('The source separates ordinary clique detection, minimum-weight clique optimization and exact-weight clique decision. Fast matrix-multiplication algorithms for the first problem do not decide whether a weighted clique has sum zero.'),
 block('The signs of the edge weights permit cancellation. With only nonnegative weights, sum zero would require every selected edge to have weight zero, giving a different and easier restriction.'),
 block('The source records a fine-grained reduction from minimum-weight clique to the exact-weight problem. Thus the minimum-weight hypothesis implies the corresponding exact-weight hypothesis; a general equivalence is not asserted here.'),
 block(r'At \(k=3\), the problem is Exact Triangle. The source relates its cubic hardness to both the 3SUM and APSP hypotheses. The card also quantifies over every other fixed clique size.'),
 block('The 2024 listing paper uses the same exact-weight assumption to prove conditional lower bounds for output-sensitive clique listing. Those reductions motivate the hypothesis without establishing it.','listing'),
 block('The later note derives clique-listing consequences that also track arboricity. Algorithms on those restricted or output-sensitive instances do not by themselves give a faster algorithm for the full signed-weight decision problem.','arboricity'),
 ],
 progress=[
 progress('2018','The survey states the randomized exact-weight hypothesis with the explicit signed edge-weight range.'),
 progress('2024-03-21','The revised clique-listing paper repeats the same hypothesis and develops conditional output-sensitive lower bounds.','listing'),
 progress('2024-07-11','The arboricity note uses the hypothesis for conditional optimality of clique-listing algorithms.','arboricity'),
 progress('2026-09-16','The review fixes the decision, numerical range, randomization and machine quantifiers; no resolution of the complete hypothesis is found in the bounded search.'),
 ],
 related_problem_ids=['TCS-6944','TCS-6937'],
),notes,sources,status,summary=[
 'The input is a simple graph with signed integer weights on its edges.',
 'The decision is whether exactly k vertices form a clique whose edge weights sum to zero.',
 'For every fixed k, the hypothesis excludes a randomized algorithm with a fixed positive improvement over the enumeration exponent.',
 'Weights have magnitude at most n to the power 100k, and time is measured on a uniform logarithmic-word RAM.',
 'The hypothesis supports conditional clique-listing lower bounds and remains distinct from ordinary unweighted clique detection.',
],expected_sha256=claim['input_sha256'],claim_token=claim['token'])
