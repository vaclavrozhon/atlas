# Library problem inventory and selection review — 11 September 2026

The expanded library yielded **187 manually written source entries from 34 sources**. These include historical questions, repeated formulations across books and broader research directions. They are not 187 distinct, currently open benchmark problems.

Read the [complete question inventory](questions.md), or use [CSV](questions.csv) / [JSON](reviewed-entries.json). Each entry retains its book, section or problem number, file page, status and selection decision.

## Results

- 33 source entries have an explicit dated status check; 24 have a resolution or reported resolution recorded.
- 61 entries have an individual status or selection disposition. Other entries remain source leads and were not added to the dataset.
- Five significant, individually formulated problems were added as reviewed cards. Existing and archived catalogue records were included in the novelty search.

- **TCS-7223 — Does integer multiplication have linear-size Boolean circuits?**
- **TCS-7224 — Can the shortest addition-chain length be computed in polynomial time?**
- **TCS-7225 — Does perfect zero knowledge equal statistical zero knowledge?**
- **TCS-7226 — Woodall’s conjecture on packing directed-cut covers**
- **TCS-7227 — Does the packing property imply the max-flow min-cut property?**

The Fourier-transform candidate was not added because TCS-7175 already covers the target. The new Boolean multiplication card differs from the machine-time question TCS-7174. Exact computation of an addition-chain length differs from Scholz–Brauer (TCS-7170). These distinctions are recorded in the [dataset review](../../../research/library-problems-20260911/README.md).

## Extraction coverage and limits

All 101 available local documents (91 personal-library files and ten downloaded documents) underwent full-document text extraction and keyword screening. 2623 merged marker passages are candidate contexts, not verified questions. Five scanned or poorly encoded books also underwent OCR of all 3,152 pages. OCR can miss or corrupt mathematical notation, so its output was not promoted automatically.

The inventory includes three complete numbered lists: 75 Schrijver survey items, 17 Barenboim–Elkin Chapter 11 problems, and all nine Canonne open questions. Other sources received selective passage review, not an exhaustive reading of every exercise or conjecture. Zero selected entries does not mean a book has no open problems. See [per-source coverage](source-coverage.json).

Ten discovered sources had no local full text for this pass. Software Foundations is available as an online series but was not downloaded or inventoried here; the other nine remained bibliographic discoveries:

- Software Foundations
- Proof Complexity
- Communication Complexity
- An Introduction to Description Logic
- Handbook of Satisfiability, Second Edition
- Modern Computer Algebra, Third Edition
- Complexity of Lattice Problems: A Cryptographic Perspective
- Scheduling: Theory, Algorithms, and Systems, Fifth Edition
- Computational Geometry: Algorithms and Applications, Third Edition
- Exact Exponential Algorithms

## Verification and publication

Status checks use primary papers and author corrections, as linked beside each checked question. “Resolved reported” records an author’s report without claiming an independent proof check. Recent preprint claims are identified as such. The new cards contain precise mathematical statements, model definitions, acceptance criteria, significance judgments and dated progress. Their editorial review is not a formal verification of the cited proofs.

`review_inventory.py` contains the human-authored paraphrases. `review_decisions.py` and `decisions.json` contain individual decisions. `extract.py` and `ocr.py` produce the screening audit; `report.py` builds this report. Raw book text and OCR caches are ignored by git. Originals in the personal library were not modified.

The library and this extraction workspace remain outside `atlas/site`. The reader receives the five normal problem cards with public bibliographic references, without access to private book paths or PDFs.
