"""Prepare the user-approved author list; canonical writes are a separate step."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
HERE = Path(__file__).resolve().parent
DATE = '2026-09-13'
BATCH = 'author-problems-20260913'
STRINGS = 'String algorithms and bioinformatics'
GEOMETRY = 'Computational geometry and metric spaces'
RAM = r'''Use a uniform sequential word RAM with word length \(w=d\lceil\log_2(L+2)\rceil\), for a fixed integer \(d\ge 8\) chosen with the algorithm. A fixed finite program must handle every input size; there is no advice, precomputed lookup table or input-dependent oracle. Unit-cost operations are reads, writes, copying, comparisons, branching, Boolean operations, logical shifts, addition, subtraction and multiplication modulo \(2^w\), and integer quotient and remainder for a nonzero divisor. Shifts by at least \(w\) return zero. Addresses and stored values fit words; multiword operations pay for their constituent instructions. Randomized algorithms, when explicitly permitted, may generate independent uniform random words. All initialization, preprocessing, tables and output writes are charged. A static query starts without input-dependent private state, and every retained copy of the input or auxiliary information counts toward index space.'''
YES = 'Give a complete mathematically correct proof checked in Lean of the stated proposition or its logical negation, with the same model, quantifiers and resource guarantees. A conditional lower bound establishes only its conditional conclusion. An improvement that does not meet the full target is insufficient.'
NUM = r'''Supply a specified real number \(a\) and a complete Lean-checked proof that its absolute distance from the defined exponent is at most \(1/100\). A certified enclosing interval of width at most \(1/50\) qualifies through its midpoint. Exact determination also qualifies. Both sides must concern the unrestricted quantity in this card; an assumed hardness conjecture proves only a conditional statement. Repeating the defining infimum or giving only an upper bound is insufficient.'''
CURVE = r'''Supply an unambiguous real-valued function \(g\) on the entire stated domain and a complete Lean-checked proof of \(|g(x)-f(x)|\le 1/100\) at every point, where \(f\) is the target function. Uniform certified upper and lower bounds of width at most \(1/50\) qualify via their midpoint. Exact equality also qualifies. A plot, finitely many sample points, one-sided improvement, or a renamed copy of the defining infimum is insufficient. This numerical acceptance tolerance does not establish a separate exact threshold conjecture.'''

def ref(key, title, url, authors, year, locator):
    return dict(id=key, title=title, url=url, authors=authors, year=year, locator=locator)

R = {
 'munro': ref('munro', 'Text Indexing and Searching in Sublinear Time', 'https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.CPM.2020.24', 'J. Ian Munro; Gonzalo Navarro; Yakov Nekrich', 2020, 'Abstract and main construction and query bounds.'),
 'isa': ref('isa', 'Constant-Time Inverse Suffix Array Queries in Compact Space and Sublinear-Time Construction of Suffix Array Indexes', 'https://arxiv.org/abs/2608.19123', 'Dominik Kempa; Tomasz Kociumaka', 2026, '19 August 2026 preprint; abstract and main theorems.'),
 'sa': ref('sa', 'Compressed Inverse Suffix Arrays', 'https://arxiv.org/abs/2607.17287v2', 'Sharma V. Thankachan', 2026, 'Revision of 2 September 2026; introduction and SA/ISA distinction; announced for FOCS 2026.'),
 'topk': ref('topk', 'Top-k Document Retrieval in Compressed Space', 'https://users.dcc.uchile.cl/~gnavarro/abstracts/soda25.html', 'Gonzalo Navarro; Yakov Nekrich', 2025, 'SODA 2025; author abstract, first paragraph and main bounds.'),
 'er': ref('er', 'The Existential Theory of the Reals as a Complexity Class: A Compendium', 'https://arxiv.org/abs/2407.18006', 'Marcus Schaefer; Jean Cardinal; Tillmann Miltzow', 2024, 'Part I: definition of the class, containments and open questions.'),
 'er25': ref('er25', 'Some Structural Complexity Results for the Existential Theory of the Reals', 'https://arxiv.org/abs/2502.00680', 'Klaus Meer; Adrian Wurm', 2025, 'Structural and relativized complexity results; compare unrelativized class equality.'),
 'jumbled': ref('jumbled', 'On Hardness of Jumbled Indexing', 'https://arxiv.org/abs/1405.0189', 'Amihood Amir; Timothy M. Chan; Moshe Lewenstein; Noa Lewenstein', 2014, 'Problem definition and alphabet-dependent lower bounds.'),
 'mono': ref('mono', 'Deterministic Monotone Min-Plus Product and Convolution', 'https://arxiv.org/abs/2605.07150v2', 'Ce Jin; Jaewoo Park; Barna Saha; Yinzhan Xu', 2026, 'ICALP 2026; abstract, application tables and monotone-convolution theorem.'),
 'oracle': ref('oracle', 'Hamming Distance Oracles', 'https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.CPM.2026.1', 'Itai Boneh; Dvir Fried; Shay Golan; Matan Kraus; Ely Porat', 2026, 'Abstract and exact-oracle bounds for constant and general alphabets.'),
 'km': ref('km', 'Space-Efficient k-Mismatch Text Indexes', 'https://arxiv.org/abs/2510.26264', 'Tomasz Kociumaka; Jakub Radoszewski', 2026, 'SODA 2026; main bounds and section 9, Conclusions.'),
 'ham': ref('ham', 'Faster Algorithms for Text-to-Pattern Hamming Distances', 'https://arxiv.org/abs/2310.13174v3', 'Timothy M. Chan; Ce Jin; Virginia Vassilevska Williams; Yinzhan Xu', 2023, 'FOCS 2023, revised 19 December 2024; exact algorithms and counting-3SUM equivalence.'),
 'eds': ref('eds', 'Elastic-Degenerate String Comparison', 'https://arxiv.org/abs/2411.07782', 'Esteban Gabory; Moses Njagi Mwaniki; Nadia Pisanti; Solon P. Pissis; Jakub Radoszewski; Michelle Sweering; Wiktor Zuba', 2024, 'Definitions, main algorithms and section 9, Open Questions.'),
 'gaps': ref('gaps', 'Gapped String Indexing in Subquadratic Space and Sublinear Query Time', 'https://arxiv.org/abs/2211.16860', 'Philip Bille; Inge Li Gørtz; Moshe Lewenstein; Solon P. Pissis; Eva Rotenberg; Teresa Anna Steiner', 2024, 'STACS 2024; query definition and space/query tradeoffs.'),
 'sum': ref('sum', 'Improved Time-Space Tradeoffs for 3SUM-Indexing', 'https://arxiv.org/abs/2512.04258v2', 'Itai Dinur; Alexander Golovnev', 2026, 'Revision of 23 April 2026; ICALP 2026; main bounds and string-indexing applications.'),
 'sets': ref('sets', 'Conditional Lower Bounds for Space/Time Tradeoffs', 'https://arxiv.org/abs/1706.05847', 'Isaac Goldstein; Tsvi Kopelowitz; Moshe Lewenstein; Ely Porat', 2017, 'SetDisjointness and 3SUM-indexing conjectures and tradeoffs.'),
 'mini': ref('mini', 'GreedyMini: generating low-density DNA minimizers', 'https://pmc.ncbi.nlm.nih.gov/articles/PMC12261476/', 'Shay Golan and coauthors', 2025, 'Definition of expected density; section 5, open questions about complexity and optimal generation.'),
 'optmini': ref('optmini', 'Generating minimum-density minimizers', 'https://doi.org/10.64898/2026.01.25.701585', 'Arseny Shur; Ido Tziony; Yaron Orenstein', 2026, '28 January 2026 preprint; abstract, Theorem 1 and complexity discussion.'),
 'lcs': ref('lcs', 'Exploring the Gap Between LCS and LCStr', 'https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.CPM.2026.27', 'Shay Golan and coauthors', 2026, 'Introduction: LCS approximation on growing alphabets and comparison with LCSS.'),
 'lcs25': ref('lcs25', 'Deterministic LCS Approximation in Near-Linear Time', 'https://arxiv.org/abs/2507.22486', 'Itai Boneh; Shay Golan; Matan Kraus', 2025, 'Abstract and main approximation theorem.'),
 'monge': ref('monge', 'Fast Distance Multiplication of Unit-Monge Matrices', 'https://doi.org/10.1007/s00453-013-9830-z', 'Alexander Tiskin', 2015, 'Algorithmica 71:859–888; definitions of simple unit-Monge matrices and introduction attributing the linear-time question to Landau.'),
 'monge25': ref('monge25', 'Core-Sparse Monge Matrix Multiplication: Improved Algorithm and Applications', 'https://arxiv.org/abs/2408.04613v2', 'Paweł Gawrychowski; Egor Gorbachev; Tomasz Kociumaka', 2025, 'ESA 2025; revised 7 July 2025; abstract retains the unit-Monge bound.'),
 'nfa': ref('nfa', 'The NFA Acceptance Hypothesis: Non-Combinatorial and Dynamic Lower Bounds', 'https://arxiv.org/abs/2311.10204', 'Karl Bringmann; Allan Grønlund; Marvin Künnemann; Kasper Green Larsen', 2024, 'TheoretiCS 2024; Hypothesis 1.1 and formal parameterized hypothesis.'),
 'regex': ref('regex', 'Sparse Regular Expression Matching', 'https://arxiv.org/abs/1907.04752', 'Philip Bille; Inge Li Gørtz', 2024, 'SODA 2024; abstract and simulation-density model.'),
 'rindex': ref('rindex', 'Optimal-Time Text Indexing in BWT-runs Bounded Space', 'https://arxiv.org/abs/1705.10382', 'Travis Gagie; Gonzalo Navarro; Nicola Prezza', 2017, 'BWT-run-bounded indexes and compressed suffix-tree representation.'),
 'rtree': ref('rtree', 'Non-overlapping Indexing in BWT-Runs Bounded Space', 'https://par.nsf.gov/servlets/purl/10539699', 'Lorraine A. K. Ayad and coauthors', 2024, 'Introduction and section 3.1: full suffix-tree space bound and unresolved run-linear representation.'),
 'ted': ref('ted', 'Hardness of Dynamic Tree Edit Distance and Friends', 'https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.ITCS.2026.78', 'Christopher Ye and coauthors', 2026, 'Abstract and discussion distinguishing the static and dynamic unweighted problems.'),
 'ed': ref('ed', 'Approximation Schemes for Edit Distance and LCS in Quasi-Strongly Subquadratic Time', 'https://arxiv.org/abs/2603.29702', 'Xiao Mao; Aviad Rubinstein', 2026, 'STOC 2026; main approximation-scheme theorem.'),
 'nn': ref('nn', 'Incremental Planar Nearest Neighbor Queries with Optimal Query Time', 'https://arxiv.org/abs/2504.07366', 'John Iacono; Yakov Nekrich', 2025, 'Abstract and main insertion/query guarantees.'),
 'nnold': ref('nnold', 'The Open Problems Project: Dynamic Planar Nearest Neighbors', 'https://topp.openproblem.net/p63', 'The Open Problems Project', 2006, 'Problem 63, statement.'),
 'voronoi': ref('voronoi', 'The Open Problems Project: Voronoi Diagram of Lines in 3D', 'https://topp.openproblem.net/p3', 'The Open Problems Project', 2001, 'Problem 3, statement, conjecture and references to Sharir.'),
 'durer': ref('durer', 'The Open Problems Project: Edge-Unfolding Convex Polyhedra', 'https://topp.openproblem.net/p9', 'The Open Problems Project', 2001, 'Problem 9, convex edge-unfolding formulation.'),
 'points': ref('points', 'Universal Point Sets for Subclasses of Planar Graphs', 'https://arxiv.org/abs/2303.00109', 'Stefan Felsner; Hendrik Schrezenmaier; Felix Schröder; Raphael Steiner', 2023, 'General problem and linear-size constructions for restricted classes.'),
 'pointsold': ref('pointsold', 'The Open Problems Project: Smallest Universal Set of Points for Planar Graphs', 'https://topp.openproblem.net/p45', 'The Open Problems Project', 2001, 'Problem 45, statement and point-set convention.'),
 'labels': ref('labels', 'Better Distance Labeling for Unweighted Planar Graphs', 'https://doi.org/10.1007/s00453-023-01133-z', 'Paweł Gawrychowski; Przemysław Uznański', 2023, 'Introduction and main label-size theorem; journal version of WADS 2021.'),
 'msa': ref('msa', 'Multiple Sequence Alignment', 'https://i.cs.hku.hk/~chin/paper/encycl_msa-1.pdf', 'Francis Y. L. Chin and coauthors', 2008, 'Encyclopedia article; sum-of-pairs objective and approximation barrier.'),
 'msaopen': ref('msaopen', 'Some Open Problems in Computational Molecular Biology', 'https://profs.sci.univr.it/~rrizzi/classes/BioComp2003/homeworks/openProblems.pdf', 'Tao Jiang', 2002, 'Multiple sequence alignment and approximation questions.'),
}

ASSIGNMENTS = [
 ('J. Ian Munro', ['P01','P02']), ('Gonzalo Navarro',['P04','P03']),
 ('Yakov Nekrich',['P04','P05']), ('Jean Cardinal',['P06','P07']),
 ('Moshe Lewenstein',['P08','P09']), ('Ely Porat',['P10','P11']),
 ('Micha Sharir',['P12','P13']), ('Erik Demaine',['P14','P15']),
 ('Stefan Felsner',['P07','P16']), ('Tomasz Kociumaka',['P17','P18','P19']),
 ('Jakub Radoszewski',['P18','P20']), ('Solon P. Pissis',['P21','P20']),
 ('Shay Golan',['P22','P23']), ('Paweł Gawrychowski',['P24','P25']),
 ('Gad Landau',['P26','P17']), ('Amihood Amir',['P19','P08']),
 ('Masayuki Takeda',['P25','P27']), ('Maxime Crochemore',['P27','P28']),
 ('Inge Li Gørtz',['P21','P29']), ('Philip Bille',['P03','P30']),
 ('Travis Gagie',['P31','P27']), ('Esko Ukkonen',['P28','P32']),
]
EXISTING = dict(P03='TCS-0467', P05='TCS-0387', P07='TCS-7177', P09='TCS-7334',
 P10='TCS-7333', P12='TCS-0318', P13='TCS-0417', P14='TCS-6498', P15='TCS-0406',
 P16='TCS-0377', P17='TCS-7235', P24='TCS-0775', P25='TCS-0468', P27='TCS-6513',
 P28='TCS-7322', P32='TCS-6669')
CARDS = {}

def card(pid, title, formal, definitions, contexts, why, refs, progress, summary,
         *, area=STRINGS, criterion='resources', qtype='yes_no', score=85,
         status='source_open', note='', answer=YES, category_note=None):
    assert len(summary)==5, pid
    CARDS[pid] = dict(
        key=f'{BATCH}:{pid.lower()}', title=title, area=area, criterion=criterion,
        question_type=qtype, formal=formal, definitions=definitions,
        context_blocks=[dict(text=x) if isinstance(x,str) else dict(text=x[0],citation=x[1]) for x in contexts],
        why=why, answer_criterion=answer, references=[R[x] for x in refs],
        progress=[dict(date=d,text=t,citation=c) for d,t,c in progress],
        year=max(R[x]['year'] for x in refs), evidence='reviewed', status=status,
        status_note='Primary sources and subsequent-result searches checked on 13 September 2026. No resolution of the precise target was located; this is a bounded literature review, not exhaustive certification of current openness. '+note,
        model_self_contained=True, requires_context=False,
        statement_review=dict(status='revised',reviewed_on=DATE,remaining_issue='',reason=note or 'Individual input, model, quantifier, source and answer-criterion review.'),
        formulation_reviewed_on=DATE, reviewed_on=DATE,
        review_note=note+' Recent preprint claims have not been independently proof-checked.',
        importance=dict(score=score,method='editorial',assessed_on=DATE,reason=why),
        category_assignment=dict(method='editorial_topic',reason=category_note or 'The main target is a general string-processing, compressed-representation or sequence-comparison primitive.'),
        working_summary=dict(sentences=summary,basis='saved_sources',written_on=DATE,source_refs=refs),
        related=[], related_problem_ids=[])

card('P01', 'Polyloglogarithmic suffix-array access in compact space',
 r'Is there a uniform deterministic static index that represents every binary string \(T\) of length \(n\ge2\) in \(O(n)\) bits and answers every suffix-array query \(\operatorname{SA}_T[i]\), for \(0\le i<n\), in \(O((1+\log\log(n+2))^c)\) worst-case time for one universal constant \(c\ge1\)?',
 r'\(\operatorname{SA}_T\) lists the starting positions of the nonempty suffixes of \(T\) in lexicographic order, with \(0<1\) and a proper prefix preceding the longer string. Positions and ranks are zero-based. Set \(L=n\) in the following model. '+RAM+r' Preprocessing is deterministic and polynomial in \(n\); its polynomial and all constants are fixed with the index. The bit-space bound includes all retained copies of the text, samples, pointers and tables. Temporary query storage is included in the same bound. The externally supplied query and returned answer each occupy one word.',
 [r'A suffix-array query translates lexicographic rank into a position in the original text. It is a central navigation operation inside compressed search indexes.',
  ('The 2026 inverse-suffix-array results distinguish this operation from translating a text position into its suffix rank.','sa'),
  ('An August 2026 preprint gives constant-time compact inverse access and a nonconstant deterministic lower bound for forward suffix-array access.','isa'),
  r'The proposed bound keeps the entire representation proportional to the binary text, rather than allowing one full pointer per suffix.'],
 'This asks whether a representation close to the information content of a text can support powerful navigation with only an iterated-logarithmic time cost.',
 ['sa','isa','munro'], [('2026-09-02','The revised inverse-suffix-array paper identifies subpolynomial-logarithmic forward access in compact space as a major remaining challenge.','sa')],
 ['A suffix array orders all suffixes of a string lexicographically.','A query asks where a suffix of a given rank starts.','The target stores a binary text and its index in linear bits.','Each query must take a fixed polynomial in the logarithm of the logarithm of the text length.','Constant-time inverse suffix-array access does not settle this direction.'],
 note='The polyloglogarithmic threshold and polynomial preprocessing convention are explicit editorial specializations of the compact-SA frontier.')

card('P02', 'Input-optimal construction of compact inverse suffix arrays',
 r'Can a uniform deterministic algorithm, given a packed binary string \(T\) of length \(n\ge2\), construct in \(O(1+n/\log(n+2))\) worst-case time an \(O(n)\)-bit static index that answers every inverse-suffix-array query in \(O(1)\) worst-case time?',
 r'The input supplies \(n\) and the consecutive bits of \(T\), packed into words with only the last word padded. \(\operatorname{ISA}_T[i]\) is the zero-based lexicographic rank of \(T[i..n)\) among all nonempty suffixes, with \(0<1\) and shorter proper prefixes first. Set \(L=n\). '+RAM+r' Every bit retained after construction, including the input if retained, counts toward the index. Query work storage is also charged to this bit bound. The construction time includes reading the packed input and writing every index word; no prebuilt instance-dependent structure is supplied.',
 [r'A packed binary text contains many symbols in a machine word. Linear time in the number of characters can therefore exceed the cost of reading the input by a logarithmic factor.',
  (r'The August 2026 preprint claims a compact constant-time inverse index with deterministic construction in \(O(n/\sqrt{\log n})\) time for binary texts.','isa'),
  r'This question concerns constructing that functionality at the scale of the packed input. The required query operation is already supported by the cited construction.'],
 'Closing the construction gap would make a fundamental compact text index as cheap asymptotically as reading and writing its representation.',
 ['isa','munro'], [('2026-08-19',r'A preprint supplies the desired final space and query functionality with \(O(n/\sqrt{\log n})\) construction time.','isa')],
 ['The input is a binary text stored in packed machine words.','The output must answer inverse suffix-array queries in constant time.','All retained information must use linear bits.','The question asks for construction time proportional to the number of input words.','The newest cited construction has a square-root-logarithmic gap from that target.'],
 status='uncertain',score=82,note='The input-optimal endpoint is an editorial strengthening tied to a very recent preprint; the precise endpoint has not been independently certified open.')

card('P04', 'Optimal top-k document retrieval in compact space',
 r'Does a uniform deterministic static index exist for every collection \(D_1,\ldots,D_d\) of nonempty strings of total length \(n\ge2\) over \([0..\sigma)\), where \(2\le\sigma\le n\), using \(O(n\log\sigma)\) bits and answering top-\(k\) queries in \(O(1+m/\log_\sigma n+k)\) worst-case time?',
 r'A query gives \(1\le k\le d\) and a nonempty packed pattern \(P\) of length \(m\le n\). The frequency of \(P\) in a document is its number of starting positions, counting overlapping occurrences. Return the identifiers of the \(\min(k,h)\) highest-frequency documents among the \(h\) documents containing \(P\), in decreasing frequency, breaking ties by increasing identifier. No occurrence crosses a document boundary. Documents are identified by their input order. The alphabet symbols occupy \(\lceil\log_2\sigma\rceil\) bits each in the packed query. Set \(L=n\). '+RAM+r' Preprocessing takes polynomial time in \(n\). Space includes document boundaries, identifiers, retained text and every persistent auxiliary structure. Query working memory, excluding the supplied pattern and streamed output, also fits the stated bit bound. All constants are uniform in \(n,d,\sigma,m,k\).',
 [r'A collection-level search query often needs the most relevant documents rather than every individual occurrence of a pattern.',
  (r'Navarro and Nekrich explicitly ask for optimal retrieval in space close to the packed text size. Their SODA 2025 structure uses a compressed suffix array plus an additional \(O(n\log\log n)\) bits.','topk'),
  r'On small alphabets that additional storage is asymptotically larger than the text. Sorting results by frequency and counting all stored boundaries are part of the target.'],
 'This joins ranked retrieval with compact text indexing, a basic requirement for searchable document and genome collections whose auxiliary indexes should not dominate their input.',
 ['topk'], [('2025','The source obtains near-optimal query costs relative to a compressed suffix array, while explicitly retaining the optimal compact-space problem.','topk')],
 ['A query asks for the documents in which a pattern occurs most often.','Documents are ranked by occurrence count with a fixed tie rule.','The desired index occupies only a constant multiple of packed text size.','The query cost must match reading the packed pattern and writing the requested identifiers.','The current source retains additional space or query overhead.'],
 score=87,note='Occurrence-count relevance, sorted results and tie-breaking fix one explicitly discussed retrieval model.')

card('P06', r'\(\exists\mathbb{R}\) versus \(\mathrm{NP}\)',
 r'Is \(\exists\mathbb{R}=\mathrm{NP}\) under polynomial-time many-one reductions between finitely encoded decision problems?',
 r'Let ETR be the following language of finite binary strings. An instance is an existential sentence \(\exists x_1,\ldots,x_m\in\mathbb R:\Phi(x_1,\ldots,x_m)\), where \(\Phi\) is an explicitly represented Boolean formula with atoms \(p=0\) or \(p>0\). Each \(p\) is an integer-coefficient polynomial, supplied as a list of monomials with coefficients and nonnegative exponents in binary. Parentheses, connectives, variable indices and all lengths are explicitly encoded; invalid encodings are rejected. Truth uses exact real arithmetic as mathematical semantics, not unit-cost computation. \(\exists\mathbb R\) is the class of languages reducible to ETR by a deterministic Turing machine in time polynomial in input bit length. \(\mathrm{NP}\) consists of languages with polynomial-length binary witnesses checked by deterministic polynomial-time Turing machines. Equivalent fixed finite-tape machine conventions may be used. The question is unrelativized.',
 [r'Real solutions describe geometric positions, distances and continuous parameters, but need not have short rational coordinate descriptions.',
  (r'The complexity class organizes a large family of geometric recognition and realization problems. Its known containments are \(\mathrm{NP}\subseteq\exists\mathbb R\subseteq\mathrm{PSPACE}\).','er'),
  ('Relativized structural results do not decide whether ordinary finite binary certificates suffice for the unrelativized class.','er25')],
 'The answer would determine whether many geometric existence problems admit the same kind of efficiently checkable discrete certificates as classical NP problems.',
 ['er','er25'], [('2024','The compendium presents the class, its containments and unresolved comparisons.','er'),('2025','Structural and oracle results leave the unrelativized equality unanswered.','er25')],
 ['Existential real formulas ask whether polynomial constraints have a real solution.','The input is a finite binary description of the constraints.','The class contains NP and is contained in PSPACE.','The question asks whether it is exactly NP.','An oracle separation or a rational-coordinate obstruction alone does not answer that class comparison.'],
 area='Computational complexity',criterion='models',score=94,category_note='This is a comparison of complexity classes; geometric realization supplies motivation rather than a restriction of the target.')

card('P08', 'Preprocessing exponent of binary jumbled indexing',
 r'Determine \(\alpha_{\mathrm{BJ}}\), the infimum of real \(a\ge1\) for which, for every rational \(\eta>0\), a uniform deterministic index for binary strings of length \(n\) has \(O(n^{a+\eta})\) worst-case preprocessing time, \(O(n)\) words of stored space and \(O(1)\) worst-case query time.',
 r'The input is an explicit string \(T\in\{0,1\}^n\), with \(n\ge2\). A query is a pair of nonnegative integers \((u,v)\) with \(1\le u+v\le n\), and asks whether a contiguous substring has exactly \(u\) zeroes and \(v\) ones. Answers must be exact. All retained text and tables count toward space. Set \(L=n\). '+RAM+r' For each proposed \(a,\eta\), one finite construction/query pair and its constants must work for every \(n\) and every string; it receives no real parameter as input and may depend only on the chosen parameters. The infimum need not be attained. The cost of the original explicit input, indexing and output is included. The target is an exponent measured in powers of \(n\); no additive tolerance is applied to a big-O expression.',
 [r'Jumbled matching ignores order inside a substring and retains only its symbol counts. A single index must answer queries of all lengths.',
  ('The binary case differs from the larger-alphabet variants for which Amir and coauthors prove conditional preprocessing/query barriers.','jumbled'),
  (r'The 2026 monotone-convolution result yields deterministic preprocessing exponent at most \(3/2\) for the binary application.','mono'),
  r'The infimal exponent records the remaining asymptotic construction gap without counting a solved first-subquadratic result as open.'],
 'A sharp construction exponent would identify the true cost of a basic order-insensitive text-search primitive and clarify its relation to structured convolution.',
 ['jumbled','mono'], [('2026',r'Deterministic monotone convolution takes \(n^{3/2+o(1)}\) time and supports the corresponding binary-jumbled construction.','mono')],
 ['The text is binary and queries prescribe counts of zeroes and ones.','A query asks whether any substring has exactly those counts.','The index has linear word space and constant query time.','The target is the best uniform deterministic preprocessing exponent.','The numerical benchmark asks for a certified value to absolute accuracy one hundredth.'],
 qtype='numerical_value',criterion='tightness',answer=NUM,status='uncertain',score=84,note='The approved optimal-preprocessing topic is formalized as an infimal exponent, with the standard absolute 0.01 numerical criterion; openness at this precise tolerance is not independently certified.')

card('P11', 'General-alphabet Hamming oracles with optimal preprocessing',
 r'Is there a uniform deterministic data structure which, for every pair of strings of lengths \(n,m\ge1\) and every integer \(1\le x\le\min(n,m)\), uses \(\widetilde O(nm/x)\) preprocessing time and stored words and answers exact substring Hamming-distance queries in \(O(x)\) worst-case time?',
 r'The strings \(A\) and \(B\) are supplied explicitly over \([0..(n+m)^2)\). A query \((i,j,\ell)\) satisfies \(0\le i\le n\), \(0\le j\le m\), and \(0\le\ell\le\min(n-i,m-j)\). It returns \(|\{t:0\le t<\ell,\ A[i+t]\ne B[j+t]\}|\). Positions are zero-based; a length-zero query returns zero. Set \(L=n+m\). '+RAM+r' The soft-O means multiplication by \((\log(L+2))^c\) for one fixed constant \(c\), independent of \(x,n,m\). One fixed algorithm receives \(x\) during preprocessing and handles all admissible parameters. The stored space includes both strings, if retained, and all auxiliary information. Query space is included; no offline knowledge of future queries is supplied.',
 [r'The same pair of strings can participate in many comparisons between internal intervals. An oracle pays once for a reusable representation.',
  (r'The CPM 2026 source gives \(\widetilde O(nm/x)\) preprocessing for constant alphabets but \(\widetilde O(nm/\sqrt{x})\) for general alphabets, both with \(O(x)\) queries.','oracle'),
  r'The question transfers the smaller preprocessing regime to general integer alphabets. Exact answers, preprocessing time and query time are separate requirements.'],
 'This isolates the cost of reusable exact similarity queries and tests whether large alphabets create an inherent preprocessing penalty.',
 ['oracle'], [('2026','The source establishes distinct exact-oracle tradeoffs for constant and general alphabets; its lower bound is conditional and restricted to combinatorial algorithms.','oracle')],
 ['Two strings are preprocessed before their substring comparisons are known.','Each query requests the exact Hamming distance between equal-length intervals.','A parameter controls the allowed query time.','The proposed preprocessing bound matches the constant-alphabet regime.','Current general-alphabet bounds have a square-root loss in that parameter.'],
 score=86,note='This is the deterministic general-alphabet endpoint of the approved tradeoff question; the source does not claim a matching general lower bound.')

card('P18', 'Linear-space k-mismatch text indexing',
 r'For every fixed integer \(k\ge2\), does a uniform deterministic static index of every text of length \(n\ge2\) exist using \(O(n)\) words, polynomial preprocessing time, and \(O(m+(\log(n+2))^{c(k)}+\mathrm{occ})\) worst-case query time for some function \(c:\mathbb N\to\mathbb N\)?',
 r'The explicit text \(T\) and explicit query pattern \(P\) use alphabet \([0..n)\). A query has length \(1\le m\le n\) and reports every position \(i\in[0..n-m]\) with \(|\{j\in[0..m):T[i+j]\ne P[j]\}|\le k\), without duplicates and in any order. \(\mathrm{occ}\) is the number of these positions. Set \(L=n\). '+RAM+r' A program may depend on fixed \(k\), but cannot depend on \(n,T,P\). Space, time and preprocessing constants may depend on \(k\). The text and all retained auxiliary information count toward linear word space, as does query workspace excluding the explicit query and streamed output. All queries are exact, and the pattern is not available during preprocessing.',
 [r'Approximate indexing supports repeated searches allowing a bounded number of substitutions. Large output size is accounted for separately.',
  (r'Kociumaka and Radoszewski improve the general-alphabet space bound to \(O(n\log^{k-1}n)\) and explicitly ask for further space and query improvements.','km'),
  r'The linear-space question fixes each error budget independently and allows a polynomial in the logarithm for query overhead. Insertions and deletions are outside the model.'],
 'This is a core approximate-search interface whose space overhead can determine whether a large collection remains indexable.',
 ['km'], [('2026',r'SODA 2026 improves the general k-errata-tree space bound while retaining its query time; section 9 poses the remaining optimization questions.','km')],
 ['A text is indexed before query patterns arrive.','A query reports all positions with at most a fixed number of substitutions.','The proposed structure uses only linear word space.','Its cost is pattern length, polylogarithmic overhead and output size.','The recent general improvement still uses additional logarithmic factors in space.'],
 score=88,note='Linear space is an editorial strengthening of the source’s explicit remaining space question; k equals one is deliberately outside this target.')

card('P19', 'Text-to-pattern Hamming distances below the square-root barrier',
 r'Does there exist a constant \(\varepsilon\in(0,1/2)\) and a uniform Las Vegas algorithm that computes the exact Hamming distance at every alignment of an explicit pattern of length \(m\) in an explicit text of length \(n\), for all \(n\ge2\) and \(1\le m\le n\), in \(O(nm^{1/2-\varepsilon})\) expected time?',
 r'The alphabet is \([0..n^2)\), and the required output is the list \(h_i=|\{j\in[0..m):P[j]\ne T[i+j]\}|\) for \(i=0,\ldots,n-m\), in increasing alignment order. Set \(L=n\). '+RAM+r' The algorithm must terminate almost surely and return the entire list correctly on every terminating random execution. The expectation is over its internal randomness for each fixed input, with universal constants. There is no text preprocessing supplied for free, and time includes every output entry. The target is a fixed positive saving in the power of \(m\), uniformly over both lengths.',
 [r'Computing the mismatch count at every position is the basic all-alignments comparison task. It asks for exact counts rather than threshold decisions or relative approximations.',
  (r'The FOCS 2023 result gives \(O(n\sqrt m)\) Las Vegas time and a fine-grained equivalence with a range-restricted counting version of 3SUM.','ham'),
  r'The equivalence does not provide an unconditional matching lower bound, and the counting problem must not be replaced by ordinary decision 3SUM.'],
 'A polynomial improvement would cross a central exponent barrier for exact approximate-matching computations and their arithmetic counting counterparts.',
 ['ham'], [('2023 / 2024',r'The revised FOCS paper obtains \(O(n\sqrt m)\) expected time and the precise counting equivalence.','ham')],
 ['The task compares one pattern against every possible text alignment.','Every mismatch count must be returned exactly.','All preprocessing and output costs are charged.','The target saves a fixed power of pattern length over the square-root bound.','The known counting-3SUM equivalence does not itself prove the target impossible.'],
 score=89,note='The fixed exponent saving is the explicit editorial threshold approved in the proposal; randomization is Las Vegas rather than bounded-error approximation.')

card('P20', 'Faster elastic-degenerate string intersection',
 r'Does there exist a constant \(\varepsilon>0\) and a uniform classical randomized algorithm deciding intersection of two elastic-degenerate strings in \(\widetilde O(N_1+N_2+n_2N_1^{\omega-1-\varepsilon}+n_1N_2^{\omega-1-\varepsilon})\) worst-case time, with probability of correctness at least \(2/3\) on every input?',
 r'An elastic-degenerate string \(E_i\) is an explicit list of \(n_i\ge1\) finite sets of distinct strings. Each set contains a nonempty string and may additionally contain the empty string. Its language consists of concatenations obtained by choosing one alternative from each set in order. Let \(N_i\) be the sum of the lengths of all alternatives, so \(N_i\ge n_i\). Delimiters are included in the encoding; the number of alternatives is at most \(2N_i\). Blocks containing only the empty string are omitted from this input convention. Symbols lie in \([0..(N_1+N_2)^2)\). The output says whether the two languages share any string; neither language is explicitly expanded. Set \(L=N_1+N_2\). '+RAM+r' Soft-O permits one fixed power of \(\log(L+2)\). Here \(\omega\) is the infimum of real exponents \(a\) such that square matrix multiplication over the rationals has uniform algebraic algorithms using \(O(t^{a+\eta})\) field operations for every fixed \(\eta>0\), with \(t\) the matrix dimension. The string algorithm need not be combinatorial. All constants and its finite program are independent of the input sizes.',
 [r'A pangenome representation can store a sequence of alternative sequence fragments. Its represented language can be exponentially larger than the explicit alternatives.',
  (r'The source gives an upper bound involving \(n_2N_1^{\omega-1}+n_1N_2^{\omega-1}\) and explicitly asks about a polynomial improvement in section 9.','eds'),
  r'The separate linear input term makes the target meaningful when the algebraic expression falls below the cost of reading the alternatives. It changes no requirement to compare entire represented languages.'],
 'This is a fundamental comparison operation on succinct pangenome representations, with substantial room between general hardness and parameter-sensitive algorithms.',
 ['eds'], [('2024','The extended paper gives algorithms and conditional lower bounds, and identifies the exponent improvement as an open question.','eds')],
 ['Each input describes many strings through ordered sets of alternatives.','The task asks whether their represented languages overlap.','The inputs are explicit alternatives rather than compressed grammars.','The target saves a fixed power over the current algebraic dependence on total alternative length.','The running time still pays for reading both representations.'],
 score=83,note='The source question is made explicit with an additive input-reading term, a normalized empty-block convention and bounded-error randomization.')

card('P21', 'Space-query exponent curve of gapped string indexing',
 r'Determine \(s_{\mathrm{gap}}(\delta)\) for every real \(\delta\in[0,1]\), where \(s_{\mathrm{gap}}(\delta)\) is the infimum of \(s\ge1\) for which gapped string reporting admits static indexes with space \(O(n^{s+\eta})\) words and query time \(O(m_1+m_2+n^{\delta+\eta}(1+\mathrm{occ}))\) for every fixed rational \(\eta>0\).',
 r'The explicit text \(T\) has length \(n\ge2\) over \([0..n)\). A query gives two explicit nonempty patterns \(P_1,P_2\) of lengths \(m_1,m_2\le n\), and integers \(0\le a\le b<n\). Report without duplicates all ordered pairs \((i,j)\) of valid starts for these patterns with \(a\le j-i\le b\); overlaps and \(i=j\) are allowed when consistent. The output may have any order and its true size is \(\mathrm{occ}\). For each chosen \(\delta,s,\eta\), one uniform finite randomized preprocessing/query pair and its constants handle every text size and query. Preprocessing must run in polynomial time; its degree may depend on the chosen parameters. Space and query time hold for every random outcome; every fixed input/query has correct complete output with probability at least \(2/3\), over preprocessing and query randomness. Set \(L=n\). '+RAM+r' Stored inputs, random seeds and tables count. Query workspace is included in the space bound, apart from the query and streamed output. The infimum need not be attained. Parameters indexing the curve select uniform programs; they are not real-number advice supplied to a computation. The target is a dimensionless exponent function, not the memory size for one finite input.',
 [r'Two sequence motifs can be meaningful together only when their occurrences lie within a requested distance range. The gap bounds here arrive with the query.',
  ('The STACS 2024 paper obtains simultaneous subquadratic space and sublinear query overhead, with explicit output-sensitive tradeoffs.','gaps'),
  ('The 2026 3SUM-indexing improvements also affect string-indexing tradeoffs.','sum'),
  r'The curve fixes one reporting-time convention over its whole domain. It does not conflate start-position distance with the number of intervening characters, or existence queries with reporting.'],
 'A tight curve would reveal how reusable space substitutes for work in a general paired-pattern search primitive important in text analysis and biological motif queries.',
 ['gaps','sum'], [('2024','The first simultaneous subquadratic-space and sublinear-overhead index is established.','gaps'),('2026','Further indexing tradeoffs improve some parameter regimes.','sum')],
 ['Queries supply two patterns and an interval of allowed separation.','Every matching pair of positions must be reported.','The separation is measured between starting positions.','The target is the optimal storage exponent as a function of query-overhead exponent.','The benchmark requires certified accuracy throughout that function’s domain.'],
 qtype='function',criterion='tightness',answer=CURVE.replace('f(x)','s_{\mathrm{gap}}(x)'),score=88,status='uncertain',
 note='The proposal’s optimal tradeoff is formalized as an exponent curve under a stated reporting convention. The 0.01 curve target is editorial; the source bounds do not independently certify openness at that precision.')

card('P22', 'Polynomial-time construction of minimum-density DNA minimizers',
 r'Is there a uniform deterministic algorithm and a universal constant \(C\) that, for all integers \(k,w\ge2\), output a total order \(\rho\) on the \(4^k\) DNA k-mers minimizing expected minimizer density exactly, in \(O((4^k+w)^C)\) bit operations?',
 r'The fixed alphabet is \(\Sigma=\{A,C,G,T\}\). The input supplies \(k\) in binary and \(w\) in unary. The output lists every member of \(\Sigma^k\) once in order. For \(X\in\Sigma^{k+w}\), let \(p_0(X)\) be the smallest starting position in \(\{0,\ldots,w-1\}\) attaining the least k-mer under \(\rho\), and define \(p_1(X)\) in the same way over \(\{1,\ldots,w\}\). Define \(d(\rho)=4^{-(k+w)}|\{X:p_0(X)\ne p_1(X)\}|\). This is the expected sampling density on an independent uniform DNA sequence with leftmost tie-breaking. Optimality requires \(d(\rho)\le d(\pi)\) for every total order \(\pi\) on \(\Sigma^k\). Time is measured on a deterministic finite-tape Turing machine and includes all output bits and preprocessing. The same finite machine handles all \(k,w\), with no advice. The resource parameter is the explicit order-table size plus the unary window parameter; no claim of polynomial time in \(\log k+\log w\) is made.',
 [r'Minimizers keep one selected k-mer from each sliding window, often reusing the same position across neighboring windows. Lower sampling density reduces the number of retained seeds.',
  ('GreedyMini asks whether minimum-density minimizers can be generated efficiently.','mini'),
  ('OptMini already provides exact exponential search and resolves various small parameter families.','optmini'),
  r'The proposed target is efficient generation of a provably optimal order. Mere finite computability of the minimum density is already established and is not the question.'],
 'This asks whether optimal seed selection can be constructed with cost polynomial in its explicit representation, connecting a widely used sequencing primitive to a sharp computational barrier.',
 ['mini','optmini'], [('2025','GreedyMini obtains low-density orders and identifies efficient optimal generation as an open issue.','mini'),('2026-01-28','OptMini gives an exact algorithm exponential in the number of distinct k-mers.','optmini')],
 ['A minimizer chooses the least k-mer in each sliding window.','The density measures how often the chosen position changes on random DNA.','The desired output is an order with globally minimum density.','The running time must be polynomial in the explicit order-table size and window parameter.','Known exact exponential search does not meet that resource bound.'],
 criterion='construction',score=84,status='uncertain',note='The approved efficient-optimal-construction direction is fixed to DNA and explicit orders. This avoids a vacuous function-computability target already settled by exact exponential algorithms.')

card('P23', 'Almost-linear constant-factor approximation of LCS',
 r'Do there exist a universal constant \(C\ge1\) and a uniform randomized algorithm which, for every pair of explicit strings of total length \(n\ge2\) over \([0..n^2)\), returns a common subsequence of length at least \(\operatorname{LCS}(A,B)/C\) with probability at least \(2/3\), in \(n^{1+o(1)}\) worst-case time?',
 r'A subsequence is obtained by deleting zero or more symbols without changing the remaining order; \(\operatorname{LCS}(A,B)\) is the maximum possible length common to both strings. Empty strings are permitted. The algorithm outputs the subsequence explicitly and must always output a valid common subsequence; only the approximation guarantee may fail. Set \(L=n\). '+RAM+r' The same finite algorithm and approximation constant work for every input size. The runtime convention means that for every real \(\eta>0\) there exist \(K_\eta,n_\eta\) such that every random execution takes at most \(K_\eta n^{1+\eta}\) steps for every \(n\ge n_\eta\). The probability is over internal randomness on each fixed input. The alphabet grows with input length; a guarantee depending on alphabet size is not a universal constant approximation.',
 [r'Longest common subsequence measures similarity under deletions and is one of the central sequence-comparison tasks.',
  ('The 2026 comparison of LCS and LCStr describes a remaining approximation gap on growing alphabets.','lcs'),
  ('Recent deterministic near-linear algorithms give input-dependent approximation factors rather than the universal constant requested here.','lcs25'),
  r'A constant-alphabet guarantee does not decide the general-alphabet target. Almost-linear time here belongs to one algorithm, not a different algorithm for each fixed polynomial runtime slack.'],
 'A constant approximation in almost-linear time would make a central similarity measure usable at input scale while avoiding degradation on large alphabets.',
 ['lcs','lcs25','ed'], [('2025','A deterministic near-linear LCS approximation has a factor growing with input size.','lcs25'),('2026','New high-accuracy LCS schemes remain far from almost-linear time.','ed')],
 ['Longest common subsequence compares strings while allowing deletions.','The alphabet may grow with the input.','The requested approximation factor is one universal constant.','One randomized algorithm must have almost-linear worst-case running time.','Constant-alphabet approximations and slower high-accuracy schemes do not satisfy the combined target.'],
 score=91,note='The quantifiers distinguish one almost-linear randomized algorithm from fixed-slack families and from constant-alphabet approximations.')

card('P26', 'Linear-time unit-Monge distance multiplication',
 r'Is there a uniform deterministic \(O(n)\)-time algorithm which, given two permutations \(\pi,\tau\) of \(\{0,\ldots,n-1\}\), returns a permutation \(\rho\) satisfying \(A_\rho(i,j)=\min_{0\le h\le n}(A_\pi(i,h)+A_\tau(h,j))\) for all \(0\le i,j\le n\)?',
 r'For a permutation \(\nu\), define \(A_\nu(i,j)=|\{t:i\le t<n,\ \nu(t)<j\}|\). This counting matrix is the implicit simple unit-Monge representation used here. The input is the two permutation arrays, and the output is the array \(\rho\); no \((n+1)\)-by-\((n+1)\) matrix is supplied or requested explicitly. The product of two such matrices has a representation of this form. Set \(L=n\ge2\). '+RAM+r' Require \(O(n)\) working words, with all preprocessing charged. All bounds are worst-case with universal constants and no randomness.',
 [r'The matrices summarize many related sequence-comparison values using only a permutation-sized representation.',
  (r'Tiskin gives an \(O(n\log n)\) algorithm and explicitly attributes the linear-time question to Landau’s question about merging DIST tables.','monge'),
  ('The ESA 2025 extension to core-sparse Monge matrices retains the same unit-Monge time bound.','monge25'),
  r'The implicit input and output are essential: an explicitly written dense product alone requires quadratic output size.'],
 'This is a reusable algebraic primitive for semi-local alignment and compressed-string comparison, so a linear bound would affect more than a single query interface.',
 ['monge','monge25'], [('2010 / 2015',r'Tiskin establishes \(O(n\log n)\) time for implicit simple unit-Monge multiplication.','monge'),('2025','The core-sparse generalization matches, rather than improves, this bound in the unit case.','monge25')],
 ['The input consists of two permutations encoding structured distance matrices.','The output must encode their exact min-plus product.','All three representations have only linear size.','The question asks whether the computation can match that size in time.','The current general unit-Monge bound has a logarithmic overhead.'],
 area='Algebraic computation',criterion='resources',score=84,note='The counting-matrix convention makes Landau’s implicit-input question self-contained, including the representation of the answer.',category_note='The direct task is multiplication of structured matrices; sequence alignment is a major application.')

card('P29', 'Dense NFA Acceptance Hypothesis',
 r'Is it true that, for every constant \(\varepsilon>0\), no uniform bounded-error randomized word-RAM algorithm decides acceptance of length-\(n\) binary words by the dense n-state automata defined below in \(O(n^{3-\varepsilon})\) worst-case time?',
 r'An instance supplies \(n\ge2\), states \(Q=\{0,\ldots,n-1\}\), a start state \(q_0\), a set \(F\subseteq Q\) of accepting states, and a transition relation \(\Delta\subseteq Q\times\{0,1\}\times Q\). There are no empty-word transitions and no multiplicities. Require \(n^2\le|\Delta|\le2n^2\); the transition relation is given as two explicit Boolean adjacency matrices. The input word is \(x\in\{0,1\}^n\), supplied explicitly. Acceptance means that states \(q_0,q_1,\ldots,q_n\) exist with \((q_{i-1},x_i,q_i)\in\Delta\) and \(q_n\in F\). Set \(L=n\). '+RAM+r' Correctness probability is at least \(2/3\) for every fixed automaton and word. The bound includes reading the automaton, and all preprocessing; no preprocessed automaton is supplied. A finite program and constants may depend on fixed \(\varepsilon\), but not on an instance. Non-combinatorial algorithms are allowed.',
 [r'Automaton acceptance follows a prescribed label sequence through a graph of possible states. A dense transition relation has quadratically many potential transitions.',
  ('The NFA Acceptance framework proposes hardness beyond the combinatorial model and relates it to language reachability and dynamic lower bounds.','nfa'),
  ('Gørtz’s related work studies sparse regular-expression simulation; that is a research connection, not authorship of this hypothesis.','regex'),
  r'The card specifies the balanced dense binary regime. Sparse-automaton conditional lower bounds alone do not establish this statement.'],
 'This is a central unresolved barrier for general automata simulation with consequences across language processing and fine-grained complexity.',
 ['nfa','regex'], [('2024','The framework formulates the NFA Acceptance hypothesis and develops consequences beyond combinatorial algorithms.','nfa')],
 ['A binary word is checked against a nondeterministic finite automaton.','The number of transitions is quadratic in the number of states.','The word length equals the number of states.','The hypothesis excludes a fixed polynomial improvement over cubic time.','Both algebraic and randomized algorithms are included in the stated model.'],
 area='Fine-grained complexity',criterion='resources',score=90,note='This is the explicitly qualified balanced dense binary regime of the broader NFA hypothesis. The density and input-encoding conventions are part of the editorial formulation.',category_note='The main target is a fine-grained hardness hypothesis for all classical algorithms, with automata acceptance as the computational primitive.')

card('P30', 'Almost-quadratic unweighted tree edit distance',
 r'Is there a uniform deterministic algorithm computing the exact unit-cost edit distance between two rooted ordered labeled trees with a total of \(n\ge2\) vertices in \(n^{2+o(1)}\) worst-case time?',
 r'Trees are supplied by explicit ordered child lists and vertex labels in \([0..n^2)\). A fixed unlabelled super-root is attached above each input root; it may not be deleted or relabelled and is not counted in \(n\). Intermediate objects may be ordered forests below this super-root. Deleting a vertex replaces it in its parent’s ordered child list by its own ordered children. Inserting a vertex is the inverse operation, grouping a consecutive block of children, possibly empty, under one new vertex. Relabelling changes one ordinary vertex label. Each of these three operations costs one. The distance is the minimum total cost of a sequence transforming the first ordered labeled object into the second. The output is this single integer, not an edit script. Set \(L=n\). '+RAM+r' The same algorithm works for all inputs. The time condition means that for every \(\eta>0\), some constants \(K_\eta,n_\eta\) bound its time by \(K_\eta n^{2+\eta}\) whenever \(n\ge n_\eta\). All preprocessing is charged, and no randomness is permitted.',
 [r'Tree edit distance compares hierarchical structures while respecting the order of siblings. Paths give the string case, but branching adds structural interactions.',
  (r'The 2026 monotone-product paper records and derandomizes an upper bound \(n^{(3+\omega)/2+o(1)}\), already below cubic.','mono'),
  ('The ITCS 2026 dynamic-hardness paper distinguishes the still-unresolved static relative difficulty of strings and unweighted trees.','ted'),
  r'The target asks for almost-quadratic exact computation. It replaces the old first-truly-subcubic question, rather than continuing to mark that resolved threshold as open.'],
 'This would locate the cost of exact hierarchical sequence comparison relative to ordinary string edit distance and a broad family of structured dynamic programs.',
 ['mono','ted'], [('2026','Current bounds already beat cubic time; this card asks for the substantially stronger almost-quadratic target.','mono')],
 ['The inputs are rooted ordered trees with symbol labels.','Insertion, deletion and relabelling each have unit cost.','The task computes the exact minimum edit cost.','The proposed bound is almost quadratic in the total number of vertices.','The earlier question of obtaining any truly subcubic algorithm has already been surpassed.'],
 score=88,note='The near-quadratic endpoint is the user-approved replacement direction for TCS-5851. Weighted and dynamic variants have different barriers.')

card('P31', 'Fully functional suffix trees in BWT-run-linear space',
 r'Does there exist a uniform deterministic static representation of the compact suffix tree of every binary text with a terminal sentinel, using \(O(r)\) words and supporting every operation listed below in \(O((\log(n+2))^c)\) worst-case time for one fixed constant \(c\), where \(n\) is text length and \(r\) its number of BWT runs?',
 r'The input is \(T\in\{0,1\}^{n-1}\#\), with \(n\ge2\) and \(\#<0<1\). Its suffix tree is the trie of all nonempty suffixes with maximal nonbranching paths contracted; edge labels are nonempty substrings. Leaves are ordered by suffix lexicographic rank. The suffix array \(\operatorname{SA}[i]\) is the starting position of leaf rank \(i\), and \(\operatorname{ISA}\) its inverse. Define \(\operatorname{BWT}[i]=T[(\operatorname{SA}[i]-1)\bmod n]\); \(r\) counts maximal nonempty intervals of equal BWT symbols. A node is identified by its inclusive interval of descendant leaf ranks, two word-sized integers. Required operations return the root; parent; lexicographically first child; next sibling; child whose edge starts with a supplied symbol; edge-count depth; root-to-node string length; lowest common ancestor of two nodes; and, for a nonroot internal node with path label \(aU\), the suffix-link node with label \(U\). Also required are a leaf by rank, \(\operatorname{SA}\), \(\operatorname{ISA}\), and \(T[i]\). Missing parents, children and siblings return a distinguished marker. Set \(L=n\). '+RAM+r' All text, samples, handles retained internally, and temporary query work count toward space. Externally supplied or returned node handles have constant word size. Construction takes polynomial time in \(n\), including all tables. The terminal sentinel is unique and included in \(n\) and \(r\).',
 [r'Highly repetitive collections can have few BWT runs even when the expanded text is enormous. A full suffix-tree interface supports navigation as well as pattern search.',
  ('The foundational r-index work obtains richer suffix-tree structures with an additional logarithmic space factor.','rindex'),
  ('Later non-overlapping-indexing work discusses the unresolved run-linear full suffix-tree representation.','rtree'),
  r'The interface here is enumerated explicitly. A run-linear counting or locating index alone does not supply all required tree and text operations.'],
 'This asks whether an entire general navigation structure can be retained at the scale of repetitive input, rather than supporting only a single search operation.',
 ['rindex','rtree'], [('2017 / 2024','The cited structures and later application retain a gap between BWT-run-linear search space and the richer suffix-tree interface.','rtree')],
 ['Repetitive texts can have few runs in their Burrows–Wheeler transform.','The target stores a complete suffix-tree navigation interface in space proportional to that run count.','Tree nodes are represented by their intervals of descendant suffixes.','All specified navigation and text-access queries must take polylogarithmic time.','Run-linear pattern search alone does not meet the full interface.'],
 score=79,status='uncertain',note='The binary alphabet and enumerated interface are explicit editorial specializations. This is not an automatic restoration of the previously removed character-access-only topic.')

REALRAM = r'Use an algebraic real RAM with exact real addition, subtraction, multiplication, division by a nonzero real, and comparisons, each at unit cost. A point coordinate, scalar, pointer or fixed-size record field occupies one cell. Reading, writing and following pointers cost one step; no floor, bit extraction from reals, or packing unbounded discrete information into a real is an available operation. The program is uniform and finite; there is no advice or free table construction. Independent random bits are permitted when explicitly stated.'

card('P05', 'Logarithmic fully dynamic planar nearest neighbors',
 r'Does a uniform Las Vegas data structure maintain a finite set of planar points under insertions and deletions, answer exact Euclidean nearest-neighbor queries in \(O(\log(n+2))\) worst-case time, and support updates in expected amortized \(O(\log(n+2))\) time, using \(O((n+1)\log^c(n+2))\) space for some fixed constant \(c\)?',
 r'The structure starts empty. An insertion supplies a real point not currently present and returns a stable handle. A deletion supplies the handle of a present point. A query supplies \(q\in\mathbb R^2\) and returns any present \(p\) minimizing \((p_x-q_x)^2+(p_y-q_y)^2\), or an empty marker. Ties may be resolved arbitrarily but correctly. At any instant \(n\) is the number of stored points. '+REALRAM+r' All answers are exact on every terminating execution and the structure terminates almost surely. For every fixed finite legal operation sequence chosen independently of its random bits, with \(u\) updates and maximum set size \(M\), the expected total update time is \(O(u\log(M+2))\); each query separately has worst-case \(O(\log(n+2))\) time on every execution. Space holds on every execution, including retained points and temporary work. All constants are universal. This states the amortization convention using the maximum size of the sequence, without an adaptive-adversary guarantee.',
 [r'Balanced search trees give a logarithmic nearest-neighbor interface on the line. The planar version must also maintain changing geometric proximity information.',
  ('The original problem asks for logarithmic insertion, deletion and exact query costs.','nnold'),
  ('Iacono and Nekrich obtain logarithmic queries and near-logarithmic insertions in an incremental structure.','nn'),
  r'This formulation permits expected amortized update costs, while retaining exact answers, worst-case queries and deletions.'],
 'A logarithmic fully dynamic structure would establish the natural two-dimensional counterpart of a basic ordered-search interface.',
 ['nnold','nn'], [('2025','The incremental result supports optimal queries, but does not include deletions or prove the full logarithmic-update target.','nn')],
 ['The structure maintains points in the Euclidean plane.','Queries ask for an exact nearest stored point.','Points can both enter and leave the set.','Queries must be worst-case logarithmic and updates logarithmic in expected amortized cost.','The recent incremental result does not meet the full dynamic target.'],
 area='Dynamic graph algorithms',score=86,note='The earlier topic label is developed with an algebraic real-RAM model, oblivious operation sequences, Las Vegas correctness and an explicit expected-amortized update convention.',category_note='The primary interface maintains a geometric solution under insertions and deletions.')

card('P10', 'Space-query exponent curve of 3SUM indexing',
 r'Determine \(\tau_{\mathrm{3SI}}(s)\) for every real \(s\in[1,2]\), where \(\tau_{\mathrm{3SI}}(s)\) is the infimum of real \(t\ge0\) for which, for every rational \(\eta>0\), a uniform randomized 3SUM index uses \(O(n^{s+\eta})\) words and answers queries in \(O(n^{t+\eta})\) worst-case time.',
 r'The input is two sets \(A,B\subseteq\{0,\ldots,n^4-1\}\), each of size \(n\ge2\), supplied explicitly. A query \(z\in\{0,\ldots,2n^4-2\}\) asks whether \(z=a+b\) for some \(a\in A,b\in B\), using ordinary addition. Set \(L=n\) and fix \(d=10\) in the word-RAM model below. '+RAM+r' Preprocessing may take arbitrary time but must terminate almost surely; this preserves the preexisting card’s space-hardness convention. Every retained input, table and random seed is counted. Each fixed input/query is answered correctly with probability at least \(2/3\) over preprocessing and query randomness, and space and query time bounds hold on every random outcome. Queries cannot communicate input-dependent state for free. For each chosen \(s,t,\eta\), one finite program pair and constants handle every \(n\); there is no per-size choice of advice. Parameters select programs and are not real-number computational inputs. The infimum need not be attained. The quantity is a dimensionless query exponent, and it ignores subpolynomial factors only through the displayed quantifiers.',
 [r'An index is built once for all future sum-membership queries. Storing every potential sum and scanning one input set occupy very different points of the space-query frontier.',
  ('The original framework separates different 3SUM-indexing hardness hypotheses; its strongest old tradeoff should not be treated as a theorem.','sets'),
  ('The revised 2026 paper improves intermediate space regimes without determining the entire frontier.','sum'),
  r'The previous card asked specifically for genuinely subquadratic space with polylogarithmic queries. The present curve broadens the target; a query exponent of zero or a numerical approximation to it does not by itself establish a polylogarithmic bound.'],
 'The curve asks how much information about a quadratic family of sums must be stored to support reusable membership queries, a general representation barrier underlying several string indexes.',
 ['sets','sum'], [('2017','The space-hardness framework distinguishes weak and strong 3SUM-indexing conjectures.','sets'),('2026-04-23','The revised work improves the tradeoff in intermediate space regimes.','sum')],
 ['Two integer sets are stored before membership queries arrive.','A query asks whether its number belongs to their sumset.','The target is the best query exponent at each allowed storage exponent.','All retained information is charged even though preprocessing time is unrestricted.','The numerical curve target is broader than the saved polylogarithmic-query existence question.'],
 area='Data structures',criterion='tightness',qtype='function',answer=CURVE.replace('f(x)',r'\tau_{\mathrm{3SI}}(x)'),score=88,status='uncertain',
 note='User-approved consolidation broadens TCS-7333 from its binary polylogarithmic-query endpoint to the underlying exponent curve. Its old statement is preserved in formulation history. Unrestricted preprocessing and the polynomial universe are retained; 0.01 accuracy does not decide every exact endpoint.',category_note='The main quantity is a static data-structure space-query frontier, rather than the cost of one 3SUM computation.')

card('P13', 'Near-quadratic Voronoi complexity of lines in three dimensions',
 r'For every real \(\varepsilon>0\), does there exist \(C_\varepsilon\) such that every regular Euclidean Voronoi diagram of \(n\ge2\) distinct affine lines in \(\mathbb R^3\), as defined below, has at most \(C_\varepsilon n^{2+\varepsilon}\) cells in total?',
 r'A line is the set \(\ell_i=\{p_i+tv_i:t\in\mathbb R\}\), where \(p_i,v_i\in\mathbb R^3\) and \(v_i\ne0\). Distances are ordinary Euclidean point-to-line distances. For every nonempty \(I\subseteq\{1,\ldots,n\}\), define \(V_I\) to be the set of points whose set of nearest lines is exactly \(\{\ell_i:i\in I\}\). Regular means that \(V_I\) is empty for \(|I|>4\), and for \(1\le|I|\le4\) each nonempty \(V_I\) is a smooth embedded manifold of dimension \(4-|I|\). The cells counted are the connected components of every nonempty \(V_I\), including unbounded components and zero-dimensional components. Let \(b_0(V_I)\) be the number of such components, with \(b_0(\varnothing)=0\); total complexity is \(\sum_{\varnothing\ne I\subseteq[n]}b_0(V_I)\). These semialgebraic sets have finitely many connected components. The statement is an extremal mathematical bound; no bit encoding or construction algorithm for real coordinates is required. The constants depend only on \(\varepsilon\), not on the lines or their coordinates.',
 [r'Voronoi diagrams encode which objects are closest to each point in space. Their combinatorial size constrains geometric proximity structures and algorithms.',
  ('The source records a quadratic lower bound, an essentially cubic upper bound and the near-quadratic conjecture for Euclidean lines.','voronoi'),
  r'The regularity definition spells out the nondegenerate diagram convention. Counts for a polyhedral distance function or a fixed distance level set concern different geometric objects.'],
 'This is a central unresolved complexity gap for a fundamental three-dimensional proximity structure, closely connected to lower-envelope and arrangement bounds.',
 ['voronoi'], [('2001','The problem source records the near-quadratic conjecture and the gap to the known general upper bound.','voronoi')],
 ['Each point in three-dimensional space has a set of nearest input lines.','Connected regions with the same nearest-line set form the diagram’s cells.','The question counts cells of all dimensions.','The proposed bound is arbitrarily close to quadratic.','The Euclidean metric and the specified nondegeneracy convention are essential parts of this formulation.'],
 area=GEOMETRY,criterion='tightness',score=88,status='uncertain',note='The saved topic is developed as the near-quadratic conjecture on explicitly defined regular diagrams. The old source supports the frontier, but the present bounded search is not an independent current-status certification of this precise stratification convention.',category_note='The target is the combinatorial size of a Euclidean geometric decomposition.')

card('P15', 'Dürer’s conjecture',
 r'For every bounded three-dimensional convex polytope \(P\subset\mathbb R^3\) with nonempty interior, is there a connected edge unfolding whose distinct face interiors do not overlap in the plane?',
 r'A convex polytope is the convex hull of a finite set of real points. Its faces here are its maximal two-dimensional facets, and adjacent facets share an entire polytope edge. Choose a spanning tree of the facet adjacency graph. Make separate copies of all facets and glue only the pairs of matching edges selected by that tree, retaining the edge identifications inherited from \(P\). An edge unfolding is a map of this glued polygonal surface to \(\mathbb R^2\) whose restriction to each copied facet is a Euclidean isometry and whose restrictions agree on glued edges. Require images of the relative interiors of distinct facets to be disjoint. Contacts between boundary points are permitted; cuts may run only along original polytope edges. The glued surface and its image are connected. This is a geometric existence statement with arbitrary real coordinates, not an algorithmic runtime claim.',
 [r'An edge unfolding is a flat net assembled from the original polygonal faces. Convexity limits the input but does not specify which edges can be kept joined.',
  ('The classical open question asks whether every convex polyhedron admits an edge unfolding without overlap.','durer'),
  r'Cuts through face interiors, separate disconnected pieces and nonconvex input polyhedra change the mathematical question. The present definition allows boundary contacts while excluding overlapping face interiors.'],
 'This long-standing question asks whether every convex three-dimensional shape has an edge-based planar net, a basic unresolved principle in geometric folding and representation.',
 ['durer'], [('2001','The problem source records the general convex edge-unfolding question as open and distinguishes known nonconvex obstructions.','durer')],
 ['The input is a convex three-dimensional polytope.','Its faces may be separated only along original edges.','The output sought is one connected planar net.','Distinct face interiors must not overlap.','Allowing cuts across faces or disconnected pieces gives a different problem.'],
 area=GEOMETRY,criterion='construction',score=93,note='The inherited topic label is developed with explicit facet gluing and nonoverlap conventions. Boundary contacts are allowed; no runtime or coordinate-size requirement is imposed.',category_note='This is geometric existence and unfolding of convex polyhedral surfaces.')

card('P16', 'Linear-size universal point sets for planar graphs',
 r'Does there exist a universal constant \(C\) such that for every integer \(n\ge1\) one can choose at most \(Cn\) distinct points in \(\mathbb R^2\) supporting a crossing-free straight-line drawing of every simple planar graph on \(n\) vertices?',
 r'The point set \(U_n\) is chosen as a function of \(n\) before the graph is supplied. For each finite simple undirected planar graph \(G\) with vertex set \([n]\), there must be an injective map \(\phi:V(G)\to U_n\). Every edge is drawn as the closed line segment between its endpoint images. Two edge segments may intersect only at the image of a shared endpoint, and the relative interior of an edge may contain no vertex image. Unused points in \(U_n\) are allowed. The injection may depend on \(G\); the same prescribed correspondence of labels to points is not required. The graph need not have a prescribed planar embedding. Coordinates are arbitrary reals, and no grid-size, computability or runtime constraint is imposed. A planar graph means one admitting a plane embedding by arcs with these same incidence and nonintersection requirements.',
 [r'Every individual planar graph can be drawn with straight edges, but a universal point set must work before it is known which graph will be drawn.',
  ('The original problem asks for the smallest size of such a set.','pointsold'),
  ('Felsner and coauthors construct linear-size sets for subclasses, while the unrestricted planar case remains the general target.','points'),
  r'The assignment of vertices to points is allowed to vary with the graph. Fixing the assignment in advance would impose a different and much stronger condition.'],
 'This asks whether a linear geometric host can represent all planar combinatorial structures of a given size, rather than dedicating a separate layout to each graph.',
 ['pointsold','points'], [('2023','Linear-size constructions for restricted planar graph classes do not establish a universal linear bound for all planar graphs.','points')],
 ['One point set is selected for each graph size.','Every planar graph of that size must have a straight-line drawing using some of those points.','Vertex assignments may depend on the graph.','The question asks whether only linearly many points suffice.','Results for subclasses do not settle the universal requirement.'],
 area=GEOMETRY,criterion='construction',score=85,note='The approved linear-size existence threshold is made explicit, with unrestricted real coordinates and graph-dependent vertex placement.',category_note='The target concerns geometric hosts for graph drawings, rather than a graph decision algorithm.')

card('P24', 'Optimal exact-distance label length for planar graphs',
 r'Determine the asymptotic growth of \(\ell_{\mathrm{planar}}(n)\) up to universal constant factors, where \(\ell_{\mathrm{planar}}(n)\) is the least integer \(b\ge0\) permitting labels of \(b\) bits that determine every pairwise distance in every connected unweighted simple planar graph on \(n\ge2\) vertices using only the two labels.',
 r'For fixed \(n,b\), a permitted decoder is a function \(D:\{0,1\}^b\times\{0,1\}^b\to\{0,\ldots,n-1\}\). The same \(D\) must work for every connected unweighted simple undirected planar graph \(G\) with vertex set \([n]\): there must be a label assignment \(\lambda_G:[n]\to\{0,1\}^b\) such that \(D(\lambda_G(u),\lambda_G(v))=\operatorname{dist}_G(u,v)\) for all vertices, where distance counts edges on a shortest path. The decoder may depend on \(n\) and \(b\), but not on \(G\), and receives no shared graph data, vertex identifiers or additional input. Both the decoder domain and graph class are finite for fixed \(n,b\); no efficiency bound is imposed on constructing labels or decoding. The target measures label information alone, with arbitrary values on label pairs never used by an assignment. Known efficient schemes provide upper bounds in this unrestricted model as well.',
 [r'Distance labels distribute a graph metric among vertices. Two labels must suffice even when the original graph is unavailable.',
  (r'Gawrychowski and Uznański give an \(O(\sqrt n)\)-bit upper bound against the known \(\Omega(n^{1/3})\) lower bound for unweighted planar graphs.','labels'),
  r'The question concerns exact labels, not approximate distances or an oracle that can also inspect a shared data structure. The unrestricted decoder convention isolates representation size.'],
 'Closing this polynomial gap would identify the information needed to distribute an entire planar graph metric into independent vertex labels.',
 ['labels'], [('2021 / 2023',r'The improved scheme removes a logarithmic factor from the previous upper bound, leaving the exponent gap between \(n^{1/3}\) and \(n^{1/2}\).','labels')],
 ['Each vertex receives a short binary label.','The exact distance between two vertices must follow from their labels alone.','The same decoder serves every graph of the chosen size.','The target is the optimal asymptotic number of label bits.','Current lower and upper bounds differ by a polynomial factor.'],
 area='Structural graph theory',criterion='tightness',qtype='asymptotic_complexity',score=88,
 answer=r'Supply a specified asymptotic rate \(f(n)>0\) and a complete Lean-checked proof of constants \(c,C>0\), \(n_0\), such that \(cf(n)\le\ell_{\mathrm{planar}}(n)\le Cf(n)\) for all \(n\ge n_0\). Both bounds must use the same unrestricted exact-decoder model. Merely renaming the defining optimum, a one-sided improvement, or conditional hardness without its assumption proved does not meet this target. The accuracy requirement is constant-factor asymptotic matching, not an additive 0.01 error on big-O notation.',
 note='The old topic label is developed as an information-theoretic label-size question. The exact decoder quantifiers are explicit; graph-specific shared storage is excluded.',category_note='The defining input restriction and target are a structural representation of planar graph distances.')

card('P32', 'Breaking two for sum-of-pairs multiple sequence alignment',
 r'Does there exist a rational constant \(\varepsilon\in(0,1)\) and a uniform deterministic polynomial-time algorithm that returns a \((2-\varepsilon)\)-approximation for minimum sum-of-pairs alignment of any number of strings under an input metric substitution-and-gap cost?',
 r'An instance gives \(k\ge2\) explicit strings over a finite alphabet \(\Sigma\), and a table \(d:(\Sigma\cup\{-\})^2\to\mathbb Q_{\ge0}\) encoded by binary numerators and denominators. The distinguished gap symbol \(-\) is not an input-string symbol. Promise \(d(a,b)=d(b,a)\), \(d(a,b)=0\) exactly when \(a=b\), and the triangle inequality for all alphabet and gap symbols. An alignment is a \(k\)-row array of equal-length strings over \(\Sigma\cup\{-\}\) such that erasing gaps from each row returns its input string, and no column consists entirely of gaps. The cost is \(\sum_{1\le i<j\le k}\sum_c d(A_{i,c},A_{j,c})\). The minimum is over all such alignments. Empty input strings are allowed, and the all-empty instance has the empty alignment and zero optimum. The output is an explicit feasible alignment with cost at most \((2-\varepsilon)\) times optimum. Time is measured on a deterministic finite-tape Turing machine in the total bit length of the explicit strings and metric table. The constant, finite program and polynomial are independent of \(k\), the alphabet, lengths and costs.',
 [r'Multiple alignment compares many sequences simultaneously, with a sum of pairwise costs accumulated column by column.',
  ('The source questions ask whether a fixed improvement below two is possible for an arbitrary number of sequences.','msaopen'),
  ('Known guarantees that approach two as the number of sequences grows are different from a universal constant improvement.','msa'),
  r'The model fixes metric substitution and gap costs. It does not substitute a column-scoring objective, fixed-number-of-strings algorithm or local alignment.'],
 'This is a principal approximation barrier for a basic bioinformatics optimization problem, requiring an improvement that survives as the number of sequences grows.',
 ['msaopen','msa'], [('2000','The open-problem article poses the general multiple-alignment approximation barrier.','msaopen')],
 ['The inputs are an arbitrary number of sequences and a metric cost table.','An alignment inserts gaps while preserving each sequence.','Its objective sums costs over every pair of rows and every column.','The question asks for a polynomial-time approximation below two by a fixed constant.','An improvement shrinking with the number of sequences does not meet the target.'],
 criterion='tightness',score=92,note='The inherited source record is developed with an explicit rational metric, feasible alignment representation and a constant approximation improvement independent of the number of strings.')

def prepare():
    # Complete the bibliography from the primary pages read during this import.
    R['er25']['title'] = r'Some structural complexity results for \(\exists\mathbb R\)'
    R['mini']['authors'] = 'Shay Golan; Ido Tziony; Matan Kraus; Yaron Orenstein; Arseny Shur'
    R['lcs']['authors'] = 'Shay Golan; Matan Kraus; Ely Porat; B. Riva Shalom'
    R['lcs25']['title'] = 'Deterministic Longest Common Subsequence Approximation in Near-Linear Time'
    R['rtree']['authors'] = 'Daniel Gibney; Paul Macnichol; Sharma V. Thankachan'
    R['ted']['authors'] = 'Bingbing Hu; Jakob Nogler; Barna Saha'
    R['msa']['title'] = 'Efficient Methods for Multiple Sequence Alignment with Guaranteed Error Bounds'
    R['msa']['authors'] = 'Francis Y. L. Chin; S. M. Yiu'
    R['msa']['year'] = None  # The supplied encyclopedia manuscript is undated.
    R['msaopen']['authors'] = 'Tao Jiang; Paul Kearney; Ming Li'
    R['msaopen']['year'] = 2000
    R['points']['title'] = 'Linear Size Universal Point Sets for Classes of Planar Graphs'
    CARDS['P29']['title'] = 'Balanced dense NFA Acceptance Hypothesis'
    CARDS['P32']['year'] = 2000
    # The metadata is additive and does not overwrite other author-list imports.
    all_pids = sorted({p for _, ps in ASSIGNMENTS for p in ps})
    assert len(all_pids) == 32 and sum(len(ps) for _, ps in ASSIGNMENTS) == 45
    assert set(CARDS) | set(EXISTING) == set(all_pids)
    before, plans = {}, []
    for pid in all_pids:
        authors = [name for name, ps in ASSIGNMENTS if pid in ps]
        association = dict(batch=BATCH, proposal_id=pid, researchers=authors,
            association_note='Editorial research connections selected in the user-approved proposal; not claims of exclusive authorship, endorsement or personal priorities.',
            proposal='research/author-problems-20260913/proposal.md', approved_on=DATE)
        if pid in EXISTING:
            identifier = EXISTING[pid]
            path = ROOT/'data/cards'/f'{identifier}.json'
            old = json.loads(path.read_text())
            before[identifier] = old
            patch = dict(CARDS.get(pid, {}))
            patch.pop('key',None)
            # Preserve prior editorial scores for already assessed cards.
            if old.get('importance',{}).get('method')=='editorial':
                patch.pop('importance',None)
            # Keep the original category unless the card is explicitly reclassified.
            if patch:
                patch['area'] = old['area']
            if pid=='P09':
                patch['answer_criterion'] = 'Give a complete Lean-checked proof of the stated universal space-query lower bound or its logical negation, with the same model and quantifiers. Assuming the conjecture to derive another lower bound is not a proof of the conjecture.'
            plans.append(dict(proposal_id=pid, existing_id=identifier, patch=patch, association=association))
        else:
            new = dict(CARDS[pid])
            new['author_problem_imports'] = [association]
            if pid=='P30':
                new['replaces_resolved_card'] = 'TCS-5851'
                new['source_consolidations'] = [dict(id='TCS-5851',reason='The first-truly-subcubic target is resolved; the user approved a new almost-quadratic target, with a separate active identity and lossless archival of the old record.')]
            plans.append(dict(proposal_id=pid, new_card=new, association=association))
    (HERE/'before.json').write_text(json.dumps(before,ensure_ascii=False,indent=2)+'\n')
    (HERE/'import-plan.json').write_text(json.dumps(dict(batch=BATCH,assignments=ASSIGNMENTS,plans=plans),ensure_ascii=False,indent=2)+'\n')
    (HERE/'new-cards.json').write_text(json.dumps([p['new_card'] for p in plans if 'new_card' in p],ensure_ascii=False,indent=2)+'\n')
    print(json.dumps(dict(new=sum('new_card' in p for p in plans),existing=sum('existing_id' in p for p in plans),detailed=len(CARDS),assignments=45)))

if __name__=='__main__':
    prepare()
