"""Complete the strong accuracy-dependent form of Mansour's conjecture."""
import sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];sys.path.insert(0,str(ROOT/'research/card-completion-20260913'))
from complete_review import complete,ref,block,progress,DATE
from review_queue import read_claims
identifier='TCS-6581';claim=read_claims(ROOT)[identifier]
notes=[
 'Preserved the strong Mansour target with one universal constant and exponent proportional to log(1/epsilon), not merely polynomial sparsity separately for each fixed accuracy.',
 'Made the Boolean sign convention, DNF term count, unrestricted overlap and width, uniform Walsh coefficients and squared-error normalization explicit.',
 'Repaired malformed inherited Fourier notation and kept the target existential rather than adding an algorithm to find the coefficient set.',
 'Checked the source distinction between weak and strong forms, the exact small-read accuracy bound, and the different basis/distribution in the June 2026 learning work.',
 'Preserved importance score 95, removed suggested proof methods and examples functioning as solution hints, and required a complete Lean-checked proof or full quantified refutation.',
]
sources=[
 'Read O’Donnell–Wright–Zhou, The Fourier Entropy–Influence Conjecture for certain classes of Boolean functions, ICALP 2011, §1.1, PDF pp. 2–3. The Mansour paragraph explicitly distinguishes arbitrary K(epsilon), the stronger O(log(1/epsilon)) choice, and the O(1/epsilon) consequence of Fourier entropy–influence.',
 'Read Klivans–Lee–Wan, ECCC TR10-023 revision 3, 4 May 2010, abstract and Introduction pp. 1–2, Theorems 1–2: random formulas and constant read number are subclasses, not all worst-case DNFs. This is the corrected final revision.',
 'Read Lecomte–Tan, arXiv:2109.04525v2 of 15 October 2021, Introduction Theorems 1–2 and §2.1 Fourier definitions. At fixed accuracy the improvement depends on log log of the read number; Theorem 2 explicitly has (s/epsilon)^{O(log(1/epsilon))} for its small-read regime. The epsilon denominator must not be silently dropped.',
 'Read the primary abstract and version history of Heidari–Khardon, arXiv:2506.01075v2, revised 2 June 2026: the representation is adapted to Bayesian-network distributions; it gives DNF learning and agnostic decision-tree learning with membership-query techniques. It does not claim the ordinary uniform Walsh concentration proposition here.',
 'Read the primary abstract and revision metadata of González–MacManus–Pereyra, arXiv:2606.00246v2, revised 9 June 2026: FEI is established for additional classes satisfying structural conditions, not every Boolean function or every DNF with the selected strong accuracy dependence.',
 f'Bounded source checks through {DATE} found no verified resolution of the full strong Mansour proposition; cited proofs were not independently formalized or exhaustively audited.',
]
complete(identifier,dict(
 criterion='tightness',question_type='yes_no',
 formal=r'''Does there exist an absolute real constant \(C>0\) such that, for every integer \(n\ge1\), integer \(s\ge2\), function \(f:\{-1,1\}^n\to\{-1,1\}\) representable by a DNF with at most \(s\) terms, and real \(0<\varepsilon\le1/2\), there is a family \(\mathcal F\subseteq 2^{[n]}\) for which
\[
 |\mathcal F|\le\left\lceil s^{C\log_2(1/\varepsilon)}\right\rceil,
 \qquad
 \sum_{S\subseteq[n],\ S\notin\mathcal F}\widehat f(S)^2\le\varepsilon?
\]
The coefficients are the ordinary Walsh–Fourier coefficients under the uniform distribution. The same constant \(C\) must work for every dimension, term count, formula and accuracy.''',
 definitions=r'''Write \([n]=\{1,\ldots,n\}\) and let \(2^{[n]}\) be its set of subsets. A literal is either the condition \(x_i=1\) or the condition \(x_i=-1\). A term is a conjunction of literals; a disjunctive normal form (DNF) is an OR of terms. Its represented function has value \(+1\) when at least one term is satisfied and \(-1\) otherwise. The number of terms, rather than the total number of literal occurrences, is the size parameter \(s\). Each term may contain any number of variables; variables may occur in arbitrarily many terms, and terms may overlap. Empty conjunctions and an empty disjunction have their usual constant meanings. The statement asks only for existence of some representation with at most \(s\) terms.

For every \(S\subseteq[n]\), define the parity character and its coefficient by
\[
 \chi_S(x)=\prod_{i\in S}x_i,\qquad \chi_{\varnothing}(x)=1,
 \qquad
 \widehat f(S)=2^{-n}\sum_{x\in\{-1,1\}^n}f(x)\chi_S(x).
\]
These characters form an orthonormal basis for real functions on the uniform Boolean cube, with inner product \(\mathbb E[g(X)h(X)]\) for uniform \(X\). In particular,
\[
 f(x)=\sum_{S\subseteq[n]}\widehat f(S)\chi_S(x),
 \qquad \sum_{S\subseteq[n]}\widehat f(S)^2=1.
\]
The empty-set coefficient is included in these sums and may belong to \(\mathcal F\).

Keeping the coefficients indexed by \(\mathcal F\) gives the real multilinear polynomial
\[
 g_{\mathcal F}(x)=\sum_{S\in\mathcal F}\widehat f(S)\chi_S(x),
\]
whose mean squared error is exactly
\[
 \mathbb E[(f(X)-g_{\mathcal F}(X))^2]
   =\sum_{S\notin\mathcal F}\widehat f(S)^2.
\]
Thus \(\varepsilon\) measures discarded squared Fourier mass, without an additional normalization factor. The approximant need not be Boolean-valued. The bound concerns the number of retained characters, not their maximum degree, pointwise error or disagreement probability.

The family \(\mathcal F\) may depend on the function and on \(\varepsilon\). No efficient algorithm for discovering it, producing the coefficients or learning the function is required. There is no promise on a DNF’s read number, which is the maximum number of its terms containing any one variable, and no random distribution on formulas. The only input distribution in the approximation is uniform on \(\{-1,1\}^n\).

This is the strong accuracy-dependent form of the conjecture. Allowing \(s^{K(\varepsilon)}\) characters for an arbitrary function \(K\) of the error would be a weaker target. Here that exponent must be bounded by one constant times \(\log_2(1/\varepsilon)\), uniformly even when \(\varepsilon\) decreases with \(n\) or \(s\).''',
 answer_criterion=r'''Give a complete Lean-checked proof of the displayed statement with one universal \(C\), or a complete Lean-checked proof of its negation.

A negative answer must show that for every \(C>0\) there are admissible \(n,s,\varepsilon,f\) for which every family of at most \(\lceil s^{C\log_2(1/\varepsilon)}\rceil\) characters leaves discarded squared mass greater than \(\varepsilon\). Defeating only one proposed constant does not refute existence of another. A theorem only for random DNFs, bounded-read formulas, fixed width or a different input distribution does not cover the target. A polynomial concentration bound with unspecified dependence of its exponent on \(\varepsilon\) establishes only the weaker form. This is an exact universal proposition; the benchmark’s numerical \(1/100\) tolerance is not a replacement for its full range of error parameters.''',
 source_formulation=dict(text='The 2011 source states polynomial Fourier concentration for DNF formulas and explicitly notes Mansour’s stronger proposed exponent proportional to the logarithm of inverse accuracy. This card preserves that stronger dependence from its existing formulation.',caption='Paraphrase of O’Donnell–Wright–Zhou, ICALP 2011 §1.1, Mansour paragraph on PDF p. 3; compare Klivans–Lee–Wan, ECCC revision 3 of 4 May 2010, Introduction.',citation='primary',format='editorial_paraphrase'),
 references=[
 ref('primary','The Fourier Entropy–Influence Conjecture for certain classes of Boolean functions','Ryan O’Donnell; John Wright; Yuan Zhou',2011,'https://www.cs.cmu.edu/~jswright/papers/fei.pdf','ICALP 2011, pp. 330–341; §1.1, PDF pp. 2–3; the Mansour paragraph distinguishes strong, weak and FEI-implied accuracy dependence'),
 ref('ref2','Mansour’s Conjecture is True for Random DNF Formulas','Adam Klivans; Homin K. Lee; Andrew Wan',2010,'https://eccc.weizmann.ac.il/report/2010/023/revision/3/download/','ECCC TR10-023 revision 3, 4 May 2010; abstract, Introduction pp. 1–2 and Theorems 1–2; corrected constant-read argument'),
 ref('sharper','Sharper bounds on the Fourier concentration of DNFs','Victor Lecomte; Li-Yang Tan',2021,'https://arxiv.org/abs/2109.04525v2','Version 2, 15 October 2021; Introduction Theorems 1–2 and §2.1; explicit dependence on read number and accuracy'),
 ref('recentfei','Further evidence towards the Fourier Entropy-Influence conjecture','María José González; Paul MacManus; María Cristina Pereyra',2026,'https://arxiv.org/abs/2606.00246v2','Version 2, 9 June 2026; primary abstract and revision metadata, further structurally restricted FEI classes'),
 ref('learning','Learning DNF through Generalized Fourier Representations','Mohsen Heidari; Roni Khardon',2026,'https://arxiv.org/abs/2506.01075v2','Version 2, 2 June 2026; primary abstract and revision history; distribution-adapted Bayesian-network representation, DNF learning and separate agnostic decision-tree result'),
 ],
 context_blocks=[
 block('DNF size counts sufficient conditions for acceptance; Fourier sparsity counts parity correlations needed for approximation. The conjecture asks whether a short representation of the first kind always yields an approximately short representation of the second, independently of the ambient dimension.'),
 block(r'The source distinguishes the stronger \(O(\log(1/\varepsilon))\) exponent from a general error-dependent exponent. Its stated FEI implication yields \(O(1/\varepsilon)\), which does not establish the stronger bound selected here.'),
 block('Random-formula and fixed-read-number theorems give important subclasses, but neither hypothesis is part of the universal target.','ref2'),
 block(r'The 2021 work improves dependence on the read number and proves a polynomial fixed-accuracy bound for a growing small-read range. Its full small-read estimate has base \(s/\varepsilon\), which matters when comparing varying accuracies.','sharper'),
 block('The June 2026 FEI preprint concerns additional classes satisfying structural conditions. Its checked abstract does not claim the strong concentration theorem for arbitrary DNFs.','recentfei'),
 block('The June 2026 learning revision changes the Fourier representation to fit Bayesian-network distributions. Learning DNFs in that model and agnostically learning decision trees are different conclusions from uniform Walsh concentration of every DNF.','learning'),
 ],
 progress=[progress('2010-05-04','The corrected ECCC revision establishes concentration for random formulas and fixed read numbers.','ref2'),progress('2011','The source explicitly separates the strong and weak versions of Mansour’s conjecture.'),progress('2021-10-15','The revised DNF analysis sharpens read-number bounds and expands the polynomial fixed-accuracy regime.','sharper'),progress('2026-06-02','A learning paper develops a different distribution-adapted Fourier representation.','learning'),progress('2026-06-09','A revised FEI preprint treats further structured classes.','recentfei')],
),notes,sources,'The checked general DNF bounds and subclass theorems do not establish the universal strong accuracy-dependent concentration bound. The June 2026 works concern restricted FEI classes or a different distribution-adapted learning framework. Bounded primary-source checks through 17 September 2026 found no verified proof or refutation of the retained strong form; the full cited proofs were not independently certified.',summary=[
 'A short DNF describes a Boolean function using a small number of conjunctions.',
 'Mansour’s conjecture asks whether such a function can always be approximated by retaining only a small number of its ordinary Fourier coefficients.',
 'The permitted discarded squared mass is epsilon under uniformly random Boolean inputs.',
 'The retained number must be at most the term count raised to a universal constant times log of inverse epsilon, with no dependence on the ambient dimension.',
 'A complete Lean-checked answer must prove or refute this strong bound for all DNFs and all stated accuracies, without an algorithmic recovery requirement.',
],expected_sha256=claim['input_sha256'],claim_token=claim['token'])
