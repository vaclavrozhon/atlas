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
