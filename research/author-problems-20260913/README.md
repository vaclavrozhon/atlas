# Applied author-based problem selection

Applied the user’s request to add the complete [research proposal](proposal.md) on 13 September 2026: **22 researchers, 45 author–problem assignments, 32 distinct active topics**.

The import created **16 cards**, updated **16 existing cards**, and archived **TCS-5851** losslessly after its first-truly-subcubic tree-edit-distance target had been resolved. Its replacement is **TCS-7374**, asking for almost-quadratic unweighted tree edit distance. Net growth from this batch is 15 active cards. Strong SetDisjointness and a 3SUM-indexing card had been added by another batch after the proposal, so their existing identities were reused.

The 16 new cards and seven substantially developed existing topics have self-contained formulations. At the import checkpoint, reused cards retained their previous review metadata, including TCS-7177’s `model_self_contained: false` flag. A subsequent [individual completion pass](../card-completion-20260913/README.md) separately completed that card; the audit records such later reviews without undoing them. The reviewed evidence level does not certify current openness. The set-disjointness answer criterion was corrected to refer to its universal lower-bound claim. Existing assessed importance scores were preserved. Author associations are additive metadata, preserving earlier research-list imports and editorial decisions.

## Formulation decisions

- **3SUM indexing:** TCS-7333 now asks for the storage/query exponent curve. Its previous subquadratic-space, polylogarithmic-query proposition remains in formulation history. Unrestricted preprocessing and its polynomial integer universe are preserved. Exponent zero does not by itself mean polylogarithmic query time.
- **Binary jumbled indexing:** the optimal-preprocessing topic is expressed as an infimal deterministic exponent. The default absolute 0.01 numerical acceptance rule applies.
- **Gapped string indexing:** the curve fixes the reporting convention, integer alphabet, starting-position gaps, output cost, randomization and polynomial preprocessing. The absolute 0.01 tolerance applies throughout the exponent domain.
- **Minimizers:** TCS-7370 asks for polynomial-time construction of an exactly minimum-density DNA order, measured in explicit order-table size and the unary window parameter. It does not re-propose finite computability, already achieved by exact exponential algorithms.
- **NFA acceptance:** the qualified title and statement specify the balanced dense binary regime of the broader hypothesis, rather than claiming all parameter regimes equivalent to this specialization.
- **Geometry and labels:** previously short records now define nearest-neighbor amortization, regular Euclidean Voronoi cells, facet gluing and nonoverlap, universal point placement, and the information-theoretic exact-label decoder model.
- **Tree edit distance:** the old card was moved through the activity workflow; its complete contents match the saved before snapshot. The new question has a separate identity and records the replacement relationship.

Recent preprint claims are explicitly qualified. The uncertain status of editorially sharpened endpoints, precision targets or interface conventions is retained where appropriate. None of the excluded runs, greedy-superstring, constant-time compact ISA, or character-access-only topics was imported under a new identity.

## Card mapping

| Proposal | Card | Title | Action |
| --- | --- | --- | --- |
| P01 | [TCS-7360](../../data/cards/TCS-7360.json) | Polyloglogarithmic suffix-array access in compact space | New |
| P02 | [TCS-7361](../../data/cards/TCS-7361.json) | Input-optimal construction of compact inverse suffix arrays | New |
| P03 | [TCS-0467](../../data/cards/TCS-0467.json) | Linear-space LZ77 random access | Existing, author association added |
| P04 | [TCS-7362](../../data/cards/TCS-7362.json) | Optimal top-k document retrieval in compact space | New |
| P05 | [TCS-0387](../../data/cards/TCS-0387.json) | Logarithmic fully dynamic planar nearest neighbors | Developed / broadened |
| P06 | [TCS-7363](../../data/cards/TCS-7363.json) | \(\exists\mathbb{R}\) versus \(\mathrm{NP}\) | New |
| P07 | [TCS-7177](../../data/cards/TCS-7177.json) | \(1/3\)–\(2/3\) conjecture | Existing, author association added |
| P08 | [TCS-7364](../../data/cards/TCS-7364.json) | Preprocessing exponent of binary jumbled indexing | New |
| P09 | [TCS-7334](../../data/cards/TCS-7334.json) | Strong SetDisjointness conjecture | Existing, author association added |
| P10 | [TCS-7333](../../data/cards/TCS-7333.json) | Space-query exponent curve of 3SUM indexing | Developed / broadened |
| P11 | [TCS-7365](../../data/cards/TCS-7365.json) | General-alphabet Hamming oracles with optimal preprocessing | New |
| P12 | [TCS-0318](../../data/cards/TCS-0318.json) | Planar k-set extremal function | Existing, author association added |
| P13 | [TCS-0417](../../data/cards/TCS-0417.json) | Near-quadratic Voronoi complexity of lines in three dimensions | Developed / broadened |
| P14 | [TCS-6498](../../data/cards/TCS-6498.json) | Dynamic optimality conjecture | Existing, author association added |
| P15 | [TCS-0406](../../data/cards/TCS-0406.json) | Dürer’s conjecture | Developed / broadened |
| P16 | [TCS-0377](../../data/cards/TCS-0377.json) | Linear-size universal point sets for planar graphs | Developed / broadened |
| P17 | [TCS-7235](../../data/cards/TCS-7235.json) | Almost-linear-time \((1+\varepsilon )\)-approximation of edit distance | Existing, author association added |
| P18 | [TCS-7366](../../data/cards/TCS-7366.json) | Linear-space k-mismatch text indexing | New |
| P19 | [TCS-7367](../../data/cards/TCS-7367.json) | Text-to-pattern Hamming distances below the square-root barrier | New |
| P20 | [TCS-7368](../../data/cards/TCS-7368.json) | Faster elastic-degenerate string intersection | New |
| P21 | [TCS-7369](../../data/cards/TCS-7369.json) | Space-query exponent curve of gapped string indexing | New |
| P22 | [TCS-7370](../../data/cards/TCS-7370.json) | Polynomial-time construction of minimum-density DNA minimizers | New |
| P23 | [TCS-7371](../../data/cards/TCS-7371.json) | Almost-linear constant-factor approximation of LCS | New |
| P24 | [TCS-0775](../../data/cards/TCS-0775.json) | Optimal exact-distance label length for planar graphs | Developed / broadened |
| P25 | [TCS-0468](../../data/cards/TCS-0468.json) | Linear-time LZ77 pattern matching | Existing, author association added |
| P26 | [TCS-7372](../../data/cards/TCS-7372.json) | Linear-time unit-Monge distance multiplication | New |
| P27 | [TCS-6513](../../data/cards/TCS-6513.json) | Constant-factor approximation of the smallest grammar | Existing, author association added |
| P28 | [TCS-7322](../../data/cards/TCS-7322.json) | Optimal approximation ratio for shortest common superstring | Existing, author association added |
| P29 | [TCS-7373](../../data/cards/TCS-7373.json) | Balanced dense NFA Acceptance Hypothesis | New |
| P30 | [TCS-7374](../../data/cards/TCS-7374.json) | Almost-quadratic unweighted tree edit distance | New |
| P31 | [TCS-7375](../../data/cards/TCS-7375.json) | Fully functional suffix trees in BWT-run-linear space | New |
| P32 | [TCS-6669](../../data/cards/TCS-6669.json) | Breaking two for sum-of-pairs multiple sequence alignment | Developed / broadened |

## Researcher coverage

| Researcher | Cards |
| --- | --- |
| J. Ian Munro | [TCS-7360](../../data/cards/TCS-7360.json), [TCS-7361](../../data/cards/TCS-7361.json) |
| Gonzalo Navarro | [TCS-7362](../../data/cards/TCS-7362.json), [TCS-0467](../../data/cards/TCS-0467.json) |
| Yakov Nekrich | [TCS-7362](../../data/cards/TCS-7362.json), [TCS-0387](../../data/cards/TCS-0387.json) |
| Jean Cardinal | [TCS-7363](../../data/cards/TCS-7363.json), [TCS-7177](../../data/cards/TCS-7177.json) |
| Moshe Lewenstein | [TCS-7364](../../data/cards/TCS-7364.json), [TCS-7334](../../data/cards/TCS-7334.json) |
| Ely Porat | [TCS-7333](../../data/cards/TCS-7333.json), [TCS-7365](../../data/cards/TCS-7365.json) |
| Micha Sharir | [TCS-0318](../../data/cards/TCS-0318.json), [TCS-0417](../../data/cards/TCS-0417.json) |
| Erik Demaine | [TCS-6498](../../data/cards/TCS-6498.json), [TCS-0406](../../data/cards/TCS-0406.json) |
| Stefan Felsner | [TCS-7177](../../data/cards/TCS-7177.json), [TCS-0377](../../data/cards/TCS-0377.json) |
| Tomasz Kociumaka | [TCS-7235](../../data/cards/TCS-7235.json), [TCS-7366](../../data/cards/TCS-7366.json), [TCS-7367](../../data/cards/TCS-7367.json) |
| Jakub Radoszewski | [TCS-7366](../../data/cards/TCS-7366.json), [TCS-7368](../../data/cards/TCS-7368.json) |
| Solon P. Pissis | [TCS-7369](../../data/cards/TCS-7369.json), [TCS-7368](../../data/cards/TCS-7368.json) |
| Shay Golan | [TCS-7370](../../data/cards/TCS-7370.json), [TCS-7371](../../data/cards/TCS-7371.json) |
| Paweł Gawrychowski | [TCS-0775](../../data/cards/TCS-0775.json), [TCS-0468](../../data/cards/TCS-0468.json) |
| Gad Landau | [TCS-7372](../../data/cards/TCS-7372.json), [TCS-7235](../../data/cards/TCS-7235.json) |
| Amihood Amir | [TCS-7367](../../data/cards/TCS-7367.json), [TCS-7364](../../data/cards/TCS-7364.json) |
| Masayuki Takeda | [TCS-0468](../../data/cards/TCS-0468.json), [TCS-6513](../../data/cards/TCS-6513.json) |
| Maxime Crochemore | [TCS-6513](../../data/cards/TCS-6513.json), [TCS-7322](../../data/cards/TCS-7322.json) |
| Inge Li Gørtz | [TCS-7369](../../data/cards/TCS-7369.json), [TCS-7373](../../data/cards/TCS-7373.json) |
| Philip Bille | [TCS-0467](../../data/cards/TCS-0467.json), [TCS-7374](../../data/cards/TCS-7374.json) |
| Travis Gagie | [TCS-7375](../../data/cards/TCS-7375.json), [TCS-6513](../../data/cards/TCS-6513.json) |
| Esko Ukkonen | [TCS-7322](../../data/cards/TCS-7322.json), [TCS-6669](../../data/cards/TCS-6669.json) |

## Validation

- `make publish` rebuilt the local reader and exports.
- `make check` passed the isolated canonical-data, import, archival, publication, ranking, export and local deployment regressions.
- `node tests/math.cjs` passed for all 1,064 active cards at the time of the check, including 11,737 mathematical expressions.
- The staged changes separately passed KaTeX parsing for 433 expressions and current record validation.
- `python3 -B research/author-problems-20260913/validate_import.py` verifies all 32 active published records, exactly two assignments per researcher except Kociumaka’s three, stable new IDs, and the unchanged contents of the one specifically archived record.

The live website was not deployed by this batch; `make publish` updates the generated local reader. The deployment regression uses an isolated local Git repository.

## Audit files

- [import-result.json](import-result.json): resulting identities, actions and all author assignments.
- [validation.json](validation.json): final scoped coverage and export check.
- [before.json](before.json): pre-import contents of the 16 existing cards and the specifically replaced record.
- [import-plan.json](import-plan.json), [new-cards.json](new-cards.json): the reviewed staged data.
- [prepare_cards.py](prepare_cards.py), [apply_import.py](apply_import.py): one-time authoring and application scripts; do not rerun against the already applied batch.
- [validate_import.py](validate_import.py): the repeatable read-only audit.
