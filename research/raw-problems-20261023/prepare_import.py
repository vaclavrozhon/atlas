"""Prepare the explicitly curated source candidates; does not select by keywords."""
import csv
import hashlib
import json
import re
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
DATE = "2026-10-23"
entries = {e["idx"]: e for e in json.loads((HERE / "source-entries.json").read_text())}
groups = json.loads((HERE / "selection-groups.json").read_text())
curation = {int(r[0]): r[1:] for r in csv.reader(
    (HERE / "curation.tsv").open(), delimiter="\t")}
assert set(entries) == set(curation) == {i for values in groups.values() for i in values}
category_by_id = {c["id"]: c for g in json.loads(
    (ROOT / "data/categories.json").read_text())["groups"] for c in g["categories"]}
category_for = {i: category_by_id[key]["key"] for key, ids in groups.items() for i in ids}
baseline = json.loads((HERE / "baseline.json").read_text())

# The categories below follow the mathematical target, not the input headings.
category_reasons = {
    "sampling": "The target is random generation, a Markov-chain transition, or the complexity of random exploration.",
    "counting": "The target is approximate counting or systematic enumeration with a specified access/delay interface.",
    "privacy": "Differential privacy is an essential requirement of the learning or optimization guarantee.",
    "testing": "The main resource is access to a large object through sublinear queries for testing or estimation.",
    "beyond": "A distributional or instance-sensitive promise is essential to the stated performance target.",
    "data-structures": "The target is a query, priority, search or external-memory interface and its resource bounds.",
    "dynamic": "The central task is maintaining information after updates, including geometric, string and logical queries.",
    "optimization": "The target is optimization, numerical computation, or the geometry of optimization relaxations.",
    "computability": "The target concerns effective presentations, reducibility, degrees or transfinite computation.",
    "reasoning": "The target concerns inference, satisfiability, unification or properties of rewriting.",
    "database": "The target concerns finite relational structures and expressive power of query languages.",
    "automata": "The target concerns language classes, automata, grammars or finite-state descriptions.",
    "semantics": "The target concerns program semantics, logical proof theory, verification or synthesis.",
    "game": "Incentives, strategic equilibrium or mechanism truthfulness determine the main target.",
    "crypto": "The target is a cryptographic security primitive or the assumptions needed to construct it.",
    "online": "The target is competitive performance under sequential information or scheduling with unknown processing times.",
    "learning": "The target is sample-based or limit learning and its statistical or memory requirements.",
    "geometry": "The geometric model and approximation representation are essential to the target.",
    "structural": "The oracle target specifically exploits the planar graph class.",
    "parallel": "The main resource is one-pass streaming space; random order is part of that specialized model.",
    "ads": "The target is a compact algorithmic representation of general terminal flow behavior.",
}
group_for = {i: key for key, ids in groups.items() for i in ids}

titles = {
    1048: "Stationary-start cover-time lower bound",
    1056: "Critical Swendsen–Wang spectral-gap exponent",
    1059: r"Cluster sampling of graph colorings with \(\Delta+1\) colors",
    1067: "Hard-core phase transition on the square lattice",
    1096: "Splay traversal conjecture",
    245: r"Deterministic \(\widetilde O(n^{5/2})\) worst-case dynamic APSP",
    757: r"Low-\(n\) Boolean algebra conjecture",
    764: "Low-two supersets lattice conjecture",
    805: "Topological computable categoricity of infinite Polish spaces",
    806: "Degree of topological categoricity of Baire space",
    363: "NP membership of context unification",
    356: "Nondeterminism versus determinism with two two-way heads",
    443: "DynProp maintenance of directed reachability",
    524: "Flowing conjecture",
    1009: "Three-competitive deterministic file migration",
    649: "Longest-example memory for automatic learning",
    424: r"Cut elimination for \(\mu\mathrm{LK}_{p}^{+}\)",
    437: r"Perpetual reduction for the \(\lambda\sigma\) calculus",
}

def title(e):
    text = titles.get(e["idx"], re.sub(r"^(The|An|A) ", "", e["title"]))
    return text[0].upper() + text[1:]

def clean_url(url):
    return url.rstrip(".,;")

def references(e):
    """Preserve supplied bibliographic labels without inventing parsed authors."""
    section = e["text"].split("References:", 1)[1]
    result, seen, last_label = [], set(), ""
    for line in section.splitlines():
        line = line.strip()
        if not line:
            continue
        urls = re.findall(r"https?://[^\s]+", line)
        label = re.sub(r"https?://[^\s]+", "", line).strip(" .;:")
        if label and len(label) > 15:
            last_label = label
        for url in urls:
            url = clean_url(url)
            if url in seen:
                continue
            seen.add(url)
            caption = label if len(label) > 15 else last_label
            if not caption:
                caption = f"Reference supplied for {title(e)}"
            years = re.findall(r"\b(?:19|20)\d{2}\b", caption)
            ref = dict(id=f"source-{len(result)+1}", title=caption, url=url,
                       locator=f"Bibliography supplied in catalogue v16, {e['area']}, "
                               f"{e['number']}{e['slot']} ({e['author']}).")
            if years:
                ref["year"] = int(years[0])
            result.append(ref)
    # Later-result links in remarks retain their warning and are not claimed as
    # proof of current status. They are kept apart from the bibliography labels.
    remark_text = e["text"].split("References:", 1)[0]
    for url in re.findall(r"https?://[^\s]+", remark_text):
        url = clean_url(url)
        if url in seen:
            continue
        seen.add(url)
        result.append(dict(
            id=f"source-{len(result)+1}", url=url,
            title=f"Additional source cited in the catalogue caveat for {title(e)}",
            locator="Supplied remark; result and applicability not independently certified."))
    assert result, e["source_id"]
    return result

CHECKS = {
    1048: ("https://www.stat.berkeley.edu/~aldous/RWG/Book_Ralph/Ch6.S6.html",
           "Open Problem 6.30 states the stationary-start lower bound. This checks the source question, not present-day openness."),
    1055: ("https://arxiv.org/abs/1607.02182",
           "Abstract confirms the critical four-state quasipolynomial gap and the distinct three-state result."),
    1056: ("https://arxiv.org/abs/1607.02182",
           "Abstract supports the critical-dynamics context; the exact exponent remains an editorial target from the supplied catalogue."),
    1071: ("https://drops.dagstuhl.de/storage/00lipics/lipics-vol327-stacs2025/html/LIPIcs.STACS.2025.16/LIPIcs.STACS.2025.16.html",
           "Problem 1 is the pivot-exchange existence question; the source distinguishes it from efficient generation."),
    1072: ("https://drops.dagstuhl.de/storage/00lipics/lipics-vol327-stacs2025/html/LIPIcs.STACS.2025.16/LIPIcs.STACS.2025.16.html",
           "Problem 2 concerns out-arborescences and a Hamilton path, not necessarily a cycle; it implies Problem 1."),
    229: ("https://openreview.net/pdf?id=lvrn4vnNdd",
          "Section 5 expressly asks whether privacy and horizon dependence can be separated additively."),
    230: ("https://arxiv.org/abs/2410.05880",
          "Abstract confirms the Goldstein-stationarity model and parameter-dependent sample bounds; no current-status certification."),
    344: ("https://www.sciencedirect.com/science/article/pii/S002186932300128X",
          "Introduction states the general Madlener–Otto conjecture and distinguishes inverse-closed special cases."),
    524: ("https://www.math.uwaterloo.ca/~bguenin/covering.html",
          "Corrected the third obstruction to complements of cuts of K5. The supplied 'blocker of the latter' wording is not used."),
    764: ("https://arxiv.org/abs/2412.01939",
          "The revised abstract explicitly says the supersets-lattice conjecture remains open despite earlier proof claims."),
    805: ("https://arxiv.org/html/2507.03972v1#S8",
          "Section 8, Problem 27 states the topological computable-categoricity question."),
    806: ("https://arxiv.org/html/2507.03972v1#S8",
          "Section 8, Problem 28 asks whether Baire space has a degree of categoricity; no isometry substitution."),
    1003: ("https://arxiv.org/abs/2406.16734",
           "Abstract confirms the all-jobs-present obligatory-testing model and distinct general/uniform test durations."),
    1004: ("https://arxiv.org/abs/2406.16734",
           "Abstract confirms the testing model; the randomized target is retained from the supplied Section 5 pointer."),
}

# Deliberately sparse substantive relations; no links are generated from keywords.
RELATED = {
    1048: ["TCS-6851"], 1055: [1056], 1059: [1060, "TCS-6621"],
    1069: [1071, 1072], 1071: [1072], 335: ["TCS-6536"],
    129: ["TCS-1033"], 279: ["TCS-0848"],
    1096: ["TCS-6498", "TCS-6508"], 1111: [1112],
    85: [111], 111: [256], 245: ["TCS-0478"],
    246: ["TCS-6625"], 187: ["TCS-6624"],
    1081: ["TCS-7181"], 1097: [1081],
    1101: ["TCS-6670"], 1126: ["TCS-7326"],
    443: [444, "TCS-3331"], 501: ["TCS-7264"],
    502: [501], 541: [542], 523: ["TCS-7227"],
    755: [774, "TCS-6647"], 756: [781], 805: [806],
    363: ["TCS-6562"], 398: ["TCS-7232"],
    412: [428, "TCS-7195"], 345: [346], 379: [380],
    416: ["TCS-4245", "TCS-6567"], 430: ["TCS-4575", "TCS-5904"],
    435: [436], 1215: ["TCS-6632"], 660: ["TCS-6550", 664],
    669: ["TCS-6551"], 668: [661], 684: ["TCS-6552"],
    1003: [1004], 993: [53, 1001], 1018: ["TCS-7316"],
    649: [650], 14: ["TCS-0408"],
}
# Rank estimation and submodularity testing only share an access model, not a
# mathematical dependency. Do not retain a relation just for category coverage.
RELATED.pop(279, None)

def answer(kind, gap):
    if kind == "yes_no":
        target = "Give a complete Lean-checked proof of the stated existence or universal proposition, or of its logical negation."
    elif kind == "numerical_value":
        target = (r"Supply a real approximation to the defined optimal constant and a Lean-checked proof of absolute error at most \(1/100\). "
                  "Exact determination also qualifies; the approximation does not establish an associated exact conjecture.")
    elif kind == "asymptotic_complexity":
        target = "Give matching upper and lower bounds at the precision specified in the statement, with complete Lean-checked proofs in the stated model."
    else:
        target = "Give a mathematically precise characterization with complete Lean-checked proofs in both directions after the target has been fully specified."
    return target + " This is a provisional candidate, not a completed benchmark specification. Pending: " + gap

cards = []
for i in sorted(entries):
    e = entries[i]
    kind, formal, why, gap = curation[i]
    refs = references(e)
    # Classification questions are not numeric curves; do not fabricate a
    # supported question type or impose the numerical 1/100 rule on a class.
    if i in {1067, 793, 400, 607}:
        kind = None
    source_key = re.sub(r"[^a-z0-9]+", "-", e["area"].lower()).strip("-")
    key = f"raw-catalogue-v16:{source_key}:{e['number']}{e['slot']}"
    caveat = e["text"].split("References:", 1)[0]
    caveat = caveat[len(e["description"]):].strip()
    context = (f"The supplied catalogue associates this question with {e['author']}. "
               "This is an editorial research connection, not a claim of authorship or a personal research agenda. "
               "The candidate retains the bibliography and dated caveats from that catalogue; "
               "these have not received a comprehensive independent literature review.")
    card = dict(
        key=key, title=title(e), area=category_for[i], formal=formal,
        definitions="Definitions and model details remain incomplete. " + gap,
        answer_criterion=answer(kind, gap), context=context, why=why,
        evidence="source", status="uncertain", is_new=True,
        criterion=("tightness" if kind in {"asymptotic_complexity", "numerical_value"} else "decision"),
        model_self_contained=False, requires_context=True,
        references=refs, progress=[], related=[],
        status_note=("The user-supplied catalogue uses a historical cutoff of 2026-01-01 and was prepared on 2026-10-21. "
                     "Known or announced full resolutions noticed during selection were omitted. "
                     "Current open status has not been independently established for this candidate."),
        review_note="Source-candidate import on 2026-10-23. The remaining issue is recorded explicitly; evidence has not been promoted to reviewed.",
        importance=dict(score=50, method="unassessed",
                        reason="Candidate motivation: " + why + " Individual ranking remains unassessed."),
        category_assignment=dict(method="editorial_topic",
                                 reason=category_reasons[group_for[i]],
                                 original_area=e["area"], assigned_on=DATE),
        statement_review=dict(status="needs_specification", reviewed_on=DATE,
                              remaining_issue=gap,
                              scope="Candidate screening and identification of missing specification; not completed formulation review."),
        import_provenance=dict(
            batch="raw-problems-20261023", source_file="raw.txt",
            source_sha256=baseline["source_sha256"], source_catalogue="Cumulative catalogue v16",
            source_cutoff="2026-01-01", source_prepared="2026-10-21",
            source_id=e["source_id"], source_line=e["line"], source_index=i,
            researcher=e["author"], original_area=e["area"],
            original_title=e["title"], original_statement=e["description"],
            supplied_caveat=caveat, relation_to_researcher="editorial association in supplied catalogue"),
    )
    if kind:
        card["question_type"] = kind
    if i in CHECKS:
        url, note = CHECKS[i]
        card["import_provenance"]["source_spot_check"] = dict(
            checked_on=DATE, url=url, finding=note, certifies_current_open_status=False)
    if refs[0].get("year"):
        card["year"] = refs[0]["year"]
    cards.append(card)

(HERE / "new-cards.json").write_text(json.dumps(cards, ensure_ascii=False, indent=2) + "\n")
(HERE / "relations.json").write_text(json.dumps(RELATED, ensure_ascii=False, indent=2) + "\n")
print(json.dumps(dict(prepared=len(cards), original_active=baseline["active_count"],
                     types_pending=sum("question_type" not in c for c in cards))))
