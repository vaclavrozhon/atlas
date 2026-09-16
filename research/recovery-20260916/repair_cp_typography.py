"""Repair the escaped-math transcription in the first recovery completion."""
import ast
import fcntl
import hashlib
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / 'scripts'))
from catalog_exports import atomic
from card_schema import reader_record
from publish import validate_record

fields = dict(
    formal=r'''Do there exist positive integers \(C,k\) such that, for every CNF formula \(F\) and every Cutting Planes refutation \(\pi\) of \(F\), there is a Cutting Planes refutation \(\pi'\) of the same formula satisfying
\[
L(\pi')\le C\bigl(N(F)+L(\pi)\bigr)^k,\qquad
M(\pi')\le C\bigl(N(F)+L(\pi)\bigr)^k?
\]
Both refutations use exactly the rules and variables defined below. The original coefficients are unrestricted, proof lines may be reused, and there is no space restriction. A negative answer is the full quantified negation: for every pair \(C,k\ge1\), some \(F,\pi\) admit no replacement satisfying both bounds. The violating instance may depend on \(C,k\).''',
    definitions=r'''A CNF formula \(F\) is a finite list of clauses over Boolean variables \(x_1,\ldots,x_n\), each taking values in \(\{0,1\}\). Each clause is a finite set of positive or negative literals. Duplicate literal occurrences are removed; tautological clauses and the empty clause are allowed. Variables are consecutively relabeled, and only variables occurring in the formula are counted. The empty conjunction is true and the empty clause is false. Fix the combinatorial input size
\[
N(F)=1+n+|F|+\sum_{C\in F}|C|.
\]
This measure is polynomially equivalent to the bit length of an explicit clause-list encoding with binary variable indices. The choice fixes the size parameter, rather than granting a succinct circuit encoding of the input.

A Cutting Planes line is a normalized integer inequality \(\sum_{i=1}^{n}a_i x_i\ge b\), with every \(a_i,b\in\mathbb Z\). Zero coefficients may be omitted in writing, but the coefficient vector is defined on all \(n\) variables. A clause with positive-variable set \(P\) and negative-variable set \(M\) contributes the input inequality \(\sum_{i\in P}x_i-\sum_{i\in M}x_i\ge1-|M|\). If both signs occur, their coefficients cancel. Boolean axioms are \(x_i\ge0\) and \(-x_i\ge-1\); the harmless constant axiom \(0\ge0\) is also permitted. No extension variables, semantic inference rules, or extra assumptions are allowed.

A proof is a finite sequence of lines. Each line is an input inequality, a Boolean or constant axiom, or follows from earlier lines by one of these rules: addition of two inequalities; multiplication of one inequality by a positive integer; or division by a positive integer \(d\) that divides every coefficient on its left side, replacing \(\sum_i a_i x_i\ge b\) by \(\sum_i(a_i/d)x_i\ge\lceil b/d\rceil\). All sums are put in normalized form by collecting coefficients. Earlier lines may be reused arbitrarily many times, so these are general directed-acyclic proofs, not tree-like proofs. A refutation ends with \(0\ge1\). Its length \(L(\pi)\) is its number of lines, including input and axiom occurrences. No bound is placed on the number of lines simultaneously retained. In particular, proof length is not algorithmic runtime, total coefficient bit length, or a memory measure.

Define the magnitude of a proof by
\[
M(\pi)=\max\bigl(\{1\}\cup\{|a_i|,|b|:\text{a line }\sum_i a_i x_i\ge b\text{ occurs in }\pi\}\bigr).
\]
The original proof may have arbitrarily large integer coefficients, written in binary. The replacement proof must bound the numerical magnitudes of all line coefficients and right-hand sides, not merely their bit lengths. Multiplication and division annotations are required to make the displayed inferences valid; the magnitude measure concerns the inequalities themselves. Every inference, including intermediate multiplication lines, counts toward length and is subject to the replacement bound.

The common polynomial bound in this card can equivalently be written \(C(N+L)^k\), for positive integers \(C,k\) independent of the formula and original proof. The same \(C,k\) bound both replacement length and coefficient magnitude. This is an existential comparison of proofs: it does not additionally require a polynomial-time algorithm that constructs the replacement proof from the original one. The parameter \(N+L\), one common polynomial, and the absence of a space bound are the user's explicit specification of the source question. Literature also discusses bounds polynomial only in input size and polynomial-time proof transformations; those additional requirements are not silently imposed here.''',
    answer_criterion=r'''Supply a complete Lean-checked proof of the displayed universally quantified simulation assertion or its full negation, for the precise syntactic proof system, \(N\), \(L\), and \(M\) defined here. An affirmative answer must establish one pair \(C,k\) working simultaneously for every input formula and every unrestricted-coefficient refutation. A negative answer must establish failure for every such pair; failure of one transformation or a lower bound with an additional memory restriction is insufficient. No numerical tolerance changes this proposition. A bibliography, experimental proof search, or a proof only for tree-like refutations does not substitute for the full theorem.''',
)

with (ROOT / '.publish.lock').open('a') as lock:
    fcntl.flock(lock, fcntl.LOCK_EX)
    path = ROOT / 'data/cards/TCS-6770.json'
    card = json.loads(path.read_text())
    before = hashlib.sha256(path.read_bytes()).hexdigest()
    if card['formal'] != fields['formal']:
        card.update(fields)
        note = 'Restored LaTeX delimiters and commands lost in the authoring-script string transport; mathematical target unchanged.'
        card['quality_review']['changes'].append(note)
        card['statement_review']['notes'].append(note)
        validate_record(reader_record(card, json.loads((ROOT/'data/criteria.json').read_text())), path,
                        json.loads((ROOT/'data/criteria.json').read_text()))
        output = json.dumps(card, ensure_ascii=False, indent=2)+'\n'
        atomic(path, output)
        queue_path = ROOT/'research/card-completion-20260913/queue.json'
        queue = json.loads(queue_path.read_text())
        row = next(r for r in queue['records'] if r['id']=='TCS-6770')
        assert row['output_sha256']==before
        row['output_sha256']=hashlib.sha256(output.encode()).hexdigest()
        atomic(queue_path,json.dumps(queue,ensure_ascii=False,indent=2)+'\n')
        with (ROOT/'research/card-completion-20260913/reviews.jsonl').open('a') as ledger:
            ledger.write(json.dumps(dict(id='TCS-6770',date='2026-09-16',
                outcome='typography_repair',changes=[note],input_sha256=before,
                output_sha256=row['output_sha256']))+'\n')
    # Restore the retained authoring script as well, without rerunning completion.
    script = ROOT/'research/recovery-20260916/complete_cp.py'
    source=script.read_text()
    lines=source.splitlines(keepends=True)
    replacements=[]
    for node in ast.walk(ast.parse(source)):
        if isinstance(node,ast.Assign):
            for target in node.targets:
                if isinstance(target,ast.Name) and target.id in ('formal','definitions'):
                    replacements.append((node.lineno-1,node.end_lineno,
                                         target.id+' = '+repr(fields[target.id])+'\n'))
        if isinstance(node,ast.keyword) and node.arg=='answer_criterion':
            replacements.append((node.lineno-1,node.end_lineno,
                                 '    answer_criterion='+repr(fields['answer_criterion'])+',\n'))
    for start,end,value in sorted(replacements,reverse=True):
        lines[start:end]=[value]
    atomic(script,''.join(lines))
print('Repaired TCS-6770 mathematical typography and synchronized its audit hash.')
