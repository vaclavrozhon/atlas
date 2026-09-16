"""Recover the uniform nondeterministic tautology target, with exact acceptance."""
import sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT/'research/card-completion-20260913'))
from complete_review import complete,ref,block,progress
from review_queue import read_claims
identifier='TCS-0562'
claim=read_claims(ROOT)[identifier]
notes=[
 'Recovered Problem 3 and Hypothesis 5, including the DNF-tautology rather than CNF-satisfiability acceptance convention.',
 'Expanded refutation as one positive exponent saving for every fixed clause width; the machine and polynomial overhead may depend on width.',
 'Fixed the uniform nondeterministic multitape Turing interpretation of the original NTIME statement, with all branches time-bounded and no random verifier.',
 'Used the same explicit formula encoding and variable-count convention as the reviewed deterministic SETH card.',
 'Corrected the column publication year from the inherited 2017 label to December 2018 using publisher-deposited Crossref metadata.',
 'Preserved the existing importance assessment; separated the 2026 conditional circuit consequences and the known randomized-verifier results from an NSETH refutation.',
]
sources=[
 'Read Vassilevska Williams, Some Open Problems in Fine-Grained Complexity, author/editor-hosted PDF: computational-model paragraph p. 3; Problem 3 and Hypothesis 5 p. 4; bibliography entry 28. Checked DOI 10.1145/3300150.3300158 through the Crossref API: SIGACT News 49(4):29–35, published 15 December 2018. The editor’s older index labels this column under 2017; the publication record is used for the reference.',
 'Read Carmosino–Gao–Impagliazzo–Mihajlin–Paturi–Schneider, ITCS 2016 pp. 261–270, author-hosted published PDF: first-page NSETH definition, §3 Turing reductions and §4 circuit consequences. The NTIME convention supplies the uniform machine model; no equivalence to every literal short-address RAM convention is asserted.',
 'Read Chukhin–Kulikov–Mihajlin–Smirnova, STACS 2026 Article 28: abstract, introduction, §1.2 Theorem 1 and Corollary 2, and §2.3 p. 10 Theorem 11. The results give conditional and disjunctive circuit lower bounds, not a truth value for NSETH. Full proofs were not independently certified.',
 'Bounded primary-source search through 16 September 2026 found continued uses and consequences of NSETH, without a general nondeterministic algorithm or proof resolving the stated hypothesis. Faster Merlin–Arthur verification explicitly uses randomness and does not meet this model.',
]
status=('The checked source asks to refute NSETH, and the STACS 2026 work still treats it as an assumption while deriving circuit consequences from either outcome. '
 'No resolution of the uniform nondeterministic hypothesis was found in the bounded later-work check. This does not independently certify current openness or any cited proof.')
complete(identifier,dict(
 title='Nondeterministic Strong Exponential Time Hypothesis',year=2018,
 criterion='resources',question_type='yes_no',
 formal=r'''Is the Nondeterministic Strong Exponential Time Hypothesis false? Precisely, is there a real constant \(\varepsilon\in(0,1)\) such that, for every integer \(k\ge3\), there are a uniform nondeterministic machine \(M_k\) and integers \(C_k\ge1,d_k\ge0\) with the following properties?

For every \(k\)-CNF formula \(F\), \(M_k\) has an accepting computation if and only if \(F\) is unsatisfiable, and every computation branch halts within
\[
C_k\,2^{(1-\varepsilon)n(F)}(L(F)+1)^{d_k}
\]
steps. Here \(n(F)\) is the number of distinct variables, \(L(F)\) is the explicit binary input length, and the machine model is defined below.

The same positive saving \(\varepsilon\) must work for every fixed width \(k\). The machine and its constants may depend on \(k\) and \(\varepsilon\), but not on the individual input. The negation of this displayed existence statement is NSETH itself.''',
 definitions=r'''A \(k\)-CNF formula is an AND of a finite list of clauses, each an OR of at most \(k\) literals. Each literal is either \(x_i\) or \(\neg x_i\). The distinct variables that occur are exactly \(x_1,\ldots,x_n\). A Boolean assignment satisfies the formula when it satisfies every clause. An empty clause is false; an empty conjunction is true and has \(n=0\). Repeated clauses, repeated literals and clauses containing both signs of a variable are permitted. There is no promise of a sparse formula, bounded occurrences, a unique assignment or a distribution on inputs.

Use the following binary encoding. For \(a\ge0\), let \(b\) be the bit length of \(a+1\), and let \(\operatorname{code}(a)\) be \(1^b0\) followed by the \(b\)-bit binary expansion of \(a+1\). Encode \(n\), the number of clauses, and then each clause's length with this code. After each clause length, list its literals; encode a literal by its sign bit, zero for positive and one for negative, followed by \(\operatorname{code}(i)\). Require all indicated lists to be complete, \(1\le i\le n\), every declared variable to occur, no trailing bits, and width at most \(k\). Let \(L(F)\) be the complete encoding length. The polynomial factor in \(L\) accounts for arbitrarily many explicitly repeated clauses.

A machine has one fixed finite program, a fixed finite number of tapes and fixed finite tape alphabets. The read-only input tape initially contains the encoding followed by an end marker; work tapes are initially blank. Tape cells are indexed by nonnegative integers, all heads initially occupy cell zero, and a left move at zero leaves the head there. Each transition reads or writes only cells under the heads and moves each head by at most one cell. A transition can choose nondeterministically between at most two possibilities. The runtime counts all transitions, including parsing, input access, generating choices and internal computation. There is no advice, random source, quantum operation, oracle or unit-cost arithmetic on unbounded integers.

For an unsatisfiable valid formula, at least one branch must accept. For a satisfiable formula, every branch must reject. Every branch on every valid formula must halt within the stated bound, including rejecting branches. All branches reject malformed strings in polynomial time in their length. A choice sequence is an existential certificate; no probability of choosing it is required. There is no restriction to certificates from a particular propositional proof system.

The machine is uniform over all input lengths at its fixed \(k\). The quantifiers permit separate machines for different widths and do not demand a computable procedure producing \(M_k\) from \(k\). Finite exceptional input lengths may be absorbed by increasing \(C_k\).

Equivalently, complement every literal and interchange AND and OR to obtain the \(k\)-DNF formula \(\neg F\). The input \(F\) is unsatisfiable exactly when this \(k\)-DNF is true on every assignment. This is the source's \(k\)-TAUT language; the transformation preserves the number of variables and has polynomial encoding overhead.

The card instantiates the original paper's \(\mathrm{NTIME}\) formulation with the standard multitape model. The later open-problem column also has a general logarithmic-word RAM convention; equivalence to every literal short-address interpretation of that convention is not assumed. Polynomial encoding and simulation overheads in the stated Turing setting may be absorbed using a smaller fixed positive exponent saving.''',
 answer_criterion=r'''Supply a complete Lean-checked proof or refutation of the existence statement in the formal question. An affirmative answer establishes one \(\varepsilon>0\), the required machines for all fixed \(k\), exact existential acceptance of unsatisfiable inputs, and the time bound on every branch. A negative answer proves NSETH with the opposite quantifiers. An improvement for only one width, a width-dependent saving that tends to zero, a randomized-verifier protocol, or a lower bound for one restricted proof system is insufficient. This is a binary asymptotic proposition; numerical \(1/100\) tolerance does not modify the exponent or acceptance condition.''',
 source_formulation=dict(text='Problem 3 asks whether NSETH can be refuted; Hypothesis 5 states the quantified nondeterministic time barrier for bounded-width DNF tautologies.',
 caption='Paraphrase of the author/editor-hosted column, PDF p. 4, Problem 3 and Hypothesis 5; published in SIGACT News 49(4), December 2018.',
 citation='primary',format='editorial_paraphrase'),
 why='A nondeterministic computation can guess a certificate that a formula has no satisfying assignment, but it must verify that certificate without random errors. A uniform exponential saving would change the limits of fine-grained reductions and would have consequences for circuit lower bounds. The question therefore tests a barrier that is stronger than the difficulty of finding a satisfying assignment deterministically.',
 references=[
 ref('primary','Some Open Problems in Fine-Grained Complexity','Virginia Vassilevska Williams',2018,
 'https://www.cs.umd.edu/~gasarch/open/finegrain.pdf',
 'Problem 3 and Hypothesis 5, PDF p. 4; SIGACT News 49(4):29–35, published 15 December 2018; DOI 10.1145/3300150.3300158'),
 ref('original','Nondeterministic Extensions of the Strong Exponential Time Hypothesis and Consequences for Non-reducibility',
 'Marco L. Carmosino; Jiawei Gao; Russell Impagliazzo; Ivan Mihajlin; Ramamohan Paturi; Stefan Schneider',2016,
 'https://people.csail.mit.edu/virgi/6.1420/papers/nseth.pdf',
 'ITCS 2016, pp. 261–270; NSETH definition p. 261, §3 Turing reductions and §4 circuit consequences; DOI 10.1145/2840728.2840746'),
 ref('later','Conditional Complexity Hardness: Monotone Circuit Size, Matrix Rigidity, and Tensor Rank',
 'Nikolai Chukhin; Alexander S. Kulikov; Ivan Mihajlin; Arina Smirnova',2026,
 'https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.STACS.2026.28',
 'STACS 2026, Article 28; §1.2 Theorem 1 and Corollary 2, §2.3 p. 10 Theorem 11'),
 ],
 context_blocks=[
 block('Guessing a satisfying assignment already solves CNF-SAT nondeterministically in polynomial time. NSETH concerns certificates for the opposite answer, so replacing unsatisfiability by satisfiability would trivialize the target.','original'),
 block('The hypothesis allows algorithms for each fixed width to improve on exhaustive search. It excludes a single positive saving that remains available across all fixed widths.'),
 block('NSETH implies deterministic SETH in the same machine convention: a fast deterministic decision algorithm could have its output complemented. Refuting NSETH alone need not refute deterministic SETH.','original'),
 block('The original paper derives barriers to deterministic fine-grained reductions from SAT to problems such as 3SUM and all-pairs shortest paths. These are conditional non-reducibility results.','original'),
 block('The source notes fast Merlin–Arthur and Arthur–Merlin protocols for related tasks. Their use of random verification is essential to the distinction from the nondeterministic target.'),
 block('The STACS 2026 paper obtains consequences from NSETH and combines them with consequences of its negation. A theorem that guarantees a circuit lower bound in either case does not decide which case holds.','later'),
 ],
 progress=[
 progress('2016','Carmosino and coauthors introduce NSETH and its non-reducibility and circuit-complexity consequences.','original'),
 progress('2018-12-15','The published open-problem column explicitly asks for a refutation.'),
 progress('2026','STACS work develops further conditional circuit consequences while retaining NSETH as an assumption.','later'),
 progress('2026-09-16','The review fixes the acceptance direction, width quantifiers and uniform time model; no general resolution is found in the bounded check.'),
 ],
 related_problem_ids=['TCS-6595','TCS-6935'],
),notes,sources,status,summary=[
 'NSETH asks whether certifying unsatisfiability remains close to exhaustive search even with nondeterministic choices.',
 'The requested refutation needs one positive saving in the exponent for every fixed clause width.',
 'Each unsatisfiable formula must have an accepting branch, while every branch on a satisfiable formula must reject.',
 'The running-time guarantee applies to every branch of a uniform machine and includes polynomial input-processing overhead.',
 'Known randomized-verifier protocols and conditional circuit lower bounds do not settle this exact nondeterministic question.',
],expected_sha256=claim['input_sha256'],claim_token=claim['token'])
