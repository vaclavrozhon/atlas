"""Complete exact validity decidability for unconditional entropy inequalities."""
import sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];sys.path.insert(0,str(ROOT/'research/card-completion-20260913'))
from complete_review import complete,ref,block,progress,DATE
from review_queue import read_claims
identifier='TCS-6608';claim=read_claims(ROOT)[identifier]
notes=[
 'Retained one rational homogeneous unconditional linear inequality, arbitrary finite alphabets, arbitrary real joint probabilities and variable number of variables.',
 'Renamed the title to unconditional entropy inequalities to avoid confusing all Shannon-entropy inequalities with the decidable narrower class of Shannon-type consequences.',
 'Specified the finite sparse input encoding, exact non-strict validity predicate and one total deterministic Turing decision procedure without a time bound or distribution oracle.',
 'Separated unconditional validity from conditional-inequality and independence-implication undecidability, and from restricted semantic classes or a bounded-alphabet test.',
 'Recorded the co-recursively-enumerable upper bound and current method-specific inequality-generation progress without treating either as a decision algorithm.',
 'Preserved importance score 95 and required a complete Lean-checked decision algorithm or undecidability proof.',
]
sources=[
 'Read Hannula, Information Inequality Problem over Set Functions, ICDT 2024 Article 19: introduction p. 19:2 explicitly calls general decidability open; finite-valued entropy definitions §2.2 p. 19:3; validity and sparse rational binary input representation §2.3. It distinguishes entropic, polymatroidal, normal and monotone semantic domains.',
 'Read Abo Khamis–Kolaitis–Ngo–Suciu, Decision Problems in Information Theory, ICALP 2020 Article 106, §4.1 Theorems 5 and 7: monotone Boolean information constraints, hence individual unconditional inequalities, are co-recursively enumerable; entropic and almost-entropic validity agree for this form. This is not a proof of total decidability.',
 'Read the primary abstract and version metadata of Li, arXiv:2205.11461v3, last revised 29 May 2022, published in IEEE Transactions on Information Theory 69(6), June 2023. Its undecidability claims are network coding, conditional information inequalities and conditional-independence implication, not the single unconditional target.',
 'Read the primary abstract and revision history of Csirmaz, Exploring the entropic region, arXiv:2509.12439v2 of 28 September 2025: comparison of inequality-generation methods and their limitations, with further open questions.',
 'Read the primary abstract and metadata of E. P. Csirmaz–L. Csirmaz, Information Inequalities for Five Random Variables, arXiv:2512.23316v2 of 3 March 2026, extended from Computation 14(2), 42. The first nine generations and two infinite families concern the stated method; even its conjectured characterization is of that method rather than all inequalities.',
 f'Bounded primary-source checks through {DATE} found no verified resolution of exact unconditional validity. The finite-generation computations and all referenced proofs were not independently rerun or certified.',
]
complete(identifier,dict(
 title='Decidability of unconditional entropy inequalities',criterion='decision',question_type='yes_no',
 formal=r'''Does one deterministic Turing algorithm exist that always halts and decides the following problem? Its input is an integer \(n\ge1\) and rational coefficients \(a_S\) for the nonempty subsets \(S\subseteq[n]\). It must answer YES exactly when
\[
 \sum_{\varnothing\ne S\subseteq[n]}a_S H(X_S)\ge0
\]
holds for every joint distribution of \(n\) finite-valued discrete random variables. The finite alphabet sizes are unrestricted, and the inequality has no premises or affine constant.''',
 definitions=r'''Let \([n]=\{1,\ldots,n\}\). The input gives \(n\) in binary and a finite list of pairs \((S,a_S)\) with distinct nonempty subsets of \([n]\). A subset is encoded as an increasing list of its binary indices, and a coefficient as a signed binary integer numerator and a positive binary integer denominator. Missing subsets have coefficient zero. Zero coefficients and an empty coefficient list are allowed. All delimiters and list lengths are explicitly encoded; malformed inputs may be rejected. This is a finite rational input, with no real-number oracle or distribution description.

For the semantic validity test, independently quantify over every choice of positive integers \(r_1,\ldots,r_n\) and every joint probability mass function
\[
 p:\prod_{i=1}^n\{1,\ldots,r_i\}\longrightarrow[0,1],
 \qquad \sum_x p(x)=1.
\]
The probability values may be arbitrary real numbers. Let \(X_i\) be coordinate \(i\) of a tuple sampled from \(p\). For a nonempty \(S\subseteq[n]\), \(X_S\) is the tuple of coordinates with indices in \(S\), in increasing order. Its marginal mass function \(p_S\) is obtained by summing over the other coordinates. Define Shannon entropy in bits by
\[
 H(X_S)=-\sum_z p_S(z)\log_2 p_S(z),\qquad 0\log_2 0=0.
\]
All these sums are finite. An alphabet size may be one, and zero-probability outcomes are allowed. The integers \(r_i\) are quantified over, not bounded by the input or supplied to the deciding algorithm.

Validity means the displayed non-strict inequality holds for every such distribution. Invalidity means that at least one finite-alphabet distribution gives a strictly negative value. No numerical separation from zero is promised. In particular, valid inequalities can achieve equality, and a total decider must handle those boundary cases.

There are no assumptions of independence, conditional independence, functional dependence, prescribed marginals, bounded support or bounded alphabet size. Coefficients of either sign are allowed. The input expresses one homogeneous linear inequality with right-hand side zero. It does not express an implication with entropy constraints as premises, a Boolean combination of inequalities, a nonzero affine term or a nonlinear function of entropies.

The term entropy inequality here includes all universal linear inequalities in Shannon entropies. It is not restricted to the class often called Shannon-type inequalities, meaning those deducible by nonnegative combinations of the elementary conditional-entropy and conditional-mutual-information inequalities. Deciding membership in that narrower class is a different problem.

A decision algorithm is a single finite deterministic Turing program returning the correct YES or NO answer after finitely many steps on every valid finite encoding, for every input value of \(n\). No polynomial or other prescribed running-time or space bound is requested. Separate procedures for only finitely many values of \(n\), a semidecision procedure that may fail to halt, or an oracle for a noncomputable real quantity do not meet this definition.''',
 answer_criterion=r'''Give a complete Lean-checked construction of a total decision algorithm and a proof of its termination and exact semantic correctness for every input; or give a complete Lean-checked proof that the set of valid input inequalities is undecidable.

A new valid inequality, a counterexample to one candidate inequality, or an incomplete proof-generation procedure answers only individual instances. A procedure requiring a promised numerical gap, a fixed alphabet bound or a fixed number of variables is insufficient unless a proved effective reduction covers the full unrestricted problem. Undecidability for conditional inequalities or a richer input language does not settle this question without a valid reduction to this exact homogeneous unconditional form. There is no numerical approximation tolerance on the validity decision.''',
 source_formulation=dict(text='Hannula defines the information-inequality problem as validity over all finite-valued entropic functions and explicitly records its general decidability as open. The source uses rational binary coefficients and allows a sparse list of coefficient–subset pairs, while studying decidable restrictions separately.',caption='Paraphrase of Hannula, ICDT 2024 Article 19, introduction p. 19:2 and §§2.2–2.3, especially the input-representation and validity discussion.',citation='primary',format='editorial_paraphrase'),
 references=[
 ref('primary','Information Inequality Problem over Set Functions','Miika Hannula',2024,'https://doi.org/10.4230/LIPIcs.ICDT.2024.19','ICDT 2024 Article 19; introduction p. 19:2, finite-valued entropy §2.2, exact validity and sparse rational input representation §2.3'),
 ref('decision','Decision Problems in Information Theory','Mahmoud Abo Khamis; Phokion G. Kolaitis; Hung Q. Ngo; Dan Suciu',2020,'https://doi.org/10.4230/LIPIcs.ICALP.2020.106','ICALP 2020 Article 106; §4.1 Theorems 5 and 7, equality of entropic/almost-entropic validity for monotone formulas and co-recursive enumerability'),
 ref('li','Undecidability of Network Coding, Conditional Information Inequalities, and Conditional Independence Implication','Cheuk Ting Li',2023,'https://arxiv.org/abs/2205.11461v3','Preprint version 3, 29 May 2022; IEEE Transactions on Information Theory 69(6), June 2023; primary abstract identifies conditional targets'),
 ref('exploring','Exploring the entropic region','László Csirmaz',2025,'https://arxiv.org/abs/2509.12439v2','Version 2, 28 September 2025; primary abstract and metadata, inequality-generation methods and limitations'),
 ref('five','Information Inequalities for Five Random Variables','Előd P. Csirmaz; László Csirmaz',2026,'https://arxiv.org/abs/2512.23316v2','Version 2, 3 March 2026; extended version of Computation 14(2), Article 42; primary abstract describes nine generations and method-specific infinite families'),
 ],
 context_blocks=[
 block('Elementary Shannon inequalities supply a useful finite proof method at each number of variables, but do not characterize all valid entropy inequalities. Failure to obtain an elementary derivation is therefore not a proof of invalidity.'),
 block('Unconditional validity is known to be co-recursively enumerable. That upper classification does not supply a procedure that halts on every valid input, which is essential to this target.','decision'),
 block('Undecidability has been proved for conditional information inequalities and conditional-independence implication. Those problems permit exact premises, and deleting them changes the mathematical statement.','li'),
 block('The source obtains complexity classifications after changing the semantic domain or imposing syntactic restrictions. These results do not decide arbitrary inequalities over all finite-valued entropy vectors.'),
 block('Recent work derives infinite collections of additional inequalities and investigates generation methods. The 2026 five-variable enumeration concerns one such method; no completeness theorem for all unconditional inequalities is supplied.','five'),
 ],
 progress=[progress('2020','Unconditional validity is placed in the co-recursively-enumerable class.','decision'),progress('2023','The conditional-inequality undecidability theorem is published.','li'),progress('2024','The source explicitly retains general validity decidability as open and studies restricted cases.'),progress('2025-09-28','A revised study compares inequality-generation methods and their limitations.','exploring'),progress('2026-03-03','The extended five-variable paper records new infinite families and a method-specific enumeration.','five')],
),notes,sources,'The 2024 primary source explicitly records general unconditional entropy-inequality decidability as open. The known undecidability theorem permits conditional premises, while the inspected 2025–2026 work concerns inequality-generation methods and restricted families. Bounded primary-source checks through 17 September 2026 found no verified resolution of this exact unrestricted finite-alphabet target; cited proofs and computations were not independently certified.',summary=[
 'The input is one rational linear inequality involving the Shannon entropies of subsets of variables.',
 'It must be tested against every joint distribution on arbitrary finite alphabets, with no conditional premises.',
 'The question asks whether one algorithm can always halt and decide exact validity, including equality cases.',
 'Decidability for restricted inequalities and undecidability for conditional statements concern different problems.',
 'A complete Lean-checked answer must provide a total decision procedure or prove undecidability of this precise input language.',
],expected_sha256=claim['input_sha256'],claim_token=claim['token'])
