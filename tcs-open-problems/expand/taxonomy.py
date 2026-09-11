"""Transparent, heuristic topical indexing; this is not an official classification."""
import re

RULES=[
 ('Differential privacy',r'differential(?:ly)? privat|local privacy|private learning'),
 ('Quantum computation',r'quantum|qubit|qma|bqp|stabilizer|non-collapsing'),
 ('Coding and information theory',r'error.correct|list.decod|reed.solomon|code equivalen|coding theor|channel capacity|information theory'),
 ('Lattices and computational number theory',r'lattice|shortest vector|closest vector|number.theoretic|discrete logarithm'),
 ('Cryptography',r'cryptograph|zero.knowledge|obfuscat|encryption|secret.shar|secure computation|multiparty computation|commitment scheme|signature scheme|one.way function'),
 ('Pseudorandomness and derandomization',r'pseudorandom|derandom|randomness extract|hitting.set generator|small.bias'),
 ('Proof complexity and logic',r'proof complexity|frege|bounded arithmetic|resolution proof|cutting.planes proof|proof system'),
 ('Communication complexity',r'communication complexity|sign.rank|log.rank'),
 ('Existential theory of the reals',r'existential theory of the real|∃R|exists.r|existential real'),
 ('Fine-grained complexity',r'fine.grained|strong exponential time|SETH|orthogonal vectors|3sum'),
 ('Algebraic and numerical computation',r'algebraic complexity|arithmetic circuit|polynomial identity|matrix multiplic|algebraic branching|polynomial factor|tensor rank'),
 ('Average-case complexity',r'average.case complexity|hardness amplification'),
 ('Computability and algorithmic information',r'kolmogorov|computability|algorithmic random|turing degree|busy beaver|reverse mathematics'),
 ('Constraint satisfaction',r'constraint satisfaction|\bCSP\b|polymorph|promise constraint'),
 ('Automated reasoning and unification',r'satisfiability|\bSAT\b|unification|automated reasoning|smt solver'),
 ('Rewriting, lambda calculus and semantics',r'rewrit|lambda|λ.calculus|type theor|dependent type|categorical semantic|game semantic|session type|linear logic|programming.language semantic'),
 ('Infinite-state systems and verification',r'petri net|vector addition|infinite.state|pushdown system|well.structured transition'),
 ('Games, synthesis and verification',r'parity game|energy game|synthesis|model.check|verification|temporal logic|bisimul|hyperlogic'),
 ('Automata and formal languages',r'automata|automaton|formal language|regular language|context.free|transducer|language theor'),
 ('Database theory and finite model theory',r'database|conjunctive quer|query answering|query evaluation|finite model|datalog|relational algebra'),
 ('Algorithms for biological structures',r'bioinform|RNA|DNA|genom|phylogenet|self.assembly|tile assembl|protein'),
 ('Computational topology',r'topolog|homolog|homotop|simplicial complex|knot'),
 ('Computational geometry',r'computational geometry|geometric|polygon|polytope|triangul|visibility|convex hull|voronoi|delaunay|point set|intersection graph|graph drawing|crossing number|rectilinear'),
 ('Temporal graph algorithms',r'temporal graph|temporal connect|temporal path|temporal clique'),
 ('Dynamic graph algorithms',r'dynamic graph|dynamic.*(?:matching|shortest path|connectivity|spanner)|sensitivity oracle'),
 ('Data structures and compressed data',r'data structure|succinct|compress|text index|string algorithm|pattern match|suffix|edit distance|longest common'),
 ('Streaming and sketching',r'streaming|stream algorithm|data stream|sketching|sketch|turnstile'),
 ('Property testing and distribution learning',r'property test|distribution test|distribution learn|tolerant test|junta test|monotonicity test|identity test'),
 ('Algorithmic game theory and fair division',r'fair divis|allocation|envy|EFX|EF1|EFM|maximin|nash|equilibri|auction|mechanism design|social choice|voting|price of anarchy'),
 ('Scheduling and packing',r'schedul|makespan|bin.pack|strip.pack|job shop'),
 ('Online algorithms, bandits and stochastic optimization',r'online algorithm|bandit|regret|reinforcement learn|competitive ratio|prophet|secretary problem|stochastic optim'),
 ('Learning theory',r'learning theory|learn|neural|generalization|empirical risk|VC.dimension|sample complexity|statistical query'),
 ('Distributed and local algorithms',r'distributed|local algorithm|byzantine|consensus|leader election|locality|congest|population protocol|gossip'),
 ('Parameterized and exact algorithms',r'parameteriz|parameteris|kerneliz|kernelis|fixed.parameter|\bFPT\b|exact algorithm'),
 ('Approximation algorithms',r'approximat|integrality gap|inapproxim|steiner|facility location'),
 ('Enumeration and counting',r'enumerat|counting|\#P|\#SAT|\#CSP|permanent'),
 ('Optimization and mathematical programming',r'optimiza|optimisa|linear program|semidefinite|convex program|submodular|subgradient|matroid'),
 ('Computational and circuit complexity',r'complexity class|circuit complexity|circuit lower|\bP/poly\b|\bNP\b|\bBPP\b|\bNC[012]?\b|\bAC[012]?\b|branching program|boolean function'),
 ('Combinatorics and graph polynomials',r'combinatori|discrepancy|ramsey|extremal|graph polynomial|chromatic polynomial|tutte|expander'),
 ('Graph theory and graph algorithms',r'graph|matching|connectivity|shortest path|spanning tree|treewidth|tree.width|clique|coloring|colouring|dominating|path|cut'),
]
VENUE={'TQC':'Quantum computation','ITC':'Cryptography','CCC':'Computational and circuit complexity','COLT':'Learning theory','ALT':'Learning theory','SoCG':'Computational geometry','GD':'Computational geometry','WABI':'Algorithms for biological structures','DNA':'Algorithms for biological structures','IPEC':'Parameterized and exact algorithms','DISC':'Distributed and local algorithms','OPODIS':'Distributed and local algorithms','SAND':'Distributed and local algorithms','ICDT':'Database theory and finite model theory','TYPES':'Rewriting, lambda calculus and semantics','FSCD':'Rewriting, lambda calculus and semantics','CPM':'Data structures and compressed data','CONCUR':'Games, synthesis and verification','CSL':'Proof complexity and logic','SAT':'Automated reasoning and unification','TIME':'Games, synthesis and verification'}

def classify(x):
    # Prefer the question and title; use publisher CCS terms before venue fallbacks.
    primary=x['paper_title']+' '+x['selected_sentence']
    for area,p in RULES:
        if re.search(p,primary,re.I):return area
    for tag in x.get('classifications',[]):
        for area,p in RULES:
            if re.search(p,tag,re.I):return area
    return VENUE.get(x['venue'],'General algorithm design')
