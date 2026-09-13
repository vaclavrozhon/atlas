"""Record the individual disposition of all 200 proposals; never edit cards."""
import collections
import json
from pathlib import Path

B = Path(__file__).resolve().parent
ROOT = B.parent.parent
DATE = '2026-09-11'
rows = json.loads((B/'matches.json').read_text())
cards = {c['personal_import']['candidate']: c for c in json.loads((B/'additions.json').read_text())}
existing = {k:'TCS-'+v for k,v in (line.split() for line in (B/'existing-map.txt').read_text().splitlines() if line.strip())}
registry = json.loads((ROOT/'data/id_registry.json').read_text())
deleted = json.loads((ROOT/'data/deleted_records.json').read_text())

# These are editorial consolidation decisions, not assertions of equivalence.
consolidated = {
    '16B': ('TCS-1058', 'The proposal uses rank n/2, while the retained explicit-rigidity target uses n/log log n. They are not equivalent. Keep one canonical rigidity program instead of a second rank-parameter variant without a separate admission rationale.'),
    '32A': ('TCS-1015', 'The proposal asks simultaneously optimal strong seeded extraction. The retained target is weak extraction with constant total entropy loss. The strong constant-error target implies the latter by adjoining the seed, not conversely; retain the existing entropy-loss frontier instead of an additional optimality variant.'),
    '71A': ('TCS-6859', 'The retained card already asks for polynomial-time construction of GV inner codes on their own size scale. Its source explicitly identifies this with the general explicit-GV challenge (2025 edition, Open Question 8.3.2 and Section 10.2). The proposed non-linear-code formulation is not literally identical to its linear-code wording; preserve that distinction without adding a second GV-construction card.'),
    '72B': ('TCS-6603', 'Randomized log-rank is a weaker variant of the retained deterministic conjecture. The original citation does not substantiate it as an independently motivated target. This is consolidation of a related consequence, not a claim that deterministic and randomized communication are equal.'),
}
excluded = {
    '10B': ('The general no-congestion edge-disjoint-paths approximation target faces superpolylogarithmic conditional hardness. Exclude this proposal editorially because it is largely a challenge to overturn that general hardness assumption, without a distinct positive frontier. It is not unconditionally resolved.', 'https://toc.cs.uchicago.edu/articles/v017a006/'),
    '53A': ('A PTAS for additive approximate bimatrix Nash equilibria is ruled out under ETH for PPAD. This is stronger and more specialized than ordinary ETH; no unconditional impossibility is claimed. The proposal does not supply an independent admission rationale beyond refuting that established hardness framework.', 'https://arxiv.org/abs/1606.04550'),
    '58B': ('The Alon–Tarsi Latin-square parity conjecture is general combinatorics. The proposal does not establish the specific computational significance required for an exception to the atlas scope boundary.', None),
    '82B': ('The simultaneous approximate-agreement round and message target is an efficiency refinement within a specific asynchronous model. Its independent breadth is insufficient under the atlas preference for general barriers, rather than parameter refinements chosen for researcher affinity.', None),
    '83A': ('Polynomial-time feasibility of optimally resilient full-information asynchronous Byzantine agreement is already established in the cited line of work. The proposed cubic-latency endpoint is a more specialized efficiency refinement; it is excluded editorially, not declared solved.', None),
    '88A': ('The proposal concerns preservation of the full FS-domain subclass by a valuation construction. Even after the broad Jung–Tix category problem has a claimed 2026 solution, that precise closure target is distinct. Exclude it as a technical closure refinement without sufficient independent significance; do not claim that the all-FS statement was proved.', None),
    '94A': ('With two variables, rectangular guards and resets to zero, stopwatch reachability is already decidable: Bouyer’s 2011–2012 notes, Exercise 23, p. 59 of the PDF. The original general hybrid-automata citation does not make this an open boundary. A different guard language must be justified separately; no replacement problem is invented.', 'https://lsv.ens-paris-saclay.fr/~bouyer/files/mpri1112.pdf'),
}
held = {
    '31B': ('The previously matched TCS-0852 was deleted concurrently in a user-authorized fundamentality screen. Its removal reason distinguishes a method-specific Ramsey route from the eligible general construction question. This review had interpreted the source more broadly. Hold the ambiguous match rather than restore a reserved identity or silently recreate the deleted mathematical target.', ['https://www.cs.umd.edu/~gasarch/open/crt.pdf']),
    '42A': ('The proposal requests trilinear maps with a “plausibly hard” target. The group family, symmetry, encoding and security experiment are unspecified, and the cited source does not recover a definite computational assumption. Hold outside the atlas until the intended proposition is identified.', []),
    '66B': ('The saved proposal and chat formulation differ on exact versus approximate random-tensor recovery. The source does not fix the requested quadratically overcomplete Gaussian recovery model, representation, accuracy or success quantifiers. Hold rather than certify an invented recovery theorem.', []),
    '79B': ('A July 2026 preprint, Bipartite Bound Information Exists, claims an affirmative solution. The proof was not independently verified in this review, so the candidate is not imported as open and the claim is not presented as an established resolution.', ['https://arxiv.org/abs/2607.25838']),
    '80A': ('An August 2026 theorem announcement claims exponential repetition for all finite two-player entangled games. The September 9 revision of a human audit withdraws its earlier apparent polarity error and reports varying review depth. Hold because of the new solution claim; do not rely on the outdated abstract alleging an error or certify the full proof independently.', ['https://hhri.foxconn.com/en/events/657','https://arxiv.org/abs/2608.14673v3','https://cdn.openai.com/pdf/ten-proofs-oai.pdf']),
    '91B': ('A 2026 I3322 repository claims an exact nonattainment certificate implying nonclosure in the (3,2) scenario, while a 2026 research course still presents the question as open. The claim and certificates were not independently verified; hold for status adjudication.', ['https://github.com/Apsiape/i3322-exact-wall/blob/main/paper/RELEASE-NOTES-v1.1.0.md','https://www.mittag-leffler.se/app/uploads/2023/06/IMLCourse2026.pdf']),
}
coverage_notes = {
    '3A': 'The almost-linear general matching target is retained; removing isolated vertices reconciles the usual n+m versus m formulations.',
    '10A': 'The existing excluded-grid card asks for the exact asymptotic dependence, including logarithmic factors, and already covers the proposed near-quadratic bound.',
    '20B': 'The existing SVP-hardness card covers the polynomial approximation-factor hardness question but still needs exact source assumptions. A second draft would duplicate that target.',
    '24A': 'TCS-1337 concerns algorithmic Reed–Solomon list decoding beyond Johnson. TCS-1011 is a different combinatorial list-size question and was rejected as a false match.',
    '25A': 'The existing source-backed linear-PCP/LTC record includes linear-length PCPs. Its broader packaging is not grounds for importing another PCP copy.',
    '31B': 'The retained explicit-Ramsey source asks for the exponential-in-k construction scale; this is the proposed logarithmic homogeneous-set target.',
    '54B': 'The existing question asks for the full asymptotic truthful-in-expectation makespan ratio, explicitly including whether it is constant.',
    '57B': 'Determining the exact Shannon capacity of C7 already includes deciding equality with its Lovász theta bound.',
    '59B': 'The currently present card is the same 5-flow conjecture. Allowing loops adds no difficulty because each loop balances itself.',
    '61B': 'The currently present PL four-sphere card covers disconnected as well as connected promised manifolds. Disconnectedness is directly detectable, so the decision targets coincide.',
    '64B': 'The retained linear-bandit card asks for the full minimax dimension dependence, including the proposed rate.',
    '67B': 'The retained Gaussian agnostic-halfspace card already asks for the optimal runtime at the desired accuracy.',
    '70A': 'The existing source draft is the same input-sparsity spectral-relative low-rank target; model gaps do not justify a duplicate.',
    '71B': 'The existing deletion-code card asks for the supremum correctable deletion fraction, containing the proposed improvement past sqrt(2)−1.',
    '78B': 'The retained depolarizing-channel capacity question includes positivity below the proposed noise threshold.',
    '84B': 'The source of the existing queue draft explicitly identifies unrestricted wait-free exact FIFO implementation with membership in Common2 (OPODIS 2020, Section 4, PDF p. 13). The shortened card title alone obscures this exact match.',
    '97A': 'The existing first-order tree-language definability record retains the relevant descendant-based logical target; signature details need formulation review within that card.',
}
groups = [set(cards),set(existing),set(consolidated),set(excluded),set(held)]
assert len(set.union(*groups)) == 200
assert sum(map(len,groups)) == 200
audit=[]
for row in rows:
    pid=row['candidate']
    r=dict(candidate=pid,researcher=row['researcher'],proposal=row['query'],original_source=row['source'],reviewed_on=DATE)
    if pid in cards:
        c=cards[pid]
        identifier=registry.get('reviewed:'+c['key'])
        r.update(action='added' if identifier else 'ready_to_import',atlas_id=identifier,key=c['key'],title=c['title'],evidence=c['evidence'],statement_review=c['statement_review']['status'],reason=c['why'],remaining_issue=c['statement_review']['remaining_issue'],sources=[x['url'] for x in c['references']])
    elif pid in existing:
        identifier=existing[pid]
        path=ROOT/'data/cards'/f'{identifier}.json'
        if path.exists():
            c=json.loads(path.read_text())
            r.update(action='already_present',atlas_id=identifier,title=c['title'],comparison='covered_by_existing_target' if pid in coverage_notes else 'same_mathematical_target',reason=coverage_notes.get(pid,'The proposed target is already represented by '+identifier+' ('+c['title']+'). Reuse the existing identity; this import does not recertify its status or completeness.'),sources=[x['url'] for x in c.get('references',[]) if x.get('url')])
        else:
            assert identifier in deleted, f'Unexplained missing identity: {identifier}'
            r.update(action='excluded',atlas_id=identifier,record_removed=True,reason='The matched card was deleted concurrently. Honor the reserved identity and the user-authorized removal; do not recreate it. Removal reason: '+deleted[identifier],sources=[row['source']])
    elif pid in consolidated:
        identifier,reason=consolidated[pid]
        r.update(action='consolidated_related_variant',atlas_id=identifier,reason=reason,not_claimed_equivalent=True)
    elif pid in excluded:
        reason,source=excluded[pid]
        r.update(action='excluded',reason=reason,sources=[source or row['source']])
    else:
        reason,sources=held[pid]
        r.update(action='held_outside_atlas',reason=reason,sources=sources or [row['source']])
    audit.append(r)
counts=dict(collections.Counter(r['action'] for r in audit))
result=dict(date=DATE,input_file='research/personal-open-problems-100-cs.json',input_researchers=100,input_problems=200,counts=counts,new_evidence=dict(collections.Counter(c['evidence'] for c in cards.values())),dispositions=audit)
(B/'dispositions.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')

md=['# Personal open-problem import, 11 September 2026','',
    'Reviewed all 200 proposals assigned to the 100 researchers. Researcher affinity is an editorial inference, not an attributed statement of their priorities. Admission follows [the atlas rules](../../docs/RULES.md).','',
    '| Disposition | Count |','| --- | ---: |']
md += [f'| {k.replace("_"," ")} | {v} |' for k,v in counts.items()]
md += ['',f'The {len(cards)} new candidates contain 28 individually revised formulations and 25 source-backed drafts with explicit remaining specification issues. Draft admission is permitted for the candidate pool; it does not certify a benchmark-ready statement. All have individually authored context, significance, sources and an editorial importance assessment.','',
    f'The {counts.get("already_present",0)} existing-target matches and four consolidation decisions do not all assert literal equivalence. The audit labels broader existing targets and different variants explicitly. No existing card is rewritten by this batch, and no focus selection is changed by it.','',
    'The review is bounded, not an exhaustive proof that every admitted target remains unresolved. In particular, the new claims for bipartite bound information, general entangled parallel repetition and the (3,2) correlation-set closure problem are held outside the atlas. The latest parallel-repetition audit withdraws its earlier apparent extraction-induced error; the hold does not allege that this error remains.','',
    'Two-stopwatch reachability with rectangular guards and zero resets is already decidable, so it was removed from the open-problem proposal set. Conditional hardness for disjoint paths and approximate Nash equilibria is recorded as conditional, not as an unconditional solution.','',
    'Source corrections include decision-tree learning, low-rank approximation, threshold circuits, the secret-sharing reference, coding-course editions and several author lists. The withdrawn 2026 signing-preprint link was replaced for the strongly explicit Ramanujan candidate.','',
    'The atlas changed concurrently during the review, including additions, revisions and a substantial user-authorized deletion pass. Verification records the observed changes separately from this import. In particular, PL four-sphere recognition and Tutte’s 5-flow conjecture were matched against those additions. Those changes are not credited to this batch. The deleted Ramsey match TCS-0852 was held outside the import rather than recreated.','',
    'Machine-readable details are in [dispositions.json](dispositions.json). The import payload is [additions.json](additions.json); [verification.json](verification.json) records publication and integrity checks. Research source extracts are not published with the reader.','',
    '| Proposal | Researcher | Decision | Atlas record / reason |','| --- | --- | --- | --- |']
for r in audit:
    identifier=r.get('atlas_id')
    target=(f'[{identifier}](../../data/cards/{identifier}.json)' if (ROOT/'data/cards'/f'{identifier}.json').exists() else f'{identifier} (removed)') if identifier else ''
    desc=r['reason'].replace('|','\\|').replace('\n',' ')
    md.append(f'| {r["candidate"]} | {r["researcher"]} | {r["action"].replace("_"," ")} | {target} {desc} |')
(B/'README.md').write_text('\n'.join(md)+'\n')
print(json.dumps(dict(counts=counts,new_evidence=result['new_evidence'])))
