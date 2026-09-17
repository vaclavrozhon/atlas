"""Review deterministic bit complexity of fixed-dimensional matrix-power signs."""
import sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT/'research/card-completion-20260913'))
from complete_review import complete,ref,block,progress
from review_queue import read_claims
identifier='TCS-4490';claim=read_claims(ROOT)[identifier]
complete(identifier,dict(
 title='Polynomial-time sign testing of matrix powers in every fixed dimension',
 status='source_open',criterion='resources',question_type='yes_no',
 formal=r'''Is it true that for every fixed integer dimension \(d\ge1\), there is a deterministic polynomial-bit-time algorithm which, given matrices \(M,W\in\mathbb Z^{d\times d}\) and an exponent \(n\ge0\), all in binary, decides whether
\[
\sum_{i=1}^{d}\sum_{j=1}^{d} W_{ij}(M^n)_{ij}\ge0?
\]
The algorithm and the degree of its polynomial running-time bound may depend on \(d\), but not on the entries of \(M,W\) or on \(n\).''',
 definitions=r'''Matrix multiplication is the usual operation over the integers, and \(M^0=I_d\). The input matrix \(W\) represents the integer linear functional \(f_W(X)=\sum_{i,j}W_{ij}X_{ij}\). Its coefficients are arbitrary signed integers, just like those of \(M\). The decision concerns this one scalar value at the supplied exponent, not entrywise nonnegativity of every matrix power or positive semidefiniteness.

For each fixed \(d\), encode \(M\) and \(W\) by their full lists of signed binary entries and encode \(n\) in binary, using fixed length delimiters. Let \(L\) be the total bit length of this representation. The statement asks for
\[
\forall d\ge1\ \exists A_d\ \exists K_d>0\ \exists a_d\in\mathbb N\ \forall(M,W,n):
\operatorname{time}_{A_d}(M,W,n)\le K_d(L+1)^{a_d},
\]
with the stated exact yes/no output. Each \(A_d\) is a deterministic multi-tape Turing machine without advice, randomness or an oracle. It must handle singular matrices, negative entries, repeated eigenvalues and exact zero values. Every arithmetic operation is charged at its bit cost. The output is a single bit; neither \(M^n\) nor \(f_W(M^n)\) must be printed in full.

The quantifiers impose no common exponent \(a_d\), no common multiplicative constant \(K_d\), and no effective procedure for converting \(d\) into the code of \(A_d\). They ask for polynomial-time membership separately in every fixed dimension. Requiring one polynomial-time machine for all input dimensions would be a stronger target. Conversely, fixing \(M\) or \(W\) in addition to \(d\) would be weaker than this question. The case \(n=0\) is included by the identity convention and is directly decidable.''',
 answer_criterion='Give a complete mathematically correct Lean-checked proof of this proposition or its logical negation. A positive proof must provide the algorithms and polynomial bit-time analyses for every fixed dimension. A negative proof must establish a fixed dimension at which no deterministic polynomial-time algorithm exists. An arithmetic-operation bound with unit-cost unbounded integers, a unary exponent algorithm, or a result only for matrices whose entries are supplied in unary does not establish the requested statement.',
 why='Matrix powering compactly describes integers with exponentially many output bits. Deciding one exact sign tests whether low-dimensional algebraic structure permits efficient computation without expanding those integers.',
 importance=dict(score=77,method='editorial',reason='A focused exact-arithmetic complexity question connected to recurrence positivity and succinct integer computation; it distinguishes fixed-dimensional spectral methods from general arithmetic circuits.'),
 source_formulation=dict(text='The source leaves the complexity of PosMatPow in higher dimensions open. This card selects deterministic polynomial bit time separately for each fixed dimension, with all entries and the exponent in binary.',caption='STACS 2015, Introduction pp.329–330; footnotes 2–3 specify bit cost and the three-dimensional encoding restriction.',citation='primary',format='editorial_paraphrase'),
 references=[
 ref('primary','On Matrix Powering in Low Dimensions','Esther Galby; Joël Ouaknine; James Worrell',2015,'https://doi.org/10.4230/LIPIcs.STACS.2015.329','Introduction pp.329–330 and footnotes 2–3; Theorems 4 and 5 in §§3–4'),
 ref('counting','Counting Problems for Parikh Images','Christoph Haase; Stefan Kiefer; Markus Lohrey',2017,'https://doi.org/10.4230/LIPIcs.MFCS.2017.12','Introduction p.12:2: PosMatPow definition, encoding restrictions, reduction to PosSLP and counting-hierarchy upper bound'),
 ],
 context_blocks=[
 block('The source proves polynomial-time decidability in dimension two with binary data. Its dimension-three theorem requires the base matrix in unary, while the exponent and functional remain binary.'),
 block('Repeated squaring uses few matrix multiplications but can create exponentially long integers. A polynomial arithmetic-operation count therefore does not by itself answer the bit-complexity question.'),
 block('The 2017 paper records a reduction of general PosMatPow to integer arithmetic-circuit sign testing, PosSLP, and hence an upper bound in the counting hierarchy. This is not a deterministic polynomial-time upper bound.','counting'),
 block('That paper also uses PosMatPow hardness in the study of counting words with prescribed letter multiplicities. Its general-dimension application should not be mistaken for a lower bound ruling out this fixed-dimension target.','counting'),
 block('The selected statement asks about a single input exponent. Universal nonnegativity over all exponents is a different recurrence problem.'),
 ],
 progress=[progress('2015','The source proves the dimension-two result and the unary-base-matrix dimension-three result, then asks about higher dimensions.'),progress('2017','PosMatPow is used as a hardness benchmark for counting problems, with its exact complexity still left open.','counting')],
),[
 'Selected every fixed dimension with dimension-dependent polynomial bounds after the optional clarification received no reply; recorded as an announced editorial default.',
 'Specified one scalar linear functional, binary exponent and all binary matrix entries, exact nonnegative output and actual bit cost.',
 'Preserved the dimension-three unary-matrix restriction and distinguished fixed dimension from an input dimension.',
 'Assessed importance individually and required complete Lean-checked algorithms or the exact logical negation.',
],[
 'Read STACS 2015 pp.329–330 including both encoding footnotes, and the Theorem 5 statement in §4. The abstract alone omits the dimension-three qualification.',
 'Read MFCS 2017 Introduction p.12:2, which restates the qualified low-dimensional results and the PosSLP reduction.',
 'Bounded primary-source searches through 17 September 2026 did not find a solution of the selected all-fixed-dimensions binary-input polynomial-time statement.',
], 'Source-open for deterministic polynomial bit time in every fixed dimension with binary matrix and functional entries. The dimension-three theorem cited in the source assumes a unary base matrix. The per-dimension polynomial-time target is an announced editorial precisification of the broader source question. Bounded status review through 17 September 2026.',summary=[
 'The input specifies an integer matrix, an integer linear functional and a nonnegative binary exponent.',
 'The task is to decide whether applying the functional to that matrix power gives a nonnegative integer.',
 'The question asks for deterministic polynomial bit time separately in every fixed matrix dimension.',
 'The polynomial bound may depend on the dimension, while all matrix and functional entries remain part of the binary input.',
 'A complete Lean-checked affirmative algorithmic proof or a fixed-dimensional impossibility proof is required.',
],expected_sha256=claim['input_sha256'],claim_token=claim['token'])
