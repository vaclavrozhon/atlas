"""Recover the normalized Ingleton-score value target and numerical criterion."""
import sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT/'research/card-completion-20260913'))
from complete_review import complete,ref,block,progress
from review_queue import read_claims
identifier='TCS-0205';claim=read_claims(ROOT)[identifier]
complete(identifier,dict(
 title='The infimal normalized Ingleton score',
 status='source_open',criterion='tightness',question_type='numerical_value',
 formal=r'''Determine, with certified absolute error at most \(1/100\), the real constant
\[
\iota_*=
\inf_{\substack{X_1,X_2,X_3,X_4\ \text{finite-valued}\\H(X_1,X_2,X_3,X_4)>0}}
\frac{I(X_1;X_2\mid X_3)+I(X_1;X_2\mid X_4)+I(X_3;X_4)-I(X_1;X_2)}
{H(X_1,X_2,X_3,X_4)}.
\]
The infimum ranges over all finite alphabet sizes and all joint probability distributions, with no common bound on the alphabets. Negative values represent violations of the Ingleton inequality.''',
 definitions=r'''Choose arbitrary positive integers \(k_1,k_2,k_3,k_4\), and a joint probability table \(p\) on \(\prod_{i=1}^4\{1,\ldots,k_i\}\), with arbitrary nonnegative real entries summing to one. The variables \(X_i\) are its coordinate projections. For any tuple \(Y\) of these variables, use its marginal distribution and define Shannon entropy in bits by
\[
H(Y)=-\sum_y\Pr[Y=y]\log_2\Pr[Y=y],\qquad 0\log_2 0:=0.
\]
For tuples \(U,V,W\), define
\[
I(U;V)=H(U)+H(V)-H(U,V),
\]
\[
I(U;V\mid W)=H(U,W)+H(V,W)-H(W)-H(U,V,W).
\]
No independence, uniformity, symmetry, group representation or linearity is assumed. Zero-probability atoms are permitted. The only exclusion is zero joint entropy, which would make the displayed quotient undefined.

The infimum is the greatest real lower bound of this nonempty set of scores. It exists as a finite real number: all three positive terms in the numerator are nonnegative and \(I(X_1;X_2)\le H(X_1,X_2,X_3,X_4)\), so every score is at least \(-1\). The infimum need not be attained by any single finite probability table. An approximating sequence may use growing alphabets. The normalization is by joint entropy, not by a Euclidean norm of the entropy vector or by a modified denominator; the resulting score is dimensionless and invariant under a common change of logarithm base.

The requested answer is a specified real number \(a\) with \(|a-\iota_*|\le1/100\), or a certified interval \([\ell,u]\) containing \(\iota_*\) and of width at most \(1/50\), whose midpoint supplies such an answer. The number may be given by an unambiguous mathematical expression; a decimal expansion is not mandatory. There is no running-time requirement for finding or evaluating it.

For interval certification, a lower bound must hold uniformly for every finite joint table: equivalently, the displayed numerator is at least \(\ell\,H(X_1,X_2,X_3,X_4)\). An upper bound can be certified by a concrete joint table with score at most \(u\), or by a rigorous sequence whose limiting score is at most \(u\). A local numerical minimum or a search over any fixed alphabet does not certify a global lower bound.''',
 answer_criterion='Supply a concrete real approximation a and a complete mathematically correct Lean-checked proof that |a−ι_*| ≤ 1/100, or a Lean-checked enclosing interval of width at most 1/50. Both sides of any interval must be justified over the full unrestricted finite-alphabet domain. Exact determination is welcome but unnecessary. Proving algebraicity, exhibiting an attaining distribution, or merely disproving the four-atom conjecture is not required and does not by itself meet this numerical criterion.',
 why='The normalized Ingleton violation measures how far general entropy vectors can depart from an inequality obeyed by linear-rank models. Locating its global infimum would give a concrete quantitative constraint on the poorly understood four-variable entropy region.',
 source_formulation=dict(text='Problem (2.1) asks how far the four-atom conjecture was from the infimal Ingleton score and additionally asks whether the infimum is algebraic and which distributions reach it. This card retains the value question, with the catalogue’s numerical acceptance tolerance; it does not combine the algebraicity and attainment questions.',caption='Dagstuhl Seminar 22301, Algorithmic Aspects of Information Theory, §4 Problem (2.1), printed p.199; posed by László Csirmaz.',citation='primary',format='editorial_paraphrase'),
 references=[
 ref('primary','Algorithmic Aspects of Information Theory (Dagstuhl Seminar 22301)','Phokion G. Kolaitis; Andrej E. Romashchenko; Milan Studený; Dan Suciu, editors; problem posed by László Csirmaz',2023,'https://doi.org/10.4230/DagRep.12.7.180','July 2022 seminar, report published 3 February 2023; §4 Problem (2.1), printed p.199 / standalone PDF p.20; reference [11]'),
 ref('convolution','Entropy region and convolution','František Matúš; László Csirmaz',2013,'https://arxiv.org/abs/1310.5957v1','Checked 22 October 2013 preprint; §8 definition and Theorem 5 p.16; Example 2 pp.17–18. Later journal version: IEEE TIT 62(11), 6007–6018 (2016)'),
 ref('improvement','Violations of the Ingleton inequality and revising the four-atom conjecture','Nigel Boston; Ting-Ting Nan',2020,'https://doi.org/10.14736/kyb-2020-5-0916','§2.2 Definition 2.3 pp.920–921, opposite sign convention; Theorem 2.6 p.921; Example 4.11 p.930 and §5 numerical search pp.930–931'),
 ref('numerics','Optimizing Distributions for Associated Entropic Vectors via Generative Convolutional Neural Networks','Shuhao Zhang; Nan Liu; Wei Kang; Haim Permuter',2024,'https://doi.org/10.3390/e26080711','Published 21 August 2024; Theorems 2–3 for a fixed alphabet, Table 2 p.14, numerical-stability discussion and Remark 2 p.15'),
 ],
 context_blocks=[
 block('The seminar identifies the score as a global geometric question and points to a reduction of the infimum to a symmetrized part of the four-variable almost-entropic region. It separately asks about algebraicity and attainment.'),
 block('Matúš and Csirmaz prove that the infimum can be minimized on a compact three-dimensional slice of the almost-entropic closure. Their Example 2 yields a value near −0.09243 and refutes the four-atom conjecture. Closure membership is not the same as finite-alphabet attainment.','convolution'),
 block('Boston and Nan use the opposite sign: positive values measure violations. Translating their convention gives the reported upper estimate near −0.0925000777 for this card’s infimum. Their Theorem 2.6 explains how an optimized modified-denominator score is approached by ordinary scores.','improvement'),
 block('Their discussion reports the universal lower bound −3/19 after sign conversion. Together with the displayed examples it leaves a gap substantially wider than 1/50, so those bounds do not meet this card’s acceptance criterion.','improvement'),
 block('The 2024 neural optimization reports −0.0925001031 after the entropy transformation and describes the tiny difference from the earlier estimate as numerical stability. Its approximation theorems concern a fixed finite alphabet; neither those theorems nor the numerical table certify the unrestricted global infimum.','numerics'),
 block('The Ingleton violation index optimized elsewhere in that paper uses a different normalization. An improved index is therefore not automatically an improved bound on the score in this card.','numerics'),
 ],
 progress=[progress('2013','The checked preprint gives the compact-slice reduction and a counterexample to the four-atom conjecture.','convolution'),progress('2020','Boston and Nan report a larger violation using a modified score and a limiting conversion back to the original normalization.','improvement'),progress('2022','The seminar asks for the infimal value, with separate algebraicity and attainment questions.'),progress('2024-08','Neural optimization recovers approximately the earlier best reported score; the reported improvement in a separate violation index is distinguished.','numerics')],
),[
 'Recovered the exact joint-entropy normalization and negative sign convention, with all four finite alphabets unbounded.',
 'Retained determination of the unknown value, applying the catalogue’s 1/100 acceptance tolerance rather than converting it to a best-known-bound barrier.',
 'Separated the value question from algebraicity and attainment and allowed limiting constructions with growing alphabets.',
 'Checked the four-atom refutation, the opposite-sign 2020 formulation and the fixed-alphabet/numerical qualifications of the 2024 results.',
 'Preserved assessed importance, repaired the imported authorship and required a complete Lean-checked two-sided numerical certificate.',
],[
 'Read Dagstuhl Problem (2.1) and reference [11], checking the report’s printed and standalone PDF page numbers.',
 'Downloaded the 2013 Matúš–Csirmaz preprint and read §8 Theorem 5 and Example 2 with the closure/attainment distinction.',
 'Downloaded Boston–Nan 2020 and read Definitions 2.3/2.5, Theorem 2.6, Example 4.11 and the subsequent numerical-search discussion.',
 'Downloaded Zhang–Liu–Kang–Permuter 2024 and read the fixed-alphabet theorem statements, Table 2, the numerical-stability qualification and Remark 2; bounded later searches through 17 September 2026 found no matching global certificate.',
], 'The unrestricted normalized infimum, including a certificate meeting the selected 1/100 accuracy, remains unresolved in the checked sources through 17 September 2026. The four-atom conjecture is already false, and numerical examples near −0.0925 give only one side. The reviewed universal lower bound and reported upper estimates do not enclose the infimum within width 1/50. No claim of exact arithmetic certification is made for the final decimal digits of numerical experiments.',summary=[
 'The Ingleton score divides a particular linear combination of four-variable entropies by their joint entropy.',
 'Negative scores measure violations of an inequality satisfied by linear-rank configurations.',
 'The target is the infimum over all finite joint distributions, with no fixed alphabet bound, to certified absolute error 1/100.',
 'Known examples near −0.0925 disprove the four-atom conjecture but do not supply the needed global lower bound.',
 'A complete Lean-checked answer must certify both sides and need not prove algebraicity or attainment.',
],expected_sha256=claim['input_sha256'],claim_token=claim['token'])
