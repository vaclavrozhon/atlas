# Broader large/small category options

The owner expected a large proportion of green cards to offer an up/down move.
The shared-state snapshot at the start of this review had 500 green cards, only
188 of them paired (37.6%). This pass adds 255 individually chosen alternatives,
bringing coverage to 443/500 (88.6%) and the total number of paired cards of
either color to 477. During the review the owner additionally selected TCS-0519
and TCS-4763 green; both also receive their natural Graph algorithms option.
The resulting coverage is 445/502 (88.6%), with 257 additions and 479 pairs in
total. The static proposal still contains 502 green cards; shared
human choices determine the different live total.

Each option connects exactly one large and one small category. Existing pairs,
editorial colors, default categories, mathematical statements, rankings, and
shared choices are preserved. A move retains the card's color and its original
computational model. These are available destinations, not automatic moves or a
new balancing pass.

The review used the saved statements, definitions, motivation, and current
category boundaries. Examples include distributed/streaming graph problems and
Graph algorithms; recurrence and matrix problems and Algebraic algorithms;
decidability questions and Computability; online-learning regret and Online
algorithms; query release and Database theory; quantum codes and Coding and
information theory. Small categories use different broad parents according to
their actual topic. Pure structural graph targets can return to Algorithms as
the broad home of graph-algorithm foundations without changing their existence
questions into construction problems.

Fifty-seven live green cards remain unpaired where a specialist counterpart
would be strained, including P versus NP, NEXP versus coNEXP, general convex
optimization, several language/logic foundations, and general cryptographic
primitive implications. A statistical learning distribution alone was not
treated as an average-case algorithmic model. The full decisions and per-category
coverage are in `review.json`; this editorial record is outside the published
reader. No whole-catalogue solvedness or numerical-precision audit was performed.

Validation passed: the editorial selection validator, all 14 service tests and
the production build, and the existing browser selection suite (including public
editing, persistence, concurrent edits, publication version skew, category
counters, map synchronization, and desktop/mobile layouts). An additional check
used the actual worker with an isolated SQLite database to exercise every one
of the 255 new pairs in both directions with both colors: 1,530 successful local
writes. No test wrote a shared live choice. Results are in `service-checks.json`
and `ui-checks.json`.

The two later additions receive the same service validation separately. The
backend manifest and reader must both be published for these new moves to be
available. Publication metadata and a read-only live verification are recorded
alongside this report after deployment.

Production verification succeeded on reader `1d09f7ccf87de07910fc` and service
manifest `36dc49cbcb490f59d0af`. The live reader reports 445 paired green cards
out of 502, with 479 pairs overall. Thirty-seven representative move buttons
were visible and enabled; long labels and both later additions were checked
in compact/full views at 320, 390, and 1440 pixels without overflow. No browser
errors or attempted selection writes occurred. All 21 saved choices present
before the final publication were returned completely unchanged afterward.
GitHub Pages run 42177882021 and Sites version 11 both deployed successfully.
