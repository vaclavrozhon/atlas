import sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from authoring import finish, step, paragraph
from locality_separation_common import LCL,DYNAMIC,LOCAL,UNIFORM,sources,simulation_context

finish('promise-free-local-dynamic-linear-constant-separation-resolved',
 id='TCS-0521',title='Linear LOCAL versus constant dynamic locality for a promise-free LCL',
 area='Distributed and local algorithms',criterion='models',question_type='yes_no',
 formal='Does there exist one promise-free LCL on bounded-degree graphs that has a deterministic incremental dynamic-LOCAL algorithm with O(1) repair radius, but requires Ω(n) rounds in deterministic LOCAL? Under the models below, the answer is no: combining the cited simulations gives a deterministic O(√n·polylog n)-round LOCAL algorithm whenever constant dynamic locality is possible.',
 definitions=LCL+LOCAL+DYNAMIC+UNIFORM,
 answer_criterion='A positive answer would require one finite total LCL specification, a constant-radius dynamic algorithm, and a linear deterministic LOCAL lower bound. A negative answer rules out this combination for every such LCL. The latter follows from the sublinear simulation described below; this is a derived corollary, not a claim that either cited paper states this exact saved question verbatim.',
 context=[
  paragraph('Dynamic computation retains the history of how a graph was built. This history can provide choices that a fresh synchronous computation has to establish through communication. The saved question asks whether local repairs could exploit that advantage so strongly that a constant repair radius replaces a linear number of communication rounds.'),
  paragraph('The requirement to work on every bounded-degree graph and every input matters. Special graph families may have global promises that affect what an algorithm can infer from a partial view. Here all intermediate graphs are valid inputs to the same total problem, so the simulations can build disjoint copies, delete edges, and introduce isolated vertices without leaving the problem’s domain.'),
  paragraph('A constant-radius dynamic algorithm yields a constant-locality online algorithm. On each online request, reveal a slightly larger constant-radius neighborhood and simulate its vertex and edge insertions. Once a requested vertex is labeled, later revelations are too far away to change it. This uses the incremental model beginning with an empty graph; unseen input labels are not supplied in advance.', 'models'),
  *simulation_context(),
  paragraph('Combining these steps gives dynamic O(1) → online O(1) → deterministic LOCAL O(√n·polylog n). Since √n times any fixed polylogarithm is o(n), a linear LOCAL lower bound is impossible. Smaller separations can still exist; the result only rules out the specified linear-versus-constant target.')],
 why='The question probes the limits of using construction history to replace communication for locally verifiable tasks. Its negative resolution places a general upper bound on that advantage and demonstrates why exact size regimes and the absence of promises matter when comparing locality models.',
 importance=dict(score=80,method='editorial',assessed_on='2026-09-10',reason='A broad model-separation benchmark resolved through general simulation machinery. Retained for its structural meaning and traceability, with resolved status rather than counted as a remaining open problem.'),
 progress=[
  step('2023','The locality framework establishes the simulations from LOCAL to incremental dynamic-LOCAL to online-LOCAL, and studies their differences for locally checkable tasks.','models'),
  step('2026-02','The updated problem list asks for a promise-free linear LOCAL versus constant dynamic separation. The corrected comparison paper provides the component-wise conversion needed for the later implication.','component'),
  step('By 2026-08','The revised quantum-advantage paper extends the clustering simulation to component-wise online locality on general graphs. Its deterministic constant-locality specialization has O(√n·polylog n) LOCAL complexity.','sublinear'),
  step('2026-09 review: negative corollary','Composing dynamic-to-online simulation, the constant-locality component-wise conversion, and the sublinear LOCAL simulation rules out the requested witness. The card records the derivation explicitly; no withdrawn dynamic derandomization theorem is invoked.','sublinear')],
 references=sources(),status='resolved',status_note='Resolved negatively in the fixed standard deterministic incremental model as a corollary of the cited model simulations and the August 2026 component-wise simulation. The chain of implications is spelled out in context. The original open statement is retained for history; the result does not classify all smaller dynamic/LOCAL separations.',formulation_reviewed_on='2026-09-10')
