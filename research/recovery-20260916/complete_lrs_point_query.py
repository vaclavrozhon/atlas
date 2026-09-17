"""Review uniform deterministic testing of one binary-addressed rational LRS term."""
import sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT/'research/card-completion-20260913'))
from complete_review import complete,ref,block,progress
from review_queue import read_claims
identifier='TCS-0095';claim=read_claims(ROOT)[identifier]
complete(identifier,dict(
 status='source_open',criterion='resources',question_type='yes_no',
 formal=r'''Does there exist one deterministic algorithm that, given a rational linear recurrence and a nonnegative index \(n\) in binary, decides whether its \(n\)-th term is exactly zero in time polynomial in the total input bit length? Both the recurrence and its initial values are part of the input, and its order is unrestricted.''',
 definitions=r'''An input consists of an integer \(k\ge1\), rational numbers \(c_0,\ldots,c_{k-1}\) and \(u_0,\ldots,u_{k-1}\), and an integer \(n\ge0\). They define the unique sequence \(f:\mathbb N\to\mathbb Q\) by
\[
f(i)=u_i\quad(0\le i<k),\qquad
f(t+k)=\sum_{i=0}^{k-1}c_i f(t+i)\quad(t\ge0).
\]
The supplied order need not be minimal; zero coefficients, repeated characteristic roots and degenerate recurrences are allowed.

Integers are encoded in binary, with a sign bit when needed. Each rational is a reduced numerator/positive-denominator pair. Use a fixed explicit length-delimited encoding for the two lists and all integers, and let \(L\) be its total length. In particular, \(n\) is not written in unary and the coefficient and initial-value bit lengths count toward \(L\).

The quantified algorithm is a deterministic multi-tape Turing machine \(M\). There must be constants \(K>0\) and \(a\in\mathbb N\) such that on every valid input it halts within \(K(L+1)^a\) steps and outputs 1 if and only if \(f(n)=0\). The machine and both constants are independent of \(k\), all rational data and \(n\). No randomness, advice or oracle is supplied. Arithmetic operations must be implemented and charged at their actual bit cost.

Only a decision bit is required, not the value \(f(n)\). For example, the sequence \(f(n)=2^n\) can require exponentially many output bits relative to the length of its index, without making its zero test difficult. The question concerns the specified index alone: it does not ask whether a zero exists at some index below \(n\), or anywhere in the sequence.''',
 answer_criterion='Give a complete mathematically correct Lean-checked proof of the existence of the stated deterministic polynomial-bit-time decider, including correctness and the uniform running-time bound, or a proof of its logical negation. A polynomial arithmetic-operation count with unbounded unit-cost integers, a randomized decider, or a separate hardcoded algorithm for each fixed recurrence does not establish the affirmative statement.',
 why='A single term of a rational recurrence has a compact arithmetic representation even when its expanded numerator is enormous. This question isolates whether exact zero testing for that representation can be performed efficiently without randomness.',
 source_formulation=dict(text='Clemente asks for polynomial-time testing of a rational recurrence term at a binary-encoded index. This review makes the varying recurrence and deterministic bit model explicit.',caption='Automata Exchange, problem 25.4, contributed 1 July 2025.',citation='primary',format='editorial_paraphrase'),
 references=[
 ref('primary','25.4 Efficient LRS evaluation','Lorenzo Clemente',2025,'https://automata.exchange/25.4-efficient-lrs-evaluation/','Full problem statement, 1 July 2025'),
 ref('skolem','On the Complexity of the Skolem Problem at Low Orders','Piotr Bacik; Joël Ouaknine; James Worrell',2026,'https://people.mpi-sws.org/~joel/publications/skolem-complexity25.pdf','SODA 2026 author version; Introduction PDF pp.1–2 (Skolem–Mahler–Lech and EqSLP); §2.1 PDF p.3 (companion-matrix representation)'),
 ],
 context_blocks=[
 block('Binary addressing makes generating every preceding term potentially exponential in the input length. The formal target therefore counts all coefficient bits and allows the order to vary.'),
 block('Repeated matrix squaring gives a small arithmetic circuit for an indexed integer term. Testing its output for zero lies in coRP. This randomized result does not give the deterministic algorithm requested here.','skolem'),
 block('Editorial extension to rational inputs: maintain numerator and nonzero denominator as integer arithmetic circuits at each rational gate. The numerator zero test preserves the same randomized upper bound.','skolem'),
 block('The Skolem–Mahler–Lech description of zero sets implies, for each fixed recurrence separately, an efficient test with its finite exceptional set and arithmetic progressions hardcoded. This editorial implication does not provide a uniform way to obtain that data.','skolem'),
 block('The SODA 2026 bounded Skolem result instead searches an interval and has a fixed-order randomized polynomial bound. Its quantifiers differ from this single-index deterministic question.','skolem'),
 ],
 progress=[progress('2025-07-01','Clemente contributes the binary-index evaluation question.'),progress('2026','The SODA paper records randomized arithmetic-circuit zero testing as a subroutine for recurrence problems.','skolem')],
),[
 'Specified the recurrence, initial values and binary index as joint input to one deterministic bit-time algorithm.',
 'Applied the announced recommended uniform interpretation after the optional question received no reply; this is an editorial default, not user confirmation.',
 'Separated single-index testing, bounded zero search and fixed-recurrence existence; preserved the existing importance assessment.',
 'Included exact rational encoding, unrestricted supplied order, and a complete Lean-checked answer criterion.',
],[
 'Read the complete Automata Exchange 25.4 statement. Its short wording does not explicitly settle fixed versus input recurrence.',
 'Read the final SODA 2026 author PDF, Introduction pp.1–2 and companion-matrix definition §2.1 p.3. The earlier arXiv version was also checked. The fixed-sequence and rational-input explanations are editorial deductions.',
 'Bounded primary-source search through 17 September 2026 did not locate a deterministic uniform polynomial-bit-time resolution.',
], 'Source-open for the specified uniform deterministic bit model. Randomized circuit zero testing and fixed-sequence nonuniform existence do not resolve this formulation. The source’s short question is made precise by an announced editorial default, not an unreceived user confirmation. Status checked through 17 September 2026.',summary=[
 'The input gives a rational linear recurrence, its initial values and an index written in binary.',
 'The target is one deterministic algorithm that decides whether exactly that indexed term is zero.',
 'Its running time must be polynomial in the combined input bit length, including the recurrence order and coefficient descriptions.',
 'Randomized testing of a compact arithmetic representation is known, while printing the full term may take exponentially many bits.',
 'An answer must provide a complete Lean-checked uniform algorithm and time analysis or prove that no such algorithm exists.',
],expected_sha256=claim['input_sha256'],claim_token=claim['token'])
