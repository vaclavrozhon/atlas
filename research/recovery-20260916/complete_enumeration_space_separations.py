"""Choose a noncircular hypothesis for the two enumeration space separations."""
import json,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT/'research/card-completion-20260913'))
from complete_review import complete,block
from review_queue import read_claims
identifier='TCS-7084';claim=read_claims(ROOT)[identifier]
card=json.loads((ROOT/'data/cards'/f'{identifier}.json').read_text())
definitions=card['definitions']
start=definitions.index('The source’s computation model')
end=definitions.index('\n\nThe class ',start)
definitions=definitions[:start]+r'''Use uniform deterministic random-access machines with a fixed finite program, integer registers, direct and indirect addressing, branching, comparison, addition, subtraction and multiplication. An arithmetic or comparison instruction on integers \(a,b\) costs \(1+\lceil\log_2(|a|+|b|+1)\rceil\); other basic instructions cost one. Input is explicitly encoded in finitely many initial registers, and all other registers initially contain zero. This fixes the source's bit-sensitive arithmetic and unit-cost random access conventions.

Space counts all bits of the registers through the largest accessed address, assigning at least one bit to each integer including zero. It also counts all retained output buffers and machine counters. Charging the stored input changes this by only a polynomial amount. A completed output is a finite bit string on an external write-only stream; the stream supplies no readable memory. Charge for writing its bits. There is no randomization, oracle or advice. The RAM model matters for unrestricted-space polynomial delay, where a growing dictionary can still support fast random access.''' +definitions[end:]
definitions+=r'''

The selected hypothesis is exactly \(\mathrm P\ne\mathrm{NP}\). Both separations must follow from this same hypothesis:
\[
\mathrm P\ne\mathrm{NP}\quad\Longrightarrow\quad
\bigl(\mathrm{DelayP}\setminus\mathrm{DelayP}^{\mathrm{poly}}\ne\varnothing\bigr)
\ \land
\bigl(\mathrm{IncP}\setminus\mathrm{IncP}^{\mathrm{poly}}\ne\varnothing\bigr).
\]
The two witness relations may differ. Each relation and its algorithms are fixed before inputs; the polynomial space bound is in input length alone, not the number of outputs. The hypothesis cannot be replaced by a stronger conjecture about enumeration, by \(\mathrm{EXP}\ne\mathrm{PSPACE}\), or by the desired separations themselves.'''
contexts=card['context_blocks'][:6]+[
 block('The historical question allowed an unspecified complexity hypothesis. This card selects P ≠ NP and therefore asks a particular converse to the known collapse under P = NP. It does not claim that this chosen implication appears verbatim in the source.'),
]
complete(identifier,dict(
 title='Does P ≠ NP imply both polynomial-space enumeration separations?',
 status='source_open',criterion='resources',question_type='yes_no',
 formal=r'''Is the following implication true for enumeration problems with polynomial-time checkable, polynomial-length solutions?
\[
\mathrm P\ne\mathrm{NP}\quad\Longrightarrow\quad
\left(\mathrm{DelayP}\ne\mathrm{DelayP}^{\mathrm{poly}}
\ \land\,
\mathrm{IncP}\ne\mathrm{IncP}^{\mathrm{poly}}\right).
\]
Here DelayP permits polynomial delay and unrestricted working space, IncP permits incremental polynomial time and unrestricted working space, and the superscript poly requires the same enumerator to obey the timing guarantee while using only polynomial space in the input length. All classes use the deterministic RAM model defined below.''',
 definitions=definitions,
 answer_criterion='Give a complete mathematically correct Lean-checked proof of the stated implication or of its logical negation. An affirmative proof must establish, under P ≠ NP, a polynomially checkable and polynomially balanced relation for each separation, an enumerator with the unrestricted timing guarantee, and the impossibility of every enumerator simultaneously obeying that timing guarantee and input-polynomial space. A negative proof must establish P ≠ NP together with equality of at least one of the two class pairs. A separation only for uncheckable solution relations, a restriction on output order or access to a black-box generator, or the space cost of a particular algorithm does not satisfy the target.',
 why='The question tests whether space can be an essential resource for efficient enumeration even when each solution is short and easy to verify. Fixing P ≠ NP asks whether this familiar decision-complexity separation already forces a time–space distinction for producing many answers.',
 importance=dict(score=81,method='editorial',reason='A structural resource-separation question for two major enumeration classes, relating simultaneous output efficiency and memory bounds to P versus NP.'),
 source_formulation=dict(text='Open problem 4.1 asks for both separations under a complexity hypothesis but leaves that hypothesis unspecified. This card selects P ≠ NP as the exact antecedent while retaining EnumP verification and solution-length requirements.',caption='Enumeration Complexity: Incremental Time, Delay and Space, §4.1 and Open problem 4.1, printed p.26 / PDF p.32.',citation='primary',format='editorial_paraphrase'),
 references=card['references'],context_blocks=contexts,progress=card['progress'],
),[
 'Completed the pending hypothesis choice with the exact implication from P ≠ NP to both source separations.',
 'Applied the announced recommended editorial default after an unanswered optional question, without recording user confirmation.',
 'Retained arbitrary output order, duplicate-free complete enumeration, polynomial verification, polynomial solution length and the full initial/terminal timing conditions.',
 'Specified arithmetic charges and the source RAM space accounting; polynomial space must hold for the same algorithm as the timing guarantee.',
 'Distinguished the 2026 polynomial-space regularization theorem and larger uncheckable-solution frameworks, assessed importance and supplied the full Lean-checked criterion.',
],[
 'Re-read the habilitation §2.2 RAM conventions and §4.1 including Open problem 4.1; retained the prior checked P = NP collapse via prefix search.',
 'Re-read the WEPA extended abstract Theorem 5 and Open Problems 1–2: the EXP/PSPACE construction is outside the efficiently checkable relation target.',
 'Re-read the published July 2026 regularization Theorem 4.2 and its proof; both its classes already require polynomial space.',
 'Bounded primary-source searches through 17 September 2026 found no proof or refutation of the selected implication. The supporting hypothesis is an editorial specialization of the broader source request.',
], 'The original conditional separation program remains open in the checked sources. This card now asks the precise implication from P ≠ NP, an announced editorial default after the optional hypothesis question received no reply. The July 2026 regularization theorem equates two classes already constrained to polynomial space, and the EXP/PSPACE construction drops efficient verification. Neither resolves the selected implication; later-work checks through 17 September 2026 were bounded.',summary=[
 'An enumeration problem has polynomial-length solutions whose validity can be checked in polynomial time.',
 'Polynomial delay bounds each wait for the next answer, while incremental polynomial time bounds the cost of every initial segment.',
 'The question asks whether P ≠ NP forces both timing classes to become strictly weaker when the same algorithm must also use input-polynomial space.',
 'Output order is unrestricted, and the two separations may have different witness problems.',
 'Known regularization and broader-framework results do not settle this precise implication, whose complete proof or refutation must be Lean-checked.',
],expected_sha256=claim['input_sha256'],claim_token=claim['token'])
