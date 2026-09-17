"""Archive the selected computability variant as a decidability corollary."""
import json,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT/'research/card-completion-20260913'))
from complete_review import complete,ref,block,progress,DATE
from review_queue import read_claims
identifier='TCS-0053'
claim=read_claims(ROOT)[identifier]
notes=[
 'Applied the user-selected computable degree bound without any growth-rate restriction, allowing polynomial sparsity overhead.',
 'Restored the domain {1,2}^n, integer coefficients, arbitrary nonnegative integer exponents and strict sign convention; degree is total degree and length counts nonzero collected monomials.',
 'Expanded the polynomial-sparsity quantifiers with a degree-bound algorithm for each fixed sparsity exponent, independent of coefficients, input degree or the represented function.',
 'Verified a reduction of fixed-truth-table s-term representability to the decidable real field with a predicate for powers of two; real coefficient witnesses can be replaced by rationals and scaled to integers.',
 'Recorded the finite truth-table decision and terminating witness-enumeration argument giving a total computable bound while preserving even the exact term budget.',
 'Archived only this computability variant as a corollary of published decidability, not every quantitative interpretation of the historical question; preserved importance 63 and did not claim a Lean formalization.',
]
sources=[
 'Read Podolskii’s Sign-representation, Dagstuhl Seminar 15242 report, §5.6 printed p. 45 (individual report PDF p. 18). It asks for a degree bound while retaining polynomially many monomials on {1,2}^n and does not name a growth class. The user selected computability without any growth limit on 17 September 2026.',
 'Read Hansen–Podolskii, Polynomial threshold functions and Boolean threshold circuits, ECCC TR13-021, 5 February 2013: introductory definitions and domain discussion, §4 pp. 11–13 and Propositions 14–16. The degree-weight conversions and three-term n^O(n) bound concern more quantitative restrictions than the selected bare computability question.',
 'Read Avigad–Yin, Quantifier elimination for the reals with a predicate for the powers of two, arXiv:cs/0610117v1, 19 October 2006: introduction, expanded language, Theorem 2.1 pp. 1–2 and effective complexity conclusions Theorem 5.7/Corollary 5.8 p. 14. Verified publication Theoretical Computer Science 370(1–3), 48–59, 12 February 2007, DOI 10.1016/j.tcs.2006.10.005. The decidable structure is the ordered real field with a unary predicate for 2^Z, not the field with unrestricted real exponentiation or all integers.',
 'Read Gallego-Hernández–Mansutti, On the Existential Theory of the Reals Enriched with Integer Powers of a Computable Number, STACS 2025 Article 37, introduction and Theorem 1(1) p. 37:2; verified publication 24 February 2025, DOI 10.4230/LIPIcs.STACS.2025.37. The fixed base 2 is algebraic, so the existential decision theorem applies unconditionally.',
 'The polynomial-threshold corollary is an editorial derivation from these published decision theorems, not a theorem explicitly attributed to their authors. The full finite-formula encoding, rationalization and effective bound construction are saved in research/recovery-20260916/review_computable_sign_degree.md. No particular numerical bound was evaluated, no useful growth-rate estimate is inferred, and no Lean certificate was produced.',
]
status='Resolved for the user-selected computability variant: representability with a fixed term budget is decidable by an existential sentence over the real field with the powers-of-two predicate. Enumerating the finitely many truth tables and finding witnesses only for those certified representable gives a total computable degree bound, even without increasing the term budget. The reduction is recorded explicitly as an editorial corollary of Avigad–Yin’s published decision theorem, also covered by STACS 2025 Theorem 1(1). This does not claim a small or practical degree bound, a resolution of every quantitative reading of the 2015 question, or an independently checked Lean proof.'
complete(identifier,dict(
 title='Computable degree bounds for sparse sign representations on {1,2}^n',
 criterion='resources',question_type='yes_no',status='resolved',year=2025,
 formal=r'''Historical target, resolved at the user-selected computability level: for every fixed integer \(a\ge1\), do there exist an integer \(b\ge1\) and a total computable function \(D_a:\mathbb{N}_{\ge1}\to\mathbb{N}\) such that the following holds for every \(n\ge1\) and every function \(f:\{1,2\}^n\to\{-1,1\}\)?

If \(f\) has an integer polynomial sign representation with at most \((n+1)^a\) monomials, then it has one with at most \((n+1)^b\) monomials and total degree at most \(D_a(n)\).

No bound on the growth or computation time of \(D_a\) is imposed. Published decidability yields a positive answer even with \(b=a\).''',
 definitions=r'''A polynomial is an element of \(\mathbb{Z}[x_1,\ldots,x_n]\) written after collecting equal monomials as
\[
 P(x)=\sum_{j=1}^{s}c_j\prod_{i=1}^{n}x_i^{e_{ij}},
 \qquad c_j\in\mathbb{Z}\setminus\{0\},\quad e_{ij}\in\mathbb{N}.
\]
The exponent vectors are distinct. Its length, or sparsity, is \(s\); a nonzero constant term counts as one monomial. Its total degree is \(\max_j\sum_i e_{ij}\). There is no bound on coefficient magnitudes or on the original exponents. These are ordinary commutative polynomials, not arithmetic circuits or formulas whose expansion may have more monomials.

Strict sign representation means \(f(x)P(x)>0\) for every \(x\in\{1,2\}^n\). In particular, the representing polynomial does not vanish at an input. If a Boolean threshold convention assigns a sign at zero, replacing an integer polynomial by \(2P+1\) or \(2P-1\), as appropriate, removes zeros with at most one additional monomial and unchanged degree. This does not change the polynomial-sparsity target, after increasing the fixed sparsity exponent if needed.

The domain is literally \(\{1,2\}^n\). A change of variables to a zero-one domain can expand a high power into many monomials, so a multilinear representation with exponentially many terms does not meet the stated sparsity requirement. The question is about arbitrary functions on this finite domain, without a promise of efficient evaluation or of a uniform algorithm generating a sequence of them.

For each fixed input sparsity exponent \(a\), the output exponent \(b\) and a finite Turing-machine program for \(D_a\) must be fixed before \(n\), \(f\) or a representing polynomial is chosen. On the binary input \(n\), that program halts and outputs the nonnegative integer \(D_a(n)\) in binary. The degree bound cannot depend on the coefficients, degree or description length of an original representation. No effective compiler from \(a\) to the program is required by the historical target, although the decidability corollary below supplies uniformity even in \(a\). Writing polynomial bounds as \((n+1)^a\) absorbs constant prefactors by increasing the fixed exponent.

A stronger sufficient statement is available: there is one total computable function \(B(n,s)\) such that any function on \(\{1,2\}^n\) representable with at most \(s\) terms has a representation with at most \(s\) terms and degree at most \(B(n,s)\). Taking \(s=(n+1)^a\) gives the selected target without increasing sparsity. This is an effective finite bound, with no asserted efficient rate.''',
 answer_criterion=r'''The original benchmark would require a complete Lean-checked proof of the computable degree-bound statement, including totality of the bound computation, its uniform dependence on the stated parameters and the sparsity guarantee. Bare finiteness of the set of Boolean functions would not prove computability, and a degree bound depending on the original coefficient magnitudes would not suffice.

The selected research target is archived because it follows from known decidability by the explicitly recorded reduction. This editorial review supplies no Lean proof and does not turn the record into a formalization task. Polynomial, elementary or other specified growth bounds are separate targets and are not claimed here.''',
 source_formulation=dict(text='The seminar asks whether polynomially sparse integer sign representations on the domain {1,2}^n can be replaced by polynomially sparse representations with a bound on degree. The user selected a computable bound with no restriction on its growth, rather than a particular quantitative rate.',caption='Paraphrase of Podolskii, Dagstuhl 15242 report, §5.6 printed p. 45; computability scope explicitly selected by the user on 17 September 2026.',citation='primary',format='editorial_paraphrase'),
 why='On the domain {1,2}^n, high powers can give a compact sign representation that loses its sparsity when expanded into a multilinear polynomial. The selected question asks only whether some degree ceiling is effectively obtainable; quantitative control of that ceiling is a separate issue.',
 references=[
 ref('primary','Sign-representation, in Complexity of Symbolic and Numerical Problems','Vladimir Podolskii',2015,'https://doi.org/10.4230/DagRep.5.6.28','Dagstuhl Seminar 15242; §5.6, printed p. 45 (individual report PDF p. 18)'),
 ref('thresholds','Polynomial threshold functions and Boolean threshold circuits','Kristoffer Arnsfelt Hansen; Vladimir Podolskii',2013,'https://eccc.weizmann.ac.il/report/2013/021/','ECCC TR13-021, 5 February 2013; introduction; §4 pp. 11–13, Propositions 14–16'),
 ref('decidability','Quantifier elimination for the reals with a predicate for the powers of two','Jeremy Avigad; Yimu Yin',2007,'https://arxiv.org/abs/cs/0610117v1','Preprint 19 October 2006; §§1–2, Theorem 2.1 pp. 1–2; Theorem 5.7 and Corollary 5.8 p. 14. Theoretical Computer Science 370(1–3), 48–59, 12 February 2007; DOI 10.1016/j.tcs.2006.10.005'),
 ref('existential2025','On the Existential Theory of the Reals Enriched with Integer Powers of a Computable Number','Jorge Gallego-Hernández; Alessio Mansutti',2025,'https://doi.org/10.4230/LIPIcs.STACS.2025.37','STACS 2025, LIPIcs 327, Article 37, published 24 February 2025; introduction and Theorem 1(1) p. 37:2, applied to the fixed algebraic base 2'),
 ],
 context_blocks=[
 block('The background paper relates degree and coefficient weight, and gives stronger quantitative results for special term budgets. Those statements should not be confused with the user’s weaker requirement that some bound be computable.','thresholds'),
 block(r'''The following is an editorial corollary of the decision theorem. Fix a truth table \(f\) and term budget \(s\). Introduce real coefficients \(w_j\) and variables \(t_{ij}\in2^{\mathbb{Z}}\) with \(t_{ij}\ge1\). For each \(v\in\{0,1\}^n\), impose \(f(2^{v_1},\ldots,2^{v_n})\sum_jw_j\prod_{i:v_i=1}t_{ij}>0\). The finite conjunction is an existential formula in the decidable real field with the powers-of-two predicate; it contains no variable-exponent operation.''','decidability'),
 block('Each allowed t-variable is two to a nonnegative integer exponent. Once these variables are fixed, the conditions on the coefficients form a finite feasible system of strict linear inequalities with integer coefficients. A rational solution therefore exists whenever a real one does, and clearing denominators gives integer coefficients. Conversely, every sparse integer sign representation supplies a solution. This proves the required equivalence for the reduction.','decidability'),
 block('Decide that formula for every truth table on the fixed finite domain. For each table declared representable, enumerate integer polynomials with at most the specified number of terms until one is found, testing its finitely many values exactly. Every search terminates, and the maximum of the finitely many resulting degrees is a computable bound. This argument preserves the term budget; finiteness alone, without the preceding decision step, would not establish an effective stopping rule.','decidability'),
 block('The STACS 2025 existential decision theorem independently covers the fixed algebraic base two. Neither it nor the older result requires a conjecture about unrestricted real exponentiation for this application. The present review does not extract a concrete small degree bound from their decision-time estimates.','existential2025'),
 ],
 progress=[
 progress('2007-02-12','The published quantifier-elimination procedure establishes effective decidability of the real field with a predicate for powers of two; the computable sparse-degree corollary is derived explicitly in this review.','decidability'),
 progress('2013-02-05','The threshold-polynomial paper studies degree-weight tradeoffs and quantitative special cases.','thresholds'),
 progress('2015','The seminar asks for a degree bound without specifying its growth class.'),
 progress('2025-02-24','The STACS theorem gives an existential decision procedure for any fixed algebraic base, including two.','existential2025'),
 ],
),notes,sources,status,summary=[
 'Sparse integer polynomials sign-represent Boolean functions on the domain {1,2}^n, with no initial degree or coefficient bound.',
 'The user selected a computable replacement degree bound without any growth-rate restriction, while retaining polynomial sparsity.',
 'Fixed-term representability reduces to the known decidable real field with a predicate for powers of two.',
 'Deciding all truth tables at a fixed dimension and then finding their certified witnesses gives a total computable degree bound without increasing the term count.',
 'This computability variant is archived as a stated corollary of known results; no practical bound, resolution of stronger rate questions or Lean proof is claimed.',
],expected_sha256=claim['input_sha256'],claim_token=claim['token'],archive_reason='The selected unrestricted-growth computable degree bound follows from published decidability of the real field with the powers-of-two predicate; the explicit finite-formula reduction and terminating bound computation are documented, preserving even the original term budget. Stronger quantitative degree questions are not declared resolved.')
p=ROOT/'research/recovery-20260916/further-scope-choices.json'
choices=json.loads(p.read_text())
next(r for r in choices if r['id']==identifier).update(state='applied',applied_on=DATE)
p.write_text(json.dumps(choices,ensure_ascii=False,indent=2)+'\n')
