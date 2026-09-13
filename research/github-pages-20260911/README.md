# GitHub Pages deployment

The atlas is live at https://vaclavrozhon.github.io/atlas/.

The `gh-pages` branch of `vaclavrozhon/atlas` contains the static reader, with
`.nojekyll` at its root. GitHub Pages publishes this branch automatically.
The remote repository was initially empty and private. Its account plan rejected
Pages for a private repository. After verifying that the only remote branch
contained exactly the 117 intended web files, it was made public and Pages was
enabled. The repository homepage points to the live atlas.

Run `make deploy` from the source workspace for subsequent updates. This rebuilds
the catalogue and pushes a locked snapshot using a temporary Git checkout,
preserving deployment history and the source working tree. The deployment helper
uses the existing SSH access; the authenticated GitHub API was needed for the
initial repository and Pages settings.

`deployment.json` records the deployed commit and dataset version, successful
GitHub build, HTTP response and live-browser checks. `build.log` and
`live-browser.log` contain the actual results. `qa/test_pages.py` also exercised
first and repeated pushes, deletion of obsolete assets, preservation of source
staging and rejection of an incomplete catalogue publication against a temporary
bare remote. `qa/pages.cjs` verified both a local project-path preview and the live
site, including assets, direct links, Top 100, JSON exports and mobile layout.
