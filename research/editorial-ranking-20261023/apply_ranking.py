"""Apply explicit editorial choices; no ranking is inferred from keywords or age."""
import hashlib
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
DATE = "2026-10-23"
BASIS = (
    "Subjective editorial preference requested by the user, based on saved titles "
    "and statement excerpts, with expanded summaries for sparse drafts. "
    "Scientific interest, breadth, conceptual clarity and topic diversity guide "
    "the explicit choices in research/editorial-ranking-20261023/decisions.json. "
    "This is not a new literature, formulation or current-open-status review. "
    "Formalization effort, prose length and publication date do not affect scores."
)

def read(path):
    return json.loads(path.read_text())

def write(path, value):
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n")

def nonranking_hash(card):
    content = {k: v for k, v in card.items() if k != "importance"}
    return hashlib.sha256(json.dumps(content, sort_keys=True, ensure_ascii=False).encode()).hexdigest()

categories = [c for group in read(ROOT / "data/categories.json")["groups"] for c in group["categories"]]
cards = {p.stem: read(p) for p in (ROOT / "data/cards").glob("TCS-*.json")}
plan = read(HERE / "decisions.json")
selection_path = ROOT / "data/benchmark_selection.json"
assert len(cards) == 1120 and len(categories) == len(plan) == 35
old_selection = read(selection_path)
snapshot_path = HERE / "before.json"
if not snapshot_path.exists():
    catalogue = read(ROOT / "build/catalog.json")
    ranks = {c["id"]: c["importance_rank"] for c in catalogue["cards"]}
    write(snapshot_path, {
        "date": DATE,
        "selection": old_selection,
        "cards": {key: {"importance": c["importance"], "rank": ranks[key],
                        "nonranking_sha256": nonranking_hash(c)}
                  for key, c in sorted(cards.items())},
    })
before = read(snapshot_path)
assert set(before["cards"]) == set(cards)

custom_motivation = {
    "TCS-0315": "Coarse geometric exclusion forcing useful separators is a broad bridge between metric structure and graph algorithms.",
    "TCS-1639": "The global growth of a hereditary graph class constraining local neighborhood diversity is an appealing structural principle, with a connection to compact labels.",
    "TCS-6874": "Optimal spectral expansion at every degree is a fundamental sparse-connectivity target; this score concerns the saved target, with its unresolved conventions and dated status unchanged.",
    "TCS-6875": "Two-sided spectral control under graph lifts is a reusable structural route to high-quality expanders; the draft's source and status qualifications remain in force.",
    "TCS-7143": "A universal pivot-minor obstruction for large rank-width would connect decomposition complexity to concrete unavoidable graph structure.",
    "TCS-7144": "Trees as unavoidable vertex-minors would give a clean structural explanation of large linear rank-width.",
    "TCS-7145": "Well-quasi-ordering would provide a broad finiteness principle for pivot-minor obstructions; the graph universe in the draft still needs specification.",
    "TCS-6607": "The user-retained 1/100 approximation target is valuable as a formalization task. Its known approximation guarantee gives it lower priority here than unresolved structural capacity questions; the target and its active status are unchanged.",
}

def band(score):
    if score >= 95:
        return "a defining landmark"
    if score >= 80:
        return "a high-priority broad or central question"
    if score >= 65:
        return "a substantial question with more specialized scope or lower comparative priority"
    return "a narrower target or a lower-priority task in this research-oriented comparison"

selection = {"version": old_selection["version"], "reviewed_on": DATE,
             "basis": BASIS + " Scores and focus prefixes were reconsidered. Equal scores express comparable preference; stable IDs break ties outside the focus prefix.",
             "areas": []}
old_by_area = {a["area"]: a for a in before["selection"]["areas"]}
seen = set()
for index, category in enumerate(categories, 1):
    decision = plan[str(index)]
    area = category["key"]
    expected = {key for key, c in cards.items() if c["area"] == area}
    scores = {}
    for score_text, identifiers in decision["tiers"].items():
        score = int(score_text)
        assert 0 <= score <= 100
        for number in identifiers.split():
            key = "TCS-" + number
            assert key not in scores and key not in seen, key
            scores[key] = score
    assert set(scores) == expected, area
    seen.update(scores)
    focus = ["TCS-" + number for number in decision["focus"].split()]
    limit = 5 if index <= 10 else 2
    assert len(focus) == min(limit, len(expected)) and len(set(focus)) == len(focus)
    assert set(focus) <= expected
    for key, score in scores.items():
        card = cards[key]
        assert nonranking_hash(card) == before["cards"][key]["nonranking_sha256"], key
        motive = custom_motivation.get(key, card.get("why", "")).strip()
        assert motive and not motive.startswith(("Source selection:", "The significance of this particular")), key
        card["importance"] = {
            "score": score, "method": "editorial", "assessed_on": DATE,
            "reason": motive + " Editorial placement in this pass: " + band(score) + ".",
            "basis": BASIS,
            "category_comparison": decision["reason"],
        }
    ordered = focus + sorted(expected - set(focus), key=lambda key: (-scores[key], key))
    selection["areas"].append({
        "area": area, "rationale": decision["reason"],
        "selected": [{"id": key, "topic": cards[key]["title"],
                      "reason": custom_motivation.get(key, cards[key]["why"])} for key in focus],
        "previous_ids": [c["id"] for c in old_by_area.get(area, {}).get("selected", [])],
        "considered_ids": ordered,
    })
assert seen == set(cards)
# Validate the entire plan before any canonical write.
for key, card in cards.items():
    assert nonranking_hash(card) == before["cards"][key]["nonranking_sha256"]
    write(ROOT / "data/cards" / (key + ".json"), card)
write(selection_path, selection)
print(json.dumps({"assessed": len(cards), "categories": len(categories), "focus": sum(len(a["selected"]) for a in selection["areas"]), "nonranking_content_unchanged": True}))
