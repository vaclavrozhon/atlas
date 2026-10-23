"""Resolve curated relations and record the source-candidate import audit."""
import hashlib
import json
from collections import Counter
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
BATCH = HERE.name
baseline = json.loads((HERE / "baseline.json").read_text())
cards = {}
paths = {}
for path in (ROOT / "data/cards").glob("TCS-*.json"):
    card = json.loads(path.read_text())
    assert card["id"] not in cards
    cards[card["id"]] = card
    paths[card["id"]] = path
selected = {
    c["import_provenance"]["source_index"]: c
    for c in cards.values()
    if c.get("import_provenance", {}).get("batch") == BATCH
}
assert len(selected) == 135
assert len(cards) == baseline["active_count"] + len(selected)
relations = json.loads((HERE / "relations.json").read_text())
for index, targets in relations.items():
    card = selected[int(index)]
    resolved = [selected[t]["id"] if isinstance(t, int) else t for t in targets]
    assert all(t in cards and t != card["id"] for t in resolved)
    card["related_problem_ids"] = sorted(set(resolved))
    paths[card["id"]].write_text(json.dumps(card, ensure_ascii=False, indent=2) + "\n")

for filename, digest in baseline["card_sha256"].items():
    assert hashlib.sha256((ROOT / "data/cards" / filename).read_bytes()).hexdigest() == digest, filename
registry = json.loads((ROOT / "data/id_registry.json").read_text())
for card in selected.values():
    aliases = [prefix + card["key"] for prefix in ("", "reviewed:", "source-import:", "proposal:")]
    assert {registry[key] for key in aliases if key in registry} == {card["id"]}
    assert card["evidence"] == "source" and card["status"] == "uncertain"
    assert card["statement_review"]["status"] == "needs_specification"
    assert card["statement_review"]["remaining_issue"] and card["references"]
    assert not card["model_self_contained"] and card["requires_context"]

added = Counter(c["area"] for c in selected.values())
after = Counter(c["area"] for c in cards.values())
ordered = sorted(selected.values(), key=lambda c: c["id"])
result = {
    "batch": BATCH,
    "input_problem_descriptions": baseline["input_problem_descriptions"],
    "source_sha256": baseline["source_sha256"],
    "active_before": baseline["active_count"],
    "active_after": len(cards),
    "new_candidates": len(selected),
    "original_active_files_unchanged": True,
    "added_by_category": dict(sorted(added.items())),
    "independent_source_spot_checks": 14,
    "current_open_status_audited": False,
    "cards": [{
        "id": c["id"], "title": c["title"], "area": c["area"],
        "source_id": c["import_provenance"]["source_id"],
        "source_index": c["import_provenance"]["source_index"],
        "remaining_issue": c["statement_review"]["remaining_issue"],
    } for c in ordered],
}
(HERE / "import-result.json").write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n")

lines = [
    "# Source candidates from the supplied catalogue v16",
    "",
    "Imported 135 new candidates (TCS-7377–TCS-7511) on 2026-10-23, bringing the active catalogue from 985 to 1,120 cards. All 985 previously active card files are byte-for-byte unchanged.",
    "",
    "The source is the user-supplied raw.txt, containing 1,344 descriptions. Its historical cutoff is 2026-01-01; its preparation date is 2026-10-21. The source SHA-256 is " + baseline["source_sha256"] + ".",
    "",
    "## Editorial scope",
    "",
    "The user requested 100–200 additions, prioritizing sparsely represented categories, as source candidates with citations and explicit gaps. Original area headings were treated as suggestions. Assignments follow the mathematical target: dynamic logical queries go to dynamic algorithms, private learning targets to differential privacy, and counting/enumeration targets to Counting and enumeration.",
    "",
    "Each candidate has an individually written provisional statement, motivation, remaining specification issue, supplied bibliography, and traceable source location. Every new card has evidence=source, status=uncertain, statement_review=needs_specification, and an unassessed importance score. No candidate is certified as currently open, self-contained, or literature-reviewed. Four classification questions deliberately omit question_type rather than pretending to ask for a numeric curve. User-supplied researcher associations are editorial connections, not claims of authorship or personal research agendas.",
    "",
    "Selection used comparisons with active cards and manual screening of titles, statements, and caveats. Known duplicates and full-resolution warnings noticed in this process were excluded. This is not an exhaustive semantic-deduplication or current-status audit of all 1,344 descriptions. Archived cards were not reconsidered. Closely related but distinct targets retain separate candidate cards with explicit gaps and selected related-problem links.",
    "",
    "## Category coverage",
    "",
    "Coverage counts describe active cards, not benchmark selection or importance rankings. Sparsity was a priority, not a quota: only two suitable new differential-privacy candidates were retained. No additions were placed in Miscellaneous.",
    "",
    "| Category | Before | Added | After |",
    "| --- | ---: | ---: | ---: |",
]
for area in sorted(added, key=lambda a: (baseline["counts"].get(a, 0), a)):
    lines.append(f"| {area} | {baseline['counts'].get(area, 0)} | {added[area]} | {after[area]} |")
lines += [
    "",
    "## Screening examples and source checks",
    "",
    "Examples of excluded overlaps (input index → existing active ID): 42 → TCS-6625; 281 → TCS-7326; 310 → TCS-6626; 622 → TCS-0724; 1098 → TCS-5825; 1129 → TCS-7328; 1130 → TCS-0474; 1132 → TCS-7112. Input 193 was dropped because the existing adaptive-adversary formulation in TCS-0543 already permits the proposed deterministic special case.",
    "",
    "Examples excluded because the supplied text flagged full resolutions or announcements: 608, 611, 630, 1068, 1070, 519, 548, 370, 393, 426, 1201, and 1203. Those warnings guided exclusion; they were not independently certified as proofs.",
    "",
    "Limited independent primary-source checks were recorded for 14 selected entries (1048, 1055, 1056, 1071, 1072, 229, 230, 344, 524, 764, 805, 806, 1003, 1004). These checks establish specific source details only; they do not certify present-day openness. The other bibliographic labels and links are preserved from the supplied text and await individual verification.",
    "",
    "A substantive correction was made to the Flowing conjecture (input 524): its third forbidden clutter is the complements of cuts of K5, following [Guenin's statement](https://www.math.uwaterloo.ca/~bguenin/covering.html). The input's blocker-of-the-latter wording was not adopted. Gray-code targets distinguish paths from cycles, and computable-categoricity targets retain topological rather than isometric equivalence.",
    "",
    "## Reproduction and audit files",
    "",
    "source-entries.json preserves the 135 selected source excerpts. curation.tsv contains the individual edited statements, motivations, and gaps. selection-groups.json records editorial category assignments. prepare_import.py creates new-cards.json and relations.json; scripts/import_cards.py allocates stable IDs and skips already-imported source keys. finalize_import.py resolves relations, checks old-file hashes and candidate metadata, and regenerates this report and import-result.json. baseline.json stores the original counts and file hashes. validation.json records the completed validation commands.",
    "",
    "The canonical cards are in data/cards. Generated publication files stay in the ignored build directory. No publication or remote push is performed by these research scripts.",
    "",
    "## Added cards",
    "",
    "| ID | Candidate | Category | Source entry |",
    "| --- | --- | --- | --- |",
]
for c in ordered:
    title = c["title"].replace("|", "\\|")
    src = c["import_provenance"]["source_id"]
    lines.append(f"| [{c['id']}](../../data/cards/{c['id']}.json) | {title} | {c['area']} | {src} |")
(HERE / "README.md").write_text("\n".join(lines) + "\n")
print(json.dumps({"added": len(selected), "active": len(cards), "original_files_unchanged": True, "categories": len(added)}, indent=2))
