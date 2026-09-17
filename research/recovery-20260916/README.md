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
