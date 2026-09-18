"""Specialize field dependence to a precisely quantified characteristic-set question."""
import sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT/'research/card-completion-20260913'))
from complete_review import complete,ref,block,progress
from review_queue import read_claims
identifier='TCS-0187';claim=read_claims(ROOT)[identifier]
complete(identifier,dict(
 title='Are characteristic sets of linear-rank inequalities finite or cofinite?',
 status='uncertain',criterion='characterization',question_type='yes_no',
 formal=r'''For every integer \(r\ge1\) and every family of rational coefficients \((c_S)_{\varnothing\ne S\subseteq[r]}\), is the set
\[
P(c)=\left\{p\text{ prime}:\ \forall d\ge0\ \forall V_1,\ldots,V_r\le\mathbb F_p^d,\quad
\sum_{\varnothing\ne S\subseteq[r]}c_S\dim_{\mathbb F_p}\!\left(\sum_{i\in S}V_i\right)\ge0\right\}
\]
either finite or cofinite in the set of all primes?''',
 definitions=r'''Here \([r]=\{1,\ldots,r\}\), \(\mathbb F_p=\mathbb Z/p\mathbb Z\), \(d\) is an arbitrary nonnegative integer, and each \(V_i\) is a linear subspace of the same ambient vector space. The sum of subspaces is the span of their union. There is no bound on ambient dimension or on the dimensions of the subspaces. The coefficients are fixed independently of \(p\), \(d\), and the subspace configuration. Coefficients may have either sign or be zero. The expression is homogeneous: no constant term or additional premise is allowed.

Write \(\mathcal P\) for the set of positive primes. Cofinite means that \(\mathcal P\setminus P(c)\) is finite. Thus the proposed assertion is
\[
\forall r\ge1\ \forall c\quad
\exists\text{ finite }F\subseteq\mathcal P:\quad
P(c)=F\ \text{or}\ P(c)=\mathcal P\setminus F.
\]
The exceptional set may depend on the entire inequality. No effective procedure, computable bound on the exceptional primes, fixed number of variables, or uniform dimension bound is requested. Empty and full characteristic sets are allowed.

Restricting to prime fields does not select a particular extension degree: validity of a homogeneous inequality over \(\mathbb F_p\), with all dimensions allowed, is equivalent to validity over every finite field of characteristic \(p\). This equivalence uses extension and restriction of scalars. The target concerns all subspace configurations, rather than representations of one specified matroid or solvability of one specified network.

A negative answer must supply a fixed rational inequality whose valid characteristic set and invalid characteristic set are both infinite. Examples with an arbitrarily large but finite exceptional set do not refute the assertion. Characteristic zero is outside the domain of this question.''',
 answer_criterion='Give a complete mathematically correct Lean-checked proof of the displayed universal assertion, or a Lean-checked refutation by a fixed number of variables and fixed rational coefficients with infinitely many valid and infinitely many invalid prime characteristics. A construction for each finite or cofinite set alone does not establish the classification.',
 why='Rank inequalities constrain what linear coding can accomplish over different alphabets. This question asks whether one such constraint can distinguish two infinite classes of prime characteristics, beyond the finite exceptional sets occurring in known constructions.',
 source_formulation=dict(text='Problem (8.3) asks broadly how linear-rank inequalities depend on field size and characteristic. The finite-or-cofinite classification of the valid prime characteristics of each fixed rational homogeneous inequality is an editorial specialization of that broad question, not a conjecture explicitly stated in the report. The optional choice remained unanswered; this previously proposed default was announced before application.',caption='Dagstuhl Seminar 22301, §4 Problem (8.3), printed p.202 / standalone PDF p.23; posed by Alexander Shen.',citation='primary',format='editorial_paraphrase'),
 references=[
 ref('primary','Algorithmic Aspects of Information Theory (Dagstuhl Seminar 22301)','Phokion G. Kolaitis; Andrej E. Romashchenko; Milan Studený; Dan Suciu, editors; problem posed by Alexander Shen',2023,'https://doi.org/10.4230/DagRep.12.7.180','July 2022 seminar; report published 3 February 2023; §4 Problem (8.3), printed p.202 / standalone PDF p.23'),
 ref('complementary','Characteristic-Dependent Linear Rank Inequalities via Complementary Vector Spaces','Victor Peña; Humberto Sarria',2019,'https://arxiv.org/abs/1903.11587v2','Checked 5 April 2019 revision; introduction on finite/cofinite constructions, §1 Theorems 7 and 9; later journal version in Journal of Information and Optimization Sciences 42(2), 345–369'),
 ref('access','Access structures for finding characteristic-dependent linear rank inequalities','Victor Peña-Macias',2023,'https://doi.org/10.14736/kyb-2023-2-0198','Kybernetika 59(2), 198–208; §2 Theorem 2.6 and the counterexamples immediately following, p.202'),
 ],
 context_blocks=[
 block('The seminar poses field size and characteristic dependence as a research direction without choosing one exact classification theorem. This card isolates a characteristic-set question and records that specialization explicitly.'),
 block('For homogeneous inequalities with unbounded ambient dimension, passing from a finite field to its prime subfield multiplies every dimension by the same extension degree; extending scalars preserves dimensions. This elementary observation removes extension degree from this particular validity question.'),
 block('The 2019 paper reviews constructions realizing finite and cofinite characteristic sets. Its Theorems 7 and 9 give inequalities valid when the characteristic divides a fixed integer and when it does not, respectively. Existence of these examples does not show that every inequality has one of those forms.','complementary'),
 block('The 2023 theorem obtains characteristic-dependent inequalities from binary matrices of determinant t > 1, separating primes dividing t from those not dividing t; the following configurations witness failure in the opposite cases. The determinant-based theorem still treats finite or cofinite sets.','access'),
 block('A theorem about the characteristics in which a single matroid is representable would concern a different quantifier pattern. Here validity ranges over every finite-dimensional subspace configuration, with no fixed rank bound.'),
 ],
 progress=[progress('2019','The checked revision presents complementary-space constructions for characteristic-dependent rank inequalities, including divisibility and nondivisibility cases.','complementary'),progress('2022','The seminar asks how linear-rank inequalities depend on field size and characteristic.'),progress('2023','The binary-matrix construction gives further inequalities whose validity depends on prime divisors of a determinant.','access')],
),[
 'Replaced a broad index label with the announced finite-or-cofinite specialization; recorded it as editorial rather than user-confirmed or a verbatim source conjecture.',
 'Fixed rational homogeneous coefficients, arbitrary numbers of subspaces, unbounded ambient dimension and all prime characteristics.',
 'Separated prime-field validity from fixed-dimension representability and explained extension-degree invariance for this model.',
 'Checked finite/cofinite constructions without treating their existence as an exhaustive classification.',
 'Preserved assessed importance and retained uncertain current status for the editorial specialization; required a complete Lean-checked proof or refutation.',
],[
 'Read Dagstuhl §4 Problem (8.3) and checked the author attribution and page locator.',
 'Read the introduction and Theorems 7 and 9 of the 5 April 2019 complementary-space revision.',
 'Read Theorem 2.6 and its characteristic-dependent counterexamples in Peña-Macias 2023.',
 'Bounded primary-source searches through 18 September 2026 found constructions and related representability work, but did not establish a resolution or an explicit prior statement of this exact general classification.',
], 'The 2022 source leaves the broad characteristic-dependence direction open. The selected finite-or-cofinite assertion is an explicitly recorded editorial specialization. Checked 2019 and 2023 constructions realize these types of characteristic sets but do not prove exhaustiveness. The bounded review through 18 September 2026 has not established the current status of this exact assertion; it is therefore marked uncertain, rather than certified currently open.',summary=[
 'Fix a rational homogeneous linear inequality in the dimensions of sums of finitely many subspaces.',
 'For each prime, test whether that inequality holds for every subspace configuration over its prime field, in every finite dimension.',
 'The question is whether the set of primes where it holds must be finite or have finite complement.',
 'Known characteristic-dependent constructions realize finite and cofinite sets but do not by themselves classify every inequality.',
 'This is an explicit specialization of the source’s broader field-dependence question, and its exact current status remains uncertain.',
],expected_sha256=claim['input_sha256'],claim_token=claim['token'])
