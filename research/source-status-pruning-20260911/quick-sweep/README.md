# Completed quick deletion sweep — 11 September 2026

The user authorized deletion of the second proposed ten and all clearly similar cases, requested coverage of every card, and explicitly assigned full review to a separate process.

The second ten were removed, then all 2,737 remaining card targets received a short skim and a scan of their saved descriptions, status notes and review outcomes. The initial text screen flagged 123 records. A supplementary summary scan and a short title/source overlap check caught additional candidates. Only selected source abstracts or identified passages were checked for the clear removal cases. This was not an exhaustive literature search, proof audit, or complete semantic deduplication review.

The sweep removed another 23 records: three duplicates or previously consolidated pointers, three already marked resolved by completed reviews, and seventeen historical questions settled by their source or a later identified result. Together with the second approved ten, this continuation removed **33** cards and left **2,714**. The earlier first approved ten are documented separately.

- `removals.json`: the additional 23 IDs and specific source-grounded reasons.
- `ledger.json`: a disposition for each of the 2,737 screened IDs.
- `full-review-handoff.json`: 36 retained cases with a concrete ambiguity or potential overlap for full review.
- `inventory.json`: the initial screening inventory, with removed entries reduced to IDs and reasons.
- `shared-source-groups.json`: source-overlap screening input, not a declaration that every group consists of duplicates.
- `validation.json`: counts, export integrity and test results.

The authoritative deletion log is `data/deleted_records.json`. Reserved identities remain in `data/id_registry.json`; no full deleted-card snapshots are retained by this cleanup. TCS-0310 and TCS-6543 already contained the bibliographies of their retired pointers. TCS-0677 now also contains the exact source formulation and locator formerly on duplicate TCS-4891. No focus selection needed replacement.

Other processes changed card contents and normalized their serialization during this pass. Their changes were preserved. The removal candidates were briefly rechecked after their hashes changed, and their new hashes were checked again before deletion. A changed byte hash in the ledger therefore does not necessarily mean the mathematical content changed. No newly added, unseen ID remained at validation.

Validation also exposed an existing timing assumption in the publication test: an independent command-line rebuild was compared against the exact timestamp of an earlier build. The test now allows only that timestamp to differ while continuing to compare all content metadata and check consistency among each build's exports. Browser checks passed. See `validation.json` for the completed offline check result.
