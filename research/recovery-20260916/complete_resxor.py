"""Individual review of unrestricted resolution-over-parities lower bounds."""
import json
import sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT/'research/card-completion-20260913'))
from complete_review import complete,ref,block,progress
from review_queue import read_claims
identifier='TCS-1253'
old=json.loads((ROOT/'data/cards'/f'{identifier}.json').read_text())
claim=read_claims(ROOT)[identifier]
refs=old['references']
refs[0]['locator']='ITCS 2026 proceedings, §3.2, printed p. 111:17 / PDF p. 17, paragraph immediately after Theorem 5'
refs += [
 ref('model2026','Supercritical Tradeoff Between Size and Depth for Resolution over Parities',
     'Dmitry Itsykson; Alexander Knop',2026,
     'https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.ITCS.2026.81',
     'ITCS 2026; §2.2 exact inference rules and line-count size; §§1.1–1.4, Theorem 2 and Corollary 3'),
 ref('regular2025','Lower Bounds for Regular Resolution over Parities',
     'Klim Efremenko; Michal Garlík; Dmitry Itsykson',2025,
     'https://doi.org/10.1137/24M1696640',
     'SIAM Journal on Computing, journal version of STOC 2024 result; abstract, regular versus unrestricted refutations'),
 ref('conditional2026','New Polynomial-Depth Res(+) Lower Bounds',
     'Yaroslav Alekseev; Nikita Gaevoy',2026,
     'https://eccc.weizmann.ac.il/report/2026/007/',
     'ECCC TR26-007, published 19 January 2026; §1.1 Theorems 1.1–1.3, distinguishing conditional, reversible and bounded-depth statements'),
 ref('quadratic2026',r'Resolution Width Lifts to Near-Quadratic-Depth \(\mathrm{Res}(\oplus)\) Size',
     'Dmitry Itsykson; Vladimir Podolskii; Alexander Shekhovtsov',2026,
     'https://eccc.weizmann.ac.il/report/2026/018/',
     'ECCC TR26-018, 12 February 2026; author abstract, depth-size tradeoff and unconditional quadratic line-count lower bound'),
 ref('seth2026','Strong ETH Holds for Bounded-Depth Resolution over Parities',
     'Klim Efremenko; Dmitry Itsykson',2026,
     'https://doi.org/10.1145/3798129.3800804',
     'STOC 2026, pp. 898–909, published 9 June 2026; publisher abstract, depth-n fragment'),
]
notes=[
 'Recovered the general superpolynomial lower-bound question from the paragraph following Theorem 5, without importing its suggested generator approach.',
 'Fixed the unrestricted DAG proof system using the primary-source parity resolution and semantic weakening rules, on exactly the input variables.',
 'Made non-polynomial boundedness the binary target and measured proof size by line count against the full CNF input size.',
 'Did not impose an unrequested explicitness, uniform construction, fixed formula family, width bound or quantitative exponential lower bound.',
 'Compared regular, bounded-depth, reversible and conditional results through September 2026; assigned an individual importance score to the previously unassessed draft.',
]
sources=[
 'Read ITCS 2026.111 §3.2 including Theorem 5 and the precise unresolved passage on PDF p. 17. Its suggested research approach is not copied into the card.',
 'Read ITCS 2026.81 §§1.1–1.4 and §2.2 in full: semantic weakening is allowed; proof size counts all lines; the variables are those of the initial CNF.',
 'Checked the regular-resolution journal abstract and its distinction from unrestricted DAG refutations.',
 'Read ECCC TR26-007 §1, particularly Theorems 1.1–1.3: arbitrary polynomial depth is conditional for general Res(+) and unconditional only for the reversible fragment.',
 'Read the ECCC TR26-018 author abstract and the STOC 2026 publisher abstract; neither claims an unrestricted superpolynomial bound. The former gives an unrestricted quadratic lower bound as well as bounded-depth improvements.',
 'Bounded later-work search on 16 September 2026 found no resolution of the unrestricted question. The cited technical proofs were not independently verified.',
]
status=('The January 2026 source explicitly leaves unrestricted superpolynomial lower bounds open. '
        'The checked 2025–2026 results concern regular or bounded-depth refutations, conditional bounds, or a reversible fragment. '
        'ECCC TR26-018 additionally reports an unconditional quadratic lower bound, which is still polynomial. '
        'The STOC 2026 SETH-type bound applies to a depth-restricted fragment. '
        'A bounded primary-source search on 16 September 2026 found no unrestricted superpolynomial resolution; this is not an exhaustive literature or proof certification.')
complete(identifier,dict(
 title=r'Superpolynomial \(\mathrm{Res}(\oplus)\) lower bounds',
 question_type='yes_no',
 formal=r'''Is resolution over parities not polynomially bounded on unsatisfiable Boolean CNF formulas? Precisely, is the following proposition true?
\[
\forall C,k\in\mathbb N_{\ge1}\ \exists F\quad
\bigl[F\text{ is an unsatisfiable CNF}\ \land\
L_{\oplus}(F)>C\bigl(N(F)+1\bigr)^k\bigr].
\]
Here \(L_{\oplus}(F)\) is the minimum number of lines in any unrestricted \(\mathrm{Res}(\oplus)\) refutation of \(F\), with the rules below, and \(N(F)\) is its full combinatorial input size. Earlier proof lines may be reused arbitrarily. There is no restriction on depth, width, regularity or space.''',
 definitions=r'''The field \(\mathbb F_2=\{0,1\}\) has addition and multiplication modulo two. A Boolean assignment to \(x_1,\ldots,x_n\) is an element of \(\mathbb F_2^n\). A literal is \(x_i\) or \(\neg x_i\); a clause is a finite set of literals interpreted as their disjunction, with the empty clause false. A CNF formula \(F\) is a finite conjunction of clauses. It is unsatisfiable if no assignment makes every clause true. Relabel its distinct occurring variables consecutively as \(x_1,\ldots,x_n\); no unused declared variables are counted. Put
\[
N(F)=n+\#\{\text{clauses of }F\}+
       \sum_{D\text{ a clause of }F}|D|.
\]
The empty conjunction and empty clauses are allowed. Clauses are listed explicitly, with signs and binary variable indices. This input measure is polynomially equivalent to the length of this ordinary explicit binary encoding, so the existence of a polynomial bound does not depend on that encoding choice.

A linear form is \(f(x)=\sum_{i=1}^n a_i x_i\), with \(a_i\in\mathbb F_2\), including the zero form. A linear equation is \(f=b\), for \(b\in\mathbb F_2\). A linear clause is a finite disjunction of these equations, again allowing the empty disjunction. Its truth value is given by evaluating all equations over \(\mathbb F_2\). Ordinary positive and negative literals are represented respectively by \(x_i=1\) and \(x_i=0\).

A refutation is a finite sequence of linear clauses ending with the empty clause. Each line is either an input clause of \(F\), translated as above, or follows from earlier lines by one of exactly these rules:

Parity resolution:
\[
\frac{A\vee(f=0)\qquad B\vee(f=1)}{A\vee B},
\]
where \(A,B\) are linear clauses and \(f\) is any linear form in the input variables. Disjunction is taken modulo order and repeated identical disjuncts.

Semantic weakening: from a linear clause \(A\), infer any linear clause \(B\) such that
\[
\forall x\in\mathbb F_2^n,\quad A(x)=1\Longrightarrow B(x)=1.
\]
This rule is implication from one previous line, not arbitrary implication from all input clauses jointly.

All equations use only the variables of \(F\); there are no extension variables, additional axiom schemes or unlisted inference rules. A previous line can serve as a premise arbitrarily many times, giving a directed acyclic proof graph. Size is the total number of lines, including occurrences of input clauses and weakening steps. It is not the sum of the lengths of the equations. Define \(L_{\oplus}(F)\) as the minimum such size. Every unsatisfiable CNF has a refutation since the system contains ordinary resolution.

The constants \(C,k\) are proposed universal bounds; the witnessing formula may depend on both. The question imposes no separate running-time condition on constructing these witnesses and fixes no particular family of formulas. It asks for unconditional non-polynomial boundedness of this fixed proof system, not for a conditional statement assuming a complexity separation.''',
 answer_criterion=r'''Supply a complete mathematically correct Lean-checked proof of the displayed proposition or its negation. An affirmative answer must rule out every uniform polynomial line-count upper bound for unrestricted refutations. A negative answer must prove that there are fixed \(C,k\ge1\) such that every unsatisfiable CNF \(F\) has a refutation of at most \(C(N(F)+1)^k\) lines; no efficient proof-finding algorithm is additionally required. Lower bounds confined to tree-like, regular, reversible or bounded-depth proofs do not meet the affirmative target, and a conditional lower bound does not settle the unconditional proposition. No additive numerical tolerance changes this binary asymptotic claim.''',
 references=refs,
 source_formulation=dict(text='Do some unsatisfiable formulas require refutations longer than every universal polynomial bound in unrestricted resolution over linear equations modulo two?',
     caption='Editorial paraphrase of the unresolved passage after Theorem 5',citation='primary',format='editorial_paraphrase'),
 context_blocks=[
     block(r'Ordinary resolution reasons with disjunctions of individual literals. \(\mathrm{Res}(\oplus)\) also permits equations asserting the parity of an arbitrary subset of variables. These equations provide compact algebraic information that ordinary resolution may express inefficiently.','model2026'),
     block(r'This system lies within constant-depth Frege reasoning augmented with parity gates, commonly denoted \(\mathrm{AC}^{0}[2]\)-Frege. The absence of general lower bounds even for this restricted proof language isolates an important boundary in understanding short propositional proofs. A lower bound here alone would not automatically prove one for the stronger Frege system.','model2026'),
     block('Regular refutations and proofs of bounded depth have received much stronger lower bounds. They still exclude possible short proofs with more complicated reuse and longer dependency chains. The unrestricted question must allow those proofs as well.','regular2025'),
     block('The 2026 polynomial-depth paper separates conditional results for the general system from unconditional results for reversible proofs. Its unrestricted polynomial-depth claim cannot be cited without its combinatorial hypothesis.','conditional2026'),
     block('A February 2026 result gives a quadratic unrestricted lower bound together with stronger size-depth tradeoffs. Quadratic growth remains polynomial, and a tradeoff can be satisfied by a short proof with sufficient depth.','quadratic2026'),
 ],
 why='A central lower-bound challenge for a small extension of resolution that can reason directly about parity. Resolving it would establish whether this algebraic ability suffices to give short refutations of every unsatisfiable CNF, or whether even unrestricted reuse of parity information leaves an unavoidable superpolynomial proof-size barrier.',
 importance=dict(score=87,method='editorial',reason='A repeatedly identified major proof-complexity barrier: one of the simplest parity-aware systems without known general superpolynomial lower bounds, with substantial recent progress on restricted fragments.'),
 progress=[
     progress('2024','An exponential lower bound was established for regular resolution over parities; the journal version appeared in 2025.','regular2025'),
     progress('2026-01','The source explicitly records the general superpolynomial lower-bound problem as unresolved.'),
     progress('2026-01-19','Arbitrary polynomial-depth lower bounds are conditional for general resolution over parities and unconditional for a reversible fragment.','conditional2026'),
     progress('2026-02-12','A new lifting result gives nearly quadratic depth tradeoffs and an unrestricted quadratic size lower bound.','quadratic2026'),
     progress('2026-06-09','A STOC paper establishes SETH-type bounds for a fragment capturing depth-n refutations.','seth2026'),
     progress('2026-09-16','The review retained the unrestricted question and specified the complete proof rules and non-polynomial boundedness quantifiers.'),
 ],
),notes,sources,status,summary=[
 'Resolution over parities extends ordinary resolution by allowing disjunctions of linear equations modulo two.',
 'The question asks whether unsatisfiable CNF formulas can require more proof lines than every universal polynomial bound in their input size.',
 'Proofs may reuse earlier lines without any restriction on depth, width, regularity or space.',
 'Recent strong lower bounds for restricted proofs and the known unrestricted quadratic bound do not settle this question.',
 'A resolution would locate a central limitation, or unexpected strength, of propositional reasoning with parity.',
],expected_sha256=claim['input_sha256'],claim_token=claim['token'])
