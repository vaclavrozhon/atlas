# TCS-0651: deterministic Euclidean SVP hardness audit

Reviewed on 16 September 2026 for the root worker's reserved card. This report
contains the substantive source and proof-chain checks behind a proposed resolved
disposition. It does not mutate the card or the review queue, and it is not a Lean
verification or a claim that Wan's hardness manuscript has been peer reviewed.
The assessed importance score of 85 and category are unchanged.

## Original target

The primary file is Huck Bennett, *The Complexity of the Shortest Vector
Problem*, author version dated 24 January 2023, included in William Gasarch's
column file [svp-color.pdf](https://www.cs.umd.edu/~gasarch/open/svp-color.pdf).
The cache is `sources/svp-det-gasarch.pdf` and its corresponding `.txt`.

- Definitions 1.1–1.2: printed page 2, PDF page 4. The default norm is Euclidean,
  and the main definition uses a nonsingular square rational basis.
- Exact-case convention and footnote 3: printed page 3, PDF page 5. “Gap” names
  the decision version; it does not require an approximation factor above one.
- Open Problem 2.1: printed page 4, PDF page 6. It explicitly asks for exact or
  approximate Euclidean GapSVP hardness under a deterministic Karp reduction.

Consequently, an unconditional deterministic polynomial-time many-one reduction
to exact decision SVP answers the entire retained target. Neither a constant gap
above one nor a dimension-dependent factor is additionally required. An archive
must preserve the original card rather than replace it with a stronger question.

## Matching result and revision history

[Daqing Wan, *NP-hardness of SVP in Euclidean Space*](https://arxiv.org/abs/2603.27398v3)
is cached as `sources/svp-det-wanbase2026.pdf` and `.txt`.

- First submission: 28 March 2026.
- Second revision: 15 July 2026.
- Third revision: 22 July 2026, the latest listed version at the cutoff.
- The actual 29-page PDF bears the internal date 23 July 2026.
- The checked record presents it as a preprint and does not indicate withdrawal
  or journal publication.

Theorem 1.8, PDF page 5, and Theorem 7.4, PDF page 28, assert deterministic
polynomial-time hardness of \(\gamma\)-GapSVP in every finite \(\ell_p\) norm for
\(1\le\gamma<2^{1/p}\). The case \(p=2,\gamma=1\) is the card's exact endpoint.
Theorem 2.2, PDF page 7, explicitly connects a deterministic polynomial-time
gadget construction to this hardness statement. The conclusion is an
unconditional reduction, rather than a reduction conditional on ETH or on a
circuit lower bound.

## Reduction and construction checks

The following portions of the actual paper were read, including their proofs.

1. **Basis and distance:** Section 3, PDF pages 8–13. Proposition 3.2 gives an
   explicit block integer basis for the congruence lattice. Its coefficients have
   polynomial bit length, and the required matrix inversion is over the prime
   field. Lemma 3.4 gives the minimum-length lower bound using Newton identities;
   its characteristic requirement follows from the stated prime and size bounds.
   The candidate center is explicit, and the relevant witnesses are binary
   vectors of one prescribed Hamming weight.
2. **Geometry:** Section 4, PDF pages 14–17. Proposition 4.2 establishes the
   complete-intersection dimensions. Proposition 4.4 proves smoothness of the
   section at infinity: a rank-deficient Jacobian would leave too few distinct
   nonzero coordinate values, and the Vandermonde equations force their positive
   multiplicities to vanish modulo a prime larger than their sum. The
   hyperplane-section bound then leaves at most isolated singularities in the
   projective closure.
3. **Counting:** Section 5, PDF pages 17–19. Proposition 5.1 states the
   Deligne–Hooley–Katz point-count bound over every finite extension. Proposition
   5.2 uses these extension-field estimates and the rational zeta function to
   control the sizes of its reciprocal roots and poles. A total Betti-number
   bound supplies a uniform explicit error coefficient. The dimensions and
   degree substitutions in that bound match the preceding construction.
4. **Distinct coordinates and projection:** Sections 6–7, PDF pages 20–28.
   The counting estimates are applied after excluding repeated coordinates and
   coordinates already prescribed by a binary pattern. The proof treats every
   binary pattern, rather than merely proving a large coset or choosing an
   unspecified good projection. The parameter inequalities make the remaining
   count positive. Theorem 7.3, PDF page 27, states the resulting common
   projection guarantee.
5. **Polynomial time:** The final paragraph on PDF pages 27–28 fixes the
   exponents before the input is supplied. The prime is sought in an interval
   polynomial in the source rank, using deterministic primality testing. The
   projection can be truncated to the desired input rank. Constant cutoffs only
   affect finitely many small inputs. No exhaustive search over an exponential
   set of seeds or witnesses is used to construct the output.

An important distinction is that the reduction only has to construct the lattice
instance. It need not find the binary witness guaranteed in the YES case; doing
so would solve the source problem. Existence of those witnesses is not a
nonuniformity defect in a many-one reduction. No such defect or an evident
superpolynomial construction cost was found in this audit.

## External statements checked

The underlying cohomology was not rebuilt in this review. Relevant external
statements were nevertheless checked in their actual primary sources, rather
than accepted from a search summary.

- Nicholas Katz, *Estimates for “Singular” Exponential Sums* (1999),
  [author-hosted PDF](https://web.math.princeton.edu/~nmk/ESES.pdf), cached as
  `sources/svp-det-katz1999.pdf` and `.txt`. Lemma 3, printed page 878 / PDF page
  4, proves the singular-dimension inequality used to pass from a smooth section
  at infinity to a bound on the singular locus of its closure. Its argument uses
  regularity under a hypersurface section and the dimension bound for a
  projective hypersurface intersection.
- Wan–Zhang, *Betti number bounds for varieties and exponential sums*,
  Advances in Mathematics 490 (2026), 110852,
  [DOI](https://doi.org/10.1016/j.aim.2026.110852), actual
  [author-hosted PDF](https://zhangdingxin.gitlab.io/math/pdf/betti.pdf), cached
  as `sources/svp-det-bettibounds.pdf` and `.txt`. Theorem 1.2.1 on PDF page 5
  bounds total compactly supported Betti number of an affine complete
  intersection by \(\binom{n-1}{r-1}(d+1)^n\). The hypotheses and substitution
  used in Wan's Proposition 5.3 match this statement. One theorem-number citation
  differs between versions, but the required bound itself is present.
- Bennett–Peikert, *Hardness of the (Approximate) Shortest Vector Problem: A
  Simple Proof via Reed-Solomon Codes*,
  [APPROX/RANDOM 2023, article 37](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.APPROX/RANDOM.2023.37),
  published 4 September 2023, cached as `sources/svp-det-bennettpeikert2023.pdf`
  and `.txt`. Theorem 12 and Corollary 13, PDF page 12, explicitly cover a
  deterministic polynomial-time construction of the gadget, including its
  projection property. The corresponding full-version labels cited by Wan are
  Theorem 2.10 and Corollary 2.11. Thus the final interface is not restricted to
  randomized or nonuniform reductions.

## Exact encoding, including irrational radii

The completed draft encodes a positive rational **squared radius** \(b\), with
decision predicate
\[
\exists z\in\mathbb Z^n\setminus\{0\},\qquad \|Bz\|_2^2\le b.
\]
This represents radius \(\sqrt b\) exactly, including square roots of integers
arising naturally in reductions. It does not require printing an irrational
number as a binary rational or rounding a comparison at the exact boundary.
The arithmetic model is a uniform deterministic multitape Turing machine,
charging all bit operations and output symbols.

For rational-basis exact SVP this convention is polynomial-time equivalent to a
rational-radius encoding. Let \(D\) be the product of the positive entry
denominators of \(B\), so \(DB\) is integral and
\(D^2\|Bz\|_2^2\) is a nonnegative integer. In one direction, a rational radius
\(r\) is simply squared. In the other, given \(b>0\), set
\[
K=\lfloor D^2b\rfloor,\qquad S=4(K+1),\qquad
U=\lfloor\sqrt{KS^2}\rfloor+1,\qquad r=\frac{U}{SD}.
\]
Integer square root is computable in polynomial bit time. These choices give
\[
K<\frac{U^2}{S^2}<K+1,
\]
including \(K=0\); the upper bound follows from
\(2\sqrt K/S+1/S^2<1\). Hence the predicates \(\|Bz\|_2^2\le b\) and
\(\|Bz\|_2\le r\) agree for every integer vector. All constructed values have
polynomial bit length. No promise gap or numerical tolerance is introduced.

The source's square rational basis convention also does not obstruct applying a
reduction that initially produces a rectangular integer basis. Given a full
column rank integer matrix \(B\in\mathbb Z^{m\times n}\), compute an integer
matrix \(C\) whose independent columns span its rational orthogonal complement,
using exact elimination and clearing denominators. For positive squared radius
\(b\), choose \(M=\lceil b\rceil+1>\sqrt b\). The square matrix
\([B\;MC]\) is nonsingular. Any nonzero coefficient vector in the complement
contributes squared norm at least \(M^2>b\), because its image under \(C\) is a
nonzero integer vector; it is orthogonal to the original part. Thus all vectors
within the threshold are exactly the original short vectors. Dimensions, bit
lengths, and running time remain polynomial. This bridge is an encoding check,
not a replacement of Euclidean norm by another norm or metric.

## Independent current recognition

Shuichi Hirahara and Kazuki Ogitsuka,
[*One-Sided-Error Parameterized Reductions for the Minimum Distance and Shortest
Vector Problems*](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.APPROX/RANDOM.2026.46),
was published on 9 September 2026. Its actual 22-page publisher PDF is cached as
`sources/svp-det-approx2026.pdf` and `.txt`.

- PDF page 2 credits Wan with derandomizing the classical line for factors
  below \(2^{1/p}\).
- PDF page 4 explicitly describes Wan's Euclidean result below \(\sqrt2\) as
  unconditional deterministic polynomial-time many-one hardness.
- Their own Theorem 6, PDF page 3, extends to all fixed constants under an
  additional nondeterministic-circuit lower-bound assumption.

This is independent primary recognition of the matching result, not just a
self-citation. It supports the status assessment but is not a substitute for
the theorem and proof-chain checks above. It also does not turn Wan's underlying
manuscript into a peer-reviewed article.

## Other current results and revision cautions

[Hair–Sahai, arXiv2604.01451v2](https://arxiv.org/abs/2604.01451v2), submitted
1 April and revised 6 April 2026, is cached as `sources/svp-det-apr2026.pdf` and
`.txt`. Theorems 3.1–3.2, PDF page 12, and their following proof give
deterministic **superpolynomial-time** reductions. Their final result has
\(\exp(n^{O(1/\log\log n)})\) size/time and uses a deterministic subexponential
complexity assumption. It would not on its own settle this Karp-hardness target.

[Wan, arXiv2608.12664v2](https://arxiv.org/abs/2608.12664v2), initially submitted
12 August and revised 8 September 2026, is cached as
`sources/svp-det-aug2026.pdf` and `.txt`. The revision note on PDF page 2 states
that a Lee-metric tensor formula and the resulting lattice identity used in v1
are false. Version 2 replaces the amplification argument and drops the earlier
dimension-dependent claims. Its Theorem 3.4, PDF page 7, imports the earlier
binary projection; the block reduction is proved in Theorem 3.5, PDF pages 8–9.
The March/July exact-hardness theorem does not use this later tensor argument,
so its first-version defect is not a defect in the exact-endpoint derivation
audited here. The new full amplification proof was not independently audited.

[Wan, arXiv2609.16711v1](https://arxiv.org/abs/2609.16711v1), submitted
15 September 2026, is cached as `sources/svp-det-cyclic2026.pdf` and `.txt`.
Definition 1.1 and Theorem 1.2, PDF page 2, claim exact deterministic hardness
even for full-rank cyclic integer lattices. The introduction's comparison with
earlier results was read; its separate 39-page structural proof was not audited
or used as a necessary premise for the disposition. No stronger cyclic, NTRU,
average-case, or cryptographic-security target is substituted for the card.

## Disposition and limits

The exact target has a directly matching positive theorem, a checked
deterministic construction and reduction interface, and independent primary
recognition. No evident mismatch in norm, approximation factor, uniformity,
running time, or exact finite encoding was identified. These checks support
archiving the original target as resolved, preserving the full record, comments,
score, category and provenance.

The scope is a bounded literature and proof-chain audit through 16 September
2026. It is not a complete independent reconstruction of the arithmetic geometry
or a machine-checked proof. Those limits and the underlying preprint status must
remain explicit. The parent performs the final disposition and any canonical
or queue mutation.
