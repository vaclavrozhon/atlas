# Benchmark selection policy

Persistent user decisions for the planned 1,000-problem benchmark. Apply these
when selecting, pruning, reviewing coverage, and proposing categories.

The agreed category lists, vacant slots, and separately labeled discussion
candidates are maintained in [CATEGORY_PLAN.md](CATEGORY_PLAN.md). Discussion
candidates are not approved category changes.

## 2026-09-10 — Second individual pruning of large categories

The user requested another 500–1,000 provisional removals, with every problem
and its individual reason printed in the conversation. The second pass reviewed
the remaining 2,134 large-category candidates and selected **543**, leaving
**1,591**. All 543 were listed and explained in the conversation. The complete
per-record rationale and exact archived cards are in
[to_delete/large-buckets-second-20260910/](to_delete/large-buckets-second-20260910/README.md).

Keep all three manifests active. This pass leaves the previous 2,069 large and
1,835 small removals in place. The small pool stays at 1,104 and the total active
pool is 2,695. These are candidate counts, not final benchmark quotas or verified
distinct currently open questions. Every reason was written individually from
the saved question and source context; no score threshold or equal removal share
was used. Reviewed cards and approved fundamental proposals were preserved.

A concurrent canonical review misrouted TCS-6572 to Beyond worst-case because its
first reference discusses smoothed analysis. Its question asks for worst-case
polynomial simplex pivots; an explicit override preserves its approved
Optimization and numerics placement. This correction is separate from removals.
The unaltered immediate pre-publication snapshot records that temporary error;
the archive manifest documents the corrected category census.

## 2026-09-10 — Preliminary importance pruning of small categories

The user requested reducing the small-category candidate pool to roughly 1,000,
with removals only provisionally moved to `to_delete/`. The pass screened 2,572
initial records plus 367 concurrent textbook/survey additions: **2,939 → 1,104**,
with **1,835 provisionally archived**. The 20-per-category quotas remain future
targets; this is not the final benchmark selection.

Decisions, original records, per-category counts and restoration instructions:
[to_delete/small-buckets-20260910/README.md](to_delete/small-buckets-20260910/README.md).
Keep both the large and small manifests active on every publication. Restore
records by changing their manifest state through the provided `restore.py`, so
later edits, references, stable IDs and browser notes survive. Do not reimport
archived records as fresh candidates or silently discard these decisions.

The review used saved questions and source topics, followed by a second reading
of ambiguous retained excerpts and a landmark-topic rescue pass. Prioritize major
barriers and broad problems over specialized variants, methodological follow-ups,
vague research directions and extraction fragments. Preserve reviewed cards and
approved fundamental proposals. Scores, source age and missing detailed text alone
were not removal rules. Remaining candidates still need precise formulation,
current-status verification, deduplication and final importance selection.

## 2026-09-10 — Preliminary importance pruning of large categories

The user requested reducing roughly 4,000 large-category candidates to roughly
2,000, with removals preserved provisionally under `to_delete/`. This supersedes
earlier descriptions of an entirely unpruned candidate pool. The final pass
screened 4,203 large-category records (including 105 concurrent additions),
archived 2,069 and retained 2,134. The 25 small categories were not pruned in that
pass; their separate pruning is recorded above.

Decisions and complete snapshots are in
[to_delete/large-buckets-20260910/README.md](to_delete/large-buckets-20260910/README.md).
The manifest is a persistent publication overlay; it must not be silently
ignored when reimporting proposals, source notes or reviewed cards. Restoration
changes an entry's state to `retained`, preserving all newer text and its ID.

Prioritize independent barriers, foundational conjectures and broad algorithmic
or decidability questions. Paper-local refinements, residual special cases,
non-problem passages, tooling tasks and repeated formulations can be archived.
Missing detail or an unassessed importance score alone is not grounds to discard.
A retained record is still a candidate, not a certified final top-1,000 choice.

## 2026-09-10 — Last small slot filled

Add **Beyond worst-case and average-case analysis** as small category 24, target
20. Miscellaneous is now 25 and stays last. There are 10 large and 25 small
categories, with no vacancies and total target 1,000. Includes smoothed analysis,
average-case hardness, planted/semi-random input models, instance-optimal algorithms
and algorithms with predictions. Kernelization remains a proposal only.

## 2026-09-10 — Structural graph theory accepted

The user has added **Structural graph theory** as a small category with a target
of **20 problems** (small 23 in the current plan; Miscellaneous remains last).
Its scope includes graph minors and decompositions; graph width parameters;
sparse classes and separators; hereditary classes and forbidden induced
subgraphs; and selected expansion/girth questions with computational relevance.
Structural bounds and characterizations belong here; algorithm running-time
questions normally belong in ADS or Parameterized and exact algorithms.

This accepted category supersedes the earlier exclusion of structural graph
theory within the agreed scope. General combinatorics remains largely excluded.
This addition left one small slot, subsequently filled as recorded above.

## 2026-09-10 — social choice and topology merges

- Merge the former small category 18, **Computational social choice**, into
  **Algorithmic game theory, mechanism design and fair division** (small 16,
  target 20). Voting and preference aggregation remain in scope.
- Merge **Computational topology** into **Computational geometry and metric
  spaces** (large 2, target 50), and remove its standalone small category.
- Preserve the destination names and their selection targets. These merges
  retained the topics and freed two small-category slots. The subsequently
  accepted Structural graph theory category fills one; Beyond worst-case and average-case analysis now fills the other.

## 2026-09-10 — large category 10: Optimization and numerics

The agreed name of large category **10** is **Optimization and numerics**, with
a target of **50 problems**. This replaces the shortened name **Optimization**.
Its scope continues to include mathematical optimization, numerical algorithms
and information-based complexity, as well as the previously absorbed online
algorithms, bandits and stochastic optimization. The rename makes the numerical
scope explicit; it does not add a category or change the selection target.

## 2026-09-10 — general combinatorics remains largely excluded

The earlier decision excluded both general combinatorics and structural graph
theory. The user has now accepted the scoped Structural graph theory category
above. General combinatorics outside the accepted categories remains
**excluded by default**, apart from selected edge cases.

- Do not create a general combinatorics category or reserve a quota for it.
  Its absence is intentional, not a coverage gap to fill in later audits.
- Retain only selected edge cases that fit the benchmark's computational scope.
  Place each retained exception in an appropriate existing category, or in
  **Miscellaneous** when no category fits clearly.
- Miscellaneous is for these occasional exceptions, not a way to retain the
  excluded fields wholesale.
- Graph algorithms remain in scope. Using combinatorial methods, or studying
  a structural result with a direct and important computational connection,
  does not by itself disqualify a problem. Judge the actual question.
- Do not exclude every record carrying an old graph/combinatorics label: the
  original categories mix algorithmic and structural work and contain labeling
  errors. Record a brief reason when retaining a borderline exception.

Do not use the accepted Structural graph theory category to restore general
combinatorics wholesale. Recording these decisions does not itself constitute
a completed record-by-record pruning pass.
