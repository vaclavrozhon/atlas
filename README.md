# Atlas

Research workspace moved from `/home/vasek/benchmark` to `/home/vasek/atlas`.

- [`tcs-open-problems/`](tcs-open-problems/): collection scripts, source data,
  research notes, catalogue exports, and the open-problems atlas.
- [`tcs-source-library/`](tcs-source-library/README.md): bibliography, source PDFs,
  extracted text, and annotated open questions.

## Open the atlas

From the repository root:

```sh
python3 -m http.server 8766 --bind 127.0.0.1 --directory tcs-open-problems/atlas/site
```

Open <http://127.0.0.1:8766/>. The reader also works by opening
`tcs-open-problems/atlas/site/index.html` directly. See the
[reader documentation](tcs-open-problems/atlas/site/README.md) and
[working notes](tcs-open-problems/atlas/WORKING_NOTES.md) for project details.
Historical notes may still refer to the former workspace path.

## Local files

All original files were preserved during the move. Download directories named
`cache/`, installed `node_modules/`, Python bytecode, and runtime publication
locks are kept locally and excluded from Git. Source data, research outputs,
source-library PDFs, and existing QA reports are versioned.

Browser-check dependencies can be restored with `npm ci` in
`tcs-open-problems/atlas/qa/`.
