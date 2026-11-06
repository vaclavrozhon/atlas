"""Finite numerical exponents, with absolute 0.01 acceptance."""

d=original('0318')
quantities=d['formal'].split('Determine a positive real-valued function')[0]
defs=d['definitions']
a=defs.index('The domain of \\(F\\)')
b=defs.index('Complementing subsets')
defs=defs[:a]+defs[b:]
defs+=r' The requested exponent is \[x_{\mathrm{kset}}=\inf\{a\in\mathbb R_{\ge0}:\exists C>0\ \forall n\ge2\ \forall 1\le k\le\lfloor n/2\rfloor,\ K_2(n,k)\le C n(k+1)^a\}.\] The integer parameter domain is the same as above. The coefficient \(C\) may depend on \(a\), but not on either parameter or the point configuration. The cited upper bound ensures \(0\le x_{\mathrm{kset}}\le1/3\). The infimum need not be attained. Thus a value zero permits subpolynomial dependence on \(k\) and does not assert a linear bound \(O(n)\). This records the exponent of the dependence on subset size after factoring out the linear dependence on the number of points; it does not assert a two-sided power-law asymptotic.'
revise('0318', 'Planar k-set growth exponent',
       r'Determine to absolute error at most \(1/100\) the exponent \[x_{\mathrm{kset}}=\inf\{a\ge0:\exists C>0\ \forall n\ge2\ \forall 1\le k\le\lfloor n/2\rfloor,\ K_2(n,k)\le Cn(k+1)^a\}.\] Here \(K_2(n,k)\) is the largest number of distinct \(k\)-point subsets strictly separable by a line in an \(n\)-point planar set with no three collinear points. Its full definition is below. The bound must be uniform in both integer parameters. Logarithmic factors and exact extremal counts are not requested.',
       'Replaced the full two-parameter constant-factor function by the finite uniform k-dependence exponent, following the owner’s Excluded Grid precision rule.',
       ['A planar k-set is a k-point subset that a line strictly separates from the remaining points.', 'The point set has no three collinear points and otherwise arbitrary real coordinates.', 'The card asks for the exponent of k after factoring out the linear number-of-points term.', 'The exponent must be located within absolute error 0.01 using bounds uniform in both parameters.', 'Exact counts and growing logarithmic factors are not part of the answer.'],
       definitions=quantities+'\n\n'+defs, kind='numerical_value',
       criterion=exponent_criterion(r'\(a_*\)'),
       context={6:'The 2024 halving-line paper improves lower-order and finite-size terms while retaining the leading four-thirds upper power in the balanced case. Such lower-order changes do not themselves determine the uniform exponent selected here.'},
       refs=['https://topp.openproblem.net/p7'])

d=original('6526')
defs=d['definitions']+r' For each fixed integer \(d\ge2\), define \[x_{\mathrm{net}}(d)=\inf\{a\ge0:\exists C>0\ \exists\varepsilon_0\in(0,1/2]\ \forall\varepsilon\in(0,\varepsilon_0],\ f_d(\varepsilon)\le C\varepsilon^{-a}\}.\] Constants may depend on \(d\) and \(a\), but not on the accuracy or point set. The classical polynomial upper bound and inverse-accuracy lower bound give \(1\le x_{\mathrm{net}}(d)\le d\), so every requested value is a finite real number. The infimum need not be attained; a polylogarithmic factor in \(1/\varepsilon\) does not change the exponent. Different fixed dimensions may use different constants, with no uniform bound on their growth requested.'
revise('6526', r'Weak \(\varepsilon\)-net size exponent',
       r'For every fixed integer \(d\ge2\), determine to absolute error at most \(1/100\) the exponent \[x_{\mathrm{net}}(d)=\inf\{a\ge0:f_d(\varepsilon)=O_d(\varepsilon^{-a})\text{ as }\varepsilon\downarrow0\}.\] The function \(f_d(\varepsilon)\), defined below, is the worst-case minimum cardinality of a weak \(\varepsilon\)-net hitting all convex sets that contain at least an \(\varepsilon\) fraction of a finite point set in \(\mathbb R^d\). Net points may lie outside the input set. The requested answer concerns the exponent, with no requirement to determine logarithmic factors.',
       'Replaced exact asymptotic cardinality by the finite exponent in inverse accuracy for each fixed dimension; retained all convex ranges and auxiliary net points.',
       ['A weak epsilon-net hits every convex set containing a sufficiently large fraction of the input points.', 'Its chosen points may lie anywhere in Euclidean space.', 'The question asks how the worst-case net size grows as a power of inverse accuracy.', 'The exponent is requested to absolute error 0.01 in every fixed dimension.', 'The target imposes no algorithmic construction requirement and ignores logarithmic factors.'],
       definitions=defs, kind='function', criterion=exponent_criterion(r'\(a(d)\)',r' for every integer \(d\ge2\)'),
       context={0:'The source asks for the true asymptotic behavior of weak-net size in every fixed dimension. The owner’s numerical-target rule selects its polynomial exponent in inverse accuracy, rather than matching the entire function within constant factors.'},
       refs=['https://arxiv.org/abs/1808.02686','https://arxiv.org/abs/0812.5039'])

d=original('6710')
defs=d['definitions']
a=defs.index('The lower-bound part must apply')
defs=defs[:a]+r'For each fixed integer \(k\ge2\), define \[x_{\mathrm{NOF}}(k)=\inf\{a\in\mathbb R_{\ge0}:\exists C>0\ \exists n_0\ge1\ \forall n\ge n_0,\ R(n,k)\le Cn^a\}.\] The constant and threshold may depend on \(k\) and \(a\). The elementary bounds above ensure \(0\le x_{\mathrm{NOF}}(k)\le1\). The infimum need not be attained. The target does not require matching logarithmic factors, a uniform constant as \(k\) grows with \(n\), or a single protocol generator. Lower bounds must apply to all permitted randomized interactive protocols.'
revise('6710', 'Fixed-player number-on-forehead disjointness exponent',
       r'For every fixed integer \(k\ge2\), determine to absolute error at most \(1/100\) the communication exponent \[x_{\mathrm{NOF}}(k)=\inf\{a\ge0:R(n,k)=O_k(n^a)\text{ as }n\to\infty\}.\] Here \(R(n,k)\) is the minimum worst-case public-coin randomized communication for deciding whether \(k\) subsets of \([n]\) have empty common intersection, with error at most \(1/3\); player \(i\) sees every set except the \(i\)-th. The full interactive broadcast model and asymptotic quantifiers are below.',
       'Selected the finite n-growth exponent at each fixed player count, rather than exact logarithmic factors and joint growing-player asymptotics. The change in precision and fixed-parameter interpretation is explicit.',
       ['In number-on-forehead communication, each player sees every input set except its own.', 'The task is to decide whether all sets have empty common intersection.', 'The card asks for the polynomial exponent of randomized communication in the universe size.', 'Each fixed number of players has its own exponent, to absolute accuracy 0.01.', 'Local computation is free and arbitrary interactive public broadcasts are allowed.'],
       definitions=defs, kind='function', criterion=exponent_criterion(r'\(a(k)\)',r' for every integer \(k\ge2\)'),
       context={4:'The numerical target keeps each fixed player count but no longer asks for a sharp bound uniform when the number of players grows with the universe. It determines polynomial exponents only; logarithmic factors and player-dependent multiplicative constants are outside its acceptance criterion.'},
       refs=['https://yehudayoff.net.technion.ac.il/files/2016/03/book.pdf','https://eccc.weizmann.ac.il/report/2013/005/'])

d=original('6785')
defs=d['definitions']
a=defs.index('A result up to constant factors supplies')
b=defs.index('This measures optimal structural')
defs=defs[:a]+defs[b:]
defs+=r' Define the exponent \[x_{\mathrm{span}}(c)=\inf\{a\ge0:\exists C>0\ \exists n_0\ge1\ \forall n\ge n_0,\ A_c(n)+1\le Cn^a\}.\] For each fixed real \(c\ge1\), the constants may depend on \(c\) and \(a\), but not on the graph or \(n\). Adding one removes zero-value conventions without changing any positive power of growth. A spanning forest has finite distances at most \(n-1\) within its components, so \(0\le x_{\mathrm{span}}(c)\le1\). The infimum need not be attained; no ordinary logarithmic-growth limit is assumed. In particular, exponent zero permits polylogarithmic or other subpolynomial error and does not promise bounded error.'
revise('6785', 'Additive-error exponent of linear-size spanners',
       r'For every fixed real edge-budget coefficient \(c\ge1\), determine to absolute error at most \(1/100\) the exponent \[x_{\mathrm{span}}(c)=\inf\{a\ge0:A_c(n)+1=O_c(n^a)\text{ as }n\to\infty\}.\] Here \(A_c(n)\), defined below, is the largest, over simple undirected unweighted \(n\)-vertex graphs, minimum additive all-pairs distance error of a spanning subgraph with at most \(\lfloor cn\rfloor\) edges and the same connected components. The edge budget is genuinely linear; no hidden logarithmic factor in the budget is allowed.',
       'Replaced the full additive-error function by a finite exponent for each existing fixed edge-budget coefficient; did not pick an arbitrary power threshold or relax the linear edge budget.',
       ['A sparse subgraph can increase distances even when all connected components are preserved.', 'The card fixes a constant multiple of the vertex count as the edge budget.', 'It asks for the exponent of the smallest worst-case additive distance error.', 'Every fixed budget coefficient has an answer to absolute accuracy 0.01.', 'New edges and hidden logarithmic increases in the edge budget are not allowed.'],
       definitions=defs, kind='function', criterion=exponent_criterion(r'\(a(c)\)',r' for every real \(c\ge1\)'),
       refs=['https://arxiv.org/abs/1909.03152','https://arxiv.org/abs/2207.11832'])

d=original('7184')
defs=d['definitions'].replace(r'\(B_{i}=\prod _{j=1}^{d} [a_{i},j,b_{i},j]\)',r'\(B_i=\prod_{j=1}^d[a_{ij},b_{ij}]\)').replace(r'\(a_{i},j\le b_{i},j\)',r'\(a_{ij}\le b_{ij}\)').replace(r'∪_\(i B_{i}\)',r'\(\bigcup_i B_i\)')
defs=defs.replace(r'The requested precision is a \(\Theta\) bound: logarithmic factors count, and constants may depend on d. ', '')
defs+=r' For a correct uniform deterministic program \(A\) in fixed dimension \(d\), let \(t_{A,d}(n)\) be its worst-case time on \(n\) boxes. Define \[x_{\mathrm{Klee}}(d)=\inf\{a\ge0:\exists A\ \exists C>0\ \exists n_0\ge1\ \forall n\ge n_0,\ t_{A,d}(n)\le Cn^a\}.\] A different uniform program may be selected for each fixed dimension and each exponent bound, but not for each input length. Elementary input access and the cited algorithm give \(1\le x_{\mathrm{Klee}}(d)\le d/2\). The infimum need not be attained; in particular a value does not prescribe matching logarithmic factors. A lower bound must concern every permitted exact program, without an unproved complexity assumption.'
revise('7184', 'Klee’s measure running-time exponent',
       r'For each fixed integer \(d\ge3\), determine to absolute error at most \(1/100\) the optimal deterministic running-time exponent \[x_{\mathrm{Klee}}(d)=\inf\{a\ge0:\text{some uniform exact algorithm has worst-case time }O_d(n^a)\}.\] The task is to compute the exact \(d\)-dimensional volume of the union of \(n\) explicitly given axis-aligned boxes in the real-RAM model below. Programs and constants may depend on fixed \(d\), but not on the coordinates or input size. Logarithmic factors in running time are not part of the numerical answer.',
       'Replaced full constant-factor running time by the finite optimal exponent in every existing fixed dimension; retained exact deterministic real-RAM computation.',
       ['Klee’s measure problem computes the volume covered by a union of axis-aligned boxes.', 'Overlaps count once, and the requested volume is exact.', 'The card asks for the optimal deterministic running-time exponent in every fixed dimension at least three.', 'Each exponent must be certified to absolute error 0.01.', 'Logarithmic factors and a fastest algorithm attaining the infimum are not required.'],
       definitions=defs, kind='function', criterion=exponent_criterion(r'\(a(d)\)',r' for every integer \(d\ge3\)'),
       context={1:r'Chan’s 2013 algorithm computes exact union volume in \(O(n^{d/2})\) time for every fixed \(d\ge3\). This gives the finite upper bound \(x_{\mathrm{Klee}}(d)\le d/2\). Connections with clique problems provide conditional evidence, not an unconditional lower bound for all algorithms.'},
       refs=['https://doi.org/10.1109/FOCS.2013.51'])

d=original('7319')
defs=d['definitions'].split('An answer must give an explicit positive function')[0]
defs+=r' Define the numerical exponent \[x_{\mathrm{cal}}=\inf\{a\ge0:\exists K>0\ \exists T_0\ge1\ \forall T\ge T_0,\ C(T)+1\le KT^a\}.\] The bound \(0\le C(T)\le T\) makes \(0\le x_{\mathrm{cal}}\le1\). The infimum need not be attained and is equivalently the limit superior of \(\log(C(T)+1)/\log T\). No ordinary limit is assumed. Adding one only handles small or zero values. The target does not ask for logarithmic factors in the calibration error.'
quantity=d['formal'][d['formal'].index('\\['):d['formal'].index('up to absolute')]
revise('7319', 'Sequential binary calibration exponent',
       r'Determine to absolute error at most \(1/100\) the exponent \[x_{\mathrm{cal}}=\inf\{a\ge0:C(T)+1=O(T^a)\text{ as }T\to\infty\},\] where \(C(T)\) is the minimax expected ordinary calibration error in the simultaneous-move game below: '+quantity+r'The finite forecast set may depend on the horizon; the adversary may depend on past forecasts but cannot observe the current random forecast before choosing the current outcome. The loss and all quantifiers are defined below.',
       'Replaced full calibration-error asymptotics by a finite exponent in the horizon, with 0.01 accuracy and no invented intermediate power threshold.',
       ['A forecaster repeatedly predicts the probability of a binary outcome.', 'Ordinary calibration groups identical forecasts and sums their absolute outcome discrepancies.', 'The adversary sees past forecasts but not the current random draw before choosing its outcome.', 'The card asks for the minimax error’s growth exponent to absolute accuracy 0.01.', 'Logarithmic factors, computation time and restrictions to a fixed forecast grid are not added.'],
       definitions=defs, kind='numerical_value', criterion=exponent_criterion(r'\(a_*\)'),
       refs=['https://arxiv.org/abs/2406.13668'])


for number in ['0056','5407','6634','7358','7381','7479','7516','4524']:
    retain(number, 'Retained the existing finite numerical optimum with absolute 0.01 precision. The owner explicitly declined invented intermediate thresholds where no natural source conjecture selects one.')
for number in ['6519','6606','6610','6665','7214','1010']:
    retain(number, 'Retained the direct information/coding rate or capacity value/curve with its existing 0.01 precision, as requested in the scope confirmation; binarizing the coding curve would also overlap the existing beyond-GV card.')
retain('6685', 'Preserved the explicitly requested exact witness-based BB(6) criterion.')
for number in ['0441','5127','6748','7099']:
    retain(number, 'Structural classification over a family of instances, rather than an unspecified numerical growth rate. No single conjectural characterization is available to assert or negate without inventing one.')
retain('6874', 'The saved statement is already binary despite missing question_type metadata. This pass does not claim a new completion or solvedness review of the inherited draft.')
retain('5651', 'Two complexity-class recognition classifications, not a numerical optimal-time exponent. Retained pending a separate choice between the GFG and GFM targets; a polynomial algorithm is already excluded conditionally by the saved hardness and is not a neutral replacement.')
retain('0724', 'A full memory/query/accuracy tradeoff with potentially infinite values, not a single finite growth exponent. Retained rather than choosing an arbitrary memory budget and accuracy scaling or imposing a power law.')
retain('1029', 'A multi-pattern removal profile over distance and graph size. Nonbipartite patterns need not have a finite polynomial exponent in inverse proximity; a finite scalar exponent would require an extra scale or pattern choice. Retained rather than silently substituting only triangles.')
retain('7447', 'A structural minimax classification depending on the full policy class and state layers. No single growth variable or power law is specified, so retained rather than inventing an input family.')
