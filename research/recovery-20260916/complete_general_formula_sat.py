"""Specify a fixed exponential saving for unrestricted explicit Boolean formulas."""
import sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT/'research/card-completion-20260913'))
from complete_review import complete,ref,block,progress
from review_queue import read_claims
identifier='TCS-6974';claim=read_claims(ROOT)[identifier]
notes=[
 'Replaced the unquantified phrase beat exhaustive search by one fixed positive saving in the variable exponent, with an explicit polynomial input-length factor.',
 'Presented fixed-exponent and weaker superpolynomial-factor targets as an optional scope question; after time for a reply, proceeded with the announced recommended default. No explicit user confirmation is claimed.',
 'Defined general Boolean formulas as explicit trees over AND, OR, NOT and constants, allowing repeated variables and unrestricted size and depth.',
 'Fixed the number of occurring variables, full binary syntax, deterministic Turing bit-time and exact correctness on every formula.',
 'Separated restricted-size counting algorithms and conditional algorithm-to-lower-bound theorems from a solution of the chosen unrestricted decision target.',
 'Retained any positive exponent improvement rather than imposing an arbitrary one-hundredth threshold.',
 'Individually assessed significance, linked the relevant distinct SAT questions and required a complete Lean-checked binary answer.',
]
sources=[
 'Read Fortnow, The Status of the P versus NP Problem, 2009 author PDF https://lance.fortnow.com/papers/files/pnp-cacm.pdf, Section 5.1, PDF p.3. The passage distinguishes general Boolean formula satisfiability from restricted SAT instances but gives no quantified saving or machine model. The fixed-saving deterministic bit-time target is an explicit editorial specification, not a quotation of a precise theorem or conjecture in that passage.',
 'Read Tal, #SAT Algorithms from Shrinkage, ECCC TR15-114, published 18 July 2015: abstract, Section 1 and Theorem 1.1. For sufficiently small fixed eta>0 it gives deterministic counting in 2^{n-n^eta} poly(n) time for de Morgan formulas with at most n^{3-16eta} leaves. Both its size restriction and sublinear saving in the exponent distinguish it from the selected target.',
 'Read Bathie–Williams, Towards Stronger Depth Lower Bounds, ITCS 2024, DOI 10.4230/LIPIcs.ITCS.2024.10, published 24 January 2024: abstract and Introduction pp.10:2–10:3, Theorem 1.1. This states a conditional consequence of improved subcubic-size #SAT algorithms for formula lower bounds. It is not an algorithm for all formulas or an unconditional impossibility theorem for this target.',
 'Bounded primary-source searches through 17 September 2026 checked the general-formula target and recent SAT/formula work; no verified resolution was found. Recent bounded-occurrence CNF and proof-system results do not automatically transfer to this unrestricted formula question. This check does not purport to enumerate all recent SAT algorithms.',
 'The deterministic SETH relation is a scope implication: every fixed-width CNF is an explicitly represented AND/OR/NOT formula with the same occurring variables and polynomial encoding overhead. Thus a positive result would refute deterministic SETH, but assuming SETH is not a proof of the requested unconditional negative answer.',
]
complete(identifier,dict(
 title='General Formula-SAT with a fixed exponential saving',criterion='resources',question_type='yes_no',
 importance=dict(score=91,method='editorial',reason='A fixed saving for arbitrary Boolean formulas would substantially improve a basic NP-complete search problem and refute deterministic SETH, going beyond algorithms exploiting bounded width, density or small formula size.'),
 formal=r'''Do there exist a rational constant \(\varepsilon\in(0,1)\), constants \(K\ge1\), an integer \(d\ge1\), and one uniform deterministic algorithm \(A\) such that every explicitly given Boolean formula \(F\) over AND, OR and NOT is correctly decided for satisfiability in at most
\[
K\,2^{(1-\varepsilon)n(F)}\bigl(L(F)+1\bigr)^d
\]
Turing-machine bit steps? Here \(n(F)\) is the number of distinct variables occurring in \(F\), \(L(F)\) is its full binary encoding length, and no restriction is placed on its size or depth. The same algorithm, positive saving and constants must work for every formula.''',
 definitions=r'''A Boolean formula is a finite rooted ordered tree. A leaf is a constant \(0\) or \(1\), or one of the variables \(x_1,\ldots,x_n\). An internal node is a unary NOT gate or a binary AND or OR gate. Each nonroot node has exactly one parent; subexpressions are supplied in full and cannot be shared by pointers as in a circuit. The same variable may label any number of different leaves. Every declared variable must occur, so \(n\) counts distinct variables rather than leaves, literal occurrences, gates or input bits. If no variable occurs, \(n=0\). Negations may appear anywhere, with the usual Boolean semantics. No monotonicity, bounded occurrence, normal-form, clause-width, density, balancing or satisfying-assignment promise is imposed.

An assignment \(a\in\{0,1\}^n\) determines every leaf value and then the root value by the gate operations. The formula is satisfiable exactly when at least one assignment gives root value one. The output is this yes/no bit. Finding an assignment or counting assignments is not required. Constants and formulas that do not use any variable are included.

For a fixed explicit encoding, let \(\operatorname{code}(a)\) for an integer \(a\ge0\) be \(1^b0\) followed by the \(b\)-bit binary representation of \(a+1\), with \(b=\lfloor\log_2(a+1)\rfloor+1\). Begin with \(\operatorname{code}(n)\), then traverse the tree in preorder. Each node has a three-bit tag specifying constant zero, constant one, variable, NOT, AND or OR. A variable tag is followed by \(\operatorname{code}(i)\), \(1\le i\le n\); other tags determine their arity and have no extra payload. There must be exactly one complete tree, no unused tags or trailing bits, and all declared variables must occur. The full length of this encoding is \(L(F)\). This includes every copy of a repeated subexpression. A succinct generator, truth-table oracle or circuit with shared gates is not an alternative input encoding.

The algorithm is one fixed finite deterministic multitape Turing machine with a read-only input tape, finitely many initially blank work tapes and finite tape alphabets. One transition reads or writes only the cells under its heads and moves each head by at most one cell; its cost is one bit step up to a fixed machine-dependent factor. It halts on every input, rejects malformed encodings in polynomial time in their length and returns the exact satisfiability answer for every valid formula. Parsing, input access, preprocessing and internal computation are included in the runtime. There is no advice, randomness, oracle, quantum computation or unit-cost arithmetic on unbounded integers. No separate workspace restriction is imposed.

The quantifier order is \(\exists(\varepsilon,K,d,A)\,\forall F\). In particular, neither the exponent saving nor the polynomial exponent may deteriorate with formula size, depth, variable-occurrence count or a chosen size bound. The target includes formulas of every polynomial size as well as larger explicit formulas; their input length remains charged through the displayed factor. For a fixed polynomial relation \(L\le n^q\), any polynomial overhead is absorbed into a smaller fixed exponential saving for sufficiently large \(n\), but no separate size-dependent algorithm is substituted for the single program demanded here.

Exhaustive evaluation gives a bound \(2^n\operatorname{poly}(L)\). The question asks to replace its exponential base by some fixed smaller value. A bound \(2^{n-n^\alpha}\operatorname{poly}(L)\), \(0<\alpha<1\), or a polynomial-factor improvement over \(2^n\) does not meet the target: its saving divided by \(n\) tends to zero. No particular numerical saving is prescribed. Restricting \(\varepsilon\) to rational values in \((0,1)\) preserves existence of a positive fixed saving.''',
 answer_criterion=r'''Give a complete mathematically correct Lean-checked proof of the displayed existence proposition or its logical negation. A positive proof must supply an exact deterministic decision algorithm and a fixed positive saving valid for every allowed formula, with all input and computation costs counted. A negative proof must rule out all algorithms and constants in the proposition unconditionally; a lower bound assuming SETH, ETH or another unproved hardness hypothesis is only a conditional result.

Results restricted to fixed clause width, bounded variable occurrences, linear-size or subcubic-size formulas do not establish the universal positive answer. A counting algorithm could establish it only if it satisfies the full stated size, time and machine requirements. There is no additive numerical tolerance or minimum required saving of one hundredth.''',
 source_formulation=dict(text='Fortnow describes general formula satisfiability as lacking algorithms that substantially improve exhaustive assignment search, unlike some restricted satisfiability problems. The passage does not specify a saving. This card adopts a deterministic fixed positive exponential saving with a polynomial factor in the full formula encoding length as an explicit editorial target.',caption='The Status of the P versus NP Problem (2009), Section 5.1, PDF p.3; announced recommended editorial default of 17 September 2026 after an optional scope question.',citation='primary',format='editorial_paraphrase'),
 why='Boolean formulas are more general than bounded-width CNF instances while still lacking arbitrary circuit sharing. A fixed exponential saving across all formula sizes would reveal algorithmic structure beyond exhaustive search and would also improve every fixed-width SAT problem with one common saving.',
 references=[
 ref('primary','The Status of the P versus NP Problem','Lance Fortnow',2009,'https://lance.fortnow.com/papers/files/pnp-cacm.pdf','Section 5.1, Brute Force, PDF p.3; qualitative general-formula discussion'),
 ref('shrinkage','#SAT Algorithms from Shrinkage','Avishay Tal',2015,'https://eccc.weizmann.ac.il/report/2015/114/','ECCC TR15-114, published 18 July 2015; abstract, Section 1 and Theorem 1.1, restricted-size deterministic counting bound'),
 ref('depth','Towards Stronger Depth Lower Bounds','Gabriel Bathie; R. Ryan Williams',2024,'https://doi.org/10.4230/LIPIcs.ITCS.2024.10','Published 24 January 2024; Introduction pp.10:2–10:3 and Theorem 1.1, conditional consequences of faster restricted-size #SAT'),
 ],
 related=['TCS-6595','TCS-6949','TCS-7270'],
 context_blocks=[
 block('The input is a formula tree, but the exponent is measured in distinct variables. Repetition can make a formula much larger without introducing new assignment bits, which is why its full encoding length appears separately.'),
 block(r'Tal gives deterministic counting for formulas with at most \(n^{3-16\eta}\) leaves in time \(2^{n-n^\eta}\operatorname{poly}(n)\), for sufficiently small fixed \(\eta>0\). This is significant restricted-size progress but has neither the universal size range nor the linear-in-\(n\) exponent saving required here.','shrinkage'),
 block('The 2024 work connects further improvements for small-formula counting to stronger formula lower bounds. Those conditional connections illustrate the importance of the algorithmic problem without deciding this general existence question.','depth'),
 block('Fixed-width CNF formulas are a special case with the same variables. Consequently, the proposed algorithm would refute deterministic SETH; that implication is not an equivalence or an unconditional negative answer.'),
 ],
 progress=[progress('2009','The survey identifies general formula satisfiability as a setting where exhaustive search remains the basic obstacle.'),progress('2015-07-18','A deterministic shrinkage-based counting algorithm handles formulas below the cubic size scale with a sublinear saving in the variable exponent.','shrinkage'),progress('2024-01-24','New conditional connections show that improved small-formula counting algorithms would strengthen formula lower bounds.','depth')],
),notes,sources,'Bounded primary-source checks through 17 September 2026 found no verified resolution of the specified deterministic fixed-saving target. The source itself is qualitative, so the exact target is an announced editorial default after an optional user question, not a claimed verbatim source formulation or confirmed user choice. The reviewed restricted-size algorithms and conditional lower-bound connections do not settle it.',summary=[
 'The input is any explicit Boolean formula tree, and the task is to decide exactly whether some assignment satisfies it.',
 'The time target is 2^((1-epsilon)n) times a fixed polynomial in the full formula length, for some fixed positive epsilon.',
 'One uniform deterministic algorithm must work for all sizes, depths and variable-occurrence patterns.',
 'Known faster algorithms for restricted-size formulas do not provide this full guarantee, and a positive answer would refute deterministic SETH.',
 'A complete Lean-checked proof or unconditional refutation is required; the precise saving is an editorial specification of the source’s qualitative question.',
],expected_sha256=claim['input_sha256'],claim_token=claim['token'])
