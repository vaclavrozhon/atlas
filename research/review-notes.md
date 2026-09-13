# Research review notes

Historical observations recorded on 10–11 September 2026, retained from the old
working checkpoints. These preserve mathematical-model distinctions, source
revisions, disputed claims and proposed follow-ups. They have not been freshly
verified during repository cleanup. Current [canonical cards](../data/cards/)
and later dated reviews may supersede them. An old “open”, “resolved” or pending
item here is not a current status certificate or an instruction to restore a
removed card. Current policy is in [docs/RULES.md](../docs/RULES.md).

Some original notes use compact notation and four-digit card IDs without the
`TCS-` prefix. Source identifiers and mathematical bounds are retained as recorded.
Publication counters, server addresses, old automation instructions and replay
commands have been removed.

## Model and source distinctions recorded on 11 September

6542 fixeseach rational constant noise separately; polynomial samples do not
imply polynomial time. Sept8 ECCC26/095 conditional code/dual-code hardness.

6547 unrestricted existence implication, both primitives nonuniform classical
security; target-before-key hashing is weaker, oracle separation not refutation.

6559 complement costs zero depth; ordinary star-height resolved but generalized
not. Cotumaccio EATCS145Feb2025 explicit open discussion.

6566 rational matrix/vectors exact zero at any real t>=0; Schanuel only bounded
conditional, low-order infinite-zero decidability is a different question.

6584 fixes causal zero-error ENTROPY capacity convention and closure, shares
edge capacity between directions. Aug6 metrics2608.06070 at most FIVE TERMINAL
LOCATIONS (not five sessions). Planar three faces each pair on same face.
2608.06042 has common-solution quantifier correction in Def3.1 footnote.
FOCS2025 Braverman/He coding gap is MULTICAST, not unicast.

6588 completed at156: primary2412.10744 v2WITHDRAWNDec20,2024, v3Oct10,2025
PDF explicitly RECTIFIES/narrows claim to supplied relatively integral solution;
record still carries withdrawal comment. Do not label allv3withdrawn or general
polylogresolved. Classical Charikar old log²quasipoly corrected tolog³ byauthor;
GLL2019log²/loglogquasipoly known. Planar Friggstad/Mousavi2023Ologk.

6596 OVH: one exponent saving must work across every fixed dimension constant;
July2026 monotone bounds apply to NEGATED OV, not general RAM algorithms.

6605 AA: L2 influence on uniform cube; Sept4 optimal CB inequality is restricted,
Aug19 bounded-round simulation does not prove the polynomial conjecture.
Keller/Klein1911.03748v2 remains withdrawn since Dec2,2019.

6607 capacity: exact curve, input-bit rate, no deletion markers/feedback; general
multiletter limit and computable approximation already known. Pinto/Ribeiro2026
upper .3578(1-d) for d>=.64; ChenAug3 Zenodo21780666 CLAIMED .11032415 lower
at .5, not independently reproduced; his refined upper has table-precision assumption.

6613 formulas over C, free constants/nonuniform/no sharing; cubic bound in MATRIX
DIMENSION, not variable count. Multilinear lower bounds do not cover general formulas.

6623 July5 2607.04073 quasipolynomial SAMPLES, not reconstruction TIME;
linear traces have no circular shift. Local-SQ lower bounds do not bound samples.

6626 exact canonical MSF, randomized strict worst-case polylog each update,
whole-sequence high probability against oblivious adversary. SODA26 dynamic
connectivity gives approximate MSF with 1/epsilon overhead, not exact polylog.
HDLT2001 deterministic log^4 amortized; HRWN2015 improved bound uses random queues.

6629 September9 2609.10516 exp(O(n(loglogn)^2/logn)) deterministic approximation
is not FPTAS. Fixed-power exponent improvement WOULD amplify to FPTAS.

6632 universal DSIC, polynomial COMMUNICATION in n,m,per-value-bit-precision;
local computation unrestricted. SODA21 Thm2 submodular loglog^2, not loglog^3.
Value-query impossibility and graph eligibility constant results do not resolve.

6637 explicitly allows randomized worst-case polynomial time, per-input 2/3 success.
Bansal/Huang/Lee2602.05904Feb5 improves colours to O(n^.19539); constant open.
Five-colour NP-hardness only excludes <=5 under NP!=RP for RANDOM algorithms.
Dawar/Molnar2504.03523v2Mar1 FPC barrier on unordered graphs not all algorithms.

6534 BH uniform p-isomorphism; conditional/nonuniform theorems are distinct.

6536 arbitrary opaque real weights; Pettie/Ramachandran uniform optimal
algorithm does not establish linear time. High-girth source is undated.

6537 constant in expected O(n) independent of word length; all preprocessing counts.

6538 general exact matching: catalytic logspace June2026 only polynomial time.

6540 fixed n log² n cells, Θ(log n)-bit words, explicit polynomial-time Boolean
queries. Ko2025 large-query random operators and Ko2026 DYNAMIC bounds do not
resolve. STOC2026 natural-proof barriers conditional, with errata caveats.

6639 general heterogeneous additive Santa Claus: restricted/identical valuations
constant factors do not resolve; 2024 reduction from makespan is one-directional.

6641 fixes UNIFORM ordinary monoid word problem; Aug2026 inverse-monoid
undecidability is a different algebra. Survey has Sep2022 correction.

6648 adaptive fresh-bit KL betting, partial computable rational stakes; 2025
open-set betting theorem uses witnesses depending on test level, not one KL/non-ML point.

6653 ordinary chromatic bound constant in graph size; 2025 n^o(1) and 2026
fixed-dimensional box intersection results do not prove the general conjecture.

6657 unit-sphere prior, iid raw Gaussian entries, explicit logarithmic-bit rounding,
unrestricted randomized polynomial BIT time; 2024 spherical recovery bound only odd
orders, 2026 independent-prior low-degree bounds not universal algorithm lower bounds.

6674 TIE expected makespan, not maximum expected load; no computation restrictions.
General lower 2-1/m, upper(m+5)/2; task-independent linear lower is restricted.
Nisan-Ronen deterministic m theorem JACM onlineFeb11,2026.

6675 per-fixed-template deterministic decision-P=>search-FP, no uniform converter.
Larrauri2504.04639v4May25,2026 CORRECTS earlier overbroad claims: rounding
hardness uses RELAXATION-accepted inputs, not necessarily A-satisfiable.

6676 all jobs eligible everywhere, arbitrary binary integer lengths, input m;
Svensson factor2 hardness uses STRONGER UGC variant with completeness/expansion.
Das/Wiese2501.09091 is ESA2022, not new2025. UMPSJuly2026 adds unique eligibility.

6678 effective monadic dependence fixed explicitly via computable powerset-graph
obstruction bounds (Maehlmann thesisDef12.24); computable f_C(k) required.
July12 2607.10941 allNIP near-linear neighborhoods and radiusONE mergewidth only.
STOC25 mergewidth v2June23,2026 still REQUIRES input decomposition.

6683 allgraphs gridSIDE r: Omega(r²logr) vs O(r9polylogr); full matching target.

2025 GridMinorRevisited has unspecified blowup c(X), SODA26 CatchingRats fixes
additional excluded minor H: O(genus(H)*r+|H|^2304), not universal linear.

1010 August2026 Alrabiah/Guruswami improves BOTH MRRW bounds; still notexact.

6515 DLV v3Sep2025 corrects rate analysis; distance/soundness log^3 losses remain.
LiLiLiu2604.01874v2July replaces INVALIDv1 argument; CCZ log^5 losses remain.

6517 UNCERTAIN: Balasubramanian/Davydova/Lin2605.10943 May11 claims
3D passive memory via thermal encoding; full proof not independently verified.
Randomized embedding proved; explicit variant lacks lifetime theorem; Eq5 typo.

6518 July2026 two-copy Werner threshold resolved; all-copyNPT remainsopen.
WuZou2608.02647 submittedJULY31 only restricted three-copy sectors.

6519 all values TOTAL Pauli error q; Aug18 certifiedpositive q=.194868,
not exactthreshold; zero q>=.25; no free classical/entanglement assistance.

6665 August2026 Marton counterexample starts input-CONSTRAINED ternary;
unconstrained construction uses larger alphabet. General capacity remains open.

6667 SatoMay2026 counts costly enumeration calls; HiraharaAug2026 conditional
deterministic NP-hardness concerns CONSTANT factors, not every polynomial factor.

6682 Hurley0.119 cites then-unreviewed Delcourt/Postle; Remark3.1 gives0.113
with published alternative. September8 directed revision retains exactReedopen.

0015 explicit=one polynomial-time algorithm; n outputs, fullB2 basis, notO(n)
means unbounded ratios along arbitrarily large lengths, not necessarily all lengths.

0016 fixes nVARIABLES and explicit incidence M=Theta(n^3) encoding; target2^Omega(n),
not exponential in encoding bits. Almost-everywhere lower bound quantifiers explicit.

6636 July2026 FO/L-hard theorem only EXPANSIONS of homogeneous model-complete
cores; not arbitrary reducts, and L-hard is not NP-complete.

6638 2−1/m is known but not a fixed constant improvement; June2026 predictions
retain worst-case2; SODA24 reductions tie improvement to general SantaClaus.

6647 unresolved complement of cone above0doubleprime includes incomparable
degrees, not merely interval below; historicCooper1999 unverified.

6652 fivevertexcases resolved, twoJun/Aug sixvertexcases + Aug28 third.
Sagi1211.3876v2 withdrawn but v3 revisedclaim; contemporary2026sourcesstillopen.

6663 proof SIZE simulation, not p-time translation; September5 ECCC26/166
is QUASIPOLY two-bucket partially commutative FORMULA IPS overGF2.

2014 tutorial overstates some candidate exclusions: quasipolyupper does not
rule out superpolyseparation; Kneser2018 preserves that distinction.

6606 is UNCERTAIN: Khandani2501.14941v12 September7 claims weak capacity;
January2026 Nair/Zhao criticism does not automatically refute this revision.

6604 quantum FEI counterexample is not classical; Han bound keeps extra term.

6612 fixed complex field, polynomial degree; symmetry results restricted models.

6625 expected worst-case Las Vegas connectivity is not deterministic polylog.

6628 August2026 permanent speedup remains bipartite.

6587 exact-k deterministic constant-factor approximation; ETH already rules out.
Bhaskara2010 polynomial n^(1/4+eps), endpoint n^1/4 only quasipolynomial.

6600 weighted PRGs != ordinary; ECCC26/064 revision3 May4 corrected attribution.
Cohen/Doron/Goldgraber July21 ordinary PRG only PERMUTATION programs.

6602 Lu/Santhanam/Tzameret ITCS2026 candidates have UNPROVED tautologicity;
Itsykson et al. Feb2026 restrict DAG depth, not logical formula depth.
Hakoniemi et al. May2026 CNF hard only restricted roABP-IPS_LIN.

6580 April2026 MIP relativizes but does not give efficient single-prover IP.
May2026 verification without trusted prep/measurement still needs trusted gates.

6585 fixes arbitrary nonsingular rational matrices, polynomial κ and inverse-poly
residual, finite-precision RAM costs and explicit vector. Nie2022 improves PV2021;
faster-than-matrix-multiplication is already solved. Workshop2602.05394 is v3Aug21.

6550 fixes polynomial modulus/noise and polynomial hardness;
circular leakage-resilient LWE is additional, not plain LWE. 6562 July2606.14167v3
claims NEXP hardness of POSITIVE BOOLEAN nonerasing word equations + lengths,
not a general NEXP upper bound. 6565 simple-LRS ultimate positivity supplies no
general effective cutoff, so positivity itself remains open. 6567 FUN2026.19
only solves STOPPING SSGs on ladders; Theorem10 is ARRIVAL, not SSG.

6568 Loff/Skomra ICALP2024.147 requires ERGODIC graphs (arXiv abstract omits it).

6572 fixes polynomial BIT time for improving primal pivots from supplied BFS;
this is weaker than strongly polynomial simplex. SODA2026 active-set lower
bound is convex QUADRATIC MAXIMIZATION, not linear. March2026 antistalling
bounds n−m−1 consecutive degenerate pivots, not total visits to vertices.

6574 Ramana only proves NP iff coNP in Turing model, not membership in either.
Henrion/Naldi/Safey2018/2021 retains generic auxiliary/objective conditions.
STOC2026 Hesse’s Redemption handles convex-polynomial minimization over a
polyhedron, not arbitrary exact SDP feasibility. Real witnesses may be irrational.

6575 randomized Ω(log²k) disproof leaves deterministic k-server open. Circle
3-server theorem first2022, journal2024. 2026 benchmark is finite testing, notproof.
Anshu/Arad/Gosset2D FF local-gap entropy bound is n^(1+o(1)),
not strict O(n). Anshu/Harrow/Soleimanifar2022 is entanglement SPREAD, not entropy.
The Jukna12.28 locator was Majority outside ACC0, not TC0 vsNC1.
Samplecompression Attias2025 OpenProblem28 is robust compression, not the standard
conjecture (which appears in §1). 2603.23561v4 is WITHDRAWN Aug3, incorrect Lemma2.

6541 fixes unordered labeled subsets + counted side bits, possibly improper.
KLS Letwin2607.24164v1 bounds psi bylog^1/4, so CP bysqrtlog.
Thin shell2507.15495v2 is resolved, notfullKLS. EF AlekseevToC2026.4 BVP
lower bounds do not translate to ordinary polynomial-sizeCNF/EF lower bounds.
Hadwiger 2609.06867v2 Sept9 claims O(t logloglog t), not t−1. Odd Hadwiger
was disproved Dec2025 (2512.20392), not ordinary Hadwiger. Planted clique
2505.01990v2 optimal advantage is CONDITIONAL and uses binomial planting.
The full card fixes exactly k vertices, equal priors, success2/3 all large n.
Martin’s full PartI quantifies all invariant functions; below-identity-only is resolved.
Pending lower-priority research: 0585 Hamiltonian sidestep radius (ESA2026.73,
2501.10633v2); 0596 OCT on P5-free graphs RESOLVED (TALG2025.16 DOI3708544,
2410.21569v2 March5 2026 also generalizes). 

## Distributed and local models

- 0595 accepts ALL THREE terminal pairings, requires anticomplete paths. ICALP2025.4
  fixed-pair and S-T flow hardness does not establish hardness of their union.
- 0518 explicitly zero-error non-signaling outcomes, marginal consistency for EVERY
  vertex subset; all bounded-degree graphs. Not just identical one-node marginals.
- 0519 deterministic connected stateless volume poly(Delta) independent of n; supplied
  proper two-coloring. Round lower bounds alone only force Omega(Delta) here.
- 0520/0521 RESOLVED NEGATIVELY by an explicit editorial composition: constant
  online -> constant component-wise online (2403.01903v4 Lemma 7.5) -> deterministic
  sqrt(n)*polylog(n) LOCAL (2504.05191v2 Section1.6/Section4.1/AppendixA). LOCAL ->
  dynamic -> online then rules out both linear-vs-constant separations. The cards spell
  out the deterministic clustering/completion proof. No withdrawn dynamic
  derandomization theorem used. Model starts with EMPTY graph and future inputs unknown.
- 0522 remains OPEN. 2608.11720v1 August12 proves linear lower bound ONLY for
  ANONYMOUS quantum-PN, success exactly1. Section1.4 leaves high-probability case open.
  2607.04852v2 July11 rooted-tree bound uses GROWING DEGREE, and its even-cycle theorem
  is for TWO colors; neither resolves degree2 three-color high-probability problem.
- 2504.05191v2 August17 strengthens quantum LCL separation to O(log n) vs
  Omega(log n*(loglog n)^0.99). The older loglog/logloglog bound is superseded there.
- 0523 July2026 Peng2607.09626 constructs log^k n only for INTEGER k>=1. The interval
  sqrt(log n) to log n remains unknown. Private per-vertex tapes reused across queries.
- 0590 original cross.pdf source is Jan4 2025, not2022; spherical-geodesic crossing
  theorem2504.07770 does not settle arbitrary curved drawings of K_n.

## Earlier algorithm and status observations

- 0515: Peng 2607.09626 July 2026 constructs RANDOMIZED intermediate volume
  complexities; explicitly leaves deterministic gap open. Connected adaptive
  probes, exact input size, polynomial IDs; no shared mutable query state.
- 0516: incremental edge additions, global graph reading allowed; only radius
  of output recolorings is restricted. Online lookaround upper bounds do not
  imply a dynamic upper bound. 2403.01903v4 (Feb 13 2026) corrects prior dynamic
  derandomization claims; always use v4, not old STOC version or author PDF.
- 6330: Sinnamon/Tarjan 2307.02772v2 Theorem 7.18 resolves multipass logarithmic
  amortized delete-min. Not worst-case and not path-balanced BST resolution.
- 5411: Domingues 2603.23119v1 Theorem 1 with epsilon=1/4 gives deterministic
  worst-case log n/loglog n, redundancy n*(log n)^1/4 = o(H), H~nlogn.
  Original 2025 question means succinct relative to H, NOT o(n) redundancy.
  SODA2026 Kuszmaul/Liang/Zhou 2510.19175 gives o(n) redundancy but amortized
  expected time. Keep resolved and preserve the exact distinction.
- 0533 is resolved by Ghaffari FOCS 2022; retain full card and resolved status.
- 0003 is UNCERTAIN: Lin 2308.09549v9 July 2026 claims a separation, unvalidated.

- Matrix exponent: August 17, 2026 paper 2608.16884v1 reports omega<2.371177;
  2404.16349v3 incorporates it on August 19. Its rational certificate is described
  in Section 4, but the repository was still being prepared. No local replay.
- Strongly polynomial LP: status UNCERTAIN because Awoniyi 2503.12041v10,
  July 4, 2026, claims a general solution; no independent validation located.
  Do not present that claim as either proved or disproved. STOC 2024 two-nonzero
  LP result is established; STOC 2026 trust-region result retains dependence on
  straight-line complexity and is not a general strongly polynomial solver.
- L versus NL: STOC 2025 Doron/Pyne/Tell/Williams gives a per-input alternative
  between improved reachability and nondeterministic random-walk estimation;
  it does not supply deterministic logspace directed reachability.
- Weighted Kamp: December 2025 Gastin slides fix the previously vague temporal
  grammar. Full card 0484 specifies the natural-number finite-word instance.
- Duplicate 0485 individually linked to full canonical DNF card 0310 through
  review_outcome.duplicate_of. Related bibliography entries are objects, never IDs.

## Data-structure and semiring questions

2016DSreport§4.1TCS0479 maximumreachablepairsinacyclicsubgraph (notmaxedges);
§4.3TCS0480 expectedoptimalalphabeticBSTunderDirichlet(1,...,1)leafweights.
Wildoriginal2015question https://cs.stackexchange.com/questions/49896/ (primary
becauseauthorhimself); stillunanswered, definesaverageredundancyandH<=C<H+2.
Aprecisebinaryspecializationcouldaskwhetherexpectedredundancyconvergesas n→∞;
doNOTassumeconstlimitifperiodictermspossible; broadsourceasksfullexpectation.
FullasymexpectedcostleadingTheta(logn)alreadytrivial,needadditiveprecisionifchosen.

2025semiringreportstartsline4386;openproblemslines5174onwards intext:

0481 singlepairundirectedshortestpathmin-pluscircuits nonnegativeweights:Omega(n²)
vsO(n³);sourceexplicitabsorptivesemiring, citeJukna2015DOI10.1007/s00224-014-9574-4.

0482 Datalogo p-stable semiring convergenceO(pn⁴) vsOmega((p+1)n), conjecture
linear((p+1)n),ref2312.14063 nowPODS2025needlatest2026beforewriting.

0483 subreductsofmonussemiringscharacterization; needsbinaryprecisetarget.

0484 weightedFOlanguage sourceasksadequatestarfreeness/LTLdefs, nofixedlogic;
likelyneedsindividualdispositionunlessexplicitconcreteunresolvedstatementfound.
Report§4.5conjunctivequerycontainmentbagsemantics decidability remainsopen2025;
findexistingIDbeforeadding/upgrading; 2026statusmustchecked.

## Heap batches and dynamic APSP

Onlyfinalmembershipvectorrequired, notdeletedidentities/order; wholeinputknown.
TCS-0478dynamicAPSPwas checked against 2025/2026 sources. FoundESA2025.113
Bootstrapping Dynamic APSP via Sparsification (likelyapproximate); arxiv2306.02662
LikelyOptimalWorstCaseUpdateTime v3 actually gives randomized tildeO(n^2.5)
worst-case vertex updates (NOT nearquadratic); the classic deterministic
tildeO(n²) bound is amortized. Target remains sparse edge-linear amortized.
Do notmistake titleLikelyOptimal(densevertexupdate)forsettledsparseO(m)target.

## Grammar, reporting and pointer-model distinctions

TCS-0477offline heap final-survivor comparison complexity fromDagRep11.1.1§5.3;
primarycachedresearch/continuation/datastructures2021.txt lines1203–1240. Source
asks O(n)comparisons, not onlinequeries nor identities/order ofdeletedminima.
0476samevolume§5.1 is only a proposed extended wordRAM instructionset, noactual
preciseconjecture: consider individual disposition rather than inventingquestion.
0478samevolume§5.2 asksfullydynamicAPSPtildeO(m)update/tildeO1query; needslateststatus.
0471halfplanepairintersectionreportingstillunreviewed; broadsource2025§5.7.

Grammar0470specifiesO(glogg)persistentbits/O(logN)query, polynomialgpreprocessing,
polylogqueryworkspaceexplicit; April2026Takasaka/I retainedglogNterm,ICALP2026
Duyster/Kociumaka uppertheoremregimeMw>glogNdoesnotsettlethisbitbudget.
Circle0472nowexpliciteditorialplanarreportingtargetO(nlog³n)preproc/space,
O(log³n+k)query. ISAAC2025Afshani/Bosch/Storandt alreadyO((n+C)log³n)preproc,
O((k+1)log³n)queries; don’tcalloriginaldirectionuntouched. Fullsourcescached.

Pointer heap paper 2604.24134 has v2 from 2 July 2026,
renamed Near-Optimal Working-Set Heaps and Dijkstra on Pointer Machines; Theorem3
still inverse-Ackermann decrease-key, open removal explicit. July2607.24621
stack-like heap has growing insertion cost, so does not settle joint O(1) target.
Chen-Dumitrescu 2019 manuscript Conjecture1 is o(n log n), NOT Omega(n log n).
Three-group linear target in2025report remainsopen; stable partition and natural
ordering explicitly required by2019source. Do not replace with repeated-step.

## Formulation audit observations

- Replaced vagueprivate-PAC, RS-product-expansion, and LPN formulations with
  explicit quantified targets. LPN’s NCP implication and the fixed-parameter
  private-PAC bound are labeled editorial specializations of broader sources.
- Strong quantum IOPs permit private workspace; restrictions concern prover
  message access and fresh quantum messages. Do not restore the earlier false
  prohibition on private memory.
- Pessiland card asks for infinitely-often one-way functions, matching ECCC
  2026/052 revision 1; do not silently strengthen to all sufficiently large n.
- Lazy B-tree target charges stable handles and limits internal memory to O(B)
  words. Fixed announced capacity N prevents hidden free storage assumptions.
- MPC lower-bound negation is not automatically an o(log n) algorithm for all n.
- Triangle detection asks for the optimal randomized CONGEST round complexity
  up to constant factors. Deterministic bounds are context, not a second target.

## Dated status findings

- LZ77 pattern matching TCS-0468: the 2011 algorithm handles self-references and
  costs O(z(1+log(N/z))+m). Ganardi–Gawrychowski 2021 / STOC 2022 solves the
  grammar-input version in O(g+m). The 2025 Dagstuhl question retains LZ-input
  linear time. Do not identify g with z or charge an index outside preprocessing.
- Splay traversal TCS-6512: arbitrary initial A, preorder of arbitrary B, same
  keys. Levy–Tarjan arXiv:1907.06309 Conjecture 2; Theorem 4 only assumes a
  weight-balanced B. Linear insertion is a different operation sequence.
- Smallest grammar TCS-6513: sum of RHS lengths, arbitrary alphabet, constant
  approximation. Casel et al. DOI 10.1007/s00224-020-10013-w appeared online
  November 2020, volume 2021; it does not rule out all constant factors.
- Pure pairing heaps TCS-6514: arXiv:2607.23118v1 July 25, 2026 leaves a
  log log log n factor in decrease-key. Single pairing pass, then select minimum
  survivor and concatenate the remaining root list before its children. This
  differs from standard and multipass heaps. Section 10 announces an improved
  standard-pairing bound for a forthcoming paper; do not treat its proof as
  present here. The card fixes a total cost using maximum live population N.
- Multipass delete-min TCS-6330 is resolved by arXiv:2307.02772 / TALG 2025,
  DOI 10.1145/3708989. This is separate from the remaining decrease-key gap.
- General Exact Matching: arXiv:2508.04081v2, revised 10 August 2026, gives
  simultaneous randomized decision for every red count in O(n^omega) FIELD
  operations. Introduction and Theorem 1.3 retain deterministic polynomial time
  as open. TCS-6511 cites this version explicitly.
- Bipartite Exact Matching: arXiv:2604.01571v3 (9 April 2026) claims a
  deterministic algorithm with O(n^6) arithmetic complexity. Its Lean appendix
  retains eight explicit hypotheses. Do not repeat v1's unqualified formal
  verification claim, infer bit complexity from arithmetic count, or generalize
  the bipartite claim to all graphs. TCS-0611 records uncertain status.
- LZ77 access: arXiv:2607.14923 gives results for LZ-End, and explicitly retains
  the linear-space LZ77 target as open. Do not equate z_end with z. TCS-0467
  specifies self-overlapping greedy LZ77, O(z) words, and O(log N) access.
- Splay deque and split conjectures: TCS-6508 and TCS-6509 specify exact legal
  operations, arbitrary initial trees, and total linear cost. Appendix D of
  arXiv:2607.18498 gives a nonconstant-factor split bound, not linear time.
- Deterministic LOCAL coloring: TCS-0524 fixes exponent .499 in
  O(Delta^.499 + log* n); TCS-0517 fixes palette O(Delta^1.001) and O(log* n)
  rounds, with constants independent of n and Delta. Faster randomized coloring
  or a bound only for each fixed degree does not resolve these propositions.
- Bipartite maximal fractional matching TCS-0525 requires exactly maximal
  rational weights in f(Delta)=o(Delta) rounds, with no additive n term, and
  a supplied bipartition. General-graph lower bounds do not settle this case.
- CONGEST even-cycle TCS-1813 asks to match the fixed-k upper exponent for all
  k >= 3. ICALP 2025.80 keeps these cases open; C4 alone is already tight.
- APSP TCS-6510 uses general real edge weights and a comparison-addition model.
  May 2026 node-weighted triangle improvements (arXiv:2605.08588) have different
  weight structure and do not resolve this target.
- Splay dynamic optimality: July 2026 arXiv:2607.18498 improves the competitive
  factor; constant competitiveness remains open. TCS-6498 states the root-BST
  model and additive initialization cost precisely.
- General randomized LOCAL MIS: new 2025 lower bound sqrt(log n); girth >=7 has
  a sublog algorithm. Do not copy the older claimed sqrt(log n) tree conjecture.
- Lazy B-trees arXiv:2507.00277v2 has a December 2025 pointer-cost erratum.
  TCS-6502 makes the unresolved stable-handle target explicit. Do not state the
  original priority-queue bounds with fully charged pointers as established.
- Bipartite perfect matching: June 2026 ECCC 100 claims NC (including search and
  polynomially bounded weights). TCS-6504 is general-graph perfect matching.
  Do not confuse perfect matching with the separate Exact Matching problem.
- Parallel reachability: August 2026 arXiv:2608.13231 gives polylog depth with
  work Otilde(T^(omega/2)), T=transitive-closure size. TCS-6507 incorporates it;
  T can be quadratic even when the input is linear-sized.
- Dynamic connectivity: FOCS 2026 accepted Meierhans/Probst Gutenberg/Yeh,
  “Dynamic Connectivity, Minimum Spanning Tree, and 2-Edge Connectivity with
  Polylogarithmic Worst-Case Update Time.” No full text located yet. Author
  webpage also lists title only. Do NOT add a deterministic polylog worst-case
  open question without checking this new result’s randomness guarantee.
- FOCS 2026 “Distances in Planar Graphs are Almost for Free!” and “Dynamic
  Entropy-Encoded Arrays in O(1) Time with Nearly Optimal Space” also need scope
  checks before importing older questions.
- ICALP 2025 dynamic succinct FID target (in TCS-5411 source note) is materially
  affected by arXiv:2603.23119 (March 2026). Succinct there means redundancy
  o(log binomial(U,n)), not necessarily o(n). Do not re-add unchanged.

## Source checks proposed at the time

1. ECCC 2026/169 (Jeronimo), received September 2026, claims RS list decoding at
   capacity for prime fields, time q^{O_gamma(1)}, list size n^{O_gamma(1)}.
   Do not treat this as polynomial in log q for arbitrary q, or a result for all
   extension fields. Check/update legacy TCS-1011 and TCS-1337 precisely.
2. ECCC 2026/171 (Gao–Ji–Xie), September 7, claims a total-function quantum
   query-memory separation resolving a question of Hao–Huang–Liu (STOC 2026).
   Do not re-add that exact existence question as open.
3. ECCC 2026/096 (Viola) refutes the dream XOR lemma. Exclude stale versions.
4. ECCC 2026/052 revision 1 changes the Pessiland approximation factor from the
   original report. The detailed card uses the June revision.
5. FORC 2026.4 improves Gaussian private selection to
   O(log|Y| (log log|Y|)^11 / sqrt(rho)); exact optimality remains open.
   Both Gaussian and pure-privacy Laplace detailed cards record this distinction.
6. ECCC 2026/150 proves 2D RS product expansion and conjectures higher dimensions.
   Its AI-generated candidate higher-dimensional proof is explicitly unverified
   by the authors. Do not treat it as a solution.
7. ECCC 2026/020 separates QMA/QCMA and quantum/classical advice relative to
   classical oracles. The unrelativized questions remain distinct and open.
8. ECCC 2026/013 revision 1 uses quantum communication with unlimited shared
   entanglement. The AND-composed result has a log^2 n factor; it is not the
   unrestricted polynomial-equivalence conjecture.
9. arXiv:2608.16884 claims omega < 2.371177, August 2026. Update matrix
   multiplication only after checking precise scope; the old card is TCS-0007.
10. ECCC 2026/076 solves whitebox PIT for nonmultilinear read-4 formulas and gives
    quasipolynomial blackbox PIT (characteristic 0 or >=5). Source includes
    remaining targets; avoid copying an already-solved whitebox question.

## BB(6) conventions

Use the binary, bi-infinite-tape runtime convention BB(6)=S(6), with six nonhalting states plus halt; count the final transition. This is distinct from Sigma(6), growth/ordinal threshold questions, and population-protocol Busy Beavers already in the catalogue.
- The primary BB(6) project page (revision 3 September 2026), dated holdout list, Antihydra page, and BB(5) proof paper support the current status and context. The task is exact determination, with an attaining machine and a matching universal bound. Larger lower bounds alone do not resolve it.

## Additional model and revision checks from 11 September

6684: fixed q≥5, assortative a>b, independent uniform labels (asymptotic balance),
expected label overlap. Ding/Hua/Slot/Steurer2502.15024v2 is CONDITIONAL on
restricted Conj1.3 bounded tests with planted expectation Ω(1); prior version
of conjecture refuted by rare events. Banks2016 assortative IT gap q≥11,
not q≥5 (that is disassortative). Chin et al2503.03047v3Aug23,2026 corrects
Theorem1.2; algorithms below KS with q growing past sqrt(n) do not resolve fixedq.

0037: NP noncontainment in uniform BQP, equivalent SAT outsideBQP; BBBV
black-box oracle bound not unrestricted. Cifuentes2606.19545June17 conditional
Pauli-detection hardness continues to assume NP noncontainment.

6520: uniform additive approximation, channel Choi matrix described by promised
Cauchy program; unrestricted halting time, no assistance/memory/zero-error.
Bhattacharyya/Mehta/Zhao2601.22471v3March30 corrects v2 Sections2,4; QMA-hard
quantum capacity uses SUCCINCT CIRCUIT input; undecidable result is restricted
ONE-SHOT CLASSICAL zero-error with MAXIMALLY ENTANGLED assistance and
PROJECTIVE decoding, not ordinary Q. 2015 unbounded block lengths does not
rule out computable input-dependent stopping; 2009 continuity not convergence.

6525: GNRS all positive weighted fixed-minor-free metrics into l1, all pairs;
CKR2010 Sherali-Adams fixed-treewidth constant approximation does NOT bound
ordinary flow-cut gap. ChekuriMay4,2026 notes still planar sqrt(logn) upper.
Mori2602.23745Feb27 exact c1(K2,n)=(3k-2)/(2k-1), k=ceil(n/2), bounded1.5.

6528: UNCERTAIN CLAIMED RESOLUTION. Chad Musick2609.06492v1Sep6 Theorem1/
Corollary1 claims P via locally minimal bridges and compressed grammar;
local-minimality lemma and compressed-update complexity not independently
validated. Lackenby2607.23350July25 new hierarchy algorithm Section9 does
NOT bound L,g by input. 2021 quasipolynomial remains an ANNOUNCEMENT in
SoCG2025source. NP1999, unconditionalcoNP2016/2021, polynomial Reidemeister
sequence existence2015 does not find sequence in polynomial time.

TCS-6533: NL=UL, one uniform ordinary read-only-input logspace machine.
RA nonuniform NL/poly=UL/poly does not remove advice. van Melkebeek/Prakriya

2019 gives polynomial-time O(log^{3/2}n) unambiguous space. Pyne/Tell2026 weak
lower-bound win-win applies to LINEAR space, not NL=UL. HozaJuly2026 lower
bound is oblivious weight-one isolation; graph-dependent isolation is not excluded.

TCS-6539: one uniform randomized word-RAM algorithm, strict worst-case
(n+m)^{1+o(1)}, not a disjunction with linear. AYZ still m^{4/3} at omega=2.
Dumitrescu2403.01085v2 withdrawn March5,2024. Vega202506.0875v3 parent-edge
rule misses triangle {0,3,6} on DFS path0..6 plus edges03,36,06. Locally checked
stated rule, NOT publisher FigureA1 implementation. Latest v13 changes topic to
vertex cover. Separate202511.2197v10Sep8,2026 claims n², not all-density nearlinear.

TCS-6543: arbitrary noiseless juntas, iiduniform labelled examples only,
poly(n,2^k,1/epsilon) with universal exponent, improper circuit hypotheses allowed.
Sample sufficiency does not solve support search. MOS2004 is JCSS69(3)421–434.
ValiantFOCS12/JACM15 roughly n^.6k; local full manuscript datedAug29,2013.
Noiseless sparse parity is Gaussian-elimination easy despite SQ/correlation barriers.
Beretta2025 DISTRIBUTION learning not Boolean labels. Cornacchia/Mikulincer/
Mossel2605.10237 May11 uses correlated RANDOM WALK samples, not iiduniform.
Inherited OpenReview wszZlP1K14 inaccessible/unidentified; preserved and explicitly
not relied on. Servedio2511.08791Nov11,2025 confirms main open model.

TCS-6546: explicitly fixes FULL-DOMAIN KEYED permutations, nonuniform
classical security for premise and conclusion, ordinary existence implication.
Rudich1988 thesis barrier conditional on combinatorial conjecture (later proven);
not an unconditional standard-world separation. Matsuda/Matsuura2011 one-bit
expanding injective adaptive OWF barrier is FULLY BLACK BOX. AS2015/752 revised
Oct11,2015,TCC16,JCryptol31(3)2018 excludes OWF black-box even dependentdomains,
separate iO barrier needs domain invariance. Shmueli/Zhandry2507.12456July16,2025
Theorem6 full-domain TDP from SUBEXP iO+SUBEXP OWF. Section1.4 distinguishes
INPUT domain invariant from KEY domain invariant; obfuscated public keys violate
latter, so no contradiction to AS. Never claim iO-only/fullcube impossibility.

TCS-6548: IND-CCA2 full adaptive allpolynomialquery security plainmodel,
classical nonuniform bothpremise/conclusion. Unrestricted existence, no black-box
requirement. Gertner/Malkin/Myers07 barrier assumes constructed Dec never calls
base Enc. Choi/DachmanSoled/Malkin/Wee08 boundedCCA2 fixes q BEFORE scheme.
HKW2020 injective TDF suffice (no lossy/correlated-product restriction), not arbitrary
PKE. KoppulaWaters19 adds HINTING PRG. Matsuda2023/1957 firstDec25,2023,PKC25,
May12,2025 revision WEAKENS BARG succinctness beyond known NIZK implication.
Brzuska/Klooß/Woo2025/1665 PKC26 latestJuly17,2026; arbitraryCPA threshold
transform uses RANDOM ORACLE, other route semi-maliciousCPA extraassumptions.

6551: classical UNLEVELED FHE, polynomial-modulus LWE, NONUNIFORM security.

2026 multi-key paper Setup takes L; quantum paper has L+1 keys/quantum Eval.

6552: reusable adaptive computational NIZK ARGUMENTS, honest private-coin CRS.

2026 black-box OWF succinct ZK is INTERACTIVE; BARG adds assumptions.

6556: bits, fixed adversarial order, randomized 2/3 decision, local time unrestricted.
GO2013 precursor CCC, revision3Feb2016 exact bound includes p^20 log^1.5 n.
Sept9 2026 monotonicity v2 retains n^.5+o1 reachability; Theorem9 reduction.

6561: four-language DD0, integer levels, ∀k∃A_k not stronger uniformity assumption.
Barloy/Cadilhac/Paperman/Straubing2501.14899v2 WITHDRAWN Jan31,2025 fatalLemma19.
Generic Results journal63(4)2019, ONLINE2018, notvolume62.

6563: partial INSIDE-OUT call-by-value ordinary output-tree equality.
Weakselfnesting source Feb2023 not2022; origin equality is different.

2026 growth and model-expressiveness equivalence do not settle checker.

6569 fixes ordinary HoTT and coherent internal finite tower; two-level/displayed theories do not solve this version. 6573 includes pointed unbounded polyhedra; 2026 polynomial CIRCUIT diameter does not bound edge diameter. 6579 scalar Crouzeix marked RESOLVED using Jin, Lorist/Schwenninger and explicit expert checking; complete conjecture remains separate. 6581 preserves strong logarithmic error dependence; FEI gives only weaker 1/epsilon exponent. 6582 exact deterministic value-tree equality includes bottom leaves; coinductive Horn reduction still conditional, higher-order polyregular equivalence uses a different model.

6589 metric TSP subtour gap keeps recent 2.05522e-30 improvement as a preprint claim; September 8 computation checks n<=16, half-integral n<=18. 6597 fixes the leading k-clique exponent with uniform randomized RAM and symbolic complex omega. 6608 concerns single unconditional rational linear information inequalities; conditional undecidability is different. 6614 deterministic finite-field factorization remains open even under GRH; sparse multivariate results suppress the univariate oracle. 6619 exact Euclidean SVP requires simultaneous 2^{O(n)} bit time and polynomial bit space; January 2026 coarse-grained sieving proposal does not prove the required worst-case exact-success bound.

6621 heat-bath Glauber uniform polynomial; Carlson/Vigoda requires MAXIMUM degree Delta>=125; Aug27 JMV girth improved eleven to SEVEN, Aug26 Chen/Liu girthFIVE fixed relative slack, not additive-two. 6624 O(n polylog n) fixed-factor ED distinct from n^{1+epsilon}; Andoni/Nosatzki SIAM55(4) onlineAug17,2026 is same FOCS2020 guarantee. 6627 explicit mate array, expected amortized, oblivious polynomial-length sequences; matching-size estimates and maximal matching differ. Original MPI report retrieved via REST endpoint, p123 confirms target. 6630 vague structural criterion replaced by explicitly EFFECTIVE DECIDABILITY target, labelled editorial specification of survey Problem3.14; ECCC26/144 containers remain universally quantified, no finite-list decider. 6633 exact complete disconnected RW deterministic; Sept4 Ye/Bai2609.05191 preprint n^{O(1)}2^n queries, not bit time; Sokolov2023 n^{8n^2(1+o1)} earlier; Cheze2025online/2026volume random INPUT profiles, not worst-case randomized algorithm.

6640 OPT+C explicit-item polynomial BIT time; LP gap and high-multiplicity
exact lower bounds are different questions.

6642 UNIFORM group presentation input; Magnus word decision does not give
negative conjugacy certificates. Gray/Reilly Aug2026 inverse monoids and GROUP
PREFIX membership undecidability do not settle group conjugacy.

6645 explicit EDITORIAL effective yes/no classifier formulation of full
self-join tractability classification; fixed-q deterministic RAM with polynomial
address space, growing memory, distinct outputs, FIRST/LAST/EMPTY delays.
Rouvroy May2025 preliminary report leaves acyclic projected cases open;
June2026 semiring incremental classification is self-join-free and dynamic.

6649 RCA0+HT implies ACA0+? Nonimplication may use nonstandard models;
negative does not automatically mean HT=ACA0. Liu/Patey2606.12962v2Jul2
fixed-dimensional UNORDERED Carlson-Simpson in ACA0, not HT/ordered counterpart.
Le Houerou/Patey2607.28116Jul30 different one-variable conservation result.

6654 decidability of CLASS SAT, not one-graph model checking. Plain MSO1 no
parity/edge sets. Bounded clique-width not sufficient for arbitrary subclasses.
Duron/Mahlmann/Torunczyk2607.10939v2Jul26 hereditary2-WQO hypothesis does
not follow from general decidable MSO1; sourceICALP2025.167Conj40 stronger.

TCS-6659 metric k-Median: CGLSS25 v2 May19,2026 strict-k randomized
2+epsilon approximation; bicriteria bound intermediate only. Hardness 1+2/e
from Max-k-Cover; randomized lower bound needs NP!=RP. Own star LP gap 2-o(1).

TCS-6661 Hyperclique: classical randomized dense word-RAM, every fixed
h>=3,k>h; one fixed polynomial exponent saving refutes. Graph case h=2 excluded.

2026 arithmetic progression and sparsity connections remain conditional.

TCS-6662 deterministic RIP: exact rational output, uniform poly(N) BIT
time, fixed distortion1/3, all sparse supports, optimal s log(eN/s) rows.
Rao DOI2024 is journal189 March2025; fewer random bits, not deterministic.
FickusLake v2July2025: ETF minimal coherence does not imply higher-order RIP.

TCS-6664 asymptotic GotsmanLinial: universal C independentd. Exact
maximizer false (Chapman SODA2018, arxiv2021), asymptotic open. Kane sqrt(n)
polylog bound remains. Chang/Slote/Volberg/Zhang2604.08095 v2Apr27 strengthens
BSA to polylog and adds Chang; BSA=E sqrt(sensitivity), not E sensitivity.
Kothari/KovacsDeak/Wang/Yang2601.08727 v2Apr8 adds author, improves degree
relation, restates GL in5.2; v1 §4.2 and Kane20 citation outdated.

TCS-6670 dynamic global mincut: simple unweighted, exact value,
expected amortized polylog updates, worstpolylog queries, polynomial space
and preprocessing, whole oblivious polynomial sequence success.
ElHayek/Henzinger/LiSODA2026 exact n^o(1) AMORTIZED and cut-size restricted;
proper nonzero cuts only internal. Treepacking deVos/Christiansen June3,2026
Algorithmica88:52 unrestricted deterministic m^(11/12), not polylog.
Incremental exact solved; weighted and s-t lower bounds do not settle simple global.

TCS-6677 one-relator group isomorphism: all finite one-relator presentations,
abstract group isomorphism, not equivalence of marked relators. Torsion case is
solved through hyperbolic-group isomorphism; generic Kapovich Aug18 2608.17238
does not handle every input. Aug3 Nyberg-Brodda 2608.01983 proves unrestricted
Diophantine undecidability in BG(1,d), not isomorphism/conjugacy undecidability.
Also updated existing TCS-6642 conjugacy with that sharper August result.

TCS-6679 ordinary Turing-equivalence Borel universality: countable CLASSES,
all oracles, nonuniform Borel reductions. Polynomial-time Turing universality
does not transfer under coarsening. Marks uniform obstruction depends on the
standard generating reductions. Day/Marks 2004.00174 v2 Feb16,2026 has conditional
many-one universality consequences, not Turing universality resolution.

TCS-6680 SROIQ Boolean CQ entailment: all finite OR INFINITE models, exact
KR2006 role regularity/simplicity; query roles may be non-simple. JAIR2010
simple-role queries and IJCAI2011 Horn-SROIQ solved; KR2016 FINITE CQ undecidable
is different. 2019 absorption only conditional termination. 2511.07933 v2
May8,2026 proves S=ALC+transitive roles 2ExpTime-complete, not full SROIQ.

TCS-0025 unrestricted Frege: complete proof BIT size vs final formula size,
no line cap, no depth cap, DAG reuse, no EF abbreviations. Tree-like Frege alone
polynomially simulates DAG Frege; 2604.28172 April30 has crucial LINE SIZE cap,
which that simulation does not preserve. Davis/Robere ECCC26/055 formalizes
bounded-depth lower bounds, not unrestricted lower bound. Alekseev ToC June21
algebraic BVP is not polynomial-size propositional CNF translation.

TCS-6521 dihedral HSP: arbitrary H, coset-separating binary-label XOR oracle,
uniform bounded-error total work polynomial in log N plus label length; no free
postprocessing or subset-sum oracle. Regev lattice consequence requires COSET
interface, not automatically arbitrary hiding-function oracle solution.
IMPORTANT CURRENT CLAIM: Daniel Simon ePrint2026/1591 received Aug3, latest
Aug17, four revisions; polynomial DCP claim disputed. Gupte/Ragavan/Zhandry
ePrint2026/1693 received Aug15, revised SEPT1 proves failure of algorithm via
truncated Fourier labels, broader restricted template. Primary abstract and
author site checked; PDF403; Lean repo description checked, not rerun.
Guo/Yang2608.16598 Aug17 correct lemmas but partition independence assumption
not supplied. Card marked UNCERTAIN with this exchange, no accepted resolution.
Moore/Young2202.09697 WITHDRAWN Feb23,2022, incorrect Lemma4.3.
Morales2608.05321 Aug5 scalar semidirect exponent/p condition excludes growing
ordinary dihedral N/2. Do not infer a general polynomial algorithm.

## Confirmed learning and edit-distance distinctions

On 11 September 2026 the user approved consolidating the mislabeled TCS-0023
source milestone into TCS-6543 (junta learning), with stable identity and source
provenance retained. The source's weaker growing-support challenge is distinct
from the canonical poly(n, 2^k, 1/epsilon) target. General distribution-free PAC
learning of DNF, TCS-5358, remains a separate question.

The user also requested (1+epsilon)-approximation of edit distance in
O(n^(2-delta_epsilon)) time for every fixed epsilon > 0, alongside TCS-6624's
constant-factor approximation in O(n polylog n) time. The accuracy and runtime
requirements differ; neither target should silently replace the other.
