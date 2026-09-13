# Four further candidates

Additional literature check on 13 September 2026, following the request for
alternatives to the two grid-class equalities. No canonical cards were added.
The emphasis here is on individual combinatorial tasks.

## Finitary factor-of-i.i.d. perfect matching on a regular tree

For a fixed integer \(\Delta\geq 3\), does the infinite regular tree
\(T_\Delta\) admit an \(\operatorname{Aut}(T_\Delta)\)-equivariant finitary
factor-of-i.i.d. perfect matching? Vertices receive independent uniform
\([0,1]\) labels. The matching choice at a vertex must be determined by some
almost surely finite neighborhood. There is no supplied edge coloring that
would already specify a matching.

[Grebík–Vidnyánszky, *From descriptive to distributed*, Problem 9.5](https://arxiv.org/html/2502.15347#S9)
states this explicitly; Section 7.1 discusses the known FIID matching. Preserve
the distinction between measurable factors and finite coding radii. Do not
add a prescribed tail bound or a finite-program computability requirement to
the existence question.

## Measurable three-coloring for free actions of the rank-two free group

Does every free Borel action of \(\mathbb F_2=\langle a,b\rangle\) on a
standard probability space \((X,\mu)\) admit a \(\mu\)-measurable proper
three-coloring of its Schreier graph for \(a^{\pm1},b^{\pm1}\)?
These graphs have components isomorphic to the four-regular tree. The
measure need not be invariant. This is
\(3\text{-}\mathsf{Col}(\mathbb F_2)\in\mathtt{MEASURE}(\mathbb F_2)\).

[Bernshteyn, *Complexity of Local Problems*, ICM 2026, Problem 7.7](https://epubs.siam.org/doi/10.1137/25M1807563)
explicitly asks this. It concerns every free action, not only the Bernoulli
shift or arbitrary unstructured four-regular Borel forests.

## Measurable Molloy bound for triangle-free graphs

For every \(\varepsilon>0\), is there a \(\Delta_0\) such that every
triangle-free Borel graph of finite maximum degree \(\Delta\geq\Delta_0\)
and every Borel probability measure \(\mu\) on its vertices satisfy
\(\chi_\mu(G)\leq(1+\varepsilon)\Delta/\log\Delta\)?

[Bernshteyn, *Distributed Algorithms, the Lovász Local Lemma, and Descriptive Combinatorics*, Problem 3.11](https://arxiv.org/html/2004.04905v7#S3.SS2)
states this question. The same paper's Theorem 3.9 gives the coefficient
\(4+\varepsilon\) for triangle-free graphs and \(1+\varepsilon\) when
four-cycles are also excluded. The discussion following Theorem 1.18 in
[Bernshteyn–Weilacher](https://arxiv.org/html/2308.14941v2#S1.SS1)
retains the analogous coefficient-one issue for Borel coloring with finite
asymptotic separation index. Neither fractional coloring results nor merely
finite-graph Molloy bounds establish the proposed measurable statement.

## Borel unfriendly coloring with bounded degree

Does every Borel graph with finite maximum degree admit a Borel coloring
\(c:V(G)\to\{0,1\}\) such that every vertex has at least as many neighbors
of the opposite color as of its own color? Equivalently, the cut is locally
optimal under changing one vertex's side.

[Grebík–Vidnyánszky, Problem 9.7](https://arxiv.org/html/2502.15347#S9)
asks this. The
[10 September 2026 preprint by Pelayo-Gómez](https://arxiv.org/html/2609.11919)
reports a counterexample with unbounded degree and explicitly retains the
bounded-degree question in its concluding discussion. Treat the new result
as a preprint claim; its proof was not independently audited here. Its cubic
forest reduction is relevant context, not grounds for silently restricting
the source problem to degree three.

## Editorial assessment and checks

The matching question has the most direct operational connection to local
algorithms. The three-coloring question is a particularly compact target
explicitly highlighted by Bernshteyn in 2026. These would be my first two
choices from this additional group. The Molloy question adds a general
coloring theorem; unfriendly coloring links local optimality with Borel
definability.

Targeted searches found no subsequent resolution of these exact targets.
Canonical-card and deletion-reason searches found no matching records.
The matching and unfriendly formulations are not attributed to Bernshteyn
personally; their connection to his research is through the shared locality
framework. These remain candidate recommendations, not completed card audits.
