# Active-card title review — 12 September 2026

Reviewed the titles of all **1,659 initially active cards** and renamed **1,148**.
Concurrent scientific reviews and pruning continued during this work. They
removed 95 cards, including 23 renamed here, leaving **1,125 title edits on
remaining cards** at the final audit. Their content changes and removals are
preserved and are not attributed to this naming review.

[titles.tsv](titles.tsv) records every reviewed ID, its outcome, and the before
and after titles for remaining cards. Concurrently deleted records retain only
their ID and removal reason. It is an audit, not a publication input. The only
source for current titles remains `data/cards/TCS-XXXX.json`.

Named problems now use their established names alone, for example
`Kannan–Lovász–Simonovits conjecture`, `Černý conjecture`, `Hadwiger’s conjecture`
and `Barendregt–Geuvers–Klop conjecture`. Standard class comparisons use forms
such as `P versus NP`. The editorial rule is recorded in
[docs/RULES.md](../../docs/RULES.md).

Descriptive titles were recovered from each card's saved question and working
summary. In particular, all 299 titles consisting of an article title and an
extraction locator were replaced with problem titles. Article headlines were
not treated as the selected question: examples include QMA versus QMA₁,
single-matroid parallel basis queries, and entropic versus submodular width.
The average length of the renamed titles fell from 88.1 to 44.9 characters.

Keep distinctions that change the target. The asymptotic Gotsman–Linial version
retains its qualifier; deterministic SETH and randomized SETH retain different
titles; the linear-size sample compression question is not silently upgraded
to compression of size exactly the VC dimension. Implications between named
conjectures are titled as implications, not as one endpoint. Equivalent named
problems may have identical titles on multiple existing IDs; this review did
not merge or remove cards.

The naming check used saved formulations and summaries, the existing source
references, and primary-source checks where identifying a standard name needed
confirmation. Representative checks:

- KLS: [Lee–Vempala survey](https://faculty.cc.gatech.edu/~vempala/papers/kls_survey.pdf).
- Sakoda–Sipser: [Pighizzini's automata survey](https://arxiv.org/abs/1208.2755).
- Barendregt–Geuvers–Klop: [weak versus strong normalization](https://doi.org/10.1016/S0304-3975(01)00012-3).
- Fourier Min-Entropy–Influence: [O'Donnell–Tan](https://www.cs.cmu.edu/~odonnell/papers/fei.pdf).
- Dürer: [Ghomi's affine unfoldings paper](https://ghomi.math.gatech.edu/Papers/durer.pdf).
- Conforti–Cornuéjols: [replication conjecture](https://arxiv.org/abs/2606.16543).
- Asser: [first-order spectra](https://www.csie.ntu.edu.tw/~tonytan/research/2018-lmcs-spec-3var.pdf).
- Freedman: [anchored rectangle packing](https://arxiv.org/abs/1401.0108).
- Recht–Ré: [original matrix-inequality conjectures](https://arxiv.org/abs/1202.4184).

This is a naming review, not a new formulation or open-status certification.
Existing draft limitations and dated status information remain in the cards.
In particular, finding a recognizable name does not promote an inherited
question to a reviewed open problem.

## Verification

Before the concurrent pruning, comparison of every one of the 1,148 edited
cards with its pre-edit record confirmed that **only `title` changed**. IDs,
statements, references, summaries, categories, rank inputs and statuses are
unchanged by this review. Later concurrent scientific edits also touched some
renamed cards; their complete content is preserved. No concurrent title changes
were overwritten.

`make publish` and the isolated `make check` suite passed for the completed title
edits. Both also passed on the final snapshot incorporating concurrent pruning
(1,582 records, version `1a1e3b14b60a2a9e617d`). All 1,125 remaining renamed titles
match the generated catalogue, and concurrently deleted IDs are absent.
