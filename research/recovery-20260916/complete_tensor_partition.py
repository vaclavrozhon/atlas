"""Complete the selected tensor-product perturbation partition-function target."""
import json,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT/'research/card-completion-20260913'))
from complete_review import complete,ref,block,progress,DATE
from review_queue import read_claims
identifier='TCS-2707'; claim=read_claims(ROOT)[identifier]
notes=[
 'Applied the user-selected tensor product H-prime with operator norm at most one; it is inside the exponential and is not a sum of one-site fields.',
 'Retained the source bounded-locality, bounded-occurrence Hamiltonian setting, with explicit rational complex matrices and deterministic classical bit complexity.',
 'Specified a fixed zero-free disk of radius R greater than one and evaluation at beta=1; the disk promise is only for the full instance, not every subsystem.',
 'Bounded every local interaction norm by a fixed constant J and allowed an arbitrary fixed R>1, so the radius and strength do not grow silently with the input or enter an unspecified running-time exponent.',
 'Required relative-error approximation for every rational epsilon in (0,1), in time polynomial in encoded input length and 1/epsilon; the question is existence of this scheme, not numerical determination of one partition value.',
 'Distinguished the proved tensorized measurement Tr(exp(-beta H)O) theorem from the additive perturbation Tr(exp(-beta H+H-prime)); no commutation or high-temperature hypothesis is added.',
 'Assessed importance at 79 and required a complete Lean-checked proof or refutation of this precise algorithmic statement.',
]
sources=[
 'Read Yao–Yin–Zhang, ICALP 2022 Article 108, DOI 10.4230/LIPIcs.ICALP.2022.108: Definition 1 and Theorem 2 pp. 108:2–108:3, Theorems 14–15 pp. 108:8–108:9, and §3.4 Equation (8) and the complete tensor-product counterexample on p. 108:13. The open expression has H-prime inside the exponential; the proved measured partition function has a tensorized operator outside it.',
 'Checked the primary publisher abstract and publication information for Mann–Minko, Algorithmic Cluster Expansions for Quantum Problems, PRX Quantum 5, 010305, 16 January 2024, DOI 10.1103/PRXQuantum.5.010305. Its stated applications concern high-temperature local quantum spin systems and thermal expectation values; the abstract does not claim this arbitrary zero-free tensor-perturbation extension. The full cluster-expansion proof was not reverified.',
 f'Bounded later-work searches through {DATE} for the source title, non-multiplicative partition functions and zero-free quantum algorithms found no matching resolution of the selected target. Search coverage and the primary abstract check do not certify exhaustive current openness.',
]
complete(identifier,dict(
 title='Zero-free quantum partition functions with a tensor-product perturbation',criterion='resources',question_type='yes_no',year=2022,is_new=False,
 formal=r'''For every fixed integers \(q\ge2\), \(k,d\ge1\), positive rational \(J\), and rational \(R>1\), does there exist a deterministic classical algorithm with the following guarantee? Its input specifies a bounded-occurrence local Hamiltonian \(H=\sum_{j=1}^m h_j\) on \(n\ge1\) sites of dimension \(q\), a tensor-product Hermitian perturbation
\[
 H'=A_1\otimes\cdots\otimes A_n,\qquad \|H'\|\le1,
\]
and a rational accuracy \(0<\varepsilon<1\). Each \(h_j\) acts on at most \(k\) sites, has operator norm at most \(J\), and each site occurs in at most \(d\) terms. Under the promise
\[
 Z(z):=\operatorname{Tr}\exp(-zH+H')\ne0
 \quad\text{for every }z\in\mathbb C\text{ with }|z|<R,
\]
the algorithm must output a rational \(\widehat Z\) satisfying
\[
 |\widehat Z-Z(1)|\le\varepsilon Z(1)
\]
in time polynomial in the binary input length and \(1/\varepsilon\). The polynomial may depend on the fixed parameters \(q,k,d,J,R\), but not on the instance or its accuracy.''',
 definitions=r'''The Hilbert space is \((\mathbb C^q)^{\otimes n}\), with the standard tensor-product basis. A matrix is Hermitian when it equals its conjugate transpose. Its operator norm is \(\|B\|=\sup_{\|v\|_2=1}\|Bv\|_2\). The trace is the sum of diagonal entries, and the matrix exponential is the convergent series \(\exp(B)=\sum_{r=0}^{\infty}B^r/r!\). Thus the value \(Z(1)\) is a strictly positive real number, although \(Z(z)\) is generally complex for nonreal \(z\).

For each interaction the input lists a nonempty set \(S_j\subseteq\{1,\ldots,n\}\) of at most \(k\) sites, in increasing order, and the full \(q^{|S_j|}\)-by-\(q^{|S_j|}\) matrix of \(h_j\) on those sites. It is extended by the identity on all other sites. Each site belongs to at most \(d\) of the listed supports; duplicate terms count separately. The empty list of terms is allowed, giving \(H=0\). An interaction is allowed to be the identity on some of its listed sites; this does not reduce the declared occurrence count.

Each \(A_i\) is supplied as a full Hermitian \(q\)-by-\(q\) matrix. The real and imaginary parts of every matrix entry are rational numbers, encoded by signed binary numerators and positive binary denominators. All matrices are given explicitly on their listed local spaces; neither a succinct circuit for a full exponentially large matrix nor a matrix-entry oracle is used. The total input length \(L\) includes these entries, supports, \(n\), and the rational \(\varepsilon\). The bounds on Hermiticity, interaction norms, occurrence and \(\|H'\|\) are promises on the input.

The norm condition concerns the full tensor product. The individual factors need not each have norm at most one. The term \(H'\) may act on every site and is represented only by its supplied one-site factors. It is not an additional bounded-locality term, not a sum \(\sum_i A_i\), and not an operator multiplied outside the exponential. No commutation between the \(h_j\), between different interactions, or between \(H\) and \(H'\) is assumed.

The zero-free disk has a fixed positive margin around the target point \(1\): its radius \(R>1\) is fixed before choosing an input. Its promise ranges over every complex point of the disk, not merely real temperatures. No proof of zero-freeness, exact partition value at zero, Taylor coefficients or auxiliary evaluation oracle is supplied. In particular, the algorithm must obtain all numerical information from the explicit local input. Zero-freeness is promised only for \(Z\) of the full input; it is not separately required after deleting sites or interactions. A result based on a stronger high-temperature condition does not by itself cover this entire promise class.

Polynomial time means that for every fixed \(q,k,d,J,R\) there exist an algorithm and constants \(C,a\ge1\) whose running time is at most \(C(L+\lceil1/\varepsilon\rceil+1)^a\) elementary steps of a deterministic multitape Turing machine. The bound includes finite-precision arithmetic and writing the rational output. The machine must terminate within its polynomial clock even on encodings outside the promises, but its approximation guarantee is required only on promised inputs. No efficient uniform dependence on the fixed parameters, in particular as \(R\) tends to one, is required. This fixes a precise disk version of the source’s broader question about zero-free regions.''',
 answer_criterion=r'''Give a complete Lean-checked proof that the stated approximation scheme exists for every fixed parameter tuple, including the promised input class, relative error and classical bit-time bound, or a complete Lean-checked refutation. An algorithm for a single fixed accuracy, a quasi-polynomial-time algorithm, or a quantum algorithm alone does not establish the target.

A negative answer must refute this existence statement for at least one fixed parameter tuple. Conditional hardness may document progress, but without the needed hardness assumption it is not an unconditional refutation. A lower bound for unrestricted global perturbations, an input oracle model, or instances whose zero-free margin shrinks with input size does not refute this card. The benchmark’s numerical absolute-error convention does not replace the relative-error guarantee of the algorithmic proposition.''',
 source_formulation=dict(text='Section 3.4 asks for polynomial-time approximation of Tr exp(-beta H+H-prime) from zero-freeness. It shows that the multiplicative framework of the paper fails even when H-prime is a tensor product of one-site operators. The user selected this tensor-product case with operator norm at most one; the card fixes a zero-free disk, a bounded local input model and relative-error bit complexity.',caption='Paraphrase of Yao–Yin–Zhang, ICALP 2022 §3.4, Equation (8), p. 108:13; tensor-product norm bound selected on 17 September 2026.',citation='primary',format='editorial_paraphrase'),
 importance=dict(score=79,method='editorial',reason='This asks whether analytic absence of zeros still yields efficient deterministic approximation when a structured global perturbation breaks the multiplicativity used by existing counting methods. It isolates a barrier beyond ordinary noncommuting local Hamiltonians.',basis='Individual assessment of the source’s explicit barrier and the user-selected tensor-product specialization; it is not a claim that all quantum partition functions share this complexity.'),
 why='Zero-free complex regions often turn a difficult counting problem into an efficient approximation problem. A tensor-product perturbation has a short description but disrupts the factorization behind the known algorithm, testing whether zero-freeness alone remains sufficient.',
 references=[
 ref('primary','Polynomial-Time Approximation of Zero-Free Partition Functions','Penghui Yao; Yitong Yin; Xinyuan Zhang',2022,'https://doi.org/10.4230/LIPIcs.ICALP.2022.108','ICALP 2022, LIPIcs 229, Article 108; Definition 1 and Theorem 2 pp. 108:2–108:3; Theorems 14–15 pp. 108:8–108:9; §3.4 Equation (8) and the open question p. 108:13'),
 ref('cluster','Algorithmic Cluster Expansions for Quantum Problems','Ryan L. Mann; Romy M. Minko',2024,'https://doi.org/10.1103/PRXQuantum.5.010305','PRX Quantum 5, 010305, published 16 January 2024; publisher abstract, specifically the high-temperature partition-function and thermal-expectation applications'),
 ],
 context_blocks=[
 block('The source proves a deterministic approximation theorem for bounded-occurrence local quantum Hamiltonians, also allowing a tensorized measurement outside the exponential. The selected additive perturbation lies inside the exponential and is explicitly identified as beyond that theorem.'),
 block('The source’s two-site example shows failure of the relevant factorization even for diagonal matrices. This is a barrier to the given framework, not a hardness proof and not evidence that commutation alone resolves the selected target.'),
 block('The 2024 cluster-expansion paper gives algorithms for specified high-temperature systems and thermal expectations. Its checked abstract does not assert an algorithm for every tensor-product perturbation satisfying only the disk promise here.','cluster'),
 ],
 progress=[progress('2022','ICALP publishes the zero-free approximation theorem and the separate open question for additive perturbations inside the exponential.'),progress('2024-01-16','A cluster-expansion framework provides further high-temperature quantum approximation results; its stated scope differs from the selected promise class.','cluster')],
),notes,sources,'The primary source explicitly leaves the additive-perturbation extension open. Its proved tensorized-measurement theorem and the checked 2024 high-temperature cluster-expansion abstract do not settle the selected tensor-product, bounded-norm disk formulation. Bounded later-work checks through 17 September 2026 found no matching resolution; this is not an exhaustive certification of current openness.',summary=[
 'The input describes local quantum interactions together with one global tensor product of one-site operators.',
 'The task is to approximate the trace of the exponential after adding that product inside the exponent.',
 'The only analytic promise is that this partition function has no zeros in a fixed complex disk extending beyond the target temperature.',
 'The requested deterministic classical algorithm must achieve every relative accuracy in polynomial bit time for fixed local parameters.',
 'The known theorem treats a different position of the tensorized operator, and a complete Lean-checked proof or refutation of this extension is required.',
],expected_sha256=claim['input_sha256'],claim_token=claim['token'])
p=ROOT/'research/recovery-20260916/further-scope-choices.json';a=json.loads(p.read_text());next(r for r in a if r['id']==identifier).update(state='applied',applied_on=DATE);p.write_text(json.dumps(a,ensure_ascii=False,indent=2)+'\n')
