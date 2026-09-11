"""Prepare the user-approved short drafts from the two accepted research lists.

This does not promote a proposal to a completed research card. Publication is
performed by the regular publish.py command and uses the stable ID registry.
"""
import csv
import hashlib
import json
import re
import sys
from pathlib import Path
from urllib.parse import urlsplit, unquote

HERE = Path(__file__).resolve().parent
ATLAS = HERE.parents[1]
sys.path.insert(0, str(ATLAS))
from taxonomy import BIG, SMALL

LARGE = ATLAS / 'research/fundamental-additions-20260910'
SMALL_DIR = ATLAS / 'research/fundamental-small-20260910'

# Explicit editorial bands, based on the previously assessed significance.
SMALL_SCORES = {
    'densest-k':97, 'directed-steiner':96, 'tsp-four-thirds':95, 'atsp-gap-two':94, 'dfvs-constant':93,
    'fpt-w1':99, 'eth':98, 'setcover-exact':94,
    'seth':99, 'orthogonal-vectors':96, 'kclique':95, 'minplus-convolution':94, 'hitting-set-conjecture':93,
    'space-prg-optimal':97, 'ef-lower':99, 'modfrege':97,
    'logrank':98, 'fei':97, 'aaronson-ambainis':96,
    'gaussian-interference':97, 'deletion-capacity':96, 'information-inequality-decision':95, 'ldc-logqueries':94, 'c7-capacity':93,
    'permanent-determinantal':98, 'vp-vbp':97, 'determinant-formulas':96, 'finite-field-factor':95, 'finite-group-iso':94, 'permanent-exact':93,
    'factoring':99, 'discrete-log':98, 'svp-polyspace':95, 'least-nonresidue':94,
    'coloring-mixing':95, 'switch-chain':94,
    'trace':96, 'edit-near-linear':95,
    'dynamic-connectivity':97, 'dynamic-msf':96, 'dynamic-approx-matching':95,
    'general-perfect-matching':97, 'deterministic-permanent':96,
    'polynomial-hereditary-testing':95, 'pure-query-release-l2':94,
    'truthful-submodular':96, 'cake-queries':95, 'randomized-distortion':94,
    'pcsp-dichotomy':98, 'infinite-csp-dichotomy':97, 'three-colourable-constant':96,
    'unrelated-machines':97, 'santa-claus':96, 'binpacking-additive':95,
    'one-relator-monoid':96, 'one-relator-conjugacy':95, 'modal-k-unification':94, 'one-rule-termination':93,
    'query-enumeration':95, 'martin-conjecture':98, 'degree-rigidity':97, 'kl-ml':96, 'hindman-strength':95,
    'dnnf-equivalence':94, 'hadwiger':98, 'erdos-hajnal':97, 'gyarfas-sumner':96, 'seese':95, 'cereceda':94,
    'planted-clique':98, 'tensor-pca':96, 'smoothed-maxcut':94,
}

LARGE_CONTEXT = {
    'sample-compression': 'A claimed proof in arXiv:2603.23561 was withdrawn; its latest version identifies an error in Lemma 2. That claim is not treated as a resolution.',
    'qltc': 'Good quantum LDPC codes and the NLTS conjecture have been resolved; the additional local-testability requirement is essential here.',
    'kls': 'This is the KLS Poincare/isoperimetric question, not the distinct slicing conjecture.',
    'cpa-cca': 'The question allows general constructions; restricted black-box barriers do not settle the unrestricted implication.',
    'owf-pke': 'The question allows general constructions; a black-box separation alone does not settle it.',
    'owf-crh': 'A black-box separation alone does not settle the unrestricted implication.',
    'pke-ot': 'The question allows general constructions rather than only black-box reductions.',
    'fhe-no-circular': 'Leveled FHE, whose allowed evaluation depth is fixed during key generation, does not settle this formulation.',
    'distributed-lll': 'The target is worst-case round complexity over all nodes. A node-averaged O(log log n) result does not meet it.',
    'fo-trees': 'The intended signature is the ordered-tree/forest setting with descendant and sibling order. Results for restricted quantifier alternation do not give the full first-order characterization.',
    'poly-simplex': 'The algorithm is restricted to simplex pivoting but may depend polynomially on coefficient bit lengths. This is distinct from the unrestricted strongly polynomial linear-programming question.',
    'general-sparse-linear-systems': 'Solving sparse systems faster than matrix multiplication has already been achieved. The target here is nearly linear time, including the stated precision and condition-number regime. It is an editorial formulation of the general complexity question, not a named conjecture asserting a positive answer.',
    'li-li-network-coding': 'The conjecture concerns independent unicast sessions and undirected capacities. Multicast or directed-network coding gains do not refute it.',
    'deterministic-static-dictionary': 'The static membership primitive and deterministic preprocessing are essential; integer sorting, practical minimal-perfect-hash tuning, and restricted nonadaptive cell-probe questions have different targets.',
    'triangle-linear': 'The proposal records a linear-time target and the weaker almost-linear milestone. A completed benchmark card must choose the required asymptotic precision explicitly.',
    'bco': 'The exact bounded-domain, loss, and feedback conventions must be fixed when developing the full card; the cited sources supply the intended normalization.',
    'det-k-server': 'The target is deterministic k-competitiveness. It is not the separate randomized logarithmic-competitiveness conjecture.',
}


def normalized_title(text):
    return re.sub(r'[^a-z0-9]+', '', text.lower())


def source_key(url):
    return unquote(url).split('#')[0].rstrip('/').replace('http://', 'https://')


def main():
    raw = (ATLAS / 'site/catalog.json').read_bytes()
    catalog = json.loads(raw)
    large_all = json.loads((LARGE / 'candidates.json').read_text())
    large = [e for e in large_all['entries'] if e['status'] == 'shortlisted']
    small = json.loads((SMALL_DIR / 'shortlist.json').read_text())
    english = {e['key']: e for e in csv.DictReader((LARGE / 'english-cards.tsv').open(), delimiter='\t')}
    assert len(large) == len(english) == 72
    assert {e['key'] for e in large} == set(english)
    assert len(small) == 72 and {e['slug'] for e in small} == set(SMALL_SCORES)
    assert all(e['status'] == 'recommended_for_editorial_review' for e in small)
    refs_by_url = {}
    for c in catalog['cards']:
        for r in c['references']:
            refs_by_url.setdefault(source_key(r['url']), r)

    def references(urls):
        result = []
        for number, url in enumerate(dict.fromkeys(urls), 1):
            known = refs_by_url.get(source_key(url))
            if known:
                r = {k: known.get(k, '') for k in ['title','authors','year','url','pdf_url','locator']}
                r['url'] = url
            else:
                host = urlsplit(url).hostname
                arxiv = re.search(r'arxiv\.org/(?:abs|html|pdf)/(\d{4}\.\d+)', url)
                venue_year = re.search(r'LIPIcs\.[A-Za-z/-]+\.(20\d\d)\.', url)
                # A link label is not fabricated bibliographic metadata. The
                # author and date stay empty when the saved proposal lacks them.
                label = 'arXiv ' + arxiv[1] if arxiv else host
                year = 2000 + int(arxiv[1][:2]) if arxiv else int(venue_year[1]) if venue_year else None
                r = dict(title='Research reference · ' + label, authors='', year=year,
                         url=url, locator='', pdf_url=url if '.pdf' in url else '')
            r['id'] = 'primary' if number == 1 else f'ref{number}'
            result.append(r)
        return result

    cards = []
    for group, entries in [('large', large), ('small', small)]:
        for e in entries:
            slug = e['key'] if group == 'large' else e['slug']
            category = (BIG if group == 'large' else SMALL)[e['category']-1]
            text = english[slug] if group == 'large' else e
            formal, why = text['question'], text['importance']
            score = int(text['score']) if group == 'large' else SMALL_SCORES[slug]
            criterion = text.get('criterion', 'decision' if re.search(r'decid|algorithm', formal, re.I) else 'tightness')
            source_file = f'research/fundamental-{("additions" if group == "large" else "small")}-20260910/{("candidates" if group == "large" else "shortlist")}.json'
            refs = references(e['sources'])
            context = LARGE_CONTEXT.get(slug, '') if group == 'large' else e['novelty_note']
            context = (context + '\n\n' if context else '') + (
                'This short research proposal states the target identified in the September 2026 '
                'fundamental-problem search. The references give the source models and related '
                'results. A full self-contained formulation and detailed progress review remain to be written.')
            related = e.get('near_existing', []) if group == 'large' else sorted(set(re.findall(r'TCS-\d{4,}', e['novelty_note'])))
            cards.append(dict(key=f'fundamental-20260910-{group}-{slug}',title=e['title'],area=category,
                formal=formal,context=context,why=why,evidence='source',status='source_open',
                status_note='Retained in the source-based research proposal dated 10 September 2026. No full resolution was found in that search; this is not a completed independent open-status review.',
                review_note='User-approved research proposal, imported as a short draft. Its importance was assessed editorially; the full research-card standard has not yet been completed.',
                progress=[],references=refs,related=related,criterion=criterion,model_self_contained=False,
                requires_context=True,classification_method='editorial_proposal',importance_method='editorial',
                year=max((r['year'] for r in refs if isinstance(r.get('year'),int)),default=None),
                importance=dict(score=score,method='editorial',reason=why,assessed_on='2026-09-10'),
                proposal_import=dict(batch='fundamental-20260910',group=group,slug=slug,category=category,
                                     source_file=source_file,source_sha256=hashlib.sha256((ATLAS/source_file).read_bytes()).hexdigest(),
                                     research_date='2026-09-10')))

    assert len(cards) == len({c['key'] for c in cards}) == 144
    assert len({normalized_title(c['title']) for c in cards}) == 144
    known_titles = {normalized_title(c['title']):c for c in catalog['cards']}
    collisions = [(c['key'],known_titles[normalized_title(c['title'])]['id']) for c in cards
                  if normalized_title(c['title']) in known_titles
                  and known_titles[normalized_title(c['title'])].get('proposal_import',{}).get('batch') != 'fundamental-20260910']
    if collisions:
        raise ValueError(f'New exact-title collisions need semantic review: {collisions}')
    batch = dict(approved_on='2026-09-10',approval_basis='User: pridaj pak vse do atlasu',
                 scope='All 72 retained large-category and 72 retained small-category proposals; excluded and shared entries are not additional cards.',cards=cards)
    out = ATLAS / 'proposals/fundamental-20260910.json'
    out.parent.mkdir(exist_ok=True)
    tmp = out.with_suffix('.json.preparing')
    tmp.write_text(json.dumps(batch,ensure_ascii=False,indent=2)+'\n')
    tmp.replace(out)
    (HERE/'preparation.json').write_text(json.dumps(dict(
        catalogue_version=catalog['meta']['version'],catalogue_records=len(catalog['cards']),
        catalogue_sha256=hashlib.sha256(raw).hexdigest(),large=len(large),small=len(small),total=len(cards),
        excluded_large=[e['key'] for e in large_all['entries'] if e['status']!='shortlisted'],
        shared_not_counted=[e['slug'] for e in json.loads((SMALL_DIR/'shared-with-large-proposal.json').read_text())],
        references=len({r['url'] for c in cards for r in c['references']}),
        bibliography_reused=sum(not r['title'].startswith('Research reference · ') for c in cards for r in c['references'])
    ),indent=2)+'\n')
    print(f'Prepared {len(cards)} approved drafts in {out}')


if __name__ == '__main__':
    main()
