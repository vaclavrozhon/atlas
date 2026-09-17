"""Complete the fixed-capacity deterministic dynamic dictionary question."""
import sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];sys.path.insert(0,str(ROOT/'research/card-completion-20260913'))
from complete_review import complete,ref,block,progress,DATE
from review_queue import read_claims
identifier='TCS-7331';claim=read_claims(ROOT)[identifier]
notes=[
 'Retained the approved fixed-capacity, logarithmic-word model, linear space, constant worst-case queries and constant amortized updates.',
 'Expanded the quantifier order, exact interface, empty initialization, all-prefix aggregate cost and prohibition of advance knowledge of future operations.',
 'Removed irrelevant randomized-machine boilerplate and explicitly counted all workspace, rebuilt tables and retained operation information.',
 'Read the source dictionary discussion and checked uniform deterministic tradeoffs, the restricted nature of classical deterministic lower bounds, and recent static/FID results.',
 'Distinguished a negative answer for at least one fixed universe exponent from an unnecessarily stronger lower bound for every exponent or every operation.',
 'Preserved importance 94, related static-construction card and Data structures category, with complete Lean verification required.',
]
sources=[
 'Read Pătrașcu, 2007 Research Statement within the job-application statements PDF, printed/PDF pp. 9–10, especially the two dictionary paragraphs at the top of p. 10. They identify the constant-time deterministic dictionary problem and collaboration with Thorup. The source is broad; the card retains the existing editorial specialization rather than attributing its exact capacity and instruction conventions verbatim to the source.',
 'Read the primary institutional abstract of Dietzfelbinger–Karlin–Mehlhorn–Meyer auf der Heide–Rohnert–Tarjan, Dynamic Perfect Hashing: Upper and Lower Bounds, Princeton TR-310-91, and checked its publication metadata for SIAM Journal on Computing 23(4), 1994, pp. 738–761. The upper bound is randomized; the deterministic lower bound covers a specified class of hashing schemes, not arbitrary word-RAM programs.',
 'Read the primary IT University of Copenhagen abstract and publication metadata for Milan Ružić, Uniform deterministic dictionaries, ACM Transactions on Algorithms 4(1), 2008, DOI 10.1145/1328911.1328912. It states uniform deterministic lookup/update tradeoffs O(t) versus amortized O(n^(1/t)), with division used for updates. The full journal proof was not independently audited.',
 'Read the primary abstract and version history of Hu–Liang–Yu–Zhang–Zhou, arXiv:2412.10655v2 of 26 March 2025, and checked the STOC 2025 proceedings entry. Its optimal-space constant-query dictionary is static and includes random hash bits; it does not assert the fully deterministic online update target.',
 'Read the primary abstract and version history of Domingues, arXiv:2603.23119v1 of 24 March 2026, marked for STOC 2026. The dynamic fully indexable dictionary supports rank/select and updates with a log_w n term, uses a small constructible precomputed table, and does not state constant updates at logarithmic word size. No independent proof audit undertaken.',
 f'Bounded primary-source searches through {DATE} found no verified resolution of the selected dynamic target. TCS-6586 concerns deterministic static construction and remains a distinct card.',
]
complete(identifier,dict(
 criterion='resources',question_type='yes_no',
 formal=r'''Is the following statement true? For every fixed integer \(c\ge2\), there exist a uniform deterministic word-RAM program \(A_c\) and a constant \(C_c\ge1\) such that, for every integer capacity \(N\ge2\), with word size
\[
 w=\lceil c\log_2(N+2)\rceil,
\]
the program maintains a dictionary of at most \(N\) word-sized key–value pairs, starting empty, and satisfies all of the following guarantees for every valid online operation sequence: initialization costs at most \(C_cN\) instructions; at most \(C_cN\) words of space are used at any time; every lookup costs at most \(C_c\) instructions; and initialization together with every finite prefix containing \(q\) lookups and \(u\) insertions or deletions costs at most \(C_c(N+q+u)\) instructions? All answers must be exact.''',
 definitions=r'''The key and value universe is \(U_w=\{0,\ldots,2^w-1\}\). A dictionary is a partial function \(D:U_w\rightharpoonup U_w\) with at most \(N\) keys in its domain. The capacity \(N\) and word size \(w\) are supplied at initialization and do not change during a sequence. Initially the domain is empty.

An operation is one of the following. \(\operatorname{Insert}(x,v)\) requires \(x\notin\operatorname{dom}(D)\) and \(|\operatorname{dom}(D)|<N\), and changes \(D\) by assigning \(D(x)=v\). \(\operatorname{Delete}(x)\) requires \(x\in\operatorname{dom}(D)\) and removes that key. \(\operatorname{Lookup}(x)\), with any \(x\in U_w\), returns its exact stored value if present and otherwise a distinguished absent marker. The marker is separate from every word value, for example represented by a presence bit and a value word. Replacing a value can be expressed by deletion followed by insertion; it is not an extra operation requiring a separate guarantee.

A valid finite sequence respects the operation preconditions at every step. There is no bound on its length, and the same keys may be inserted and deleted repeatedly. Operations arrive one at a time. Each must terminate and return its result before the next arrives; the program has no advance access to later operations. The guarantee is for every such sequence, including one whose next operation is chosen after observing earlier answers or execution costs. Lookup may modify the internal representation, but must preserve the represented partial function.

The program has a fixed finite instruction list for the chosen \(c\), independent of \(N\), the keys, values and operation sequence. Registers and addressed memory cells contain unsigned \(w\)-bit words. Addresses must fit in one word. Unit-cost operations are reading, writing and copying words, comparisons, branches, addition, subtraction and multiplication modulo \(2^w\), unsigned integer quotient and remainder with nonzero divisor, bitwise Boolean operations and logical shifts. Shifting by at least \(w\) positions yields zero. Computation involving multiple words costs the corresponding instructions. No random instruction, random seed, nonuniform advice, input-dependent oracle or uncharged table is available.

Only the current operation and its constant number of words are newly supplied. The program cannot reread a history of earlier operations from external storage; any retained information must be in its counted memory. Initialization begins with zero memory and the supplied parameters. Constructing constants that depend on \(w\), choosing hash functions, preparing lookup tables, copying records, rebuilding representations, managing memory, and writing answers all count toward the instruction cost. Fixed constants in the finite program are allowed, but a different table or program for each word size is not.

Space includes every live register, retained input word, auxiliary table and temporary workspace, including both old and new structures during rebuilding. It is measured by the number of simultaneously used words. The \(C_cN\) bound applies during initialization and all operations, not just between operations. Memory outside the retained state conveys no information from earlier operations. In particular, a table indexed by every possible key counts in full if retained or used as allocated storage.

The initialization bound, individual lookup bound, space bound and total prefix bound must all hold with constants depending only on \(c\). The aggregate prefix bound is the precise amortized convention in this card: costly individual updates are allowed, but cannot violate the bound on any prefix. No average over sequences or inputs is taken. No constant worst-case bound is required for a single insertion or deletion. Space is linear in the fixed capacity \(N\), rather than in the possibly smaller current number of keys.''',
 answer_criterion=r'''Supply a complete Lean-checked proof of the displayed statement or its logical negation.

A positive answer must provide, for each fixed \(c\ge2\), a uniform program satisfying the exact interface, every individual lookup bound, every aggregate prefix bound and the simultaneous space bound. A family whose constants depend on \(c\) is allowed; size-dependent programs or free precomputation are not.

A negative answer must establish that for at least one fixed \(c\ge2\), no admissible uniform deterministic program and constant \(C_c\) satisfy all of the guarantees for all capacities and valid sequences. It need not prove a superconstant bound for every operation or every value of \(c\). A lower bound restricted to one hashing scheme or a comparison-only machine is insufficient, as is a conditional impossibility result under an unproved conjecture.

A static dictionary, a randomized expected-time implementation, or an algorithm with constant amortized lookup cost but occasional slow queries does not alone settle the target.''',
 source_formulation=dict(text='The research statement asks whether deterministic dictionaries must take more than constant time and describes this as a possible fundamental advantage of randomization. The card keeps its approved concrete version: logarithmic words, linear capacity space, constant worst-case lookup and constant amortized updates.',caption='Paraphrase of Pătrașcu, Research Statement (2007), dictionary discussion pp. 9–10; the exact machine and amortization conventions are the retained editorial specialization.',citation='primary',format='editorial_paraphrase'),
 references=[
 ref('primary','Research Statement','Mihai Pătrașcu',2007,'https://people.csail.mit.edu/mip/docs/job-application07/statements.pdf','Research statement within the combined job-application PDF; dictionary discussion printed/PDF pp. 9–10, especially the first two paragraphs of p. 10'),
 ref('randomized','Dynamic Perfect Hashing: Upper and Lower Bounds','Martin Dietzfelbinger; Anna Karlin; Kurt Mehlhorn; Friedhelm Meyer auf der Heide; Hans Rohnert; Robert E. Tarjan',1994,'https://www.cs.princeton.edu/research/techreps/15','Primary abstract of Princeton TR-310-91 and journal metadata: SIAM Journal on Computing 23(4), 1994, pp. 738–761; restricted deterministic lower-bound class'),
 ref('uniform','Uniform deterministic dictionaries','Milan Ružić',2008,'https://pure.itu.dk/en/publications/uniform-deterministic-dictionaries/','Primary institutional abstract; ACM Transactions on Algorithms 4(1), DOI 10.1145/1328911.1328912; uniform deterministic lookup/update tradeoff'),
 ref('static2025','Optimal Static Dictionary with Worst-Case Constant Query Time','Yang Hu; Jingxun Liang; Huacheng Yu; Junkai Zhang; Renfei Zhou',2025,'https://arxiv.org/abs/2412.10655v2','26 March 2025 revision, STOC 2025; primary abstract, static succinct dictionary and random hash bits'),
 ref('fid2026','Compressing Dynamic Fully Indexable Dictionaries in Word-RAM','Gabriel Marques Domingues',2026,'https://arxiv.org/abs/2603.23119v1','24 March 2026, listed for STOC 2026; primary abstract, rank/select interface and log_w n time term; proof not independently audited'),
 ],
 why='A fully deterministic dictionary with these guarantees would match the basic operation bounds of randomized dynamic hashing in linear space. An unconditional obstruction would establish a substantive limitation of determinism for this central data-structure interface.',
 context_blocks=[
 block('Dynamic perfect hashing gives constant worst-case lookup and expected amortized constant updates with randomization. The same paper proves deterministic lower bounds for a restricted class of hashing schemes, so those lower bounds cannot be applied to every word-RAM program.','randomized'),
 block('The source singles out a superconstant deterministic dictionary lower bound as an open problem. The target here keeps its concrete capacity, word-size and amortization conventions.'),
 block('Uniform deterministic dictionaries are known with query/update tradeoffs. The cited construction avoids free word-size-dependent constants, but its stated tradeoff does not provide constant bounds for both operations.','uniform'),
 block('The STOC 2025 succinct dictionary result concerns static sets and includes random hash bits. Its worst-case constant lookup guarantee does not supply fully deterministic dynamic maintenance.','static2025'),
 block(r'The 2026 fully indexable dictionary supports rank and select as well as updates. Its stated time includes \(\log_w n\), where \(n\) is the current number of stored keys, and therefore does not give constant update time throughout the logarithmic-word capacity regime.','fid2026'),
 ],
 progress=[progress('1994','Dynamic perfect hashing provides the randomized benchmark; deterministic lower bounds are proved for restricted hashing schemes.','randomized'),progress('2007','The research statement highlights the unresolved deterministic constant-time regime.'),progress('2008','Uniform deterministic dictionaries provide explicit query/update tradeoffs.','uniform'),progress('2025-03-26','The revised static succinct dictionary result provides worst-case constant lookup.','static2025'),progress('2026-03-24','A deterministic dynamic fully indexable dictionary improves redundancy while retaining a nonconstant time term in the general logarithmic-word regime.','fid2026')],
),notes,sources,'The bounded primary-source review through 17 September 2026 found no verified deterministic implementation or unconditional impossibility result for the selected fixed-capacity word-RAM target. Restricted hashing lower bounds, static succinct dictionaries and the checked 2026 rank/select result do not resolve it. This is not exhaustive certification of openness or an independent audit of every cited proof.',summary=[
 'A dictionary stores word-sized keys and values while keys are repeatedly inserted and deleted.',
 'Every lookup must return its answer in constant worst-case time, and updates share a constant amortized budget.',
 'The question asks whether a uniform deterministic program can achieve these bounds using space linear in a fixed capacity.',
 'Randomized hashing gives the basic benchmark, while restricted deterministic lower bounds do not cover every permitted program.',
 'A solution must give a complete Lean-checked construction or impossibility proof with the specified machine and online guarantees.',
],expected_sha256=claim['input_sha256'],claim_token=claim['token'])
