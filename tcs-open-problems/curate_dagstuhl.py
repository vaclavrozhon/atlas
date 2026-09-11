from collect import *
import collections
ss=json.loads((ROOT/'dagstuhl_sections.json').read_text())
# Exclude workshop agendas, application wishlists and sections without a delimited question.
BAD_SEMINARS=set('24282 21351 22402 22102 18431 14332 14361 14131 15342 15071 13492 11101 23491 24361 23191 25351 25171 12382 17401 11391 13381 13111 13042 12381'.split())
BAD_KEYS=set('19181:4.10 16101:4.2 16241:4.1 16241:4.9 13151:5.5 13151:5.6 18081:5.2 18081:5.3 23331:5.1 25191:5.2 25191:5.6 24401:4.3 24401:4.4 23091:4.1 23091:4.4 23091:4.7 25392:5.1 25392:5.2 25131:4.1 24021:5.1 24021:5.2'.split())
# Known resolutions, substantial later changes, or a duplicate formulation.
STALE={
'17171:4.3':('Linear-time maximum triangle algorithms appeared in 2017.','https://arxiv.org/abs/1706.03049'),
'17041:4.11':('Parameterized Even Set hardness was subsequently established.','https://arxiv.org/abs/1803.09717'),
'17041:4.12':('FPT inapproximability of Clique and Dominating Set has since been established; old mixed formulation omitted.',''),
'17041:4.14':('Directed odd-cycle transversal has subsequent parameterized hardness results; old formulation omitted pending exact comparison.',''),
'16241:4.10':('Sokal’s zero-free neighborhood conjecture was resolved by Peters and Regts.','https://arxiv.org/abs/1701.08049'),
'14451:4.1':('The older integer-programming running-time target is superseded by later algorithms.',''),
'13331:6.9':('Near-linear pseudopolynomial Subset Sum algorithms supersede this old target.',''),
'19041:4.9':('Parameterized SVP hardness in l1 was subsequently established.','https://arxiv.org/abs/2211.07900'),
'19041:4.6':('Duplicate of the three shortest disjoint paths question in the same report.',''),
'17121:5.2':('Parameterized approximation for Steiner Tree has substantial subsequent results; old target omitted pending comparison.',''),
'11182:4.8':('The combined B1-EPG/B1-VPG recognition record has later hardness resolutions.',''),
'11182:4.12':('Subsequent circle-graph recognition algorithms address the old target.',''),
'17361:4.1':('Use the more recent, precise C3-equivalent vertex-cover gap question in seminar 22051.',''),
'19041:4.4':('Duplicate stochastic bounding-box question; retain seminar 21181.',''),
'13331:6.8':('Duplicate planar-treewidth question; retain seminar 16221.',''),
'13421:4.10':('Duplicate map-graph recognition question; retain seminar 11182.','')}
RENAME={
'19181:4.1':'Deciding negative contractible walks on genus-two surfaces',
'19181:4.2':'Weighted planar level sets and weighted centerpoints',
'19181:4.3':'Tetrahedron multiplicity from face areas, volume and circumradius',
'19181:4.4':'Fast separators in Delaunay triangulations and convex hulls',
'19181:4.5':'Motion planning with symmetric disconnected direction cones',
'19181:4.6':'Additivity of extension complexity under Cartesian products',
'19181:4.7':'Two-edge-colorings minimizing monochromatic geometric crossings',
'19181:4.8':'Subquadratic preprocessing for substring-LCS comparison queries',
'19181:4.9':'Recognizing Minkowski sums of zero-one polytopes',
'19181:4.11':'Perfect plane grid embeddings of trees',
'19181:4.12':'Minimum-weight perfect matching with odd red-edge parity',
'19181:4.13':'Self-improving sorting beyond independent input distributions',
'19181:4.14':'Hamiltonian cycles in first-order Delaunay graphs',
'16101:4.1':'Acyclic subgraphs preserving maximum transitive closure',
'16101:4.3':'Expected optimal alphabetic search-tree cost for random weights',
'22051:4.2':'Tighter query bounds for Tarski fixed points on grids',
'16241:4.5':'Counting colorings through a suitable Q(Delta) construction',
'16241:4.6':'When Cayley-graph homomorphism counts are polynomial',
'16241:4.7':'Dimensions of spaces spanned by graph polynomials',
'18081:5.1':'Second-order cone representability of semialgebraic convex hulls',
'25191:5.7':'Geometric intersection-reporting data structures',
'25191:5.9':'Random access to grammar-compressed strings with fewer auxiliary bits',
'25191:5.10':'Worst-case selection time using median-of-three groups',
'21171:4.5':'Temporal communities, multistage meta-theorems and burstiness',
'24092:4.1':'Subcubic representative computation in persistent homology',
'24092:4.2':'Optimal discrete Morse extensions of partial matchings',
'24092:4.3':'Efficient algorithms for multiparameter persistence',
'24092:4.4':'Proving guarantees for manifold reconstruction',
'24092:4.5':'Efficient computation of topological information gain',
'24092:4.6':'Detecting planted cliques using topological data analysis',
'24092:4.7':'Monotonicity of Euclidean metric magnitude',
'16221:4.1':'Planar vertex-disjoint paths parameterized by path count',
'16221:4.2':'Planar two-edge-connectivity approximation schemes',
'16221:4.3':'Parameterized planar weighted Max Cut',
'16221:4.4':'Planar Steiner Tree parameterized by the solution',
'16221:4.5':'Planar graph immersion algorithms',
'16221:4.6':'Computational complexity of planar treewidth',
'16221:4.7':'Finding large independent sets in restricted planar graphs',
'16221:4.8':'Parameterized subgraph isomorphism in planar graphs',
'16221:4.9':'Optimal exact-distance labels for planar graphs',
'16221:4.10':'Planar minimum-cost Steiner perfect matching',
'12021:4.6':'Structural questions on K-trivial degrees',
'12021:4.7':'Structural questions on higher algorithmic randomness',
'18361:5.5':'Comparisons of Weihrauch degrees for choice principles',
'18421:4.1':'Enumerating mutually diverse feasible solutions',
'18421:4.2':'Output-sensitive enumeration complexity classifications',
'18421:4.8':'Enumeration across primal and dual representations',
'15401:4.3':'Prefix diversity bounds for Boolean languages',
'15392:4':'Weihrauch reducibility and reverse-analysis questions',
'21071:5.1':'Bit-complexity guarantees in extensions of word RAM',
'21071:5.2':'Dynamic all-pairs shortest-path data structures',
'21071:5.3':'Bounding the cost of sequences of heap operations'}
# Multiple explicitly posed questions may be grouped in a source subsection. Splits below
# use the authors' list/numbering; the unsplit parent is removed.
SPLITS={
'25191:5.4':[('bullet 1','Linear-time pattern matching on Lempel–Ziv compressed text'),('bullet 2','Linear-space logarithmic-time random access for Lempel–Ziv strings')],
'25191:5.7':[('bullet 1','Segment-circle queries for connected segment sets'),('bullet 2','Reporting object intersections inside half-plane queries')],
'19181:4.2':[('item 1','Maximum number of weighted separable planar point subsets'),('item 2','Near-linear-time weighted planar centerpoints')],
'19181:4.11':[('Question 1','Complexity of recognizing perfect plane grid embeddings of trees'),('Question 3','Do subcubic trees always admit perfect plane grid embeddings?')],
'19443:5.1':[('item '+str(i),t) for i,t in enumerate(['Reconstructing low-level phylogenetic networks from trinets','Polynomial-time trinet reconstruction of tree-child networks','Parameterized reconstruction from non-dense trinet sets','Triplet reconstruction parameterized by network level','Temporal phylogenetic reconstruction parameterized by reticulations','Tree-child networks displaying three or more binary trees','Orienting unrooted networks into tree-child or stack-free networks','Nonbinary phylogenetic reconstruction parameterized by reticulation count','Single-exponential reticulation algorithms for four binary trees'],1)],
'14342:4.1':[('von Stengel question','Maximum number of extreme equilibria in five-by-five bimatrix games')],
'14342:4.2':[('Savani: congestion games','Complexity of equilibria in asymmetric two-player network congestion games'),('Savani: network coordination','Complexity of mixed equilibria in identical-payoff polymatrix games'),('Paparas: monotone utilities','Polynomial-time equilibrium computation for all monotone utility classes'),('Paparas: non-monotone utilities','Equilibrium hardness using only non-monotone utilities'),('von Stengel: Nash codes','Structure of equilibria in noisy-channel signaling games')]
}
def area(x,title):
 t=x['title'].lower();q=title.lower()
 if re.search('weihrauch|computability|randomness|information theory',t):return 'Computability and algorithmic information'
 if 'graph polynomials' in t or 'permutation' in t or 'pattern avoidance' in t:return 'Combinatorics and graph polynomials'
 if 'phylogen' in t:return 'Algorithms for biological structures'
 if 'scheduling' in t or 'packing' in t:return 'Scheduling and packing'
 if 'parameter' in t or 'graph structure' in t or 'graph decomposition' in t or 'planar' in t or 'exponential' in t:return 'Parameterized and exact algorithms'
 if re.search('geometry|graph drawing|drawing graphs|metric sketch',t):return 'Computational geometry'
 if 'topolog' in t or 'persistence' in q or '3-manifold' in q:return 'Computational topology'
 if re.search('data structure|big data',t):return 'Data structures and compressed data'
 if re.search('game|social|fair division|economics',t):return 'Algorithmic game theory and fair division'
 if re.search('semiring|database|model theory',t):return 'Database theory and finite model theory'
 if re.search('automata|sequence processing',t):return 'Automata and formal languages'
 if re.search('quantum',t):return 'Quantum computation'
 if 'crypt' in t:return 'Cryptography'
 if 'proof' in t:return 'Proof complexity and logic'
 if re.search('logic|verification|formal',t):return 'Games, synthesis and verification'
 if 'dynamic graph' in t or 'distributed meets dynamic' in t:return 'Dynamic graph algorithms'
 if 'temporal graph' in t:return 'Temporal graph algorithms'
 if 'programmable matter' in t:return 'Distributed and local algorithms'
 if 'graph' in t:return 'Graph theory and graph algorithms'
 if 'complexity' in t:return 'Computational and circuit complexity'
 if 'algebra' in t or 'group' in t:return 'Algebraic and numerical computation'
 if 'stochastic' in t:return 'Online and stochastic algorithms'
 if 'enumeration' in t:return 'Enumeration and counting'
 if 'continuous' in t or 'optimization' in t or 'nonlinear' in t:return 'Optimization and mathematical programming'
 if 'learning' in t:return 'Learning theory'
 return 'Algorithms and complexity'

def author(x):
 m=re.search(r'©\s+([^\n]+)',x['text']);return clean(m.group(1)) if m else ''
def make(x,title,sub=''):
 title=re.sub(r'^(?:Open Problem|Problem)\s*\d+:?\s*','',title)
 # The report records the precise formulation and model; this file is an index.
 return dict(title=title,area=area(x,title),source_url=x['source_url'],source_collection='Dagstuhl Reports',source_year=x['source_year'],source_locator='Seminar '+x['seminar']+', section '+x['locator']+('; '+sub if sub else ''),authors=author(x),status='source_open_unverified',status_note='Posed in the seminar report; later resolution has not been exhaustively checked.',scope='focused',accessed='2026-09-09',source_title=x['title'].split(' Edited by')[0],pdf_url=x['issue_url']+'#page='+str(x['pdf_page']),source_key=x['seminar']+':'+x['locator']+(':'+sub if sub else ''))
rows=[];excluded=[]
for x in ss:
 key=x['seminar']+':'+x['locator'];title=RENAME.get(key,x['section_title'])
 if key in STALE:
  reason,solution=STALE[key];excluded.append(dict(title=title,source_url=x['source_url'],reason=reason,solution_url=solution));continue
 if x['seminar'] in BAD_SEMINARS or key in BAD_KEYS:continue
 if key in SPLITS:
  for loc,t in SPLITS[key]:rows.append(make(x,t,loc))
  continue
 # Unstructured parent sections will be curated independently, not counted as questions.
 if '.' not in x['locator']:continue
 # Remove presenters accidentally captured on the title line in older report formats.
 title=re.sub(r' (?:Fedor V\. Fomin|Dimitrios M\. Thilikos|Isolde Adler|Gena Hahn|Paul Hunter|Spyros Angelopoulos|Stephan Kreutzer|Pierre Fraigniaud|Antonios Antoniadis|Christoph Dürr|Anupam Gupta|Magnus M\. Halldórsson|Christos Kalaitzis|Benjamin Moseley|Kirk Pruhs|Tjark Vredeveld|Alexander S\. Kulikov|Andrew Drucker|Eunjung Kim|Fedor V\. Fomin|Hans Bodlaender|Jesper Nederlof|Łukasz Kowalik|Marek Cygan|Mikko Koivisto|Rolf Niedermeier|Rahul Santhanam|Serge Gaspers|Shachar Lovett|Saket Saurabh|Stefan Schneider|Thore Husfeldt)(?: and .*)?$','',title)
 if re.search('various|questions|perspectives|paradigm|classification',title,re.I):r=make(x,title);r['scope']='problem_family';rows.append(r)
 else:rows.append(make(x,title))
(ROOT/'dagstuhl_rows.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2))
(ROOT/'dagstuhl_excluded.json').write_text(json.dumps(excluded,ensure_ascii=False,indent=2))
print('DAG',len(rows),collections.Counter(r['area'] for r in rows))
