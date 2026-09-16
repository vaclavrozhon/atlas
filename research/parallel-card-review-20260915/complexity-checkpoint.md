# Constraint games, ARRIVAL, Tarski and cell probes

16 September 2026. The overall review continues; this is a checkpoint for four individually completed records.

- **TCS-5544**: retained the forward implication from a perfect-completeness d-to-one conjecture for some fixed d to full UGC. Defined the games, gap quantifiers, classical value and deterministic polynomial reductions. The source's complete Appendix B proof only yields completeness 1/d. The September 2026 D₄ claim would establish the antecedent, making the implication equivalent to UGC conditional on that theorem; it does not settle UGC. Score 94.
- **TCS-6006**: recovered the exact ARRIVAL-in-P question in the source's terminating two-destination model. Defined successor multiplicity, self-loops, initial bits, update order, validity and deterministic bit complexity. Checked the general 2021 subexponential algorithm and the restricted 2025/2026 results. Score 88.
- **TCS-3509**: completed and immediately archived as resolved. The original totalized Tarski circuit problem lies in PLS∩PPAD. Published class equalities from STOC 2021 and CCC 2022 establish both CLS and EOPL membership. The card retains monotonicity violations as legal outputs and distinguishes EOPL from UEOPL. Full original membership proofs and the main CCC 2022 reductions were read; no new independent proof or Lean formalization is claimed. Score 84.
- **TCS-0949**: specified the general succinct deterministic exact Boolean matrix-vector query problem, with adaptive logarithmic-word probes, arbitrary encoding, uncharged computation and total space n²+o(n²). The 2018 lower bound retains the unchanged matrix and counts entries, so neither its representation scope nor its redundancy-dependent word-probe consequence settles the general statement. Score 91.

All four used parent worker `card-review-third-862815` and the atomic claim/completion workflow. Each completion was locally published. No current record was overwritten by another worker; the long publication ID lists reflect derived publication changes as well as direct review work.

## Validation and evidence

- Canonical schema checks and queue-hash checks passed for the three active records. The Tarski archive path and absence from active publication were checked from metadata without reopening its archived body. See `complexity-hashes.json`.
- Twelve browser cases passed for active cards at desktop/mobile widths in compact/full layouts, with canonical/publication parity, rendered mathematics, linked source statements, no horizontal overflow and no browser/HTTP errors. Snapshot: `6cd70bbe18acec00c46a`. See `complexity-browser-audit.json`.
- All 25,615 mathematical expressions across 1,031 active cards parsed. The 56 mathematical expressions in the newly authored Tarski script also parsed, without accessing the archived record. See `complexity-math.json` and `tarski-authored-math.json`.
- Targeted whitespace checks passed. `complexity-sources.json` records thirteen cached primary-source hashes and the exact reading scopes.
- No external publication, commit or push occurred, and no pre-existing archive body was read.

Queue snapshot: 502 completed, 412 pending, one outside active scope, out of 915 initial records. The parent next claimed TCS-0002, TCS-0004 and TCS-6533; their existing substantial content will be preserved and individually checked against their sources and the acceptance rules.
