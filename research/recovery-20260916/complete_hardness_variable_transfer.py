"""Fix the hardness scales, explicitness and field in the variable-transfer question."""
import sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT/'research/card-completion-20260913'))
from complete_review import complete,ref,block,progress
from review_queue import read_claims
identifier='TCS-5240';claim=read_claims(ROOT)[identifier]
complete(identifier,dict(
 title='Does explicit multivariate hardness imply univariate hardness over F₂?',
 status='source_open',criterion='reductions',question_type='yes_no',
 formal=r'''Over the two-element field \(\mathbb F_2\), is the following implication true?

If there exist an explicit family of multilinear polynomials \(f_n\in\mathbb F_2[x_1,\ldots,x_n]\), a real constant \(\alpha>0\), and an integer \(n_0\) such that
\[
\operatorname{size}_{\mathbb F_2}(f_n)\ge 2^{\alpha n}\qquad(n\ge n_0),
\]
then there exist an explicit family of univariate polynomials \(g_d\in\mathbb F_2[t]\) of degree at most \(d\), a real constant \(\beta>0\), and an integer \(d_0\) such that
\[
\operatorname{size}_{\mathbb F_2}(g_d)\ge d^\beta\qquad(d\ge d_0).
\]
Explicitness means coefficient computation in deterministic time \(2^{O(n)}\) for the first family and \(d^{O(1)}\) for the second, with one uniform coefficient algorithm for each family.''',
 definitions=r'''The field \(\mathbb F_2=\{0,1\}\) has addition and multiplication modulo two. All polynomials here are formal commutative polynomials. Equality means equality of every monomial coefficient, not merely agreement on the two-element evaluation domain.

An arithmetic circuit is a finite directed acyclic graph with input gates labeled by variables or the constants 0 and 1, internal gates of fan-in two labeled by addition or multiplication, and one output gate. Gates may feed arbitrarily many later gates. Its size is the total number of gates, including inputs and constants. The notation \(\operatorname{size}_{\mathbb F_2}(h)\) is the minimum size of a circuit whose output is the formal polynomial \(h\). Subtraction adds no new operation in this field. There is no division, extension-field constant, depth bound, restriction on intermediate degrees or uniformity requirement on the circuits used in this minimum. In particular the circuit computing a multilinear output need not be a multilinear circuit.

The family \((f_n)_{n\ge1}\) has the form
\[
f_n(x)=\sum_{u\in\{0,1\}^n}a_{n,u}\prod_{i=1}^n x_i^{u_i},\qquad a_{n,u}\in\mathbb F_2.
\]
Its required explicitness is the existence of one deterministic multitape Turing machine \(M\) and constants \(K,c>0\) such that, for every \(n\ge1\) and \(u\in\{0,1\}^n\), \(M\) receives \((1^n,u)\), outputs \(a_{n,u}\), and halts within \(K2^{cn}\) bit operations. Constants and the algorithm are fixed for the family.

The family \((g_d)_{d\ge1}\) has the form
\[
g_d(t)=\sum_{j=0}^d b_{d,j}t^j,\qquad b_{d,j}\in\mathbb F_2.
\]
Its required explicitness is the existence of one deterministic multitape Turing machine \(N\) and constants \(K',c'>0\) such that, for every \(d\ge1\) and \(0\le j\le d\), \(N\) receives binary encodings of \(d,j\), outputs \(b_{d,j}\), and halts within \(K'(d+1)^{c'}\) bit operations. Time is polynomial in the degree parameter itself, not in its binary length. For these parameter scales, computing all coefficients changes either explicitness bound only by adjusting its constant exponent.

Both hardness bounds hold at every sufficiently large parameter, not just infinitely often. The conclusion can use a different family and new constants and machines. No algorithm transforming a supplied multivariate circuit, polynomial or lower-bound proof into a univariate one is required. The assertion is an implication between the two stated existence claims; it does not assume that either hardness claim has already been established.''',
 answer_criterion='Give a complete mathematically correct Lean-checked proof of the implication with the stated field, coefficient algorithms, hardness scales and quantifiers, or a proof of its logical negation. A negative answer must establish the multivariate existence claim and the failure of the univariate existence claim; a failure of one proposed substitution does not suffice. A positive answer may use any construction or argument, but must preserve the required explicitness and the eventually-every-parameter lower bounds.',
 why='Low-characteristic derandomization can use hard polynomials with very few variables. Understanding whether conventional multivariate hardness already supplies such polynomials would connect two presently different hardness assumptions and clarify what variable compression can preserve.',
 importance=dict(score=85,method='editorial',reason='A structural implication between strong arithmetic lower-bound hypotheses with direct relevance to low-characteristic polynomial identity testing; it isolates a major limitation of current hardness-to-randomness methods.'),
 source_formulation=dict(text='The source asks whether multivariate lower bounds imply comparable lower bounds for a constant number of variables. This card selects its univariate specialization over F₂, with exponential multivariate hardness, polynomial-in-degree univariate hardness, and coefficient explicitness at the source’s corresponding parameter scales.',caption='Algebraic Hardness Versus Randomness in Low Characteristic: arXiv version, Definition 2.4, Lemma 2.6, §6 and §7 question 4.',citation='primary',format='editorial_paraphrase'),
 references=[
 ref('primary','Algebraic Hardness Versus Randomness in Low Characteristic','Robert Andrews',2020,'https://arxiv.org/abs/2005.10885v1','Definition 2.4 and Lemma 2.6 pp.7–8; §6 pp.25–28; §7 question 4 p.29; conference version: CCC 2020, article 37, DOI 10.4230/LIPIcs.CCC.2020.37'),
 ],
 context_blocks=[
 block('The reverse implication has a simple mechanism. Write each exponent of a hard univariate polynomial in binary and use one multilinear variable for each bit. Substituting successive squared powers of one variable recovers the univariate polynomial with only logarithmic extra circuit work. The source formalizes this as Lemma 2.6.'),
 block('That observation does not prove the direction asked here: an easy univariate polynomial can hide difficult coefficient structure, so compressing a particular multivariate polynomial requires a separate hardness argument.'),
 block('The source’s evidence against a direct converse of that particular map concerns constant-free circuits in characteristic zero and the complexity of factorials. Its concluding question explicitly asks what happens in positive characteristic. That evidence is not a refutation of this F₂ implication.'),
 block('The source defines explicitness through coefficient computation. Here it is instantiated as exponential time in the multilinear variable count and polynomial time in the univariate degree. No efficiently evaluable circuit is presumed by either coefficient algorithm.'),
 block('The selected output has one variable, a fixed special case of the source’s constant-variable regime. The two hardness exponents may differ, and the conclusion need not use the direct binary-exponent substitution.'),
 ],
 progress=[progress('2020','The paper proves that suitable explicit constant-variable hardness supports low-characteristic identity-test derandomization, establishes the easy transfer to many variables, and leaves the opposite direction open.')],
),[
 'Fixed the field to F₂ after the optional field question received no reply; applied and announced the recommended editorial default, not a user confirmation.',
 'Selected a precise implication from eventually exponential multilinear-family hardness to eventually polynomial-in-degree univariate-family hardness.',
 'Defined formal-polynomial circuits, all-gate size, unrestricted intermediate degrees and uniform coefficient algorithms with their exact parameter scales.',
 'Distinguished an existence implication from an effective transformation and from a lower-bound-preserving claim for one fixed substitution.',
 'Assessed importance individually and required a full Lean-checked implication or its logical negation.',
],[
 'Read the original arXiv paper’s Definition 2.4, Lemma 2.6 and surrounding open question, §6 introduction, the statement of Conjecture 6.4 and Theorem 6.5, and the final characteristic restriction plus §7 question 4.',
 'Checked the author’s current publication list and bounded primary-paper searches through 17 September 2026. No resolution of the selected implication was located. A thesis copy was not retrievable and is not claimed as a fully read additional source.',
], 'Source-open as the multivariate-to-constant-variable transfer in Andrews (2020). The source does not itself select this single field and fully quantified pair of hardness scales; this card records the announced editorial specialization to F₂ and a univariate conclusion. The characteristic-zero obstruction to a specific constant-free substitution is not a resolution. Bounded later-work checks through 17 September 2026 found no matching resolution.',summary=[
 'Assume an explicit family of multilinear polynomials over F₂ requires circuits of exponential size in its number of variables.',
 'The question asks whether some explicit family of univariate polynomials must then require size polynomial in its degree.',
 'Coefficients must be computable uniformly in exponential time in the first parameter and polynomial time in the second.',
 'Circuit complexity concerns exact formal polynomials and permits unrestricted arithmetic circuits with constants in F₂.',
 'The requested transfer is an existence implication, not a claim about one substitution, and requires a complete Lean-checked proof or refutation.',
],expected_sha256=claim['input_sha256'],claim_token=claim['token'])
