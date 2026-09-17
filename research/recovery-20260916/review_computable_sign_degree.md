# TCS-0053: the selected computable bound is a decidability corollary

The user explicitly selected a computable degree bound with no growth-rate
restriction, permitting polynomial sparsity overhead. This is weaker than
the quantitative degree questions usually studied for sparse threshold
polynomials. The following reduction establishes a positive answer using
published decidability; it even preserves the number of terms. This is an
editorial derivation from the cited theorem, not a claim that its authors
state this polynomial-threshold corollary, or that a Lean proof was produced.

Fix positive integers n and s and a truth table f on {1,2}^n. Let A(t) mean
t belongs to 2^Z. For j=1,...,s and i=1,...,n introduce real variables w_j
and t_ij, and form the existential sentence

    exists w,t:
      AND_(i,j) [A(t_ij) and t_ij >= 1]
      and AND_(b in {0,1}^n)
        [ f(2^b_1,...,2^b_n) * SUM_j w_j PROD_(i:b_i=1) t_ij > 0 ].

The second conjunction is expanded into its finite 2^n list. There is no
variable exponent or unrestricted integer predicate. This is a sentence
in the ordered real field with a predicate for powers of two.

An integer polynomial with at most s monomials realizing f gives a witness
by setting t_ij=2^(exponent_ij) and padding with zero coefficients. Conversely,
a real solution fixes nonnegative integer exponents through the t_ij. With
these t_ij fixed, the constraints on w are finitely many strict linear
inequalities with integer coefficients. A feasible real point has a
neighborhood of feasible points, hence a rational feasible point. Clearing
positive denominators gives integer coefficients. Equal monomials can be
combined, leaving at most s terms. Thus the sentence is true exactly when
the truth table admits a strict sign representation with at most s terms.

Avigad–Yin, Theorem 2.1 and the effective procedure (Theorem 5.7,
Corollary 5.8), decide this sentence. Alternatively, Gallego-Hernández–Mansutti,
STACS 2025 Theorem 1(1), applies directly with the fixed algebraic base 2.
Neither appeal needs Schanuel's conjecture or decidability of real
exponentiation. The latter theorem is stated in ExpSpace in formula length;
this note does not infer a specific degree bound from its time bound.

To compute B(n,s), enumerate all 2^(2^n) truth tables and decide the sentence
for each. For every yes table, enumerate finite lists of at most s integer
coefficients and nonnegative integer exponent vectors until a representation
is found, checking all its values exactly. Enumeration can be by increasing
maximum absolute coefficient and exponent, so it is effective and exhaustive.
Every such search terminates because the decision was yes. Take the maximum
of the finitely many found degrees. B is total computable and every
s-term representable function has an s-term representation of degree at most
B(n,s). No stopping test based on a plateau in the enumeration is used.

For the selected polynomial-sparsity target set s=(n+1)^a and
D_a(n)=B(n,(n+1)^a); no sparsity overhead is needed. The procedure is uniform
even in a, though that is stronger than required for each fixed exponent.
The input polynomials have no coefficient-size or exponent-size restriction.
If a threshold convention assigns a Boolean value at zero, replacing an
integer polynomial P by 2P+1 or 2P-1 implements the corresponding strict
convention with at most one additional monomial and unchanged degree. Thus
this convention does not affect the selected polynomial-sparsity question.

Checked sources on 17 September 2026:

- Podolskii, Dagstuhl 15242 report, §5.6 printed p. 45: the historical
  formulation says only “any bound” and does not specify a growth class.
- Hansen–Podolskii, ECCC TR13-021, 5 February 2013: introductory domain and
  length conventions, §4 pp. 11–13, Propositions 14–16. Degree versus weight
  estimates and the length-three bound are separate quantitative questions.
- Avigad–Yin, arXiv:cs/0610117v1, 19 October 2006, §§1–2, Theorem 2.1,
  Theorem 5.7 and Corollary 5.8. Published Theoretical Computer Science
  370(1–3), 48–59, 12 February 2007, DOI 10.1016/j.tcs.2006.10.005.
- Gallego-Hernández–Mansutti, STACS 2025 Article 37, Theorem 1(1), p. 37:2,
  publication 24 February 2025, DOI 10.4230/LIPIcs.STACS.2025.37.

Archive only the user-selected computability variant. This does not assert
a polynomial, elementary or otherwise specified useful degree bound, and
does not resolve all interpretations of the historical quantitative question.
