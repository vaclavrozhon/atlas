"""Join individually selected pairs and authored short formulations to live cards."""
import collections
import hashlib
import json
from pathlib import Path

BASE=Path(__file__).resolve().parent
ROOT=BASE.parent.parent
DATE='2026-09-11'
rows=[l.split('\t') for l in (BASE/'plan.tsv').read_text().splitlines()]
short=dict(l.split('\t',1) for l in (BASE/'short-problems.tsv').read_text().splitlines())
short.update({
    '0033':'What is the largest separation between quantum query complexity and bounded approximate degree for partial Boolean functions? The polynomial must stay in [0,1] on every Boolean input, including inputs outside the promise.',
    '0036':'Is BQP strictly larger than BPP: is there a total decision problem with a quantum polynomial-time algorithm but no classical randomized polynomial-time algorithm?',
    '0037':'Is NP outside BQP: does SAT have no bounded-error quantum polynomial-time algorithm?',
    '0054':'Can an order-three tensor be decomposed in polynomial time whenever its rank-R factor matrices have Kruskal ranks k_A+k_B+k_C≥2R+2? This is the full uniqueness promise, not an assumption of randomly chosen factors.',
    '1099':'Do there exist integers i>j≥1 for which Buss’s theories T₂^i and T₂^j prove different sentences?',
    '2997':'What is the optimal randomized round complexity of triangle detection in CONGEST on arbitrary n-vertex networks?',
    'new-komlos':'Does every real matrix whose columns have Euclidean norm at most one admit a ±1 column signing with every row sum bounded by a universal constant?',
    'new-beck-fiala':'Does every set system in which each element belongs to at most t sets have discrepancy O(√t), independently of the numbers of sets and elements?',
    'new-matroid-secretary':'Does the general matroid secretary problem admit a constant-competitive randomized strategy for adversarial weights arriving in uniformly random order?',
    'new-polylog-kserver':'Does randomized k-server on every finite metric admit a polylog(k)-competitive strategy against an oblivious adversary, with no dependence on the number of metric points?',
    'new-hierarchical-clustering':'Does Dasgupta’s graph-based hierarchical clustering cost admit a deterministic polynomial-time constant-factor approximation on arbitrary nonnegatively weighted graphs?',
    'new-calibration':'What is the minimax expected ℓ₁ calibration error after T sequential binary forecasts against an adaptive adversary that does not observe the current forecast?',
    'new-counting-dichotomy':'Is approximate counting for every fixed finite family of nonnegative rational Boolean log-supermodular constraints approximation-preserving reducible to #BIS?',
    'new-real-pnp':'Is P_ℝ=NP_ℝ in the exact unit-cost Blum–Shub–Smale model over the ordered real field, allowing finitely many arbitrary real machine constants?',
    'new-superstring':'Can shortest common superstring be approximated within factor two in polynomial time by some algorithm, without restricting it to maximum-overlap greedy?',
    'new-pir-owf':'Do arbitrary one-way functions suffice for sublinear-communication single-server private information retrieval without a database-dependent client hint? The joint security and communication parameters remain to be specified.',
    'new-offline-oram':'Is logarithmic bandwidth overhead unavoidable for offline ORAM with unrestricted data encoding and constant client storage? The exact word-size, memory and security parameters remain to be specified.',
    'new-linear-bellman':'Can stochastic-transition linear Bellman-complete MDPs be learned with polynomial sample and computational complexity in d, H, A and 1/ε, without an exploration oracle? Representation and arithmetic conventions remain to be specified.'
})

affinity={
104:'Sorting and its analysis connect the general integer-sorting barrier with the long-standing average-case complexity of Shellsort.',
112:'Precedence scheduling and min-plus convolution connect approximation limits with resource-sensitive combinatorial algorithms.',
119:'Randomized service and unrelated-machine scheduling connect online load management with the algorithmic difficulty of allocating work.',
121:'Influence-maximization adaptivity and matroid secretary selection concern the value of information in sequential combinatorial optimization.',
123:'Dimension dependence in integer programming and semidefinite extension complexity both ask how efficiently discrete feasible sets can be represented or optimized.',
127:'Integer shortest paths and sparse linear systems are two basic targets for the fast graph and continuous optimization methods in this profile.',
128:'Parallel reachability and min-plus distance circuits ask, in different models, which graph computations can be made fundamentally faster.',
130:'P-matrix complementarity and Smale’s energy problem expose foundational complexity questions in continuous optimization.',
137:'Exact maximum flow and general sparse linear systems capture the reach of nearly linear numerical and graph algorithms.',
140:'Exact planar matching and the planar Steiner ratio connect geometric distances to optimal network structure.',
142:'Polyhedral diameter and Tarski fixed-point queries concern the complexity of navigating geometric and ordered feasible sets.',
143:'Entrywise low-rank approximation and weak convex ε-nets link geometric approximation with compact representations of data.',
150:'The pair concerns the space needed to support random access in two central compressed-text representations.',
151:'The pair connects the approximation of grammar size with searching directly in compressed input.',
153:'Multiple-sequence alignment and approximate edit distance are central algorithmic primitives for comparing biological sequences.',
155:'Circuit minimization and unambiguous logarithmic space connect metacomplexity with the structural space-complexity side of this profile.',
159:'Small-soundness PCPs and the hardness of approximate graph colouring are two substantive manifestations of the PCP and inapproximability program.',
162:'Log-supermodular approximate counting and exact assignment-market equilibrium connect this profile’s counting and equilibrium-complexity work.',
166:'Polynomial simplex rules and deterministic approximate counting connect continuous optimization to derandomized combinatorial computation.',
167:'Log-rank and arithmetic branching-program simulation connect communication lower bounds with algebraic computation.',
169:'The pair concerns polynomial representations of computation and the possibility of exponential quantum savings in communication.',
173:'Restart-free CDCL and Frege versus Extended Frege ask how practical proof mechanisms and stronger proof systems compare.',
180:'The pair links derandomization assumptions to the strength of the circuit lower bounds they imply.',
185:'Classical factoring and the Boolean circuit cost of multiplication concern the basic arithmetic underlying computational number theory.',
    189:'Communication rank and tree codes connect the complexity of interaction with its reliable transmission.',
    190:'Beck–Fiala discrepancy and the log-rank conjecture connect combinatorial structure with the complexity of rounding and communication.',
194:'Adversarial Reed–Solomon list decoding and explicit Gilbert–Varshamov codes separate efficient decoding from explicit code construction.',
202:'The existence of one-way functions and their relation to permutations ask what mathematical foundations symmetric cryptography actually requires.',
210:'Collision-resistant hashing and a worst-case foundation for noisy parity both concern the strength and justification of cryptographic hardness.',
215:'Unleveled FHE and one-way permutations from LWE ask which cryptographic capabilities follow from the lattice assumption alone.',
216:'Exact SVP with limited space and polynomial-factor approximation are two central algorithmic barriers for Euclidean lattices.',
219:'Fourier concentration of DNF and uniform-distribution decision-tree learning connect structural approximation with efficient learning.',
220:'Sample compression and teaching dimension ask whether fundamental learning complexity has equally economical combinatorial explanations.',
221:'Hierarchical clustering and metric k-Median are two central, explicitly defined clustering objectives with unresolved approximation thresholds.',
222:'Entrywise low-rank approximation and information-efficient proper learning connect representation constraints with statistical guarantees.',
224:'Simultaneous scoring-rule regret and calibration ask what one predictor can guarantee under multiple measures of sequential performance.',
227:'Sparse robust estimation and the KLS conjecture connect high-dimensional statistics with concentration and functional inequalities.',
228:'Hierarchical clustering and learning intersections of halfspaces connect data organization with computational learnability.',
230:'Private sample complexity and efficient marginal release concern the statistical and computational price of privacy.',
232:'Gaussian-mixture density estimation and tensor decomposition under Kruskal’s condition ask when statistical identifiability yields efficient algorithms.',
234:'Private stochastic prediction and private marginal release connect sequential statistical estimation with simultaneous data analysis.',
    233:'Private PAC sample complexity and continual counting ask how much accuracy must be lost when statistical outputs protect individuals.',
    235:'Private continual counting and efficient marginal release address the accuracy and computational cost of processing large private datasets.',
    237:'Counting perfect matchings and sampling graph colourings are central barriers in approximate counting and Markov-chain computation.',
238:'The log-supermodular counting boundary and deterministic DNF counting address classification and derandomization of approximate counting.',
    241:'Critical Ising mixing and the KLS conjecture connect high-dimensional sampling with the geometry and phase transitions of probability measures.',
    245:'Deterministic symmetry breaking and CONGEST triangle detection measure the cost of network-wide coordination under different communication constraints.',
248:'Wait-free queue implementation and robustness of consensus numbers concern the computational strength of shared objects, closely connected to topological solvability.',
250:'Optimal deterministic restricted-isometry matrices and optimal sparse-recovery decoding distinguish measurement design from efficient reconstruction.',
252:'Hypergraph cut sparsifiers and Earth Mover Distance sketches ask how much information can be retained in small summaries.',
253:'Streaming reachability and the MPC cycle distinction expose communication barriers behind graph processing with limited local memory.',
268:'Choiceless polynomial time and L versus NL connect descriptive complexity with the power of small-space computation.',
272:'Skolem decidability and deterministic equivalence of d-DNNFs concern exact symbolic questions underlying verification and model representation.',
275:'Simple stochastic games and mean-payoff games are central quantitative game-solving barriers relevant to timed and reactive verification.',
277:'Generalized star height and synchronizing automata ask how algebraic descriptions constrain the expressive and operational behavior of finite automata.',
279:'Internal semisimplicial types and normalization in pure type systems concern the expressive foundations of dependent type theory.',
280:'Word-equation complexity and one-relation monoid equality connect unification to the basic decision theory of rewriting.',
281:'Word equations with lengths and equivalence of decomposable circuits are two concrete decision barriers related to symbolic program analysis.',
    284:'Semisimplicial types and equivalence of decomposable circuits connect expressive foundations with exact reasoning about symbolic program representations.',
285:'One-rule termination and shortest word-equation solutions concern the decision procedures supporting symbolic automation.',
    286:'Modal unification and the consistency of computational hardness with bounded arithmetic concern proof search and the mathematical foundations of automated reasoning.',
287:'One-rule rewriting termination and normalization of pure type systems are foundational questions about semantics-preserving symbolic computation.',
289:'Exact clique-width recognition and minimal dominating-set enumeration concern graph structure and output-sensitive algorithms.',
291:'The exact exponential-time barriers for TSP and Set Cover fit the algebraic and combinatorial algorithmic side of this profile.',
294:'Continuous Local Search and sequential calibration connect equilibrium computation with learning dynamics and forecasting.',
296:'Metric voting distortion and existence of competitive equilibrium connect social-choice information limits with allocation.',
300:'Minimum circuit size and adaptive algorithmic randomness connect description complexity with the foundations of information.'
}

registry=json.loads((ROOT/'data/id_registry.json').read_text())
deleted=json.loads((ROOT/'data/deleted_records.json').read_text())
cards={}
assignments=[]
for row in rows:
    n,name,a,b,why=row
    pair=[]
    for target in (a,b):
        identifier=registry['reviewed:personal-101-300-20260911-'+target[4:]] if target.startswith('new-') else 'TCS-'+target
        assert identifier not in deleted, (name,identifier,'deleted during review')
        path=ROOT/'data/cards'/f'{identifier}.json'
        card=json.loads(path.read_text())
        assert card.get('status') not in ('resolved','excluded'), (identifier,card.get('status'))
        assert target in short, (name,target)
        cards[identifier]=card
        review=card.get('statement_review') or {}
        draft=(not card.get('model_self_contained') or review.get('status')=='needs_specification' or not card.get('definitions'))
        pair.append(dict(target=target,atlas_id=identifier,disposition='new' if target.startswith('new-') else 'existing',short=short[target],source_draft=bool(draft),evidence=card.get('evidence'),status=card.get('status'),references=card.get('references',[]),remaining_issue=review.get('remaining_issue','')))
    assignments.append(dict(number=int(n),researcher=name,affinity=affinity.get(int(n),why),affinity_basis='Editorial inference from the supplied profile and the mathematical targets; not a claim about stated personal priorities.',problems=pair))

assert [r['number'] for r in assignments]==list(range(101,301))
assert all(len(r['problems'])==2 and r['problems'][0]['atlas_id']!=r['problems'][1]['atlas_id'] for r in assignments)
counts=collections.Counter(p['atlas_id'] for r in assignments for p in r['problems'])
new=sorted(k for k,c in cards.items() if c.get('personal_import',{}).get('batch')=='personal-101-300-20260911')
stats=dict(researchers=200,assignments=400,distinct_problems=len(counts),new_cards=len(new),reused_cards=len(counts)-len(new),repeated_assignments=400-len(counts),new_source_drafts=sum(cards[k]['evidence']=='source' for k in new),new_formulation_reviewed=sum(cards[k]['evidence']=='reviewed' for k in new),unique_source_drafts=len({p['atlas_id'] for r in assignments for p in r['problems'] if p['source_draft']}),new_ids=new)
(BASE/'assignments.json').write_text(json.dumps(dict(date=DATE,scope='Researchers 101–300 supplied by the user; two substantial problem suggestions each.',review_limits='Source-backed editorial selection. Existing cards retain their own review status; this report is not a new exhaustive current-openness or formulation certificate for every reused card.',stats=stats,researchers=assignments),ensure_ascii=False,indent=2)+'\n')
(BASE/'stats.json').write_text(json.dumps(stats,indent=2)+'\n')
(BASE/'import-result.json').write_text(json.dumps(dict(imported=new,skipped=[]),indent=2)+'\n')

out=['# Researcher problem suggestions 101–300','',f'Review date: {DATE}. {stats["assignments"]} assignments, {stats["distinct_problems"]} distinct problems: {stats["reused_cards"]} existing cards and {stats["new_cards"]} additions.','',
'Each researcher receives two substantial questions. Affinity is an editorial inference from the supplied research profile and the mathematical content; it is not an assertion that the researcher personally endorsed these priorities. The list gives short formulations, not full technical specifications. The linked canonical cards carry models and references.','',
f'Of the 12 new cards, nine have individually reviewed formulations and three remain explicitly marked source drafts. Across the full selection, {stats["unique_source_drafts"]} distinct cards have incomplete formulation metadata. Reusing an existing card does not newly certify its current openness or its formal completeness. Recent claims and rejected candidates are documented in [the admission audit](admission-audit.md).','',
'Repeated questions point to the same ID. Related but distinct targets retain their existing IDs; for example, exact versus approximate edit distance, or information-theoretic code existence versus efficient construction. The rejected constant-time LCL decidability problem TCS-0513 is absent.','']
for row in assignments:
    out.extend([f'## {row["number"]}. {row["researcher"]}','',row['affinity'],''])
    for p in row['problems']:
        identifier=p['atlas_id'];c=cards[identifier]
        marks=('new; ' if p['disposition']=='new' else '')+('source draft' if p['source_draft'] else 'formulated card')
        if p['status']=='uncertain':
            marks+='; status unverified'
        refs=p['references']
        primary=refs[0] if refs else {}
        source=primary.get('url') or primary.get('pdf_url')
        if not source:
            source=next((x.get('url') or x.get('pdf_url') for x in refs if x.get('url') or x.get('pdf_url')),None)
        assert source, identifier
        out.append(f'- **[{identifier}](../../data/cards/{identifier}.json)** ({marks}): {p["short"]} [Source]({source}).')
    out.append('')
(BASE/'assignments.md').write_text('\n'.join(out)+'\n')

# The live snapshots are verification inputs, not another editable catalogue.
(BASE/'selected-card-digests.json').write_text(json.dumps({k:hashlib.sha256((ROOT/'data/cards'/f'{k}.json').read_bytes()).hexdigest() for k in sorted(cards)},indent=2)+'\n')
print(json.dumps(stats,ensure_ascii=False))
