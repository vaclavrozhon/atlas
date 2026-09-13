# Approved second-pass small-category import — 10 September 2026

The user explicitly requested adding all 26 prepared proposals to the atlas.
They are published as English source drafts in 24 small categories, with stable
IDs TCS-6659 through TCS-6684, source links, model distinctions and individually
assessed importance. No new Miscellaneous candidate was selected.

The canonical seed is `../../proposals/fundamental-small-second-20260910.json`.
`prepare.py` preserves the researched questions and bibliography and supplies
English importance reasons. The regular `../../publish.py` allocates IDs and
publishes the normal catalogue, ranking, offline data and live updates. It keeps
subsequent canonical reviews instead of replacing them with draft content.

`publication.json` maps all 26 proposals to IDs. `validation.json` records their
categories, content preservation and export parity, including concurrent full
reviews of older proposals. `browser-validation.json` records successful display
and search of all 26 cards, source links, direct navigation, note persistence,
selection export, mobile width and offline loading. The all-category ranking
check `python3 qa/ranking.py` passed for 6,683 records and 35 categories.

`finish.py` refreshes the latest-26 and combined-170 addition indexes and the
offline ZIP. The historical category-leader assertions in the ranking check were
replaced with a check of the highest current editorial score and stable ID tie
breaking, allowing newly approved higher-priority questions to lead a category.

To reproduce: run `prepare.py`, `../../publish.py`, then `finish.py`. The saved
before/after snapshots document this import; the research novelty audit predates
publication and must not be rerun to misclassify these own new IDs as duplicates.

[Latest 26 in the atlas](../../web/fundamental-small-second-additions.md) ·
[All 170 approved additions](../../web/fundamental-additions.md)
