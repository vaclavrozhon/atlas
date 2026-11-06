# NEXP versus coNEXP addition — 6 November 2026

The user requested NEXP = coNEXP if absent, selected green. No active card states that class equality. The related TCS-7232, Asser’s problem, instead corresponds to NE = coNE with time `2^O(n)`, as explicitly stated in Kopczyński and Tan’s 2018 paper, Introduction and footnote 1. That distinction is retained.

Added **TCS-7524**, *NEXP versus coNEXP*, green in **Computational complexity**, with no forced alternate category. The source proposal has 502 green and 646 red cards; Computational complexity has 26 greens against its target of 25. Existing shared manual choices remain independent of the source proposal.

The statement uses ordinary binary languages, complements over the entire binary-string domain, and one uniform nondeterministic machine per language with a branchwise bound `C 2^((n+1)^k)`. Complement machines may have different fixed constants and exponents. No advice, oracle, promise restriction, effective complement compiler or preservation of the original exponent is required. The acceptance criterion is a complete Lean-checked equality or unconditional separation proof.

Primary sources checked: Tony Tan’s FLOLAC 2023 notes, Section 2.1 and Theorem 2.5; Kopczyński–Tan, *A Note on First-Order Spectra with Binary Relations*, Introduction; Neil Thapen’s *On the consistency of stronger lower bounds for NEXP*, November 2025 revision, Introduction, Theorem 2 and Section 3. The latter’s parameter-free formalization caveat is recorded, and its consistency result is not treated as an unconditional separation. Targeted later-work searches did not identify a verified resolution; the deferred catalogue-wide status audit has not resumed.

Browser selection checks passed with 502 default greens, including anonymous editing, category movement, quotas, persistence, conflicts and mobile layout. All 39,652 active-card math expressions parsed. The selection service passed all 12 tests and its production build. The isolated `make check` suite also passed. Deployed versions and live verification are recorded in the adjacent JSON files.
