TCS-1246 individual review — 16 September 2026

Ready inert draft: /tmp/atlas-draft-1246.py.
Root owns the reservation; no canonical, queue, selection, comments or publication changed.

The target is exactly the general Eulerian weak-immersion conjecture, not the bounded-width theorem in the source title.

Model recovered from the actual full version:

- All finite directed multigraphs; loops and parallel arcs are explicitly allowed.
- Eulerian means in-degree equals out-degree at each vertex, with no connectivity requirement.
- Loops count once in each degree. Empty graphs, isolated vertices and edgeless graphs are included.
- Vertex map injective; each source arc maps to one nonempty directed trail with matching directed endpoints.
- Trails use distinct arcs individually and have mutually disjoint arc sets. Vertices may repeat or be shared, including branch vertices.
- A loop maps to a nonempty closed directed trail, never a zero-length route.
- The full source calls such trails “paths”; the draft expands the convention instead of importing vertex simplicity.

The exact positive quantifiers are ∀ infinite sequences ∃ i<j with G_i weakly immersing in G_j. The full negative is ∃ one infinite sequence ∀ i<j excluding that immersion. Neither sequence computability nor an algorithm choosing witnesses is required.

Primary locators:

- ICALP 2026 article 51, published 1 July 2026: PDF pp. 1–2 define the order/relation; p. 4 and footnote 6 omit connectivity; Conjecture 3.2 p. 8; Theorems 4.6–4.7 p. 13; Theorem 4.10 p. 17.
- Full arXiv 2605.07468v1, 8 May 2026: Conjecture 1.4 p. 6; finite incidence model pp. 7–8; trail convention Definition 2.4 p. 8; immersion Definition 2.12 and loop remark p. 10; quasi-order Observation 2.15 p. 11.
- Surface preprint 2509.26260v1, 30 September 2025: restricted scope in abstract p. 1; same general weak conjecture numbered 1.7 on p. 5.

Partial results do not resolve the target. The source proves strong WQO for a fixed carving-width bound, and weak WQO with bounded treewidth and at most one vertex above a fixed degree threshold. Its strong-immersion antichain does not exclude weak immersions.

Status nuance: the hosted author seminar abstract of 10 March 2026 says the authors believe they have proofs of both general conjectures. No complete proof accompanies the page. The later May and July sources still label the general weak statement a conjecture; isolated prose calling Conjecture 1.4 a theorem is not treated as a theorem proof. A bounded later primary review found no verified general resolution. Draft status is uncertain, with those different pieces of evidence clearly separated.

Individual importance 88 replaces the unassessed 50. It is motivated by the broad directed structural-ordering target and its finite-obstruction and fixed-property testing consequences. Graph category and legacy provenance remain intact.

Source cache prefix: eulerian-wqo-.
The draft has lowercase fields/notes/sources/status_note/summary, five English sentences, valid references and intact LaTeX. Its expressions passed the reader's bundled KaTeX check; this is artifact validation, not a Lean proof.
