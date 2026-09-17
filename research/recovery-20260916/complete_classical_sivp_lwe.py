"""Specify the same-dimension classical SIVP-to-LWE target."""
import sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT/'research/card-completion-20260913'))
from complete_review import complete,ref,block,progress
from review_queue import read_claims
identifier='TCS-6861';claim=read_claims(ROOT)[identifier]
complete(identifier,dict(
 title='A classical same-dimension reduction from SIVP to polynomial-modulus LWE',
 status='source_open',criterion='reductions',question_type='yes_no',
 formal=r'''For every fixed integer \(c\ge3\), do there exist constants \(C,K,a>0\), an integer \(b\ge0\), and one uniform classical randomized oracle algorithm \(\mathcal R_c\) with the following property?

For all \(n\ge2\), all admissible parameters \(q,\alpha,m,t\) below, every rank-\(n\) integer lattice basis \(B\), and every admissible search-LWE oracle \(A\), the algorithm \(\mathcal R_c^A(B,q,\alpha,m,t)\) outputs \(n\) linearly independent lattice vectors of length at most
\[
\gamma(n,\alpha)\lambda_n(\mathcal L(B)),\qquad
\gamma(n,\alpha)=C\frac n\alpha\bigl(\log_2(n+2)\bigr)^b,
\]
with probability at least \(2/3\) on each input basis, using at most \(K(L+m+t+1)^a\) bit operations and oracle calls on every run? Every LWE query must have dimension exactly \(n\), modulus exactly \(q\), and exactly \(m\) samples with the noise parameter \(\alpha\) in the oracle guarantee. Here \(L\) is the complete binary input length, and the constants and algorithm may depend on \(c\), not on the instance.''',
 definitions=r'''Let \(B\in\mathbb Z^{h\times n}\) have full column rank, where \(h\ge n\). The lattice is \(\mathcal L(B)=\{Bz:z\in\mathbb Z^n\}\), endowed with \(\|v\|_2=(\sum_i v_i^2)^{1/2}\). Its last successive minimum \(\lambda_n\) is the least radius of a closed Euclidean ball about zero containing \(n\) linearly independent lattice vectors. The output is a tuple of nonzero integer coefficient vectors \(z_1,\ldots,z_n\) such that \(Bz_1,\ldots,Bz_n\) are linearly independent over \(\mathbb R\) and each meets the stated length bound. They need not form a basis of the entire lattice. This is the shortest independent vectors problem (SIVP), not a shortest-vector decision problem.

The matrix entries, dimensions and all rational and integer parameters are explicitly encoded in binary with delimiters. Admissible parameters have prime \(q\le(n+2)^c\), integers \(1\le m\le(n+2)^c\) and \(2\le t\le(n+2)^c\), and a positive rational \(\alpha=u/v\le1/2\) in lowest terms with \(u,v\le(n+2)^c\), satisfying \(\alpha q>2\sqrt n\). Thus both the modulus and inverse noise rate are polynomially bounded for fixed \(c\).

Define an integer noise variable by drawing a real random variable \(E\) with density
\[
\frac{1}{\alpha q}\exp\left(-\frac{\pi x^2}{(\alpha q)^2}\right),
\]
rounding it to the nearest integer, and reducing modulo \(q\). Denote its exact distribution on \(\mathbb Z_q\) by \(\chi_{q,\alpha}\). Ties have probability zero. This is the rounded Gaussian convention from the original LWE reduction, not an assertion that rounding gives the exact discrete Gaussian on the integers.

A search-LWE test instance is sampled by first choosing a uniformly random secret \(s\in\mathbb Z_q^n\). Independently choose \(m\) uniform vectors \(a_i\in\mathbb Z_q^n\) and \(m\) errors \(e_i\leftarrow\chi_{q,\alpha}\), and give the ordered list
\[
(a_i,\langle a_i,s\rangle+e_i\bmod q)_{i=1}^m
\]
to the oracle. The oracle is any fixed randomized map from such lists to \(\mathbb Z_q^n\cup\{\bot\}\), using fresh independent randomness on each invocation, which outputs the actual sampled \(s\) with probability at least \(1/t\), averaged over the uniformly random secret, all samples and its randomness. There is no per-list guarantee; on other lists it may behave arbitrarily. The reduction must work for every such map, with no access to the secret or the oracle's internal random bits. It may make arbitrary adaptive list queries; their correctness is controlled only by this distributional guarantee.

The reduction is a classical probabilistic multitape Turing machine using independent fair random bits. Its cost includes preparing and writing every finite query, reading the returned vector, processing its input and producing its output, but excludes computation inside the oracle. The exact Gaussian distribution defines the oracle promise. The reduction must implement any sampling or numerical approximation it needs in finite bit time, with its errors included in the final failure probability; it receives no exact-real or Gaussian-sampling primitive. It has no quantum computation, advice or other oracles. The all-run polynomial bound and per-basis success guarantee hold even when the admissible oracle gives adversarial replies away from its average-case guarantee.''',
 answer_criterion='Give a complete mathematically correct Lean-checked construction and proof of the stated classical reduction for every fixed c, or prove the logical negation of this quantified statement. A positive solution must include the same-dimension query interface, noise convention, approximation factor, average-to-worst-case success analysis and finite-bit running time. A quantum reduction, a classical reduction only from GapSVP, an exponential modulus, or a polynomial-modulus reduction that enlarges the LWE dimension does not settle this target.',
 importance=dict(score=91,method='editorial',reason='A same-dimension classical SIVP-to-LWE reduction would remove a central quantum step in the worst-case foundations of lattice cryptography while retaining the approximation and parameter scales that make the connection useful.'),
 why='LWE is a classical noisy linear problem, yet the strongest known worst-case connection to SIVP uses quantum computation. Matching that connection classically at polynomial modulus and unchanged dimension would clarify which parts of the hardness foundation actually depend on quantum operations.',
 source_formulation=dict(text='Question 1 asks whether a classical worst-case hardness reduction fully subsumes the quantum LWE reduction. This card selects its SIVP branch with polynomial modulus and unchanged dimension. The rounded Gaussian, finite sample interface and polynomial parameter bounds make that selected branch precise.',caption='Peikert, A Decade of Lattice Cryptography, §7.1 Question 1, printed p.74 / PDF p.76.',citation='primary',format='editorial_paraphrase'),
 references=[
 ref('primary','A Decade of Lattice Cryptography','Chris Peikert',2016,'https://eprint.iacr.org/2015/939','§4.2.1 Definitions 4.2.1–4.2.3 and footnote 4, printed p.22; §7.1 Question 1, printed p.74 / PDF p.76'),
 ref('quantum','On Lattices, Learning with Errors, Random Linear Codes, and Cryptography','Oded Regev',2009,'https://cims.nyu.edu/~regev/papers/qcrypto.pdf','Author version dated 2 May 2009; Theorem 1.1 p.2; Gaussian discretization Eq.(8) p.15; Theorem 3.1 p.18; Lemma 3.17 p.29'),
 ref('classical','Classical Hardness of Learning with Errors','Zvika Brakerski; Adeline Langlois; Chris Peikert; Oded Regev; Damien Stehlé',2013,'https://arxiv.org/abs/1306.0281v1','STOC 2013 full version; informal Theorem 1.1 p.2, modulus-reduction discussion p.3, Open questions pp.4–5'),
 ],
 context_blocks=[
 block('The source explicitly separates the quantum SIVP and GapSVP guarantees from the classical GapSVP-only connection and its modulus–dimension tradeoff. Retaining the SIVP branch avoids conflating those different conclusions.'),
 block('Regev’s quantum reduction iterates a lattice Gaussian-sampling procedure and then extracts sufficiently many short independent vectors. The resulting approximation factor is Õ(n/α) while the LWE dimension remains n.','quantum'),
 block('The 2013 classical modulus reduction reaches polynomial-modulus LWE but increases the dimension. Its informal theorem relates an n-dimensional LWE solver to a worst-case lattice problem in dimension approximately √n; the open-question discussion also explicitly identifies the missing SIVP connection.','classical'),
 block('Polynomial modulus alone is therefore not the target. The card simultaneously preserves the rank, the SIVP output and the quantum theorem’s approximation scale, with constants allowed to depend on the fixed polynomial parameter range.'),
 block('The prime-modulus and at-most-one-half noise restrictions are stated editorial specializations. The source asks a still broader question that also includes GapSVP and other modulus regimes; solving this card need not settle every branch of that larger request.'),
 ],
 progress=[progress('2009','The checked journal-era author version gives the quantum LWE connection and its SIVP consequence.','quantum'),progress('2013','The classical polynomial-modulus result retains a dimension loss and a GapSVP-based starting point; its open questions call out both limitations.','classical'),progress('2016','Question 1 asks for a classical reduction fully matching the quantum guarantees.')],
),[
 'Selected the recommended same-dimension SIVP and polynomial-modulus branch after an unanswered optional question and an explicit default announcement.',
 'Specified successive minima, independent-vector output and the approximation bound rather than treating SIVP as a basis-reduction or decision problem.',
 'Defined prime modulus, rational noise, rounded Gaussian errors, sample count and an average-case oracle success guarantee.',
 'Made the classical bit model, parameter quantifiers, arbitrary off-distribution behavior and uniform per-input success explicit.',
 'Assessed importance and required a full Lean-checked reduction or negation, while retaining the broader source’s scope in context.',
],[
 'Read Peikert’s LWE definitions and Gaussian footnote, together with the full Question 1 discussion.',
 'Read the saved 2 May 2009 Regev author version’s Theorem 1.1, Gaussian discretization, Theorem 3.1 and Lemma 3.17; identified the actual version rather than inferring its date from the local filename.',
 'Read the Brakerski–Langlois–Peikert–Regev–Stehlé full version’s main theorem, modulus tradeoff and Open questions pp.4–5.',
 'Bounded primary-source searches through 17 September 2026 found no matching classical same-dimension SIVP reduction in this polynomial parameter regime.',
], 'The selected SIVP branch remains unresolved in the checked sources through 17 September 2026. It was an announced recommended editorial default after no reply to an optional question. The 2013 polynomial-modulus classical result does not preserve both the dimension and SIVP starting problem. The finite oracle interface and prime-modulus parameter range are explicit specifications, not a claim to reproduce every part of the broader original request.',summary=[
 'LWE hides a uniformly random modular vector behind noisy linear equations.',
 'The card asks for a classical reduction from worst-case short independent lattice vectors to polynomial-modulus LWE in the same dimension.',
 'The target approximation factor is n/α times a fixed power of a logarithm, with precise rounded Gaussian errors.',
 'Known quantum reductions achieve the relevant connection, while the reviewed classical route loses dimension and starts from a different lattice problem.',
 'A complete Lean-checked answer must settle the explicitly quantified reduction and its average-case oracle guarantees.',
],expected_sha256=claim['input_sha256'],claim_token=claim['token'])
