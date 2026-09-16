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
