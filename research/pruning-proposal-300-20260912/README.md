# Editorial proposal for 300 removals

**Update, 12 September 2026:** [Six example cards have been removed or consolidated](applied-examples.md) after user approval. The original 300-card proposal below is historical; 294 recommendations remain unapplied by this change.

Start with the [searchable review table](proposal.html) or [complete report](proposal.md).
The [TSV](proposal.tsv) is suitable for a spreadsheet; [JSON](decisions.json) includes
retained IDs, current-card hashes and the review scope. No canonical data is changed.

`candidates.tsv` contains the individually authored editorial decisions.
`review.py` is a read-only card viewer that records fields and hashes in
`read-ledger.json`. `baseline.json` contains initial IDs, status and hashes only.
`pending-detail.json` is the larger screening shortlist, not an additional deletion list.
`build_report.py` renders the proposal and checks count, uniqueness, active status,
current detailed reads and retained-card references. It does not select candidates.

The original renderer was `python3 research/pruning-proposal-300-20260912/build_report.py`.
It validates that every proposed card still exists and has a current detailed
read; it intentionally cannot regenerate this historical snapshot after the
six approved removals. Keep the proposal and application receipt distinct.
