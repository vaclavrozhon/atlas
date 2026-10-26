# New-card completion review

Completed 26 October 2026: all 135 imported cards, TCS-7377 through TCS-7511, now have individual statements, definitions, acceptance criteria, context, dated progress, references and five-sentence summaries. The first 84 were reviewed on 23 October; the remaining 51 on 26 October. See queue.json for card-level source links and scope notes, and final-audit.json for preservation checks.

The review preserves the prior editorial ordering, category assignment, import keys and all 985 original card files. Explicitly selected variants and changes to broad source questions are recorded in each card’s statement review and status note. Completion means editorial completion, not mathematical resolution or Lean formalization. Literature checks are bounded and do not certify exhaustive current openness or every cited proof.

Notable caveats: TCS-7461 retains an uncertain status because historical rigidity claims need care. TCS-7504 explicitly records that published bounds already meet the default numerical tolerance, although the exact optimum is a stronger question; it is not advertised as requiring a new numerical estimate. TCS-7468 selects decision-only classification via Borel codes, and TCS-7469 selects decision-only bounded gaps with limit starts under an explicit machine convention.

Validation passed: `make check PYTHON=python3.13` and `node tests/math.cjs` (1,120 active cards, 39,101 expressions). The research files are local provenance; the deployed reader is generated from the canonical cards.
