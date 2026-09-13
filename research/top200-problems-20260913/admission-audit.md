# Admission and exclusion audit

Date: 13 September 2026.

The task was to find two major problem candidates related to each of the 200 researchers in the preceding conference-based selection, compare them with the atlas, and add missing suitable cards. It was not a requirement to create 400 different problems. The result has 400 associations, 206 distinct problems, 198 reused identities, and eight new identities. Sixteen associations use the new cards; 384 use existing cards.

The hand-authored affinities are in `assignments.txt`. `build_report.py` resolves their stable IDs against active cards, checks that every researcher has exactly two different active targets, carries through references and status notes, and produces the Markdown, JSON and CSV reports. Researcher affinity is an editorial inference from the preceding bibliographic review and the research program described there. It is not a priority attributed to the researcher.

## New admissions

Every new card has a self-contained mathematical statement, an answer criterion, primary references, dated progress, a five-sentence summary, an individual importance assessment and an explicit review scope. Numerical constants use the project's absolute 0.01 acceptance tolerance. Approximation thresholds quantify over arbitrary uniform randomized polynomial-time algorithms, with expected cost, full bit encodings and an infimum that need not be attained.

| Card | Target and source review | Comparison with existing identities |
|---|---|---|
| [TCS-7352](../../data/cards/TCS-7352.json) | Real Grothendieck constant. Checked the [2011/2013 breakthrough](https://arxiv.org/abs/1103.6161) and the [August 2026 bounds](https://arxiv.org/abs/2608.11158). The reported interval is still wider than the benchmark tolerance. | No active or indexed retired identity for this constant was found. It is a universal bilinear-relaxation constant, not the Max-Cut approximation threshold. |
| [TCS-7353](../../data/cards/TCS-7353.json) | Optimal unrestricted Euclidean k-means approximation. Read the definition and introduction of the [July 2026 paper](https://arxiv.org/abs/2607.14654), which permits centers anywhere in Euclidean space and reports a ratio approaching 3 + ln 2. | Distinct from k-median and hierarchical clustering. The comparison found only retired k-means heuristic, fuzzy-clustering and planar-complexity variants. Neither dimension nor k is fixed here. |
| [TCS-7354](../../data/cards/TCS-7354.json) | Optimal metric k-means approximation. The [same paper](https://arxiv.org/abs/2607.14654) defines the metric candidate-center model and reports a ratio approaching 4.9. | General metrics and continuous Euclidean centers have materially different approximation behavior. The card fixes the unweighted client set and exact center budget. The squared-distance objective differs from k-median. |
| [TCS-7355](../../data/cards/TCS-7355.json) | FPRAS for PSD mixed discriminants. Checked [Gurvits's explicit question](https://eccc.weizmann.ac.il/report/2007/037/revision/1/) and the [constrained-DPP paper](https://doi.org/10.4230/LIPIcs.APPROX-RANDOM.2017.36), including its mixed-discriminant section. Targeted 2025–2026 searches did not locate a resolution. | No existing identity found. The diagonal specialization is a nonnegative permanent; known randomized approximation for that specialization is not the general PSD result. The coefficient normalization is explicitly fixed to avoid different factorial conventions. |
| [TCS-7356](../../data/cards/TCS-7356.json) | Optimal algorithmic ratio for metric TSP. Checked the [below-3/2 theorem](https://arxiv.org/abs/2007.01409) and later-work searches. | TCS-6589 asks for a fixed LP's gap. TCS-0954 has a subquadratic distance-query/value-estimation model. The archive index describes TCS-6719 as an improvement request specifically seeking 4/3 through the subtour LP. This new target is the unrestricted algorithmic infimum, not that LP conjecture or an intermediate improvement milestone. No archived card was restored. |
| [TCS-7357](../../data/cards/TCS-7357.json) | Optimal algorithmic ratio for ATSP. Read the [March 2026 improvement below fifteen](https://arxiv.org/abs/2603.14334). | TCS-6590 asks for a fixed LP's gap. The indexed retired TCS-6720 asked only for a constant factor, which is already known. Determining the optimal constant is a different remaining target. |
| [TCS-7358](../../data/cards/TCS-7358.json) | Optimal unrestricted Steiner Tree approximation. Checked the [ln 4 result](https://doi.org/10.1145/2432622.2432628) and [Traub–Zenklusen's 2025 alternative](https://doi.org/10.1145/3722101). | Different from Directed Steiner Tree, Steiner Forest, and the indexed retired bidirected-cut LP-gap questions TCS-5442/TCS-5961. This asks for the best algorithm, not the strength of a selected relaxation. |
| [TCS-7359](../../data/cards/TCS-7359.json) | Public-key quantum money from quantum-hard LWE alone. Checked [iO-plus-LWE constructions](https://arxiv.org/abs/2411.04482), the [2025 evasive-obfuscation barrier](https://eprint.iacr.org/2025/325), and the [group-action constructions in Zhandry's bibliography](https://mzhandry.github.io/pubs.quantum.html). | No active public-money identity found. The card fixes LWE parameters, quantum adversaries, reusable verification and k-to-k+1 unforgeability. A restricted black-box barrier does not refute arbitrary constructions, and a group-action assumption is not LWE alone. |

The archive comparison used the small identity/reason index for collision avoidance. Archived card bodies were not opened or restored. Canonical content lives only in `data/cards/`; the research report contains associations and audit information rather than an alternative card database.

## Candidates not added or not used

| Candidate | Disposition |
|---|---|
| Almost-linear Gomory–Hu trees | Removed from consideration after finding the deterministic 2025 result; the old frontier is no longer a suitable open target. |
| Matrix Spencer conjecture | A [28 August 2026 preprint](https://arxiv.org/abs/2608.28816) claims the full conjecture. Its proof was not independently verified, so the candidate was not admitted as confidently open. |
| Beating 1/2 for single-pass semi-streaming matching | A [July 2026 preprint](https://arxiv.org/abs/2607.14656) claims a matching impossibility theorem. Did not add the stale open question. |
| Optimal sublinear-space single-pass CSP approximation | The [April 2026 lower bound](https://arxiv.org/abs/2604.08731) and [algorithmic result](https://arxiv.org/abs/2604.01575) address the proposed BasicLP frontier. Did not create an open card from one paper's earlier introduction alone. |
| Efficient covariance-aware private Gaussian mean estimation | The [COLT 2023 research summary](https://differentialprivacy.org/colt23-bsp/) explicitly describes the efficient-algorithm breakthrough. Did not reintroduce its former open problem. |
| Pure-DP Euclidean query-release rate | The existing historical TCS-6631 review already identifies Nikolov's 2022/SODA 2023 resolution. It was excluded from the active assignments. The maximum-coordinate variant also has 2026 claimed progress, so the old 2021 post alone is insufficient for admission. |
| Exponential parallel repetition for all two-player entangled games | The existing TCS-5077 review records a directly matching August 2026 claimed resolution. Replaced these proposed researcher assignments with quantum PCP, quantum local testability or quantum-witness questions. |
| Sub-square-root secret-sharing exponents | The existing TCS-0465 review records Nir's August 2026 directly matching claim. Replaced the proposed assignments with local OWFs or one-way permutations. |
| Generic compression to information cost | TCS-5326's inherited wording does not fix the information measure or simulation target; important directions have known separations. Used the more definite total-function direct-sum card TCS-5892 for the selected communication researchers. |
| Generic sketching-versus-streaming, dynamic maximal matching, and dynamic edge coloring | Existing draft titles lacked a selected self-contained target. Used more definite existing graph, reachability and embedding cards in the assignments, without creating duplicates or silently rewriting the drafts. |
| Nuclear-norm sketching and online sparse regression drafts | Used better specified existing embedding and convex-chasing targets for the relevant researchers. No claim that the old questions were resolved. |
| PTAS for bimatrix Nash equilibrium | Not admitted after the identity comparison encountered a prior archived identity. No archive restoration was part of this batch. |

## Scope of the reused-card review

The reused-card pass checked identity, activity, title, source locator, existing status notes and research affinity. It was not a fresh systematic literature review of all 198 reused problems. The resulting 206 distinct selected cards have the following recorded statuses: 155 `source_open`, 20 `open`, and 31 `uncertain`. Their evidence levels are 152 `reviewed`, 34 `source`, and 20 `index`.

In particular, incomplete inherited coding, learning and quantum-query cards remain visibly incomplete in the detailed report. The current reviews of P versus BPP and strongly polynomial LP record unverified direct claims while also identifying mainstream work that treats these as outstanding questions. Those familiar central targets were retained with their uncertainty intact; they were not reported as independently certified open.

Checks of selected older quantum targets also distinguished deterministic-versus-quantum query complexity, whose quartic bound is tight, from randomized-versus-quantum complexity, whose cubic-to-quartic gap remains discussed as open in a [recent introduction](https://yassine-hamoudi.github.io/files/publications/QueryComplexity.pdf). Likewise, [OWSG-to-EFI results and oracle separations](https://arxiv.org/abs/2410.03453) must not be confused with a full unrelativized equivalence. These checks do not promote the underlying draft cards' review levels.

## Publication and checks

- Imported the eight cards with `scripts/import_cards.py`; stable IDs allocated as TCS-7352–TCS-7359.
- `make publish` passed and refreshed the local reader and exports, with 1,049 active cards in that snapshot.
- `make check` passed, including isolated rebuild, export parity, stable ranking, activity/identity protection and importer checks. Its deployment test used a temporary local Git remote; no external deployment was performed by this task.
- `node tests/math.cjs` passed for all 1,049 active cards and 11,279 mathematical expressions in that snapshot.
- `build_report.py` checks 200 ordered researchers, exactly two distinct active IDs each, 400 total associations, references on every selected card, reuse only of baseline identities, and inclusion of every new card in the mapping.

The workspace had concurrent work on card completion and archive organization. This task added its eight canonical cards and research artifacts; it did not overwrite unrelated card edits. Publication counts include the existing shared catalogue.
