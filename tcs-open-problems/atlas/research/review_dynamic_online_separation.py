import sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from authoring import finish, step, paragraph
from locality_separation_common import LCL,DYNAMIC,ONLINE,UNIFORM,sources,simulation_context

finish('promise-free-dynamic-online-linear-constant-separation-resolved',
 id='TCS-0520',title='Linear dynamic versus constant online locality for a promise-free LCL',
 area='Distributed and local algorithms',criterion='models',question_type='yes_no',
 formal='Does there exist one promise-free LCL on bounded-degree graphs with deterministic online-LOCAL complexity O(1), but deterministic incremental dynamic-LOCAL complexity Ω(n)? Under the models below, the answer is no: constant online locality implies deterministic O(√n·polylog n) LOCAL complexity and hence a sublinear dynamic repair radius.',
 definitions=LCL+ONLINE+DYNAMIC+UNIFORM,
 answer_criterion='A positive answer requires one finite total LCL specification, a constant-locality online algorithm, and a linear dynamic-radius lower bound for all deterministic maintenance algorithms. A negative answer excludes every such witness. The cited simulations imply the negative answer; the conclusion is an editorial composition of the results, with its reasoning given below.',
 context=[
  paragraph('Online lookaround reveals nearby parts of the eventual graph before a vertex commits to its output. Incremental dynamic computation instead sees the graph as it is built and repairs earlier outputs. The question asks whether even constant lookaround can prevent changes that would otherwise have to spread linearly far.'),
  paragraph('These are spatial resource bounds. A dynamic algorithm may examine the whole current graph and perform very expensive computation, yet its output changes must remain close to the update. An online algorithm may use all previously revealed information but cannot revise a requested vertex. Neither definition bounds ordinary centralized running time.', 'models'),
  *simulation_context(),
  paragraph('A deterministic T(n)-round LOCAL algorithm also supplies a dynamic algorithm with repair radius at most T(n)+O(1). Recompute its prescribed outputs after each insertion. Farther vertices have unchanged input neighborhoods and therefore unchanged outputs. For growing graphs, use the fixed size bound N and pad unseen vertices as isolated vertices with fixed dummy inputs; the problem is total and its legality is independent of N, so outputs on the real components remain valid.', 'models'),
  paragraph('The complete implication is online O(1) → component-wise online O(1) → deterministic LOCAL O(√n·polylog n) → dynamic O(√n·polylog n). This excludes the requested linear dynamic lower bound. It does not prove that online and dynamic locality always agree, nor give a constant-radius dynamic simulation.')],
 why='This asks whether a small view into the eventual graph can eliminate a global repair cost. Its negative resolution is a useful constraint on future separation constructions: a promise-free LCL with constant online locality must already permit sublinear dynamic repair.',
 importance=dict(score=79,method='editorial',assessed_on='2026-09-10',reason='A structural comparison of online lookaround and dynamic repair, now bounded by a general sublinear simulation. Preserved as a resolved historical question, distinct from the separate LOCAL-versus-dynamic comparison.'),
 progress=[
  step('2023','Akbari and coauthors formalize online lookaround and incremental dynamic locality and establish LOCAL → dynamic-LOCAL → online-LOCAL simulations.','models'),
  step('2026-02','The primary problem list records the promise-free linear-versus-constant separation target. Lemma 7.5 of the corrected comparison paper turns constant online locality into constant component-wise online locality on all bounded-degree graphs.','component'),
  step('By 2026-08','The general-graph clustering simulation yields a sublinear deterministic LOCAL algorithm from a constant-locality component-wise online algorithm. The revised paper explains the online extension in Section 1.6 and Appendix A.','sublinear'),
  step('2026-09 review: negative corollary','Combine that sublinear LOCAL algorithm with local recomputation after updates. The resulting O(√n·polylog n) repair radius contradicts any linear dynamic lower bound, so the saved separation target has a negative answer.','sublinear')],
 references=sources(),status='resolved',status_note='Resolved negatively in the specified promise-free deterministic models by composition of the cited simulations. The derivation is made explicit rather than attributed to an exact theorem statement about this catalogue ID. The conclusion concerns linear-versus-constant separation, not equivalence of the two models.',formulation_reviewed_on='2026-09-10')
