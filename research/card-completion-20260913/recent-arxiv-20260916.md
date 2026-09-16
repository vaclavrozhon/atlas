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
| [BVASS/VASS geometry, 2609.15869](https://arxiv.org/abs/2609.15869) | Extended FOSSACS 2026 paper; the abstract distinguishes reachability-set geometry and effective semilinearity in dimension five. A full theorem/model check is needed before altering TCS-1649's arbitrary-dimensional decidability status. |
| [Ideal lattices, 2609.15813](https://arxiv.org/abs/2609.15813), and [cyclic SVP, 2609.16711](https://arxiv.org/abs/2609.16711) | General number rings, canonical versus coefficient embeddings, discriminants, exact versus approximate SVP, and cryptographic parameter restrictions must be separated when completing the broad TCS-6863 draft. These abstracts do not establish hardness for every ring-SIS/LWE cryptographic distribution. |
| [Randomized queries versus certificates, 2609.15063](https://arxiv.org/abs/2609.15063), and [quantum/certificate separation, 2609.11664](https://arxiv.org/abs/2609.11664) | Claims concern certificate complexity; they cannot be substituted for block sensitivity, randomized complexity of a named function, or communication complexity merely because those quantities are related. |

The recent Matrix Spencer, Bilu–Linial signing, influential-coalition,
max-distance network-creation and Medvedev-logic titles were also screened.
No direct active target was identified by the title/formulation searches used
here; existing archive bodies were not consulted. The Friedgut coalition result
is distinct from the active Fourier Entropy–Influence conjecture.

The active randomized k-server and total-function communication-gap cards are
reserved for a full follow-up formulation pass. A deterministic factor-k claim
does not determine the randomized optimal-ratio function. The 2021 communication
source's title mentions efficient players, but its imported total-function
question is a background communication-only question; that distinction is being
checked against the full source before completing the draft.
