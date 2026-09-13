# Authorship and validation

All 1,591 active large-bucket records are frozen in `manifest.json`; descriptions
are intermediate English explanations, not new reviewed cards or a current-status audit.

Final work split after balancing:
- Root: quantum 128, cryptography 68, learning 40 (236).
- Algorithms agent: algorithms 271, complexity 138, distributed 86 (495).
- Geometry agent: geometry 212, optimization 146, learning 87 (445).
- Logic agent: automata 149, semantics 180, distributed 86 (415).

Each description has five individually authored sentences and supporting external
source URLs. Saved full source passages were consulted for imported question
locators, mathematical restrictions, and introductory questions solved later in
the same paper. Specific caveats are retained in each authoring file's `note`;
`validation.json` collects them. Root reviewed a sample across categories and
separately reviewed the four ambiguity cases 6199,1560,4661,3142 flagged by the
geometry agent.

Publication combines this work with the independently authored small-bucket
summary overlay. Original card content is compared against the compressed
baseline, including status, evidence, rank, archive selection and references.
The offline publication regression tests exercise changes and removals in both
authoring formats. Browser checks cover ten large categories, visible prose and
citations, live changes preserving notes and focus, escaping, mobile layout and
offline reading. The existing small-category browser check also passes after the
shared UI adjustment that removes duplicate full statements on reviewed cards.

Run after publication:
```sh
python 3 tcs-open-problems/atlas/qa/descriptions.py
node tcs-open-problems/atlas/qa/large-descriptions.cjs
```

The algorithms agent independently reviewed root descriptions 0679, 0680, 1157,
1305, 1315 and 1361 against their full saved sources. The review led to an
explicit proper-learner restriction in 0679; no material corrections were needed
for the other five.
