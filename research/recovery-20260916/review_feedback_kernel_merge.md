# Directed feedback kernel consolidation

Reviewed 17 September 2026. TCS-7033 is consolidated into TCS-6379 under
the duplicate-consolidation rule in docs/RULES.md. This does not claim that
the general kernel question has been solved.

The published survey by Crespelle, Drange, Fomin and Golovach, Computer
Science Review 48 (2023), 100556, §3.1, p. 14, explicitly records reductions
in both directions under the same parameter before Open Problem 3.1.
The retained card already asks the vertex version with that parameter.
The arc version is therefore not an independent kernel-existence target.

For completeness, the elementary reduction check used for consolidation is:

- From arc deletion to vertex deletion, use the directed line graph: its
  vertices are the input arcs, and consecutive input arcs are adjacent.
  Deleting selected line-graph vertices corresponds to deleting those arcs.
  A directed closed walk contains a directed cycle, so the two residual
  graphs are acyclic together. Self-loops are handled by the same rule.
- From vertex deletion to arc deletion, split each vertex into an in-vertex
  and out-vertex with one distinguished arc between them. Replace every
  original arc by k+1 internally vertex-disjoint two-arc paths from its
  source out-vertex to its target in-vertex. First dispose of the trivial
  case k at least the number of input vertices, so this replication is
  polynomial in the explicit input length, even with binary budgets.
  A cut of at most k arcs cannot destroy every path in a bundle.
  The vertices whose distinguished arcs were cut must therefore hit every
  original directed cycle. Conversely, deleting the distinguished arcs of
  a vertex feedback set destroys all cycles in the construction.

Both constructions keep budget k. Composing either transformation with a
kernel for the other problem and the reverse transformation gives a kernel
for the original problem. Before any reverse replication, cap a kernel's
budget by the number of its vertices or arcs, as appropriate; larger budgets
are trivially YES. Thus a polynomial bound on the complete kernel encoding,
not merely its number of vertices, remains polynomial after composition.
This note checks the mathematical equivalence; it is not a Lean certificate.

The original TCS-7033 JSON is archived byte for byte. TCS-6379 gains the survey
reference and a June 2025 source that still distinguishes the open general
question from restricted-class kernels. Its formal target and assessed
importance remain unchanged. The answer criterion now states the existing
global Lean requirement explicitly.
