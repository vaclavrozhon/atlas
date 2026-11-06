# Short cycle decomposition addition

The owner requested short cycle decomposition if absent and selected it green.
The active catalogue had no card for this task. Added **TCS-7525**,
**Near-linear-time short cycle decomposition**, in **Graph algorithms**, with
**Algorithms** as its single broad alternate category. The static proposal now
contains 503 green and 646 red cards; Graph algorithms has 11 against its target
of 10. Existing selections, including the shared red choice for TCS-6173, are
independent persistent records and must remain intact.

The selected baseline asks for one uniform randomized algorithm running in
`(n+m) polylog(n)` time, partitioning the edges into edge-disjoint simple cycles
of length `polylog(n)` and at most `n polylog(n)` leftover edges. All logarithmic
powers are fixed globally. The graph is simple, undirected and unweighted;
cycles may share vertices. The card specifies the word-RAM model, explicit
input/output, success probability and worst-case time. A separate sharper
variant would require `O(log n)` cycle length and `O(n)` leftover edges at the
same running time; this is not silently imposed. An optional clarification
about these two variants was offered, and the baseline was stated as the
working choice while the work continued.

Primary sources checked on 6 November 2026:

- Chu et al., FOCS 2018, [arXiv:1805.12051](https://arxiv.org/abs/1805.12051):
  the definition, existing decomposition quality, slower construction, and
  algorithmic applications.
- Parter and Yogev, [ICALP 2019](https://doi.org/10.4230/LIPIcs.ICALP.2019.89),
  Definition 1 and Theorems 2–3: the tradeoff between construction time and
  decomposition quality. The card uses theorem numbering from the published
  conference version, not the differently numbered full manuscript.
- Lawrence Li's [Toronto seminar announcement](https://www.cs.toronto.edu/tss/talks-list.html),
  14 February 2024: explicitly describes the near-linear-time improvement as open.
- Ding et al., [ITCS 2025](https://doi.org/10.4230/LIPIcs.ITCS.2025.43), Lemma 17:
  near-linear space with the almost-linear running-time guarantee retained.

A bounded search for later work included 2025/2026 short-cycle results and
indexed OpenAI math material. No verified resolution of this precise target
was identified. Results about weighted resistance-based graph contractions or
cycles in cubic graph pursuit games do not establish the requested unweighted
edge partition and simultaneous bounds. The card remains `source_open`, not a
claim of exhaustive current-status verification. This targeted addition does
not resume the deferred whole-catalogue audit.

Source-default green is also recorded as an explicit shared green choice when
the new service manifest is deployed, subject to the service's per-card
revision checks. Other shared choices are never rewritten. Deployment and
validation records are saved alongside this report.

Validation passed: the isolated publication/ranking/taxonomy/selection/import/
archive checks (`make check`), the active-card KaTeX check (39,701 expressions),
all 14 service tests and its production build, and the browser selection suite
covering shared edits, category moves, persistence, conflicts, publication
compatibility, counters and mobile layouts. No existing editorial selection
default changed. Live verification follows deployment.
