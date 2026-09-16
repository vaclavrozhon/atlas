# TCS-7283 independent source/model audit

Date: 2026-09-16. Root owns the reservation and authors the card. Read the canonical active card and the relevant primary-source passages. No canonical, queue, selection, completion or publication writes. Preserve assessed importance 92 and the current category.

**Verdict:** retain the exact, unrestricted, nonuniform real SDP-lift target for perfect matching. The source's all-matchings version is polynomially equivalent by explicit face/projection operations. Do not impose coordinate symmetry, coefficient bit bounds, efficient constructibility, a hierarchy, approximate equality, or a stronger eventual-growth claim.

## Source question and precise model sources

Sinha, *Lower Bounds for Interactive Compression and Linear Programs* (2018), Open Question 8.4, **printed 158 / PDF 169**, asks whether the matching polytope has polynomial-size positive-semidefinite extended formulations. His PMAT(n) includes **all** matchings: Chapter 6, **printed 93 / PDF 104**, and Chapter 7, **printed 118 / PDF 129**. Section 6.3.5, **printed 110–111 / PDF 121–122**, explicitly does not give a full SDP-lift definition. Cite an actual precise definition as well.

Fawzi–Gouveia–Parrilo–Saunderson–Thomas, *Lifting for Simplicity: Concise Descriptions of Convex Sets*, **arXiv:2002.09788v2, 19 November 2021**, gives Definition 1.4 and the matrix-order size convention on **printed/PDF 6**. Its matching open-status discussion is on **printed/PDF 42**. The inspected preprint has 47 pages; journal publication is **SIAM Review 64(4), 866–918 (2022), DOI 10.1137/20M1324417**. The cache filename says 2022, but the actual edition is the 2021 preprint revision.

Lee–Raghavendra–Steurer, *Lower bounds on the size of semidefinite programming relaxations*, **arXiv:1411.6317v1, 24 November 2014**, defines the lift in **Section 1.1, printed/PDF 4**: a real PSD cone of matrix order k, arbitrary affine slice and linear projection. Its cut/TSP/stable-set results are not a matching theorem (Corollary 1.2, printed/PDF 5).

## All matchings and perfect matchings

Let MATCH_n be the all-matchings polytope in edge coordinates of K_n, and PM_n the perfect-matching polytope for even n. Then
\[
PM_n=MATCH_n\cap\{x:\sum_e x_e=n/2\}.
\]
Every matching has at most n/2 edges and equality means perfect. A convex combination attaining that maximum uses only maximum constituents. Thus this is exactly a face.

For every n, coordinate projection of PM_2n onto the edges among the first n vertices gives exactly MATCH_n. Restricting a perfect matching gives a matching. Conversely, if a first-copy matching M has m edges, pair its n−2m unmatched vertices to distinct second-copy vertices; the remaining 2m second-copy vertices can be paired among themselves. This extends M to a perfect matching. Projection commutes with convex hull.

An exact lift is closed under affine projection without increasing matrix order, by composing the output map. It is closed under an affine hyperplane intersection by adding the pulled-back equation to the slice. Therefore
\[
xc_{\rm SDP}(PM_n)\le xc_{\rm SDP}(MATCH_n)
                 \le xc_{\rm SDP}(PM_{2n})
\]
for even n, and the second inequality holds for every n. Polynomial bounds for either family exist if and only if they exist for the other. Odd n on the all-matchings side causes no issue because 2n is even. Negating preserves exactly the non-polynomial-boundedness question.

Rothvoß records these inequalities and the projection construction in *The matching polytope has exponential extension complexity*, **arXiv:1311.2369v4**, **printed/PDF 3**, before Theorem 1 and in footnote 1. Although that passage measures LP size, the explicit face/projection operations just checked apply equally to SDP lifts. The footnote's final phrase says projection of a face; its construction in fact projects the whole polytope, which is an allowable improper face.

## Model to preserve

For integer r≥1 let Sym_r(R) be real symmetric r-by-r matrices and
\[
S^r_+=\{X\in{\rm Sym}_r(\mathbb R):z^\top Xz\ge0
                      \text{ for every }z\in\mathbb R^r\}.
\]
A size-r lift has an affine subspace L and an affine output map π, with **exact set equality** P=π(L∩S^r_+). An affine subspace is equivalently a finite system of linear equations in matrix entries; no unrestricted nonlinear constraints are present. All coefficients may be arbitrary real numbers, chosen separately for each n. No coefficient encoding, efficient generation or solver running-time requirement is imposed.

Size is matrix order r, not ambient dimension r(r+1)/2, number of equalities, or the largest order in arbitrarily many PSD blocks. Blocks must be combined block-diagonally with their orders added. “Semidefinite extension degree” would mean a different parameter, which can be one for every polytope.

No topological closure is added around the image. Every point of P must have a feasible preimage, and all feasible matrices must project into P. Do not add Slater conditions or full dimensionality. Perfect-matching polytopes lie in a proper affine subspace. A least positive lift order exists: a diagonal PSD slice whose diagonal entries are nonnegative and sum to one projects to the convex hull of the finite vertex list. The case n=2 is harmless.

### Affine versus linear output

LRS and the survey use linear maps; the canonical card permits affine maps. This is an equivalent convention for polynomial boundedness, with a precise additive-one overhead. If π(X)=A(X)+b, use blockdiag(X,1) in an affine slice of S_+^{r+1}; the linear output is A(Y_top-left)+bY_(r+1,r+1). Linear maps are already affine. Thus
\[
xc_{\rm affine}(P)\le xc_{\rm linear}(P)
                  \le xc_{\rm affine}(P)+1.
\]
Keep affine maps if desired and disclose this convention. The argument does not assert equality of the two numerical minima.

### Quantifiers and acceptance

The canonical target is
\[
\forall C,c\in\mathbb R_{>0}\ \exists n\ge2\ {\rm even}:
             xc_{\rm SDP}(PM_n)>Cn^c.
\]
Its full negation is
\[
\exists C,c\in\mathbb R_{>0}\ \forall n\ge2\ {\rm even}:
             xc_{\rm SDP}(PM_n)\le Cn^c.
\]
In the negation each n may have independently chosen exact lift data. Positive integer C,k are an equivalent polynomial-boundedness convention by rounding upper-bound constants and exponents upward.

“Superpolynomial” must retain the explicit meaning **not bounded by any polynomial**. Do not strengthen to eventual domination at every sufficiently large n, or to an exponential lower bound. Require a complete Lean proof of the full assertion or negation. Finite examples, symmetry/hierarchy restrictions and conditional complexity implications do not settle it. Numerical 1/100 tolerance does not apply to this binary exact statement.

## Symmetry theorem: exact qualification

Braun, Brown-Cohen, Huq, Pokutta, Raghavendra, Roy, Weitz and Zink, *The matching problem has no small symmetric SDP*, **arXiv:1504.00703v5**, was submitted **30 November 2016**, but the actual PDF's title-page date is **15 October 2018**. The cached PDF has **19 pages**, despite metadata comments saying 18. Conference reference: SODA 2016, 1067–1078.

Definition 2.2, **printed 4 / PDF 5**, distinguishes group-symmetric and **group-coordinate-symmetric** formulations. The formal main Theorem 3.10, **printed 9 / PDF 10**, concerns **A_n-coordinate-symmetric** SDP formulations, where the group acts by simultaneous permutations of PSD row and column coordinates. It gives an exponential bound including the exact case. Public progress should explicitly say “coordinate-symmetric SDP formulations.” This extra invariance is different from the ordinary matrix symmetry X=Xᵀ required in all real PSD lifts. The card assumes no graph-relabeling invariance.

Rothvoß's exponential **linear** lower bound is also different. Its v4 closing remarks, **printed/PDF 21**, explicitly retain the polynomial-size SDP question. The JACM publication is 64(6), Article 41, 1–19, **28 September 2017**, DOI 10.1145/3127497; the inspected preprint is 23 pages, so distinguish pagination.

## Bounded later primary review through 16 September 2026

**MIP Insights no. 2, October 2023**, “A chat with two Integer Programmers co-awardees of the 2023 Gödel Prize,” **PDF 2–3**, explicitly lists compact semidefinite formulations for matching as a remaining question. It is in Sam Fiorini's answer in the **right column of PDF 3**, not Thomas Rothvoß's adjacent answer. Actual three-page newsletter cached: https://www.mixedinteger.org/newsletter/mip-insights-02.pdf . This is a later firsthand status statement, not proof of nonresolution through 2026.

**Au–Lindzey–Tunçel**, *On Connections Between Association Schemes and Analyses of Polyhedral and Positive Semidefinite Lift-and-Project Relaxations*, **arXiv:2008.08628v4, 20 August 2025**, published **Discrete Mathematics 349(2), 114767, February 2026**, DOI 10.1016/j.disc.2025.114767. Cached actual 39-page preprint; inspected PDF 1–3 and Section 4, PDF 17–18. Theorem 19, PDF 18, concerns iteration counts for the **specific Lovász–Schrijver LS+ hierarchy** on generalized hypermatching relaxations. It does not lower-bound arbitrary exact SDP lifts. Revision: https://arxiv.org/abs/2008.08628v4 .

**Gharibian–Hecht–Rudolph**, *Semidefinite extension complexity of the separable set, with applications to approximate disentanglers*, **arXiv:2609.09033v1, 8 September 2026**, is a very recent related-terminology search hit. Cached actual 38-page PDF and inspected abstract/introduction. Its object is separable quantum states and approximate formulations, not matching polytopes. No full proof or claimed Lean formalization was audited: https://arxiv.org/abs/2609.09033v1 .

Searches combined matching/perfect matching with semidefinite extension complexity, PSD rank, SDP and 2024–2026 terms. Other hits concerned polytope diameters, odd-red matching LPs, spanning-tree symmetric LP complexity and unrelated SDP optimization. No verified resolution of the unrestricted exact target was found. This remains a bounded review, not an exhaustive bibliography or certification that no result exists.

## Cache manifest

Files are under research/random-card-review-20260914/sources/ with extracted .txt counterparts.

| File | Physical PDF pages | SHA-256 |
| --- | ---: | --- |
| matching-sdp-sinha2018.pdf | 181 | ce6fe69b5ef629a690a3c6eec3ca696ed8c1726c53549b2eed33fc491cf634b9 |
| matching-sdp-symmetric2016.pdf | 19 | d1dfff256596a748c9e0c480a248233ccfcff6655cb8e29eaf8da0089c25115c |
| matching-sdp-lrs2014.pdf | 46 | df6ea7e760c17f439588d384e6432f3491961f5ba55948388cf8556d26c970be |
| matching-sdp-lp2017.pdf | 23 | d6bfbc16c928589574ecb27c9d82ecc2b0b63e536a6e9d56a6a635545582e09c |
| matching-sdp-survey2022.pdf | 47 | ffe017bfdb100163828fb2619089a724fa07dadd82f113358f4ceb681c1b4a8d |
| matching-sdp-interview2023.pdf | 3 | c36867dc6e5f5687935c32986b34e72e52592be4b14a6c3bb773cc16ee0aed4c |
| matching-sdp-association2025.pdf | 39 | e3411dc0f93e9a882fe71787b85ab8bb63c5ea64391fb0a4bd2cb7459b5b8fe8 |
| matching-sdp-separable2026.pdf | 38 | f9b0114f2c95bf26120ad4d5b28dc3d797e01da069775fc1169e7f0c0707b01e |

The reductions and model audit are mathematical checks, not Lean verification. Full literature proofs were not independently reverified.

## Final inert-draft read

Independently read the complete root-authored /tmp/atlas-draft-7283.py after creation. The exact quantifiers, their full negation, nonuniform arbitrary-real affine model, matrix-order convention and public source qualifications match the audit above. No required mathematical or source-claim fix was found. The script parses, its summary has five sentences, delimiters balance, and all 36 mathematical expressions render with strict KaTeX error checks. No draft or canonical content was modified during this final validation.
