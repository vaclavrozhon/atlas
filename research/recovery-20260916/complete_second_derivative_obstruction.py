"""Preserve and archive the literal Hessian-overhead claim with a counterexample."""
import sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT/'research/card-completion-20260913'))
from complete_review import complete,ref,block,progress
from review_queue import read_claims
identifier='TCS-6885';claim=read_claims(ROOT)[identifier]
notes=[
 'Read the literal all-second-partials constant-overhead question and found an unconditional distinct-output-polynomial obstruction.',
 'Specified binary scalar arithmetic gates, arbitrary complex constants, all-gate size and free repeated output designations; the obstruction persists even if input gates are free.',
 'Used the product of n variables, whose binomial(n,2) distinct off-diagonal derivatives of degree n-2 require different internal gates, while the product has a 2n-1-node circuit.',
 'Distinguished an actual computed output from an implicit Hessian representation or a Hessian-vector product, and did not silently repair the target to O(s+n^2).',
 'Asked an optional choice between archival and the replacement target; after independent work without a reply, announced and used the recommended archival default. No explicit user confirmation is claimed.',
 'Preserved a complete historical statement and Lean acceptance criterion, assessed the literal claim individually, and archived it as unconditionally refuted by the explicit mathematical argument.',
]
sources=[
 'Read Shpilka–Yehudayoff, Arithmetic Circuits: A Survey of Recent Results and Open Questions, §2.3, Theorem 2.5 and its proof, printed pp.15–16; Open Problem 5 on printed p.16 (PDF p.21). The paragraph explicitly refers to all order-n^2 second derivatives with a constant increase in size. Its following matrix-product implication does not supply a lower-bound assumption needed for the elementary obstruction.',
 'Independently checked the literal target in the scalar circuit model: p_n=product_i x_i has at most 2n-1 total nodes; for n>=4 its binomial(n,2) off-diagonal derivatives indexed by unordered pairs are distinct monomials of degree n-2, hence each needs a different non-input output node. Taking n=4K+2 refutes H(f)<=K(C(f)+1). Full calculation and model scope are saved in research/recovery-20260916/review_second_derivative_obstruction.md.',
 'The resolution is an editorial algebraic derivation, not a claim that the cited survey states the counterexample or that an external theorem or a Lean implementation has been verified. The proof does not depend on the results of the bounded later-literature search through 17 September 2026.',
]
status='Archived as unconditionally refuted in the literal scalar-output circuit model. For p_n=product_i x_i, a circuit has size at most 2n-1, while its second partials include binomial(n,2) distinct non-input monomials requiring different output gates for n>=4. Their ratio is unbounded even when output designations are free. This is an explicit editorial mathematical argument recorded in the review, not an attributed resolution in the 2010 survey or a completed Lean formalization. An output-sensitive O(s+n^2) or implicit-output replacement is a different target and was not silently adopted.'
complete(identifier,dict(
 title='Constant-overhead computation of all second partial derivatives',
 status='resolved',criterion='resources',question_type='yes_no',
 formal=r'''Does there exist an integer \(K\ge1\) such that for every integer \(n\ge1\) and every polynomial \(f\in\mathbb C[x_1,\ldots,x_n]\),
\[
\operatorname{H}(f)\le K\bigl(\operatorname{C}(f)+1\bigr)?
\]
Here \(\operatorname{C}(f)\) is the minimum size of a scalar arithmetic circuit computing \(f\), and \(\operatorname{H}(f)\) is the minimum size of one circuit simultaneously computing all \(n^2\) second partial derivatives \(\partial^2 f/(\partial x_i\partial x_j)\). The exact gate and output conventions are below. This historical proposition is false under these conventions.''',
 definitions=r'''A scalar arithmetic circuit over \(\mathbb C\) is a finite directed acyclic graph. Input gates are labeled by variables \(x_i\) or arbitrary complex constants; each internal gate applies addition or multiplication to two predecessor values. The same predecessor can be used twice, and a gate can feed arbitrarily many later gates. Values are exact formal polynomials in commuting variables. There are no divisions, branches, approximation operations or vector-valued primitive gates. Negative constants allow subtraction to be expressed with these operations.

Size counts all gates, including inputs and constants. No restriction is placed on circuit depth, constant magnitude or constant description length. A single-output circuit has one designated gate computing its output. A circuit for all second partials has a designated gate for every ordered pair \((i,j)\in\{1,\ldots,n\}^2\). Different designations may point to the same gate when the required polynomials agree. Designating or copying an output is free; it does not compute a new polynomial. All designated outputs must be simultaneously present as actual gate values. An implicit representation, a procedure requiring further arithmetic for an individual entry, and a circuit that only multiplies a Hessian by a supplied vector are not this output interface.

The formal derivative is defined on monomials by
\[
\partial_i\left(c\prod_{r=1}^n x_r^{e_r}\right)=
\begin{cases}
c e_i x_i^{e_i-1}\prod_{r\ne i}x_r^{e_r},&e_i>0,\\
0,&e_i=0,
\end{cases}
\]
and extended linearly over finite sums. The second partial \(\partial_i\partial_j f\) includes both mixed and repeated derivatives. Mixed derivatives commute, so symmetric entries can share an output gate; zero derivatives can all use one zero constant. Correctness is equality of formal polynomials for arbitrary complex values of the input variables.

The numbers \(\operatorname{C}(f)\) and \(\operatorname{H}(f)\) minimize gate count over their respective circuit classes. They are finite because finite polynomial expansions can be computed by arithmetic circuits. The Hessian circuit need not also output \(f\) or its first derivatives. The universal constant must be independent of the number of variables, polynomial degree, coefficients and original circuit. The harmless additive one only fixes constant-size cases; there is no additive \(n^2\) allowance. No efficient algorithm for constructing the Hessian circuit is requested: the proposition already fails at the level of existence.''',
 answer_criterion=r'''Give a complete mathematically correct Lean-checked proof or refutation of the universal inequality. A refutation must establish that \(\operatorname{H}(f)/(\operatorname{C}(f)+1)\) is unbounded in the stated model. For the recorded product-family counterexample, formalize the small original circuit, the derivative identities, distinctness of the mixed partials and the lower bound from distinct gate values. Merely charging separately for the output labels is not the argument, since those labels are free here.

The mathematical counterexample is already recorded in the archive. Archival does not assert that its Lean formalization has been supplied. A theorem about first derivatives, implicit Hessian access, a Hessian-vector product, or an \(O(\operatorname{C}(f)+n^2)\) bound concerns a different proposition.''',
 why='The literal statement tests whether the constant-overhead phenomenon for first derivatives extends unchanged to the full Hessian. Its explicit-output version has an elementary quadratic output obstruction, so it is retained as a resolved historical formulation rather than an active research target.',
 importance=dict(score=35,method='editorial',assessed_on='2026-09-17',reason='The precise imported constant-overhead claim is ruled out by elementary counting of distinct computed outputs. The surrounding automatic-differentiation topic is substantial, but this literal statement is not a substantive unresolved lower-bound frontier.'),
 source_formulation=dict(text='After the first-derivative theorem, the survey asks whether all second partial derivatives can be computed with only a constant increase in circuit size. The card preserves that literal universal claim with explicit scalar-output conventions and records its elementary refutation.',caption='Shpilka–Yehudayoff, §2.3, Open Problem 5, printed p.16 (PDF p.21). The counterexample is the present editorial derivation, not a claim attributed to the source.',citation='primary',format='editorial_paraphrase'),
 references=[ref('primary','Arithmetic Circuits: A Survey of Recent Results and Open Questions','Amir Shpilka; Amir Yehudayoff',2010,'https://www.cs.tau.ac.il/~shpilka/publications/SY10.pdf','§2.3, Theorem 2.5 and proof, printed pp.15–16; Open Problem 5, printed p.16 (PDF p.21)'),ref('review','Editorial proof of the full-Hessian output obstruction','Atlas catalogue editorial review',2026,'https://github.com/vaclavrozhon/atlas/blob/main/research/recovery-20260916/review_second_derivative_obstruction.md','Product-family derivative identity, distinct-node count and n=4K+2 contradiction')],
 context_blocks=[
 block('The Baur–Strassen phenomenon lets one share work when obtaining all first derivatives of a scalar circuit. The imported question asks for the same constant-size-overhead conclusion for the entire Hessian.'),
 dict(citation='review',text=r'For the product \(p_n=\prod_{i=1}^n x_i\), the original circuit has at most \(2n-1\) nodes. Its distinct mixed second partials are \(\prod_{k\notin\{i,j\}}x_k\), one for each unordered pair \(i<j\). For \(n\ge4\), these are \(\binom n2\) different polynomials of degree at least two. This is the editorial counterexample.'),
 dict(citation='review',text=r'Each of those polynomials must occur at a different internal gate. Hence \(\operatorname{H}(p_n)\ge\binom n2\), even though repeated output labels are free. Choosing \(n=4K+2\) gives \(\binom n2>2Kn\ge K(\operatorname{C}(p_n)+1)\), contradicting any proposed universal integer \(K\).'),
 block('The source also observes that its proposed bound would imply quadratic-size matrix multiplication. That implication does not establish that the universal premise is open, and no matrix multiplication conjecture is needed for the output-count counterexample.'),
 dict(citation='review',text='An output-sensitive bound that includes the number of derivative entries would be a different mathematical question. The archive preserves the original literal target and its resolution without silently replacing it.'),
 ],
 progress=[progress('2010','The survey states the first-derivative theorem and asks about a constant-size-overhead analogue for all second derivatives.'),dict(date='2026-09-17',citation='review',text='The individual review refutes the literal scalar-output formulation by the product family and distinct-gate counting; this is an editorial derivation, with no completed Lean formalization claimed.')],
),notes,sources,status,summary=[
 'The historical claim asks for all Hessian entries with a universal constant multiple of the original scalar circuit size.',
 'Repeated output labels are free, but different derivative polynomials must be computed at different gates.',
 'The product of n variables has a linear-size circuit and quadratically many distinct mixed second partials.',
 'This gives an unconditional counterexample to the literal constant-overhead assertion without assuming matrix multiplication hardness.',
 'The card is archived with the precise model and proof, while a complete Lean formalization remains the stated answer criterion.',
],expected_sha256=claim['input_sha256'],claim_token=claim['token'],archive_reason='Literal constant-overhead full-Hessian assertion is unconditionally false in the scalar circuit model: product_i x_i has a circuit of size at most 2n-1 but binomial(n,2) distinct non-input mixed second partials for n>=4, each requiring its own gate. Detailed editorial proof preserved in research/recovery-20260916/review_second_derivative_obstruction.md; no implicit-output or O(s+n^2) replacement was silently made.')
