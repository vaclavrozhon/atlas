# Recovery and continuation — 16 September 2026

The user requested completion of all remaining active reviews after a computer
crash. The starting queue contained 644 completed reviews, 270 pending reviews
and one record outside the active scope.

The last completion, TCS-6659, survived in its canonical card and queue entry
with a matching SHA-256 hash. Its ledger entry was lost: the suffix of
reviews.jsonl consisted of 4,005 null bytes. The entry was reconstructed from
the card's saved quality review, status note and queue input hash. The original
ledger and reservations were copied to the ignored local recovery cache before
any change. An explicit recovery record was appended.

All 18 reservations from the stopped sessions were released after checking
their canonical input hashes and the surviving process/session evidence.
The detailed record is in [recovery.json](recovery.json). Relevant earlier user
scope choices were recovered into
[prior-user-decisions.json](prior-user-decisions.json). Their Czech wording is
preserved as quoted user input, not new project prose.

The individual authoring scripts in this directory retain the reviewed
statements, definitions, source scopes and completion notes. They use the shared
claim/hash/lock mechanism and are intended to run once per still-pending card.
Completed cards remain canonical in data/cards/; a newly resolved card is
moved intact through the normal archive workflow.

Completed in this continuation:

- TCS-6770: the approved uniform polynomial coefficient/length simulation
  question, with unrestricted memory.
- TCS-0805: the original sub-base-two exact counting question, completed and
  archived after reviewing Oka's August 2026 preprint.
- TCS-3075: the approved planar perfect matching sampling specialization,
  including the error and parallel computation model.
- TCS-4193: the approved randomized general-graph LOCAL lower-bound target.
- TCS-3381: the approved leaderless population protocol question, measured in
  the original quantified Presburger formula.
- TCS-6767: the approved sharp width-versus-length resolution target, with
  unrestricted refutations and the additive exponent loss quantified uniformly.
- TCS-0970: the approved sparse-vector Johnson–Lindenstrauss application target,
  with the independent short-seed objective removed.
- TCS-1022: the quantitative NEXP circuit-hardness consequence of promise
  derandomization, including its infinitely-often convention.
- TCS-5275: the historical resolution size-depth existence question, completed
  and archived after checking the published STOC 2025 theorem.
- TCS-1253: unrestricted Resolution over GF(2), with semantic weakening,
  exact line-count convention and the scope of the 2026 restricted lower bounds.
- TCS-1097: nonprovability of NP circuit upper bounds in the precise bounded
  arithmetic theory T2^1, including its axioms and circuit encoding.
- TCS-6525: the all-excluded-minors weighted GNRS conjecture and the scope of
  recent special-family results.
- TCS-6573: polynomial edge diameter of general pointed polyhedra, distinguishing
  the 2026 circuit upper bound and July coherent-monotone-path lower bound.
- TCS-7242: PL recognition of the four-sphere among closed combinatorial
  four-manifolds, including the exact finite input and undecidability alternative.
- TCS-0318: the full planar k-set function up to constant factors, with strict
  separation and the correct indexing of the known upper and lower bounds.
- TCS-0990: constant-factor planar Earth Mover Distance in one insertion pass
  and polylogarithmic bit space.
- TCS-6528: polynomial-time unknot recognition, retaining uncertain status
  while recording the unverified September 2026 preprint claim precisely.
- TCS-1125: constant-error, sub-log-squared seeds for standard-order width-four
  branching programs, distinguishing recent weighted-generator results.
- TCS-1133: constant-error, sub-log-squared seeds in every polynomial CNF/DNF
  size regime, with unrestricted variable reuse.
- TCS-1124: the exact dimension, alphabet and error dependence in optimal
  combinatorial-rectangle generators.
- TCS-1122: logarithmic-degree binary polynomial tests, with the user's
  explicit one-bit-saving and constant-error convention.
- TCS-0163 and TCS-0171: the approved merge into the NP-membership question
  for plain word equations; TCS-0171 is preserved intact in the archive.
- TCS-0071: nonuniform constant-depth proof systems for directed reachability,
  with exact range equality and the correct scope of known positive results.
- TCS-5114: existential polynomial-line Lovász–Schrijver simulation of
  Cutting Planes over real coefficients.
- TCS-6880: a constant-distortion cut-cone approximation with exact rational
  membership and strong separation in polynomial bit time.
- TCS-0834: the full four-parameter degree-distribution query function,
  with only the vertex count supplied to the algorithm.
- TCS-1588: the joint continuous chemical-reaction classification, with
  fixed arbitrary positive rate constants and the exact source output classes.
- TCS-2753: the historical fault-adaptive binary Byzantine agreement question,
  completed and archived after matching published PODC 2026 Theorem 3.1.

The six scope answers received during this continuation are preserved in
[current-user-decisions.json](current-user-decisions.json). They authorize the
word-equation merge and settle the graph-query, directed-reachability,
Lovász–Schrijver, cut-cone and logarithmic-degree generator conventions.

For TCS-5275, the published Theorem 2.10 supplies a concrete witness with
k = 40, c = 20 and m = t^3: formula size O(t^33), variable count O(t^24),
short proof size O(t^172), a larger proof budget at least 2^(-60)t^180, and
required depth Omega(t^40). The published definitions, lifting theorem and
simulation lemma were read, together with the full preprint lifting proof.
The underlying compressed cops-and-robber lower bound was not independently
reconstructed. The source's separate conjecture about Cutting Planes is not
claimed resolved.

The coefficient-normalization card also received a typography repair after
an escaped-string error was detected. The authoring script was repaired, the
canonical output hash and ledger were updated under the review lock, and the
math check now rejects stray control characters before scanning formulas.

The recovery checkpoint was committed and pushed as cf61f9a4. The live site
was deployed through the normal publication workflow after the seventh review
(publication version 1ef14bec6efb5d099b6c). Later local completions remain
tracked by the queue and subsequent checkpoints.

The next source checkpoint was a4f99767, through the ninth completion.
After thirteen completions the queue has 657 completed records, 257 pending
records and one outside active scope. Of 1,019 active cards, 762 have completed
reviews and 257 remain pending. All completed output hashes match and every
ledger line parses. Local publication a084db123e413f01f387 and the formula check
passed on all 1,019 active cards and 32,252 expressions.

For TCS-0805, the review covered the complete new proof: the chain-partition
bound, forced profile decoding, aggregation by released count and deadline,
state enumeration, and polynomial bit lengths. Both exponential-base
inequalities were checked with exact integer/rational powers. The author
verifier passed for all 5,231 naturally labeled posets of orders one through
six, 100 random instances, and 120 targeted instances. These finite tests are
supporting evidence, not a substitute for the proof or a Lean formalization.
The source remains explicitly identified as a preprint.

The initial recovery checkpoint passed make check, the bundled KaTeX checks
on all active cards, and the desktop/mobile reader checks in tests/pages.cjs.
Each completion is validated and locally published. The live queue and
unfinished inventory remain authoritative; this checkpoint does not mark the
entire task complete.

After twenty-one completions the queue contains 665 completed records,
249 pending records and one outside active scope. Of 1,019 active cards,
770 have completed individual reviews. The offline publication checks and
desktop/mobile reader checks passed after completion twenty; the formula check
covered 32,518 expressions at that checkpoint. Local publication after
completion twenty-one is 3ce330c4c952990b9552.

After twenty-seven queue dispositions, including the word-equation duplicate,
the queue contains 671 completed records, 243 pending records and one outside
active scope. Of 1,018 active cards, 775 have completed individual reviews.
The formula check passed on all active cards and 32,748 expressions.
All six user scope choices received during recovery have now been applied.

After twenty-nine dispositions the queue contains 673 completed records,
241 pending records and one outside active scope. Of 1,017 active cards,
776 have completed individual reviews. The formula check passed with 32,788
expressions. Source checkpoint f12a0d73 covers the first twenty-seven
dispositions and was pushed. Its publication c63459973fda7453a902 passed
the offline checks and was deployed.

Other user work concurrently changed the reader and contribution service.
Those uncommitted source changes are not part of these editorial commits.
An isolated publication initially replaced the newer live frontend; the six
affected assets were immediately restored byte-for-byte from the preceding
deployment, retaining the new card data. The corrected deployment is
6f9a99dc41c90f8e162b32a05a7407833b7f23f8. Those frontend files also match
the shared working copy as checked on 16 September 2026.

After thirty-one dispositions the queue contains 675 completed records,
239 pending records and one outside active scope. Of 1,016 active cards,
777 have completed individual reviews. TCS-4763 now has the source's
disjunctive parallel-flow target and a checked 2026 status comparison.
TCS-5427 was an invalid extraction of a historical background sentence:
the same 2016 source announces and presents the multipass extension.
It was archived intact with an individual source-context review, without
inventing a replacement theorem or asserting an independent proof certification.
The formula check after the flow revision covered 32,842 expressions.
Local publication after the extraction disposition is f32f911c47c43a0f6a84.

The subsequent scope choices are recorded in pending-scope-choices.json.
Source checkpoint 3cad09e0 covers the first twenty-nine
dispositions and was pushed; the corresponding live publication is
157b4940117c617de4e8, deployment fdcc46bcd4b751ecda0334075f2ca3bc087b8180.

After thirty-six dispositions the queue contains 680 completed records,
234 pending records and one outside active scope. Of 1,014 active cards,
780 have completed individual reviews. The five additional scope answers
have all been applied: TCS-3384 asks for a polynomial-in-optimum graph matching;
TCS-5015 is archived intact after consolidation into TCS-1961;
TCS-4231 retains its historical threshold and is archived after source-proof
review; TCS-6380 keeps general-message MPC; TCS-6206 asks for the full
bandwidth-sensitive detection complexity within absolute constant factors.
The latest local publication is 0f4deb40d0da6d6998e9. All completed queue hashes
match their saved outputs and all review ledger lines parse.
Source checkpoint 51c2ef28 covers the first thirty-one dispositions and was
pushed; live deployment d4b225ce0036cfba2c6d44b8620b12fde7a02275 covers that
checkpoint with publication f32f911c47c43a0f6a84.

The thirty-seventh completion, TCS-6105, fixes the unconditional Mandelbrot
compact-set computability question, with all-precision Hausdorff approximation
and a checked conditional-result comparison through MFCS 2025. The queue is
now 681 completed, 233 pending and one outside active scope; 781 of 1,014
active cards are reviewed. Local publication is a3cc11a1ebe6f219d18a.
The offline checks passed through completion thirty-six, as did the formula
check on 32,966 expressions. A new source-scope choice for TCS-6692 is pending;
the original quantitative-security and newer black-box formulations are not
silently conflated.

After forty-one dispositions the queue contains 685 completed records,
229 pending records and one outside active scope. Of 1,014 active cards,
785 have completed individual reviews. TCS-5793 now states the uniform
learning-hardness to same-class PRF implication; TCS-0254 specifies algorithmic
network cut sufficiency; TCS-5010 keeps existential all-support private-randomness
coding; and TCS-2202 expands the source’s uniform polynomial-regime hardness
reduction. The Boolean-valued network classification explicitly permits a real
approximation within 1/100 under the benchmark acceptance policy.
All completed queue hashes match and every review ledger line parses.
The formula check passes on 33,189 expressions across all 1,014 active cards.
The additional unanswered source-scope choices are recorded in
[further-scope-choices.json](further-scope-choices.json); they remain pending.
Source checkpoint 71db88c7 and deployment 6f6ff83d41e7f58fd682b1f18ace31b87137a723
cover the first thirty-seven dispositions, with publication a3cc11a1ebe6f219d18a.

After forty-four dispositions the queue contains 688 completed records,
226 pending records and one outside active scope. Of 1,012 active cards,
786 have completed individual reviews. TCS-1059 now gives the constant-factor
width and direct-input-degree linearization conjecture. TCS-0220 is archived
after matching the 2021 external-information separation, and TCS-1540 is
archived after matching the COLT 2026 all-function noisy-query lower bound.
The formula check passes on 33,225 expressions. All completed output hashes
match, and the review ledger parses. Nine source-scope questions remain
pending in further-scope-choices.json.
Source checkpoint aeec4db9 and deployment
1b45ad6706fcc5392d483a8c149d001592384e07 cover the first forty-one
dispositions, with publication 918c39f76753ffdaed28.
Local publication after forty-four is edec3b5e07f009a8411c.

After forty-seven dispositions the queue contains 691 completed records,
223 pending records and one outside active scope. Of 1,012 active cards,
789 have completed individual reviews. TCS-0562 now fixes uniform
nondeterministic acceptance of UNSAT and the all-width exponent saving.
TCS-4771 specifies total-function adaptive RP-oracle communication, and
TCS-6710 specifies randomized interactive NOF disjointness in both parameters.
The formula check passes on 33,362 expressions; all completed hashes match
and the ledger parses. Eleven source-scope choices remain pending.
Source checkpoint 6e22a683 and deployment
ab965ecb723d54c039740a4da8b0cccdb174d1f2 cover the first forty-four
dispositions with publication edec3b5e07f009a8411c.
Local publication after forty-seven is 35d3b83c975c97770175.

After forty-nine dispositions the queue contains 693 completed records,
221 pending records and one outside active scope. Of 1,012 active cards,
791 have completed individual reviews. TCS-6945 fixes the signed-integer
Exact-Weight k-Clique hypothesis and its word-RAM model; TCS-0854 expands
the Promise-ZPP to Promise-BPP derandomization implication into explicit
promise pairs and simulation quantifiers. All completed hashes match and
all 851 ledger entries parse. Eleven scope choices remain pending.
Source checkpoint 2aa0441b and deployment
b243fad707c17590458cd5bf9675d5d7ab924fc4 cover the first forty-seven
dispositions with publication 35d3b83c975c97770175.
Local publication after forty-nine is cd09bba08a3bd4155a32.

After fifty-three dispositions the queue contains 697 completed records,
217 pending records and one outside active scope. Of 1,012 active cards,
795 have completed individual reviews. TCS-1137 now specifies the complete
almost-all-inputs hardness converse; TCS-1956 preserves the nonuniform,
signed-advantage demi-bit to super-bit implication; TCS-6693 preserves mildly
explicit AC0[2] generators; and TCS-6689 restores indexed explicitness for
simultaneously optimal averaging samplers. All completed hashes match and
all 855 ledger entries parse. Eleven scope choices remain pending.
Source checkpoint b96622e2 and deployment
2dd347c99a3703f8f1fdaf641c1c3b657c1dbcb7 cover the first forty-nine
dispositions with publication cd09bba08a3bd4155a32.
Local publication after fifty-three is bfb4557fcc711396a6ac.
After fifty-five dispositions the queue contains 699 completed records,
215 pending records and one outside active scope. Of 1,012 active cards,
797 have completed individual reviews. TCS-6728 specifies deterministic
base-two-time chromatic number computation with polynomial space; TCS-6749
specifies a deterministic polynomial-time, polynomial-size clause-deletion
Almost 2-SAT kernel. Recent results for both were checked against the full
simultaneous resource requirements. All completed hashes match and all
857 ledger entries parse. The formula check passes on 33,699 expressions.
Thirteen source-scope choices are pending.
Source checkpoint c8a596e2 and deployment
0639bedd42a7920ee5c149f9e931321a94305c94 cover the first fifty-three
dispositions with publication bfb4557fcc711396a6ac.
Local publication after fifty-five is 6dfe9dd8633d08522505.

The fifty-sixth disposition, TCS-6731, records strictness at every positive
adjacent level of the W-hierarchy, with explicit weighted-circuit and reduction
definitions. Its later oracle evidence is distinguished from the unrelativized
question. The queue is now 700 completed, 214 pending and one outside active
scope; 798 of 1,012 active cards are reviewed. All completed hashes match,
all 859 ledger lines parse, and the formula check passes on 33,760 expressions.
The complete offline check passed through disposition fifty-five. The final
source-locator correction gives publication 6563b8c237e4314a5c87.

After sixty dispositions the queue contains 704 completed records,
210 pending records and one outside active scope. Of 1,011 active cards,
801 have completed individual reviews. TCS-0800 fixes exact general-graph
cutwidth below exponential base two; TCS-6591 specifies the weighted
constant-factor approximation target on arbitrary digraphs; TCS-7033 is
consolidated into the equivalent existing kernel question TCS-6379; and
TCS-7027 restores edge deletion in the perfect-graph FPT question.
The duplicate's original JSON is archived intact. Seventeen source-scope
choices are pending in further-scope-choices.json.

Source checkpoint f1b4dcb2 and deployment
f803e547462d2795c27de1b6b9ea094a6348a503 cover the first fifty-six
dispositions with publication 6563b8c237e4314a5c87.
The complete offline check passed through disposition fifty-nine, and the
formula check at that point covered 33,849 expressions.
Local publication after sixty is a7f79e61e65e9a16b321.

After sixty-four dispositions the queue contains 708 completed records,
206 pending records and one outside active scope. Of 1,011 active cards,
805 have completed this individual completion standard; the publisher's
broader "detailed" count is 897 and is not the completion count.
TCS-6615 specifies Cayley-table group isomorphism in polynomial bit time
and retains uncertain status because of a separately identified unverified
claim. TCS-6655 fixes the d-dependent quadratic Cereceda conjecture at
d+2 colors. TCS-6078 states NP membership for ordinary infinite pinwheel
packing and records the April 2026 NP-hardness advance. TCS-1115 specifies
exact EF1 and integral Pareto optimality for arbitrary additive rational
goods valuations in polynomial bit time.

All completed hashes match, all 868 ledger entries parse, and the formula
check passes on 34,062 expressions. The full offline check and desktop/mobile
page checks pass through disposition sixty-four. Seventeen source-scope
choices remain pending. Publication is 7918bf8c84d8a0313660.
Source checkpoint e2371c78 and deployment
2ea3c9b4ef05af10826bc0e432f26a2251fa3a96 cover the first sixty dispositions.

After sixty-eight dispositions the queue contains 712 completed records,
202 pending records and one outside active scope. Of 1,011 active cards,
809 have completed this individual completion standard. TCS-0935 preserves
polynomial-time unit-job scheduling for every fixed machine count; TCS-7250
retains the full Barnette conjecture; TCS-7249 fixes the exact repeated
six-matching multigraph cover; and TCS-7253 preserves uncertain status for
the unverified full-proof claim about second neighborhoods. Its stronger
matching variant has a separate counterexample and is not the card's target.

All completed hashes match, all 873 ledger entries parse, and the formula
check passes on 34,174 expressions. The full offline and desktop/mobile
checks last passed at disposition sixty-four. Eighteen source-scope choices
are now pending; review_positional_scope.md records why the 2026 randomized
equilibrium theorem does not settle TCS-0571's original pure-strategy question.
Publication is 6b5ac04f34e87e46eaed.
Source checkpoint 31c86cbb and deployment
e360eeb75e1f35fb1550bbcd013ce5479a8a722c cover the first sixty-four dispositions.

After seventy-two dispositions the queue contains 716 completed records,
198 pending records and one outside active scope. Of 1,011 active cards,
813 have completed this individual completion standard. TCS-6649 specifies
formal provability of omega-jump closure from full Hindman over RCA0 and
records the July 2026 one-application limitation without treating it as a
separation of theories. TCS-6614 fixes unconditional uniform deterministic
finite-field factorization in polynomial bit time. TCS-6642 preserves uniform
one-relator conjugacy decidability, and TCS-6654 preserves plain vertex-set
MSO decidability implying bounded clique-width.

All completed hashes match, all 877 ledger entries parse, and the formula
check passes on 34,239 expressions. The full offline check and desktop/mobile
page checks pass through disposition seventy-two. Eighteen source-scope
choices remain pending. Publication is 3378b2a224eba38d5536.
Source checkpoint 085c5a3b and deployment
bf8f5188f8c04bfca925c4b78392efb69f62d22c cover the first sixty-eight dispositions.

After eighty dispositions the original queue contains 724 completed records,
190 pending records and one outside active scope. This batch completes
TCS-6640 (constant additive bin packing), TCS-6619 (single-exponential-time
polynomial-space exact SVP), TCS-6627 (explicit dynamic matching),
TCS-6645 (effective CQ classifier), TCS-0571 (pure all-reachability equilibrium)
and TCS-0801 (the user-selected existential base below two). TCS-0784 is
archived with its explicit NP-not-in-coNP/poly assumption and TCS-7352 as
the known unrestricted approximation target, both at the user's request.

All eighteen pending scope questions were answered explicitly and saved;
four are applied and fourteen are selected pending application. There are
no unanswered scope questions in further-scope-choices.json. The formula
check passes on 34,391 expressions and desktop/mobile page checks pass
on publication 64e25e70a007a0c209e4. The full offline check also passes
through disposition eighty.

The shared checkout also contains another thread's authorized archival of
TCS-2470, TCS-4193 and TCS-6125, plus seven newly created TCS+ cards,
TCS-7377 through TCS-7383. These are separate from this recovery batch.
The two completed queue entries moved by that archive have identical
content hashes; their working-tree output paths have been reconciled.
The currently published 1,013 active cards and 903 detailed records are
not the individual-completion count. All completed queue hashes match
and all 889 ledger lines parse in the shared checkout.
Source checkpoint 2b41f9f6 and deployment
7428909a44ba25f43873eb5b43a69a9dfc3572d4 cover the first seventy-two dispositions.

After eighty-five dispositions, the shared queue contains 730 completed
records, 184 pending records and one outside active scope. Five further
reviews apply the user's choices: TCS-6949 (NC-SETH), TCS-6942 (the same
logarithmic-dimension OV and Hitting Set hypotheses as the individual cards),
TCS-1008 (infinite fully explicit additive-loss expander families), TCS-5202
(the universal quantitative quantum-extractor bound), and TCS-0540
(near-linear-bit maximum flow with local outputs). A finite-input address
correction in TCS-6599 leaves its asymptotic hypothesis unchanged. TCS-5202's
open-problems locator and summary parentheses were corrected during review.

The other thread completed TCS-7376 independently, accounting for the sixth
queue completion since the preceding checkpoint. Its card and queue entry,
the three archival moves, seven new cards and reader changes remain outside
this source commit. The shared checkout has 1,013 active cards and 909
detailed publisher records; neither count is the individual-review count.
All completed queue hashes match, and all 897 ledger lines parse.

Nine of the eighteen scope selections are now applied. TCS-6692 retains the
chosen quantitative security goal, with one further question pending about
whether the generator may depend on the requested security/error parameters;
the source ambiguity and inspected definitions are recorded in
review_quantitative_prg.md. The other eight selections await application.
The full offline check passes through disposition eighty-four.
The formula check passes on 34,641 expressions and desktop/mobile page
checks pass through disposition eighty-five, publication 734dfd3d3625b0fb8f87.
Source checkpoint be8bb503 and deployment
2aab7ced904b07267b66505b9285f0a0356a1a50 cover the first eighty dispositions.

After ninety dispositions, the shared queue contains 735 completed records,
179 pending records and one outside active scope. This batch applies five more
user selections: TCS-0053 is archived because the unrestricted-growth computable
degree bound follows from a published decidability theorem; TCS-4991 specifies
a universal polynomial EPR-pair budget; TCS-2707 specifies the tensor-product
perturbation inside the exponential; TCS-0218 asks for the full cryptogenography
success function; and TCS-0279 specifies infinite-oracle extraction with a
two-thirds probability threshold and logarithmic losses. The last card retains
uncertain status because only the abstract of a related August 2026 claim was
accessible. Its title was then adjusted to the required noun-phrase convention.

Fourteen of the eighteen selections are applied. Three secondary scope
questions are pending: TCS-6692's security/error parameter dependence,
TCS-4734's local-dimension growth, and TCS-0240's Hamming-pair complexity
restriction. TCS-6871 remains selected pending application. The existing
choices themselves are preserved; no earlier selection is being asked again.

All completed hashes match. All 904 ledger lines parse after the title-only
amendment. The full offline check passes through disposition eighty-eight;
the formula check passes on 34,813 expressions through disposition ninety.
Desktop/mobile page checks pass through ninety before the title-only change.
The resulting publication is c855bb588a2c1f98d444, with 1,012 active cards and
913 detailed publisher records, which are not the original-queue completion
count. Another thread's TCS-7376 completion, three archive moves, seven new
cards and reader changes remain outside this recovery source checkpoint.
Source checkpoint 507b2e25 and deployment
247733db639299d95849daf7cde03cbe1009445f cover the first eighty-five dispositions.

After ninety-five dispositions, the shared queue contains 740 completed records,
174 pending records and one outside active scope. This batch completes
TCS-6871 (the selected sole GapSVP foundation with a quantum reduction),
TCS-4734 (one locality-preserving amplification step with constant output
local dimension), TCS-6692 (the selected quantitative linear-seed PRG,
permitted to depend on security and error), TCS-6633 (polynomial worst-case
queries for exact complete envy-free cake cutting), and TCS-6551 (classical
unleveled FHE from the retained ordinary polynomial-modulus LWE assumption).

All three follow-up choices have been explicitly answered and saved.
Seventeen of the eighteen scope selections are applied. TCS-0240 retains
Hamming-distance pairs of nearly maximal complexity and maximal-length keys;
its further precision choice is pending, between a normalized asymptotic rate
within 1/100 and a finite-length communication cost within O(log n).
The accidental pasted TCS-6624 request was withdrawn by the user and did not
trigger a new mathematical review.

Other work archived TCS-5706 and TCS-7235 and adjusted only contextual
comparisons and related links in TCS-6624 and TCS-7220. Their queue paths
and hashes have been reconciled in the shared checkout, with explicit ledger
entries and no change to their mathematical targets. These changes, the
previous other-thread archive moves, TCS-7376 completion, seven new cards
and reader/service changes remain outside this recovery source commit.
Shared-file staging starts from HEAD and applies only this batch's five
individual completion records; the worktree keeps the other threads' entries.

All completed output hashes match and all 914 ledger lines parse. The full
offline check passes through disposition ninety-three. The formula check
passes on all 1,010 active cards and 34,899 expressions, and desktop/mobile
reader checks pass through disposition ninety-five. Local publication is
f4d4fc0c178879215cbd. The publisher's 914 detailed records are not the original
queue's individual-completion count. Source checkpoint 97ead183 and deployment
8e0ef1f07264cbaf12b2f8a2e84f20f91a77e3a6 cover the first ninety dispositions.

After one hundred recovery dispositions, the shared queue contains 745 completed
records, 169 pending records and one outside active scope. The five new reviews
are TCS-6589 (the universal metric-TSP subtour-LP integrality gap within 1/100),
TCS-6597 (the asymptotic clique exponent relative to the matrix-multiplication
exponent), TCS-6581 (the strong Mansour Fourier-concentration conjecture),
TCS-6608 (exact decidability of unconditional entropy inequalities), and
TCS-6552 (reusable adaptive NIZK arguments from ordinary one-way functions).
The distinction between unrestricted targets and restricted, conditional or
reverse-direction results is recorded in each individual review. Their existing
importance assessments are preserved. TCS-0240's communication-precision choice
remains pending; all previously answered scope choices remain saved.

All completed output hashes match and all 919 ledger lines parse. The full
offline check, formula check on 34,943 expressions and desktop/mobile reader
checks pass through disposition one hundred. The local publication is
3ca070208168265cfaa2, containing 1,010 active cards and 914 detailed publisher
records; these publisher totals are not individual completion counts.
The source commit stages only this batch's five card reviews and their queue,
ledger and inventory changes. Other-thread completions, archives, additions
and reader/service edits remain in the shared worktree outside this commit.
Source checkpoint 75dbca89 and deployment
9eb087286c2c4031a57c7f82f18658eb92dee8be cover the first ninety-five dispositions.

After one hundred and five recovery dispositions, the shared queue contains
750 completed records, 164 pending records and one outside active scope.
This batch completes TCS-6548 (unrestricted CPA-to-CCA2 public-key encryption),
TCS-6546 (full-domain one-way permutations from one-way functions), TCS-6539
(an almost-linear triangle detector), TCS-7356 (the unconditional algorithmic
metric-TSP approximation threshold), and TCS-0240 (the Hamming-family secret-key
communication-rate curve). TCS-6539 retains uncertain status: the directly
relevant 2025 sketching claim was examined, including a specific discrepancy
in its repetition probability estimate, without treating that limited audit
as a complete refutation or verification.

All eighteen saved scope selections are now applied. The user explicitly
selected TCS-0240's asymptotic communication rate in bits per input bit, with
pointwise absolute accuracy 1/100. Its formalization makes the logarithmic
complexity deficiency and key/secrecy losses explicit, uses worst-case
communication, and requires success separately for every promised input pair.
The accidental TCS-6624 paste remains withdrawn.

All completed output hashes match. The ledger has 925 valid entries, including
a title-only correction to TCS-7356's hardness reference. The offline check
passes through disposition 105 before that reference-title correction; the
publisher validates the corrected record. The math check passes on 35,084
expressions across 1,010 active cards, and desktop/mobile reader checks pass
on the corrected publication 1d0b51ccb6fd299289ac. There are 915 detailed
publisher records; this is not the individual-completion count.

Only this batch's five reviews, their authoring scripts, the scope-choice
update and their own queue/ledger/inventory changes enter the source commit.
Other-thread completions, archives, additions and reader/service changes
remain in the shared worktree. Source checkpoint 50301dbd and deployment
1aac8ce538948e9605fc75004ac46ffb6df53bc5 cover the first one hundred dispositions.

After one hundred and ten recovery dispositions, the shared queue contains
755 completed records, 159 pending records and one outside active scope.
This batch completes TCS-6453 (the classical Pessiland implication to
infinitely-often one-way functions), TCS-7346 (strongly polynomial sub-mn
maximum flow), TCS-7349 (almost-linear-work, subpolynomial-depth exact parallel
maximum flow), TCS-7341 (near-linear signed-real single-source shortest paths),
and TCS-7338 (the charged word-RAM multiphase conjecture).

The source reviews distinguish the revised June 2026 Pessiland statements,
the numerical dependence retained in the September 2026 integer-weight
shortest-path preprint, and the predicate and asymptotic scope of recent
multiphase Inner Product results. None of these checks is recorded as an
independent audit of the entire new proof. All eighteen saved user selections
remain applied, and the accidental TCS-6624 paste remains withdrawn.

All completed output hashes match, and the ledger has 930 valid entries.
The offline check passes through disposition 110, the math check passes on
35,231 expressions across 1,010 active cards, and desktop/mobile reader checks
pass on publication c66723d83af65f4597f4. The publisher's 915 detailed records
are separate from the individual-completion count.

Only these five reviews, their authoring scripts and their own queue, ledger
and inventory changes enter the source commit. Other-thread changes remain
in the shared worktree. Source checkpoint 5fd484df and deployment
f9e8e8379abbd1e35e69554dfa0dc0cde5664f13 cover the first 105 dispositions.

After one hundred and fifteen recovery dispositions, the shared queue contains
760 completed records, 154 pending records and one outside active scope.
This batch completes TCS-7331 (uniform deterministic dynamic dictionaries),
TCS-7281 (unconditional Max-Cut hardness at the Goemans–Williamson threshold),
TCS-6503 (online Boolean matrix–vector multiplication), TCS-7241 (FPT
approximation of twin-width), and TCS-7264 (deterministic single-exponential
integer-programming feasibility).

The source checks distinguish randomized from deterministic integer-programming
bounds and retain the determinant factor in the September 2026 preprint.
Special graph classes, stronger structural parameters, and cell-probe models
with free computation are not treated as solutions to the unrestricted targets.
All eighteen saved user selections remain applied.

All completed output hashes match, and the ledger has 936 valid entries.
The offline check passes through disposition 115, the math check passes on
35,282 expressions across 1,009 active cards, and desktop/mobile reader checks
pass on publication a2c71b0ba4d1d2d31a0a. The publisher has 914 detailed records.
The reader test now selects its sample card from the current Top 100 export;
its old hardcoded card was archived in another thread. This preserves the
direct-link, contribution-draft and publication-deletion checks after archives.

Only these five reviews, their authoring scripts, their own queue, ledger and
inventory changes, and the small reader-test fixture repair enter the source
commit. Other-thread changes remain in the shared worktree, including the
byte-preserving archive-path reconciliation for TCS-6575. Source checkpoint
f3414c56 and deployment 8550d7254e86da076331a62278737c62820311f0 cover the
first 110 dispositions.

After one hundred and twenty recovery dispositions, the shared queue contains
765 completed records, 149 pending records and one outside active scope.
This batch completes TCS-7266 (constant-factor uniform sparsest cut), TCS-7268
(the sliding-scale PCP endpoint), TCS-7252 (Tuza's exact factor-two conjecture),
TCS-7313 (the deterministic ETH-to-Gap-ETH implication), and TCS-6500
(Erdős's girth conjecture for every fixed parameter).

Tuza's card follows the 17 September MANIFEST/RULES preference for exact sharp
conjectures. The September preprint's stated factor 165/59 is progress toward
two, not a resolution; its advertised Lean formalization was not executed.
The other reviews distinguish polynomially many PCP alphabet symbols from
constant bit queries, the positive exponential rate from weaker PCP
consequences, and all short cycles from one forbidden cycle length.
All eighteen saved user selections remain applied.

The five new output hashes match their queue records; the shared ledger has
942 valid entries at this checkpoint. Other-thread edits to ten previously
completed cards remain outside this batch and are not globally reconciled by
this review. The offline check passes through disposition 120, the math check
passes on 35,359 expressions across 1,007 active cards, and desktop/mobile
reader checks pass on publication 27c9a62ef400ed4bc35a. The publisher has 912
detailed records. A display-math spacing correction for TCS-7313 has its own
ledger entry and is included with the batch.

Only these five reviews, their authoring scripts and their own queue, ledger
and inventory changes enter the source commit. Other-thread work remains in
the shared worktree. Source checkpoint a3ee6ddb and deployment
c949398d709c114bee76104d418ec3f50b522572 cover the first 115 dispositions.

After one hundred and twenty-five recovery dispositions, the shared queue
contains 770 completed records, 144 pending records and one outside active
scope. This batch completes TCS-7359 (static public-key quantum money from
plain LWE), TCS-7254 (Neumann–Lara's two-colour conjecture), TCS-0492
(conjunctive-query containment under bag semantics), TCS-1020 (constant-query
polynomial-length binary locally decodable codes), and TCS-6511
(deterministic Exact Matching on general graphs).

The source checks distinguish public verification with reusable notes from
time-dependent or extra-assumption money schemes, bag containment from
equivalence and unions, and unrestricted LDCs from relaxed or restricted
code constructions. The August Exact Matching revision remains randomized;
the bipartite preprint's formalization has explicit structural hypotheses
and was not executed or independently certified by this review.

The five new output hashes match their queue records; the ledger has 947
valid entries at this checkpoint. Other-thread edits to ten completed cards
remain outside this batch and are not globally reconciled here. The offline
check passes through disposition 125, the math check passes on 35,479
expressions across 1,007 active cards, and desktop/mobile reader checks pass
on publication f42701935d8a6fb8f32d. The publisher has 913 detailed records.

Only these five reviews, their authoring scripts and their own queue, ledger
and inventory changes enter the source commit. Other-thread work remains
in the shared worktree. Source checkpoint fbbe2c81 and deployment
c8ec014f72f94baaffbfefc1b9d154de5cd763fc cover the first 120 dispositions.

After one hundred and thirty recovery dispositions, the shared queue contains
775 completed records, 139 pending records and one outside active scope.
This batch completes TCS-7371 (almost-linear constant-factor LCS), TCS-7332
(logarithmic Las Vegas dynamic connectivity), TCS-7343 (deterministic
almost-linear vertex connectivity), TCS-7353 (the unrestricted Euclidean
k-means approximation constant), and TCS-7347 (directed unweighted APSP
with a fixed exponent improvement below five-halves).

The reviews preserve the distinction between one almost-linear algorithm and
a family with fixed exponent slack, expected amortized updates and expected
worst-case updates, and exact deterministic connectivity and parameterized
or randomized bounds. The k-means card retains determination of the full
constant; the July improvement is not automatically promoted to a new barrier.
The APSP card retains any fixed positive exponent saving and records the
assumptions of the 2026 equivalences separately.

The five output hashes match their queue records; the shared ledger has 952
valid entries. Other-thread hash changes remain outside this batch. The
offline check passes through disposition 130, the math check passes on 35,567
expressions across 1,007 active cards, and desktop/mobile reader checks pass
on publication 3043f344400fa1c17c97. The publisher has 913 detailed records.

Only these five reviews, their authoring scripts and their own queue, ledger
and inventory changes enter the source commit. Other-thread work remains
in the shared worktree. Source checkpoint 32e231f4 and deployment
8fe0f1182fd94153d40e6e924a5b62ed0275657d cover the first 125 dispositions.

After one hundred and thirty-five recovery dispositions, the raw shared queue
contains 780 completed records, 134 pending records and one outside its original
active scope. Concurrent category pruning has since archived seven still-pending
rows: the live queue tool reports 127 pending active reviews, 702 completed active
queue records and 152 active records outside the queue, for 981 active cards.
These are different counters; neither publisher detail nor prior completion
implies that a record remains active.

This batch completes TCS-7342 (Steiner shortcuts with unrestricted auxiliary
vertices), TCS-7348 (single-exponential exact cut mimicking networks), TCS-7354
(the metric k-means approximation infimum), TCS-1012 (explicit binary
list-decoding capacity), and TCS-7362 (compact optimal top-k document retrieval).
The coding review explicitly corrects the source's reversed capacity inequality
and the inherited title. The indexing review distinguishes full query guarantees
from CSA-relative, long-pattern and unsorted-output results. The metric clustering
card preserves its full numerical target and exact center budget.

The five output hashes match their queue records; the ledger has 957 valid
entries. Other-thread changes and archival decisions remain outside this source
batch. The offline check passes, the math check passes on 34,828 expressions
across 981 active cards, and desktop/mobile reader checks pass on publication
ddb9838382f431eaf37a. The publisher has 895 detailed records. The changed active
and detailed totals reflect concurrent pruning, not lost completed reviews.

Only these five reviews, their authoring scripts and their own queue, ledger
and inventory changes enter the source commit. Source checkpoint 0eb905ed and
deployment 7ef629b6248d5b2d0d18ff7a537755e3e485d39f cover the first 130
dispositions. Unrelated category, website and archival edits remain in the shared
worktree.

After one hundred and forty recovery dispositions, the raw shared queue contains
785 completed records, 129 pending records and one outside its original active
scope. The live queue reports 122 pending active reviews, 707 completed active
queue records and 152 active records outside the queue, for 981 active cards.
Seven raw pending rows were archived by concurrent category work.

This batch completes TCS-7372 (linear-time implicit unit-Monge multiplication),
TCS-7367 (a fixed exponent improvement for exact Hamming distances), TCS-7374
(one almost-quadratic deterministic tree-edit algorithm), TCS-7364 (the optimal
binary-jumbled-index preprocessing exponent), and TCS-7375 (the specified
suffix-tree interface in run-linear total space). The reviews distinguish
sequential time from MPC rounds, exact distances from approximations, static
tree edit distance from dynamic conditional bounds, and total compressed space
from index space additional to a text oracle. The jumbled-index card retains
its full numerical target; the new upper bound is not automatically a barrier.

The five output hashes match their queue records; the ledger has 962 valid
entries. The offline check passes, the math check passes on 34,889 expressions
across 981 active cards, and desktop/mobile reader checks pass on publication
cc77a3df43f3435ea27b. The publisher has 895 detailed records.

The separate TCS-7366 research note records an outstanding user choice of query
time and the limits of the alphabet verification. It is not a completed review.
Only this batch's five reviews, authoring scripts, pending research note and own
queue, ledger and inventory changes enter the source checkpoint. Source
checkpoint 9f513f9a and deployment b9667df2acef02efa6e6bd6eed46d9a4503c2bc9
cover the first 135 dispositions. Unrelated edits remain in the shared worktree.

After one hundred and forty-five recovery dispositions, the raw shared queue has
790 completed records, 124 pending records and one outside its original active
scope. The live queue has 117 pending active reviews, 711 completed active queue
records and 152 active records outside the queue, for 980 active cards. Seven raw
pending rows were archived by concurrent category work.

This batch completes TCS-7370 (exact optimal DNA minimizer ordering), TCS-7368
(elastic-degenerate language intersection), TCS-6814 (the general job-shop FPT
approximation scheme), and TCS-7366 (the user-selected fast-query linear-space
mismatch index). It archives TCS-4637 as conditionally resolved under ETH. The
Steiner review distinguishes terminal count from solution size and pins the full
proof to the original preprint version. The scheduling review allows machine
revisits without making route length a hidden parameter. The mismatch choice
supersedes the outstanding choice recorded at checkpoint 140; its note now
records the applied decision and the remaining older-result verification limit.

All five output hashes match their queue records; the shared ledger has 968 valid
entries, including the archival event. The full offline check passes. Math checks pass on 35,007 expressions
across 980 active cards, and desktop/mobile reader checks pass on publication
88c4692158181ab20ea8. The publisher has 896 detailed records.

Only these five reviews, their scripts, the updated mismatch research note and
their own queue, ledger, inventory and archival changes enter this checkpoint.
Source checkpoint 4a986662 and deployment
11463d20ae6dcac4ebc67590868dbc5270b109c4 cover the first 140 dispositions.
Unrelated changes remain in the shared worktree.

After one hundred and fifty recovery dispositions, the raw shared queue contains
795 completed records, 119 pending records and one outside its original active
scope. The live queue has 112 pending active reviews, 716 completed active queue
records and 152 active records outside the queue, for 980 active cards. Seven raw
pending rows were archived by concurrent category work.

This batch completes TCS-6950 (the randomized SETH/APSP/3SUM disjunction),
TCS-6928 (a computable encoding linear in minimum attractor size, measured in
logarithmic words), TCS-6974 (a fixed exponential saving for unrestricted
Formula-SAT), TCS-0468 (linear-time self-referential LZ matching), and TCS-0466
(all-length certification of a supplied Karp–Rabin fingerprint). The attractor
and formula targets are announced editorial defaults after optional questions;
no user confirmation is claimed. The LZ review distinguishes grammar input and
the division-free lower-bound model. The fingerprint review distinguishes all
lengths from power-of-two and sampled-comparison verification.

The five output hashes match their queue records; the shared ledger has 973 valid
entries. The full offline check passes. Math checks pass on 35,178 expressions
across 980 active cards, and desktop/mobile reader checks pass on publication
f032744430512b737986. The publisher has 899 detailed records.

Only these five reviews, their authoring scripts and their own queue, ledger and
inventory changes enter this checkpoint. Source checkpoint 1860dc61 and deployment
a705c5e7898ecf8892d1f9fe25b3a48f65daa986 cover the first 145 dispositions.
Unrelated edits remain in the shared worktree.

After one hundred and fifty-five recovery dispositions, the raw shared queue has
800 completed records, 114 pending records and one outside its original active
scope. The live queue has 107 pending active reviews, 721 completed active queue
records and 152 active records outside the queue, for 980 active cards. Seven raw
pending rows were archived by concurrent category work.

This batch completes TCS-0470 (grammar access at the grammar bit-space scale),
TCS-6513 (constant approximation for minimum grammar size), TCS-6508 (the exact
linear splay-deque conjecture), TCS-7326 (worst-case logarithmic dynamic planar
extreme-point queries), and TCS-7328 (tight standard pairing-heap decrease-key
charges). The reviews distinguish bits from words, small-ratio hardness from
hardness of every constant, general competitiveness from deque optimality, and
amortized from worst-case updates. The pairing review explicitly forbids mixing
operation charges from different potential analyses and keeps the announced
standard-heap improvement separate from the published pure-heap proof.

All five output hashes match their queue records; the shared ledger has 978 valid
entries. The full offline check passes. Math checks pass on 35,301 expressions
across 980 active cards, and desktop/mobile reader checks pass on publication
a4ba5da0916ab681c020. The publisher has 899 detailed records.

Only these five reviews, their authoring scripts and their own queue, ledger and
inventory changes enter this checkpoint. Source checkpoint c47cf66d and deployment
a8652ea5c8e63573052d44b2487dc67bf977d179 cover the first 150 dispositions.
Unrelated edits remain in the shared worktree.


After one hundred and sixty recovery dispositions, the raw shared queue contains
805 completed records, 109 pending records and one outside its original active
scope. The live queue has 102 pending active reviews, 725 completed active queue
records and 152 active records outside the queue, for 979 active cards. Seven raw
pending rows were archived by concurrent category work.

This batch completes TCS-7344 (exact almost-linear global directed edge cuts),
TCS-7345 (exact almost-linear directed vertex connectivity), TCS-7223 (linear-size
nonuniform multiplication circuits), TCS-7270 (fixed-density Circuit-SAT with a
fixed exponential saving), and TCS-0734 (the selected Set Cover inapproximability
question). TCS-0734 is archived as conditionally resolved by a parameter
consequence of the explicit gap construction in the same-day Guruswami–Ren ECCC
revision. The supporting note checks the universe-size convention and the
completeness-parameter divisor; it does not certify the sharper headline ratio
or a Lean formalization. The cut reviews separate exact computation from
inverse-precision approximation costs. The Circuit-SAT review repairs the
source attribution while retaining the previously selected stronger target.

The user explicitly confirmed the existing TCS-6928 and TCS-6974 formulations
and selected the Set Cover question for TCS-0734. The confirmations are saved in
[current-user-decisions.json](current-user-decisions.json); the earlier account
of the two editorial defaults remains an accurate record of their completion
before those replies arrived. No mathematical amendment to them was necessary.

All five output hashes match their queue records; the shared ledger has 984 valid
entries, including the archival event. The full offline check passes. Math checks
pass on 35,378 expressions
across 979 active cards, and desktop/mobile reader checks pass on publication
2bd22b1363ef3b81a57b. The publisher has 899 detailed records.

Only these five reviews, their authoring scripts, the supporting Set Cover note,
the three saved user decisions, and their own queue, ledger, inventory and
archive changes enter this checkpoint. Source checkpoint 0d4a6321 and deployment
6d92053adcef81b34fb515c6431a7e045c35de3a cover the first 155 dispositions.
Unrelated edits remain in the shared worktree.


After one hundred and sixty-five recovery dispositions, the raw shared queue
contains 810 completed records, 104 pending records and one outside its original
active scope. The live queue has 97 pending active reviews, 730 completed active
queue records and 152 active records outside the queue, for 979 active cards.
Seven raw pending rows were archived by concurrent category work.

This batch completes TCS-0611 (deterministic bipartite Exact Matching), TCS-0474
(pointer-machine working-set heaps), TCS-0481 (single-pair tropical shortest-path
circuits), TCS-0482 (universal linear semiring-iteration convergence), and TCS-0478
(exact fully dynamic APSP with edge-capacity-sensitive updates). Exact Matching
keeps uncertain status because the recent claimed derandomization is not fully
verified here. Semiring convergence likewise remains uncertain because the
announced optimal-convergence paper has no theorem text in the inspected author
listings. The other reviews distinguish constant operation charges from
inverse-Ackermann or iterated-logarithmic overhead, single-pair from all-pairs
circuit lower bounds, and exact online distance maintenance from approximate
or planar offline results.

All five output hashes match their queue records; the shared ledger has 989
valid entries. The full offline check passes. Math checks pass on 35,470
expressions across 979 active cards,
and desktop/mobile reader checks pass on publication 8678fe573332fabc601a. The
publisher has 899 detailed records.

Only these five reviews, their authoring scripts and their own queue, ledger and
inventory changes enter this checkpoint. Source checkpoint 9deb6680 and deployment
266c7ecc32d6806b9c5bef469ed1ff8e1f6116f1 cover the first 160 dispositions.
Unrelated edits remain in the shared worktree.


After one hundred and seventy recovery dispositions, the raw shared queue
contains 815 completed records, 99 pending records and one outside its original
active scope. The live queue has 92 pending active reviews, 734 completed active
queue records and 152 active records outside the queue, for 978 active cards.
Seven raw pending rows were archived by concurrent category work.

This batch completes TCS-6882 (homogeneous versus unrestricted formulas),
TCS-6883 (semantic multilinear versus unrestricted circuits), TCS-6893 (a
multilinear VNP family lower bound), TCS-7269 (the full logarithmic growth scale
of permanent formula size), and TCS-6885 (literal constant-overhead full-Hessian
computation). The first three use complex coefficients. The user explicitly
confirmed that field choice for the first two after their announced default
was applied, and selected a VNP family for the third before completion. These
choices are saved in current-user-decisions.json. Semantic and syntactic
multilinearity, formulas and circuits, ordinary and weighted homogeneity,
and one lower-bound endpoint versus full scale determination remain distinct.

The current arXiv record revealed that the April 2026 claimed unconditional
multilinear rank-method barrier was withdrawn on 11 May because of a missing
conditional probability estimate. Its claim is not used as an established
result. The final May 2026 homogenization paper was read rather than relying
on the older preprint's now-stale factorization discussion.

TCS-6885 is archived with an explicit unconditional counterexample: the product
of n variables has a linear-size circuit but quadratically many distinct mixed
second derivatives, each requiring a different non-input gate. The supporting
note checks the argument even with free repeated output labels. The optional
choice of an output-sensitive replacement had no reply when the recommended
archival default was announced and applied; that different target was not
silently substituted. No completed Lean formalization is claimed.

All five output hashes match their queue records; the shared ledger has 996
valid entries, including an archival event and a correction of the Aaronson
section locator to section 6.5.2. The full offline check passes. Math checks
pass on 35,543 expressions across
978 active cards, and desktop/mobile reader checks pass on publication
4103e7b04f7c9b13c6df. The publisher has 902 detailed records.

Only these five reviews, their authoring scripts, the supporting Hessian note,
the saved user choices, and their own queue, ledger, inventory and archive
changes enter this checkpoint. Source checkpoint d3ea0ebc and deployment
69fa663067f26c42130a38b66fe4cc502f4a0e6c cover the first 165 dispositions.
Unrelated edits remain in the shared worktree.


After one hundred and seventy-five recovery dispositions, the raw shared queue
contains 820 completed records, 94 pending records and one outside its original
active scope. The live queue has 87 pending active reviews, 738 completed active
queue records and 152 active records outside the queue, for 977 active cards.
Seven raw pending rows were archived by concurrent category work.

This batch completes TCS-6903 (degree-sensitive deterministic noncommutative
PIT), TCS-6890 (an explicit noncommutative circuit lower-bound family),
TCS-6914 (the historical factoring-to-PIT reduction), TCS-3318 (degree-independent
p-th-root circuit closure), and TCS-1102 (positive-characteristic VBP factor
closure). Optional choices for the first, second, third and fourth were given
reasonable time during independent work and then their recommended editorial
defaults were announced and applied. They are not recorded as user confirmations.

The noncommutative lower-bound review incorporates the May 2026 quadratic
palindrome result and the July revision of the concurrent multiplication bound;
the January claim that the general frontier remained only n log n is not reused
as current. The September 2026 PIT preprint supplies a randomized restricted-depth
result, not deterministic PIT for arbitrary circuits. TCS-6914 is archived as
resolved by the Kopparty–Saraf–Shpilka reduction (2014/2015), with exact arithmetic
cost and the univariate factoring primitive explicit. The two positive-characteristic
closure cards distinguish degree-independent general circuits from degree-bounded
branching programs, existential closure from algorithms, formal polynomials from
finite-field functions, and same-field factors from field extensions.

All five output hashes match their queue records; the shared ledger has 1002
valid entries, including the archival event. The full offline check passes.
Math checks pass on 35,662 expressions
across 977 active cards, and desktop/mobile reader checks pass on publication
3fcfd5af5d92aa67959b. The publisher has 906 detailed records.

Only these five reviews, their authoring scripts and their own queue, ledger,
inventory and archive changes enter this checkpoint. Source checkpoint 23ec902c
and deployment 095fd1093763b1f63584355b779244a973fdba18 cover the first 170
dispositions. Unrelated edits remain in the shared worktree.


After one hundred and eighty recovery dispositions, the raw shared queue has
825 completed records, 89 pending records and one outside its original scope.
The live catalogue has 977 active cards: 82 pending active reviews, 743 completed
active queue records and 152 active records outside the queue. Seven raw pending
rows have been archived by concurrent category work.

This batch completes TCS-0010 (constant-degree unrestricted circuit lower bounds),
TCS-1058 (binary matrix rigidity), TCS-5260 (rigidity over small number fields),
TCS-0095 (uniform deterministic recurrence-term zero testing), and TCS-1151
(bounded-interval continuous zero testing over effective real fields).
The optional rational-coefficient, rigidity-quantifier and recurrence-uniformity
choices received no reply during independent work; the recommended defaults were
announced and applied as editorial choices, not recorded as user confirmations.

The circuit card retains a superlinear target without silently strengthening it
to a fixed power saving. Both rigidity cards specify their coefficient fields,
efficient exact output and all fixed constants in the near-linear rank scale.
The number-field card bounds the joint field degree, not just individual degrees.
The recurrence card distinguishes uniform input from hardcoded fixed sequences
and randomized circuit zero testing. The continuous card supplies the source's
effective-field definition and retains endpoint and tangential zeros; a conditional
algebraic-coefficient result does not resolve it. Relevant primary sources through
September 2026 were checked, including final SODA 2026 and MFCS 2026 papers.

All five output hashes match their queue records; the shared ledger has 1007 valid
entries. The full offline check passes, mathematical rendering passes for 35,820
expressions across 977 cards, and desktop/mobile reader checks pass on publication
518b8b7b9602ac985e12. There are 911 detailed records in the published catalogue.

Only these five reviews, their authoring scripts, this log, and their own queue,
ledger and inventory changes enter the checkpoint. Source checkpoint cb1e039a
and deployment 83bfd61f4b7d7b96107d10283c9b28818f0e9802 cover the first 175
dispositions. Unrelated shared-worktree changes remain unstaged.


After one hundred and eighty-five recovery dispositions, the raw shared queue
contains 830 completed records, 84 pending records and one outside its original
scope. The live queue has 77 pending active reviews, 748 completed active queue
records and 152 active records outside the queue, for 977 active cards.

This batch completes TCS-5921 (arbitrary integer 2 by 2 matrix semigroups),
TCS-4490 (binary-input matrix-power signs in every fixed dimension), TCS-1103
(presentable border VP in VNP), TCS-0046 (integer min-plus feasibility), and
TCS-0047 (exact Kronecker-polytope membership). The optional matrix-dimension
choice received no reply during independent work; its recommended per-dimension
polynomial-time interpretation was announced and applied as an editorial default.

The original 2025 Question 8 and its June 2026 revision both concern presentable
VP epsilon. TCS-1103's inherited ordinary-border label was therefore corrected,
with coefficient-generation cost and the defining paper's main-variable degree
bound made explicit. Matrix-power context retains the unary-matrix condition of
the dimension-three theorem. The semigroup card permits arbitrary mixtures of
singular and nonsingular integer generators; the 2024 structured-set theorems
do not resolve it. The two feasibility cards distinguish binary input length
from coefficient magnitude and inverse numerical tolerance, respectively.

All five hashes match their queue records; the shared review ledger has 1012
valid entries. The full offline check passes. Mathematical rendering passes on
35,932 expressions across 977 cards, and desktop/mobile reader checks pass on
publication 192e29ea925dd2ab317f, with 916 detailed records.

Only these five reviews, their authoring scripts, this log, and their own queue,
ledger and inventory changes enter the checkpoint. Source checkpoint a9375cb1
and deployment 4b847734ccb08339c959d0954a7a557bb127f669 cover the first 180
dispositions. Concurrent unrelated changes are left in the shared worktree.

After one hundred and ninety recovery dispositions, the raw shared queue contains
835 completed records, 79 pending records and one outside its original scope.
The live catalogue has 977 active cards: 72 pending active reviews, 753 completed
active queue records and 152 active records outside the queue.

This batch completes TCS-1544 (the uniform Cayley-table membership dichotomy),
TCS-1069 (real Zariski-adherence membership in existential real complexity),
TCS-5240 (multivariate-to-univariate hardness over F₂), TCS-7082 (the clique-free
domination candidate for a natural enumeration separation), and TCS-7084
(enumeration time–space separations under P ≠ NP). Optional target questions
received no replies during independent work; recommended editorial defaults were
announced and applied, without being recorded as user confirmations.

The semigroup review checks the expanded three-author revision of 14 September
2026, including its promise on the generated subsemigroup and uniform reductions.
The Zariski review keeps finite-bit explicit input and distinguishes Euclidean
closure. The hardness-transfer card fixes both explicitness scales and does not
misapply a characteristic-zero obstruction to a specific substitution. The two
enumeration cards finish earlier source reviews whose precise targets were still
pending. Their RAM arithmetic costs and memory conventions are explicit; the
WADS 2025 subclass algorithm and July 2026 regularization theorem are not claimed
to settle the broader chosen targets.

All five output hashes match their queue records; the shared ledger contains
1017 valid entries. The full offline check passes. Mathematical rendering passes
for 36,031 expressions across 977 active cards, and desktop/mobile reader checks
pass on publication ce9d5863a92eb2c1e6b2, with 921 detailed records.

Only these five reviews, their authoring scripts, this log and their own queue,
ledger and inventory changes enter the checkpoint. Source checkpoint 1eadde8c
and deployment 60e68887022cb9571e7132c6458c83f0f65d63b9 cover the first 185
dispositions. Concurrent unrelated work remains unstaged.

After one hundred and ninety-five recovery dispositions, the raw shared queue
contains 840 completed records, 74 pending records and one outside its original
scope. The live catalogue has 977 active cards: 67 pending active reviews,
758 completed active queue records and 152 active records outside the queue.

This batch completes TCS-0648 (constant-gap Euclidean unique-SVP), TCS-0656
(semiprime factoring to polynomial-factor GapSVP), TCS-0659 (a sublinear-factor
classical SIS reduction), TCS-0657 (the logarithmically improved coNP certificate
bound), and TCS-0655 (polynomial-factor Euclidean hardness under NP ⊄ RP).
Unanswered optional choices were announced and applied as editorial defaults,
not recorded as user confirmations.

The reviews specify binary inputs, lattice rank, promise boundaries, reduction
interfaces and error guarantees. The August 2026 polynomial-factor hardness
result applies to p > 2; its explicit Euclidean obstruction was checked. A
separate optional archival choice received no reply, and the recommended p = 2
specialization was retained. The September revision of the deterministic
hardness paper explicitly withdraws its older dimension-dependent claims;
those claims are not used. The coNP target requires deterministic certificates,
and the SIS target fixes ordinary compressing instances without auxiliary hints.

All five output hashes match their queue records; the shared ledger contains
1022 valid entries. The full offline check passes. Mathematical rendering passes
for 36,180 expressions across 977 active cards, and desktop/mobile reader checks
pass on publication 5dacd9c805fff7ffb66c, with 926 detailed records.

Only these five reviews, their authoring scripts, this log and their own queue,
ledger and inventory changes enter the checkpoint. Source checkpoint dd82be69
and deployment 55064d5a57511c36b382a44da60c78a513ecebe8 cover the first 190
dispositions. Concurrent unrelated work remains unstaged.

After two hundred recovery dispositions, the raw shared queue contains 845
completed records, 69 pending records and one outside its original scope. The
live catalogue has 976 active cards: 62 pending active reviews, 762 completed
active queue records and 152 active records outside the queue.

This batch completes TCS-6868 (the historical NTRU reduction request, archived
with a proved ratio-recovery specialization), TCS-0653 (the explicit quantum
Euclidean SVP lower bound from QSETH), TCS-6861 (classical same-dimension SIVP
to LWE), TCS-6864 (classical cyclotomic ideal-SVP to ring-LWE), and TCS-0205
(the normalized Ingleton-score infimum). Unanswered optional target choices were
announced and applied as editorial defaults, without recording user confirmation.

The NTRU record distinguishes changed distributions and ratio recovery from
standard ternary short-vector recovery, and does not import an ERH assumption
from the separate worst-case branch into the search-to-decision theorem. The
quantum card counts finite gates and classical control and retains the one-half
QSETH baseline; the ICALP 2026 nonadaptive reduction barrier is not treated as a
refutation. The LWE cards fix finite samples and oracle success guarantees. The
ring variant preserves the bounded elliptical family and the dual-ring scaling
rather than asserting fixed spherical-error hardness. The Ingleton review fixes
opposite sign conventions, separates a modified score and a distinct violation
index, and retains global two-sided numerical certification over all alphabets.

All five output hashes match their queue records, including the archived record;
the shared ledger contains 1028 valid entries. The full offline check passes.
Mathematical rendering passes for 36,350 expressions across 976 active cards,
and desktop/mobile reader checks pass on publication a9f63a22160cdf928565,
with 930 detailed active records.

Only these five reviews, their authoring scripts, this log, their queue/ledger/
inventory changes and the NTRU archival entries enter the checkpoint. Source
checkpoint d9b477e0 and deployment a96ebe93d2de3c6cfe7d210398d51eb820d0bdff
cover the first 195 dispositions. Concurrent unrelated work remains unstaged.

After two hundred and five recovery dispositions, the raw shared queue contains
850 completed records, 64 pending records and one outside its original scope.
The live catalogue has 975 active cards: 57 pending active reviews, 766 completed
active queue records and 152 active records outside the queue.

This batch completes TCS-0187 (characteristic sets of rank inequalities), TCS-0178
(bounded-alphabet approximation of the entropy face), TCS-4968 (a positive binary
rate advantage over linear codes), TCS-6738 (linear-length locally testable proofs),
and TCS-6739 (the resolved constant-alphabet three-query length separation,
archived). Unanswered optional choices were announced and applied as editorial
decisions, never as user confirmations.

The rank card records that its finite-or-cofinite specialization has uncertain
current status, rather than attributing that exact conjecture to the broad
seminar question. The entropy card fixes the visualization's beta convention,
uses normalized entropy rays and separates actual bounded-alphabet realizations
from transformed almost-entropic samples. The coding-rate card accepts any fixed
positive gap and checks the unchanged RANDOM 2026 LP bound. The proof card retains
Goldreich's stronger requirement to reject far proofs of true assertions; good
LTCs and ordinary PCPs do not settle it. The archived decoding card explicitly
allows whole-symbol adaptive queries and does not claim the binary bit-query
version resolved. The construction and the original arbitrary-alphabet lower
bound were checked, including their radius and recovery guarantees.

All five output hashes match their queue records, including the archived record;
the shared ledger contains 1034 valid entries. The full offline check passes.
Mathematical rendering passes for 36,470 expressions across 975 active cards,
and desktop/mobile reader checks pass on publication 6495d05840c0bdad861a,
with 934 detailed active records.

Only these five reviews, their authoring scripts, this log, their queue/ledger/
inventory changes and the RLDC archival entries enter the checkpoint. Source
checkpoint bbd56267 and deployment 0a1b28c581016f1cdc8f9b76cd61959315e2c82f
cover the first 200 dispositions. Concurrent unrelated work remains unstaged.

After two hundred and ten recovery dispositions, the raw shared queue contains
855 completed records, 59 pending records and one outside its original scope.
The live catalogue has 974 active cards: 52 pending active reviews, 770 completed
active queue records and 152 active records outside the queue.

This batch completes TCS-4802 (the constant-rate binary interactive error
threshold), TCS-5189 (factor-two hardness of circuit decision-tree depth),
TCS-0464 (finite-round OR information cost, archived as a known approximation),
TCS-4927 (strict intermediate quantum decision power) and TCS-2571 (the selected
ordinary-KW candidate characterization). Thirty received user scope confirmations
are recorded on already completed cards and in the audit ledger; they do not
increase the disposition count. The exact choices and identifiers are preserved
in record_user_scope_confirmations.py. The final three targets were explicitly
selected by the user before completion.

The interactive-code review replaces an obsolete 2/7 upper bound by the checked
13/47 shared-budget bound. The decision-tree card separates multiplicative from
known additive hardness. The OR card supplies a finite message-alphabet and
support-preserving probability-grid certificate, including an explicit entropy
error bound for every message count; archival does not claim an exact formula
or a Lean formalization. The quantum card fixes the single-output decision
interface and separates sampling, postselection and physical nonuniversality
from strict complexity-class containments. The KW card defines both mapping
reductions and quasipolynomial dimension growth, and marks the precise editorial
candidate's status uncertain rather than attributing it to the source.

The full offline check passes. Mathematical rendering passes for 36,639
expressions across 974 active cards, and desktop/mobile reader checks pass on
publication 12418926a040efa5d7b2, with 938 detailed active records. The shared
ledger has 1070 valid entries. All owned output hashes are checked before staging.

Only these five new reviews, thirty confirmation updates, their scripts, this
log, their queue/ledger/inventory changes and the OR archival entries enter the
checkpoint. Source checkpoint 71d0a884 and deployment
2a17a443d9c6e93e910781db8216e75e4006a3c3 cover the first 205 dispositions.
Concurrent unrelated work remains unstaged; the committed queue therefore has
854 completed and 60 pending records, while the live inventory additionally
reflects concurrent work and retirements.

After two hundred and fifteen recovery dispositions, the raw shared queue contains
860 completed records, 54 pending records and one outside its original scope.
The live catalogue has 972 active cards: 47 pending active reviews, 773 completed
active queue records and 152 active records outside the queue.

This batch completes TCS-0560 (logarithmic-dimension Hitting Set to 3SUM),
TCS-6946 (APSP to 3SUM), TCS-6025 (an easier unbounded-treewidth pattern class),
TCS-1024 (the conditionally resolved low-entropy samplable-extractor target,
archived), and TCS-0987 (the weaker RIP milestone, merged into TCS-6662 and
archived). All five target choices were explicitly confirmed by the user.
The first three confirmations were recorded after initial authoring and do not
increase the disposition count. The RIP target retains its stronger formulation.

The reductions count all adaptive oracle queries and preserve one source saving
across fixed dimension or weight exponents. The treewidth card distinguishes
uncolored Subgraph Isomorphism from partitioned lower bounds and the core-only
uncolored corollary. The extractor record states the exact E-versus-Sigma-5
oracle-circuit assumption and polynomial-error theorem; it does not claim the
separate negligible-error branch resolved. The June 2026 retraction of ECCC
2026/089 was checked and that preprint was not used as resolution evidence.
The RIP merge supplies an explicit rational rescaling showing that the existing
optimal-row target implies the imported weaker norm and row-count milestone.

The full offline check passes. Mathematical rendering passes for 36,759
expressions across 972 active cards, and desktop/mobile reader checks pass on
publication 898ce075bd5f1cbc3f71, with 941 detailed active records. The shared
ledger has 1080 valid entries. All six owned output hashes match their queue rows.

Only these five dispositions, the RIP target amendment, three confirmation
updates, their scripts, this log and their shared queue, ledger, inventory and
archival deltas enter the checkpoint. Source checkpoint 19003e22 and deployment
4a63ed7fc882bd1f5ca48975dbefea0ee34cc181 cover the first 210 dispositions.
Concurrent unrelated work remains unstaged; the committed queue therefore has
859 completed and 55 pending records.

After two hundred and twenty recovery dispositions, the raw shared queue contains
865 completed records, 49 pending records and one outside its original scope.
The live catalogue has 972 active cards: 42 pending active reviews, 778 completed
active queue records and 152 active records outside the queue.

This batch completes TCS-3958 (polynomial-stretch PRGs for superlinear-gate
threshold circuits), TCS-0597 (FPT coloring of induced-P5-free graphs), TCS-1945
(binary Nearest Codeword lower bounds for every constant factor from ETH),
TCS-4778 (the circuit-hardness implication for amplified relations), and TCS-2201
(the universal two-source extractor oracle conversion). All final scopes were
explicitly selected by the user. The last PRG answer supersedes an earlier
one-bit choice; two other choices were confirmed after initial authoring.

The PRG review found that the proposed one-bit milestone follows from known
average-case hardness, so the final card requires polynomial stretch. Its audit
retains both the initial proposal and the explicit correction. The coding review
checks the May 2026 some-factor result and preserves the paper's stated open
all-factor direction. The two general pseudorandomness implications mark their
precise editorial formulations uncertain, rather than attributing those exact
statements to broader source questions. The coloring bibliography distinguishes
the 2022 seminar from its May 2023 report publication and corrects the editor list.

All five output hashes match their queue rows. The shared ledger contains 1089
valid entries. The full offline check passes; mathematical rendering passes for
36,941 expressions across 972 cards. Desktop/mobile reader checks pass on
publication 26b85ef84a91194ad185 with 946 detailed active records.

Only these five cards, their authoring and correction scripts, the confirmation
updates, this log and the owned queue, ledger and inventory deltas enter the
checkpoint. Source checkpoint 621a4121 and deployment
b8d7b5171544714be2b4d032ffcbac7d8a800bf2 cover the first 215 dispositions.
Concurrent unrelated work remains unstaged; the committed queue has 864 completed
and 50 pending records.

After two hundred and twenty-five recovery dispositions, the raw shared queue
contains 870 completed records, 44 pending records and one outside its original
scope. The live catalogue has 970 active cards: 37 pending active reviews,
781 completed active queue records and 152 active records outside the queue.

This batch completes TCS-6309 (a true constant-factor capacitated k-median
approximation), TCS-2662 (subexponential constant-gap Clique under ordinary ETH),
TCS-5374 (the generalized DAG-treewidth homomorphism-counting dichotomy),
TCS-0088 (the known conditional Max Di-Cut ratio to the requested precision,
archived), and TCS-0711 (general adversarial contextual-bandit model selection,
archived following the 2021 negative result). The five optional scope questions
have not received answers; the announced recommendations are recorded as
editorial defaults, not user confirmations.

The clustering card preserves exact capacities and the number of facilities;
the ICALP 2026 source still identifies this polynomial-time target as open.
The Clique card distinguishes a graph-size exponent from a parameterized bound.
The counting card defines generalized reachability bags and both sides of the
proposed parameterized dichotomy. The Max Di-Cut record states its UGC and
NP-not-in-BPP assumptions and a certified interval narrower than 1/50; it does
not claim the exact optimum ratio known. The bandit record fixes the adaptive
adversary, feedback, comparator and parameter dependence covered by the cited
impossibility result. Archival records do not claim completed Lean proofs.

All five output hashes match their queue rows. The shared ledger contains 1096
valid entries. The full offline check passes; mathematical rendering passes for
37,071 expressions across 970 cards. Desktop/mobile reader checks pass on
publication bd23ceb5c185cf8275b2 with 949 detailed active records.

Only these five cards, their authoring scripts, this log and the owned queue,
ledger, inventory and archival deltas enter the checkpoint. Source checkpoint
742ebdc0 and deployment b9f0df73b654aa0d33042e265ea6d77ffabd3427 cover the first
220 dispositions. Concurrent unrelated work remains unstaged; the committed
queue has 869 completed and 45 pending records.
