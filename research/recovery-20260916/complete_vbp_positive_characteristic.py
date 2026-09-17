"""Review factor closure of commutative ABPs in positive characteristic."""
import sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT/'research/card-completion-20260913'))
from complete_review import complete,ref,block,progress
from review_queue import read_claims
identifier='TCS-1102';claim=read_claims(ROOT)[identifier]
complete(identifier,dict(
 status='source_open',criterion='resources',question_type='yes_no',
 formal=r'''For every field \(F\) of positive characteristic, do there exist a real constant \(K_F>0\) and an integer \(a_F\ge1\) such that for every integer \(n\ge1\) and all nonzero polynomials \(f,g\in F[x_1,\ldots,x_n]\) with \(g\mid f\),
\[
\operatorname{ABP}_F(g)\le
K_F\bigl(\operatorname{ABP}_F(f)+n+1\bigr)^{a_F}?
\]
Here \(\operatorname{ABP}_F\) denotes minimum size of a commutative arithmetic branching program over the same field \(F\), as defined below. Factors of arbitrary multiplicity are included. The constants may depend on the fixed field, but not on the polynomials, their coefficients, the number of variables, or their degrees.''',
 definitions=r'''A field \(F\) has positive characteristic if there is a prime \(p\) for which the sum of \(p\) copies of its multiplicative identity is zero. The question quantifies over all such fields, finite or infinite, with no perfectness or algebraic-closure assumption. The same field is used for the input polynomial, its factors and every branching-program coefficient. No extension of the field is permitted in the conclusion.

An arithmetic branching program is a finite layered directed acyclic graph with a distinguished source in its first layer and a distinguished sink in its last layer. The source and sink are distinct. Each edge goes from one layer to the next and is labeled by an affine linear polynomial
\[
c_0+c_1x_1+\cdots+c_nx_n\qquad(c_i\in F).
\]
There is at most one edge between any ordered pair of vertices. The polynomial of a path from source to sink is the product of its edge labels, and the output polynomial is the sum of these products over all such paths. Variables commute throughout. Edge labels can include constants or the zero polynomial; an empty path sum is zero. There are no division, root, approximation or test gates. Width and number of layers are unrestricted, and a variable may occur on many edges and repeatedly along a path.

Size is the total number of vertices. A size-\(s\) program has at most \(s^2\) edges and \((n+1)s^2\) coefficient positions, so linear labels do not hide an exponential description. All constants are arbitrary elements of \(F\), with no bit-description charge. Counting coefficients or replacing affine labels by individual constant/variable edges changes the relevant bounds by polynomial factors. A path has at most \(s-1\) edges, so a nonzero output has total degree at most \(s-1\). Layering a general acyclic branching program also costs only polynomial size.

The value \(\operatorname{ABP}_F(h)\) is the minimum vertex count of any such program computing the formal polynomial \(h\) exactly. It is finite, since a polynomial is a finite sum of monomials. Polynomial equality is coefficientwise equality, not equality merely on points of a finite field. The divisibility condition \(g\mid f\) means that \(f=gh\) for some polynomial \(h\) over \(F\) in the same commuting variables. The input \(f\) is nonzero to exclude the vacuous fact that every polynomial divides zero. A constant factor is allowed, as are products of distinct irreducible factors and repeated factors. No circuit for the complementary factor is supplied or assumed small.

For a fixed field, \(\mathrm{VBP}_F\) is the class of polynomial families in polynomially many variables admitting polynomial-size arithmetic branching programs, with no uniformity requirement. Their degrees are automatically polynomially bounded by their sizes. The displayed statement expresses closure of this class under taking factors. It is an existence assertion for small programs, not a request for a deterministic or randomized factoring algorithm, and it does not ask for bounds uniform over changing fields. A bound for unrestricted arithmetic circuits computing the factor would not establish an ABP bound.''',
 answer_criterion=r'''Give a complete mathematically correct Lean-checked proof of the universal factor-size assertion or of its logical negation. A positive proof must cover each fixed positive-characteristic field and all multiplicities, and return a branching-program size bound over that same field. A negative proof must establish a fixed field for which no polynomial size overhead works; merely showing that one factoring procedure fails is insufficient. Characteristic-zero closure, a theorem restricted to square-free inputs or favorable multiplicities, field-extension results, and unrestricted-circuit factor bounds do not settle the stated question.''',
 why='Branching programs are a central algebraic model between formulas and unrestricted circuits. Understanding whether taking factors preserves their polynomial size in positive characteristic would complete an important structural closure property beyond the characteristic-zero theorem.',
 source_formulation=dict(text='The revised survey explicitly asks whether VBP is closed under taking factors over fields of positive characteristic. The card retains the full field scope and all factors, and spells out the nonuniform size guarantee and the dependence on the fixed field.',caption='Bhargav–Dwivedi–Saxena, revision of 12 June 2026, §4.5, Open Problem 4.5.1, printed p.33. This updates the original imported Question 4 locator.',citation='primary',format='editorial_paraphrase'),
 references=[
 ref('primary','A primer on the closure of algebraic complexity classes under factoring','C. S. Bhargav; Prateek Dwivedi; Nitin Saxena',2026,'https://eccc.weizmann.ac.il/report/2025/083/revision/1/','12 June 2026 revision; §4.5, Definitions 4.10 and 4.12, Theorem 4.13 and Open Problem 4.5.1, printed pp.30–33; Remark 7.9 p.57'),
 ref('zero','Factorization of Polynomials Given by Arithmetic Branching Programs','Amit Sinhababu; Thomas Thierauf',2023,'https://image.informatik.htw-aalen.de/~thierauf/Papers/ABP-factors.pdf','Author version dated 8 March 2023; §2 p.4 fixes characteristic zero, §4 Theorem 4.1 p.14, §5 “Assumption on the underlying Field” p.25; CCC 2020 preliminary and 2021 journal publication'),
 ref('roots','Algebraic Hardness Versus Randomness in Low Characteristic','Robert Andrews',2020,'https://doi.org/10.4230/LIPIcs.CCC.2020.37','§3.1 Corollary 3.6 and Remark 3.7; §4.1, p.37:18, distinction between p-th powers as polynomials and finite-field functions'),
 ],
 context_blocks=[
 block('The sum over paths lets a small graph represent a polynomial with many monomials. A factor may have a much less obvious path representation, so its degree bound alone does not give a polynomial-size branching program.'),
 block('Sinhababu and Thierauf prove factor closure in characteristic zero. Their main theorem concerns all factors and a polynomial ABP-size bound; the underlying field assumption is essential to interpreting the theorem.','zero'),
 block('In characteristic p, derivatives of p-th powers vanish. The factoring manuscript explains that this obstructs reducing certain repeated factors to multiplicity one and may leave a power of a desired factor instead of the factor itself.','zero'),
 block('The June 2026 survey still lists positive-characteristic VBP factor closure as open. Its discussion of newer factor-closure techniques retains a qualification involving powers of the characteristic.','primary'),
 block('The separate p-th-root circuit card concerns unrestricted circuits and a degree-independent size bound over algebraically closed fields. This card concerns branching programs, whose degree is bounded by their path length, and retains all positive-characteristic fields.','roots'),
 ],
 progress=[progress('2020','The characteristic-zero ABP factor-closure result appears in the CCC preliminary version, followed by the 2021 journal article.','zero'),progress('2023-03-08','The updated author manuscript explains the repeated-factor obstruction in positive characteristic.','zero'),progress('2026-06-12','The revised survey explicitly retains positive-characteristic VBP factor closure as Open Problem 4.5.1.')],
),[
 'Replaced the title-only formulation by explicit factor-size quantifiers for every fixed positive-characteristic field.',
 'Defined commutative layered ABPs, affine linear labels, vertex-count size and exact formal polynomial semantics.',
 'Excluded the zero dividend, retained arbitrary factor multiplicity and prohibited silently passing to an extension field.',
 'Separated existential nonuniform closure from efficient factor construction, and from unrestricted circuit p-th-root closure.',
 'Read the newer June 2026 source revision and the full field qualification in the characteristic-zero factoring paper instead of relying on an unqualified abstract.',
 'Preserved the existing individually assessed importance score and required a complete Lean-checked closure proof or its logical negation.',
],[
 'Read Bhargav–Dwivedi–Saxena Revision 1, dated 12 June 2026, §4.5 Definitions 4.10 and 4.12, Theorem 4.13 and Open Problem 4.5.1, printed pp.30–33. The prose immediately after the theorem retains the positive-characteristic question. The original imported Question 4 locator is superseded by this explicitly identified revision.',
 'Read Sinhababu–Thierauf author PDF dated 8 March 2023, §2 p.4, §4 opening and Theorem 4.1 p.14, and §5 “Assumption on the underlying Field” p.25. The theorem assumes characteristic zero, and the discussion identifies the repeated-factor/p-th-root obstruction in positive characteristic. The broad abstract is not used to claim arbitrary-characteristic closure.',
 'Read the current survey Remark 7.9, p.57: newer positive-characteristic extensions retain an inseparability/p-th-power qualification. This is not a full positive-characteristic factor-closure theorem.',
 'Read Andrews CCC 2020 root-construction and formal-versus-functional discussion as background for the related but different circuit-root target. No efficient general ABP-root procedure is inferred from its small-variable results.',
 'Bounded later-work checks through 17 September 2026 did not identify a resolution of the full all-factor, same-field positive-characteristic VBP closure question. This status is supported chiefly by the explicit June 2026 source question, without independent verification of every cited proof.',
], 'Source-open in the 12 June 2026 survey revision, Open Problem 4.5.1. The established ABP factor-closure theorem is stated for characteristic zero; the author manuscript identifies a repeated-factor obstruction to unrestricted positive-characteristic closure. The card preserves all fixed positive-characteristic fields, exact factors over the same field and all multiplicities. No resolution was found in bounded checks through 17 September 2026.',summary=[
 'The question asks whether taking any factor preserves polynomial-size commutative arithmetic branching programs in every fixed field of positive characteristic.',
 'A branching program sums products of affine edge labels along its source-to-sink paths.',
 'The factor must have a small program over the original field, including when its multiplicity is divisible by the characteristic.',
 'This is a nonuniform existence question and does not require an efficient factorization algorithm.',
 'A complete Lean-checked polynomial size bound or a counterexample field and superpolynomial factor-size separation is required.',
],expected_sha256=claim['input_sha256'],claim_token=claim['token'])
