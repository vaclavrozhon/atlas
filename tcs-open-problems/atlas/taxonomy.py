"""Agreed selection categories. Topic routing is not an open-status review.

Keep original subjects and all records, including auditable scope exclusions.
Use saved questions and primary source titles, never generated background prose.
"""
import collections
import json
import re
import unicodedata
from pathlib import Path

BIG = [
    'Quantum computation',
    'Computational geometry and metric spaces',
    'Computational complexity',
    'Algorithms & data structures',
    'Learning theory',
    'Cryptography',
    'Distributed, parallel and sublinear algorithms',
    'Automata and formal languages',
    'Semantics, logic and verification',
    'Optimization and numerics',
]
SMALL = [
    'Approximation algorithms and hardness of approximation',
    'Parameterized and exact algorithms',
    'Fine-grained complexity',
    'Pseudorandomness and derandomization',
    'Proof complexity',
    'Communication complexity and Boolean function analysis',
    'Coding and information theory',
    'Algebraic computation',
    'Lattices and computational number theory',
    'Randomized algorithms and sampling',
    'String algorithms and bioinformatics',
    'Dynamic graph algorithms',
    'Counting and enumeration',
    'Property testing and distribution learning',
    'Differential privacy',
    'Algorithmic game theory, mechanism design and fair division',
    'Constraint satisfaction',
    'Scheduling and packing',
    'Automated reasoning and unification',
    'Database theory and finite model theory',
    'Computability and algorithmic information',
    'Knowledge representation and reasoning',
    'Structural graph theory',
    'Beyond worst-case and average-case analysis',
    'Miscellaneous',
]
NAMES = BIG + SMALL
(QUANTUM, GEOMETRY, COMPLEXITY, ADS, LEARNING, CRYPTO, PARALLEL,
 AUTOMATA, SEMANTICS, OPTIMIZATION) = BIG
(APPROXIMATION, PARAMETERIZED, FINE, RANDOMNESS, PROOF, COMMUNICATION,
 CODING, ALGEBRA, LATTICES, SAMPLING, STRINGS, DYNAMIC, COUNTING,
 TESTING, PRIVACY, GAME, CSP, SCHEDULING, REASONING, DATABASE,
 COMPUTABILITY, KNOWLEDGE, STRUCTURAL, BEYOND, MISC) = SMALL
OUTSIDE = 'Outside selection scope'
DIRECT = {name: name for name in NAMES}
DIRECT.update({
    'Computational geometry': GEOMETRY,
    'High-dimensional data and metric spaces': GEOMETRY,
    'Computational topology': GEOMETRY,
    'Existential theory of the reals': GEOMETRY,
    'Computational and circuit complexity': COMPLEXITY,
    'Average-case complexity': BEYOND,
    'Graph theory and graph algorithms': ADS,
    'Data structures and compressed data': ADS,
    'Temporal graph algorithms': ADS,
    'Distributed, parallel and streaming algorithms': PARALLEL,
    'Distributed and local algorithms': PARALLEL,
    'Streaming and sketching': PARALLEL,
    'Games, synthesis and verification': SEMANTICS,
    'Infinite-state systems and verification': SEMANTICS,
    'Rewriting, lambda calculus and semantics': SEMANTICS,
    'Approximation algorithms': APPROXIMATION,
    'Proof complexity and logic': PROOF,
    'Communication complexity': COMMUNICATION,
    'Algebraic and numerical computation': ALGEBRA,
    'Optimization and mathematical programming': OPTIMIZATION,
    'Optimization, mathematical programming and numerical algorithms': OPTIMIZATION,
    'Online algorithms, bandits and stochastic optimization': OPTIMIZATION,
    'Information-based complexity and numerical algorithms': OPTIMIZATION,
    'Randomized search and optimization': OPTIMIZATION,
    'Enumeration and counting': COUNTING,
    'Algorithmic game theory and fair division': GAME,
    'Computational social choice': GAME,
    'Algorithms for biological structures': STRINGS,
})
LEGACY_AREAS = set(DIRECT) | {'General algorithm design', 'Combinatorics and graph polynomials'}
ASSIGNMENT_FIELDS = {'original_area', 'selection_group', 'selection_target',
                     'category_assignment', 'scope_exclusion'}
OVERRIDES_PATH = Path(__file__).with_name('category_overrides.json')
PRELIMINARY_PATH = Path(__file__).parent / 'to_delete/large-buckets-20260910/manifest.json'
SMALL_PRELIMINARY_PATH = Path(__file__).parent / 'to_delete/small-buckets-20260910/manifest.json'
SECOND_LARGE_PRELIMINARY_PATH = Path(__file__).parent / 'to_delete/large-buckets-second-20260910/manifest.json'

def editorial_card(card):
    """Remove routing metadata for comparison with the canonical authored card."""
    result = {k: v for k, v in card.items() if k not in ASSIGNMENT_FIELDS | {'importance_rank', 'importance_count', 'textbook_notes'}}
    result['area'] = card.get('original_area', card['area'])
    return result


def problem_text(card):
    legacy = card.get('legacy') or {}
    fields = [card.get('title'), card.get('formal'),
              (card.get('source_formulation') or {}).get('text'),
              legacy.get('question_excerpt'), legacy.get('source_title')]
    # The primary source supplies context when the saved question is truncated.
    fields.extend(r.get('title') for r in card.get('references', [])[:1])
    text = unicodedata.normalize('NFKC', ' '.join(str(x) for x in fields if x))
    return text.replace('–', '-').replace('—', '-').replace('−', '-')


def has(pattern, text):
    return re.search(pattern, text, re.I) is not None


def metric_topic(text):
    return has(
        r'metric embeddings?|embedding.{0,45}(?:metric|ultrametric|euclidean|normed|hilbert|banach)|'
        r'johnson[\s-]*lindenstrauss|dimension(?:ality)?[ -]reduction|doubling (?:dimension|metric)|'
        r'earth[ -]mover|wasserstein|locality[ -]sensitive hashing|'
        r'(?:high[ -]dimensional|metric|euclidean|geometric).{0,35}(?:data|search|clustering|coreset|spanner)|'
        r'(?:coreset|spanner).{0,35}(?:metric|euclidean|geometric)|'
        r'nearest[ -]neighbou?r (?:search|problem|data structure)|'
        r'approximate nearest[ -]neighbou?r', text)


def parallel_topic(text):
    # MPC also means secure multiparty computation. "Parallel" alone includes
    # axis-parallel rectangles, scheduling, proof repetition and process syntax.
    if has(r'secure.{0,30}(?:MPC|multi[ -]?party)|resettable MPC|parallel repetition|'
           r'intersection type|parallel composition|parallel substitution', text):
        return False
    return has(r'semi[ -]streaming|(?:data[ -])?streaming (?:model|algorithm)|'
               r'(?:multi|single|one|two)[ -]pass (?:stream|algorithm)|'
               r'massively parallel|\bMPC algorithms?\b|\bPRAM (?:model|algorithm)|'
               r'parallel (?:and distributed )?algorithms?|parallel implementation|'
               r'parallel.{0,90}(?:depth and work|work and depth)|'
               r'(?:near[ -]linear|linear|polynomial).{0,20}work.{0,35}(?:polylog|depth)|'
               r'parallel matroid|sampling.{0,35}in parallel|'
               r'(?:constant|polylogarithmic) parallel time|parallel queries|'
               r'fork[ -]join|deterministic NC\b|RNC sampling', text)



# Narrow, recognizable subjects can cross the old, often noisy categories.
KR_PATTERN = (r'knowledge representation|knowledge compilation|knowledge bases?|'
    r'description logics?|ontology|ontologies|ontological|answer[ -]set|'
    r'non[ -]?monotonic|belief (?:revision|merging|update)|'
    r'abstract argumentation|argumentation framework|default logic|'
    r'epistemic logic|autoepistemic|circumscription|common belief|factional belief')
STRING_PATTERN = (r'\bstrings?\b|suffix|\bBWT\b|burrows[ -]wheeler|lempel[ -]ziv|'
    r'\bLZ(?:77|78|W)\b|palindrom|pattern matching|text index|stringology|'
    r'word equations?|lyndon|repetitiveness|\bk[ -]?mers?\b|minimizers?|'
    r'phylogen|genom|\bRNA\b|\bDNA\b|bioinformatic|genealog|chromatin|'
    r'gene trees?|protein|biological|sequence alignment')
SAMPLING_PATTERN = (r'markov chain|mixing time|glauber|\bMCMC\b|'
    r'metropolis[ -]hastings|rapid mixing|perfect sampl|approximate sampl|'
    r'uniform(?:ly)? sampl|sampling algorithms?|random sampling algorithm|'
    r'algorithmic lov[aá]sz local lemma|partial rejection sampling|'
    r'coupling from the past|monte[ -]carlo algorithms?|gibbs sampling|kawasaki dynamics|'
    r'random walks?|mixing in non-quasirandom|mixing few|samplers? for|'
    r'sampling (?:in|list|of|from)|counting and sampling|correlated sampling|'
    r'partial sampling|approximate rejection sampling|joys of sampling')
STRUCTURAL_PATTERN = (r'graph minors?|minor[ -]closed|graph structure theorem|'
    r'tree[ -]?width|clique[ -]?width|twin[ -]?width|shrub[ -]?depth|'
    r'mim[ -]?width|SC[ -]?depth|bounded expansion|nowhere dense|nowhere-dense|'
    r'monadically stable|hereditary (?:graph )?class|forbidden induced|'
    r'chi[ -]bounded|χ[ -]bounded|erd[oőö]s[ -]p[oó]sa|'
    r'graph product structure|product structure of|ramanujan|'
    r'expanding expanders|ultra[ -]sparse expanders|girth conjecture')

ROUTES = [
    (QUANTUM, r'\bquantum\b|qubits?|forrelation|entangled|non[ -]local games'),
    (CRYPTO, r'cryptograph|obfuscat|zero[ -]knowledge|one[ -]way function|secure.{0,25}MPC'),
    (PRIVACY, r'differential(?:ly)? privat|privat(?:e|ely).{0,35}learn'),
    (KNOWLEDGE, KR_PATTERN),
    (RANDOMNESS, r'derandom|pseudorandom|randomness extract|\bPRGs?\b|polynomial identity testing|rank condensers?'),
    (COMMUNICATION, r'communication complexity|communication lower bound|boolean function|fourier analysis|log[ -]rank|log[ -]approximate[ -]rank|lifting with sunflowers'),
    (PROOF, r'proof complexity|frege|cutting[ -]planes|resolution refutation|sum of squares bounds|\bSOS lower bounds'),
    (FINE, r'\bSETH\b|fine[ -]grained|truly sub(?:quadratic|cubic)|orthogonal vectors|non-combinatorial.*lower bounds'),
    (STRINGS, STRING_PATTERN),
    (PARAMETERIZED, r'\bFPT\b|W\[[12]\]|kernelization|polynomial kernel|enumeration kernels|fixed[ -]parameter|parameterized'),
    (CODING, r'error[ -]correct|list[ -]decod|reed[ -]solomon|reed[ -]muller|code rate|mutual information'),
    (LATTICES, r'\blattices?\b|shortest vector|integer factori|discrete logarithm|abc[ -]conjecture'),
    (REASONING, r'unification|theorem proving|automated (?:deduction|reasoning)|satisfiability modulo'),
    (DATABASE, r'database|\bdatalog\b|conjunctive quer|finite model|query evaluation'),
    (SEMANTICS, r'bisimulat|model checking|reachability games?|synthesis|verification|'
        r'lambda calculus|type (?:theor|system)|rewrit|semantics|monads?|coalgebra|'
        r'relation algebra|calculus of relations|pi[ -]calculus|normalisation|normalization|'
        r'process decomposition|\b(?:VASS|VAS|GKAT|ProbGKAT|wGKAT)\b|petri net'),
    (AUTOMATA, r'automata|automaton|formal language|regular language|transducer|grammar|word equations?|first-order logic without'),
    (COMPUTABILITY, r'computability|kolmogorov complexity|algorithmic randomness|turing degree|busy beaver|intuitionistic arithmetic'),
    (CSP, r'constraint satisfaction|\b[PV]?CSPs?\b'),
    (GAME, r'fair division|envy[ -]free|nash equilib|mechanism design|auction|price of anarchy|social choice|voting|strategyproof|selfish routing|tax scheme'),
    (TESTING, r'property testing|distribution (?:testing|learning)|sample complexity of testing'),
    (LEARNING, r'learn|classification|\bPAC\b|neural network|statistical query|robust PCA|\bVC[ -]class|teaching dimension'),
    (OPTIMIZATION, r'\bonline\b|bandit|regret|competitive ratio|stochastic optimization|experts and combinatorial games'),
    (DYNAMIC, r'dynamic.{0,35}(?:graph|connectivity|matching|shortest path|spanner|set cover)'),
    (PARALLEL, r'\bCONGEST\b|distributed algorithm|\bLOCAL model\b|streaming|sketching|load balancing'),
    (SAMPLING, SAMPLING_PATTERN),
    (ADS, r'data structure|priority queue|search tree|sorting|comparison[ -]based|range quer|distance oracle'),
    (SCHEDULING, r'scheduling|makespan|bin packing|strip packing|tardy jobs'),
    (GEOMETRY, r'homolog|homotop|simplicial complex|topological|knot theory|torus|tverberg|'
        r'geometr|polygon|rectangle|triangulat|convex hull|point set|arrangement|'
        r'voronoi|hyperplane|delaunay|lens system|signotop|sphere|curve|disc packing|kd[ -]tree'),
    (APPROXIMATION, r'approximat|\bPTAS\b|inapproximab'),
    (OPTIMIZATION, r'linear programm|convex optim|integer programm|gradient|interior[ -]point|'
        r'pivot rules?|simplex method|numerical integr|linear (?:program|system)|discrepancy|spencer conjecture'),
    (ALGEBRA, r'matrix multipli|\bpermanent\b|arithmetic circuit|polynomial multipli|'
        r'polynomial system|group isomorphism|tropical|slice rank|isotropic spaces|convolution'),
    (COUNTING, r'counting|enumeration|iteration|gray code'),
    (COMPLEXITY, r'circuit|decision lists|\b(?:NP|PSPACE|NEXP|BPP|P|MA)[ -]complete\b|\bNP[ -]hard|\bTFNP\b|interactive proofs|computational complexity|query complexity'),
    (ADS, r'\bgraphs?\b|hypergraph|matroid|chromatic|hamilton|steiner tree|'
        r'minimum (?:spanning tree|cut)|shortest path|vertex|vertices|tournament'),
]


# Additional recognizable source subjects for formerly generic or mislabeled records.
FALLBACK_ROUTES = [
    (QUANTUM, r'Pauli observables|QRAM|teleportation'),
    (CRYPTO, r'password|card-based protocols'),
    (KNOWLEDGE, r'common belief|factional belief'),
    (SAMPLING, SAMPLING_PATTERN),
    (COMMUNICATION, r'decision tree complexity|block sensitivity|convex influences|symmetric functions|low-sensitivity functions|transitive functions|uncertain communication|unambiguous certificates|lifting theorem|garden-hose'),
    (PROOF, r'stabbing planes|QBF resolution|small width in resolution|Expander Construction in VNC1'),
    (RANDOMNESS, r'lossless expanders|cayley expanders|high[ -]dimensional expanders|black box identities|pseudo[ -]deterministic'),
    (FINE, r'3XOR|k-SUM|k-means|subset sum|pigeonhole equal|element distinctness'),
    (CODING, r'deletion codes|noiseless feedback|trace reconstruction'),
    (COUNTING, r'holant|spin systems'),
    (CSP, r'constraint languages|presidential type predicates|XSAT'),
    (REASONING, r'linear integer arithmetic|linear arithmetic constraints|Skolem|tree share formulas'),
    (DATABASE, r'XPath|tree patterns|choiceless polynomial time|first-order definable structures|dependence logic'),
    (COMPUTABILITY, r'constructive dimension|dimension spectrum|ergodic|algorithmic information|information carried by programs|higher randomness|subrecursive|Turing complete|undecidab|not recursive|domino problem|subshifts|large cardinals|Zermelo-Fraenkel|forcing with closed sets|polynomial space randomness'),
    (AUTOMATA, r'word complexity|binary words|abelian.*avoidable|subword|regular expressions|regular tree language|syntactic monoid|rational functions|logic of subsequences|word problem|automatic structures|repetitions|periods and borders|downward closure|unambiguous morphisms|SORE-definability|keyboards as a new model'),
    (SEMANTICS, r'bisimil|reachability|process calcul|invocation contexts|mu-calculus|Kleene algebra|fixed point|fixpoints|parametricity|functors?|monoidal|modal logic|dynamic logic|presheaf|realizability|axiomatisation|BPA|network games|bidding games|positional payoffs'),
    (STRINGS, r'shortest cover after edit|runs over.*alphabets|genetic|sexual reproduction|mutation trees|agreement forests'),
    (GEOMETRY, r'centerpoint|moving (?:sensors|entities)|guard problems|plane.sweep|coresets?|geometric|free space construction|conley index|plane with angular|motion planning|sparse random embeddings|interference|ant be confined'),
    (PARALLEL, r'radio networks|mobile agents|firing squad|OBLOT|local robots|sliding windows|shared randomness|collective fast delivery'),
    (GAME, r'coordination games|flow games|carpooling|risk scores|sell information'),
    (LEARNING, r'decision tree heuristics|agglomerative clustering|probability matrices'),
    (OPTIMIZATION, r'paging|reordering buffer|server problem|Dantzig-Wolfe|Pareto optima|budgeted red-blue median|sink orientations|clustering|linear functions|crystal structure|spectral analysis|reinforcement planning|decision making'),
    (SCHEDULING, r'packing|Fit into One A0'),
    (ALGEBRA, r'polynomials|matrix powering|products of permutations|finite groups|wreath products|quintic|arithmetic complexity|integer complexity|S-unit equations|submonoid|real stability'),
    (COMPLEXITY, r'PSPACE|Tetris|Hive|puzzles?|puzzle|token swapping|chess|card game|mirror games|spatial games|client-waiter|waiter-client|poset positional games|MA and AM|gate elimination|cook completeness|karp-levin|negation-limited|min, \\+'),
    (ADS, r'knapsack|maximum flows|network designs|capped hose|sorting|sorters|timsort|quicksort|merge sorts|dictionary|cuckoo filter|bit-probe|data structure|dynamic optimality|external memory|spanner|Tutte Paths|queries on indistinguishable|memory faults|sparsification|pebbling|packing cycles'),
]


def classify(card, overrides=None):
    old = card.get('original_area', card['area'])
    text = problem_text(card)
    override = (overrides or {}).get(card['id'])
    if override:
        return (OUTSIDE if override.get('exclude') else override['area'],
                'scope_policy' if override.get('exclude') else 'editorial_topic', override['reason'])
    if card.get('proposal_import') and card.get('evidence') != 'reviewed':
        approved_area = card['proposal_import']['category']
        if approved_area not in NAMES:
            raise ValueError('Unknown approved proposal category')
        return approved_area, 'editorial_topic', 'Category from the approved fundamental-problem proposal'
    if card.get('textbook_import') and card.get('evidence') != 'reviewed':
        approved_area = card['textbook_import']['category']
        if approved_area not in NAMES:
            raise ValueError('Unknown textbook question category')
        return approved_area, 'editorial_topic', 'Topic of the imported textbook or survey question'
    destination = DIRECT.get(old)
    # Average-case complexity and explicit beyond-worst-case input models.
    # Keep quantum/crypto questions and statistical instance-optimality in their
    # specialist homes unless their old subject explicitly says average-case.
    if destination == BEYOND:
        return BEYOND, 'existing_area', 'Average-case complexity and hardness'
    if destination not in {QUANTUM, CRYPTO, SEMANTICS, AUTOMATA, PROOF, COMMUNICATION, CODING, SAMPLING, TESTING, PRIVACY} and has(
            r'beyond[ -]worst[ -]case|average[ -]case|smoothed|semi[ -]random|'
            r'planted (?:clique|dense|partition|model|subgraph|coloring)|'
            r'perturbation (?:resilien|stabil)|self[ -]improving|'
            r'learning[ -]augmented|algorithms? with predictions|random[ -]order|random order', text):
        return BEYOND, 'topic_rule', 'Average-case, smoothed, semi-random or prediction-assisted analysis'
    if destination in {ADS, GEOMETRY, OPTIMIZATION, None} and has(r'instance[ -]optimal', text):
        return BEYOND, 'topic_rule', 'Instance-optimal analysis beyond a uniform worst-case bound'
    # Knowledge representation has a distinct application focus within logic.
    if destination in {ADS, SEMANTICS, PROOF, REASONING, DATABASE, COMPLEXITY, CSP, AUTOMATA, None}:
        if has(KR_PATTERN, text):
            return KNOWLEDGE, 'topic_rule', 'Knowledge bases, ontologies or nonmonotonic reasoning'
    movable = {ADS, LEARNING, GEOMETRY, PARAMETERIZED, FINE, APPROXIMATION,
               PARALLEL, COUNTING, OPTIMIZATION, DATABASE, CODING, GAME,
               COMPLEXITY, ALGEBRA, STRINGS, SAMPLING, STRUCTURAL, None}
    if destination in movable and parallel_topic(text):
        return PARALLEL, 'topic_rule', 'Parallel, distributed or streaming computation'
    if destination in movable and metric_topic(text):
        return GEOMETRY, 'topic_rule', 'High-dimensional geometry or metric algorithms'
    if destination in {ADS, STRINGS, GEOMETRY, PARAMETERIZED, FINE, COUNTING, None} and has(STRING_PATTERN, text) and not has(r'\bstring graphs?\b', text):
        return STRINGS, 'topic_rule', 'String algorithms, compression or computational biology'
    if destination in {COMPLEXITY, RANDOMNESS, COMMUNICATION, PROOF, None} and has(
            r'boolean function|fourier (?:analysis|spectrum)|total influence|noise sensitivity|sensitivity conjecture', text) and not has(r'circuit lower bound|circuit complexity|frege|proof complexity', text):
        return COMMUNICATION, 'topic_rule', 'Boolean function analysis'
    if destination in {ADS, COUNTING, OPTIMIZATION, COMPLEXITY, RANDOMNESS, SAMPLING, GEOMETRY, None} and has(SAMPLING_PATTERN, text):
        return SAMPLING, 'topic_rule', 'Sampling, Markov chains or general randomized algorithms'
    # Running-time problems on bounded-width graphs retain their algorithmic home.
    question = ' '.join(str(x or '') for x in [card.get('source_formulation',{}).get('text'), card.get('legacy',{}).get('question_excerpt'), card.get('formal'), card.get('title')])
    algorithmic = has(r'algorithm|running time|solv|tractab|hardness|computing|computation|\btime\b|\bFPT\b|kernel|NP[ -]hard|complexity|decidab|parameterized', text)
    if destination in {ADS, COMPLEXITY, GEOMETRY, STRINGS, STRUCTURAL, None} and has(STRUCTURAL_PATTERN, text) and not algorithmic:
        return STRUCTURAL, 'topic_rule', 'Graph structure, width parameters, sparse classes or expansion'
    if old == 'Proof complexity and logic' and has(r'type system|type theory|functional programming|monads?|lambda|bisimulat', text) and not has(r'frege|proof complexity|proof length|resolution refutation', text):
        return SEMANTICS, 'topic_rule', 'Programming-language logic and semantics'
    if old == 'Algebraic and numerical computation' and has(r'numerical|condition number|convex optim|gradient descent|linear programming|linear system|tensor decomposition|conic intrinsic', text):
        return OPTIMIZATION, 'topic_rule', 'Numerical computation or optimization'
    # The old biological label used an unbounded RNA/DNA match (e.g. external).
    # Require a real subject signal rather than perpetuating those false positives.
    if old == 'Algorithms for biological structures':
        destination = None
    if destination == ADS and has(r'sample compression|teaching|learnability', text):
        return LEARNING, 'topic_rule', 'Sample compression and teaching in learning theory'
    if destination in movable and has(r'social choice|voting rules?|strategyproof|preference aggregation', text):
        return GAME, 'topic_rule', 'Social choice and strategic preferences'
    if destination == ADS and has(r'fully dynamic|dynamic (?:shortest|connectivity|matching|graph|APSP)', text):
        return DYNAMIC, 'topic_rule', 'Dynamic graph algorithms'
    if destination:
        return destination, 'existing_area', 'Mapped from the existing subject category'
    for area, pattern in ROUTES + FALLBACK_ROUTES:
        if has(pattern, text):
            return area, 'topic_rule', 'Specific topic in the problem or primary source'
    return MISC, 'fallback', 'No clear category identified from the saved problem and source'


def apply_taxonomy(data):
    overrides = json.loads(OVERRIDES_PATH.read_text()) if OVERRIDES_PATH.exists() else {}
    ids = {c['id'] for c in data['cards']}
    decisions, decision_sources = {}, {}
    for manifest_path, allowed_categories in [(PRELIMINARY_PATH, BIG),
                                              (SMALL_PRELIMINARY_PATH, SMALL),
                                              (SECOND_LARGE_PRELIMINARY_PATH, BIG)]:
        if not manifest_path.exists():
            continue
        preliminary = json.loads(manifest_path.read_text())
        batch = preliminary.get('records', {})
        if decisions.keys() & batch.keys():
            raise ValueError('Conflicting preliminary removal batches')
        if any(d.get('category') not in allowed_categories for d in batch.values()):
            raise ValueError('Preliminary removal outside its batch category scope')
        decisions.update(batch)
        for identifier in batch:
            decision_sources[identifier] = dict(
                archive=str(manifest_path.with_name('records.json').relative_to(Path(__file__).parent)),
                review_id=preliminary['review_id'])
    if decisions.keys() - ids:
        raise ValueError('Preliminary removal targets an unknown record')
    for decision in decisions.values():
        if (decision.get('state') not in {'quarantined', 'retained'} or
                decision.get('category') not in NAMES or not decision.get('reason')):
            raise ValueError('Invalid preliminary removal decision')
    if overrides.keys() - ids:
        raise ValueError('Category override targets an unknown record')
    for override in overrides.values():
        if not override.get('reason') or (not override.get('exclude') and override.get('area') not in NAMES):
            raise ValueError('Invalid category override')
    counts, adds, reviewed = collections.Counter(), collections.Counter(), collections.Counter()
    for card in data['cards']:
        original = card.get('original_area', card['area'])
        area, method, reason = classify(card, overrides)
        decision = decisions.get(card['id'])
        quarantined = decision and decision['state'] == 'quarantined'
        if quarantined:
            area, method, reason = OUTSIDE, 'preliminary_quality', decision['reason']
        group, target = ('large', 50) if area in BIG else ('small', 20)
        card.pop('scope_exclusion', None)
        if area == OUTSIDE:
            group, target = 'excluded', 0
            card['scope_exclusion'] = {'reason': reason, 'policy': 'SELECTION_POLICY.md', 'date': '2026-09-10'}
            if quarantined:
                card['scope_exclusion'].update(
                    kind='preliminary_quality', previous_area=decision['category'],
                    reason_code=decision['reason_code'],
                    **decision_sources[card['id']])
                if decision.get('duplicate_of'):
                    card['scope_exclusion']['duplicate_of'] = decision['duplicate_of']
        card.update(area=area, original_area=original, selection_group=group,
                    selection_target=target,
                    category_assignment={'method': method, 'reason': reason})
        if area == OUTSIDE:
            continue
        counts[area] += 1
        adds[area] += bool(card.get('is_new'))
        reviewed[area] += card.get('evidence') == 'reviewed'
    areas = []
    total = sum(counts.values())
    for group, names, target in [('large', BIG, 50), ('small', SMALL, 20)]:
        for position, name in enumerate(names, 1):
            areas.append(dict(area=name, label=name, group=group, position=position,
                              target=target, count=counts[name], reviewed=reviewed[name],
                              before=counts[name]-adds[name], added=adds[name],
                              after_pct=100*counts[name]/total if total else 0))
    data['areas'] = areas
    data['meta']['taxonomy'] = dict(version='selection-35-v4', large_groups=10,
        small_groups=25, vacant_small_groups=0, assigned_target=1000,
        reserved_target=0, target_total=1000,
        pruned=any(d['state'] == 'quarantined' for d in decisions.values()), candidate_count=total,
        scope_excluded_count=len(data['cards'])-total,
        preliminary_removal_count=sum(d['state'] == 'quarantined' for d in decisions.values()),
        subject_exclusion_count=sum(c.get('scope_exclusion', {}).get('kind') != 'preliminary_quality'
                                    for c in data['cards'] if c.get('scope_exclusion')),
        assignment_counts=dict(collections.Counter(c['category_assignment']['method'] for c in data['cards'])))
    data['meta']['methodology'] = [p for p in data['meta'].get('methodology', [])
        if not p.startswith('Selection groups follow')]
    data['meta']['methodology'].append(
        'Selection groups follow the agreed 10 large groups of 50 and 25 named small '
        'groups of 20: all 1,000 planned places are assigned to named categories. '
        'These are future targets. Preliminary editorial pruning is recorded in the '
        'large- and small-category manifests under to_delete/; final quota selection '
        'and a complete deduplication audit have not been performed. '
        'Topic assignments use original subjects, saved questions and primary source titles. '
        'Unclear cases go to Miscellaneous. General combinatorics outside the accepted '
        'scope is archived with a reason. Preliminary removals retain their reason and '
        'pre-removal selection category separately from original subject labels. '
        'Archived records remain accessible through the Selection scope filter and full exports. '
        'Original categories and stable IDs are preserved. Classification does not '
        'verify the statement or its current open status.')
    return data
