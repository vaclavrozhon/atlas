"""Apply the selected existential sub-two base, allowing bounded error."""
import json,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT/'research/card-completion-20260913'))
from complete_review import complete,ref,block,progress,DATE
from review_queue import read_claims
identifier='TCS-0801'
claim=read_claims(ROOT)[identifier]
notes=[
 'Applied the user’s explicit alternative: O(c^n) for some fixed c<2, rather than the source’s literal O(1.999^n).',
 'Specified all finite loopless directed graphs, opposite arcs allowed, exact existence rather than counting parity, and per-input success at least two thirds.',
 'Fixed a uniform classical randomized RAM with linear-bit words sufficient to address exponential memory, charged operations and worst-case time over every random tape.',
 'Made the base and all constants independent of graph size and structure; polynomial factors may be absorbed into a slightly larger fixed base still below two.',
 'Checked July 2026 exact counting and September 2026 parity results; neither supplies the selected fixed-exponent improvement for detection on general digraphs.',
 'Preserved assessed importance 69 and required a complete Lean-checked proof covering both resource and correctness guarantees.',
]
sources=[
 'Read Husfeldt’s complete §6.20, printed pp. 70–71, in Dagstuhl Seminar 13331, Exponential Algorithms: Algorithms and Complexity Beyond Polynomial Time (2013), DOI 10.4230/DagRep.3.8.40. The literal numerical target is 1.999^n; the user selected the weaker existential base c<2 on 17 September 2026.',
 'Read Björklund–Kaski–Koutis, arXiv:1607.04002v2, 25 April 2017, abstract and introduction pp. 1–4, Theorems 3–4. Prime-power modular counting and algorithms for bounded-degree, few-cycle or large-independent-set inputs have scope restrictions. Published at ICALP 2017, LIPIcs 80, 91:1–91:14, DOI 10.4230/LIPIcs.ICALP.2017.91.',
 'Read Arvind–Chakraborty–Datta–Khan, arXiv:2512.08600v1, 9 December 2025, abstract and introduction pp. 1–2. The directed fast Hamiltonian-path case is bipartite and does not cover general digraphs.',
 'Read Baitian Li, Counting Perfect Matchings and Hamiltonian Cycles Faster, ICALP 2026, LIPIcs 374, 138:1–138:16, published 1 July 2026, DOI 10.4230/LIPIcs.ICALP.2026.138: abstract, §1.1 Theorem 1 and Corollary 2, pp. 138:1–138:3. The exact integer count has a 2^{n-Omega(sqrt(n))} upper bound; this is not a fixed linear saving in the exponent.',
 'Read Hanqing Li, arXiv:2609.11982v1, 7 September 2026, abstract and introduction pp. 1–2, Theorem 1.1. The claimed deterministic O*((3/2)^n) algorithm computes parity only. A zero parity answer is compatible with a positive even number of Hamiltonian cycles. The complete new proof was not independently certified.',
 f'Bounded primary-source searches through {DATE} found these partial improvements but no resolution of general directed detection in O(c^n) for one fixed c<2.',
]
status='The selected general directed detection question remains unresolved in the checked sources. ICALP 2026 improves exact counting to 2^{n-Omega(sqrt(n))}, which does not give a fixed base below two. The September 2026 preprint improves parity counting, a different task. Restrictions such as bipartiteness, bounded degree or a bound on the number of cycles are absent here; the bounded literature review does not independently certify every cited proof.'
complete(identifier,dict(
 criterion='resources',question_type='yes_no',year=2026,
 formal=r'''Do there exist one uniform classical randomized algorithm \(A\), a fixed rational constant \(c\in(1,2)\), and constants \(K\ge1\) and integer \(B\ge2\) such that the following holds for every \(n\ge2\) and every directed graph \(G\) on \([n]\)?

In the RAM model below, using \(Bn\)-bit words, \(A\) halts within \(Kc^n\) operations on every random tape and correctly decides whether \(G\) has a directed Hamiltonian cycle with probability at least \(2/3\). The same algorithm and constants must handle all such graphs.''',
 definitions=r'''The input is \(n\) and the full \(n\times n\) Boolean adjacency matrix of a loopless directed graph, stored as one Boolean entry per input cell. An arc is an ordered pair of distinct vertices. There is at most one arc for each ordered pair, but both \((u,v)\) and \((v,u)\) may be present. No degree, density, bipartiteness, connectivity or cycle-count promise is made.

A directed Hamiltonian cycle is a permutation \((v_1,\ldots,v_n)\) of \([n]\) with arcs \((v_i,v_{i+1})\) for \(1\le i<n\) and \((v_n,v_1)\). In particular, on two vertices it requires both opposite arcs. The algorithm outputs one bit indicating existence. It need not count cycles, determine the parity of their number or output a witness. The empty and one-vertex loopless cases can be assigned the fixed answer no and do not affect the asymptotic target.

The algorithm is a finite program independent of \(n\), with no advice. Its word length is \(w=Bn\) bits for the fixed integer \(B\). Memory cells have \(w\)-bit addresses and initially contain zero. Each read, write, indirect memory access, comparison, branch, bitwise Boolean operation, shift, addition, subtraction, multiplication, or integer quotient or remainder with a nonzero divisor costs one operation. Addition, subtraction and multiplication are modulo \(2^w\), and shifts by at least \(w\) return zero. A fresh independent uniform \(w\)-bit random word costs one operation. Larger values require multiple words with all operations charged. The model has no arbitrary-precision unit-cost arithmetic, special graph instructions, precomputed graph advice or quantum operations.

The linear word length permits addressing exponential memory; there is no separate polynomial-space requirement. Unused cells need not be initialized, but every actual access, preprocessing step and output operation is charged. This fixes a finite-precision random-access convention for exponential-time algorithms rather than implicitly forbidding exponential tables by limiting addresses to logarithmically many bits.

For every fixed input graph, probability is over the algorithm’s own randomness, and its Boolean answer must be correct with probability at least \(2/3\). Both false positives and false negatives are allowed within that error bound. The runtime bound holds for every random tape, not only in expectation or for a random input graph. Deterministic algorithms are included as algorithms that ignore randomness.

The base \(c\), the word-length multiplier \(B\) and \(K\) do not depend on \(n\), the graph or any structural parameter. The selected target is some fixed \(c<2\), not specifically \(1.999\). A running time \(O(c_0^n n^d)\) with fixed \(c_0<2\) and fixed \(d\) suffices by absorbing the polynomial into a larger fixed base below two. A saving of only a sublinear term from the exponent \(n\) in a bound of the form \(2^{n-o(n)}\) does not by itself establish this target. These remarks concern asymptotic bounds within the specified model, not an unproved interchangeability of all computation models.''',
 answer_criterion=r'''Supply a uniform algorithm and a complete Lean-checked proof of the fixed-base runtime bound on every random tape and success probability at least \(2/3\) for every graph, or give a complete Lean-checked proof that no algorithm and constants in the stated model satisfy the proposition.

A parity or modular-counting algorithm alone is not an existence test. A speedup for only a restricted graph class, a base tending to two as a graph parameter grows, or a sublinear exponent saving is insufficient. A conditional lower bound must retain its assumption and does not by itself refute the unconditional existence proposition. Numerical \(1/100\) tolerance does not relax this binary algorithm-existence question.''',
 source_formulation=dict(text='Husfeldt’s entry asks literally for a directed Hamiltonian-cycle algorithm in time O(1.999^n). The user selected the broader fixed-base target O(c^n) for some c<2, allowing a randomized algorithm correct with probability at least two thirds on every graph.',caption='Paraphrase of Seminar 13331, §6.20, printed pp. 70–71; the existential-base alternative was explicitly selected on 17 September 2026.',citation='primary',format='editorial_paraphrase'),
 why='Direction prevents the symmetric treatment of cycle traversals available in undirected graphs. A fixed improvement in the exponential base for arbitrary digraphs would cross a long-standing boundary of exact graph algorithms, beyond modular counting and speedups restricted to particular structures.',
 references=[
 ref('primary','Exponential Algorithms: Algorithms and Complexity Beyond Polynomial Time — Directed Hamiltonicity','Thore Husfeldt',2013,'https://doi.org/10.4230/DagRep.3.8.40','Seminar 13331, §6.20, printed pp. 70–71; literal O(1.999^n) target'),
 ref('laplacian','Directed Hamiltonicity and Out-Branchings via Generalized Laplacians','Andreas Björklund; Petteri Kaski; Ioannis Koutis',2017,'https://arxiv.org/abs/1607.04002v2','Version 2, 25 April 2017; introduction pp. 1–4, Theorems 3–4; ICALP 2017, LIPIcs 80, Article 91, DOI 10.4230/LIPIcs.ICALP.2017.91'),
 ref('counting','Counting Perfect Matchings and Hamiltonian Cycles Faster','Baitian Li',2026,'https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.ICALP.2026.138','Published 1 July 2026; LIPIcs 374, 138:1–138:16; §1.1 Theorem 1 and Corollary 2, pp. 138:2–138:3'),
 ref('parity',r'A Deterministic \(O^*((3/2)^n)\) Algorithm for the Parity of Directed Hamiltonian Cycles','Hanqing Li',2026,'https://arxiv.org/abs/2609.11982v1','Version 1, 7 September 2026; abstract and introduction pp. 1–2, Theorem 1.1; parity, not detection'),
 ],
 context_blocks=[
 block('The question concerns a constant improvement in the coefficient of the vertex count in the exponent. An improvement that removes only a square-root-sized term can be substantial while still falling short of this fixed-base target.'),
 block('The generalized-Laplacian results speed up counting modulo prime powers and detection under further structural or cycle-count restrictions. Their constants do not supply one bound for every unrestricted digraph.','laplacian'),
 block(r'The July 2026 exact-counting result gives a bound of \(2^{n-\Omega(\sqrt n)}\) for directed Hamiltonian cycles. Exact counting determines existence, but this published bound has a sublinear rather than linear saving in the exponent.','counting'),
 block('The September 2026 preprint claims a smaller fixed base for parity. Parity zero includes graphs with a positive even number of cycles, so this faster answer is not itself a correct test for whether a cycle exists.','parity'),
 ],
 progress=[
 progress('2013','The original entry states the numerical O(1.999^n) challenge for directed Hamiltonicity.'),
 progress('2017-04-25','The revised generalized-Laplacian paper improves modular counting and restricted directed detection.','laplacian'),
 progress('2026-07-01','ICALP 2026 improves the exponent saving for unrestricted exact counting to a square-root term.','counting'),
 progress('2026-09-07','A preprint claims deterministic O*((3/2)^n) parity computation; it does not claim general existence detection.','parity'),
 ],
),notes,sources,status,summary=[
 'The question asks for a randomized test for a Hamiltonian cycle in every finite loopless directed graph.',
 'Its running time must be O(c^n) for one fixed c below two, as explicitly selected by the user.',
 'Success must be at least two thirds on each input, and the stated RAM time bound must hold on every random tape.',
 'The 2026 exact-counting improvement saves only a sublinear term in the exponent, while the September fixed-base improvement concerns parity alone.',
 'A complete Lean-checked solution must establish the full unrestricted detection guarantee or refute it; restricted graphs and modular counts do not finish the target.',
],expected_sha256=claim['input_sha256'],claim_token=claim['token'])
p=ROOT/'research/recovery-20260916/further-scope-choices.json'
choices=json.loads(p.read_text())
next(r for r in choices if r['id']==identifier).update(state='applied',applied_on=DATE)
p.write_text(json.dumps(choices,ensure_ascii=False,indent=2)+'\n')
