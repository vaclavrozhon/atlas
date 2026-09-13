# Atlas

An atlas of open problems in theoretical computer science, with a research source
library. Its purpose is to benchmark AI research on significant mathematical
questions. The catalogue contains candidates at different review stages;
inclusion alone does not certify current openness.

Our primary goal is a benchmark of **500 problems**. The **Top 100** is a
priority subset of those same 500, with secondary editorial attention. Both
share the same category order and ranking within each category. Selection and
review primarily develop the full Top 500.

The [project manifest](docs/MANIFEST.md) allows proposition, numerical and curve
questions, with Lean-checked answers and default absolute accuracy 0.01 for
numerical targets, including integers. Explicit exact targets such as BB(6)
use the answer representation specified on their card.
Scientific selection, precise statements, sources, categories and benchmark
success are defined in [docs/RULES.md](docs/RULES.md).
All project-authored content is English.

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

## Repository layout

| Path | Contents |
| --- | --- |
| [data/](data/README.md) | One complete JSON file per problem, category and selection registries, deleted IDs. |
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

Public notes and votes use the separately deployed [notes service](services/notes/README.md).
Shared thumbs-up/down scores determine the live order and Top selections within
each category, with the editorial order breaking ties. One changeable vote per
problem is remembered in each browser without login.
Visitors can post without an account and optionally add an unverified display name.
The submitting browser retains a deletion token. Existing GitHub notes and problem
proposals continue to load from GitHub issues.
