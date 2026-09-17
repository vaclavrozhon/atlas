"""Correct the imported border-class label and review the source's presentable class."""
import sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT/'research/card-completion-20260913'))
from complete_review import complete,ref,block,progress
from review_queue import read_claims
identifier='TCS-1103';claim=read_claims(ROOT)[identifier]
complete(identifier,dict(
 title='Containment of presentable border VP in VNP over every field',
 status='source_open',criterion='models',question_type='yes_no',
 formal=r'''Is
\[
\mathrm{VP}^{\varepsilon}_F\subseteq\mathrm{VNP}_F
\]
true for every field \(F\), where \(\mathrm{VP}^{\varepsilon}_F\) is the presentable border class defined below? The same field is used for approximation and for the VNP representation. It is fixed throughout each polynomial family. The question includes infinite fields of every characteristic.''',
 definitions=r'''An arithmetic circuit over a field \(F\) is a finite directed acyclic graph with inputs labeled by variables or arbitrary elements of \(F\), binary addition, subtraction and multiplication gates, and one output. Size counts all vertices. No division gates are allowed. Computation means equality of formal polynomials. Constants have unit algebraic cost; no bit representation or uniform algorithm for generating a circuit family is required.

A family \(f=(f_n)_{n\ge1}\), with \(f_n\in F[x_1,\ldots,x_{m_n}]\), belongs to \(\mathrm{VP}^{\varepsilon}_F\) when there are constants \(A\ge1\), \(a\in\mathbb N\), circuits \(C_n\) over \(F\), integers \(r_n\ge0\), and polynomials \(Q_n\in F[\mathbf x,\varepsilon]\) such that their outputs \(G_n=C_n(\mathbf x,\varepsilon)\) satisfy
\[
G_n(\mathbf x,\varepsilon)
=\varepsilon^{r_n}f_n(\mathbf x)
+\varepsilon^{r_n+1}Q_n(\mathbf x,\varepsilon),
\qquad
\max\{m_n,\deg f_n,\deg_{\mathbf x}G_n,|C_n|\}
\le A(n+1)^a.
\]
Here \(\varepsilon\) is one additional indeterminate. The degree \(\deg_{\mathbf x}\) counts only original variables, excluding \(\varepsilon\); for degree bounds assign the zero polynomial degree 0. There is no polynomial bound on the degree in \(\varepsilon\) or on \(r_n\). Every polynomial in \(\varepsilon\) used by the computation must be produced by counted gates from \(\varepsilon\) and constants in \(F\). Arbitrary \(F[\varepsilon]\) or \(F(\varepsilon)\) expressions are not available as unit-cost input constants. This is what “presentable” specifies.

The family is in \(\mathrm{VNP}_F\) if there are constants \(B\ge1\), \(b\in\mathbb N\), integers \(q_n\ge0\), and polynomials \(h_n(\mathbf x,\mathbf y)\) computed by circuits \(H_n\) over \(F\) such that
\[
f_n(\mathbf x)=\sum_{\mathbf e\in\{0,1\}^{q_n}}h_n(\mathbf x,\mathbf e),
\qquad
\max\{m_n,q_n,\deg h_n,|H_n|\}\le B(n+1)^b.
\]
The degree bound on \(h_n\) is total degree in all its variables. If \(q_n=0\), the sum has one term. The values 0 and 1 and all summation arithmetic are interpreted in \(F\). Even over a finite field the displayed equality is formal polynomial equality, not merely equality as functions on that field.

The statement quantifies over every field and every family meeting the first definition, asking whether witnesses to the second definition exist. The polynomial bounds and circuits may depend on the field and family, but not on the index within a family. It does not ask for an effective conversion of input approximation circuits to VNP verifiers. Ordinary border VP, which permits free univariate approximation constants of unrestricted circuit complexity, is a potentially larger class and is not this target.''',
 answer_criterion='Give a complete mathematically correct Lean-checked proof of the inclusion for every field, or its logical negation. A positive answer must bound verifier size, witness count and total verifier degree polynomially for each input family over the same field. A negative answer must establish a field and a presentable family outside VNP. A finite-field-only proof or a proof solely about unrestricted ordinary border circuits does not settle the stated universal presentable-class question.',
 why='Charging for approximation coefficients gives an intermediate model between exact circuits and unrestricted border complexity. Understanding whether its limits admit small algebraic verifiers tests how much power approximation adds when its coefficients have compact circuits.',
 source_formulation=dict(text='Question 8 in the original survey, retained as Open Problem 5.3.1 in the 2026 revision, asks about presentable VP epsilon, not unrestricted border VP. The imported title omitted this distinction.',caption='Original 2025 survey p.43; revised §5.3, Definition 5.17 and Open Problem 5.3.1, pp.48–49.',citation='primary',format='editorial_paraphrase'),
 references=[
 ref('primary','A primer on the closure of algebraic complexity classes under factoring','C. S. Bhargav; Prateek Dwivedi; Nitin Saxena',2026,'https://eccc.weizmann.ac.il/report/2025/083/','Original Question 8 p.43; revision 1, 12 June 2026, §5.3 Definitions 5.15/5.17, Theorem 5.18 and Open Problem 5.3.1, pp.46–49'),
 ref('presentable','Learning the coefficients: A presentable version of border complexity and applications to circuit factoring','C. S. Bhargav; Prateek Dwivedi; Nitin Saxena',2024,'https://www.cse.iitk.ac.in/users/nitin/papers/PresentableVNP.pdf','STOC 2024 full author version; §1.2 pp.4–5, Theorem 1 p.5, Definition 4.10 p.20 and Conclusion p.29'),
 ],
 context_blocks=[
 block('The source distinguishes ordinary border complexity from presentable approximation by charging for circuits that generate the univariate approximation coefficients.'),
 block('The 2024 theorem puts presentable VNP, and therefore presentable VP, inside VNP over finite fields. The general-field extension remains the target.','presentable'),
 block('The coefficient-extraction method can exploit finite-field arithmetic through Boolean computation. The source’s conclusion highlights large intermediate integers as an obstacle over fields such as the rationals.','presentable'),
 block('The 2026 revision preserves the question over arbitrary fields. Its factoring applications and its results over finite fields do not prove the universal inclusion.'),
 block('The main-variable degree requirement follows the defining paper’s Definition 4.10. Large approximation-parameter degree is allowed, so substituting a polynomial total-degree restriction would weaken the question.','presentable'),
 ],
 progress=[progress('2024','The finite-field presentable-border inclusion is proved.','presentable'),progress('2025-06-24','Question 8 asks for the extension to every field.'),progress('2026-06-12','The revised survey retains the target as Open Problem 5.3.1.')],
),[
 'Corrected the title from ordinary border VP to the presentable VP epsilon appearing in the original numbered question.',
 'Defined counted approximation-parameter computations, polynomial main-variable degree, formal polynomial equality and same-field VNP witnesses.',
 'Retained all fields, nonuniform algebraic circuit size and the existing individual importance score.',
 'Distinguished the proved finite-field case from the universal inclusion and required a complete Lean-checked proof or exact negation.',
],[
 'Read original ECCC TR25-083 Question 8 p.43 and the 12 June 2026 revision §5.3 pp.46–49. Both ask about VP epsilon; the original imported label was inaccurate.',
 'Read the STOC 2024 author version, §1.2, Theorem 1, Definition 4.10 and Conclusion. Used its explicit bound on the approximant’s degree in the original variables and its finite-field theorem.',
 'Bounded primary-source review through 17 September 2026 found no extension settling the inclusion over every field.',
], 'Source-open for presentable border VP over every field, as retained in the June 2026 survey. The finite-field case is proved in STOC 2024. The imported title incorrectly referred to unrestricted border VP; this review restores the class explicitly named in original Question 8. Status checked through 17 September 2026.',summary=[
 'The target asks whether presentable border VP is contained in VNP over every field.',
 'A small approximation circuit must generate its parameter-dependent coefficients using counted arithmetic gates.',
 'Its degree in the original variables is polynomial, while the degree in the approximation parameter may be much larger.',
 'The required exact representation is a Boolean-cube sum of a polynomial-size, polynomial-degree verifier over the same field.',
 'Finite fields are covered by a known theorem; the universal extension requires a complete Lean-checked proof or counterexample.',
],expected_sha256=claim['input_sha256'],claim_token=claim['token'])
