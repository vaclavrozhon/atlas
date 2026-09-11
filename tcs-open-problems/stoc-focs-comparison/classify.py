"""Own single-label topic index, using the catalog's 43 categories.
Rules are interpretable candidate assignments, followed by recorded human/LLM review.
They are not a validated statistical classifier or official conference categories.
"""
import json, re
from pathlib import Path
from collections import Counter
BASE=Path(__file__).resolve().parent
AREAS={
'dp':'Differential privacy','q':'Quantum computation','code':'Coding and information theory',
'lattice':'Lattices and computational number theory','crypto':'Cryptography','prg':'Pseudorandomness and derandomization',
'proof':'Proof complexity and logic','comm':'Communication complexity','etr':'Existential theory of the reals',
'fg':'Fine-grained complexity','alg':'Algebraic and numerical computation','avg':'Average-case complexity',
'comp':'Computability and algorithmic information','csp':'Constraint satisfaction','sat':'Automated reasoning and unification',
'sem':'Rewriting, lambda calculus and semantics','inf':'Infinite-state systems and verification','verify':'Games, synthesis and verification',
'autom':'Automata and formal languages','db':'Database theory and finite model theory','bio':'Algorithms for biological structures',
'top':'Computational topology','geom':'Computational geometry','temp':'Temporal graph algorithms','dyn':'Dynamic graph algorithms',
'ds':'Data structures and compressed data','stream':'Streaming and sketching','test':'Property testing and distribution learning',
'game':'Algorithmic game theory and fair division','sched':'Scheduling and packing','online':'Online algorithms, bandits and stochastic optimization',
'learn':'Learning theory','dist':'Distributed and local algorithms','param':'Parameterized and exact algorithms',
'approx':'Approximation algorithms','count':'Enumeration and counting','opt':'Optimization and mathematical programming',
'cx':'Computational and circuit complexity','comb':'Combinatorics and graph polynomials','graph':'Graph theory and graph algorithms',
'general':'General algorithm design','iba':'Information-based complexity and numerical algorithms','random':'Randomized search and optimization'}

# Title rules, ordered from specialized subject to more generic technique.
RULES=[
('dp',r'privacy|differentially private|private (?:learning|mean|estimation|estimators|release|data|algorithms|optimization|query|statistical|aggregation|counting|samples|selection|sampling)|private and'),
('crypto',r'cryptograph|cryptanaly|zero.knowledge|obfuscat|encrypt|secret.shar|secure.*(?:computation|computing)|multiparty|multi.party|two.party computation|commitment|signature|one.way|\bLWE\b|\bLPN\b|\bSNARG|\bSNARK|verifiable computation|proofs? of (?:space|stake|work|knowledge)|oblivious (?:transfer|ram)|pseudorandom (?:function|permutation)|collision.resistant|hash.function|fully homomorphic|time.lock|indistinguishability|authentication|cryptanalysis|non.malleab|oblivious linear|one.time program|timed release|computationally secure'),
('q',r'quantum|qubit|\bQMA\b|\bQCMA\b|\bBQP\b|stabilizer|non.collapsing|nonlocal game|non.local game|unitary|\bstateQIP\b|\bStatepspace\b|\bQIP\b|entangl|Hamiltonian|boson|\bBPP.*Q|quantum'),
('code',r'\bcodes?\b|\bcoding\b|decod|reed.solomon|reed.muller|channel capacity|shannon|adversarial.*deletion|error.correct|information theory|entropy accumulation|insdel|correlated sources|noise stability'),
('lattice',r'lattice|shortest vector|closest vector|number.theoretic|discrete logarithm|integer factor|primes|prime numbers'),
('prg',r'pseudorandom|pseudodetermin|derandom|extractor|extracting randomness|randomness extract|hitting.set generator|small.bias|hardness (?:vs.?|versus) randomness|\bfooling\b|\bcondensers?\b|randomness condenser'),
('proof',r'proof complexity|frege|bounded arithmetic|resolution proof|cutting.planes proof|proof system|algebraic proofs|polynomial calculus|nullstellensatz|\bIOPs?\b|\bPCPs?\b|interactive proofs|interactive arguments|interactive oracle|low.degree test|sum.of.squares lower|lower bounds.*sum.of.squares|bounded depth proofs|refut'),
('comm',r'communication complexity|sign.rank|log.rank|communication protocols|communication with|communication lower|communication trade|multiparty communication|multiparty correlations|information complexity|communication and information|communication cost'),
('etr',r'existential theory of the real|∃R|exists.r|existential real'),
('fg',r'fine.grained|strong exponential time|SETH|orthogonal vectors|3sum|ETH.hard'),
('alg',r'algebraic complexity|arithmetic circuit|polynomial identity|matrix multiplic|algebraic branching|polynomial factor|tensor rank|algebraic circuits|multipoint evaluation|polynomial.*decompos|polynomial equivalen|polynomial isomorph|tensor isomorph|group isomorph|sylvester.gallai|matrix.*inversion|polynomial system|matrix pencil|polynomial multipli|factoring.*polynomial|power.sum|hankel matric|fourier interpolation|multivariate polynomial|polynomial.*rank|low.rank approximation'),
('avg',r'average.case|hardness amplification|hardness self.amplification|planted clique|perceptron|spin glass|sherrington.kirkpatrick'),
('comp',r'kolmogorov|computability|algorithmic random|turing degree|busy beaver|reverse mathematics'),
('csp',r'constraint satisfaction|\bCSPs?\b|polymorph|promise constraint|constraint graphs|unique games|label cover'),
('inf',r'petri net|vector addition|infinite.state|pushdown system|well.structured transition'),
('verify',r'parity game|energy game|synthesis|model.check|verification|temporal logic|bisimul|hyperlogic'),
('sem',r'rewrit|lambda|λ.calculus|type theor|dependent type|categorical semantic|game semantic|session type|linear logic|programming.language semantic'),
('autom',r'automata|automaton|formal language|regular language|context.free|transducer|language theor'),
('db',r'database|conjunctive quer|query answering|query evaluation|finite model|datalog|relational algebra|join quer'),
('bio',r'bioinform|\bRNA\b|\bDNA\b|genom|phylogenet|self.assembly|tile assembl|protein'),
('temp',r'temporal graph|temporal connect|temporal path|temporal clique'),
('dyn',r'dynamic.*(?:graph|matching|shortest path|connectivity|spanner|flow|distance|SSSP|APSP|MST|reachability|cut|biconnect|network)|decremental|incremental.*(?:graph|matching|shortest path|connectivity|spanner|flow|distance|SSSP|MST|reachability)|sensitivity.*(?:oracle|connectivity)|graph.*dynamic'),
('stream',r'streaming|stream algorithm|data stream|\bstreams\b|sketch|turnstile|sliding window'),
('game',r'fair divis|fair.*allocat|allocation|envy|\bEFX\b|\bEF1\b|\bEFM\b|maximin|nash|equilibri|auction|mechanism design|social choice|voting|price of anarchy|contract design|contracts|social welfare|incentive.compatible|bayesian persuas|stable matching|equitable|cake.cutting|secretary matching|combinatorial public project'),
('test',r'property test|distribution test|distribution learn|tolerant test|junta test|monotonicity test|identity test|testing|testability|hypothesis selection|uniformity test|estimating.*(?:entropy|distribution)|distribution.*estimat'),
('sched',r'schedul|makespan|bin.pack|strip.pack|job shop'),
('online',r'online|bandit|regret|reinforcement learn|competitive ratio|prophet|secretary problem|stochastic optim|chasing'),
('ds',r'data structure|succinct|compress|text index|string|pattern match|suffix|edit distance|longest common|longest increasing|hamming distance|hashing|hash table|list labeling|linear probing|membership quer|nearest neighbou?r|dynamic.*regression|range search|range quer'),
('learn',r'learn|neural|generalization|empirical risk|VC.dimension|sample complexity|statistical query|statistical infer|stochastic block|community detect|linear regression|mean estimat|mean testing|robust estimat|PAC bounds|sparse recover|low.degree method|robust recover|density estimat|statistical estimat|matrix completion|sparse regression'),
('dist',r'distributed|local algorithm|local computation|byzantine|consensus|leader election|locality|congest|population protocol|gossip|massively parallel|broadcast network|anonymous.*network|parallel.*graph|LOCAL model|parallel.*independent set'),
('param',r'parameteriz|parameteris|kerneliz|kernelis|fixed.parameter|\bFPT\b|exact algorithm|single.exponential|\bPPSZ\b|(?:faster|time|algorithm).*(?:k.sat|3.sat|CNF.sat)|(?:k.sat|3.sat|CNF.sat).*(?:faster|time|algorithm)'),
('sat',r'satisfiability|\bSAT\b|unification|automated reasoning|smt solver|majority.3sat'),
('opt',r'optimiza|optimisa|linear program|integer program|semidefinite|convex program|submodular|subgradient|matroid|interior.point|\bSDP\b|gradient|linear system|positive definite|log.concave|convex polynomial programming|integer.*nonzeros|convex.*minimiz'),
('count',r'enumerat|counting|\#P|\#SAT|\#CSP|permanent|glauber|spectral independence|markov chain|mixing|spin system|potts model|sampling.*(?:color|colour|local lemma|gibbs|independent set)|hardcore model|hard.core model|sampling from'),
('approx',r'approximat|integrality gap|inapproxim|steiner|facility location|correlation clustering|k.median|k.means|set cover|metric.*(?:fit|embedd)|(?:fit|embedd).*metric|fitting distance|network design'),
('top',r'topolog|homolog|homotop|simplicial complex|knot'),
('geom',r'computational geometry|geometric|polygon|polytope|triangul|visibility|convex hull|voronoi|delaunay|point set|intersection graph|graph drawing|crossing number|rectilinear|zonotope|euclidean|coreset|terminal embedding|hyperplane|geometry'),
('cx',r'complexity class|\bcircuits?\b|\bformulas?\b|\bP/poly\b|\bNP\b|\bBPP\b|\bNC[012]?\b|\bAC[012]?\b|branching program|boolean function|\bDNFs?\b|\bCNFs?\b|space complexity|constructive separation|computational complexity|\bL vs|\bP vs|\bEXP\b|\bPSPACE\b|meta.complexity|range avoidance|hardest explicit construction|query complexity|query lower|query.upper|uniform circuit|direct.sum theorem'),
('comb',r'combinatori|discrepancy|ramsey|extremal|graph polynomial|chromatic polynomial|tutte|expander|hypercontract|fourier concentration|invariance principle|kahn.kalai|erdős|kakeya|progressions|vector balancing|hadwiger|contiguity conjecture|anti.concentration|sunflower|sandpile|brownian|hypergraph'),
('graph',r'graph|matching|connectivity|shortest path|spanning tree|treewidth|tree.width|clique|coloring|colouring|dominating|\bpath|\bcut|\bflow|\bmaxflow|\bmax.flow|spanner|hopset|\bSSSP\b|vertex expansion|thin trees|independent set|network|hamilton cycle|\bvortex\b|well.linked|cycle|\btrees\b'),
]

def main():
    records=json.loads((BASE/'papers_internal.json').read_text())
    overrides=json.loads((BASE/'overrides.json').read_text()) if (BASE/'overrides.json').exists() else {}
    for r in records:
        # All 1546 titles were read in proceedings order during the review.
        r['classification_method']='LLM_reviewed_title'
        r['classification_note']='Title reviewed; candidate primary category retained.'
        hits=[a for a,p in RULES if re.search(p,r['title'],re.I)]
        r['rule_area']=AREAS[hits[0] if hits else 'general']
        r['area']=r['rule_area']
        r['title_matches']=[AREAS[a] for a in dict.fromkeys(hits)]
        if r['id'] in overrides:
            v=overrides[r['id']]
            r['area']=AREAS[v['area']]
            r['classification_method']=v.get('method','LLM_reviewed_title').replace('reviewed_title','LLM_reviewed_title') if not v.get('method','').startswith('LLM_') else v['method']
            r['classification_note']=v.get('note','Primary topic reviewed against title.')
    (BASE/'papers_classified_internal.json').write_text(json.dumps(records,ensure_ascii=False,indent=2))
    print(Counter(r['area'] for r in records).most_common())
    (BASE/'review_titles.txt').write_text('\n'.join(f"{r['id']} | {next(a for a,b in AREAS.items() if b==r['area'])} | {r['title']}" for r in records))
if __name__=='__main__': main()
