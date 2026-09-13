.DEFAULT_GOAL := help

PYTHON ?= python3
PORT ?= 8766
ATLAS := scripts

.PHONY: help serve publish deploy check check-web

help:
	@printf '%s\n' \
	  'make serve              Serve the reader at http://127.0.0.1:8766/' \
	  'make serve PORT=8767    Use a different port' \
	  'make publish            Apply editorial changes and refresh local exports' \
	  'make deploy             Publish and push the web reader to GitHub Pages' \
	  'make check              Isolated offline data and publication checks' \
	  'make check-web          Browser checks (Playwright and Chrome)'

serve: publish
	$(PYTHON) -m http.server $(PORT) --bind 127.0.0.1 --directory build

publish:
	$(PYTHON) $(ATLAS)/publish.py

deploy: publish
	$(PYTHON) $(ATLAS)/deploy_pages.py

check:
	$(PYTHON) scripts/check.py

check-web: publish
	node tests/map.cjs
	node tests/math.cjs
	node tests/math-browser.cjs
	node tests/pages.cjs
	node tests/deletions.cjs
	cd services/notes && npm test
	node tests/community.cjs
	node tests/votes.cjs
