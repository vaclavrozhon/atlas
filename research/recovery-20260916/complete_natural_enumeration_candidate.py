"""Finish the previously read natural-enumeration request with an explicit candidate."""
import json,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT/'research/card-completion-20260913'))
from complete_review import complete,ref,block,progress
from review_queue import read_claims
identifier='TCS-7082';claim=read_claims(ROOT)[identifier]
card=json.loads((ROOT/'data/cards'/f'{identifier}.json').read_text())
definitions=card['definitions'].replace('The following definitions fix the verified background, without supplying the missing criterion of naturalness. ','')
start=definitions.index('The source uses deterministic random-access machines')
end=definitions.index('\n\nPut ',start)
definitions=definitions[:start]+r'''Enumeration algorithms are uniform deterministic random-access machines with a fixed finite program and integer registers, direct and indirect addressing, branching, comparison, addition, subtraction and multiplication. Each arithmetic or comparison instruction on integers \(a,b\) costs \(1+\lceil\log_2(|a|+|b|+1)\rceil\); other basic instructions cost one. This is the source's bit-sensitive arithmetic convention, with unit-cost random access. Register contents initially vanish, except for an explicit finite encoding of the input. Output writes a finite binary string to an external stream, which cannot be read back as free storage. Charge for writing its bits as well; solution lengths are polynomial in input length. There is no randomization, oracle, advice or imposed working-space bound. We include initial and terminal work. An empty solution set must be recognized within polynomial input time.''' +definitions[end:]
definitions+=r'''

Write \(\mathrm{Dom}_t\) for the enumeration relation for \(K_t\)-free graphs just defined, with \(t\ge3\) fixed. The selected assertion is
\[
\mathrm{TFNP}\ne\mathrm{FP}\quad\Longrightarrow\quad
\exists t\ge3:\ \mathrm{Dom}_t\in\mathrm{OutputP}\setminus\mathrm{IncP}.
\]
Here \(\mathrm{TFNP}\ne\mathrm{FP}\) means that at least one polynomially balanced, polynomial-time checkable total search relation has no deterministic polynomial-time witness selector. No completeness assumption about TFNP is made. The existential quantifier chooses one fixed integer \(t\), not an input-dependent clique bound. Failure of IncP excludes every uniform deterministic enumerator and every fixed pair of polynomial exponents in the definition. No extra informal test of naturalness or required search-reduction notion is part of this selected target.'''
contexts=card['context_blocks'][:5]+[
 block('This card adopts the graph candidate suggested in the source and asks for its conditional separation under TFNP ≠ FP. That is a precise specialization of the source’s broader natural-example request; the known abstract separation does not ensure that this particular candidate witnesses it.'),
 block('The WADS 2025 paper gives polynomial delay and polynomial space for chordal bipartite graphs. Its introduction still lists the bounded-clique-number result as output-polynomial. An upper bound on that special bipartite subclass does not cover all graphs with a fixed forbidden clique.','chordal'),
]
complete(identifier,dict(
 title='A natural OutputP versus IncP separation from clique-free domination',
 status='source_open',criterion='resources',question_type='yes_no',
 formal=r'''Does \(\mathrm{TFNP}\ne\mathrm{FP}\) imply that there is a fixed integer \(t\ge3\) for which enumerating all inclusion-minimal dominating sets of \(K_t\)-free graphs belongs to \(\mathrm{OutputP}\) but not to \(\mathrm{IncP}\)?

The graph is explicitly given. Enumeration is deterministic, without repetitions and in any order. Total output-polynomial time is already known for every fixed \(t\); the question is whether this specific family supplies the conditional failure of incremental polynomial time.''',
 definitions=definitions,
 answer_criterion='Give a complete mathematically correct Lean-checked proof or refutation of the stated implication. An affirmative answer must establish the conditional existence of a fixed t, retain the output-polynomial upper bound and rule out every incremental-polynomial enumerator for that relation. A negative answer must establish TFNP ≠ FP together with incremental-polynomial enumerability for every fixed t ≥ 3. The existing padded construction for an arbitrary enumeration relation does not settle this candidate-specific implication, and neither does slow behavior of a particular domination algorithm.',
 why='This would locate the gap between efficient total enumeration and efficient initial output in a standard graph problem. The concrete candidate tests whether a known abstract total-search separation can be realized without constructing artificial padded solution sets.',
 importance=dict(score=75,method='editorial',reason='A concrete natural witness for a central distinction in enumeration complexity, connecting graph enumeration to the hardness of total search rather than only to an artificial class-separation construction.'),
 source_formulation=dict(text='Open problem 3.1 requests a natural OutputP problem outside IncP and suggests minimal dominating sets in graphs excluding a fixed clique. This card adopts that candidate and asks for the separation under TFNP ≠ FP.',caption='Enumeration Complexity: Incremental Time, Delay and Space, Open problem 3.1, printed p.16 / PDF p.22.',citation='primary',format='editorial_paraphrase'),
 references=card['references']+[
 ref('chordal','Enumerating Minimal Dominating Sets and Variants in Chordal Bipartite Graphs','Emanuel Castelo; Oscar Defrain; Guilherme C. M. Gomes',2025,'https://doi.org/10.4230/LIPIcs.WADS.2025.15','Abstract p.15:1; §1 known graph classes p.15:2 and Theorem 18 p.15:10; polynomial-delay and polynomial-space result for chordal bipartite graphs'),
 ],
 context_blocks=contexts,
 progress=card['progress']+[progress('2025','The WADS paper improves the chordal-bipartite subclass to polynomial delay and space, while its introduction retains the bounded-clique-number output-polynomial benchmark.','chordal')],
),[
 'Completed the previously pending naturalness choice by adopting the source’s specific clique-free domination candidate and the hypothesis TFNP ≠ FP.',
 'Applied the announced recommended editorial default after an unanswered optional question; did not record it as user confirmation.',
 'Retained the earlier individually checked enumeration definitions and specified the source RAM arithmetic charges exactly.',
 'Fixed the existential clique bound outside the input and distinguished the candidate implication from the known abstract equivalence.',
 'Checked the WADS 2025 subclass improvement, assessed importance and supplied a full Lean-checked logical answer criterion.',
],[
 'Re-read the habilitation §2.2 computation and arithmetic-cost conventions, Proposition 3.4 and Open problem 3.1.',
 'Re-read Capelli–Strozecki Proposition 9 with its padding argument and Bonamy et al. Theorem 1.1 with its fixed-t convention.',
 'Read Castelo–Defrain–Gomes WADS 2025 abstract, §1 classification discussion and Theorem 18. It does not supply an incremental algorithm for all K_t-free graphs.',
 'Bounded primary-source searches through 17 September 2026 found no resolution of the selected conditional graph-candidate implication.',
], 'The source leaves the natural-example request open and explicitly proposes this graph candidate. The card now selects that candidate with the stated TFNP ≠ FP hypothesis, an announced editorial default after an unanswered optional question. Output-polynomial enumeration is known for every fixed t, but the checked later subclass result does not settle incremental enumeration for all K_t-free graphs. The exact conditional implication is an editorial specialization, not a theorem claimed by the source.',summary=[
 'For a fixed forbidden clique size, the task is to list every inclusion-minimal dominating set of the input graph once.',
 'An algorithm with total running time polynomial in the input and the entire output is already known.',
 'The question asks whether TFNP ≠ FP forces some fixed clique size for which no algorithm produces every initial output segment in incremental polynomial time.',
 'This selects the concrete graph candidate suggested by the source instead of imposing an undefined condition of naturalness.',
 'The existing abstract separation and algorithms for smaller graph classes do not settle this implication, whose proof or refutation must be Lean-checked.',
],expected_sha256=claim['input_sha256'],claim_token=claim['token'])
