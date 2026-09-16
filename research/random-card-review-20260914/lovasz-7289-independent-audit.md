# TCS-7289 independent audit

Reviewed 16 September 2026. Root owns the claim and canonical update. This audit changes no canonical card, review selection, queue, claim, comment or publication.

## Verdict

The inert draft /tmp/atlas-draft-7289.py faithfully retains the general Lovász Hamiltonian-path question for finite nonempty connected vertex-transitive simple undirected graphs. Its formal assertion, definitions and full negative criterion are correct. No degree bound, Cayley representation, prescribed endpoint, closing edge, computational bound or constructive uniformity has been added. The existing assessed importance 88 and Structural graph theory category should remain unchanged.

The first inspected draft had an author error, “Ben Green Bedert”; the correct name is Benjamin Bedert. Root reports correcting it. The actual dense-paper PDF title page and arXiv metadata agree on Benjamin Bedert, Nemanja Draganić, Alp Müyesser and Matías Pavez-Signé. No other substantive defect was found.

## Exact mathematical target

Taking vertices to be [n] = {1,...,n}, with n >= 1 and E a set of two-element subsets, covers all finite nonempty simple undirected graphs up to isomorphism. Connectedness allows a walk of length zero from a vertex to itself. Vertex transitivity requires an adjacency-preserving permutation taking each chosen u to each chosen v; equality of degrees alone is insufficient.

A Hamiltonian path is a bijection p:[n]->[n] whose consecutive pairs are edges. For n=1 the condition over [0] is vacuous. There is no closing-edge condition. The exact negation is existence of one n and E satisfying connectedness and vertex transitivity such that every permutation has a missing consecutive edge. The draft correctly permits a proof of existence of such a graph without imposing an efficient counterexample search. The exact decision target does not acquire a numerical approximation tolerance.

The draft requires a complete Lean-checked proof of the positive assertion or its full negation. This audit checks the statement and source scopes, not a supplied Lean proof of the open conjecture.

## Primary sources actually inspected

1. Matija Bucić, Micha Christoph, Alexey Pokrovskiy and Raphael Steiner, *Towards the Lovász conjecture via sublinear expanders*, [arXiv:2606.09742v2](https://arxiv.org/abs/2606.09742v2).
   - Actual cached PDF/text: sources/lovasz-path2026.pdf and .txt.
   - Revision submitted 24 July 2026; the PDF title page is dated 27 July 2026. These dates should not be conflated.
   - PDF p. 1, abstract and introduction: the undirected conjecture asks for a Hamiltonian path; an eventual Hamiltonian-cycle conjecture is separately attributed to Thomassen.
   - Theorem 1.1, PDF p. 2: for every epsilon > 0 there is N(epsilon) such that every connected vertex-transitive n-vertex graph with n >= N(epsilon) contains a cycle of length at least n^(2/3-epsilon).
   - This is a nonspanning asymptotic guarantee. It does not establish the Hamiltonian-path assertion.

2. Benjamin Bedert, Nemanja Draganić, Alp Müyesser and Matías Pavez-Signé, *The Lovász conjecture holds for moderately dense Cayley graphs*, [arXiv:2603.08675v2](https://arxiv.org/abs/2603.08675v2).
   - Actual cached PDF/text: sources/lovasz-dense2026.pdf and .txt.
   - Initial submission 9 March 2026; inspected second revision 20 April 2026, 16 pages.
   - Theorem 1.2, PDF p. 2: there exists c >= 1/200 such that, for all sufficiently large n, every connected n-vertex Cayley graph of degree d > n^(1-c) has a Hamilton cycle.
   - Use the strict inequality from the theorem. The abstract instead writes a non-strict inequality.
   - Both the Cayley condition and degree condition restrict the theorem. It is not a solution for all connected vertex-transitive graphs.
   - The introduction's attribution of a universal Hamiltonian-cycle statement to Lovász is inaccurate and must not replace the path target. The main and directed papers state the path formulation correctly.

3. Bowen Li and Abhishek Methuku, *Long Directed Cycles in Vertex-Transitive Digraphs*, [arXiv:2607.05807v2](https://arxiv.org/abs/2607.05807v2).
   - Actual cached PDF/text: sources/lovasz-directed2026.pdf and .txt.
   - Initial submission 7 July 2026; inspected second revision 19 August 2026, 14 pages.
   - PDF p. 1, introduction: explicitly retains the undirected Lovász Hamiltonian-path and eventual-cycle conjectures as open.
   - PDF p. 2 defines the perimeter gap as order minus longest directed-cycle length. Theorem 1.3 gives infinitely many n with connected vertex-transitive digraphs whose gap is at least n/12.
   - The digraph result concerns directed cycles. Removing directions can introduce additional paths and cycles. Failure of a directed Hamiltonian cycle therefore supplies no counterexample to the general undirected Hamiltonian-path conjecture.
   - PDF p. 3 distinguishes underlying connectedness and strong connectedness; the later construction is strongly connected. The distinction does not change the preceding scope conclusion.

## Additional bounded later-work check

4. Tianlei Zhou, *On Hamilton cycles in connected vertex-transitive graphs of order 2pq*, [arXiv:2608.02349v2](https://arxiv.org/abs/2608.02349v2).
   - Newly cached actual PDF/text: sources/lovasz-audit-2pq2026.pdf and .txt.
   - Initial submission 3 August 2026; inspected second revision 30 August 2026. PDF author order is Tianlei Zhou; arXiv author metadata displays Zhou Tianlei.
   - PDF p. 1 correctly recalls the finite connected vertex-transitive Hamiltonian-path question and reports that no graph without such a path is known. The surrounding introduction retains the broader problem as open.
   - PDF p. 2, Theorem 1.2, concerns graphs of order 2pq with additional non-quasiprimitive group-action conditions involving prime-length orbits of a maximal intransitive normal subgroup.
   - PDF p. 3 explicitly fixes finite simple undirected graphs.
   - This is additional August status evidence and restricted progress, not a general resolution. The theorem proof was not independently verified in this review; the source can be used for status/scope without presenting it as a checked proof.

5. Domagoj Bradač and Oliver Janzer, *Hamiltonicity of regular sublinear expanders*, [arXiv:2605.15043v1](https://arxiv.org/abs/2605.15043v1), submitted 14 May 2026.
   - Newly cached actual PDF/text: sources/lovasz-audit-expanders2026.pdf and .txt.
   - PDF p. 1, abstract: Hamiltonicity under quantitative expansion and degree bounds, together with a bipartite-or-far-from-bipartite promise. These are additional assumptions, not properties asserted for every graph in the card's target.
   - Abstract/statement scope was checked; no independent proof validation is claimed.

The search also returned a 2026 algorithmic paper concerning the Győri–Lovász connected-partition theorem, arXiv:2608.30945. That is a different theorem and was excluded as a name collision.

The bounded primary-source check through 16 September 2026 found no verified solution to the general target. The inspected July and August sources explicitly retain the relevant path conjecture. Source-open status is supported as a bounded literature assessment, not an exhaustive certificate of all publications or proof correctness.

## Public-content guidance

The draft's three principal references already support its exact statement and status. The 30 August source is optional additional evidence and belongs in the audit even if omitted from the card for concision. No proof methods from any inspected paper are needed in the public statement or answer criterion. The five-sentence summary accurately states the graph model, path target, unrestricted scope, significance and complete positive/negative proof requirement.
