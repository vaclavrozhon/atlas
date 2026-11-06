"""Apply the owner's logarithmic-exponent target to TCS-7174."""
import copy
import json
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
HERE = Path(__file__).resolve().parent
path = ROOT / 'data/cards/TCS-7174.json'
before_path = HERE / 'before.json'
if not before_path.exists():
    before_path.write_text(path.read_text())
before = json.loads(before_path.read_text())
card = copy.deepcopy(before)

card['title'] = 'Logarithmic exponent of integer multiplication'
card['question_type'] = 'numerical_value'
card['formal'] = r'''For a uniform deterministic multitape Turing machine \(M\) that exactly multiplies every pair of \(n\)-bit nonnegative binary integers, let \(t_M(n)\) be its worst-case transition count. Determine to absolute error at most \(1/100\) the logarithmic-overhead exponent
\[
\alpha_{\mathrm{mult}}=\inf\left\{a\in\mathbb R_{\ge0}:\exists M\ \exists C>0\ \exists n_0\in\mathbb N_{\ge1}\ \forall n\ge n_0,\quad t_M(n)\le Cn\bigl(\log_2(n+2)\bigr)^a\right\}.
\]
The machine model and quantifiers are specified below. The linear factor \(n\) accounts for the bit scale of the input and output; the requested number describes the power of the logarithmic overhead. The output is the exact product, explicitly written in \(2n\) bits. The exponent lies in \([0,1]\); attaining its infimum is not required.'''

old = r'The notation \(o(n\log n)\) means \(\lim_{n\to\infty}t_M(n)/(n\log_2(n+2))=0\). '
assert old in card['definitions']
card['definitions'] = card['definitions'].replace(old, '')
card['definitions'] += r'''

The infimum ranges over logarithmic powers attainable as upper bounds by correct machines in this model. For each candidate exponent \(a\), the machine \(M\), multiplicative constant \(C\) and threshold \(n_0\) may depend on \(a\), but not on the input length or input values. One fixed machine must meet each asserted bound at every sufficiently large length and remain correct at all lengths. It is not permissible to minimize separately over a different hardcoded program for each \(n\).

The explicit output requires \(\Omega(n)\) transitions. The known \(O(n\log n)\) algorithm makes the defining set nonempty and gives \(0\le\alpha_{\mathrm{mult}}\le1\). This definition neither assumes an ordinary growth limit nor requires one machine to attain the infimum. Exponent zero does not by itself assert a linear-time algorithm: it allows separate upper bounds with arbitrarily small positive powers of \(\log n\). Multiplicative constants and iterated-logarithmic factors are not part of the requested numerical accuracy.'''

card['answer_criterion'] = r'''Supply an unambiguously specified real number \(b\) and a complete, mathematically correct Lean-checked proof that \(|b-\alpha_{\mathrm{mult}}|\le1/100\), in the stated uniform deterministic multitape model. A certified enclosing interval of width at most \(1/50\) qualifies via its midpoint; both endpoints must be justified. An exact value also qualifies. Upper bounds must respect the order of quantifiers: each machine is fixed across all input lengths. A lower bound must cover every correct machine in the model. A lower bound on the infimum does not require an attained optimal time or an eventual matching lower bound at every input length. The answer concerns the logarithmic exponent after the linear factor \(n\), not a polynomial exponent of \(n\), a matching full running-time function, or a rounded estimate without a proved error bound.'''

card['context_blocks'][0]['text'] = r'For example, \(11_2\) multiplied by \(11_2\) is \(1001_2\): the input integers are 3 and 3, and the exact product is 9. The task scales to arbitrarily long binary inputs. The numerical question measures how much logarithmic overhead is necessary beyond the linear cost of handling the input and output bits.'
card['context_blocks'][2]['text'] = r'Harvey and van der Hoeven proved an \(O(n\log n)\) algorithm in the multitape Turing model in 2021. This establishes \(\alpha_{\mathrm{mult}}\le1\), but does not determine the optimal exponent. Their 2025 paper records the absence of an unconditional superlinear lower bound in this unrestricted model.'
card['context_blocks'].append({
    'title': 'What the logarithmic exponent measures',
    'text': r'The exponent records the power of \(\log n\) multiplying the linear term. For example, a bound \(n(\log n)^{1/2}\) would give \(\alpha_{\mathrm{mult}}\le1/2\). The rates \(n\log n\) and \(n\log n/\log\log n\) both have logarithmic growth exponent one, so distinguishing their iterated-logarithmic factors is outside this target. The infimum convention also avoids assuming that a single optimal machine exists.'
})
if 'context' in card:
    card['context'] = '\n\n'.join(block['text'] for block in card['context_blocks'])

card['working_summary'] = {
    'sentences': [
        'The inputs are two binary integers and the output is their exact product.',
        'Time counts elementary transitions of one fixed deterministic multitape Turing machine.',
        'The requested exponent is the infimum of attainable powers of the logarithmic overhead beyond linear time.',
        'This exponent lies between zero and one and must be determined to absolute accuracy 0.01.',
        'A machine attaining the infimum and matching iterated-logarithmic factors are not required.'
    ],
    'basis': 'saved_sources',
    'source_basis': 'owner_authorized_logarithmic_exponent_review',
    'written_on': '2026-11-06',
    'source_refs': ['publisher', 'transpose']
}
reason = ('Owner explicitly selected the logarithmic exponent of integer multiplication. '
          'Retained the necessary linear bit-length factor: n (log n)^a, with absolute 0.01 accuracy. '
          'This supersedes the earlier below-n-log-n binary target and the still earlier full-function target.')
card['updated_at'] = datetime.now(timezone.utc).isoformat(timespec='seconds')
card['formulation_reviewed_on'] = '2026-11-06'
card['statement_review'] = {
    'status': 'revised', 'reviewed_on': '2026-11-06', 'remaining_issue': '',
    'notes': [reason, 'Preserved the exact deterministic multitape model, global program uniformity and explicit output cost.'],
    'scope': 'Targeted formulation and source-bound check; no new catalogue-wide solvedness audit.'
}
card['quality_review'] = {
    'reviewed_on': '2026-11-06', 'state': 'revised', 'reference_card': 'TCS-0001',
    'changes': card['statement_review']['notes'],
    'checked_sources': ['https://annals.math.princeton.edu/2021/193-2/p04', 'https://arxiv.org/abs/2503.22848'],
    'scope': card['statement_review']['scope']
}
for field in ('id', 'area', 'importance', 'status', 'evidence', 'benchmark_eligibility', 'status_note'):
    assert card.get(field) == before.get(field), field
assert len(card['working_summary']['sentences']) == 5
path.write_text(json.dumps(card, ensure_ascii=False, indent=2) + '\n')
print('Revised TCS-7174 to the finite logarithmic-overhead exponent; selection unchanged.')
