# Independent audit of TCS-6888

16 September 2026. Read the complete inert parent draft
[/tmp/atlas-draft-6888.py](/tmp/atlas-draft-6888.py).
No canonical card, queue, reservation, selection, archive or publication was changed.

The proposed permanent target over C is coherent and fully quantified.
It is a standard source-supported specialization of the original generic
formula lower-bound problem, not a verbatim equivalence to Open Problem 8
in isolation. The draft makes this distinction explicit. I found no
mathematical defect in its formal statement, definitions or answer criterion.

## Original source and model

Shpilka–Yehudayoff 2010, actual cached arithmetic-survey2010.pdf/.txt:

- Definition 1.1, printed p. 2 / PDF p. 7: binary +/× gates, input
  variables or arbitrary field constants, formulas as directed trees,
  size counted in edges.
- Printed p. 3 / PDF p. 8 distinguishes formal polynomials from evaluated
  functions. Remark 1.1 states that field choice matters; the survey generally
  considers arbitrary fields, mentioning prime fields and R as examples.
- Open Problem 8, printed p. 27 / PDF p. 32, asks for a superpolynomial
  arithmetic-formula size lower bound. That sentence does not itself supply
  a field, explicitness definition or polynomial family.
- The preceding discussion involves determinant and Kalorkoti's polynomial
  bound. Choosing determinant as the hard family would be a stronger,
  distinct target from the weakest standard VNP-versus-VF separation.

The draft's vertex count equals one plus the source's edge count for every
tree, so polynomial boundedness is unchanged. Primitive +/× gates with
arbitrary complex constants permit cancellation and simulate subtraction at
constant-factor cost. Division is excluded in both the chosen target and the
survey's basic model. Arbitrary complex labels have unit size; they need not
have computable or finite binary descriptions. This is nonuniform algebraic
complexity, not bit-cost numerical evaluation.

## Permanent equivalence and quantifiers

The source defines permanent on printed p. 4 / PDF p. 9 and states its
VNP-completeness under polynomial projections in Theorem 1.1,
printed p. 5 / PDF p. 10, for characteristic different from two.
In particular it applies over C.

Polynomial-size formula families are closed under these projections: each
leaf is replaced by a variable or constant without increasing the tree size.
Together with VF contained in VNP, this proves that permanent not in VF
is equivalent to VF != VNP over C. It adds no uniform formula generator or
uniform procedure for computing the complex constants. The permanent is a
fully specified fixed family, so no undefined explicitness predicate remains.
The target does not quantify over other fields.

The draft correctly uses:

    for all integers K,C >= 1, there exists n >= 1 such that
    every formula computing Per_n has size > K*n^C.

Its full negation is correctly:

    there exist integers K,C >= 1 such that for every n >= 1
    there exists a formula computing Per_n with size <= K*n^C.

The tree and its constants may depend on n. The matrix dimension is n and the
variable count is n²; polynomial boundedness in either parameter is equivalent.
The lower-bound target is failure of a single polynomial bound across the
family, not a requirement of eventual pointwise growth above every power.
The draft expressly preserves that distinction. Arbitrarily large witnessing
dimensions follow by absorbing any finite initial segment into K.

The contextual VNP definition is sufficient: the polynomial variable and
witness counts, polynomial degree and polynomial circuit size use bounds
independent of the family index; summation cannot increase degree. The
permanent statement itself remains the acceptance target.

A positive answer does not establish VP != VNP, since formulas are a restricted
circuit model. A negative answer would imply VF = VNP and consequently
VP = VNP. The draft does not reverse these implications.

## Bounded later primary review

1. Rossman–Zhu, *Multi-Quadratic Sum-Of-Squares Lower Bounds Imply
   VNC¹ != VNP*, ITCS 2026 article 113,
   [publisher metadata](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.ITCS.2026.113).
   Actual cached formula-general-itcs2026.pdf/.txt.
   PDF p. 1 expressly calls VF (= VNC¹) versus VNP a major open problem.
   Theorem 1.3 and Corollary 1.6 on PDF p. 3 are conditional implications
   from strong SoS/PT-rank lower bounds, not unconditional separations.
   **Publisher date is 23 January 2026**, not 27 January.

2. Forbes, *Low-Depth Algebraic Circuit Lower Bounds over Any Field*,
   CCC 2024 article 31, DOI 10.4230/LIPIcs.CCC.2024.31.
   Actual cached formula-general-lowdepth2024.pdf/.txt.
   PDF pp. 1–3 retain a product-depth restriction. Enlarging the field scope
   does not remove that depth restriction. The first theorem on PDF p. 3
   is numbered **Theorem 1**, not Theorem 1.1.

3. Narayanan, *Arithmetic circuit lower bounds from sumset expansion*,
   arXiv:2607.15848v1, 17 July 2026.
   Actual cached tensor-sumset2026.pdf/.txt.
   PDF p. 5 Theorem 3 concerns depth-bounded complex circuits.
   PDF p. 7 explicitly says its semi-explicit high-rank tensors need not
   define a poly-definable polynomial family. Its unrestricted formula
   consequence is expressly for that not-necessarily-poly-definable family.
   VNP-completeness therefore cannot simply transfer this claim to permanent.

4. OpenAI, *Ten Advances in Mathematics and Theoretical Computer Science*,
   announced 1 August 2026; checked PDF says updated 6 August 2026.
   Actual cached formula-general-oai2026.pdf/.txt.
   [Primary report](https://cdn.openai.com/pdf/ten-proofs-oai.pdf);
   [primary announcement](https://openai.com/index/ten-advances-in-mathematics/).
   Chapter 5, printed p. 115 / PDF p. 119, Theorem 1.2 claims for n >= 32:
   variable leaves >= n⁴/(128 log₂ n) and arithmetic gates >= n⁴/(256 log₂ n).
   These are unrestricted division-free complex formula bounds and concern
   the right model, but remain polynomial. They do not exclude polynomial
   upper bounds of larger fixed degree. The next theorem gives the
   division-enabled variant with changed constants.
   The draft correctly labels these as claims with theorem-scope review.
   This audit did not independently verify the full proofs or run external
   Lean code.

5. **Additional primary source found during this audit:** Deepanshu Kush,
   *On the Tension Between Full-Rankness and Self-Reducibility for
   Set-Multilinear Polynomials*, MFCS 2026 article 69,
   DOI 10.4230/LIPIcs.MFCS.2026.69; publisher date **21 August 2026**.
   [Primary metadata](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.MFCS.2026.69).
   Downloaded actual PDF and text as formula-general-kush-mfcs2026.pdf/.txt.
   PDF p. 1 explicitly treats VF != VNP as the target and spells out the
   conventional explicit family as one in VNP. PDF pp. 1–3 explain why
   restricted set-multilinear bounds do not alone give a general formula bound.
   Its theorem is a barrier for one combination of full rank and
   self-reducibility; it does not prove VF != VNP or VF = VNP.
   This is relevant primary context after the August report. The parent
   may include it as a newer status reference; the source is not a
   suggested solution method.

Bounded searches through 16 September 2026 used exact formula, permanent
and VF/VNP phrases in primary arXiv, ECCC and Dagstuhl sources. No checked
resolution of the specified permanent target was found. This is a bounded
status review, not an exhaustive literature certificate.

## Disposition and minor edits

Importance 96 is supported as an editorial judgment: the weakest standard
separation of polynomial formulas from VNP is a foundational algebraic
lower-bound barrier. Age and publication count are not the reason.

Active TCS-6613 asks for polynomial-size formulas for determinant. It is
distinct: a negative answer there implies the present positive lower-bound
statement, but a positive answer there does not settle permanent.
Active TCS-0010 asks about constant-degree circuits, and active TCS-6882
compares homogeneous and unrestricted formulas. Neither is a duplicate.
Inactive related IDs were not consulted.

The inert draft's ITCS publication date and incorrect Forbes theorem locator
were corrected during this audit. The report reference now uses the exact
chapter title on PDF p. 118, "Circuit and Formula Lower Bounds for the Permanent",
rather than its abbreviated contents-page heading. At the parent's request,
the Kush paper was added as a reference, progress item and audit entry, with no
proposed proof method in public problem prose. The mathematical target was
not changed. A bounded source-open label with the draft's explicit specialization
and verification limits is appropriate; this audit does not certify a Lean
formalization or all cited proofs.
