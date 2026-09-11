import json, re, unicodedata, hashlib, csv
from pathlib import Path
from collections import Counter
import sys
ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT))
from taxonomy import SMALL
D=Path(__file__).resolve().parent
a=json.loads((D/'shortlist.json').read_text())
catalog_bytes=(ROOT/'site/catalog.json').read_bytes()
catalog=json.loads(catalog_bytes)
baseline=json.loads((D/'baseline.json').read_text())
assert SMALL==baseline['categories'], "Taxonomy changed: review before finalizing."
old={x['id']:x for x in baseline['records']}
live={x['id']:x for x in catalog['cards']}
seeds={x['slug']:x for x in json.loads((D/'novelty-screen.json').read_text())}
# Manually chosen editorial ordering, not generated from age or source counts.
order={
1:'densest-k directed-steiner tsp-four-thirds atsp-gap-two dfvs-constant',
2:'fpt-w1 eth setcover-exact',
3:'seth orthogonal-vectors kclique minplus-convolution hitting-set-conjecture',
4:'space-prg-optimal',
5:'ef-lower modfrege',
6:'logrank fei aaronson-ambainis',
7:'gaussian-interference deletion-capacity information-inequality-decision ldc-logqueries c7-capacity',
8:'permanent-determinantal vp-vbp determinant-formulas finite-field-factor finite-group-iso permanent-exact',
9:'h10q factoring discrete-log svp-polyspace least-nonresidue',
10:'coloring-mixing switch-chain',
11:'trace edit-near-linear',
12:'dynamic-connectivity dynamic-msf dynamic-approx-matching',
13:'general-perfect-matching deterministic-permanent',
14:'polynomial-hereditary-testing',
15:'pure-query-release-l2',
16:'truthful-submodular cake-queries randomized-distortion',
17:'pcsp-dichotomy infinite-csp-dichotomy three-colourable-constant',
18:'unrelated-machines santa-claus binpacking-additive',
19:'word-equations-length one-relator-monoid one-relator-conjugacy modal-k-unification one-rule-termination',
20:'query-enumeration',
21:'martin-conjecture degree-rigidity kl-ml hindman-strength',
22:'dnnf-equivalence',
23:'hadwiger erdos-hajnal gyarfas-sumner seese cereceda',
24:'planted-clique tensor-pca smoothed-maxcut',
25:''}
patterns={
'ldc-logqueries':r'locally.decod|local.decod|\\bLDC',
'polynomial-hereditary-testing':r'polynomial.*testab|hereditary.*test|forbidden.*test',
'one-relator-monoid':r'one.relat|one.relation',
'kl-ml':r'Kolmogorov.Loveland|Loveland|Martin.Lof',
'information-inequality-decision':r'information.inequal|entropy.inequal|entropic',
'determinant-formulas':r'determinant|arithmetic.formula',
'atsp-gap-two':r'ATSP|asymmetric.*travel|asymmetric.*sales|subtour',
'dfvs-constant':r'directed.*feedback|feedback.*vertex',
'orthogonal-vectors':r'orthogonal.vector',
'hitting-set-conjecture':r'hitting.set.conjecture|hitting.set.hypothesis',
'permanent-determinantal':r'permanent|determinant',
'least-nonresidue':r'non.?residue|Vinogradov',
'edit-near-linear':r'edit.distance',
'dynamic-approx-matching':r'dynamic.*match|match.*dynamic',
'truthful-submodular':r'truthful|submodular.*auction',
'infinite-csp-dichotomy':r'infinite.domain|finitely.bounded|Bodirsky|Pinsker',
'three-colourable-constant':r'3.colou?r|three.colou?r',
'word-equations-length':r'word.equation|length.constraint',
'one-rule-termination':r'one.rule|single.rule|one.rewrite|one.*rule.*termin',
'one-relator-conjugacy':r'one.relat|conjugacy',
'martin-conjecture':r'Martin.s.conjecture|degree.invariant|Turing.invariant',
'hindman-strength':r'Hindman|finite.sums',
'space-prg-optimal':r'branching.program|read.once',
'pure-query-release-l2':r'query.release|statistical.quer|Nikolov'}
def norm(s):
 return ''.join(c for c in unicodedata.normalize('NFKD',s).lower() if not unicodedata.combining(c)).replace('–','-').replace('—','-').replace('−','-')
def question(c):
 sf=c.get('source_formulation') or {};lg=c.get('legacy') or {}
 return ' '.join(str(x) for x in [c.get('title'),c.get('formal'),sf.get('text'),lg.get('question_excerpt')] if x)
shared_slugs={'h10q','word-equations-length'}
shared=[]
retained=[]
for x in a:
 if x['slug']=='gyarfas-sumner':
  x['sources']=['https://arxiv.org/abs/2302.08922']
  x['novelty_note']=x['novelty_note'].replace('Author page lists A note on the Gyarfas-Sumner conjecture (2024).','Nguyen-Scott-Seymour explicitly formulate the general conjecture in their 2024 paper.')
 if x['slug']=='aaronson-ambainis':
  x['novelty_note']='No matching question found. The specific source is Bhattacharya, ITCS 2025, article 17.'
 if x['slug']=='truthful-submodular':
  x['sources']=['https://epubs.siam.org/doi/10.1137/20M1316068','https://theory.stanford.edu/~shaddin/papers/randompower-focs09.pdf']
 if x['slug']=='coloring-mixing':
  x['sources'].append('https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.ICALP.2026.134') if len(x['sources'])==1 else None
 if x['slug'] in shared_slugs:
  x['status']='already_proposed_in_large_category_report'
  x['cross_proposal']='../fundamental-additions-20260910/REPORT.md'
  x['placement_note']='The present taxonomy suggests this small-category home, but this is not an additional distinct suggestion beyond the parallel large-category proposal.'
  shared.append(x)
 else:retained.append(x)
# Reruns preserve the cross-proposal list.
if not shared and (D/'shared-with-large-proposal.json').exists():
 shared=json.loads((D/'shared-with-large-proposal.json').read_text())
a=retained
a.sort(key=lambda x:(x['category'],order[x['category']].split().index(x['slug'])))
counts=Counter(x['category'] for x in a)
audit=[]
for c in range(1,26):
 rows=[x for x in a if x['category']==c]
 for rank,x in enumerate(rows,1):
  x['category_name']=SMALL[c-1]
  x['rank_in_category']=rank
  x['ranking_method']='editorial: foundational significance, breadth of consequences, centrality; not an objective metric'
  if x['slug'] in seeds:pattern=seeds[x['slug']]['pattern']
  else:pattern=patterns[x['slug']]
  rx=re.compile(pattern,re.I)
  hits=[]
  for card in live.values():
   kind='question' if rx.search(norm(question(card))) else 'source_context' if rx.search(norm(' '.join(r.get('title','') for r in card.get('references',[])))) else None
   if kind:hits.append({'id':card['id'],'title':card['title'],'match_type':kind,'question':question(card)})
  audit.append({'slug':x['slug'],'pattern':pattern,'matches':hits,'editorial_novelty_note':x['novelty_note']})
assert len(a)==len({x['slug'] for x in a})
assert all(1<=x['category']<=25 and x['question'] and x['importance'] and x['sources'] for x in a)
assert all(u.startswith('https://') for x in a for u in x['sources'])
assert all(x['status']=='recommended_for_editorial_review' for x in a)
reject=json.loads((D/'rejections.json').read_text())
for x in reject:
 if x['slug']=='prime-construction':x['sources']=[live['TCS-5930']['references'][0]['url']]
 if x['slug']=='superstring-two':x['sources']=[live['TCS-0816']['references'][0]['url']]
(D/'rejections.json').write_text(json.dumps(reject,ensure_ascii=False,indent=2)+'\n')
(D/'shortlist.json').write_text(json.dumps(a,ensure_ascii=False,indent=2)+'\n')
(D/'shared-with-large-proposal.json').write_text(json.dumps(shared,ensure_ascii=False,indent=2)+'\n')
(D/'final-novelty-audit.json').write_text(json.dumps(audit,ensure_ascii=False,indent=2)+'\n')
meta={'review_date':'2026-09-10','catalog_version':catalog['meta']['version'],'catalog_records':len(live),'catalog_sha256':hashlib.sha256(catalog_bytes).hexdigest(),'new_catalog_ids_since_baseline':sorted(set(live)-set(old)),'new_suggestions':len(a),'shared_with_large_proposal':len(shared),'requested_minimum_per_category':5,'quota_met':all(counts[c]>=5 for c in range(1,26)),'categories':[{'number':c,'name':SMALL[c-1],'new':counts[c],'shortfall_to_five':max(0,5-counts[c])} for c in range(1,26)],'checks':['Current small-category taxonomy matches the baseline.','All 6513 current question records included in final lexical cross-check; lexical results are not themselves semantic proofs.','Every retained entry has a question, importance rationale, sources, novelty note and editorial rank.','Known duplicates and claimed/resolved candidates are excluded from retained entries.','Two suggestions already present in the large-category proposal are cross-referenced and not counted again.'],'limitations':['This is a research proposal, not 72 completed formal catalogue cards.','Older or truncated catalogue records can still conceal semantic overlaps; specific close matches are documented.','No guarantee that every later solution was found, and no independent validation of newly claimed proofs.','The requested five-to-ten new fundamental problems in each category was not achieved.']}
(D/'validation.json').write_text(json.dumps(meta,ensure_ascii=False,indent=2)+'\n')
gap={
4:'P versus BPP, L versus BPL, general PIT, explicit Ramsey graphs, tree codes and prime construction already have catalogue records; their restatements are not new additions.',
5:'Frege lower bounds and optimal proof-system questions already occur in the catalogue. Fixed-system variants were not multiplied to meet a quota.',
10:'Many natural landmark candidates were either already solved in the stated model or belonged primarily to the large geometry/optimization groups.',
11:'The 2-approximate-superstring suggestion was withheld because the existing SCS source already includes the stronger greedy conjecture. General word equations with length constraints are cross-referenced below.',
14:'Recent progress essentially closes the main adaptivity exponent gap for Boolean monotonicity testing. Narrow residual improvements were excluded.',
15:'The maximum-coordinate pure-DP query-release conjecture has a July 2026 claimed solution. The retained entry is the separate Euclidean-error problem. Several major private-learning questions are already present.',
19:'Word equations with linear length constraints are already in the large-category proposal and are cross-referenced, not counted again.',
20:'Uniform tractable CSP and finite controllability already occur in the catalogue. A 2025 publication claims a logic capturing PTIME; that claim was not adjudicated in this pass, so the problem is held out.',
21:'The list separates general Martin\'s conjecture from solved restricted cases and does not turn the various randomness notions into a quota of nearby variants.',
22:'Complementation of d-DNNF already occurs in the catalogue, the SDD/d-DNNF succinctness separation is known, and finite SROIQ satisfiability is decidable. Unverified broad ontology questions were not padded into the list.',
24:'Low-degree lower bounds are evidence about restricted algorithms, not resolutions of the unrestricted computational thresholds.',
25:'No additional orphan problem passed both the fundamental-importance test and the agreed scope policy. General combinatorics was not restored through Miscellaneous; a recent sunflower proof claim was held for separate adjudication.'}
lines=['# Additional fundamental problems for the current small categories','',
'Research date: **10 September 2026**. Scope: the **25 small categories in the current CATEGORY_PLAN.md**, not the earlier category list.','',
f'**{len(a)} new suggestions** survived this pass. **{len(shared)} further strong problems are already in the large-category proposal** and are cross-referenced instead of counted twice. The request for **5–10 additions in every category was not met**. This is not a claim that no more qualifying problems exist; it records the limits of this research pass.','',
'Entries are ordered within each category by editorial importance: foundational significance, breadth of consequences and centrality to the field. No routine follow-up was added to fill a numerical gap. Each entry supplies a concrete target, an importance rationale, primary sources and a novelty note. Statements below are proposal sketches, not completed self-contained benchmark cards.','',
'Novelty was checked against all **6,513 catalogue records**, including source excerpts and differently classified entries, with full-source inspection for identified close matches. The final snapshot and limitations are recorded in [validation.json](validation.json); keyword hits are preserved in [final-novelty-audit.json](final-novelty-audit.json). Neither absence of a keyword nor a recent citation alone guarantees novelty or current open status.','',
'## Coverage','', '| # | Current small category | New | Missing to reach 5 |','|---|---|---:|---:|']
for c in range(1,26):lines.append(f"| {c} | {SMALL[c-1]} | {counts[c]} | {max(0,5-counts[c])} |")
for c in range(1,26):
 lines += ['',f'## {c}. {SMALL[c-1]}','',f'**New suggestions: {counts[c]}.**']
 for x in [x for x in a if x['category']==c]:
  lines += ['',f"**{x['rank_in_category']}. {x['title']}**",'',x['question']+' '+ ' '.join(f"[Primary source {j+1}]({u})." for j,u in enumerate(x['sources'])),'',f"**Why fundamental:** {x['importance']}",'',f"**Novelty check:** {x['novelty_note']}"]
 for x in [x for x in shared if x['category']==c]:
  lines += ['',f"**Already proposed elsewhere — not counted: {x['title']}.** {x['question']} See the [large-category proposal](../fundamental-additions-20260910/REPORT.md). Its natural small-category placement would be here."]
 if c in gap:lines += ['',f'**Selection limit:** {gap[c]}']
 elif counts[c]<5:lines += ['','**Selection limit:** This pass did not substantiate five additional independent landmark problems. Existing entries and weaker variants were not counted to make up the difference.']
lines += ['','## Important exclusions and status corrections','',
'- Polynomial kernels for Directed Feedback Vertex Set and Vertex Planarization already occur as **TCS-6379/TCS-6441** and **TCS-5901/TCS-0813**, respectively.',
'- Core non-emptiness in approval elections is already in the full source of **TCS-4249**.',
'- Uniform algorithms for tractable CSPs are already **TCS-0504**.',
'- General additive-chores EFX has a [June 2026 counterexample claim](https://arxiv.org/abs/2606.08872); it is excluded.',
'- The maximum-coordinate pure-DP query-release conjecture has a [July 2026 solution claim](https://arxiv.org/abs/2607.20418); it is excluded. The retained Euclidean-error question is different.',
'- The [2025 monotonicity-testing lower bound](https://arxiv.org/abs/2511.04558) essentially closes the previously large adaptive-query exponent gap.',
'- The [2025 ICPT publication](https://arxiv.org/abs/2005.04598) claims a logic capturing PTIME; this pass did not independently assess the proof and does not present the general problem as unqualified open.',
'- [2026 sunflower proof claim](https://arxiv.org/abs/2606.02667): held for separate verification, not used as a confirmed-open Miscellaneous entry.','',
'Other rejections and holds are in [rejections.json](rejections.json). Brainstorming files are not accepted problem lists.','',
'## Deliverable and validation','',
'The retained machine-readable list is [shortlist.json](shortlist.json); a compact export is [shortlist.csv](shortlist.csv). No new catalogue cards were published. The existing site, taxonomy, problem IDs and concurrent research work were preserved.','']
(D/'proposal.md').write_text('\n'.join(lines))
with (D/'shortlist.csv').open('w',newline='') as f:
 w=csv.DictWriter(f,fieldnames=['category','category_name','rank_in_category','title','question','importance','sources','novelty_note'])
 w.writeheader()
 for x in a:
  row={k:x[k] for k in w.fieldnames};row['sources']=' | '.join(x['sources']);w.writerow(row)
print(json.dumps({'new':len(a),'shared':len(shared),'counts':dict(sorted(counts.items())),'catalog_version':meta['catalog_version'],'quota_met':meta['quota_met']},indent=2))

