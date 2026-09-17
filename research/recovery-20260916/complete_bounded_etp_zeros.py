"""Review bounded continuous zero testing with exact effective-field input."""
import sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT/'research/card-completion-20260913'))
from complete_review import complete,ref,block,progress
from review_queue import read_claims
identifier='TCS-1151';claim=read_claims(ROOT)[identifier]
complete(identifier,dict(
 status='source_open',criterion='decision',question_type='yes_no',
 formal=r'''Is the following proposition true? For every computable discrete subfield \(K\subseteq\mathbb R\) with a fixed effective presentation, there exists an algorithm which, given a constant-coefficient homogeneous linear differential equation with coefficients and initial values in \(K\), together with \(T\in\mathbb Q_{\ge0}\), decides whether its unique solution \(f\) satisfies
\[
\exists t\in[0,T]\quad f(t)=0.
\]
The order of the equation is part of the input and has no fixed upper bound. The algorithm may depend on the presented field, but must halt correctly on every valid equation and endpoint over that field. No unproved number-theoretic hypothesis is assumed.''',
 definitions=r'''A computable discrete subfield is a countable subfield \(K\subseteq\mathbb R\) equipped with a decidable set of integer codes \(D_K\subseteq\mathbb N\) and a surjective interpretation \(p_K:D_K\to K\). Codes need not be unique. Its presentation supplies computable operations on codes for addition and multiplication, a partial computable inverse defined exactly on codes of nonzero elements, and decidable equality of interpreted elements. Fixed codes for 0 and 1 are available. It also supplies a computable function \(E:D_K\times\mathbb N\to\mathbb Q\) such that
\[
|E(a,r)-p_K(a)|<2^{-r}.
\]
Thus both symbolic equality and arbitrarily accurate rational approximation are available. “Discrete” refers to effective exact equality, not to a discrete topology on \(K\). Negative elements can be found by enumerating codes and testing their sum with the given element for zero.

An instance gives an integer \(m\ge1\), codes for \(c_1,\ldots,c_m\in K\) and \(u_0,\ldots,u_{m-1}\in K\), and a nonnegative rational \(T\). These specify
\[
f^{(m)}(t)+c_1 f^{(m-1)}(t)+\cdots+c_m f(t)=0,
\qquad f^{(j)}(0)=u_j\quad(0\le j<m).
\]
The unique real solution is analytic on all of \(\mathbb R\). This differential-equation representation defines an exponential-trigonometric polynomial over \(K\) for this card; characteristic roots are not required to belong to \(K\), and no separate input representation of those complex roots is needed. The supplied order need not be minimal.

All codes, list lengths and rational numerator/positive-denominator pairs are finite binary strings in a fixed length-delimited encoding. A decider is an ordinary deterministic Turing machine using the computable procedures of this fixed field presentation; there are no noncomputable oracles. It outputs 1 exactly when a real zero exists in the closed interval and outputs 0 otherwise. It must handle zeros at either endpoint, zeros without a sign change, identically zero solutions and \(T=0\). No quantitative running-time bound is requested.

The quantifiers are \(\forall\) fixed presented fields \(K\), \(\exists\) a decider \(A_K\), \(\forall\) valid finite instances over \(K\). A single algorithm taking arbitrary field presentations as additional input is not required. Conversely, choosing a new machine separately for each equation or each order is insufficient. The coefficient field need not contain \(\pi\).''',
 answer_criterion='Give a complete mathematically correct Lean-checked proof of the proposition or its logical negation. A positive answer must establish termination and exact correctness for every valid input over every fixed presented field. A negative answer must exhibit a computable discrete subfield with a specified effective presentation for which the bounded zero problem is undecidable. Numerical approximations, a procedure that halts only on one answer, conditional decidability, or undecidability solely on an unbounded interval does not settle this question.',
 why='Exact zero detection is a basic reachability question for linear continuous dynamics. A bounded interval removes long-term behavior but still requires deciding tangential contact with zero, which numerical approximation alone need not certify.',
 importance=dict(score=80,method='editorial',reason='A precise computability boundary for linear differential systems, linking effective algebra and exact analytic reachability; the broader coefficient-field scope distinguishes it from algebraic-coefficient results.'),
 source_formulation=dict(text='The source asks whether bounded zero existence is decidable over an arbitrary computable discrete real subfield. Its input functions are specified by linear differential equations and initial values.',caption='MFCS 2026, Open Problem 1, printed p.65:16; Definition 4 and equation (2) supply the model.',citation='primary',format='editorial_paraphrase'),
 references=[
 ref('primary','On Positivity of Exponential-Trigonometric Polynomials and Irrationality Exponents','Pieter Collins; Bernard Hanzon; Eike Neumann',2026,'https://doi.org/10.4230/LIPIcs.MFCS.2026.65','Equation (2), p.65:1; Definition 4, pp.65:5–6; Open Problem 1, p.65:16'),
 ref('conditional','On the Zeros of Exponential Polynomials','Ventsislav Chonev; Joël Ouaknine; James Worrell',2023,'https://doi.org/10.1145/3603543','JACM 70(4), article 26; §3 and Theorem 3.5, printed p.26:10; author PDF https://people.mpi-sws.org/~joel/publications/zeros-exp-polys23.pdf'),
 ],
 context_blocks=[
 block('The source’s field model supplies exact arithmetic, equality testing and a computable real embedding. Arbitrary computable real numbers without decidable equality would be a different input model.'),
 block('The differential equation keeps all input data in the given field while allowing its solution to involve complex characteristic roots. The exact root expression is not additional advice.'),
 block('For real algebraic coefficients and initial values, bounded zero existence is decidable assuming Schanuel’s conjecture. Theorem 3.5 uses factorization and control of repeated zeros. Its hypothesis remains essential to the stated result.','conditional'),
 block('An even-multiplicity zero can occur without a sign change. This explains why testing finitely many sample signs alone does not prove exact correctness.','conditional'),
 block('The 2026 article separates its unbounded-interval hardness results from this bounded-interval question, which it explicitly leaves open.'),
 ],
 progress=[progress('2023','Conditional bounded zero decidability is established for algebraic data in Theorem 3.5.','conditional'),progress('2026-08-21','MFCS 2026 states the arbitrary computable discrete field version as Open Problem 1.')],
),[
 'Read the source field definition and used the ODE presentation, retaining all orders and arbitrary fixed computable discrete real subfields.',
 'Made per-field quantification, exact equality, endpoints, tangential zeros and the absence of a time bound explicit.',
 'Distinguished conditional algebraic-coefficient decidability and unbounded-interval hardness from this target.',
 'Individually assessed importance and required a complete Lean-checked decidability or undecidability proof.',
],[
 'Read MFCS 2026 equation (2), Definition 4, and Open Problem 1 at the cited locators. The per-field decider convention explicates its “Let K” formulation.',
 'Read Chonev–Ouaknine–Worrell 2023, §3 and Theorem 3.5, including the algebraic-data and Schanuel assumptions. The theorem addresses bounded intervals.',
 'Bounded primary-source status review through 17 September 2026 found no unconditional resolution of the selected full-field statement.',
], 'Source-open as explicitly stated in MFCS 2026, Open Problem 1. The question retains every fixed computable discrete real coefficient field and arbitrary equation order. The algebraic-coefficient theorem depends on Schanuel’s conjecture, while the source’s unbounded-interval hardness is a separate result. Bounded review through 17 September 2026.',summary=[
 'The input specifies a linear differential equation with constant coefficients, initial values and a nonnegative rational endpoint.',
 'The task is to decide exactly whether its real solution has any zero in the closed bounded interval.',
 'The question ranges over every fixed computable real subfield with effective arithmetic, equality and rational approximation.',
 'A decider may depend on the field but must handle every equation order, including endpoint zeros and zeros without sign changes.',
 'A complete Lean-checked unconditional decidability proof or a field-specific undecidability counterexample is required.',
],expected_sha256=claim['input_sha256'],claim_token=claim['token'])
