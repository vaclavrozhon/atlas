"""Complete the deterministic positive-exponent ETH-to-Gap-ETH implication."""
import sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];sys.path.insert(0,str(ROOT/'research/card-completion-20260913'))
from complete_review import complete,ref,block,progress,DATE
from review_queue import read_claims
identifier='TCS-7313';claim=read_claims(ROOT)[identifier]
notes=[
 'Preserved the implication target and deterministic positive-exponent conventions, avoiding an unannounced switch to a single subexponential algorithm or randomized hardness.',
 'Expanded both hypotheses through fast-algorithm predicates with a fixed bit-machine model, explicit formula encoding and polynomial factors uniform in input size.',
 'Made the sparse promise, perfect completeness, clause multiplicities, empty formulas, and unrestricted answers outside the gap explicit.',
 'Recorded that negating the implication requires ETH together with the failure of every fixed sparse constant-gap exponential lower bound; an oracle separation or reduction barrier alone is insufficient.',
 'Read the December 2025 revision of the source and distinguished dense MAXLIN, ETH-implied PIH, quasi-linear PCP size and April 2026 lattice consequences from sparse gap 3-SAT.',
 'Preserved importance 93 and category, filtered only inactive related links by active-file existence, and required a complete Lean-checked proof.',
]
sources=[
 'Read Bitansky–Harsha–Ishai–Rothblum–Wu, ECCC TR24-114 original report and Revision 2 of 30 December 2025: Section 1.1.2, Section 3.3 and Section 6. The source explicitly distinguishes dense MAXLIN hardness from local MAX-kLIN and says ETH implying Gap-ETH is a longstanding open problem. The source uses an exponential-rate hypothesis; the card retains its already explicit deterministic interpretation.',
 'Read Guruswami–Lin–Ren–Sun–Wu, Parameterized Inapproximability Hypothesis under ETH, JACM 72(5), Article 32, October 2025, primary journal text: Theorem 1.2 establishes ETH implies PIH and Theorem 1.3 gives a parameterized PCP with a large alphabet. This is not the sparse Boolean constant-gap 3-CNF assertion.',
 'Read Bafna–Minzer–Vyas–Yun, Quasi-Linear Size PCPs with Small Soundness from HDX, STOC 2025, primary MIT repository abstract. Its ETH consequence retains a polylogarithmic loss in the exponent; the quasi-linear proof-size statement does not assert the linear-size gap reduction needed to directly transfer a positive exponential rate.',
 'Read Aggarwal–Gupta–Morolia–Zhang, arXiv:2504.02695v2, revised 21 April 2026, primary abstract: the deterministic CVP consequence and randomized SVP consequence build on dense MAXLIN. They concern lattice problems, not the unrestricted ETH-to-Gap-ETH implication. Full proofs not independently audited.',
 f'Bounded primary-source searches through {DATE} found no verified resolution of the selected deterministic implication. A result replacing Gap-ETH by ETH for a particular application was not treated as equivalence of the hypotheses.',
]
complete(identifier,dict(
 criterion='assumptions',question_type='yes_no',
 formal=r'''Is the implication
\[
 \mathsf{ETH}_{\mathrm{det}}\ \Longrightarrow\quad
 \mathsf{GapETH}_{\mathrm{det}}
\]
true for the following precise hypotheses?
\[
\begin{aligned}
 \mathsf{ETH}_{\mathrm{det}}
   &:\quad \exists\eta\in\mathbb Q_{>0}\ 
           \neg\operatorname{FastSAT}(\eta),\\
 \mathsf{GapETH}_{\mathrm{det}}
   &:\quad \exists B\in\mathbb N_{\ge1}\ 
           \exists\delta\in\mathbb Q\cap(0,1)\ 
           \exists\eta\in\mathbb Q_{>0}\ 
           \neg\operatorname{FastGapSAT}(B,\delta,\eta).
\end{aligned}
\]
The fast-algorithm predicates below use deterministic bit computation, exponent parameter equal to the number of variables, and a fixed polynomial factor in the whole binary input length. The gap predicate concerns formulas with at most \(Bn\) clauses and the promise of full satisfiability or value at most \(1-\delta\).''',
 definitions=r'''A 3-CNF formula \(F\) is a finite list of clauses on Boolean variables \(x_1,\ldots,x_n\), each clause being a disjunction of at most three signed variables. The indices are in \(\{1,\ldots,n\}\), and each of these variables occurs somewhere unless \(n=0\). Clauses and literals may repeat, and tautological and empty clauses are allowed. Satisfiability means that one assignment makes every clause true. A list with no clauses is satisfiable, while an empty clause is false under every assignment.

For definiteness, encode a nonnegative integer \(z\) by \(1^t0\operatorname{bin}(z)\), where \(\operatorname{bin}(0)=0\) and \(t\) is the length of the usual binary expansion. The input contains the codes of \(n\) and the clause count \(m\), then each clause length in \(\{0,1,2,3\}\) followed by its literals, each a sign bit and a coded positive variable index. There is no trailing data. The full encoded length is \(L\); the exponent parameter is \(n\), not \(L\) or \(m\). The variable-naming convention prevents a large binary index from declaring unused variables. Invalid encodings are outside the mathematical input domain.

For \(m>0\), define
\[
 \operatorname{val}(F)=
 \max_{z\in\{0,1\}^n}
 \frac{\#\{j\in\{1,\ldots,m\}:\text{clause }j\text{ is true under }z\}}{m}.
\]
Clause occurrences are counted with their multiplicities. Put \(\operatorname{val}(F)=1\) when \(m=0\). Thus \(\operatorname{val}(F)=1\) is precisely satisfiability, including the empty conjunction.

For a fixed rational \(\eta>0\), \(\operatorname{FastSAT}(\eta)\) means that there exist a single deterministic Turing machine \(A\), a constant \(K>0\) and an integer \(d\ge1\) such that, for every valid formula \(F\), the machine halts within
\[
 K2^{\eta n}(L+1)^d
\]
bit operations and returns 1 exactly when \(F\) is satisfiable, returning 0 otherwise. There is no bound on the clause count in this predicate. The existential machine and constants may depend on \(\eta\), but not on \(n,m,L\) or the particular input.

For fixed \(B\ge1\), \(0<\delta<1\) and \(\eta>0\), \(\operatorname{FastGapSAT}(B,\delta,\eta)\) means that there exist a single deterministic machine \(A\), a constant \(K>0\) and an integer \(d\ge1\) with the same displayed bit-time bound on every valid formula with \(m\le Bn\). It must return 1 when \(\operatorname{val}(F)=1\) and 0 when \(\operatorname{val}(F)\le1-\delta\). For formulas strictly between those values, either answer is allowed, but the time bound still holds. There is no required behavior for valid formulas violating \(m\le Bn\). The fixed parameters \(B,\delta,\eta\) specify which algorithm is under discussion and are not additional variable input parameters. The machine and its polynomial factors may depend on them, but not on a formula.

All machines are uniform classical deterministic bit machines with finite programs, no advice, no oracle, no random bits and no quantum operations. Input processing, intermediate computation and output are charged. In each predicate the polynomial exponent and multiplicative constant are fixed independently of input size. The assertion of a positive exponential lower-bound rate means that at least one fixed positive \(\eta\) admits no such algorithm; it does not merely rule out one chosen algorithm. Restricting the fixed rate and gap constants to rational values and the density bound to integers does not change these existential positive-rate conventions.

The implication is between these particular mathematical propositions. It does not assert either hypothesis separately, and it does not request a proof specifically by a chosen reduction. It retains a perfectly satisfiable YES case. Randomized hypotheses, other completeness thresholds, other computational models and hardness of other approximation problems are not substituted without a proof connecting them to these definitions.''',
 answer_criterion=r'''Give a complete Lean-checked proof of the displayed implication, with no unproved premise besides its stated antecedent, or a complete Lean-checked proof of its logical negation.

The negation is \(\mathsf{ETH}_{\mathrm{det}}\) together with \(\neg\mathsf{GapETH}_{\mathrm{det}}\). Under the definitions above the latter says that, for every fixed \(B\in\mathbb N_{\ge1}\), rational \(\delta\in(0,1)\) and rational \(\eta>0\), \(\operatorname{FastGapSAT}(B,\delta,\eta)\) holds. Different fixed parameters may have different uniform machines and polynomial factors; no effective compiler from these parameters to programs is demanded. Ruling out one reduction method or giving a relativized separation does not prove this unrelativized negation.

An ETH-based lower bound for a different gap problem, a parameterized inapproximability theorem, or a PCP construction with a superlinear increase that loses the required positive exponential rate does not by itself prove the implication. If a reduction is used, its completeness, soundness, size, running time and deterministic conventions must suffice for the exact hypotheses here. Further unproved assumptions establish only a more conditional statement.''',
 source_formulation=dict(text='The dot-product-proof paper obtains ETH-based exponential approximation hardness for dense linear-equation constraints and explicitly distinguishes that result from the open implication ETH ⇒ Gap-ETH for local constraint problems. The card isolates the deterministic implication with fixed positive exponential rates and sparse 3-CNF inputs on the gap side.',caption='Paraphrase of Bitansky et al., Section 1.1.2 and Section 3.3, ECCC TR24-114 Revision 2.',citation='primary',format='editorial_paraphrase'),
 references=[
 ref('primary','Dot-Product Proofs and Their Applications','Nir Bitansky; Prahladh Harsha; Yuval Ishai; Ron D. Rothblum; David J. Wu',2025,'https://eccc.weizmann.ac.il/report/2024/114/revision/2/','Revision 2, 30 December 2025; Section 1.1.2, Section 3.3 and Section 6; original report 2024'),
 ref('pih','Parameterized Inapproximability Hypothesis under ETH','Venkatesan Guruswami; Bingkai Lin; Xuandi Ren; Yican Sun; Kewen Wu',2025,'https://doi.org/10.1145/3749982','JACM 72(5), Article 32, October 2025; Theorems 1.2 and 1.3; STOC 2024 conference version'),
 ref('pcp','Quasi-Linear Size PCPs with Small Soundness from HDX','Mitali Bafna; Dor Minzer; Nikhil Vyas; Zhiwei Yun',2025,'https://dspace.mit.edu/entities/publication/9bbf3cdb-ea42-4d50-8d98-7b0f2c30432e','STOC 2025, pp. 45–53; abstract, ETH consequence with a polylogarithmic loss in the exponent'),
 ref('lattice','Mind the Gap? Not for SVP Hardness under ETH!','Divesh Aggarwal; Rishav Gupta; Aditya Morolia; Chuanqi Zhang',2026,'https://arxiv.org/abs/2504.02695v2','21 April 2026 revision; abstract, deterministic CVP reduction and randomized SVP reduction from MAXLIN-based consequences'),
 ],
 why='The implication would show that exponential hardness of exact satisfiability already supplies the sparse constant-gap hardness used in many fine-grained approximation lower bounds.',
 context_blocks=[
 block('Exact satisfiability permits an unsatisfiable formula whose assignments each violate only a tiny fraction of clauses. The gap hypothesis asks for exponential hardness even when the NO instances have a fixed positive fraction of unavoidable violations.'),
 block('The dot-product-proof result removes the need for a gap assumption in a dense linear-equation approximation problem. The source expressly distinguishes that accomplishment from establishing Gap-ETH for sparse local constraints.'),
 block('ETH is known to imply the Parameterized Inapproximability Hypothesis. Its parameterized constraint model and alphabet bounds do not yield the particular sparse Boolean exponential-rate assertion on this card.','pih'),
 block('The quasi-linear-size PCP construction gives strong ETH-based approximation consequences, but its stated bound retains a polylogarithmic loss in the exponent.','pcp'),
 block('The April 2026 lattice work obtains further consequences from dense MAXLIN, distinguishing deterministic and randomized reductions. These are results for specific applications, not a proof that the two general hypotheses coincide.','lattice'),
 ],
 progress=[progress('2024','Dot-product proofs give ETH-based hardness for dense MAXLIN while distinguishing the ETH-to-Gap-ETH question.'),progress('2025-06-15','The quasi-linear PCP construction improves size-efficient approximation hardness with a remaining polylogarithmic exponent loss.','pcp'),progress('2025-10','The JACM version proves ETH implies PIH in the parameterized setting.','pih'),progress('2025-12-30','The revised dot-product-proof source retains the distinction between its dense consequence and Gap-ETH.'),progress('2026-04-21','The revised lattice paper gives further ETH-based consequences through MAXLIN.','lattice')],
 related_problem_ids=[i for i in ['TCS-0734','TCS-1945','TCS-2662','TCS-6593','TCS-6595','TCS-6738','TCS-6935','TCS-7268'] if (ROOT/'data/cards'/f'{i}.json').exists()],
),notes,sources,'The bounded source check through 17 September 2026 found no verified resolution of the deterministic positive-exponent ETH-to-sparse-Gap-ETH implication. The December 2025 source explicitly retains the distinction; ETH-implied PIH, quasi-linear PCPs and April 2026 lattice consequences have different models or quantitative guarantees. Full proofs of the later results were not independently audited.',summary=[
 'ETH asserts a fixed positive exponential-time lower bound for exact 3-SAT.',
 'The selected Gap-ETH asserts such a lower bound for sparse formulas promised to be satisfiable or to leave a fixed fraction of clauses unsatisfied under every assignment.',
 'The question asks whether the deterministic exact hypothesis implies this deterministic gap hypothesis.',
 'All exponential rates and polynomial input-length factors have explicit quantifiers, and the YES case requires perfect satisfiability.',
 'A complete Lean-checked resolution must establish the implication or its actual logical negation, rather than hardness for a different approximation problem.',
],expected_sha256=claim['input_sha256'],claim_token=claim['token'])
