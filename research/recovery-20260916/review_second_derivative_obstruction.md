# TCS-6885: literal constant-overhead Hessian target

The primary survey, Shpilka–Yehudayoff (2010), §2.3, printed pp.15–16
(Open Problem 5 on PDF p.21), literally discusses simultaneously computing
all second partial derivatives with a constant increase in circuit size.
The copied target has an elementary obstruction in the stated scalar-gate
model. This is an editorial mathematical check, not a newly attributed
published theorem or a claim of a completed Lean formalization.

Let `C(f)` count every input and binary arithmetic gate in a division-free
complex circuit for `f`. Let `H(f)` be the minimum gate count for a circuit
with outputs for all second partials; output designations may repeat and
are free. For

\[
p_n=\prod_{i=1}^n x_i,
\qquad C(p_n)\le 2n-1,
\]

the off-diagonal second derivatives, one per unordered pair, are

\[
\partial_i\partial_j p_n=\prod_{k\notin\{i,j\}}x_k
\qquad(1\le i<j\le n).
\]

For `n ≥ 4`, these are `n(n−1)/2` distinct monomials of degree `n−2 ≥ 2`.
Two different omitted pairs yield different exponent vectors. None of these
polynomials is a constant or an input variable. Thus each needs a distinct
internal gate as an output, regardless of sharing elsewhere in the circuit,
which proves `H(p_n) ≥ n(n−1)/2` even if input gates were free. Symmetry
between `(i,j)` and `(j,i)` and the zero diagonal have already been accounted
for; they do not remove this quadratic number of distinct values.

For any integer `K ≥ 1`, choose `n=4K+2`. Then

\[
H(p_n)\ge\frac{n(n-1)}2>2Kn\ge K(C(p_n)+1).
\]

Consequently there is no universal constant `K` for the literal assertion
`H(f) ≤ K(C(f)+1)`. This is an unconditional algebraic obstruction; it does
not rely on matrix multiplication hardness or a conjecture about its exponent.

The source's reduction through `x^T A B y` shows that a positive answer to
its literal assertion would imply quadratic-size matrix multiplication.
That implication does not show the premise is open: the product family above
already refutes it under the specified scalar-output model. No claim is made
about the authors' intended unstated modification.

Possible repaired targets such as `O(C(f)+n^2)`, implicit Hessian outputs,
Hessian-vector products, or a selected subset of partials are different
statements. None is silently substituted into this historical card.
An optional user choice between archival and an output-sensitive replacement
was asked on 17 September 2026. After independent work and no reply, the
recommended archival default was announced. A later choice of the new target
can be applied explicitly through the ordinary activity workflow.

The original first-derivative theorem and the copied question were read in
full at the locators above. Bounded later-source searches do not provide the
proof here; the displayed derivative identity and distinct-node counting do.
