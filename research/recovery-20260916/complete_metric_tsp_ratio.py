"""Complete the algorithmic metric-TSP threshold, distinct from its LP gap."""
import sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];sys.path.insert(0,str(ROOT/'research/card-completion-20260913'))
from complete_review import complete,ref,block,progress,DATE
from review_queue import read_claims
identifier='TCS-7356';claim=read_claims(ROOT)[identifier]
notes=[
 'Preserved the unconditional numerical infimum over uniform randomized polynomial-time approximation algorithms, with absolute 1/100 Lean acceptance.',
 'Specified explicit rational strict metrics, full binary input length, always-feasible tours, worst-case polynomial time on every random tape and expected approximation quality.',
 'Separated the infimum from an attained optimum, and algorithmic lower bounds from an integrality gap or a conditional hardness theorem.',
 'Checked the original breakthrough, derandomization, the 2024 constant, restricted July 2026 progress and the September explicit-saving claim without calling these a threshold determination.',
 'Preserved importance 94 and the relation to TCS-6589; no complexity separation is assumed in the answer criterion.',
]
sources=[
 'Read Karlin–Klein–Oveis Gharan, arXiv:2007.01409v6, submitted 25 October 2023, PDF header 26 October, abstract and §1 Theorem 1.1 p. 1. The first preprint is from 2020 and the conference result from 2021; this theorem is relative to the integral tour optimum.',
 'Read Karlin–Klein–Oveis Gharan, arXiv:2212.06296v1, 13 December 2022, primary abstract: deterministic polynomial-time approximation below three halves. No full derandomization proof was independently audited.',
 'Read Gurvits–Klein–Leake, arXiv:2311.09072v2, 9 May 2024, §4.2 Lemma 4.5 and Corollary 4.6 p. 10 and Appendix A.4 p. 26. The stated ratio is 3/2 minus 2.18*10^{-34}; the text also records derandomization.',
 'Read Karpinski–Lampis–Schmied, arXiv:1303.6437v2, 10 June 2013, introduction pp. 1–3, §5 Theorem 4 and its proof: NP-hardness of every constant ratio strictly below 123/122. This is recorded as hardness, not an unconditional lower bound against randomized polynomial-time algorithms.',
 'Read Jin–Klein–Williamson, arXiv:2607.01536v2, 3 July 2026, abstract and introduction pp. 1–2. The ten-sevenths guarantee is for half-integral cycle-cut instances, not all input metrics.',
 'Read Song, Preprints.org 202609.0140/v1, posted 2 September 2026, abstract and Theorem 1 in full HTML. It claims expected polynomial-time approximation with a universal saving greater than 2.05522*10^{-30}. Proof and numerical certificate were not independently audited; this claimed bound would still not determine the numerical threshold within 1/100.',
 f'Bounded primary-source searches through {DATE} found no verified determination of the unrestricted algorithmic infimum to the required precision. Restricted-family and finite LP-gap results were not counted as such a determination.',
]
complete(identifier,dict(
 criterion='tightness',question_type='numerical_value',
 formal=r'''Determine, to absolute accuracy \(1/100\), the optimal expected polynomial-time approximation ratio for symmetric metric traveling-salesperson problems:
\[
 \rho_{\mathrm{TSP}}=\inf\mathcal R,
\qquad
 \mathcal R=\{r\in\mathbb R:r\ge1\text{ and }r\text{ is achievable as defined below}\}.
\]
The infimum ranges over all uniform classical randomized algorithms in the stated bit model and all finite input metrics. It is an unconditional real constant; no unproved complexity assumption is part of its definition.''',
 definitions=r'''An input \(I\) consists of an integer \(n\ge3\) and the full explicitly listed matrix \(d\in\mathbb Q^{n\times n}\), with
\[
 d(i,i)=0,\qquad d(i,j)=d(j,i)>0\quad(i\ne j),\qquad
 d(i,k)\le d(i,j)+d(j,k)\quad(i,j,k\in\{1,\ldots,n\}).
\]
Integers are binary encoded, and a rational entry is given by a binary numerator and positive binary denominator. Let \(L(I)\) be the full binary encoding length, including all entries and their delimiters. There is no promise of an embedding, a graph representation, bounded aspect ratio or a restricted metric family.

A feasible output is a permutation \(\pi\) of \(\{1,\ldots,n\}\). Its tour cost includes the closing edge:
\[
 \operatorname{cost}_I(\pi)=\sum_{i=1}^{n}d(\pi(i),\pi(i+1)),
 \qquad \pi(n+1)=\pi(1).
\]
The positive number \(\operatorname{OPT}(I)\) is the minimum of this cost over all permutations.

An algorithm is one uniform classical randomized Turing machine with independent fair random bits. For some polynomial \(p\), on every valid input and every random tape it halts within \(p(L(I))\) steps and outputs a feasible tour. Its program is finite and independent of the input length; no input-length advice, external oracle or uncharged real arithmetic is available. The runtime bound is worst-case over the coins, although approximation quality is measured in expectation over those coins. Deterministic algorithms are included.

A real number \(r\ge1\) is achievable if there exist such an algorithm \(A\) and polynomial bound \(p\) with
\[
 \mathbb E[\operatorname{cost}_I(A(I))]\le r\operatorname{OPT}(I)
 \quad\text{for every valid }I.
\]
The algorithm and its polynomial may depend on the fixed value \(r\), but not on the particular input or its unknown optimal tour. There is no requirement of an effective procedure that takes \(r\) and produces the algorithm. The set \(\mathcal R\) is nonempty by known constant-factor algorithms, so its infimum is a finite number at least one. The infimum need not itself be achievable.

This quantity compares efficient algorithms with the integral tour optimum. It is distinct from the supremum of the integral optimum divided by the optimum of the subtour linear program. An integrality-gap example is not by itself a lower bound against every algorithm. A result for one rounding method, a bounded number of vertices, graph metrics, Euclidean metrics or a special class of fractional solutions does not determine this unrestricted algorithmic infimum.

The accuracy requirement is absolute error in the dimensionless ratio. No runtime bound is imposed on evaluating a submitted mathematical expression for the answer. If \(P=NP\), exact optimization gives \(\rho_{\mathrm{TSP}}=1\); conditional inapproximability results must therefore keep their assumptions and cannot silently be substituted for unconditional lower bounds.''',
 answer_criterion=r'''Supply a specified real number \(a\) and a complete Lean-checked proof that
\[
 |a-\rho_{\mathrm{TSP}}|\le1/100.
\]
A Lean-proved interval \(L\le\rho_{\mathrm{TSP}}\le U\) of width at most \(1/50\) qualifies via its midpoint. A certified finite mathematical expression may specify the answer; a decimal expansion or efficient evaluation algorithm is not required.

Upper control must establish achievable guarantees approaching the proposed bound, or an equivalent proof about the infimum; an algorithm attaining the infimum is not required. Lower control must concern every admissible algorithm. Merely improving a single algorithm, proving an LP integrality gap, giving conditional hardness under an unproved assumption, or restating the defining infimum is insufficient. A proof using an unproved complexity assumption answers only that conditional variant, not this card's unconditional target.''',
 source_formulation=dict(text='The original breakthrough gives an expected polynomial-time approximation strictly below three halves for every metric TSP instance. The hardness source describes determination of the best approximation ratio as the broader open problem. This card retains its numerical version: the infimum over all uniform randomized polynomial-time algorithms, with the project’s absolute 1/100 tolerance.',caption='Editorial paraphrase of Karlin–Klein–Oveis Gharan, §1 and Theorem 1.1, and Karpinski–Lampis–Schmied, introduction; the precise algorithm model and numerical acceptance convention are retained from the card.',citation='primary',format='editorial_paraphrase'),
 references=[
 ref('primary','A (Slightly) Improved Approximation Algorithm for Metric TSP','Anna R. Karlin; Nathan Klein; Shayan Oveis Gharan',2021,'https://arxiv.org/abs/2007.01409v6','STOC 2021 result; checked version 6, 25 October 2023, §1 Theorem 1.1 p. 1'),
 ref('hardness','New Inapproximability Bounds for TSP','Marek Karpinski; Michael Lampis; Richard Schmied',2013,'https://arxiv.org/abs/1303.6437v2','Version 2, 10 June 2013; introduction and §5 Theorem 4, NP-hardness below 123/122'),
 ref('deterministic','A (Slightly) Improved Deterministic Approximation Algorithm for Metric TSP','Anna R. Karlin; Nathan Klein; Shayan Oveis Gharan',2022,'https://arxiv.org/abs/2212.06296v1','13 December 2022; primary abstract, deterministic guarantee below three halves'),
 ref('gkl','From Trees to Polynomials and Back Again: New Capacity Bounds with Applications to TSP','Leonid Gurvits; Nathan Klein; Jonathan Leake',2024,'https://arxiv.org/abs/2311.09072v2','Version 2, 9 May 2024; §4.2 Corollary 4.6 p. 10 and Appendix A.4 p. 26'),
 ref('restricted',r'Maximum Entropy is a \(10/7\)-Approximation Algorithm for the TSP on Half-Integral Cycle Cut Instances','Billy Jin; Nathan Klein; David P. Williamson',2026,'https://arxiv.org/abs/2607.01536v2','Version 2, 3 July 2026; abstract and §1 pp. 1–2, restricted instance class'),
 ref('song','A Sharper Explicit Bound on the Subtour-LP Integrality Gap for Metric TSP','Zhao Song',2026,'https://www.preprints.org/manuscript/202609.0140/v1','Posted 2 September 2026; abstract and Theorem 1 read in full HTML; proof and numerical certificate not independently audited'),
 ],
 context_blocks=[
 block(r'The 2021 breakthrough establishes a universal expected approximation strictly below \(3/2\), after decades at that threshold. Its theorem compares the returned tour with the optimal integral tour, matching this card’s denominator.'),
 block(r'The later derandomization gives a deterministic guarantee below \(3/2\). Thus the current progress is not confined to algorithms with only an expected runtime bound.','deterministic'),
 block(r'The 2024 analysis records the explicit ratio \(3/2-2.18\cdot10^{-34}\). This improves a universal upper bound, but does not determine the best achievable ratio to absolute precision \(1/100\).','gkl'),
 block(r'Approximating within any fixed factor strictly below \(123/122\) is NP-hard in the cited theorem. Such a hardness statement does not itself prove an unconditional numerical lower bound on the infimum over randomized polynomial-time algorithms.','hardness'),
 block(r'The July 2026 \(10/7\) guarantee applies to half-integral cycle-cut instances. It does not give that ratio for every metric in this card.','restricted'),
 block(r'A September 2026 preprint claims a larger universal saving above \(2.05522\cdot10^{-30}\) below \(3/2\). Its statement was checked, but its proof and numerical certificate were not independently audited. Even the claimed upper bound is far from a two-sided determination within \(1/100\).','song'),
 ],
 progress=[progress('2021','The expected approximation threshold improves strictly below three halves.'),progress('2022-12-13','A deterministic polynomial-time guarantee below three halves is announced.','deterministic'),progress('2024-05-09','The revised analysis gives an improved explicit universal approximation constant.','gkl'),progress('2026-07-03','A revised theorem improves an algorithm on half-integral cycle-cut instances.','restricted'),progress('2026-09-02','A preprint claims a further small universal saving; its proof was not independently audited.','song')],
),notes,sources,'Bounded primary-source checks through 17 September 2026 found no verified numerical determination of the unrestricted polynomial-time approximation infimum within 1/100. General approximation improvements, restricted-instance theorems and conditional hardness statements do not supply this unconditional two-sided estimate. The September explicit-saving preprint is recorded as an unaudited claim, whose stated bound would also leave the target unresolved.',summary=[
 'Metric TSP asks for a cheapest closed tour visiting every point in a finite metric.',
 'This card asks for the infimum of expected approximation ratios achieved by uniform randomized polynomial-time algorithms.',
 'All inputs are explicit rational metrics, every execution must finish in polynomial time, and every output must be a valid tour.',
 'Known improvements below three halves and conditional hardness results leave the unconditional optimal ratio undetermined.',
 'An answer needs a complete Lean-checked estimate within absolute error 1/100, controlling the algorithmic infimum on both sides.',
],expected_sha256=claim['input_sha256'],claim_token=claim['token'])
