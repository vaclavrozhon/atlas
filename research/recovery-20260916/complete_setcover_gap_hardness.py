"""Complete the selected Set Cover question and record its conditional resolution."""
import sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT/'research/card-completion-20260913'))
from complete_review import complete,ref,block,progress
from review_queue import read_claims
identifier='TCS-0734'; claim=read_claims(ROOT)[identifier]
notes=[
 'Applied the user’s explicit selection of ordinary Set Cover and factor c*(log n)^0.99, with n equal to universe size; removed the separate Exact Set Cover and Densest k-Subgraph questions.',
 'Corrected the misleading title: the question seeks a stronger consequence under Gap-ETH, not a weakening of that assumption.',
 'Defined the parameterized gap problem, full incidence encoding, uniform deterministic FPT time and sparse deterministic Gap-ETH, consistent with TCS-7313.',
 'Used max(1,c*(log_2(n+2))^(99/100)) so the approximation threshold never drops below one on small inputs.',
 'Read the newly published 17 September 2026 ECCC revision and checked the conversion from candidate-set count to universe size, including the completeness-parameter divisor in its explicit gap construction.',
 'Recorded a conditional resolution of the selected weaker exponent using the explicit construction and a computable small-instance cutoff; did not rely solely on the headline near-logarithmic ratio.',
 'Assessed significance individually, retained the full Lean-checked implication criterion, and archived the historical target with the preprint and verification limits explicit.',
]
sources=[
 'Read Manurangsi, FPT Inapproximability Results Beyond Gap-ETH, §5.4 of Parameterized Approximation: Algorithms and Hardness, Dagstuhl Report 23291, DOI 10.4230/DagRep.13.7.96, printed p.105. Item 1 asks for Omega(log^0.99 n) FPT inapproximability of k-Set Cover under Gap-ETH, where n counts universe elements. Items 2 and 3 are separate questions and were excluded by the user’s choice.',
 'Read Guruswami–Ren, Almost Optimal FPT Inapproximability for k-SetCover, ECCC TR26-186 revision 1, posted 17 September 2026 at 06:14 according to the primary page: abstract, Introduction pp.1–3, Theorems 1.1–1.2 p.2, Definitions 2.1–2.4, Lemmas 2.5–2.6 and §3 pp.4–6. The statement uses candidate-set count, and the explicit construction yields a completeness-m versus soundness-h gap with h=floor(log N/log log N) and polynomial output size. The Introduction gives the direct Clique version with m=binom(k,2).',
 'Checked the consequence for the card’s exponent separately: after deleting isolated source vertices, the explicit universe has at most N^D elements for a fixed D, and h/[m*(log(N^D+2))^0.99] tends to infinity for each fixed parameter m. A computable cutoff depending on the source parameter allows smaller instances to be handled by brute force in FPT time. Thus an FPT algorithm for the selected gap would give an FPT Clique algorithm, excluded under ETH; sparse deterministic Gap-ETH implies the required deterministic ETH hardness. Details and scope limits are in research/recovery-20260916/review_setcover_0734.md.',
 'The publication is a same-day primary preprint. Its complete proof has not been independently formalized or audited here. The selected conclusion uses the explicitly read reduction and standard parameterized ETH hardness; it does not certify the stronger sharp ratio or time bound advertised in the abstract, nor the disjoint-cover variant.',
]
status='Archived as conditionally resolved for the user-selected exponent 0.99. The explicit gap construction in Guruswami–Ren, ECCC TR26-186 revision 1 (17 September 2026), has polynomial output size and yields the selected universe-size lower bound after a computable parameter-dependent small-instance cutoff. ETH suffices, so the stated sparse deterministic Gap-ETH also suffices. This is a checked parameter consequence of a new primary preprint, not an unconditional impossibility theorem or an independent Lean verification of the paper. The sharper headline ratio and the other two seminar questions are not certified by this review.'
complete(identifier,dict(
 title='Near-logarithmic FPT inapproximability of Set Cover under Gap-ETH',
 criterion='assumptions',question_type='yes_no',status='resolved',
 importance=dict(score=76,method='editorial',reason='The selected target closes the exponent gap between logarithmic greedy approximation and older parameter-dependent lower bounds for a central parameterized covering problem. Its significance is stronger approximation hardness under a fixed assumption, rather than weakening Gap-ETH itself.'),
 formal=r'''Does sparse deterministic Gap-ETH imply that, for some rational constant \(c>0\), no uniform deterministic FPT algorithm can distinguish
\[
\operatorname{OPT}(U,\mathcal S)\le k
\quad\text{from}\quad
\operatorname{OPT}(U,\mathcal S)>\rho_c(n)k,
\qquad
\rho_c(n)=\max\{1,c(\log_2(n+2))^{99/100}\},
\]
where \(n=|U|\) is the number of universe elements, \(\mathcal S\) is an explicitly given family of subsets of \(U\), and \(k\) is the parameter? FPT means time \(f(k)(L+1)^d\) for some computable function \(f\) and fixed exponent \(d\), with \(L\) the full input bit length. The two alternatives are promised; the definitions below fix the hypothesis and model.''',
 definitions=r'''A Set Cover instance consists of a universe \(U=\{1,\ldots,n\}\) with \(n\ge1\), a list \(\mathcal S=(S_1,\ldots,S_M)\) of subsets of \(U\), and an integer \(1\le k\le\max\{1,M\}\). The sets need not be disjoint and may be empty or repeated. A cover is a set of indices \(J\subseteq\{1,\ldots,M\}\) with \(\bigcup_{j\in J}S_j=U\). Its cost is \(|J|\), and \(\operatorname{OPT}\) is the minimum cost, or \(+\infty\) if no cover exists. No disjoint-cover promise is imposed, even in the YES case.

Supply \(n,M,k\) in self-delimiting binary followed by the explicit \(n\)-by-\(M\) incidence matrix, in row order. For definiteness, a nonnegative integer \(z\) is coded by \(1^b0\) and then the \(b\)-bit expansion of \(z+1\), where \(b=\lfloor\log_2(z+1)\rfloor+1\). There is no trailing data. The total length is \(L\). The variable \(n\) in the approximation factor counts elements, not sets, incidences or encoding bits.

For fixed \(c\), an FPT gap algorithm means one uniform deterministic multitape Turing machine \(A\), an integer \(d\ge1\) and a total computable \(f:\mathbb N\to\mathbb N_{\ge1}\) such that every valid instance halts within \(f(k)(L+1)^d\) bit steps. It returns YES when \(\operatorname{OPT}\le k\), and NO when \(\operatorname{OPT}>\rho_c(n)k\). Between the two thresholds either answer is permitted, while the time bound still holds. All computation is charged, with no advice, randomness or oracle. A covering algorithm with the same parameterized time bound and guaranteed cost at most \(\rho_c(n)k\) whenever a size-\(k\) cover exists would in particular distinguish this gap.

Sparse deterministic Gap-ETH is the following proposition. There exist an integer \(B\ge1\) and rational constants \(\eta>0\) and \(0<\delta<1\) such that no deterministic uniform Turing machine, with any fixed constants \(K>0\) and integer \(q\ge1\), distinguishes satisfiable 3-CNF formulas from formulas whose assignments all satisfy at most a \(1-\delta\) fraction of clauses, in time
\[
K2^{\eta v}(\ell+1)^q.
\]
Here \(v\) is the number of occurring variables, there are at most \(Bv\) clauses, each clause contains at most three signed variables, and \(\ell\) is the full explicit binary clause-list encoding length. Encode counts, clause lengths and variable indices by the same self-delimiting integer code, with a sign bit for each literal. Clause occurrences count with multiplicity. The formula with no clauses has value one; an empty clause is false. Every declared variable must occur. The time bound holds for all valid formulas of this density, and either output is allowed outside the satisfiable-versus-gap promise. There is no randomness or advice in either hypothesis or conclusion.

The question is the implication from this hypothesis to \(\exists c>0\) with no FPT gap algorithm as defined above. It does not ask to prove Gap-ETH itself. The clipping of \(\rho_c\) at one only fixes small inputs and leaves the selected asymptotic factor unchanged.''',
 answer_criterion=r'''Give a complete mathematically correct Lean-checked proof of the displayed implication, with no unproved premise beyond its stated Gap-ETH antecedent, or a complete Lean-checked proof of its logical negation. A positive proof must justify the selected universe-size approximation factor and exclude every computable \(f(k)\) and fixed polynomial exponent in the stated deterministic model.

The logical negation requires Gap-ETH together with the existence, for every rational \(c>0\), of an FPT algorithm for the corresponding gap. Merely failing to prove a reduction or giving an approximation in time \(n^{g(k)}\) does not refute the implication. A lower bound using the number of candidate sets must justify its conversion to the universe-size convention. Hardness only for a factor depending on \(k\), a disjoint-cover promise or another optimization problem is not the selected target. Archival records the mathematical resolution reported in the checked source; it is not a claim that this Lean formalization has already been supplied.''',
 source_formulation=dict(text='Item 1 asks for FPT inapproximability of Set Cover of order (log n)^0.99 under Gap-ETH, where n is universe size. The user selected this item rather than the two subsequent questions.',caption='Manurangsi, §5.4, item 1, printed p.105 of Dagstuhl Report 23291. The deterministic hypothesis, incidence encoding and small-input clipping are explicit conventions for the historical target.',citation='primary',format='editorial_paraphrase'),
 references=[
 ref('primary','Parameterized Approximation: Algorithms and Hardness — §5.4, FPT Inapproximability Results Beyond Gap-ETH','Pasin Manurangsi',2023,'https://doi.org/10.4230/DagRep.13.7.96','Dagstuhl Seminar 23291, §5.4 item 1, printed p.105; n counts universe elements'),
 ref('resolution','Almost Optimal FPT Inapproximability for k-SetCover','Venkatesan Guruswami; Xuandi Ren',2026,'https://eccc.weizmann.ac.il/report/2026/186/revision/1/','Revision 1, 17 September 2026; Introduction pp.1–3, Lemmas 2.5–2.6 and §3 pp.4–6; explicit completeness-m versus soundness-h construction'),
 ],
 context_blocks=[
 block('The greedy algorithm gives logarithmic approximation. The seminar asks whether parameterized running time still cannot achieve a factor with a slightly smaller fixed power of that logarithm.'),
 block('The parameter is the number of sets allowed in a small cover. Arbitrarily expensive dependence on that parameter is permitted, provided the exponent of the input length is fixed.'),
 block('A new primary preprint gives a gap construction with logarithmic-over-logarithmic soundness threshold and polynomial output size. Its completeness threshold is also parameter-dependent and must be included when computing an approximation ratio.','resolution'),
 block('For the selected exponent 0.99, the size bounds allow the parameter-dependent loss to be absorbed above a computable cutoff; smaller source instances can be handled in parameter-dependent time. This yields the selected universe-size consequence under ETH, hence under the stated stronger gap hypothesis. This consequence is inferred from the explicit construction, rather than by relabeling the preprint’s size variable.','resolution'),
 block('The archived conclusion is conditional on the hypothesis. The same-day preprint has not been independently formalized here, and the two other questions in the seminar contribution are outside this card.'),
 ],
 progress=[progress('2023','The seminar explicitly asks for universe-size logarithmic-power FPT inapproximability under Gap-ETH.'),progress('2026-09-17','A new ECCC revision supplies an explicit gap construction whose polynomial size bounds imply the selected exponent-0.99 target under ETH; the parameter conversion is recorded in the review.','resolution')],
),notes,sources,status,summary=[
 'The historical target concerns ordinary Set Cover with the requested cover size as parameter.',
 'It asks for Gap-ETH-based exclusion of FPT algorithms with approximation factor c times the universe-size logarithm to the power 0.99.',
 'The explicit input model permits arbitrary computable dependence on the parameter and a fixed polynomial dependence on total input length.',
 'A new September 2026 preprint’s explicit gap construction implies this selected target after checking its size parameters and a parameter-dependent cutoff.',
 'The card is archived for that conditional resolution, without claiming an unconditional lower bound or a completed Lean formalization.',
],expected_sha256=claim['input_sha256'],claim_token=claim['token'],archive_reason='Selected universe-size (log n)^0.99 FPT inapproximability target is conditionally resolved by the explicit gap construction in Guruswami–Ren, ECCC TR26-186 revision 1, 17 September 2026. Its polynomial output-size bound and a computable parameter-dependent cutoff give this consequence under ETH, hence under the stated sparse deterministic Gap-ETH. New primary preprint; no independent Lean formalization or certification of its sharper headline ratio is claimed.')
