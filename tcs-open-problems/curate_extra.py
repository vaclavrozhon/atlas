from collect import *
rows=[]
def add(title,area,url,collection,year,locator,**kw):
 rows.append(dict(title=title,area=area,source_url=url,source_collection=collection,source_year=str(year),source_locator=locator,authors=kw.pop('authors',''),status='source_open_unverified',status_note=kw.pop('note','Explicitly posed as open in this source; later literature has not been exhaustively checked.'),scope=kw.pop('scope','focused'),accessed='2026-09-09',**kw))
# Concise index labels, with the exact mathematical formulation at the cited locator.
S={
2:'Busy Beaver thresholds for iterated exponentiation',3:'First Busy Beaver value exceeding diagonal Ackermann',4:'Busy Beaver thresholds below epsilon-zero',5:'Busy Beaver thresholds at epsilon ordinals',6:'Busy Beaver thresholds up to Gamma-zero',7:'Busy Beaver thresholds for finite tree and graph theorems',
10:'Fewer-state machines for Goldbach counterexamples',11:'Fewer-state machines for Fermat-prime search',12:'Fewer-state machines for Brocard numbers',14:'Fewer-state machines for Riemann-hypothesis counterexamples',17:'Universal decidable reformulation of weak Collatz',19:'Fewer-state machines detecting nontrivial Collatz cycles',25:'Smaller machines encoding subtle-cardinal consistency',
27:'Degree-four vertices in one-crossing critical graphs',28:'Complexity of four-coloring with one crossing',29:'Four-coloring parameterized by crossing number or genus',30:'Crossing threshold for four-coloring hardness',31:'Reducible configurations permitting one crossing',32:'Four-coloring locally planar toroidal graphs',
33:'Simpler explicit Ramsey lower-bound proofs',34:'Exponential explicit Ramsey graphs via Li’s construction',
36:'Elementary three-party disjointness communication protocols',37:'Elementary k-party disjointness communication protocols',
53:'Expected circuit complexity of detecting half the cliques',
58:'Does derandomizing Promise-ZPP derandomize Promise-BPP?',59:'Query efficiency of PRGs constructed from arbitrary OWFs',60:'Seed efficiency of PRGs constructed from arbitrary OWFs',
69:'Deterministic NP-hardness reductions for Euclidean SVP',70:'Polynomial-factor SVP hardness from standard assumptions',71:'Explicit quantum exponential-time lower bounds for Euclidean SVP',72:'Beyond-base-two lower bounds for lattice problems',73:'Deterministic local density using prime-number lattices',74:'Deterministic local density using Reed–Solomon lattices',75:'Stronger worst-case reductions to SIS and LWE',76:'Smaller-factor coNP or coAM certificates for SVP',77:'Improved exponential-time lattice protocols and reductions',78:'Sub-square-root approximation in coMA for SVP',79:'Dimension-preserving search-to-decision reductions for SVP',80:'Constant-gap hardness of unique SVP',81:'All-constant-factor parameterized approximation hardness of SVP in l1',82:'SVP hardness for fixed-rank module lattices',83:'Reducing factoring or discrete logarithms to approximate SVP',84:'Standard-assumption hardness for cryptographic-factor SVP',86:'Unconditional exponential hardness for cryptographic lattice problems',
101:'Hill’s formula for complete-graph crossing numbers',102:'Albertson’s chromatic-number crossing conjecture',
106:'SAT multi-prover proofs using efficient SAT-oracle provers',107:'A counting function capturing exactly P with NP access',
108:'Halving all complexities of a string tuple',109:'Constant precision for prefix-complexity entropy inequalities',110:'Removing polynomial slack from combinatorial entropy inequalities',111:'Complexity profiles conditioned on one fixed string',112:'Axiomatic strength beyond string complexity',113:'Realizable algorithmic Gray–Wyner profiles',114:'Comparing algorithmic common-information profiles',115:'Random-oracle invariance of Gray–Wyner profiles',116:'An algorithmic Ahlswede–Körner lemma',117:'Faster algorithms for the restricted Ahlswede–Körner lemma',118:'Networks characterized by information-flow inequalities',119:'Equivalence of Shannon and algorithmic network coding',120:'A common theorem for both Slepian–Wolf settings',121:'Reducing information-search tasks to complexity profiles',122:'Efficient search using a Kolmogorov-complexity oracle',123:'Communication for algorithmic secret-key agreement',124:'Secret-key agreement with adversarial side information',125:'Multiparty communication for algorithmic key agreement',126:'Maximum complexity within Hamming neighborhoods',127:'Minimum complexity within Hamming neighborhoods',128:'Complexity distributions on finite affine lines',129:'Quantitative randomness tests using monotone complexity',130:'Finite-prefix characterization of randomness deficiency',131:'Complexity formulas for tests of measure classes',132:'Quantitative forms of randomness preservation theorems',
135:'Unprovability in ZF of BB(20)',136:'Unprovability in PA of BB(10)',137:'Eventually exponential growth between consecutive Busy Beavers',138:'Comparing Busy Beaver runtime and one-count with shifted states',
157:'Polynomial-time construction of longest linked sequences',158:'Complexity of extending linked sequences',159:'Computing optimal linked-sequence length',160:'Counting optimal linked sequences',161:'Complexity of linked sequences over arbitrary finite sets',169:'Decidability and complexity of discrete lambda-convex closures',
175:'Improving the dependence on clause width in k-SAT',177:'Refuting nondeterministic SETH',178:'Fine-grained reductions between OV, 3SUM and APSP',179:'Fine-grained complexity as the number of OV sets grows',180:'Fine-grained reductions from Hitting Set to 3SUM',181:'Subexponential savings for balanced quantified Boolean formulas',
184:'Stronger log-space time lower bounds for SAT',185:'Supercubic uniform formula lower bounds for SAT',186:'Stronger uniform depth-three majority lower bounds for SAT',187:'Excluding quasilinear-time log-space Max Clique',188:'Excluding one-sided randomized quasilinear-time log-space SAT'}
qs=json.loads((ROOT/'sigact_questions.json').read_text())
years={'fast.pdf':2026,'bb.pdf':2026,'cross2.pdf':2026,'crt.pdf':2025,'forehead.pdf':2025,'clique.pdf':2024,'luca.pdf':2024,'svp-color.pdf':2023,'cross.pdf':2022,'oracles.pdf':2021,'kolm.pdf':2021,'busybeaver.pdf':2020,'nate.pdf':2019,'convexfgh.pdf':2018,'finegrain.pdf':2017,'lbfornp.pdf':2016}
for i,title in S.items():
 x=qs[i];fn=x['source_url'].split('/')[-1]
 area='Computability and algorithmic information'
 if fn in ['cross.pdf','cross2.pdf']:area='Graph theory and graph algorithms'
 elif fn=='crt.pdf':area='Pseudorandomness and derandomization'
 elif fn=='forehead.pdf':area='Communication complexity'
 elif fn=='luca.pdf':area='Pseudorandomness and derandomization'
 elif fn=='svp-color.pdf':area='Lattices and computational number theory'
 elif fn in ['oracles.pdf','lbfornp.pdf','clique.pdf']:area='Computational and circuit complexity'
 elif fn=='finegrain.pdf':area='Fine-grained complexity'
 elif fn=='nate.pdf':area='Exact and exponential-time algorithms'
 loc=re.match(r'(?:Open )?(?:Problem|Question|Conjecture)\s+[\d.]+|Q\d+',x['label']).group().rstrip('.')
 add(title,area,x['source_url'],'SIGACT Open Problems Column',years[fn],loc,pdf_url=x['source_url']+'#page='+str(x['pdf_page']))
# Nine recent, separately numbered CSP conjectures.
u='https://www.cs.umd.edu/~gasarch/open/streamapprox.pdf';t=fetch(u)['text']
stream=['Linear space for random-order Max-Cut approximation','An n log n space barrier for streaming Max-Cut','Linear pass-space tradeoffs for Max-Cut','Square-root pass-space tradeoffs for Max-Cut','Polynomial-pass barriers to near-exact streaming Max-Cut','A square-root space barrier for Max-3And','A square-root space barrier for Max-kMonarchy','Lifting sketching resistance to sublinear streaming resistance','An approximation barrier for sublinear-space Max-DiCut']
for i,title in enumerate(stream,1):add(title,'Streaming and sketching',u,'SIGACT Open Problems Column',2025,'Conjecture '+str(i),authors='Noah G. Singer')
# Workshop questions, retaining separate formulations explicitly numbered by the authors.
u='https://pacs2024.github.io/pacs2024-open-problems.pdf'
pacs=['Parameterized complexity of Min-2-Lin over Z4','FPT approximation for deleting negative directed cycles','Edge-deletion list homomorphisms to the specified mixed graph','Sub-base-two algorithms for symmetric Boolean CSPs','Sub-base-two CSP algorithms for Sidon-set relations','Beating meet-in-the-middle for partial-Maltsev SAT','SETH lower bounds for partial-near-unanimity SAT','Characterizing CSP languages with linear non-redundancy','Polynomial kernels for Boolean MinCSP']
for i,title in enumerate(pacs,1):
 if i==1:continue
 add(title,'Constraint satisfaction and parameterized complexity',u,'PACS 2024 workshop',2024,'Question '+str(i))
# LOCAL questions: solved updates and redundant intermediate exponent targets omitted.
u='https://jukkasuomela.fi/open/'
local=[('local','Sub-square-root degree dependence for (Delta+1)-coloring'),('local','Near-linear colors in iterated-logarithmic LOCAL time'),('local','Sublinear-degree LOCAL time for fractional maximal matching'),('local','Sublinear-degree fractional matching on bipartite graphs'),('local','Deciding deterministic LCL complexity on unrooted trees'),('local','Deciding randomized LCL complexity on unrooted trees'),('quantum-local','Quantum speedup for cycle three-coloring'),('non-signaling','Constant-locality non-signaling versus quantum LCL separation'),('non-signaling','Non-signaling LCLs beyond iterated-logarithmic deterministic LOCAL'),('volume','Polynomial-volume maximal matching on bipartite graphs'),('volume','Intermediate deterministic LCL volume complexities'),('volume','Randomized LCL volume between log-star and logarithmic'),('dynamic-online','Constant-locality dynamic three-coloring of unrooted trees'),('dynamic-online','Logarithmic-locality dynamic three-coloring of bipartite graphs'),('dynamic-online','Promise-free linear-versus-constant LOCAL/dynamic-LOCAL separation'),('dynamic-online','Promise-free linear-versus-constant dynamic/online-LOCAL separation')]
for anchor,title in local:add(title,'Distributed and local algorithms',u+'#'+anchor,'Jukka Suomela: locality problems',2026,anchor+' section',authors='Jukka Suomela',note='Page updated 2026-02-23; items explicitly resolved in its updates were omitted. Later literature not exhaustively checked.')
# Independent, dated problem pages submitted by TCS researchers.
u='https://tcsopenproblems.com/';s=soup(fetch(u))
for a in s.select('a[href]'):
 if not re.fullmatch(r'/problem/\d+',a['href']) or a['href']=='/problem/11':continue
 n=int(a['href'].split('/')[-1]);url=urljoin(u,a['href']);r=fetch(url)
 if r.get('code')!=200:continue
 title=txt(a);area='Quantum computation' if n in [2,5,9,10,12,13] else 'Algorithmic game theory and fair division' if n in [3,4] else 'Pseudorandomness and derandomization' if n==7 else 'Coding and information theory' if n==6 else 'Approximation algorithms' if n==1 else 'Graph theory and graph algorithms'
 add(title,area,url,'TCS Open Problems',2026,'Problem '+str(n),scope='landmark' if n==3 else 'focused')
# Amarilli's actively maintained page, selected for databases, logic and representation theory.
# Labels are condensed to avoid reproducing the page's discussions.
u='https://a3nm.net/work/research/questions/'
A={
'oracle-complexity-of-skyline-queries':'Skyline-query oracle complexity',
'constraint-classes-where-separability-is-decidable':'Decidable constraint separability',
'open-world-query-answering-with-linear-rules-and-transitivity-assertions':'Linear rules with transitive predicates',
'decidable-unary-language-with-number-restrictions':'Unary logic with counting restrictions',
'decidability-of-conjunctive-query-containment-under-bag-semantics':'Bag-semantics conjunctive-query containment',
'determinacy-of-path-queries-by-unions-of-path-views':'Path-query determinacy from union views',
'do-tractable-queries-on-probabilistic-instances-have-tractable-lineages':'Tractable probability versus tractable lineage',
'does-bounded-derivation-depth-imply-finite-controllability':'Finite controllability from bounded derivation',
'what-is-the-complexity-of-testing-if-a-query-is-safe':'Recognizing safe probabilistic queries',
'complexity-of-query-evaluation-parameterized-by-treewidth':'Query evaluation with treewidth parameter',
'how-can-one-strengthen-lower-bounds-for-probabilistic-query-evaluation-on-unbounded-treewidth-families':'Probabilistic queries on large-treewidth classes',
'lower-bounds-on-lineage-sizes':'Necessary size of query lineages',
'complexity-of-uniform-reliability-for-homomorphism-closed-queries':'Uniform reliability of homomorphism-closed queries',
'uniform-ptime-algorithm-for-tractable-csps':'Uniform algorithms across tractable CSPs',
'complexity-of-testing-if-a-boolean-function-is-evasive':'Recognizing evasive Boolean functions',
'conciseness-gap-between-formulae-and-circuits':'Formula versus circuit succinctness',
'SmoothStructured':'Efficient smoothing of structured circuits',
'ptime-complementation-of-d-dnnf':'Efficient negation of d-DNNFs',
'weighted-falsifiability-for-unambiguous-dnfs':'Weighted falsification of unambiguous DNFs',
'languages-recognized-by-polynomial-size-dfas':'Languages with small length-specific DFAs',
'context-freeness-of-primitive-words':'Primitive words and context-freeness',
'words-without-shuffle-squares':'Avoiding shuffle-square patterns',
'which-regular-tree-languages-can-be-recognized-by-a-word-automaton':'Word-automaton recognition of tree languages',
'equivalence-of-unambiguous-context-free-grammars':'Equivalence for unambiguous grammars',
'context-free-grammars-with-exactly-two-derivation-trees-per-word':'Exactly-two-parse context-free grammars',
'complexity-of-word-equation-satisfiability':'Complexity of satisfiable word equations',
'complexity-of-counting-antichains-in-restricted-poset-classes':'Counting antichains in restricted posets',
'complexity-of-finding-linear-extensions-of-a-labeled-poset-in-a-regular-language':'Regular-language constrained linear extensions',
'representing-bounded-treewidth-partial-orders':'Representing posets of bounded treewidth',
'complexity-of-the-exact-bipartite-matching-problem':'Deterministic exact bipartite matching',
'graph-reachability-labellings-with-total-orders':'Order-based labels for directed reachability',
'complexity-of-makespan-scheduling-of-unit-jobs-with-precedence-constraints':'Unit-job precedence scheduling complexity',
'complexity-of-multi-machine-scheduling-of-jobs-with-start-dates-end-dates-and-equal-duration':'Equal-length job scheduling with windows'}
s=soup(fetch(u))
for anchor,title in A.items():
 h=s.find(id=anchor);assert h is not None,anchor
 area='Database theory and finite model theory'
 if anchor in list(A)[14:19]:area='Computational and circuit complexity'
 if anchor in list(A)[19:26]:area='Automata and formal languages'
 if anchor in list(A)[26:31]:area='Graph theory and graph algorithms'
 if anchor in list(A)[31:]:area='Scheduling and packing'
 add(title,area,u+'#'+anchor,'Antoine Amarilli: research questions','',anchor,authors='Antoine Amarilli',note='In the active questions section of the page accessed 2026-09-09; no dated current-status guarantee.')
(ROOT/'extra_rows.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2))
print('EXTRA',len(rows))
