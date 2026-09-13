# 100 removal candidates after the previous pruning

The [searchable table](proposal.html) and [complete report](proposal.md) contain
exactly 100 candidates selected after screening all 1,066 currently active cards.
The 36 already resolved cards are outside this proposal. No canonical card,
status, score, selection or deployment was changed.

The recommendation contains 4 historical questions answered by later work,
3 duplicate targets, 6 consolidations that require scope alignment, 2 problematic
extractions, and 85 comparative editorial cuts. Recommendation confidence is
high for 13, medium for 69, and borderline for 18. These are judgments about
removal, not certifications of mathematical truth or current open status.

All active cards received a title and saved-target-summary screen; 150 received
further assessment of the target, motivation and source locators. All 100 selected
cards have a current further assessment. The exact displayed fields are recorded
in `read-ledger.json`; the review does not claim that every card received a full
new formulation or literature audit. Targeted primary-source checks are in
[source-checks.json](source-checks.json).

The list is independent of scores, ranking, category sizes and formalization
effort. None of the twenty cards retained in the preceding 480-removal review is
included. Accepting all recommendations would leave 966 active cards, without
altering category quotas.

Several plausible cuts were reconsidered because their consequences were broader
than a first glance suggested:

- TCS-1714 links integral feasibility with efficient stable-coalition construction.
- TCS-4185 asks about intrinsic limitations of efficient statistical explanations.
- TCS-5422 would connect a basic fine-grained frontier to the weaker ETH assumption.
- TCS-3691 asks for a general VC uniform-convergence principle under weak dependence.
- TCS-5847 connects information usage with VC dimension across concept classes.
- TCS-0491 asks whether fixed dimension increases the query exponent of monotone fixed-point search.
- TCS-3917 would organize an entire forbidden-pattern tractability classification by its components.
- TCS-7163 tests whether efficient preprocessing changes proof-system simulation power.
- TCS-1259 tests bounded-depth expressive power even after removing every size restriction.

The all-field VF/VBP question TCS-2506 was not treated as a duplicate of the
complex-field determinant formula question. TCS-7203 was not called resolved by
complete connected cake-cutting impossibility: its explicit disposal permission
changes the target. TCS-5554 was not called solved by a subpolynomial saving or a
factor above three. These distinctions matter independently of editorial taste.

Artifacts:

- `candidates.tsv`: individually authored reasons and scope conditions.
- `proposal.tsv`: spreadsheet export with current titles and links.
- `decisions.json`: current hashes, bibliographic references and all decisions.
- `all-card-review.tsv`: every active ID and its proposed/not-shortlisted outcome.
- `baseline.json`: initial identities, status and hashes; no full-card backup.
- `read-ledger.json`: fields displayed during the screen and further assessments.
- `validation.json`: count, active status, coverage, hash and retained-link checks.

`python3 research/pruning-proposal-100-20260912/build_report.py` regenerates the
report only if the inventory and card bytes still match the reviewed snapshot.
It deliberately fails after subsequent card changes, so it cannot silently
present stale decisions as newly verified. Canonical files are never written.

No publication build is needed for this research-only report.
