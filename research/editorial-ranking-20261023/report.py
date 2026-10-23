"""Report the verified publication order and compare it with the prior ranking."""
import hashlib
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
read = lambda path: json.loads(path.read_text())
before = read(HERE / "before.json")
data = read(ROOT / "build/catalog.json")
plan = read(HERE / "decisions.json")
assert len(data["cards"]) == len(before["cards"]) == 1120
assert not data["meta"]["benchmark_selection"]["issues"]
assert data["meta"]["importance"]["provisional"] == 0
published = {c["id"]: c for c in data["cards"]}
changed_rank = sum(c["importance_rank"] != before["cards"][c["id"]]["rank"] for c in data["cards"])
changed_score = sum(c["importance"]["score"] != before["cards"][c["id"]]["importance"]["score"] for c in data["cards"])
focus_changes = []
old_focus = {a["area"]: [x["id"] for x in a["selected"]] for a in before["selection"]["areas"]}
for i, area in enumerate(data["areas"], 1):
    d = plan[str(i)]
    focus = ["TCS-" + n for n in d["focus"].split()]
    scores = {"TCS-" + n: int(score) for score, ids in d["tiers"].items() for n in ids.split()}
    intended = focus + sorted(set(scores) - set(focus), key=lambda key: (-scores[key], key))
    actual = [c["id"] for c in data["cards"] if c["area"] == area["area"]]
    assert intended == actual, area["area"]
    for key in actual:
        c = read(ROOT / "data/cards" / (key + ".json"))
        nonranking = {k: v for k, v in c.items() if k != "importance"}
        digest = hashlib.sha256(json.dumps(nonranking, sort_keys=True, ensure_ascii=False).encode()).hexdigest()
        assert digest == before["cards"][key]["nonranking_sha256"], key
        assert c["importance"]["score"] == scores[key]
    if focus != old_focus[area["area"]]:
        focus_changes.append(area["area"])

benchmark_ids = {name: [c["id"] for c in read(ROOT / "build" / (name + ".json"))["cards"]]
                 for name in ("top100", "top500", "top1000")}
for small, large in (("top100", "top500"), ("top500", "top1000")):
    ids = set(benchmark_ids[small])
    assert [key for key in benchmark_ids[large] if key in ids] == benchmark_ids[small]
new_ids = {key for key, c in published.items() if c.get("import_provenance", {}).get("batch") == "raw-problems-20261023"}
summary = {
    "date": "2026-10-23", "publication_version": data["meta"]["version"],
    "cards": 1120, "categories": 35, "explicitly_scored": 1120,
    "changed_rank": changed_rank, "changed_score": changed_score,
    "changed_focus_categories": len(focus_changes), "focus_categories": focus_changes,
    "nonranking_card_content_unchanged": True,
    "published_order_matches_all_explicit_choices": True,
    "nested_exports_preserve_order": True,
    "benchmarks": {name: len(ids) for name, ids in benchmark_ids.items()},
    "new_candidates_in_benchmarks": {name: len(new_ids & set(ids)) for name, ids in benchmark_ids.items()},
}
(HERE / "audit.json").write_text(json.dumps(summary, ensure_ascii=False, indent=2) + "\n")

def md(text):
    return str(text).replace("|", "\\|").replace("\n", " ")

lines = [
    "# Editorial preference ranking — 23 October 2026", "",
    "The user's request was to review the problems and order them by editorial preference within each category. This pass explicitly scored all 1,120 active cards in all 35 categories, including the 135 newly imported candidates.", "",
    "## How to read the order", "",
    "This is subjective editorial judgment based on saved titles and statement excerpts, with expanded summaries for sparse drafts. I favor consequential mathematical barriers, reusable structural principles, and concise conceptual targets. Conceptual clarity refers to the underlying question; unfinished prose and formalization effort do not reduce a score. Age, publication date and the length of a card do not increase it. This pass did not independently verify the literature or current open status.", "",
    "The first five entries in each large category and the first two in each small category form a deliberately ordered focus prefix balancing importance and topic diversity. Remaining entries follow decreasing editorial scores, with stable-ID tie-breaking. Equal scores express comparable preference, not a hidden fine-grained distinction. Scores are rough editorial bands, not probabilities of truth, tractability or eventual solution.", "",
    "Scientific motivation in each importance assessment is retained from the card, with new explicit comparisons at category level. Sparse drafts received targeted motivation based on their saved summaries. Statements, definitions, citations, scientific status, evidence and formulation-review flags are unchanged. In particular, a higher score does not promote a source candidate to a reviewed problem. Both saved girth-conjecture formulations receive the same score; this ranking pass does not merge cards.", "",
    "The static catalogue and exports reproduce this editorial order. The existing live reader can apply community votes on top of it; voting behavior was not changed.", "",
    "## Changes", "",
    f"- {changed_rank} cards changed their position within a category.",
    f"- {changed_score} scores changed; all 1,120 now have an explicit editorial assessment.",
    f"- {len(focus_changes)} categories have a changed focus prefix.",
    "- The nested exports contain 100, 488 and 886 entries respectively. Existing per-category quotas remain unchanged.",
    f"- Newly imported candidates represented: {summary['new_candidates_in_benchmarks']['top100']} in Top 100 and {summary['new_candidates_in_benchmarks']['top500']} in Top 500.",
    "- Non-ranking card content was verified unchanged by hashes for every active card.", "",
    "## Audit and reproduction", "",
    "decisions.json contains every individually assigned score tier, the ordered focus prefixes and the category comparisons. before.json preserves the previous assessments, ranks and focus selections. apply_ranking.py applies those choices after validating complete and unique coverage. It does not infer priority from keywords or reuse old scores to select the new tiers. After make publish, report.py verifies all 35 orders and produces this report and audit.json. validation.json records the completed checks.", "",
    "## Complete ranking", "",
    "Previous position refers to the local catalogue immediately before this ranking pass. Focus marks the Top 100 prefix. Every row links to its canonical card.", "",
]
for i, area in enumerate(data["areas"], 1):
    lines += ["### " + area.get("label", area["area"]), "", plan[str(i)]["reason"], "",
              "| Rank | Previous | Score | Focus | Problem |", "| ---: | ---: | ---: | :---: | --- |"]
    for c in data["cards"]:
        if c["area"] != area["area"]:
            continue
        key = c["id"]
        focus = "yes" if c.get("benchmark_focus") else ""
        lines.append(f"| {c['importance_rank']} | {before['cards'][key]['rank']} | {c['importance']['score']} | {focus} | [{md(c['title'])}](../../data/cards/{key}.json) ({key}) |")
    lines.append("")
(HERE / "README.md").write_text("\n".join(lines).rstrip() + "\n")
print(json.dumps(summary, ensure_ascii=False, indent=2))
