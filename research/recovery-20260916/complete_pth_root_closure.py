"""Review degree-independent pth-root circuit closure in fixed characteristic."""
import sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT/'research/card-completion-20260913'))
from complete_review import complete,ref,block,progress
from review_queue import read_claims
identifier='TCS-3318';claim=read_claims(ROOT)[identifier]
complete(identifier,dict(
 status='source_open',criterion='resources',question_type='yes_no',
 formal=r'''For every prime \(p\), do there exist constants \(K_p>0\) and integers \(a_p\ge1\) such that, for every integer \(n\ge1\) and every polynomial \(g\in\overline{\mathbb F_p}[x_1,\ldots,x_n]\),
\[
\operatorname C_p(g)\le K_p\bigl(\operatorname C_p(g^p)+n+1\bigr)^{a_p}?
\]
Here \(\operatorname C_p\) is division-free arithmetic circuit size over the algebraic closure of the prime field, with arbitrary constants from that same field. The constants may depend on \(p\), but not on \(n\), \(g\), its coefficients or its degree. There is no degree parameter in the size bound.''',
 definitions=r'''For a prime \(p\), \(\mathbb F_p\) is the field of integers modulo \(p\), and \(\overline{\mathbb F_p}\) is its algebraic closure. It has characteristic \(p\), so the sum of \(p\) copies of 1 is zero. Every element has a unique \(p\)-th root in this field. This field choice removes the separate obstruction that a scalar root might not belong to the coefficient field. All coefficients and circuit constants belong to this one fixed field for the chosen \(p\).

The variables commute. Polynomials are formal finite sums of monomials with field coefficients. Equality means coefficientwise equality, not equality as functions on a finite set of field elements. In characteristic \(p\),
\[
\left(\sum_{\alpha}c_{\alpha}x_1^{\alpha_1}\cdots x_n^{\alpha_n}\right)^p
=\sum_{\alpha}c_{\alpha}^p x_1^{p\alpha_1}\cdots x_n^{p\alpha_n}.
\]
This is the polynomial \(g^p\) in the question. For example, even over \(\mathbb F_p\), the formal polynomials \(x^p\) and \(x\) differ although they induce the same function on that finite prime field.

A circuit is a finite directed acyclic graph with one output. Input gates are variable symbols or arbitrary field constants. Each internal gate adds or multiplies two predecessor values; a predecessor may serve both operands. The size is the total number of gates, including inputs. Fan-out, reuse, depth and intermediate degrees are unrestricted. There are no division gates, root gates, coefficient-extraction gates, tests or limit operations. A field constant costs one gate irrespective of the degree of the finite extension in which it lies. This is a nonuniform algebraic size measure, not a bit-complexity measure. \(\operatorname C_p(h)\) is the minimum size of such a circuit whose exact formal output is \(h\), including \(h=0\) and constant polynomials.

The question is about existence of small circuits. It does not require an efficient procedure to discover \(g\), extract its coefficients, or convert a given circuit for \(g^p\). In particular, allowing scalar constants with roots already in the field does not supply a polynomial-root operation on a circuit's entire output. A circuit for \(g^p\) may use cancellations between intermediate polynomials that are not themselves \(p\)-th powers.

There is no bound on the degree of \(g\) in terms of \(n\). It can be exponentially large in the supplied circuit size. A bound polynomial in \(\operatorname C_p(g^p)+n+\deg(g)\) would be a different, weaker assertion. The displayed quantifier order permits a different fixed polynomial size overhead for each prime; it does not ask for uniform dependence on a variable characteristic.''',
 answer_criterion=r'''Give a complete mathematically correct Lean-checked proof of the stated inequality for every fixed prime or of its logical negation. A positive answer must cover all numbers of variables and all degrees while using only the allowed arithmetic gates. A negative answer must exhibit a prime \(p\) for which every proposed pair \(K_p,a_p\) fails on some polynomial. Bounds only for a fixed number of variables, for degree-bounded inputs, or for polynomial functions rather than formal polynomials are insufficient. No efficient conversion algorithm is required, but proving its existence with the same size guarantee would suffice.''',
 why='In positive characteristic, taking a power can conceal the coefficient structure needed for circuit factorization and hardness-to-randomness arguments. Removing such powers with polynomial size overhead would eliminate a basic inseparability obstacle in algebraic complexity.',
 importance=dict(score=82,method='editorial',reason='A fundamental positive-characteristic circuit closure question with consequences for factoring and algebraic derandomization; the degree-independent target goes beyond the known few-variable construction.'),
 source_formulation=dict(text='Andrews states that obtaining a small circuit for g from a small circuit for g^p remains open, while giving a construction that is polynomial when the number of variables is sufficiently small. This card fixes algebraically closed fields of each prime characteristic and asks for degree-independent polynomial overhead.',caption='Andrews, CCC 2020, §4.1, printed p.37:18; §3.1, Corollary 3.6 and Remark 3.7, printed p.37:13.',citation='primary',format='editorial_paraphrase'),
 references=[
 ref('primary','Algebraic Hardness Versus Randomness in Low Characteristic','Robert Andrews',2020,'https://doi.org/10.4230/LIPIcs.CCC.2020.37','§2.1 Theorem 2.8; §3.1 Corollary 3.6 and Remark 3.7, p.37:13; §4.1 unresolved circuit-root question, p.37:18'),
 ref('abp','Factorization of Polynomials Given by Arithmetic Branching Programs','Amit Sinhababu; Thomas Thierauf',2023,'https://image.informatik.htw-aalen.de/~thierauf/Papers/ABP-factors.pdf','Author version dated 8 March 2023, §5, “Assumption on the underlying Field”, printed p.25; underlying journal article 2021'),
 ref('current','A primer on the closure of algebraic complexity classes under factoring','C. S. Bhargav; Prateek Dwivedi; Nitin Saxena',2026,'https://eccc.weizmann.ac.il/report/2025/083/revision/1/','Revision of 12 June 2026, §4.4, Open Problem 4.4.1 and Andrews log-variate discussion, printed p.29; positive-characteristic qualification in Remark 7.9, p.57'),
 ],
 context_blocks=[
 block('The scalar Frobenius map raises coefficients to the p-th power and multiplies all monomial exponents by p. Its simple expanded form does not itself give a small-circuit inverse when the output is available only as a shared arithmetic computation.'),
 block(r'Andrews constructs a root circuit of size at most \(3s p^{2n}+2^n\) over the perfect closure of the coefficient field. This is polynomial in \(s\) when \(n=O(\log_p s)\), but is exponential in an unrestricted number of variables.'),
 block('The chosen algebraically closed field is already perfect, so the scalar-extension requirement in that construction is automatically met. The unresolved issue here is the number of gates, not the mere existence of coefficient roots.'),
 block('The finite-characteristic discussion of the branching-program factoring paper also identifies removal of p-th powers as a missing step for several arithmetic models. A result for one of those restricted models should not be silently identified with the present general-circuit assertion.','abp'),
 block('The June 2026 survey retains positive-characteristic factor closure as open and discusses the small-variable progress. That degree-sensitive factorization question does not automatically establish this stronger degree-independent root bound.','current'),
 ],
 progress=[progress('2020','Andrews provides the exponential-in-variable-count root construction and explicitly retains the general small-circuit question.'),progress('2023-03-08','The updated branching-program manuscript reiterates the p-th-power obstacle in finite characteristic.','abp'),progress('2026-06-12','The revised factorization survey retains the positive-characteristic closure frontier and the limited-variable progress.','current')],
),[
 'Retained the source’s small-circuit root target without adding a degree-dependent allowance.',
 'Applied the announced recommended editorial default after the optional degree-scope question remained unanswered; no user confirmation is claimed.',
 'Fixed algebraic closures of prime fields, with a separate polynomial overhead allowed for each fixed prime, and arbitrary constants in that field.',
 'Specified formal polynomial equality, all-gate size, unrestricted sharing and degrees, and existence rather than efficient circuit conversion.',
 'Read the published root construction and distinguished its exponential variable dependence from the desired polynomial overhead.',
 'Individually assessed importance and retained a complete Lean-checked existence or negation criterion.',
],[
 'Read the published CCC 2020 PDF, Andrews §2.1 Theorem 2.8, §3.1 Corollary 3.6 and Remark 3.7 (p.37:13), and §4.1 p.37:18. The stated circuit size is 3*s*p^(2n)+2^n over the perfect closure, with polynomial size for n=O(log_p s); the later passage explicitly calls general small-circuit p-th-root extraction open.',
 'Read the finite-characteristic discussion in Sinhababu–Thierauf’s author version dated 8 March 2023. The characteristic-zero factoring proof fails on suitable repeated factors, and the manuscript explicitly identifies small formula/ABP/circuit recovery from a p-th power as open.',
 'Read Bhargav–Dwivedi–Saxena Revision 1 dated 12 June 2026, §4.4 p.29 including Open Problem 4.4.1 and the Andrews log-variate discussion, and Remark 7.9 p.57 on positive-characteristic inseparability. General factor closure retains degree bounds, so it is not equated with the degree-independent target here.',
 'Bounded primary-source searches through 17 September 2026 found no resolution of the selected all-variable, degree-independent root-size assertion. Choosing algebraic closures and allowing constants to depend on the fixed characteristic are explicit editorial precisifications.',
], 'Source-open for degree-independent polynomial circuit-size overhead for p-th roots over the algebraic closure of each fixed prime field. Andrews explicitly states the small-circuit question and gives an exponential-in-variable-count bound; the 2023 and June 2026 primary discussions retain the associated inseparability obstruction. No resolution of this precise stronger degree-independent target was identified in bounded checks through 17 September 2026.',summary=[
 'For each fixed prime p, the question compares the circuit sizes of g and its p-th power over the algebraic closure of the prime field.',
 'The desired size overhead is polynomial in the original size and number of variables, with no degree dependence.',
 'Circuits may share arbitrary intermediate computations and use arbitrary constants, but may not use root gates.',
 'The target is formal polynomial computation and existence of small circuits, not equality of finite-field functions or efficient reconstruction.',
 'A complete Lean-checked universal size bound or a counterexample to every such bound in some fixed characteristic is required.',
],expected_sha256=claim['input_sha256'],claim_token=claim['token'])
