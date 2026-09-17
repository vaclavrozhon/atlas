"""Specify the SIS branch of the improved worst-case-to-average-case reduction target."""
import sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT/'research/card-completion-20260913'))
from complete_review import complete,ref,block,progress
from review_queue import read_claims
identifier='TCS-0659';claim=read_claims(ROOT)[identifier]
complete(identifier,dict(
 title='A classical SIS reduction from sublinear-factor GapSVP',
 status='source_open',criterion='reductions',question_type='yes_no',
 formal=r'''Do there exist absolute constants \(0<\varepsilon<1\) and \(C\ge1\), polynomially bounded computable modulus parameters as defined below, and a classical randomized polynomial-time worst-case-to-average-case reduction
\[
\operatorname{GapSVP}_{\gamma(n)}\ \longrightarrow\
\operatorname{SIS}_{n,m(n),q(n),\sqrt{m(n)}},
\qquad \gamma(n)=\max\{1,Cn^{1-\varepsilon}\},
\]
in the Euclidean norm? The reduction must solve every promised rank-\(n\) GapSVP instance from a SIS oracle that succeeds on only an inverse-polynomial fraction of uniformly random matrices. It must have polynomial overhead in the inverse of that success probability.''',
 definitions=r'''The modulus is one integer-valued function \(q(n)\), for \(n\ge2\), computed from \(1^n\) by one deterministic algorithm in time polynomial in \(n\). For some fixed integer \(d\ge3\), require
\[
n^3\le q(n)\le(n+1)^d,\qquad
m(n)=2n\lceil\log_2 q(n)\rceil+1.
\]
The function, its algorithm, and \(d\) are existentially chosen once. Primality is not required. These conventions select a polynomial-modulus, compressing SIS family, without fixing one numerical modulus schedule.

An SIS instance is a matrix \(A\in(\mathbb Z/q(n)\mathbb Z)^{n\times m(n)}\), with entries sampled independently and uniformly from the residues \(0,\ldots,q(n)-1\). A valid solution is a nonzero vector \(z\in\mathbb Z^{m(n)}\) satisfying
\[
Az=0\pmod{q(n)},\qquad
\sum_{i=1}^{m(n)}z_i^2\le m(n).
\]
This is an exact Euclidean norm bound, not an infinity-norm bound or a restriction to binary solutions. Encode each coordinate with a sign bit and \(\lceil\log_2(m(n)+1)\rceil\) magnitude bits, allowing unused encodings to be rejected. The trivial vector with a coordinate equal to \(q(n)\) is too long. Every matrix has a valid solution: since \(2^{m(n)}>q(n)^n\), two distinct binary vectors have the same image under \(A\), and their difference meets the displayed bound.

A worst-case input is an explicit full-column-rank integer matrix \(B\in\mathbb Z^{h\times n}\), with \(h\ge n\ge2\), and a positive rational radius \(r\). Entries, dimensions, and the numerator and denominator of \(r\) are given in binary; their complete length is \(L\). Write
\[
\mathcal L(B)=\{Bv:v\in\mathbb Z^n\},\qquad
\lambda_1(\mathcal L(B))=\min_{v\in\mathbb Z^n\setminus\{0\}}\|Bv\|_2.
\]
The promise is either \(\lambda_1\le r\), a yes-instance, or \(\lambda_1>\gamma(n)r\), a no-instance. The algorithm need not decide inputs between these thresholds.

The oracle formulation makes the average-case guarantee precise. For any integer \(t\ge1\), a permitted SIS oracle at parameter \(n\) is a fixed, possibly randomized map from matrices to either a valid solution in the stated encoding or a failure symbol \(\bot\), with
\[
\Pr_{A,\,O}[O(A)\ne\bot]\ge1/t
\]
when \(A\) is uniform. Calls use fresh independent oracle coins; the oracle has no mutable state between calls. It may fail on any selected set of inputs consistent with this average guarantee. No distributional assumption is made about its valid solutions, and the oracle need not be efficiently computable.

The desired reduction is one uniform classical probabilistic multitape oracle Turing machine \(R\) and constants \(K,a>0\). On input \((B,r,1^t)\), it may make adaptive queries to this rank-\(n\) SIS oracle, all with the parameters above. For every \(n,t\), every promised \((B,r)\), and every permitted oracle, it must output the correct yes/no answer with probability at least \(2/3\), over its own independent fair coins and the oracle coins. Every execution takes at most \(K(L+t+1)^a\) bit operations, including parameter computation, queries and responses; only the oracle's internal computation is free. For \(t\) polynomial in \(n\), this is the usual polynomial overhead for a non-negligible average success probability. There is no advice, quantum computation, auxiliary short-vector hint or other oracle.''',
 answer_criterion='Give a complete mathematically correct Lean-checked proof of a reduction with some fixed ε > 0 and the stated SIS parameters, overhead and universal oracle guarantee, or a proof that no such choice exists. Improving only the modulus, assuming a solver correct on every SIS matrix, supplying hints with the matrices, or allowing superpolynomial reduction time does not establish this target. The two LWE alternatives in the source are not substitutes for the selected SIS branch.',
 why='Current worst-case guarantees for SIS rely on roughly linear approximation factors when parameters support nontrivial compression. A fixed exponent improvement would base average-case short-integer-solution hardness on a weaker worst-case lattice assumption.',
 source_formulation=dict(text='Open Problem 4.1 gives separate SIS, classical-LWE and quantum-LWE targets. This card selects the classical SIS target with factor O(n^(1−ε)) and fixes a polynomial-modulus compressing family and a black-box average-success convention.',caption='The Complexity of the Shortest Vector Problem, Open Problem 4.1, printed p.13 / PDF p.15.',citation='primary',format='editorial_paraphrase'),
 references=[
 ref('primary','The Complexity of the Shortest Vector Problem','Huck Bennett',2023,'https://www.cs.umd.edu/~gasarch/open/svp-color.pdf','§4.1 polynomial-gap reductions and Open Problem 4.1, printed pp.12–13 / PDF pp.14–15; following discussion distinguishes superpolynomial-time reductions'),
 ref('sis','A Decade of Lattice Cryptography','Chris Peikert',2016,'https://eprint.iacr.org/2015/939','§4.1.1 Definition 4.1.1 and pigeonhole/compression discussion, printed pp.18–19; §4.1.2 Theorem 4.1.2 and parameter improvements, printed pp.20–21'),
 ],
 context_blocks=[
 block('The source reports classical SIS reductions at approximation scale roughly n times polylogarithmic factors for meaningful parameters, and asks for a fixed positive saving in the exponent of n.'),
 block('The SIS modulus, number of columns and solution norm are part of the problem. The chosen family has more input bits than output residues, guarantees a short solution by counting, and excludes the immediate q-multiple solution.','sis'),
 block('The hardness theorem must use an oracle that works on random matrices with noticeable probability. Requiring correctness on every matrix would replace the requested worst-case-to-average-case connection by a different claim.','sis'),
 block('The known refinements improve modulus requirements and related parameters. The selected target instead lowers the approximation factor of the worst-case input by a fixed power of its rank.','sis'),
 block('The survey also discusses reductions using superpolynomial time. Such results can improve tradeoffs but do not meet the polynomial overhead required here.'),
 ],
 progress=[progress('2004–2013','Successive worst-case-to-SIS reductions improve approximation and modulus parameters; the survey summarizes roughly linear approximation for compressing SIS choices.','sis'),progress('2023','Open Problem 4.1 explicitly asks for a fixed exponent improvement below the classical SIS approximation scale.')],
),[
 'Selected the classical SIS branch after an unanswered optional SIS/LWE question and announced it as an editorial default rather than user confirmation.',
 'Specified a polynomially generated polynomial modulus, compressing number of columns and a nontrivial Euclidean solution bound guaranteeing totality.',
 'Defined every worst-case input and the rank-dependent approximation factor with a fixed positive exponent improvement.',
 'Made average success, fresh stateless oracle randomness, arbitrary bad input sets and polynomial inverse-success overhead explicit.',
 'Retained the importance assessment and required a complete Lean-checked reduction or negation in this model.',
],[
 'Read Bennett §4.1 including the SIS/LWE alternatives of Open Problem 4.1 and its following superpolynomial-time qualifications.',
 'Read Peikert §4.1 Definition 4.1.1, the nontriviality and pigeonhole requirements, Theorem 4.1.2, and its parameter-improvement discussion.',
 'Bounded searches through 17 September 2026 did not locate a polynomial-time sublinear-factor worst-case reduction for this ordinary SIS target; results with auxiliary hints and superpolynomial running time do not match its interface.',
], 'Source-open in the classical SIS branch of Bennett’s Open Problem 4.1. This card fixes a compressing polynomial-modulus SIS family and the black-box inverse-success overhead that the source leaves implicit. The SIS branch was an announced editorial default after an unanswered optional question. The reviewed parameter refinements and superpolynomial-time or hinted variants do not settle the target; later-work checks through 17 September 2026 were bounded.',summary=[
 'A random SIS instance is a matrix modulo a polynomial-size integer, and the goal is a short nonzero integer vector in its modular kernel.',
 'The question asks for a classical reduction from every Euclidean GapSVP instance with approximation factor O(n^(1−ε)) for some fixed ε > 0.',
 'The chosen matrix dimensions ensure that a solution exists while excluding the trivial modulus-sized vector.',
 'The reduction must work even when its SIS oracle succeeds only on an inverse-polynomial fraction of uniformly random matrices.',
 'Polynomial overhead includes the inverse success probability, and a complete Lean-checked reduction or impossibility proof is required.',
],expected_sha256=claim['input_sha256'],claim_token=claim['token'])
