# Audit of the old parent-edge detection rule

Checked 11 September 2026. This audits the rule described in Section 3 of
Frank Vega, A Linear-Time Solution to the Triangle Finding Problem,
https://www.preprints.org/manuscript/202506.0875/v3 (19 August 2025).
It does not claim to execute the publisher's Figure A1 implementation or its
September 2026 replacement.

Graph: vertices 0,...,6; edges of the path 0-1-2-3-4-5-6 and edges
0-3, 3-6, 0-6. Exhaustive triple checking finds exactly one triangle, {0,3,6}.
A legal DFS tree is the entire displayed path: give each next path neighbour
priority. No edge of this tree belongs to any triangle. Thus every test restricted
to {parent(u),u,v} fails, even if v is not required to have been visited.
The paper's completeness argument does not cover a triangle consisting entirely
of back edges. A small local simulation and brute-force triangle check confirmed
these facts. This is a counterexample to the stated parent-edge rule.

The later manuscript https://www.preprints.org/manuscript/202511.2197/v10
(posted 8 September 2026) claims O(n²), which is not almost linear for all
sparse graphs. Its separate correctness claim was not adjudicated in this audit.
