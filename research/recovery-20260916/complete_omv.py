"""Complete the Boolean online matrix-vector conjecture's algorithmic target."""
import sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];sys.path.insert(0,str(ROOT/'research/card-completion-20260913'))
from complete_review import complete,ref,block,progress,DATE
from review_queue import read_claims
identifier='TCS-6503';claim=read_claims(ROOT)[identifier]
notes=[
 'Preserved the algorithm-existence orientation: a yes answer refutes the named OMv conjecture, and a no answer proves it in the stated model.',
 'Specified one uniform classical randomized word-RAM, a fixed positive exponent saving, charged preprocessing, explicit Boolean inputs and online output deadlines.',
 'Made the total bound worst-case over random executions and success a joint event for the entire sequence, with fixed inputs independent of the coins.',
 'Distinguished all-input word-RAM time from the known subcubic cell-probe bound, restricted structured-matrix algorithms and uncharged-preprocessing variants.',
 'Read the original conjecture, the faster randomized algorithm, the exact 2025 non-Boolean equivalence list and the February 2026 structured-matrix revision.',
 'Corrected the origin year to 2015, preserved importance 94 and category, replaced first-person motivation and removed the worked reduction from reader context.',
]
sources=[
 'Read Henzinger–Krinninger–Nanongkai–Saranurak, arXiv:1511.06773v1 of 20 November 2015, §1 Conjecture 1.1 p. 3 and §1.1 on dynamic consequences. Also checked the separate §2.1 heading and formulation for polynomial preprocessing; it is not substituted for the charged-total target.',
 'Read Larsen–Williams, arXiv:1605.01695v2 of 6 May 2016 (SODA 2017), §1.1 Theorem 1.1 p. 1 and Theorem 1.3 pp. 2–3. The randomized algorithm saves a superpolylogarithmic but subpolynomial factor, whereas the truly subquadratic query bound is in the cell-probe model with computation free.',
 'Read Hu–Polak, ESA 2025 Article 54, publisher date 1 October 2025, §1.1 Theorem 1 pp. 54:2–54:3 and the following cell-probe discussion. Equality and dominance are existential versions; the list also includes min-witness, min-max and bounded monotone min-plus. These are equivalences, not a proof of their hardness. The bounded monotone min-plus implication permits randomization.',
 'Read Anand–van den Brand–McCarty, arXiv:2502.21240v3 of 9 February 2026, primary abstract and version history; NeurIPS 2025 publication also checked. Its subquadratic query bound depends on bounded VC dimension (or a non-Boolean structural parameter), not arbitrary Boolean matrices. Full proof not independently audited.',
 f'Bounded primary-source searches through {DATE} found no verified classical truly subcubic algorithm or unconditional lower bound for unrestricted Boolean OMv in the specified model. Later works applying OMv as a hypothesis do not themselves establish its truth.',
]
complete(identifier,dict(
 criterion='resources',question_type='yes_no',year=2015,
 formal=r'''Do there exist a real constant \(\varepsilon\in(0,1)\), a constant \(K>0\), an integer word-size constant \(B\ge3\), and one uniform classical randomized algorithm \(A\) with the following property? For every integer \(n\ge2\), every Boolean matrix \(M\in\{0,1\}^{n\times n}\), and every sequence \(v_1,\ldots,v_n\in\{0,1\}^n\) supplied online, the algorithm outputs each \(Mv_t\) before receiving \(v_{t+1}\), and outputs \(Mv_n\) at the end, using at most
\[
 K n^{3-\varepsilon}
\]
word-RAM instructions in total on every execution, including preprocessing of \(M\), with probability at least \(2/3\) that all \(n\) output vectors are correct? Products are over the Boolean semiring:
\[
 (Mv_t)_i=\bigvee_{j=1}^{n}\bigl(M_{ij}\wedge(v_t)_j\bigr).
\]
The OMv conjecture asserts a negative answer.''',
 definitions=r'''The input initially supplies \(n\) and all \(n^2\) entries of the fixed matrix \(M\), in row-major order. After the algorithm's initial preprocessing, vectors arrive one at a time in the order \(v_1,\ldots,v_n\). Each vector is an arbitrary length-\(n\) bit string. The next vector is unavailable until the algorithm has finished returning the current vector's complete answer. The algorithm may preserve its computed state and earlier vectors, but cannot postpone an output to use future inputs. There is no per-query time bound beyond the total bound and these deadlines.

Both the matrix bit string and each input vector are explicitly packed into consecutive words with known zero padding. An output vector contains its \(n\) bits in coordinate order; an explicit array with one Boolean value per word is an allowed canonical output representation. Returning an implicit circuit, a pointer to uncomputed answers, a count of nonzero entries or just one queried coordinate is insufficient. All input access and output writes are charged. The matrix never changes. The operations \(\wedge\) and \(\vee\) mean Boolean AND and OR; this is neither arithmetic multiplication over the reals nor multiplication over the field of two elements.

The computation is a sequential word RAM with
\[
 w=B\lceil\log_2(n+2)\rceil
\]
bits per word and one fixed finite program for all \(n\). Memory cells, registers and addresses are word-sized. Unit-cost instructions are reads, writes, copies, comparisons, branches, bitwise Boolean operations, logical shifts, addition, subtraction and multiplication modulo \(2^w\), and unsigned quotient and remainder with nonzero divisor. Shifts by at least \(w\) positions return zero. Multiword computations cost their component instructions. An independent uniform random \(w\)-bit word can be generated in one instruction. This permits deterministic algorithms as a special case. There are no quantum instructions, nonuniform advice, free precomputed tables or input-dependent oracles. Unused memory initially contains zero.

All instructions are counted, including construction of auxiliary tables, allocation or initialization performed by the program, preprocessing before the first vector, work between vectors, generation of random words, copying and output. There is no separate allowance for an arbitrary polynomial preprocessing phase. Space has no additional sublinear or near-linear restriction, but every address must fit in a word and writing any used state costs instructions. Only the currently supplied input is made available by the online interface; it supplies no information about a future vector.

For the success guarantee, the matrix and complete vector sequence are fixed independently of the algorithm's randomness. The probability is over the program's random words, and the successful event requires every bit of every output to be correct. A separate success probability of \(2/3\) for each individual query is not the specified joint guarantee. The time bound holds for every random execution, including erroneous executions. Every output deadline and eventual termination must likewise be met on every execution.

The constants \(\varepsilon,K,B\) and the program are chosen once, independently of the input dimension and contents. Any fixed \(\varepsilon\in(0,1)\) suffices. A merely logarithmic or subpolynomial improvement in total time is not a fixed exponent saving. No restriction to combinatorial algorithms is imposed: every algorithm implementable by the specified word-RAM instructions is allowed.''',
 answer_criterion=r'''Give a complete Lean-checked proof that the stated algorithm exists, or a complete Lean-checked proof that no such algorithm and constants exist.

A positive answer must establish the fixed exponent saving after charging preprocessing and all input/output work, the online deadlines, and joint success for every fixed input. It refutes the OMv conjecture in this model. A negative answer must exclude every admissible uniform randomized program, every fixed word-size constant and every positive exponent saving. It proves the conjecture in this model and cannot assume the conjecture itself or another unproved hardness hypothesis.

An algorithm for structured matrices, an offline matrix product, a query bound after uncharged preprocessing, or a cell-probe bound with free computation does not meet the target without a proved extension. Neither does a speedup of the form \(n^3/2^{\Omega(\sqrt{\log n})}\), which supplies no fixed positive saving in the exponent.''',
 source_formulation=dict(text='Conjecture 1.1 rules out a fixed polynomial saving over cubic total time for online Boolean matrix-vector multiplication with error at most one third. The card asks for an algorithm with such a saving, so its conjectured answer is no, and makes the charged uniform word-RAM and complete-sequence error conventions explicit.',caption='Paraphrase of Henzinger–Krinninger–Nanongkai–Saranurak, arXiv:1511.06773v1, §1 Conjecture 1.1 p. 3; STOC 2015.',citation='primary',format='editorial_paraphrase'),
 references=[
 ref('primary','Unifying and Strengthening Hardness for Dynamic Problems via the Online Matrix-Vector Multiplication Conjecture','Monika Henzinger; Sebastian Krinninger; Danupon Nanongkai; Thatchaphol Saranurak',2015,'https://arxiv.org/abs/1511.06773v1','20 November 2015 version, STOC 2015; §1 Conjecture 1.1 p. 3 and dynamic consequences in §1.1; §2.1 treats a separate preprocessing formulation'),
 ref('faster','Faster Online Matrix-Vector Multiplication','Kasper Green Larsen; Ryan Williams',2017,'https://arxiv.org/abs/1605.01695v2','6 May 2016 version, SODA 2017; §1.1 Theorem 1.1 p. 1 and distinct cell-probe Theorem 1.3 pp. 2–3'),
 ref('equivalence','Non-Boolean OMv: One More Reason to Believe Lower Bounds for Dynamic Problems','Bingbing Hu; Adam Polak',2025,'https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.ESA.2025.54','Published 1 October 2025; §1.1 Theorem 1 pp. 54:2–54:3 and following cell-probe discussion'),
 ref('structured','The Structural Complexity of Matrix-Vector Multiplication','Emile Anand; Jan van den Brand; Rose McCarty',2026,'https://arxiv.org/abs/2502.21240v3','Revision of 9 February 2026, NeurIPS 2025 paper; primary abstract, VC-dimension-dependent query bound; full proof not independently audited'),
 ],
 why='The conjecture supports many precise lower bounds for dynamic graph and data-structure problems. A general truly subcubic online algorithm would overturn these conditional barriers, while an unconditional lower bound would explain a shared obstacle to faster dynamic algorithms.',
 context_blocks=[
 block('The online requirement separates this task from ordinary matrix multiplication: each answer must be committed before a future query arrives. The original work develops reductions from this task to many dynamic problems.'),
 block(r'Larsen and Williams obtain a randomized total bound of \(n^3/2^{\Omega(\sqrt{\log n})}\). Its speedup is larger than any fixed polylogarithmic factor but does not supply the fixed exponent saving requested here.','faster'),
 block(r'The same work gives a genuinely subquadratic query bound in the cell-probe model, where computation between memory accesses is free. This separates a known information-access bound from the charged computation required by the card.','faster'),
 block('Hu and Polak establish subcubic equivalences with existential equality and dominance products, min-witness, min-max and bounded monotone min-plus variants. These equivalences transfer algorithmic breakthroughs or hypotheses; they do not prove the hypotheses.','equivalence'),
 block('The February 2026 revision gives faster queries when the matrix has bounded VC dimension, with corresponding extensions to other structured inputs. Arbitrary Boolean matrices are not subject to that promise.','structured'),
 ],
 progress=[progress('2015','The online Boolean conjecture is formulated and used to derive dynamic-problem lower bounds.'),progress('2016-05-06','A randomized algorithm gives a superpolylogarithmic speedup, and a separate cell-probe result reaches a fixed exponent saving.','faster'),progress('2025-10-01','Several non-Boolean online products are shown equivalent at the truly subcubic scale.','equivalence'),progress('2026-02-09','The revised structured-matrix work gives faster queries under a VC-dimension bound.','structured')],
),notes,sources,'The fixed-exponent improvement for unrestricted Boolean OMv remains unresolved in the bounded primary-source review through 17 September 2026. The checked faster general algorithm, cell-probe algorithm, non-Boolean equivalences and February 2026 structured-matrix revision do not settle the charged uniform word-RAM target. This is not exhaustive certification of openness or independent verification of every cited proof.',summary=[
 'A fixed Boolean matrix is given first, followed by a sequence of Boolean vectors.',
 'The algorithm must return each Boolean product before it sees the next vector.',
 'The question asks for a fixed polynomial saving over cubic total time, including preprocessing, with a constant probability that every answer is correct.',
 'Known speedups, free-computation cell-probe bounds and faster structured-matrix queries do not resolve the unrestricted word-RAM target.',
 'A complete Lean-checked resolution would either refute or prove a central hypothesis behind dynamic-problem lower bounds.',
],expected_sha256=claim['input_sha256'],claim_token=claim['token'])
