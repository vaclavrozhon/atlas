# Binary edit-distance distortion threshold

The owner requested replacing TCS-7297's determination of the optimal l1
embedding distortion up to constant factors by the question whether its
lower bound is `2^(Omega(sqrt(log n)))`. Omega is interpreted as the usual
capital-Omega lower bound: there exist constants `c > 0` and `n0 >= 2` such
that `D_ED(n) >= 2^(c sqrt(log_2 n))` for every integer `n >= n0`.
The target uses `sqrt(log n)`, with no log-log factor.

The statement, title, definitions, question type (`yes_no`), acceptance
criterion, summary and review metadata now express this single assertion.
Its precise negation permits a sequence of arbitrarily large violating
lengths for every positive `c`; it does not require a uniform little-o upper
bound over every length. The metric, all-pairs quantifiers, unrestricted
finite dimension and absence of algorithmic constraints are unchanged.
A matching upper bound and the optimal value of `c` are not required.

The [Ostrovsky–Rabani primary draft](https://web.cs.ucla.edu/~rafail/PUBLIC/68.pdf)
and [Krauthgamer–Rabani primary paper](https://www.wisdom.weizmann.ac.il/~robi/papers/KR-EmbedLB-SODA06.pdf)
were checked for their baseline upper/lower bounds and unit-substitution
convention. Neither cited bound decides the requested threshold. This is
an explicitly selected editorial question, not an identically worded
conjecture attributed to either paper. The previous review of matching
asymptotic growth is retained in `TCS-7297-before.json`; a fresh whole-catalogue
current-status audit remains deferred.

The stable ID, importance score 90, green default and existing category pair
(Computational geometry and metric spaces / String algorithms and
bioinformatics) are preserved. Only reader content changes; no selection
service update or selection write is needed.

Validation passed: publication updated only TCS-7297, all 39,715 active-card
math expressions parse, and the selection/taxonomy checks retain 504 static
green and 645 red cards, 35 categories and 480 category pairs. The selection
manifest remains `d51d7cb1b88fe12850c9`; the reader version is
`8f3ea5b38615c789e0c4`.

Published and verified on the live reader after GitHub Pages run 42190029747
completed successfully. The card is green, uses the specified quantified
lower bound and offers its String algorithms category move. Compact and full
views pass at 320, 390 and 1440 pixels with no math errors, page errors or
viewport overflow. All 22 existing shared decisions are unchanged, and the
browser check performed no selection writes. Live verification is recorded
in `live-check.json` and `shared-selection-check.json`.
