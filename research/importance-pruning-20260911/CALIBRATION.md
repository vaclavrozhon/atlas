# User calibration and source-context corrections

The user explicitly prefers excluding TCS-0458 (Path ORAM buckets three or four instead of five) as too incremental. This example is persisted in ../../docs/RULES.md and was relayed to all three reviewers. It does not imply deleting every optimal-constant question: a universal limit for an entire canonical model differs from tuning one construction.

The user requested more context for TCS-0464 (information leakage for two-bit OR), without approving exclusion. We explained output-forced disclosure versus avoidable transcript disclosure. Further source checking found that the corresponding standard two-bit AND information-complexity problem has known optimal protocols and consequences for exact asymptotic set-disjointness communication. OR is related by local negation, but the seminar entry does not specify the distribution, information measure or precise remaining finite-round target. Retain for its fundamental topic while requiring those distinctions before a final open-problem card. This is not a new assertion of openness.

Sources checked for that explanation:

- Dagstuhl Seminar 22301, section 4, problem 1.3, attributed to Alexander Shen: https://drops.dagstuhl.de/storage/04dagstuhl-reports/volume12/issue07/22301/DagRep.12.7.180/DagRep.12.7.180.pdf
- Mark Braverman's author overview, section “The two-bit AND function and Disjointness,” including limiting optimality and round approximation: https://mbraverm.princeton.edu/research/information-complexity/
- Filmus, Hatami, Li and You, Information complexity of the AND function in the two-party and multiparty settings, explaining the earlier STOC 2013 result and its set-disjointness consequence: https://arxiv.org/abs/1703.07833

TCS-2731 was initially suspected to be only an ABR-specific proof repair. Reading the complete abstract and conclusion of Revisiting Collision and Local Opening Analysis of ABR Hash corrected that judgment: arbitrary-domain hashing at Stam's optimal compression-call bound is a general target supported by independent prior work. It is retained, with the correction recorded in root-review-04.json. Source: ../expand/papers/10.4230_LIPIcs.ITC.2022.11.json, abstract and PDF page 22; https://doi.org/10.4230/LIPIcs.ITC.2022.11.
