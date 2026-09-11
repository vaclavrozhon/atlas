"""Prepare the 26 approved second-pass proposals for the normal atlas publisher."""
import gzip
import hashlib
import json
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ATLAS = HERE.parents[1]
sys.path.insert(0, str(ATLAS))
from taxonomy import SMALL

BATCH = 'fundamental-small-second-20260910'
SOURCE = ATLAS / 'research' / BATCH / 'candidates.json'

# Individual English importance reasons; shared editorial scale from
# EDITORIAL_STANDARD.md. These are judgments, not measured rankings.
ASSESSMENTS = {
    'metric-k-median-optimal': (95, 'tightness', 'A central unresolved approximation threshold for metric clustering, asking for the final achievable ratio rather than a small improvement to one algorithm.'),
    'edge-multiway-cut-kernel': (93, 'resources', 'A central graph-cut kernelization problem: whether arbitrarily large instances can be compressed to size polynomial in the edge-deletion budget.'),
    'hyperclique-hypothesis': (95, 'resources', 'A principal fine-grained hardness hypothesis for higher-arity interactions, supporting a different network of conditional lower bounds from ordinary graph clique.'),
    'optimal-rip': (95, 'construction', 'A major gap between random and explicit constructions, asking for optimal sparse-signal measurements without randomness.'),
    'frege-extended-frege': (97, 'models', 'Determines whether naming intermediate formulas fundamentally shortens proofs, separating or relating two central propositional proof systems.'),
    'asymptotic-gotsman-linial': (95, 'tightness', 'A fundamental sensitivity bound for low-degree threshold functions with consequences for Boolean function analysis, learning, and circuit complexity.'),
    'broadcast-capacity': (97, 'characterization', 'One of the basic unsolved models of network information theory: one sender transmitting separate messages to two receivers.'),
    'shub-smale-tau': (98, 'resources', 'A central algebraic complexity conjecture whose truth would separate P and NP in computation over the complex numbers.'),
    'polynomial-factor-svp-algorithm': (97, 'decision', 'Asks whether Euclidean shortest vectors can be approximated within any fixed polynomial factor in polynomial time, a central gap between lattice algorithms and cryptographic assumptions.'),
    'critical-ising-3d': (93, 'resources', 'A fundamental question about efficient sampling at a phase transition in the standard three-dimensional Ising model.'),
    'msa-below-two': (92, 'tightness', 'A principal approximation barrier for a core bioinformatics optimization problem, requiring a constant improvement independent of the number of sequences.'),
    'dynamic-global-mincut': (95, 'resources', 'A basic unresolved question about maintaining whole-network resilience under updates, for the exact global cut at arbitrary connectivity.'),
    'euler-tours-fpras': (93, 'decision', 'A canonical unresolved approximate-counting problem for natural graph traversals, distinct from the tractable approximation of Eulerian orientations.'),
    'bounded-degree-isomorphism-testing': (92, 'resources', 'Tests the fundamental power of sublinear access to compare two sparse graphs without reading the entire input.'),
    'pure-dp-continual-counting': (94, 'tightness', 'Continual counting is a basic privacy primitive; the target is the optimal price of pure privacy across the entire stream.'),
    'randomized-truthful-scheduling': (96, 'models', 'A central mechanism-design question about whether randomness can overcome the efficiency loss imposed by truthful cost reporting.'),
    'pcsp-search-decision': (96, 'reductions', 'Would establish the relationship between deciding feasibility and constructing solutions across the full class of finite promise constraint satisfaction problems.'),
    'precedence-makespan-below-two': (96, 'tightness', 'A classical major scheduling problem asking whether general precedence constraints permit a constant improvement over list scheduling.'),
    'one-relator-isomorphism': (95, 'decision', 'One of the classical decision problems for a fundamental class of finite group presentations, asking for the boundary of algorithmic decidability itself.'),
    'monadic-nip-model-checking': (96, 'characterization', 'A central proposed characterization of graph classes supporting efficient logical query evaluation, linking finite model theory, database theory, and graph structure.'),
    'turing-equivalence-universal': (95, 'characterization', 'Asks whether equality of computational power can represent every countable Borel classification problem, a classical bridge between computability and descriptive set theory.'),
    'sroiq-cq-decidability': (95, 'decision', 'A basic unresolved decidability boundary for querying expressive ontologies: decidable satisfiability does not automatically provide decidable query entailment.'),
    'dnf-ddnnf-succinctness': (93, 'resources', 'Determines the representation-size cost of determinism when compiling knowledge into a form supporting exact model counting.'),
    'reed-colouring': (97, 'characterization', 'A major structural colouring conjecture seeking a universal relationship among maximum degree, clique size, and chromatic number.'),
    'optimal-excluded-grid': (96, 'tightness', 'A foundational quantitative question in graph minor theory, controlling grid obstructions to small treewidth and their algorithmic applications.'),
    'sbm-ks-threshold': (96, 'tightness', 'A canonical statistical-versus-computational gap: whether the Kesten–Stigum threshold is the true efficient-recovery barrier for sparse communities.'),
}

def normalized(s):
    return re.sub(r'[^\w]+', '', s.casefold())

def main():
    raw = SOURCE.read_bytes()
    candidates = json.loads(raw)
    current_raw = (ATLAS / 'site/catalog.json').read_bytes()
    current = json.loads(current_raw)
    assert len(candidates) == len(ASSESSMENTS) == 26
    assert {e['key'] for e in candidates} == set(ASSESSMENTS)
    assert all(e['status'] == 'recommended_for_editorial_review' for e in candidates)
    snapshot = HERE / 'prepublication-catalog.json.gz'
    if not snapshot.exists():
        with gzip.open(snapshot, 'wb') as f:
            f.write(current_raw)
    known_refs = {r['url']: r for c in current['cards'] for r in c['references']}
    cards = []
    for e in candidates:
        score, criterion, why = ASSESSMENTS[e['key']]
        category = SMALL[e['category'] - 1]
        assert category == e['category_name']
        references = []
        for i, source in enumerate(e['sources'], 1):
            url = source['url']
            old = known_refs.get(url, {})
            arxiv = re.search(r'arxiv\.org/(?:abs|html|pdf)/(\d{4})\.\d+', url)
            # Unknown metadata stays unknown; the research date is not the source year.
            year = old.get('year') or (2000 + int(arxiv[1][:2]) if arxiv else None)
            references.append(dict(id='primary' if i == 1 else f'ref{i}',
                title=source['title'], authors=old.get('authors', ''), year=year,
                url=url, locator=source.get('locator', ''),
                pdf_url=url if url.split('#')[0].endswith('.pdf') else old.get('pdf_url', '')))
        cards.append(dict(
            key=f'{BATCH}-{e["key"]}', title=e['title'], area=category,
            formal=e['question'], context=e['status_note'] + '\n\n' + e['novelty_note'],
            why=why, references=references, progress=[], criterion=criterion,
            evidence='source', status='source_open',
            status_note='Retained in the source-based research proposal dated 10 September 2026. ' + e['status_note'],
            review_note='User-approved research proposal, imported as a short draft. The cited sources and model distinctions were checked in the research pass; this is not a completed independent proof or full-card review.',
            related=e.get('near_existing', []), model_self_contained=False, requires_context=True,
            classification_method='editorial_proposal', importance_method='editorial',
            year=max((r['year'] for r in references if isinstance(r['year'], int)), default=None),
            importance=dict(score=score, method='editorial', reason=why, assessed_on='2026-09-10'),
            proposal_import=dict(batch=BATCH, group='small', slug=e['key'], category=category,
                source_file=str(SOURCE.relative_to(ATLAS)), source_sha256=hashlib.sha256(raw).hexdigest(),
                research_date='2026-09-10', rank_in_research_category=e['rank_in_category'])))
    titles = {normalized(c['title']): c for c in current['cards']}
    collisions = [(c['title'], titles[normalized(c['title'])]['id']) for c in cards
        if normalized(c['title']) in titles and titles[normalized(c['title'])].get('proposal_import', {}).get('batch') != BATCH]
    assert not collisions, collisions
    assert len({c['key'] for c in cards}) == len({normalized(c['title']) for c in cards}) == 26
    batch = dict(approved_on='2026-09-10', approval_basis='User: pridej pak vse do atlasu',
        scope='All 26 retained second-pass small-category proposals, in 24 categories. Earlier imported proposals and rejected or held candidates are not added again.', cards=cards)
    target = ATLAS / 'proposals' / (BATCH + '.json')
    temp = target.with_suffix('.json.preparing')
    temp.write_text(json.dumps(batch, ensure_ascii=False, indent=2) + '\n')
    temp.replace(target)
    (HERE / 'preparation.json').write_text(json.dumps(dict(batch=BATCH, prepared=len(cards),
        categories=len({c['area'] for c in cards}), source_sha256=hashlib.sha256(raw).hexdigest(),
        prepublication_count=len(current['cards']), prepublication_version=current['meta']['version']), indent=2) + '\n')
    print(f'Prepared {len(cards)} approved English source drafts: {target}')

if __name__ == '__main__':
    main()
