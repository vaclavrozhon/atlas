# Exclusions, status traps and the next comparison pool

This accompanies [the fourteen recommendations](recommendations.md) and the
[complete source ledger](screening.csv). It records why apparently attractive
entries were not recommended. A deferred entry is not a judgment that its
mathematics is unimportant, nor a certification that it remains open.

## Resolutions and misleading old labels

| Source target | Finding and consequence |
| --- | --- |
| OpenTCS / RTA 90: context unification | [Jeż (2013)](https://arxiv.org/abs/1310.4367) proves PSPACE membership for the usual finite-signature model. The combined page also asks about linear second-order unification; that broader question must be checked separately. The user's example of stale context-unification status is correct. |
| RTA 94: higher-order matching | [Stirling (2009)](https://arxiv.org/abs/0907.3804) settles classical higher-order matching. The page additionally discusses many base atoms. Neither this variant nor beta-only matching should be silently conflated with the classical beta-eta theorem. |
| TOPP 51–52: planar queue-number / linear-volume grid drawings | These old targets are covered by the [2019 planar product-structure paper](https://arxiv.org/abs/1904.04791). The two list entries should not generate new open cards. |
| TOPP 67 / Garden: fair convex partitions | The [2018 equal-area/equal-perimeter theorem](https://arxiv.org/abs/1804.03057) supplies every prescribed number of parts. |
| Sublinear 38: polynomial partition oracles | The [2021 polynomial partition-oracle result](https://arxiv.org/abs/2102.00556) supersedes the collection's old quasipolynomial progress note. |
| Separability workshop 6–7: polynomial UFA separators and complements | [Göös–Kiefer–Yuan, revised 2022](https://arxiv.org/abs/2109.09155), refute both polynomial-size expectations. Their separation instance already consists of a language and its complement, so every separator must recognize that language. Register automata and infinite alphabets require a separate analysis. |
| Bonnet 5: polynomial chi-boundedness | [Bourneuf–Thomassé](https://arxiv.org/abs/2303.11231) prove it for bounded twin-width. This does not resolve computing a twin-width decomposition, recommendation R1. |
| Korhonen 1: independent set excluding a fixed grid as an induced minor | The [10 September 2026 Bonnet–Chang preprint](https://arxiv.org/abs/2609.11285) supplies a hardness counterexample; the author's list was updated to mark the question solved. This is a very recent preprint, not a proof checked by this review. |
| Korhonen 2–3: exact-treewidth ETH lower bound; dynamic treewidth | The author marks these solved, linking the [2024 lower bound](https://arxiv.org/abs/2406.11628) and [2025 dynamic result](https://arxiv.org/abs/2504.02790). Existing treewidth cards need statement-level comparison before any status update. |
| Garden / West: ordinary cycle double cover | July 2026 proof material has independent expositions by [Oum](https://arxiv.org/abs/2607.16356) and [Geelen](https://arxiv.org/abs/2607.15399). Do not recommend the ordinary conjecture as a fresh open question. This review did not verify the proof or its formalization. Strong five-cover and prescribed-cycle variants are separate. |
| Garden: Feige-type probability bound | [Fu et al. (July 2026)](https://arxiv.org/abs/2607.23980) settle the sharp extension for delta at least one; [Nie–Wei](https://arxiv.org/abs/2607.24528) address the classical conjecture. The Garden page quantifies over every positive delta. Its smaller-delta remainder must not be declared solved on this evidence. |
| Garden: Hedetniemi | [Shitov's counterexamples](https://arxiv.org/abs/1905.02167) refute the general product-coloring identity. |
| Garden: Goldberg–Seymour | [Chen–Jing–Zang](https://arxiv.org/abs/1901.10316) provide a proof of the edge-coloring conjecture. |
| Garden: Erdős–Faber–Lovász | [Kang et al.](https://arxiv.org/abs/2101.04698) prove the assertion for sufficiently large instances. Preserve that qualification when interpreting a page quantifying over every size. |
| cstheory: sensitivity versus block sensitivity | [Huang (2019)](https://arxiv.org/abs/1907.00847) resolves the sensitivity conjecture. |

The ledger additionally records older resolutions explicitly reported on TOPP,
sublinear.info, RTA, TLCA and Amarilli's pages. These rows say
`source_reports_solved`: they are not represented as new independent literature
audits. Where the page mixes resolved and residual questions, the disposition
is `partial_resolution`.

## Existing coverage to use instead of new cards

The new Marwaha collection does not yield a recommended addition: all thirteen
main questions have corresponding active or historical records. Examples are
QMA(2) versus BQEXP (TCS-0861), EFX (TCS-0011), acyclicity testing (TCS-0847),
and the EPR Hamiltonian (TCS-0858). Some of its other questions were deliberately
archived. Finding them on another collection does not supply a reason to restore
them.

OpenTCS similarly repeats many already indexed original questions. It is useful
for discovery, but is a secondary index with inherited status. Automata Exchange
largely repeats the Atlas's existing numbered source records. Archived copies
remain part of the comparison, even where the current reader no longer shows
them. TCS-0474 and the eight removed Wikipedia direction placeholders remain
excluded/reserved.

Several tempting renamed targets already have particularly clear homes:

| Candidate | Existing coverage / distinction |
| --- | --- |
| Exact clique-width computation | TCS-7181. Do not confuse it with R1, approximation of twin-width. |
| Planar treewidth complexity | TCS-0771. |
| Exact bipartite matching, deterministic polynomial time | TCS-0611. |
| Explicit superlinear Boolean circuit lower bounds | TCS-0015. R3 chooses a specific stable-compaction function. |
| Graph reconstruction / edge reconstruction | TCS-7216 / TCS-7217 respectively. Similarity retrieval initially prefers the wrong one for the vertex question, illustrating why name scores cannot certify duplicates. |
| List edge coloring | TCS-7218. |
| Reed's coloring bound / Erdős–Hajnal | TCS-6682 / TCS-6652. |
| Edge unfolding / universal planar point sets | TCS-0406 / TCS-0377. |
| Log-rank / protocol partition gap | TCS-6603 / TCS-6711; these are separate communication targets. |
| L versus NL | TCS-0004, stated as deterministic logarithmic-space directed reachability. TCS-6533 is NL versus UL and would be the wrong match. |
| Finding a prime deterministically | TCS-5930 locates related prime-construction work but remains a draft. Review and repair it before creating another card; this is not an assertion that its current saved statement is already an exact duplicate. |

Other logical distinctions worth preserving: exact quadratic matrix
multiplication is stronger than merely exponent two; AM contained in the
second universal PH level is weaker than AM=NP; computing generalized star
height is different from showing that some language needs height greater than
one. These receive `related_existing`, not a false equivalence certificate.

## Credible alternatives deferred from the fourteen

The selection is a reasoned shortlist, not a proof that every omitted question
has lower scientific value. These are the most useful follow-up groups if the
discussion changes the desired balance.

| Candidate / source | Why it is not in the recommendation set |
| --- | --- |
| [Planar-faced hexahedral meshing, TOPP 27](https://topp.openproblem.net/p27) | Strong geometry alternative. A topological mesh or straight edges do not guarantee planar quadrilateral faces. The [2022 survey](https://doi.org/10.1145/3554920) and [2024 specialized constructions](https://kilian.ac/thesis) need a more precise comparison before certifying the remaining general target. |
| [Dynamic orientations of forests, Korhonen 7](https://tuukkakorhonen.com/problems.html) | Potentially strong dynamic-algorithms addition. Fix explicit versus implicit output, word-RAM cost, adversarial/randomized guarantees and worst-case versus amortized update. Constant recourse is not constant update time. |
| Polynomial expansion versus bounded twin-width, Bonnet 3 | A plausible structural boundary. Current counterexample/status review is not sufficient for a recommendation. |
| Explicit bounded-degree constructions of large twin-width, Bonnet 2 | Formalization cost is irrelevant, but the meaning of explicitness affects the actual theorem. Specify the construction algorithm and its resource bound. |
| Single-exponential clique-width algorithms without a supplied expression, Korhonen 5 | A family of algorithmic questions. Choose the underlying problem before adding a card. |
| Connectivity-oracle branchwidth, Korhonen 6 | Fix the oracle cost and an exact requested asymptotic bound; the source asks for the optimal dependence. |
| Directed-cycle reliability FPRAS, Amarilli | Promising counting question. The solved source-target reliability problem does not automatically provide a cycle-reliability FPRAS. |
| Exact profile maximum likelihood, Sublinear 84 | The [efficient approximation work](https://arxiv.org/abs/1905.08448) changes the old motivation; isolate exact optimization, approximation and statistical utility before deciding. |
| Stack simulation using two queues, cstheory 2562 | An attractive classic, but precise online operation costs and modern simulation lower bounds remain to be checked. |
| Prime acceptance by a finite automaton, cstheory answer 22503 | Potential decidability addition. Base/encoding and subsequent number-theoretic automata results need a dedicated check. |
| A complete problem for NP intersect coNP, cstheory 38105 | Potential foundational question; the reduction model and known conditional obstructions need to be explicit. |
| TLCA: B/omega fixed points; subtype entailment; minimal-theory CPO models | These are plausible logical targets, not rejected because formalization is difficult. Current status and the exact intended systems are not sufficiently established here. |
| Separability workshop: one-counter and branching-VASS variants | Some contain crucial disjointness, tree-versus-word, dimension or alphabet promises. Neither ordinary VASS results nor finite-UFA lower bounds can safely be transferred wholesale. |

The main graph alternatives are Sheehan, total coloring, Borodin–Kostochka,
linear arboricity, strong edge coloring and bipartite crossing-number questions.
They are in the residual comparison pool, not blacklisted as general
combinatorics. Each would need a current-status check and a case for replacing
one of the selected graph topics. [West's list](https://dwest.web.illinois.edu/openp/)
is valuable for that category discussion; the smaller Atlas focus should avoid
becoming a list of similar coloring/flow assertions.

## Source and formulation quality

Garden has substantial spam and many questions outside the Atlas's accepted
scope. Its mathematical notation often uses image `alt` text; extracting only
visible HTML strings loses assumptions and formulas. The review extraction was
corrected for this before checking relevant targets. Bare list membership and
popularity were never used as admission evidence.

Amarilli's MSO-with-cardinality question, as written with arbitrary recursive
predicates, needs a model restriction: applying a fixed hard unary recursive
predicate to the universe size can already defeat a polynomial-time claim on
edgeless inputs. This is a formulation observation, not a claimed new resolution
of a properly restricted MSO meta-theorem. Similarly, Garden's counting-logic
discussion needs separation of FPC from stronger choiceless models.

Fresh proof claims are treated cautiously and specifically. R13 records a
complete-proof claim alongside a later specialist paper still stating the
general second-neighborhood conjecture as open. The July 2026 CDC and Feige
results are identified by date and source, with no assertion that this review
has checked their proofs. A future import should refresh these status checks
at the time the actual cards are prepared.
