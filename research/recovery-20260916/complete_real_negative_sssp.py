"""Complete near-linear comparison-addition SSSP with arbitrary signed reals."""
import sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];sys.path.insert(0,str(ROOT/'research/card-completion-20260913'))
from complete_review import complete,ref,block,progress,DATE
from review_queue import read_claims
identifier='TCS-7341';claim=read_claims(ROOT)[identifier]
notes=[
 'Preserved the approved arbitrary-real, comparison-addition target with polylogarithmic overhead, bounded error and worst-case operation cost.',
 'Specified the negative-cycle promise globally, exact distances to every vertex, unreachable markers and the empty source path.',
 'Expanded the real-cell/control-word separation and charged all input access, random generation and output; retained polynomial rational encoding lengths and space.',
 'Read the exact source question and distinguished it from the adjacent integer-weight derandomization question, which later work answers.',
 'Checked both independent February 2026 almost-quadratic real-weight results, the integer-weight deterministic results and the new 14 September 2026 revision with remaining numerical dependence.',
 'Preserved importance 94 and category, removed the broad textbook background citation, and required a Lean proof covering every density and real weight assignment.',
]
sources=[
 'Read Bringmann–Cassis–Fischer, arXiv:2304.05279v1 of 11 April 2023, §1.4 Question 3 printed p. 9: removal of the weight-scale factor and strongly polynomial near-linear time. Read the neighboring Question 4 separately; it asks for derandomization in the integer-weight setting.',
 'Read Bernstein–Nanongkai–Wulff-Nilsen, arXiv:2203.03456v6 of 20 May 2025, primary abstract, and its historical attribution in the 2023 source: the 2022 breakthrough has integral weights and a log W factor.',
 'Read Haeupler–Jiang–Saranurak, arXiv:2511.08551v1 of 11 November 2025, primary abstract, with explicit integer weights and log(nW) dependence; checked its official STOC 2026 proceedings entry. Also read Jason Li, arXiv:2511.07859v2 of 8 April 2026, primary abstract, independently giving deterministic near-linear integer-weight SSSP.',
 'Read Li–Li–Zhang, arXiv:2602.16153v1 of 18 February 2026, abstract, introduction and Theorem 1 p. 1: randomized n^{2+o(1)} time for real weights. Read the primary abstract of the independent Khanna–Song arXiv:2602.16638v1 from the same day: the same asymptotic bound with high probability. Neither stated bound gives near-linear time on sparse graphs or a polylogarithmic dense overhead.',
 'Read Duong, arXiv:2609.05590v2, revised 14 September 2026, primary abstract and version history. It states deterministic O((m+n log log n) log^2 n log(nW)) time for integral weights at least -W. The full proof was not independently audited; even the stated improvement retains numerical dependence.',
 'Read Hair–Li–Li–Zhang, arXiv:2607.19342v1 of 21 July 2026, primary abstract. The work/span tradeoff explicitly assumes nonnegative real weights, so it does not supply the general signed-real target. No full proof audit was undertaken.',
 f'Bounded primary-source searches through {DATE} found no verified near-linear comparison-addition algorithm for all real-weighted graphs. Related active TCS-7263 concerns nonnegative weights and exactly linear time; TCS-6510 concerns all-pairs distances and a subcubic bound.',
]
complete(identifier,dict(
 criterion='resources',question_type='yes_no',
 formal=r'''Do there exist one uniform classical randomized comparison-addition algorithm \(A\), constants \(C>0\), integers \(k\ge0\) and \(B\ge3\), and a polynomial \(p\) with the following property? For every directed graph with \(n\ge2\) vertices, \(m\) arcs, arbitrary real arc lengths and no negative directed cycle, and every specified source \(s\), every execution of \(A\) halts within
\[
 C(m+n)\lceil\log_2(n+2)\rceil^k
\]
instructions in the model below, and with probability at least \(2/3\) outputs all exact distances from \(s\)? The bound is uniform over all graph densities and real weight assignments and is independent of numerical magnitude or encoding length. On rational inputs the additional encoding-space bound is \(p(L)\), where \(L\) is the full binary input length.''',
 definitions=r'''The input contains the vertex set \(V=\{1,\ldots,n\}\), a source \(s\in V\), and an explicit ordered list \(E\) of \(m\) directed arcs with their real lengths \(\lambda_e\in\mathbb R\). There are no loops and at most one arc per ordered pair; opposite arcs are allowed. Thus \(0\le m\le n(n-1)\). Isolated vertices and disconnected graphs are allowed. Lengths may be positive, zero or negative and are otherwise unrestricted.

The length of a finite directed walk is the sum of its traversed arc lengths, counting repeated arcs. The empty walk from a vertex to itself has length zero. The promise is that every directed cycle in the entire graph has nonnegative total length, including cycles unreachable from \(s\). For each vertex \(v\), define
\[
 d(s,v)=\inf\left\{\sum_{e\in P}\lambda_e:
                 P\text{ is a directed walk from }s\text{ to }v\right\}.
\]
If no such walk exists, the output is a distinguished \(+\infty\) marker. Otherwise the promise makes the value finite, attained by a simple path (or the empty path when \(v=s\)). In particular \(d(s,s)=0\). The algorithm must explicitly output all \(n\) entries in vertex order, with exact real values for reachable vertices. Reporting a negative cycle is not an alternative valid answer on a promised input. Behavior outside the negative-cycle promise is not part of the requested guarantee.

The machine is a comparison-addition RAM with exact real cells and unsigned control/address words of
\[
 w=B\lceil\log_2(n+2)\rceil
\]
bits. Input arcs, endpoints and lengths initially occupy explicit memory cells. The program is finite and fixed for all sizes, with only finitely many fixed rational constants. It has no nonuniform advice, input-dependent precomputed table or numerical-encoding oracle. Unused memory initially contains zero.

On real cells the unit-cost operations are reading, writing, copying, addition, subtraction and exact comparison. No multiplication or division of real values, floor, bit extraction or conversion of an input-dependent real value into a word is available. Real cells cannot be used as addresses. The infinity output is a tagged marker, not a real on which unrestricted arithmetic is allowed.

Word operations have unit cost: reads, writes, copies, comparisons, branches, bitwise Boolean operations, logical shifts, addition, subtraction and multiplication modulo \(2^w\), and unsigned integer quotient and remainder with a nonzero divisor. Shifts by at least \(w\) positions return zero. Word arithmetic cannot inspect or operate on an encoding of a real cell. Multiword calculations cost their component instructions. A fresh independent uniform \(w\)-bit random word costs one instruction; all generated random words are independent. Every used address must fit in one word.

All computation is charged, including memory access, control, preprocessing, random generation and output. The time bound holds for each promised input and every random execution, including those producing an incorrect answer. Correctness is the joint event that the complete distance vector and all unreachable markers are correct, with probability at least \(2/3\) for each fixed input. Deterministic algorithms are included.

On rational inputs, encode each real input length by a binary numerator and positive denominator, and let \(L\) count these bits together with the entire graph description. Every stored rational, written in reduced form, must have numerator and denominator lengths at most \(p(L)\), and the total bit space used to represent all cells and control words must also be at most \(p(L)\), on every execution. This additional condition is separate from the arithmetic operation count. No finite encoding is imposed on an arbitrary real input; the comparison-addition operations specify how it can be accessed.

The program and \(C,k,B,p\) are chosen once and cannot depend on the graph, source, weight values or their ordering. The term near-linear in this card means the displayed fixed polylogarithmic overhead over \(m+n\). It is not the weaker overhead \((m+n)^{o(1)}\). Restricting lengths to bounded integers or requiring all lengths to be nonnegative changes the task.''',
 answer_criterion=r'''Supply a complete Lean-checked proof of the stated algorithm's existence or a complete Lean-checked proof of the logical negation.

A positive answer must establish exactness of the entire output, the per-input success probability, worst-case comparison-addition cost for arbitrary real lengths, and polynomial encoding space on rational inputs. It must cover sparse as well as dense graphs. A deterministic algorithm with these bounds qualifies.

A negative answer must exclude every admissible uniform algorithm and every fixed polylogarithmic exponent in this model. A lower bound for one particular framework or a conditional result under an unproved conjecture does not establish that negation. An integer-weight algorithm whose operation count depends on weight magnitude, an almost-quadratic bound independent of m, or a merely approximate-distance algorithm is insufficient without a proved extension meeting the full target.''',
 source_formulation=dict(text='Question 3 asks whether the numerical weight factor can be removed entirely, yielding a strongly polynomial near-linear algorithm for negative-weight single-source shortest paths. The card retains the approved comparison-addition formulation over arbitrary real lengths and a promise excluding negative cycles.',caption='Paraphrase of Bringmann–Cassis–Fischer, arXiv:2304.05279v1, §1.4 Question 3 p. 9; the separate derandomization question is Question 4.',citation='primary',format='editorial_paraphrase'),
 references=[
 ref('primary','Negative-Weight Single-Source Shortest Paths in Near-Linear Time: Now Faster!','Karl Bringmann; Alejandro Cassis; Nick Fischer',2023,'https://arxiv.org/abs/2304.05279v1','11 April 2023; §1.4 Question 3 printed p. 9; Question 4 is the separate integer-weight derandomization target'),
 ref('bernstein','Negative-Weight Single-Source Shortest Paths in Near-linear Time','Aaron Bernstein; Danupon Nanongkai; Christian Wulff-Nilsen',2022,'https://arxiv.org/abs/2203.03456v6','Original 2022 result; checked version 6, 20 May 2025, primary abstract with integral weights and log W dependence'),
 ref('detinteger','Deterministic Negative-Weight Shortest Paths in Nearly Linear Time via Path Covers','Bernhard Haeupler; Yonggang Jiang; Thatchaphol Saranurak',2026,'https://arxiv.org/abs/2511.08551v1','11 November 2025 preprint, STOC 2026; primary abstract, explicit integer-weight bound with log(nW) dependence'),
 ref('padded','Deterministic Padded Decompositions and Negative-Weight Shortest Paths','Jason Li',2026,'https://arxiv.org/abs/2511.07859v2','Version 2, 8 April 2026; STOC 2026; primary abstract, deterministic near-linear integer-weight result'),
 ref('dense2026','Bellman-Ford in Almost-Linear Time for Dense Graphs','George Z. Li; Jason Li; Junkai Zhang',2026,'https://arxiv.org/abs/2602.16153v1','18 February 2026; introduction and Theorem 1 p. 1, randomized n^{2+o(1)} time for real weights'),
 ref('khanna',r'An \(n^{2+o(1)}\) Time Algorithm for Single-Source Negative Weight Shortest Paths','Sanjeev Khanna; Junkai Song',2026,'https://arxiv.org/abs/2602.16638v1','18 February 2026; primary abstract, independent almost-quadratic real-weight result; full proof not independently audited'),
 ref('september','Size-Sensitive Padded Decompositions for Faster Deterministic Negative-Weight Shortest Paths','Khoi Duong',2026,'https://arxiv.org/abs/2609.05590v2','Version 2, 14 September 2026; primary abstract and version history; integral weights and remaining log(nW) factor; full proof not independently audited'),
 ],
 context_blocks=[
 block('The source separates removing numerical dependence from derandomizing an integer-weight algorithm. The former is this card’s target; progress on the latter does not by itself answer it.'),
 block(r'The 2022 near-linear breakthrough applies to integral weights and includes a \(\log W\) factor, where W bounds the negative weight scale. This is different from a bound depending only on the graph size.','bernstein'),
 block('The path-cover result gives deterministic near-linear time for integer weights while retaining numerical dependence. Independently, the padded-decomposition result also derandomizes the integer-weight setting.','detinteger'),
 block(r'The February 2026 real-weight theorem gives \(n^{2+o(1)}\) time. That is almost linear when \(m=\Theta(n^2)\), but does not provide the sparse-graph bound or guarantee a fixed polylogarithmic overhead.','dense2026'),
 block('An independent paper from the same day obtains the same almost-quadratic real-weight scale. Its scope likewise leaves the general near-linear target unanswered.','khanna'),
 block(r'The preprint revised on 14 September 2026 states a faster deterministic bound for integral weights, but still includes \(\log(nW)\). Its abstract and version history were checked; the proof was not independently audited. Even its stated improvement does not remove numerical dependence.','september'),
 ],
 progress=[progress('2022','Near-linear integer-weight algorithms become available with numerical scaling dependence.','bernstein'),progress('2023-04-11','The improved integer-weight algorithm explicitly leaves strong polynomiality as an open question.'),progress('2025-11-11','Deterministic near-linear integer-weight algorithms are announced.','detinteger'),progress('2026-02-18','An almost-quadratic algorithm is announced for arbitrary real weights.','dense2026'),progress('2026-02-18','An independent real-weight result reaches the same asymptotic scale.','khanna'),progress('2026-09-14','The revised deterministic integer-weight preprint improves logarithmic factors while retaining numerical dependence.','september')],
),notes,sources,'The checked real-weight algorithms remain almost quadratic in n, while the integer-weight advances, including the preprint revised on 14 September 2026, retain dependence on weight scale. Bounded primary-source checks through 17 September 2026 found no verified near-linear comparison-addition algorithm with fixed polylogarithmic overhead for all arbitrary-real inputs in the stated promise. This is not an exhaustive certification of openness or an independent proof audit of all cited results.',summary=[
 'The input is a directed graph with arbitrary real arc lengths and no negative directed cycle.',
 'The task is to output every exact distance from one source, marking unreachable vertices.',
 'The question asks for a uniform randomized comparison-addition algorithm with only polylogarithmic overhead over the graph size.',
 'Recent integer-weight improvements retain numerical dependence, and almost-quadratic real-weight algorithms do not give the sparse-graph target.',
 'An accepted answer must provide a complete Lean-checked resolution with worst-case operation bounds and polynomial rational encoding space.',
],expected_sha256=claim['input_sha256'],claim_token=claim['token'])
