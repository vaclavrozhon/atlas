"""Specify a finite-input classical ideal-SVP to ring-LWE reduction."""
import sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT/'research/card-completion-20260913'))
from complete_review import complete,ref,block,progress
from review_queue import read_claims
identifier='TCS-6864';claim=read_claims(ROOT)[identifier]
complete(identifier,dict(
 title='Classical ideal-SVP hardness of ring-LWE in power-of-two cyclotomic rings',
 status='source_open',criterion='reductions',question_type='yes_no',
 formal=r'''For every fixed integer \(c\ge3\), do there exist constants \(C,K,a>0\), integers \(b\ge0,n_0\ge2\), and one uniform classical randomized oracle algorithm that, for every power of two \(n\ge n_0\), reduces worst-case ideal-SVP in \(R_n=\mathbb Z[X]/(X^n+1)\) to the same-ring search-LWE problem defined below, with approximation factor
\[
\gamma(n,\alpha)=C\frac{\sqrt n}{\alpha}\bigl(\log_2(n+2)\bigr)^b?
\]
The reduction must succeed with probability at least \(2/3\) on every input ideal basis, for every admissible oracle, and use at most \(K(L+m+t+1)^a\) classical bit operations and oracle calls on every run. Its queries must retain the degree \(n\), modulus \(q\), noise-family bound \(\alpha\) and sample count \(m\). The constants and algorithm may depend on \(c\), but not on the ideal or the other parameters.''',
 definitions=r'''Put \(K_n=\mathbb Q[X]/(X^n+1)\). Since \(n\) is a power of two, this is a number field with ring of integers \(R_n\). A nonzero integral ideal \(I\subseteq R_n\) is given by a full-rank integer matrix \(B\in\mathbb Z^{n\times n}\): its columns are the power-basis coefficient vectors of a \(\mathbb Z\)-basis of \(I\). The input is promised to generate a set closed under multiplication by \(X\), hence by every element of \(R_n\). All entries, dimensions and parameters are encoded explicitly in binary with delimiters; \(L\) is their total length.

Let \(\sigma_j\) be the embeddings sending \(X\) to the roots of \(X^n+1\). Use the canonical Euclidean norm
\[
\|v\|_{\rm can}^2=\sum_{j=1}^n|\sigma_j(v)|^2,
\qquad \lambda_1(I)=\min_{v\in I\setminus\{0\}}\|v\|_{\rm can}.
\]
The required output is a nonzero integer vector \(z\) such that the ideal element with coefficient vector \(Bz\) has norm at most \(\gamma(n,\alpha)\lambda_1(I)\). A short vector must actually be produced; deciding whether one exists is not the task. In this ring the canonical norm is \(\sqrt n\) times the coefficient Euclidean norm. Also, multiplying a shortest nonzero element by \(1,X,\ldots,X^{n-1}\) gives independent vectors of the same length, so the first and last successive minima of an ideal agree.

Admissible parameters have a prime \(q\le(n+2)^c\), integers \(1\le m\le(n+2)^c\), \(2\le t\le(n+2)^c\), and a rational \(\alpha=u/v\in(0,1/2]\), in lowest terms with \(u,v\le(n+2)^c\), satisfying \(\alpha q\ge(\log_2(n+2))^2\). Let \(R_{n,q}=R_n/qR_n\); its elements are encoded by \(n\) coefficients in \(\{0,\ldots,q-1\}\).

Here is the exact finite-output family of error distributions. Extend the power-basis coefficient space to \(K_{n,\mathbb R}=\mathbb R[X]/(X^n+1)\). Choose one embedding from each complex-conjugate pair and define the real isometry
\[
\tau(v)=\bigl(\sqrt2\operatorname{Re}\sigma_j(v),\sqrt2\operatorname{Im}\sigma_j(v)\bigr)_{j=1}^{n/2}\in\mathbb R^n.
\]
For any vector \(\rho=(\rho_1,\ldots,\rho_{n/2})\) with \(0<\rho_j\le\alpha\), sample independently two real Gaussian coordinates for pair \(j\), each of density \(\rho_j^{-1}\exp(-\pi x^2/\rho_j^2)\). Let \(e\in K_{n,\mathbb R}\) be their inverse image under \(\tau\). Expand \(nq e\) in the power basis, round each real coefficient to its nearest integer and reduce modulo \(q\). The resulting element of \(R_{n,q}\) has distribution \(\chi_\rho\). Ties occur with probability zero. The factor \(n\) is intentional: it converts rounding in the dual ring \(R_n^\vee=n^{-1}R_n\) to this ordinary-ring representation.

An admissible oracle \(A\) is a fixed randomized map from ordered lists of \(m\) pairs in \(R_{n,q}^2\) to \(R_{n,q}\cup\{\bot\}\). For every fixed \(\rho\) in the family, choose a uniformly random secret \(s\in R_{n,q}\), independently sample uniform \(a_1,\ldots,a_m\in R_{n,q}\) and errors \(\eta_i\leftarrow\chi_\rho\), and form
\[
(a_i,a_i s+\eta_i)_{i=1}^m.
\]
On this input the oracle must output the sampled \(s\) with probability at least \(1/t\), averaged over the secret, samples and oracle randomness. The same oracle must satisfy this for every \(\rho\); neither the secret nor \(\rho\) is given as side information. It has fresh independent randomness on every invocation. Away from these distributional guarantees its answers are arbitrary. The reduction may make adaptive finite-list queries and must work for every such oracle.

Computation uses a classical probabilistic multitape Turing machine with fair independent random bits. Query construction, input reading, oracle-answer reading, all numerical approximations and output writing are charged; only the oracle's internal computation is excluded. Exact real Gaussians define probability distributions, not computational primitives available to the reduction. Its implementation must use finite arithmetic and include sampling errors in its total failure probability. There are no quantum operations, advice or additional oracles. This is a family-of-noises search target, not the stronger fixed spherical-noise or decision target.''',
 answer_criterion='Give a complete mathematically correct Lean-checked classical reduction with the stated approximation factor, finite sample distributions, same-degree queries, bit cost and per-ideal success guarantee, or prove the logical negation of the quantified claim. A quantum worst-case reduction, a classical search-to-decision reduction, a decision GapSVP starting point, or a generic-to-ideal reduction whose number field varies with the input does not settle this target.',
 importance=dict(score=89,method='editorial',reason='A classical worst-case connection for cyclotomic ring-LWE would address a foundational gap for structured lattice cryptography; the search ideal-lattice starting point avoids an easy decision surrogate.'),
 why='Ring structure makes LWE-based constructions more compact, but the useful worst-case ideal-lattice connection uses quantum computation. A classical reduction at comparable approximation and modulus scales would strengthen the theoretical understanding of that connection.',
 source_formulation=dict(text='Question 4 asks for a meaningful classical worst-case hardness reduction for ring-LWE and explains why the ordinary GapSVP starting point is insufficient on ideal lattices. This card selects approximate search-SVP in power-of-two cyclotomic rings and the elliptical error family of the known quantum reduction, with explicit finite rounding.',caption='Peikert, A Decade of Lattice Cryptography, §7.1 Question 4, printed p.75 / PDF p.77.',citation='primary',format='editorial_paraphrase'),
 references=[
 ref('primary','A Decade of Lattice Cryptography','Chris Peikert',2016,'https://eprint.iacr.org/2015/939','§7.1 Question 4 and preceding explanation, printed p.75 / PDF p.77'),
 ref('quantum','On Ideal Lattices and Learning with Errors Over Rings','Vadim Lyubashevsky; Chris Peikert; Oded Regev',2012,'https://cims.nyu.edu/~regev/papers/ideal-lwe.pdf','Author version dated 24 April 2012; §2.2.1 p.10; Definitions 3.1–3.4 pp.18–19; power-of-two dual scaling p.19; rounding paragraph p.20; Theorem 4.1 and following SVP/SIVP consequence pp.21–22'),
 ref('classical','Classical Hardness of Learning with Errors','Zvika Brakerski; Adeline Langlois; Chris Peikert; Oded Regev; Damien Stehlé',2013,'https://arxiv.org/abs/1306.0281v1','Open questions pp.4–5: the classical GapSVP starting point and its insufficiency for ideal lattices'),
 ref('variable','NP-hardness of ideal lattice problems','Daniel E. Martin',2026,'https://arxiv.org/abs/2609.15813v1','Submitted 14 September; manuscript dated 15 September 2026; abstract and Theorem 1.1 / Remark 1.2; variable totally real fields and monogenic orders'),
 ],
 context_blocks=[
 block('The source calls the classical reduction question meaningful only when its worst-case premise carries useful ideal-lattice hardness. It explicitly notes that the decision GapSVP problem is easy at the relevant polynomial factors.'),
 block('The quantum theorem first reduces an ideal Gaussian-sampling problem to search ring-LWE for an entire family of elliptical errors. It yields an Õ(√n/α) factor for independent vectors, and hence also short vectors in cyclotomic ideals.','quantum'),
 block('The power-of-two dual ring is exactly n⁻¹R. Scaling its secrets to R and rounding the noise in a dual basis explains the n in this card’s finite sample definition. Treating the ordinary coefficient Gaussian as though it had the same canonical parameter would change the problem.','quantum'),
 block('The known search theorem requires a solver for every bounded elliptical shape. A fixed spherical error distribution is a distinct stronger hardness target; classical search-to-decision conversions do not remove the quantum worst-case step.','quantum'),
 block('The September 2026 generic-to-ideal preprint changes the ambient number field with the input and allows monogenic orders. Its abstract qualifies the full-ring-of-integers extension. It does not establish a classical reduction to ring-LWE in the fixed cyclotomic family used here.','variable'),
 ],
 progress=[progress('2012','The checked author version proves the quantum ideal-lattice reduction and explicitly describes finite coefficient rounding.','quantum'),progress('2013','The classical LWE paper explains why its GapSVP route does not supply the analogous useful ideal-lattice result.','classical'),progress('2016','Question 4 asks for a meaningful classical worst-case reduction.'),progress('2026-09','A variable-field ideal-lattice hardness preprint addresses a different connection; its scope does not resolve this fixed cyclotomic ring-LWE target.','variable')],
),[
 'Applied the announced recommended power-of-two cyclotomic editorial default after an unanswered optional field-scope question.',
 'Selected search ideal-SVP and the Õ(√n/α) quantum scale, with the same degree and polynomial modulus.',
 'Defined ideal input, canonical norm, complex-pair Gaussian coordinates and the dual-to-ordinary-ring rounding factor.',
 'Retained the full bounded elliptical error family and an average-case finite-list oracle rather than silently strengthening to fixed spherical error.',
 'Assessed importance, checked the distinct September 2026 variable-field result and supplied the full Lean-checked criterion.',
],[
 'Read the full Question 4 paragraph and its GapSVP qualification in Peikert’s survey.',
 'Read the actual 24 April 2012 Lyubashevsky–Peikert–Regev author version’s Gaussian conventions, ring-LWE definitions, dual scaling, rounding paragraph, Theorem 4.1 and following approximation consequence.',
 'Read the classical LWE paper’s open-question discussion and the September 2026 ideal-lattice preprint’s abstract and field/order qualifications.',
 'Bounded primary-source searches through 17 September 2026 found no classical reduction matching the selected cyclotomic search target.',
], 'The selected classical worst-case ring-LWE reduction remains open in the checked primary sources through 17 September 2026. The cyclotomic scope was an announced editorial default after an unanswered optional question. The finite rounding and bounded elliptical family preserve the distinctions in the quantum source. The September variable-field ideal-hardness preprint does not give this fixed-ring classical reduction.',summary=[
 'Ring-LWE consists of noisy multiplication samples in a finite polynomial quotient ring.',
 'The card asks for a classical reduction from finding a short vector in every ideal of a power-of-two cyclotomic ring.',
 'The target keeps the degree and polynomial modulus and seeks the known quantum approximation scale Õ(√n/α).',
 'Its oracle must solve the full bounded elliptical error family, with explicit dual-ring scaling and finite coefficient rounding.',
 'The classical connection remains unresolved in the checked sources, and a full Lean-checked reduction or refutation is required.',
],expected_sha256=claim['input_sha256'],claim_token=claim['token'])
