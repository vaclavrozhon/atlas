# Research-affinity selection audit

The user asked whether some cards entered the atlas because they were close to
his own research. This audit identifies plausible cases and separates a
documented research connection from an inference about selection bias. No cards,
scores, categories, status labels or focus selections were changed.

The strongest concern is concentration of related targets and source lists.
No inspected rationale explicitly says that personal relevance caused inclusion.
The findings therefore support a targeted selection reassessment, not a claim
that these problems lack independent scientific value.

## Evidence and method

The author's [research overview](https://vaclavrozhon.github.io/research/) and
[publication list](https://vaclavrozhon.github.io/research/papers/) establish the
relevant research connections. The current export was scanned for both accented
and unaccented author spellings; 34 arXiv identifiers linked from the publication
page were also compared with card references. That cross-check found no additional
reference matches with missing author attribution. The publication page itself
warns that it is not fully current, so this is not an exhaustive bibliography.
Saved card provenance, source labels, priorities and importance rationales were
then inspected. A wider topic scan included clustering, instance optimality,
shortest paths, heaps and local algorithms.

[audit.json](audit.json) records the exact catalogue version, counts, source
references and card assessments used here. It contains 14 cards that directly
cite work coauthored by the user; two are already marked resolved. Citation
alone is not a reason to exclude any of them.

Two measurable concentrations stand out:

- Four of the first ten ADS cards concern splay trees: dynamic optimality,
  deque operations, traversal and splitting.
- Thirteen of the first fifty distributed/parallel/sublinear cards derive from
  [Suomela's locality list](https://jukkasuomela.fi/open/). The export contains
  sixteen cards from that list in total, including two marked resolved. This
  documents source concentration, rather than thirteen separate personal
  research connections. The list is a primary source by another researcher,
  which is positive evidence of specialist motivation.

There is also a plausible historical mechanism. The
[editorial standard](../../docs/RULES.md) explicitly prioritized
developing data-structure, distributed and graph-algorithm cards. Earlier pruning
rules in the [selection policy](../../docs/RULES.md) preserved reviewed
cards. Preferential review could consequently help related cards survive before
the broader selection had been assessed evenly. This is an inference: the
priority was an authorized workflow choice and does not establish an improper
personal motive. The current standard also explicitly says review recency must
not raise importance, and the newer policy applies significance review to
previously completed cards too.

## First cards to reassess

The order below is an editorial recommendation. Ranks are within each card's
current category, as captured in the JSON snapshot.

| Card | Rank | Connection and assessment |
|---|---:|---|
| [TCS-6509: splay splitting](../../data/cards/TCS-6509.json) | ADS 10 | Its first reference is the user's 2026 splay paper and its motivation is a restricted structural target within the same adaptive-tree programme. This is one of the clearest candidates for reassessing whether it needs its own benchmark place alongside dynamic optimality, traversal and deque. |
| [TCS-6512: splay traversal](../../data/cards/TCS-6512.json) | ADS 8 | The user is a coauthor of the cited recent progress. The older Levy–Tarjan source gives independent motivation, but four closely related splay targets in the first ten ADS positions merit a joint diversity review. |
| [TCS-0518: non-signaling locality beyond log-star LOCAL](../../data/cards/TCS-0518.json) | Distributed 12 | Closely connected to the user's online/quantum locality work. Its high position in a bucket also covering parallel and sublinear algorithms deserves a stronger comparison of scientific consequences against other candidates. The source list supplies specialist support; personal influence is unproved. |
| [TCS-0523: sublogarithmic randomized VOLUME collapse](../../data/cards/TCS-0523.json) | Distributed 18 | Directly continues a gap conjecture in work by Brandt, Grunau and Rozhoň. Its placement should be reconsidered jointly with the deterministic VOLUME question and the other locality-landscape cards. These are different mathematical targets, not asserted duplicates. |
| [TCS-0516: dynamic-LOCAL bipartite three-coloring](../../data/cards/TCS-0516.json) | Distributed 22 | The corrected comparison paper is coauthored by the user. This more specialized model comparison is another plausible beneficiary of the locality source concentration. The underlying question was already posed by other authors. |

For the first two cards, coauthorship is verified on the primary
[2026 splay preprint](https://arxiv.org/abs/2607.18498). Being coauthor of recent
progress does not mean the user originated these older conjectures.

Three further candidates deserve a **joint** review rather than automatic
removal: [TCS-0513](../../data/cards/TCS-0513.json) and
[TCS-0514](../../data/cards/TCS-0514.json), the two unrooted-tree LCL decidability
questions at positions 14 and 15, and
[TCS-0515](../../data/cards/TCS-0515.json), deterministic VOLUME collapse at 17.
Their connections are direct, but the classification/decidability stakes provide
substantive independent reasons for inclusion. The concern is how many related
barriers this broad bucket should represent, not the mere fact of a common author.

The full source-cluster list in the JSON also exposes narrower parameter variants
and unfinished labels near the selection boundary: TCS-0517 (39), TCS-0525 (48),
TCS-0511 (49), and TCS-0512 (50). TCS-0526 is immediately outside at 51.
These warrant ordinary significance and formulation review; no direct personal
authorship connection was found in their saved references.

## Historical heap card

**TCS-0474**, pointer-machine working-set heaps with constant insertion and
decrease-key, is the strongest historical example to inspect. It follows the
same working-set/shortest-path programme as the user's research and directly
cites his heap work. The current selection policy records its removal and its
former focus place; it is absent from the current export.

The historical canonical card was recovered read-only from the repository's
initial commit and saved as
[historical-TCS-0474.json](historical-TCS-0474.json), including its commit and path.
It had importance 79 and a specific model-restriction target. Its original
problem contributor was John Iacono. The
[pointer-machine paper](https://arxiv.org/abs/2604.24134) is by van der Hoog,
Iacono, Rotenberg and Rutschmann, not by Rozhoň. The personal connection is to
the surrounding research programme and another cited paper; misattributing the
pointer-machine paper would overstate the evidence.

## Connected cards with strong reasons to keep

- [TCS-6498: dynamic optimality](../../data/cards/TCS-6498.json), ADS 1:
  a longstanding central adaptive-data-structure question. It should not be
  penalized for the user's recent contribution.
- [TCS-6506: deterministic logarithmic-round MIS](../../data/cards/TCS-6506.json),
  Distributed 13: a general algorithmic target for a basic task. The user’s
  network-decomposition paper is relevant background, not evidence of narrowness.
- [TCS-6508: splay deque](../../data/cards/TCS-6508.json), ADS 7:
  independently motivated over many years; a more defensible additional splay
  representative than retaining every member of that cluster. This is a
  comparative editorial judgment, not a claim of equivalence among conjectures.
- Distributed LLL, general parallel matching and reachability should likewise
  not be downgraded merely because they overlap the user's subject area.

[TCS-2735](../../data/cards/TCS-2735.json), uniform complexity beyond
logarithmic inverse error, is directly extracted from a paper coauthored by the
user. However, its provenance says automatic conference-paper extraction, and
its rank is 96 with an explicitly unassessed score of 50. It is a formulation
candidate outside this bucket's first fifty, not evidence of a personally
promoted benchmark slot. TCS-0520 and TCS-0521 are already marked resolved and
sit at positions 181 and 180; their continued historical presence should not be
counted as selected unresolved benchmark questions.

## Limits

This is an audit of provenance, concentration and editorial choices. It does not
recheck every theorem or certify current open status. Topic overlap is weaker
evidence than an explicit admission rationale. No numerical score changes or
deletions are implied by this report; the highest-priority recommendations above
identify where a broader comparative selection review would be most useful.
