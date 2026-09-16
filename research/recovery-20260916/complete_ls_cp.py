"""Individual review of the approved real-coefficient, line-count simulation."""
import sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT/'research/card-completion-20260913'))
from complete_review import complete,ref,block,progress
from review_queue import read_claims
identifier='TCS-5114'
claim=read_claims(ROOT)[identifier]
refs=[
 ref('primary','Representations of Monotone Boolean Functions by Linear Programs','Mateus de Oliveira Oliveira; Pavel Pudlák',2017,
 'https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.CCC.2017.3',
 'CCC 2017, 3:1–3:15; §4.1, pp. 3:6–3:7, and §4.4; the explicitly open direction is LS simulating CP'),
 ref('full','Representations of Monotone Boolean Functions by Linear Programs','Mateus de Oliveira Oliveira; Pavel Pudlák',2019,
 'https://users.math.cas.cz/~pudlak/monotoneLP.pdf',
 'Author draft with January 2019 header; §6.1, pp. 13–14, §6.5 and Corollary 6.9; final journal article: ToCT 11(4), Article 22, DOI 10.1145/3337787'),
 ref('tree','Exponential Lower Bounds and Integrality Gaps for Tree-Like Lovász–Schrijver Procedures','Toniann Pitassi; Nathan Segerlind',2012,
 'https://www.cs.toronto.edu/~toni/Papers/matrix-cut.pdf',
 'SIAM Journal on Computing 41(1), 128–159; abstract and §1.1, pp. 128–130; DOI 10.1137/100816833'),
 ref('closures','A Hereditary Property of Cutting Plane Procedures','Gérard Cornuéjols; Vrishabh Patil',2026,
 'https://arxiv.org/abs/2609.02038v1',
 'Version 1, 2 September 2026; abstract: closure operations and faces, not a DAG proof-length simulation theorem'),
]
notes=[
 'Applied the user’s explicit choice of existential polynomial line-count simulation with real coefficients.',
 'Retained arbitrary finite initial systems of real linear inequalities over Boolean variables, as in the source, rather than silently restricting to encoded CNFs.',
 'Defined the basic quadratic LS rules and linear CP rounding rule completely, with unrestricted DAG reuse and no extension variables.',
 'Used one polynomial bound uniform in variable count, initial inequality count and CP proof length; no coefficient bit cost or proof compiler is required.',
 'Separated the known reverse separation and tree-like restrictions from the open DAG-like direction.',
 'Individually assessed the previously provisional importance score and supplied the exact Lean criterion.',
]
sources=[
 'Read CCC 2017 §4.1 and the explicit open sentence on p. 3:7. The source asks whether LS polynomially simulates CP after proving the reverse separation.',
 'Read the longer 2019 author draft §6.1 and §6.5: real constants, positive linear combinations, multiplication of linear inequalities only, Boolean quadratic axioms, and CP rounding when all variable coefficients are integral.',
 'Read the 2019 introduction and Corollary 6.9, with the polynomial LS refutation in Theorem 6.8. The source’s general input consists of linear inequalities rather than only CNF encodings.',
 'Read Pitassi–Segerlind’s published abstract and §1.1: tree-like LS+ does not polynomially simulate tree-like CP, and their statements do not apply to unrestricted DAG-like LS.',
 'Checked the September 2026 hereditary-closure preprint abstract and a bounded later-work search. This geometric closure result does not state the requested simulation. Full related proofs were not all independently reconstructed.',
]
status=('The source proves that Cutting Planes does not polynomially simulate LS and explicitly leaves the reverse direction open. '
 'The known failure for tree-like LS applies to a stricter proof model. '
 'The user fixed the present target to existential polynomial line count with real coefficients on 16 September 2026. '
 'No later resolution of this target was found in the bounded primary-source review through that date.')
complete(identifier,dict(
 title='Lovász–Schrijver simulation of Cutting Planes',
 criterion='decision',question_type='yes_no',
 formal=r'''Does the basic Lovász–Schrijver system \(\mathrm{LS}\) polynomially simulate Cutting Planes \(\mathrm{CP}\) in the following real-coefficient, line-count sense?

There exist a real constant \(C\ge1\) and an integer \(k\ge1\) such that, for every \(n\ge1\), every \(m\ge0\), every finite initial system
\[
\Phi=\left\{\sum_{j=1}^{n}a_{ij}x_j\ge b_i:1\le i\le m\right\},
\qquad a_{ij},b_i\in\mathbb R,
\]
and every CP refutation \(\Pi\) of \(\Phi\), there is an LS refutation \(\Lambda\) of the same initial system satisfying
\[
|\Lambda|\le C\bigl(n+m+|\Pi|+1\bigr)^k.
\]
All variables are Boolean. The proof systems and the length measure are defined below. The constants are independent of the initial coefficients and both proofs.''',
 definitions=r'''A line is an inequality \(f(x)\ge0\). Polynomials are over \(\mathbb R\) in the original variables \(x_1,\ldots,x_n\); algebraically identical polynomials are identified by collecting coefficients. The initial lines are the members of \(\Phi\), written with the right-hand side moved to the left. Boolean axioms \(x_j\ge0\) and \(1-x_j\ge0\) are available. The harmless constant axioms \(0\ge0\) and \(1\ge0\) are also permitted; they can be derived from the Boolean axioms with constantly many steps.

Both systems permit nonnegative linear combination: from earlier lines \(f\ge0\) and \(g\ge0\), derive \(\alpha f+\beta g\ge0\) for any \(\alpha,\beta\in\mathbb R_{\ge0}\). Coefficients are exact real numbers. Combining any finite number of earlier lines instead of two changes length by at most a polynomial factor, so the binary version fixes a definite convention.

CP contains only affine-linear lines. Its additional rounding rule is
\[
\frac{\sum_{j=1}^{n}c_jx_j\ge d}
{\sum_{j=1}^{n}c_jx_j\ge\lceil d\rceil},
\qquad c_1,\ldots,c_n\in\mathbb Z,\ d\in\mathbb R.
\]
The rounding premise must have integer variable coefficients; the right side and intermediate combination coefficients may be real. Rounding is justified by the Boolean, hence integer, values of the variables.

Basic LS contains lines of degree at most two. In addition to the common rules and axioms it permits both \(x_j^2-x_j\ge0\) and \(x_j-x_j^2\ge0\). From an earlier affine-linear inequality \(f\ge0\), it may derive \(x_jf\ge0\), or \((1-x_j)f\ge0\), as one line each. Multiplication is permitted only for an affine-linear premise. Nonnegative combination may combine linear or quadratic lines. The source’s linear weakening rule \(a\cdot x\ge d\Rightarrow a\cdot x\ge d'\) for \(d'\le d\) is permitted; it is also obtainable by adding a nonnegative multiple of \(1\ge0\). There is no unrestricted multiplication rule, no rule freely adding arbitrary squares, and no rounding rule in LS. Boolean reduction of quadratic monomials must be justified by the displayed axioms; equality merely on Boolean assignments is not free algebraic rewriting.

A refutation is a finite sequence of justified lines ending with \(-1\ge0\), equivalently \(0\ge1\). Any negative constant conclusion can be normalized by a positive scalar in one further step. An earlier line may be used any number of times: proofs are directed acyclic graphs, not necessarily trees. There are no auxiliary extension variables. Length \(|\Pi|\) is the number of listed lines, counting each occurrence of an initial inequality or axiom that appears, and each derived line. Reuse adds no copy unless a new line is written.

No bound is imposed on the magnitude or bit representation of real coefficients, and no effective transformation from \(\Pi\) to \(\Lambda\) is requested. The statement quantifies mathematically over finite systems of real inequalities; its size parameters count variables, initial inequalities and proof lines. This is the convention selected by the user, not a bit-size or polynomial-time simulation assertion.''',
 answer_criterion=r'''Give a complete Lean-checked proof or refutation of the uniform polynomial line-count assertion. A positive answer must prove the existence of the LS refutation bound for every allowed CP refutation and initial system. A negative answer must show that every candidate polynomial bound fails for some allowed initial system and CP proof. A lower bound restricted to tree-like LS, a simulation only with restricted coefficients, or the already known separation in the opposite direction does not decide this statement. No numerical \(1/100\) tolerance applies to this binary assertion.''',
 source_formulation=dict(text='After separating LS from Cutting Planes in one direction, the source asks whether every short Cutting Planes refutation admits a polynomially bounded LS refutation. The user selected existence measured in lines, with the source’s real coefficients.',
 caption='Paraphrase of the explicit open direction in §4.1 of the CCC 2017 paper, with the size convention fixed by the user on 16 September 2026.',citation='primary',format='editorial_paraphrase'),
 importance=dict(score=83,method='editorial',reason='This comparison would locate the relative power of two central geometric proof systems and determine whether Boolean quadratic reasoning can always match short cutting-plane refutations.',basis='Individual review of the basic DAG-like LS and CP systems, the known reverse separation and the remaining simulation direction.'),
 why='Cutting Planes derives integer consequences by rounding, while LS derives consequences using Boolean identities and quadratic inequalities. Establishing or separating their remaining simulation direction would clarify whether the latter rules can always match concise arguments based on rounding. The known reverse separation makes this a concrete boundary between major proof systems.',
 references=refs,
 context_blocks=[
 block('An inconsistent zero-one system has no assignment of zeros and ones satisfying all its inequalities. A refutation proves this by deriving an impossible inequality. Two complete systems may both refute every inconsistent system while requiring very different numbers of steps.','full'),
 block('The systems exploit integrality differently. CP rounds a lower bound upward when its left side is integer-valued. LS uses products with a variable or its Boolean complement, together with the identities for zero-one values. Keeping all intermediate degrees at most two is part of the basic LS model.','full'),
 block('The paper gives systems with polynomially many LS proof lines but superpolynomial CP length. Therefore CP cannot polynomially simulate LS. That theorem addresses the opposite direction from this card and does not show whether LS always matches short CP proofs.','full'),
 block('Pitassi and Segerlind separate tree-like LS+, even with extra square axioms, from tree-like CP. In a tree proof a derived result cannot be shared freely between branches. The present target permits sharing through a general directed acyclic graph, so the tree restriction is material.','tree'),
 block('Counting lines ignores the cost of writing or manipulating their coefficients. The user explicitly chose this measure with real coefficients. A proof of an efficient algorithm translating finite rational encodings would be a stronger kind of result; this card requires only the quantified existence of short proofs.'),
 block('The September 2026 hereditary-property paper studies how geometric cutting-plane closures interact with faces of convex sets. Properties of closure rounds and faces do not by themselves bound the length of a DAG refutation in the specified syntactic systems. Its abstract contains no resolution of this simulation question.','closures'),
 ],
 progress=[
 progress('2012-01-31','Pitassi and Segerlind establish a non-simulation result for tree-like LS+ versus tree-like CP.','tree'),
 progress('2017','The source separates CP from LS in one direction and explicitly leaves LS simulating CP open.'),
 progress('2019','The full treatment retains the open reverse direction and gives the detailed real-coefficient rules.','full'),
 progress('2026-09-02','A new closure result concerns geometric hereditary properties, rather than this proof-length simulation.','closures'),
 progress('2026-09-16','The user selects real coefficients and existential polynomial line count; individual review fixes the unrestricted DAG formulation.'),
 ],
),notes,sources,status,summary=[
 'The question asks whether every Cutting Planes refutation has a polynomially longer Lovász–Schrijver refutation.',
 'Both systems start from the same real linear inequalities over Boolean variables.',
 'Length counts proof lines, with real coefficients unrestricted and earlier lines freely reusable.',
 'The reverse simulation is known to fail, and the failure of tree-like LS simulation does not settle the general DAG case.',
 'The user selected an existence theorem for short proofs, without requiring an efficient proof-conversion algorithm.',
],expected_sha256=claim['input_sha256'],claim_token=claim['token'])
