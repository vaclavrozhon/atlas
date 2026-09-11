# Approved proposal import — 10 September 2026

The user requested adding all prepared proposals to the atlas. The import contains 72 retained large-category and 72 retained small-category suggestions, including the three second-round additions. The two questions shared across the research lists are counted once; rejected or held candidates are not imported.

The canonical seed batch is `../../proposals/fundamental-20260910.json`. `prepare.py` builds it from the accepted research lists and the individually written English translations in `../fundamental-additions-20260910/english-cards.tsv`. The batch remains at source-draft evidence; it is not a set of completed research cards.

`../../proposals.py` restores missing approved drafts using stable IDs in `../../id_registry.json`. It never overwrites an existing card. `../../publish.py` serializes concurrent publishers and produces the normal site exports. Explicit category and importance overrides continue to take precedence; later canonical detailed reviews retain their priority.

[publication.json](publication.json) maps every accepted suggestion to its atlas ID. [validation.json](validation.json) records counts, export parity, repeated-publication stability and preservation of concurrent canonical reviews. The pre-publication snapshot is local evidence for the preservation check. Browser checks are in `../../qa/proposals-results.json` and `../../qa/quick-results.json`.

To regenerate the seed batch, run `python3 atlas/research/import-fundamental-20260910/prepare.py` from the repository root, then `python3 atlas/publish.py`. Repeated publication adds no duplicates. Do not rerun the historical novelty scans against the newly published catalogue and interpret matches to these own new IDs as earlier duplicates.
