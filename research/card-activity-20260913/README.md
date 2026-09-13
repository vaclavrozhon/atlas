# Active and inactive card migration

Implemented the user's decision of 13 September 2026:

- Active cards remain in `data/cards/`; routine editing, review, publication and
  validation use these cards only.
- Inactive content is retained in `data/archive/cards/`, outside normal work,
  search, rankings, selection and published exports.
- `data/archive/index.json` replaces the former deletion log and reserves IDs
  and historical import keys. The old reasons are preserved.
- `scripts/archive_cards.py` moves exact files, records decisions and removes
  archived focus selections. `--restore` requires an explicit editorial decision
  and validates only the requested card. Ordinary imports cannot restore cards.

The migration recovered 6,262 historical cards from saved Git and research
snapshots, then moved 37 already resolved cards intact out of active inputs.
The resulting archive holds 6,299 card files; the active directory holds 1,041.
Ten legacy inactive IDs have no recovered complete content and retain their
existing reasons. `data/archive/recovery.json` records every recovery source and
the missing IDs. Recovery preserves a historical snapshot, not a guarantee that
it was the last version before removal; it performs no mathematical review.

The one-time `migrate.py` is retained for provenance and refuses to rerun after
the legacy deletion index has been migrated. Future archival uses the regular
command, not this recovery script.

Regression coverage checks complete-file preservation, explicit restoration,
reserved IDs and aliases, focus and related links, removal deltas, untouched
archive contents, malformed historical content, and invalid batches/collisions.
Routine check snapshots omit archived card bodies; fixtures exercise the
mechanism without reviewing thousands of inactive cards.
