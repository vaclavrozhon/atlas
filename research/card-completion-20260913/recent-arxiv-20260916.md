# Recent arXiv intake, 16 September 2026

This is a bounded current-status intake for **active cards only**, prompted by
arXiv:2609.14555 and arXiv:2609.15979. No existing archived card bodies were
reviewed. A matching theorem statement is not independent verification of its
proof. Fresh matching claims receive `uncertain`, with explicit source scope;
they are not recorded as verified resolutions.

## Changes from the first intake

| Active card | Primary result inspected | Disposition |
| --- | --- | --- |
| TCS-7316, Matroid secretary | [Singla, 2609.14555v1](https://arxiv.org/abs/2609.14555), submitted 13 September; full PDF §3 Theorem 3.1, with nonnegative fixed weights and arrived-only independence queries | Completed the full formulation; changed to uncertain. The claimed factor four covers the target, with less advance information. |
| TCS-5779, Correlated online contention resolution | Same preprint, together with [Dughmi, ICALP 2020 Theorem 4.1](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.ICALP.2020.42) and the [ITCS 2022 equivalence](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.ITCS.2022.58) | Replaced the placeholder with the complete known-prior, random-order, per-element target; uncertain. The main secretary claim would imply a factor-four loss relative to offline balance. |
| TCS-6575, Deterministic k-server ratio | [Coester–Koutsoupias–Zbysiński, 2609.15979v1](https://arxiv.org/abs/2609.15979), submitted 14 September; full PDF §1.1 Theorem 1.2 and model | Changed to uncertain. The claim covers all metrics, repeated initial locations, lazy serving and a finite additive term depending only on the initial placement. Combined with the classical lower bound, it would determine the retained function exactly. |
| TCS-4737, QMA perfect completeness over Clifford+T | [Grewal–Rudolph, 2609.13032v1](https://arxiv.org/abs/2609.13032), Theorem 1.1 and Corollary 1.2; [Liu–Vidick, 2609.15926v1](https://arxiv.org/abs/2609.15926), Theorem 1.3 and §2.1 | Changed to uncertain. The first paper explicitly covers Clifford+T; both have fixed gates exactly implementable in the selected model. Their finite-register one-message claims are distinct from the older infinite-counter and oracle results. |
| TCS-6450, Polynomial classical/quantum communication relation | [Gavinsky, 2608.18784v1](https://arxiv.org/abs/2608.18784), Theorem 1; [Le Gall, 2609.16726v1](https://arxiv.org/abs/2609.16726), Theorems 2–3 and §2 | Changed to uncertain. The claimed total-function separations use public-coin classical lower bounds with arbitrary interaction and worst-case communication. Entanglement-free quantum upper bounds also apply to the card's entanglement-assisted model. The previous bounded search missed the August claim. |

The complete proofs of these fresh claims were **not** independently certified,
and no Lean verification was performed. In Singla §4, the single-sample prophet
and intersection extensions defer detailed proofs; those announcements are not
used as established theorems. The two supplied PDFs have title-page dates of
15 September, which differ from their arXiv submission dates.

## Intake scope and nearby results

Recent-title listings were retrieved for cs.DS (first 50 entries), cs.CC (43),
cs.DM (41), cs.GT (68), cs.CG (19), cs.LO (first 50), cs.CR (first 50), and
quant-ph (499). These contain cross-list duplicates. Most theoretical-category
listings cover 10–16 September; the first cs.CR page covers only 15–16 September.
The quant-ph list received a targeted title screen for complexity, communication,
verification, codes, entanglement and related active subjects, not a full-paper
review of every entry. Additional older cs.DS titles were visible in a cached
listing. Bulk/paginated arXiv requests sometimes returned HTTP 429, and one
cached listing ended on 15 September; this intake is **not a complete crawl**.
Retrieved source PDFs and raw listings stay in the ignored `sources/` directory.

| Primary item | Boundary checked against active work |
| --- | --- |
| [Almost Linear Universal Point Sets, 2609.10916](https://arxiv.org/abs/2609.10916) | TCS-0377 already records the new claim. The bound `n^{1+o(1)}` does not establish its fixed-constant `O(n)` target. |
| [Complex Komlós discrepancy, 2609.15071](https://arxiv.org/abs/2609.15071) | Allows arbitrary unit-modulus complex coefficients, rather than only real signs. It is not a replacement for TCS-7314. That card already records the matching real-sign claim [2609.11189](https://arxiv.org/abs/2609.11189) as uncertain; its live page still lists version 1. |
| [List decoding and linear hashing, 2609.17020](https://arxiv.org/abs/2609.17020) | The abstract concerns random linear codes, not the full-length Reed–Solomon family of TCS-1011. It does not by itself settle that card. |
| [Planar excluded-grid bound, 2609.15596](https://arxiv.org/abs/2609.15596) | The `4t+4` theorem is for planar graphs. TCS-6683 asks for the all-graphs threshold. |
| [High-multiplicity bin packing, 2609.16923](https://arxiv.org/abs/2609.16923) | FPT in the number of distinct sizes with binary multiplicities is different from the uniform polynomial-time additive-error guarantees in TCS-6721/TCS-6640. |
| [BVASS/VASS geometry, 2609.15869](https://arxiv.org/abs/2609.15869) | Full PDF checked: Theorem 5.2 is structural, Remark 5.4 explains the effectiveness gap, and Theorem 7.3 distinguishes 5-BVAS from 2-BVASS. Refreshed TCS-1649; its arbitrary-dimensional problem is explicitly still open in the new conclusion. |
| [Ideal lattices, 2609.15813](https://arxiv.org/abs/2609.15813), and [cyclic SVP, 2609.16711](https://arxiv.org/abs/2609.16711) | Completed TCS-6863 with an expressly labeled classical polynomial-time, polynomial-factor search-SVP target on power-of-two cyclotomic ideals. Read both full introductions and main theorem/model statements. Neither the variable totally real number rings nor exact cyclic coefficient-SVP hardness covers this selected family and approximation target; source_open retained. These claims do not establish hardness for every ring-SIS/LWE cryptographic distribution. |
| [Randomized queries versus certificates, 2609.15063](https://arxiv.org/abs/2609.15063), and [quantum/certificate separation, 2609.11664](https://arxiv.org/abs/2609.11664) | Claims concern certificate complexity; they cannot be substituted for block sensitivity, randomized complexity of a named function, or communication complexity merely because those quantities are related. |

The recent Matrix Spencer, Bilu–Linial signing, influential-coalition,
max-distance network-creation and Medvedev-logic titles were also screened.
No direct active target was identified by the title/formulation searches used
here; existing archive bodies were not consulted. The Friedgut coalition result
is distinct from the active Fourier Entropy–Influence conjecture.

The follow-up pass completed TCS-7317 (randomized k-server) and TCS-4952
(total-function communication gaps). The former retains constant-factor
asymptotics and source-open status: a deterministic factor-k claim does not
determine the randomized scale. The latter now has a precise infinite-family
polylogarithmic-versus-polynomial target and uncertain status matching the two
new communication claims. The full ITCS 2021 source confirms that efficient
players belong to its separate partial-function result, rather than its imported
background question. TCS-1649 was also refreshed after reading the complete
relevant theorem/model passages in the extended BVASS paper.

The lattice follow-up also completed TCS-0661. The inherited SIGACT Question 4.9 permits some fixed module rank and some ring family; the selected full formulation uses cyclotomic rings with the canonical Euclidean norm and deterministic many-one hardness. [Liu–Feng–Pan, 2609.01469v1](https://arxiv.org/abs/2609.01469), submitted 1 September, claims a matching rank-two prime-conductor result. The full model, Theorem 1.1, Corollary 1.2 and the stated reduction/verification conclusions were read; the complete new proof was not independently certified. The card is uncertain. This additional item predates the recent-list window and was found through the adjacent lattice literature.

The scheduling follow-up completed TCS-6674 and inspected
[Universally truthful mechanisms for scheduling, 2609.12621v1](https://arxiv.org/abs/2609.12621),
submitted 11 September. The full introduction, model and main theorem statements
were checked. Its claimed linear lower bound restricts to countably supported
mixtures of deterministic truthful rules; the active card allows arbitrary
truthfulness in expectation. Finite outcome support at each fixed report does
not supply that additional hypothesis. The card therefore remains source-open;
the new result is recorded as restricted progress, without independent proof
certification. No other active card with this scheduling target was found.

The general-allocation pass completed TCS-6639 and checked the
[14 September revision of Distributed Santa Claus via Global Rounding](https://arxiv.org/abs/2604.27983v2).
Its full introduction and main model use restricted assignment and CONGEST
communication rounds. Section 1.3.2 separately retains the unrestricted
agent-specific valuation problem as open. The card remains source-open; neither
the distributed theorem nor the restricted valuation promise resolves its
centralized constant-factor target.

The trace-reconstruction pass completed TCS-6623 and checked
[Degree Sequence Reconstruction from Subgraph Traces, 2609.09397v1](https://arxiv.org/abs/2609.09397),
submitted 8 September. Its full introduction acknowledges the July quasipolynomial
upper bound and the polynomial lower bound for ordinary binary strings. Its new
results concern vertex-deleted graph observations and graph degree sequences,
so they do not determine the string card’s constant-factor sample complexity.
An active-only search found no matching graph-degree-sequence target. The July
paper’s full Theorem 43 and its distinction between samples and running time
were checked separately; no external proof was independently formalized.

The deletion-capacity pass completed TCS-6607 and inspected
[Soysal, 2609.13351v1](https://arxiv.org/abs/2609.13351), submitted 11 September.
The full introduction, Theorem 1.1, operational model, limitations and formal
verification appendices were read. The claimed capacity upper bound is
`(1-d)/4` for `13/20 <= d < 1`, with finite-block corrections. The accompanying
[repository](https://github.com/factoreminv/bdc) reports modular fresh Lean
replay and final assembly over verified imports; its README and machine-readable
verification record were inspected, but this review did not execute the large
certificate or replay the proof. The result is one-sided and covers only part
of the parameter domain. Separately, the classical uniform finite-block bound
already gives unrestricted fixed-accuracy approximation of the full curve.
After being told this, the user explicitly retained absolute 0.01 accuracy as
a formalization task. The revised card distinguishes that known approximation
guarantee from the separate open exact-capacity question.
