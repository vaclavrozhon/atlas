# Admission audit: researchers 101–300

Review date: 11 September 2026. The complete selection is in [assignments.md](assignments.md), with the same records in [assignments.json](assignments.json).

## Scope and editorial decisions

The requested two-to-five range was implemented as two questions for each of the 200 supplied researchers. There are 400 assignments and 295 distinct targets. Of these, 283 already had atlas cards; 12 were added. Repeated assignments reuse the same stable ID. No researcher- or category-specific quota was used to justify adding a weaker question.

Scientific significance takes priority over a direct coauthorship link. The affinity notes are reasoned suggestions based on the supplied career profiles and the content of the selected questions. They are not claims that 200 researchers publicly named these exact priorities, and this report does not claim to have read every researcher’s publication record exhaustively.

The review compared proposed targets with active cards, historical source keys and deletion reasons. Title matching was insufficient: MCSP hardness was already present under a sum-of-squares paper title, and an existing shortest-superstring card concerns exact exponential-time algorithms rather than approximation. No deleted identity was restored, including the specifically rejected TCS-0513.

Full formulations are different from brief suggestions. The nine new formulation-reviewed cards contain explicit models and quantifiers. Three important new targets remain source drafts with concrete remaining issues. Existing cards keep their own evidence and status; 104 distinct selected cards have incomplete formulation metadata. This report does not promote those drafts or certify that every inherited question is currently open. An `uncertain` status is displayed explicitly in the assignment report. In particular, the atlas records unverified claims concerning P versus BPP, strongly polynomial LP and parity games; those claims are not treated as established resolutions.

## New cards

| ID | Target | Admission and duplicate decision | Formulation |
| --- | --- | --- | --- |
| [TCS-7314](../../data/cards/TCS-7314.json) | Komlós vector balancing | A defining discrepancy conjecture; no existing full target found. Implies TCS-7315. | Reviewed |
| [TCS-7315](../../data/cards/TCS-7315.json) | Beck–Fiala discrepancy | The full set-system conjecture is distinct from the excluded method-specific passage TCS-5224. Its logical dependence on Komlós is documented. | Reviewed |
| [TCS-7316](../../data/cards/TCS-7316.json) | General matroid secretary | The general adversarial-weight/random-order conjecture, not the random-assignment variant, an ordinal/cardinal comparison, or a particular algorithm family. | Reviewed |
| [TCS-7317](../../data/cards/TCS-7317.json) | Polylog(k) randomized k-server | The ratio is independent of metric cardinality. This is not the refuted O(log k) conjecture. | Reviewed |
| [TCS-7318](../../data/cards/TCS-7318.json) | Constant approximation for Dasgupta clustering | A fundamental graph objective, without stability or comparison-oracle promises. Small-Set Expansion gives conditional hardness; the dependence is stated. | Reviewed |
| [TCS-7319](../../data/cards/TCS-7319.json) | Minimax sequential calibration | The complete remaining rate question, not the already broken T^{2/3} barrier. Distinct from scoring-rule regret in TCS-1529. | Reviewed; asymptotic target |
| [TCS-7320](../../data/cards/TCS-7320.json) | Log-supermodular #CSP to #BIS reduction | A precise unresolved classification barrier. Neither the solved exact-counting dichotomy nor an unsupported global approximation trichotomy. | Reviewed |
| [TCS-7321](../../data/cards/TCS-7321.json) | P_ℝ versus NP_ℝ | The BSS real model is specified and differs from classical bit computation. | Reviewed |
| [TCS-7322](../../data/cards/TCS-7322.json) | General 2-approximation for superstring | TCS-0816 asks a separate exact-time question. The new target allows any polynomial-time algorithm. | Reviewed |
| [TCS-7323](../../data/cards/TCS-7323.json) | PIR from arbitrary one-way functions | A broad assumption relationship, not the bundle of narrower work/communication questions excluded as TCS-0461. | Source draft: joint security and communication parameters |
| [TCS-7324](../../data/cards/TCS-7324.json) | Unrestricted offline ORAM lower bounds | A circuit-complexity barrier for oblivious computation. Online and indivisible-data lower bounds do not settle it. | Source draft: word sizes, space and security |
| [TCS-7325](../../data/cards/TCS-7325.json) | Stochastic linear Bellman-complete RL | The general computational-statistical gap, beyond deterministic transitions. | Source draft: state/feature representation and arithmetic model |

The authoring input is [author_cards.py](author_cards.py); the imported payload is [additions.json](additions.json). Stable IDs were allocated by the repository importer under its publication lock. Existing cards were not overwritten by this import.

## Cases changed or withheld after source review

- **MCSP hardness and white-box PIT:** matched to TCS-5501 and TCS-7113. Both were already present under less obvious titles, so neither received a new ID. The short formulations do not silently complete their canonical model review.
- **Metrical task systems and logarithmic k-server:** the proposed O(log n) worst-case MTS target and O(log k) randomized k-server conjecture were rejected as open targets. The [Bubeck–Coester–Rabani lower-bound paper](https://arxiv.org/abs/2211.05753) resolves the relevant old conjecture negatively. The [2026 k-server paper](https://arxiv.org/abs/2605.01497) still has metric-size dependence in its general-metric guarantee; it does not answer TCS-7317.
- **Greedy superstring:** [Shibata’s September 2026 preprint](https://arxiv.org/abs/2609.01365) claims a factor-9/4 counterexample. Its correctness is not independently certified here. The general factor-two question survives that claim and is separated from it in the new card. The [August 2026 cycle-cover report](https://eccc.weizmann.ac.il/report/2026/157/) concerns a general 7/3 approximation.
- **Calibration:** the [Dagan–Daskalakis–Fishelson–Golowich–Kleinberg–Okoroafor paper](https://arxiv.org/abs/2406.13668) already improves the two-thirds exponent and proves a lower bound above the square-root scale. Neither threshold was recycled as open. The selected target is the remaining minimax rate. Results for multicalibration use a different loss and do not identify that rate.
- **Nash PTAS:** the proposed general target matched a previously excluded identity, TCS-4573. It was not restored under a new name. Daskalakis receives Continuous Local Search and calibration instead.
- **Three-party disjointness:** the old super-log-cubed target TCS-1046 was not retained. Primary [research-seminar descriptions of the polynomial lower bounds](https://www.cs.columbia.edu/theory/s09-theoryread.html) already supersede that historical threshold. Sherstov instead receives the total-function quantum/classical communication question.
- **Clique versus independent set:** TCS-1043’s historical superlogarithmic target was not retained. The [Göös–Jayram–Pitassi–Watson paper](https://research.ibm.com/publications/randomized-communication-versus-partition-number) strengthens earlier deterministic bounds with near-optimal randomized lower bounds. Gábor Tardos receives log-rank instead.
- **Private online finite mistake bounds:** TCS-0510 was not retained. Subsequent [lower-bound work](https://papers.neurips.cc/paper_files/paper/2024/file/77fa8253adfc8b33209639f3e9985741-Paper-Conference.pdf) and [adaptive-adversary algorithms](https://arxiv.org/abs/2510.00574) materially change the old question. A sublinear or logarithmic mistake guarantee must not be confused with a bound independent of the horizon.
- **Private Euclidean query release:** TCS-6631 is marked resolved by the live atlas’s individual review of Nikolov’s result. It was removed from both planned assignments during the final live-status check.
- **Computational versus statistical privacy:** TCS-6825’s working summary records a [FOCS 2023 conditional separation](https://doi.org/10.1109/FOCS57990.2023.00042). The old textbook question was not used as an unqualified open replacement.
- **Switch-chain mixing:** the live TCS-6622 review records [Fu–Qin–Wang’s 2026 claimed resolution](https://arxiv.org/abs/2606.22636), including a reported Lean artifact. This task did not verify that proof or artifact. The target was withheld rather than advertised as an ordinary open problem.
- **MELL:** the live TCS-7192 review records the general decidability consequence claimed in [Bizière–Leroux–Sutre, July 2026](https://arxiv.org/abs/2607.09558). It was withheld without upgrading the claim to an established theorem.
- **Coq, excluded middle and Church’s Thesis:** partial consistency results for fragments must not be substituted for the full source question. The initial TCS-3031 assignments were replaced rather than presenting a prematurely simplified yes/no statement.
- **Online sparse regression:** the historical draft TCS-0715 was replaced after checking the [Foster–Kale–Karloff hardness result](https://proceedings.mlr.press/v49/foster16.pdf).
- **Other broad source labels:** TCS-0655 and TCS-0659 did not yet fix a particular approximation/assumption proposition; low-dimensional VASS thresholds and a time-bounded Kolmogorov label also did not provide sufficiently clear choices for this short list. They were replaced by established, more precisely stated problems, without deleting or rewriting the existing cards.

These are admission decisions for this selection. They are not a bulk status update for every historical card mentioned above.

## Verification and reproducibility

- [finalize_report.py](finalize_report.py) checks all 200 consecutive researcher numbers, exactly two distinct targets per researcher, live canonical IDs, absence of deleted/resolved/excluded cards, and a source link for every assignment.
- [stats.json](stats.json) records the exact counts. [import-result.json](import-result.json) lists the 12 allocated IDs.
- [selected-card-digests.json](selected-card-digests.json) fingerprints the cards used for the final report. Other workspace edits are not attributed to this task.
- Source discovery and follow-up results are saved in the adjacent research JSON files; downloaded primary documents are in `sources/`. These are research inputs, not additional editable catalogues.
- Publication and repository checks are recorded in [verification.json](verification.json). Passing these checks establishes repository consistency, not mathematical correctness of open-problem statements.
