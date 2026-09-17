"""Review ordinary homogeneous versus unrestricted formula size over C."""
import sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT/'research/card-completion-20260913'))
from complete_review import complete,ref,block,progress
from review_queue import read_claims
identifier='TCS-6882';claim=read_claims(ROOT)[identifier]
notes=[
 'Recovered Open Problem 2 as a nonuniform superpolynomial separation for homogeneous outputs, with ordinary total degree rather than weighted degree.',
 'Asked an optional field clarification and, after continuing independent source and checkpoint work without a reply, announced the recommended complex-field default. This is an editorial specialization, not an explicit user confirmation.',
 'Specified division-free binary formula trees, arbitrary complex constants, all-node size, semantic homogeneity at every node and exact polynomial equality.',
 'Used a polynomial-size unrestricted family with no polynomial-size homogeneous family; wrote the infinitely-often quantifiers rather than silently imposing a stronger eventual lower bound.',
 'Read the 2024 weighted and quasi-homogeneous results and the final May 2026 Shpilka paper, including its factor-closure equivalence. Restricted-model tightness does not resolve this ordinary homogeneous target.',
 'Individually assessed importance, retained bounded source-open status and required a complete Lean-checked answer.',
]
sources=[
 'Read Shpilka–Yehudayoff, Arithmetic Circuits: A Survey of Recent Results and Open Questions, §2.2, Theorems 2.2–2.3 and Open Problem 2, printed pp.13–14 (PDF pp.18–19). The question concerns the cost of homogenizing formulas for homogeneous polynomials; the following paragraph separately reports a homogeneous-multilinear versus multilinear separation.',
 'Read Fournier–Limaye–Srinivasan–Tavenas, On the Power of Homogeneous Algebraic Formulas, ECCC TR23-191 manuscript associated with STOC 2024: abstract; Introduction pp.2–3; definitions §2; Theorem 4 p.5 and its discussion p.6; Theorem 5 and Corollary 6 p.6. The lower bound is for weighted homogeneity. The improved conversion depends on degree and depth, while quasi-homogeneity only bounds intermediate degree and is a different model.',
 'Downloaded and read the final publisher PDF of Shpilka, On Approximate Symmetric Polynomials and Tightness of Homogenization Results, Computational Complexity 35:5, DOI 10.1007/s00037-026-00286-x. The PDF says published online 7 May 2026. Read abstract, Theorems 1.1–1.3 pp.2–3, §1.1 pp.5–7, and §4 pp.21–23 including Question 4.1 and Theorem 4.2 (attributed to Spiizer 2025). This final version incorporates formula-factor closure, unlike the earlier ECCC TR25-053 version; it still poses homogeneous factor closure and separates multilinear/monotone tightness from general homogeneity.',
 'Bounded primary-source searches through 17 September 2026 did not identify a superpolynomial separation or polynomial homogenization theorem resolving the selected unrestricted-depth, ordinary-total-degree target over C. The cited proofs were not independently formalized or fully audited.',
]
complete(identifier,dict(
 status='source_open',criterion='resources',question_type='yes_no',
 formal=r'''Does there exist a family of homogeneous polynomials \(f_n\in\mathbb C[x_1,\ldots,x_n]\), indexed by integers \(n\ge2\), and an integer \(a\ge1\), such that
\[
\operatorname{F}(f_n)\le n^a\qquad\text{for every }n\ge2,
\]
but
\[
\forall k\ge1\ \forall N\ge2\ \exists n\ge N:
\operatorname{HF}(f_n)>n^k?
\]
Here \(k,N,n\) are integers, \(\operatorname{F}\) is unrestricted arithmetic formula size and \(\operatorname{HF}\) is homogeneous arithmetic formula size over \(\mathbb C\), as defined below. In other words, can homogeneous outputs have polynomial-size general formulas but no polynomial-size homogeneous formulas?''',
 definitions=r'''An arithmetic formula over \(\mathbb C\) is a finite rooted binary tree. Each leaf is labeled by one input variable or an arbitrary complex constant. Each internal node applies either addition or multiplication to its two children. The polynomial at a node is computed recursively in the commutative polynomial ring \(\mathbb C[x_1,\ldots,x_n]\). There are no division gates, tests, limits or approximation operations. Negative constants allow subtraction to be expressed using these gates. Equality of outputs means equality as formal polynomials, including all coefficients.

The size is the total number of nodes, including variable and constant occurrences. Each repeated use of a subexpression needs a separate copy of its tree; intermediate computations cannot be shared. Fan-in is two, and there is no depth bound. Complex constants count as single leaves, irrespective of their description length. This is an algebraic size question, not a bit-complexity or evaluation-accuracy question.

The ordinary total degree of a monomial \(x_1^{e_1}\cdots x_n^{e_n}\) is \(\sum_i e_i\). A nonzero polynomial is homogeneous when all its nonzero monomials have the same total degree. The zero polynomial is considered homogeneous. All variables have weight one. A formula is homogeneous when the actual polynomial computed at every node is homogeneous; its output is therefore homogeneous as well. Neither multilinearity nor monotonicity is required. In particular, powers of variables and negative or nonreal coefficients are allowed at intermediate nodes.

For any polynomial \(f\), \(\operatorname{F}(f)\) is the minimum size of a formula computing it. For homogeneous \(f\), \(\operatorname{HF}(f)\) is the minimum size among homogeneous formulas. Both minima exist, since a finite monomial expansion gives a formula, and homogeneous monomials of a fixed degree can be added homogeneously. The family need not use every named variable. Its output degrees may grow with \(n\); the bound on ordinary formula size already bounds them polynomially because a binary formula cannot create a degree larger than its number of variable leaves.

The comparison is nonuniform: different formulas and constants may be chosen for each \(n\), and no efficient algorithm generating the family or its formulas is required. The same fixed field \(\mathbb C\) is used on both sides. The second displayed condition means that the minimum homogeneous sizes are not bounded by any polynomial in \(n\). It asks for arbitrarily large violating indices for each fixed exponent, not an eventual \(n^{\omega(1)}\) lower bound at every index.''',
 answer_criterion=r'''Give a complete mathematically correct Lean-checked proof of the existence statement or its logical negation. A positive answer must establish a polynomial-size unrestricted formula family and superpolynomial homogeneous formula size for the same homogeneous outputs over \(\mathbb C\). No additional constructive uniformity is required, but the family and both size claims must be defined and proved.

A negative answer must prove that every family of homogeneous polynomials with polynomial-size unrestricted formulas also has polynomial-size homogeneous formulas. It need not provide an efficient algorithm that finds the latter formulas. A lower bound only for homogeneous multilinear formulas, monotone formulas, weighted-homogeneous formulas or bounded-depth formulas does not establish this separation. A polynomial-size quasi-homogeneous formula whose intermediate polynomials mix degrees does not disprove it.''',
 why='Homogenization is a central bridge between restricted algebraic lower bounds and general formula complexity. A superpolynomial separation would show that insisting on a single degree at every intermediate computation loses essential power, even when the final polynomial is homogeneous.',
 importance=dict(score=85,method='editorial',assessed_on='2026-09-17',reason='A core structural comparison in algebraic formula complexity, directly testing the scope of homogenization-based lower-bound methods beyond bounded-depth and multilinear restrictions.'),
 source_formulation=dict(text='The survey asks whether homogeneous formulas are superpolynomially weaker than unrestricted formulas. The card fixes complex coefficients and expresses the comparison as a nonuniform family separation for homogeneous outputs with ordinary total degree.',caption='Shpilka–Yehudayoff, §2.2, Open Problem 2, printed p.14 (PDF p.19); the field choice is an editorial specialization.',citation='primary',format='editorial_paraphrase'),
 references=[
 ref('primary','Arithmetic Circuits: A Survey of Recent Results and Open Questions','Amir Shpilka; Amir Yehudayoff',2010,'https://www.cs.tau.ac.il/~shpilka/publications/SY10.pdf','§2.2, Theorems 2.2–2.3 and Open Problem 2, printed pp.13–14 (PDF pp.18–19)'),
 ref('power','On the Power of Homogeneous Algebraic Formulas','Hervé Fournier; Nutan Limaye; Srikanth Srinivasan; Sébastien Tavenas',2024,'https://eccc.weizmann.ac.il/report/2023/191/','STOC 2024 paper; ECCC manuscript, Introduction pp.2–3, §2, Theorems 4–5 and Corollary 6 pp.5–6'),
 ref('tightness','On Approximate Symmetric Polynomials and Tightness of Homogenization Results','Amir Shpilka',2026,'https://doi.org/10.1007/s00037-026-00286-x','Final journal version, published online 7 May 2026; Theorems 1.1–1.3, §1.1, §4 pp.21–23 and Theorem 4.2'),
 ],
 context_blocks=[
 block('Ordinary arithmetic formulas can mix terms of different degrees and cancel unwanted terms later. Homogeneous formulas keep each intermediate polynomial at a single degree. The question asks whether this restriction can require more than every polynomial increase in size.'),
 block('Circuits can share the components created by a homogenization procedure, while a formula has to duplicate each reused subexpression. Efficient homogenization of circuits therefore does not automatically provide efficient homogenization of formulas.'),
 block('The 2024 work proves lower bounds for weighted homogeneity and improves conversion bounds for ordinary homogeneity in certain degree and depth regimes. Its quasi-homogeneous conversion permits intermediate mixtures of degrees, so it does not identify the two classes on this card.','power'),
 block('The final 2026 paper proves tightness results with additional multilinear or monotone requirements. Its discussion still asks about homogeneous factor closure and records an equivalence with polynomial-overhead formula homogenization. These results sharpen the surrounding landscape without resolving the ordinary homogeneous comparison.','tightness'),
 ],
 progress=[progress('2010','The survey poses the superpolynomial formula separation and records efficient low-degree homogenization.'),progress('2024','Weighted-homogeneous lower bounds and improved ordinary or quasi-homogeneous conversion bounds are established in distinct models.','power'),progress('2026-05-07','The final journal version gives restricted-model tightness results and records the factor-closure equivalence while retaining the homogeneous closure question.','tightness')],
),notes,sources,'Source-open over the selected complex field. The final May 2026 primary paper still poses the related homogeneous factor-closure question and distinguishes its multilinear/monotone tightness results from unrestricted homogeneous formulas. Bounded checks through 17 September 2026 found no resolution of the selected ordinary-total-degree, unbounded-depth family separation; they do not certify exhaustive current openness.',summary=[
 'A homogeneous polynomial has all its nonzero monomials at one ordinary total degree.',
 'The question compares arbitrary complex arithmetic formula trees with trees whose every intermediate polynomial is homogeneous.',
 'It asks for outputs with polynomial-size general formulas but no polynomial-size homogeneous formulas.',
 'Weighted homogeneity, multilinearity, monotonicity and bounded depth impose different restrictions and their lower bounds do not settle this target.',
 'The requested answer is a complete Lean-checked nonuniform family separation or proof that polynomial formula size always survives homogenization.',
],expected_sha256=claim['input_sha256'],claim_token=claim['token'])
