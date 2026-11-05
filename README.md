# Atlas

An atlas of open problems in theoretical computer science, with a research source
library. Its purpose is to benchmark AI research on significant mathematical
questions. The catalogue contains candidates at different review stages;
inclusion alone does not certify current openness.

The final-selection proposal contains **500 green problems**: 25 in each of ten
large categories and 10 in each of twenty-five small categories. Every other
active card is red. Green/red decisions are separate from scientific status,
votes and the older Top 100/500/1000 ranking views. Editors can change colors and
move suitable cards between one specific large and one specific small category;
shared counts may be above or below target. See the
[finalization record](research/final-selection-20261105/README.md).

The [project manifest](docs/MANIFEST.md) allows proposition, numerical and curve
questions, with Lean-checked answers and default absolute accuracy 0.01 for
numerical targets, including integers. Explicit exact targets such as BB(6)
use the answer representation specified on their card.
Scientific selection, precise statements, sources, categories and benchmark
success are defined in [docs/RULES.md](docs/RULES.md).
All project-authored content is English.

Only **active** cards in `data/cards/` receive routine editorial work. Inactive
cards keep their full contents in `data/archive/cards/` and are absent from the
reader, exports and benchmark selection. Pruning archives a card instead of
erasing it; reactivation requires an explicit user request. See the
[manifest](docs/MANIFEST.md) for this policy.

## Everyday work

Python 3.10+ and Make are sufficient for publication and data checks.

```sh
make serve      # build and serve at http://127.0.0.1:8766/
make publish    # rebuild the reader and exports in build/
make check      # isolated data, clean rebuild and deployment tests
make check-web  # build and run browser checks (Playwright and Chrome)
make deploy     # build and push the reader to GitHub Pages
```

Choose another port with `make serve PORT=8767`. After building, the reader also
opens directly from [build/index.html](build/index.html).

For the active card completion pass, use the
[unfinished-card inventory](research/card-completion-20260913/unfinished.md) and
[parallel review workflow](research/card-completion-20260913/README.md#parallel-review-workflow).
Before starting a card in a shared checkout, reserve it with
`python3 scripts/review_queue.py claim --worker YOUR_PROCESS_NAME`.

## Repository layout

| Path | Contents |
| --- | --- |
| [data/](data/README.md) | Active cards, a separate inactive archive, category and selection registries. |
| [web/](web/README.md) | Reader source assets. |
| [services/notes/](services/notes/README.md) | Account-free public notes API and durable storage. |
| `build/` | Generated reader and exports, ignored by Git and safe to rebuild. |
| [scripts/](scripts/) | Publication, import, validation and deployment code. |
| [tests/](tests/README.md) | Data, publication and browser checks. |
| [docs/RULES.md](docs/RULES.md) | Current editorial and repository rules. |
| [research/](research/README.md) | Research conclusions, sources and ongoing reviews. |
| [library/](library/README.md) | Independent bibliography, PDFs, texts and annotations. |

Edit `data/cards/TCS-XXXX.json` to change a problem. Its statement, sources,
category, importance and working summary live together. `make publish` derives
the reader without rewriting these inputs or recovering content from old outputs.
See [data/README.md](data/README.md) for imports and removals.

## Deployment

The reader is published at **https://vaclavrozhon.github.io/atlas/**.
`make deploy` copies `build/` into a temporary checkout and pushes an ordinary
commit to `origin`'s `gh-pages` branch. The source checkout and index stay unchanged.
In GitHub Settings → Pages, use branch `gh-pages`, directory `/`.

After building, `python3 scripts/deploy_pages.py --dry-run` validates the local
snapshot without uploading it. Library and research files are outside the
published directory.

Votes and shared selection use the separately deployed
[service](services/notes/README.md). Thumbs-up/down scores determine live order
within categories, with editorial priority breaking ties. Green/red decisions
persist independently and require the shared editor key. Existing community
feedback is preserved in `research/community-feedback-20261105/` and in the
service, but the final reader neither loads nor displays it. New problem proposals
can still be submitted through the GitHub form.
