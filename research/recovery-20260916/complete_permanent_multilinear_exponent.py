"""Review the retained full logarithmic-scale permanent formula target."""
import sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT/'research/card-completion-20260913'))
from complete_review import complete,ref,block,progress
from review_queue import read_claims
identifier='TCS-7269';claim=read_claims(ROOT)[identifier]
notes=[
 'Preserved the user-authorized determination of the full asymptotic scale of log2 F(n), up to universal constant factors, rather than reverting to one exponential lower-bound conjecture.',
 'Retained arbitrary complex constants, binary tree formulas, all-node size, semantic multilinearity at every node and exact polynomial equality.',
 'Separated the matrix dimension n from its n^2 independent variables and ruled out uncharged sharing, Boolean-input-only correctness and output-only multilinearity.',
 'Read Aaronson’s actual exponential-strengthening discussion and Raz’s original model and theorem; checked the inclusion-exclusion upper bound from the arithmetic survey.',
 'Checked the 2026 sparse-determinant primary manuscript, which retains the quasipolynomial lower-bound scale for a different polynomial family and does not determine this exponent.',
 'Preserved importance and made the complete Lean-checked matching-bounds criterion explicit, including its prohibition on a tautological restatement of the minimum formula size.',
]
sources=[
 'Read Aaronson, P=?NP, ECCC TR17-004, the saved primary manuscript: end of §6.5.2, printed pp.79–80, Theorem 84 and following discussion. It records n^Omega(log n) multilinear formula lower bounds and describes a 2^Omega(n) strengthening as open, while separately discussing constant-depth and non-cancelling restrictions. The card’s full exponent determination is the previously authorized editorial extension, not an equivalent quotation of the survey conjecture.',
 'Read Raz, Multi-Linear Formulas for Permanent and Determinant are of Super-Polynomial Size, ECCC TR03-067 primary manuscript: Introduction, §1.1 printed p.2 and Proposition 2.1 pp.3–4. The binary-tree, field-constant, all-node-size model and semantic multilinearity match the card. The author’s publication list and Princeton institutional publication record identify the journal publication as JACM 56(2), Article 8, 2009; the read manuscript is explicitly the earlier ECCC version.',
 'Read Shpilka–Yehudayoff 2010, §1.2, Fact 1.1 (Ryser) printed p.4, and §3.6, Theorem 3.10 pp.36–37. The inclusion-exclusion expression is a sum of products of row-linear sums; each product combines disjoint rows, so it gives an O(n^2*2^n) multilinear formula even with tree-copying charged. This verifies the stated exponential upper-bound scale in the selected model.',
 'Read Boyapati–Chillara–Vempati, Multilinear Formula Lower Bounds for Sparse Determinants, ECCC TR26-090: primary metadata, submission 30 May and publication 2 June 2026; manuscript abstract and Introduction pp.1–3. It retains n^Omega(log n) hardness while reducing the variable count of a determinant family. It is not an exponential permanent lower bound or a determination of this card’s exponent.',
 'Bounded primary-source searches through 17 September 2026 did not locate matching bounds determining log2 F(n) for unrestricted-depth multilinear formulas computing the permanent. Search hits about monotone models, constant depth, rank-method limitations or circuit algorithms were not conflated with this formula target. No independent verification of the full cited lower-bound proofs is claimed.',
]
complete(identifier,dict(
 status='source_open',criterion='resources',question_type='asymptotic_complexity',
 formal=r'''Determine the asymptotic growth of \(\log_2 F(n)\), up to universal multiplicative constants, where \(F(n)\) is the minimum size of a multilinear arithmetic formula over \(\mathbb C\) computing the permanent of an \(n\times n\) matrix of independent variables.

More precisely, give an explicitly characterized positive scale \(g:\{2,3,\ldots\}\to\mathbb R_{>0}\) and prove that there exist constants \(a,A>0\) and an integer \(n_0\ge2\) such that
\[
2^{a g(n)}\le F(n)\le2^{A g(n)}
\qquad\text{for every integer }n\ge n_0.
\]
The scale must determine the growth rate, rather than restating \(F(n)\) or another unresolved minimum-formula-size quantity.''',
 definitions=r'''Let \(X=(x_{ij})_{1\le i,j\le n}\) have \(n^2\) independent commuting variables, and let \(S_n\) be the set of permutations of \(\{1,\ldots,n\}\). The permanent is the polynomial
\[
\operatorname{perm}_n(X)=\sum_{\pi\in S_n}\prod_{i=1}^{n}x_{i,\pi(i)}.
\]
Here \(n\) is the number of rows and columns, not the number of variables.

An arithmetic formula is a finite rooted binary tree. Leaves are labeled by an entry variable \(x_{ij}\) or an arbitrary complex constant. Each internal node adds or multiplies the polynomials of its two children. There are no division gates, tests, limits or approximation operations. The size is the total number of nodes, including leaves and all repeated occurrences. Intermediate computations cannot be shared, so every reuse of a subexpression requires a new copy. No depth restriction is imposed, and constants have no numerical-description or magnitude bound. Negative and nonreal constants are allowed.

A polynomial is multilinear when every variable has exponent at most one in each of its monomials with nonzero coefficient. A formula is multilinear when the actual polynomial computed at every node is multilinear. Constants and zero are multilinear. This semantic definition permits cancellations, and does not demand disjoint syntactic variable sets as an additional condition. Correctness means equality in \(\mathbb C[x_{11},\ldots,x_{nn}]\), equivalently equality on all complex input matrices, not merely on Boolean matrices.

For each \(n\), \(F(n)\) minimizes the all-node size over exactly these formulas computing \(\operatorname{perm}_n\). The minimum exists: the defining sum of monomials is one valid multilinear formula and possible sizes are positive integers. The model is nonuniform; the formula and its constants may depend on \(n\), with no efficient generator requirement.

The requested precision is constant factors in the logarithm of the optimum. Thus an answer \(g(n)\) permits different positive constants in the lower and upper exponents. It does not require constant-factor approximation of \(F(n)\) itself, an exact leading constant in its exponent, or a numerical approximation at one fixed \(n\). The two bounds must hold at every sufficiently large integer \(n\), not only on an infinite subsequence.''',
 answer_criterion=r'''Give a complete mathematically correct Lean-checked determination of an explicit asymptotic scale \(g(n)\), together with the two displayed bounds for the exact formula model. The upper bound must establish formulas of the claimed size and account for duplicated subexpressions; the lower bound must cover all allowed complex constants, cancellations and depths.

Defining \(g(n)=\log_2 F(n)\), or replacing it by an equivalent search over formulas whose growth has not been determined, is not an answer. A lower bound alone, an upper bound alone or bounds at different asymptotic scales do not settle the task. A bound only for monotone, non-cancelling, row-set-multilinear or bounded-depth formulas does not automatically apply to the full model. The original exponential conjecture would establish \(g(n)=n\) when combined with the known exponential upper bound, but any other rigorously matched scale is an admissible resolution.''',
 source_formulation=dict(text='After presenting Raz’s quasipolynomial lower bound, the survey asks about strengthening it to an exponential lower bound. The retained card asks for the actual logarithmic growth rate, allowing intermediate scales, as previously authorized by the user.',caption='Aaronson, P=?NP, end of §6.5.2, printed pp.79–80, Theorem 84 and following discussion. The full exponent target is an editorial extension, not an asserted equivalence.',citation='primary',format='editorial_paraphrase'),
 references=[
 ref('primary','P=?NP','Scott Aaronson',2017,'https://eccc.weizmann.ac.il/report/2017/004/','End of §6.5.2, printed pp.79–80, Theorem 84 and following exponential-strengthening discussion'),
 ref('raz','Multi-Linear Formulas for Permanent and Determinant are of Super-Polynomial Size','Ran Raz',2009,'https://eccc.weizmann.ac.il/report/2003/067/','JACM 56(2), Article 8; earlier ECCC manuscript read: Introduction, §1.1 p.2 and Proposition 2.1 pp.3–4'),
 ref('ryser','Arithmetic Circuits: A Survey of Recent Results and Open Questions','Amir Shpilka; Amir Yehudayoff',2010,'https://www.cs.tau.ac.il/~shpilka/publications/SY10.pdf','§1.2, Fact 1.1 (Ryser), printed p.4; §3.6, Theorem 3.10 pp.36–37'),
 ref('sparse','Multilinear Formula Lower Bounds for Sparse Determinants','Pruthvi Boyapati; Suryajith Chillara; Pratyush Vempati',2026,'https://eccc.weizmann.ac.il/report/2026/090/','Submitted 30 May, published on ECCC 2 June 2026; abstract and Introduction pp.1–3'),
 ],
 context_blocks=[
 block('The permanent is a canonical explicit polynomial for algebraic lower bounds. Requiring every intermediate polynomial to be multilinear creates a restricted model where a superpolynomial lower bound is already known, even at unrestricted depth.'),
 block(r'Raz’s theorem gives \(F(n)\ge n^{\Omega(\log n)}\), or \(\log_2 F(n)=\Omega((\log n)^2)\). This leaves room for several very different growth rates above the known lower-bound scale.','raz'),
 block(r'Ryser’s inclusion-exclusion formula gives \(F(n)\le O(n^2 2^n)\). Each product combines linear forms from different rows, preserving multilinearity, and explicitly copying the expression still gives that formula-size bound. Consequently \(\log_2 F(n)=O(n)\).','ryser'),
 block('An exponential lower bound would close the gap at the linear logarithmic scale. The full determination target also allows an intermediate answer, provided upper and lower bounds match. It is therefore broader than proving or refuting the source’s suggested endpoint.'),
 block('The 2026 sparse-determinant paper shows that the quasipolynomial formula lower-bound phenomenon persists with substantially fewer variables. Its polynomial family and parameter improvement differ from determining the exponent for the full permanent.','sparse'),
 ],
 progress=[progress('2009','The journal version of Raz’s multilinear formula lower bound appears; its original ECCC manuscript dates to 2003.','raz'),progress('2017','The survey highlights the unresolved strengthening from quasipolynomial to exponential multilinear formula size.'),progress('2026-06-02','The sparse-determinant preprint retains the quasipolynomial lower-bound scale while reducing its variable count.','sparse')],
),notes,sources,'Source-open quantitative extension of the exponential lower-bound question. The checked primary sources give a quasipolynomial lower bound and an exponential upper bound in the selected formula model. The 2026 sparse-determinant result concerns a different family and does not determine this scale. Bounded searches through 17 September 2026 found no matching-bound resolution, without claiming exhaustive current openness.',summary=[
 'The permanent is evaluated by a binary tree of exact additions and multiplications over the complex numbers.',
 'Every intermediate polynomial must be multilinear, while sharing is forbidden and arbitrary complex constants are allowed.',
 'The question asks for the asymptotic growth of the logarithm of the minimum formula size, up to constant factors.',
 'The known lower and upper scales for that logarithm are quadratic in log n and linear in n, respectively.',
 'A complete Lean-checked answer must match the upper and lower exponents for every sufficiently large matrix dimension.',
],expected_sha256=claim['input_sha256'],claim_token=claim['token'])
