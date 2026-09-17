"""Individually specify the discrete Zariski-adherence membership question."""
import sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT/'research/card-completion-20260913'))
from complete_review import complete,ref,block,progress
from review_queue import read_claims
identifier='TCS-1069';claim=read_claims(ROOT)[identifier]
complete(identifier,dict(
 title='Does real Zariski-closure membership belong to ∃R?',
 status='source_open',criterion='decision',question_type='yes_no',
 formal=r'''Does the following language belong to \(\exists\mathbb R\)? An input is a quantifier-free Boolean formula \(\varphi\) in real variables \(x_1,\ldots,x_n\), with explicitly encoded integer polynomial equations and inequalities. It is accepted exactly when
\[
0\in\overline{S_\varphi}^{\,Z},\qquad
S_\varphi=\{x\in\mathbb R^n:\varphi(x)\}.
\]
Here \(\overline{S_\varphi}^{\,Z}\) is the real Zariski closure. The target is a deterministic polynomial-bit-time many-one reduction to the existential theory of the reals, for arbitrary input dimension and polynomial degree.''',
 definitions=r'''The input specifies an integer \(n\ge1\) and a finite formula tree built with AND, OR and NOT from atoms \(p(x)=0\) and \(p(x)>0\). Thus weak inequalities and disequalities can also be expressed. Each \(p\in\mathbb Z[x_1,\ldots,x_n]\) is given by a finite list of monomials, each with a signed binary integer coefficient and an exponent vector in \(\mathbb N^n\). Exponents and the declared dimension are written in unary; use an explicit length-delimited encoding for lists and the formula. Repeated monomials are added with their displayed coefficients. Let \(L\) be the complete binary encoding length, including all coefficients, exponents and Boolean connectives. No polynomial is supplied as a succinct arithmetic circuit. There is no fixed bound on dimension, degree, coefficient size or formula size.

For any \(S\subseteq\mathbb R^n\), define
\[
\overline S^{\,Z}=\{z\in\mathbb R^n:
\forall p\in\mathbb R[X_1,\ldots,X_n],
[(\forall x\in S,\ p(x)=0)\Rightarrow p(z)=0]\}.
\]
The universal quantifier in this definition ranges over all finite real-coefficient polynomials, with no degree bound. It is a mathematical definition, not an additional part of the input. The closure is taken in real affine space. In particular the closure of the empty set is empty. The question concerns the origin, whose coordinates need not be supplied.

ETR is the language of true sentences \(\exists y_1\cdots\exists y_m\,\psi(y)\), where \(\psi\) is a finite Boolean formula in integer polynomial equalities and strict inequalities with the explicit encoding just described. A language belongs to \(\exists\mathbb R\) if it has a deterministic polynomial-time many-one reduction to ETR. Accordingly, the requested reduction is one Turing machine and constants \(K,a>0\) which, on every well-formed \(\varphi\) of length \(L\), output such an existential sentence in at most \(K(L+1)^a\) bit operations and satisfy
\[
0\in\overline{S_\varphi}^{\,Z}
\quad\Longleftrightarrow\quad
\mathbb R\models\exists y\,\psi(y).
\]
The time bound includes writing the output; hence its length is polynomially bounded. Ordinary deterministic multitape Turing-machine time is used. Invalid encodings may be rejected directly. This is a finite-bit complexity question, not a unit-cost real-machine bound or an approximate closure test.''',
 answer_criterion='Give a complete mathematically correct Lean-checked proof that the specified language belongs to ∃R, including a uniform reduction, its bit complexity and both directions of its correctness, or a proof that it does not belong to ∃R. Proving hardness alone, giving an unrestricted-time closure algorithm, or resolving the corresponding Euclidean-closure problem does not meet this target.',
 why='This asks whether algebraic consequences of a real feasible region have existential real certificates of polynomial description length. It isolates a concrete boundary in real algebraic complexity that is not determined by the known classification for ordinary metric limits.',
 source_formulation=dict(text='Entry A37 asks for the complexity of the Zariski version of adherence. This card selects the concrete membership-in-∃R target, with finite-bit input and an explicit polynomial representation.',caption='The Existential Theory of the Reals as a Complexity Class: A Compendium, §15 and A37, pp.40 and 49.',citation='primary',format='editorial_paraphrase'),
 references=[
 ref('primary','The Existential Theory of the Reals as a Complexity Class: A Compendium','Marcus Schaefer; Jean Cardinal; Tillmann Miltzow',2024,'https://arxiv.org/abs/2407.18006v1','§15 explicit polynomial convention p.40; A37 p.49, including the open Zariski-topology question'),
 ref('hardness','Exotic quantifiers, complexity classes, and complete problems','Peter Bürgisser; Felipe Cucker',2005,'https://eccc.weizmann.ac.il/report/2005/138/','ECCC TR05-138 preprint; semialgebraic descriptions pp.5–6; Proposition 5.1 and homogenization reduction pp.9–10; final journal article appeared in Foundations of Computational Mathematics 9 (2009), 135–170'),
 ],
 context_blocks=[
 block('The source classifies origin membership in the Euclidean closure as ∃R-complete, then separately leaves the complexity for the Zariski topology open. The card asks for the missing existential upper bound in that second problem.'),
 block('These closures can differ even in one dimension: the real interval (1,2) has Zariski closure all of the real line, because a nonzero univariate polynomial cannot vanish throughout an interval. Its Euclidean closure is [1,2], which excludes the origin.'),
 block('The homogenization reduction in Proposition 5.1 gives Zariski adherence hardness. Applying it to explicitly encoded integer feasibility instances also yields a polynomial-bit reduction: if the feasible set is nonempty its homogenized cone approaches the origin, and otherwise its closure is empty. This discrete application is an editorial consequence of the displayed reduction.','hardness'),
 block('The input retains inequalities and Boolean combinations. Replacing the feasible set by the complex zeros of its displayed equations would change the problem. Nor is the target restricted to additive descriptions of semilinear sets.'),
 ],
 progress=[progress('2005','The ECCC preprint proves adherence hardness using homogenization; the final journal version appeared in 2009.','hardness'),progress('2024','The compendium explicitly lists the Zariski-topology complexity question as open, separately from Euclidean closure.')],
),[
 'Selected membership in ∃R after the unanswered optional target question; applied the announced editorial default without recording user confirmation.',
 'Defined real Zariski closure via all real polynomial relations vanishing on the semialgebraic set.',
 'Specified arbitrary-dimensional Boolean-formula inputs, integer coefficients, explicit monomial lists, unary exponents and finite-bit deterministic reductions.',
 'Separated the source’s Euclidean-completeness statement and real-machine hardness result from the selected discrete upper-bound target.',
 'Preserved the existing individual importance assessment and required a complete Lean-checked membership or nonmembership proof.',
],[
 'Read the compendium’s §15 input convention and all of A37, including the distinct Zariski open question; checked the available arXiv version through 17 September 2026.',
 'Read ECCC TR05-138’s semialgebraic-input convention and Proposition 5.1 with its homogenization proof. The preprint was read; the later journal version was not silently substituted.',
 'A bounded later-work search through 17 September 2026 did not locate a resolution of this general semialgebraic Zariski-adherence target. Semilinear/additive variants do not establish it.',
], 'Source-open as the Zariski variant in compendium entry A37. This card chooses the precise ∃R-membership question within that broader complexity request; the choice was an announced editorial default after an unanswered optional question. The 2005 hardness reduction and known Euclidean closure classification do not provide this upper bound. Later-work search through 17 September 2026 was bounded.',summary=[
 'The input describes a real semialgebraic set by a Boolean formula of explicitly written integer polynomial constraints.',
 'Its real Zariski closure consists of the points satisfying every real polynomial relation that vanishes on the set.',
 'The question asks whether testing that the origin lies in this closure belongs to the existential theory of the reals complexity class.',
 'A positive answer needs one polynomial-bit-time transformation to an equivalent existential real sentence for all input dimensions and degrees.',
 'The source leaves Zariski adherence open, and the known Euclidean result does not settle this target; a complete Lean-checked answer is required.',
],expected_sha256=claim['input_sha256'],claim_token=claim['token'])
