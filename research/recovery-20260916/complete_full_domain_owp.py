"""Complete the full-Boolean-domain keyed OWP existence implication."""
import sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];sys.path.insert(0,str(ROOT/'research/card-completion-20260913'))
from complete_review import complete,ref,block,progress,DATE
from review_queue import read_claims
identifier='TCS-6546';claim=read_claims(ROOT)[identifier]
notes=[
 'Retained the already specified public-key family of permutations of the full Boolean cube, not a silently stronger unkeyed target or a weaker key-dependent sparse domain.',
 'Specified uniform generation/evaluation, every-key bijectivity, polynomially computable domain length, independent sampling and average-over-keys nonuniform classical inversion security.',
 'Distinguished the public key from the private generator coins and required no inversion trapdoor, efficient key-membership test or bijection on malformed keys.',
 'Separated the OWF-only black-box barrier from the domain-invariant obfuscation barrier and from the unrestricted existence implication.',
 'Checked the 2025 full-domain trapdoor theorem and its explicit subexponential OWF/iO assumptions; bounded 2026 checks found no verified bare-OWF resolution.',
 'Preserved importance score 95 and required a complete Lean-checked proof with no additional hardness premise.',
]
sources=[
 'Read Asharov–Segev, ePrint 2015/752 primary abstract and revision history, revised 11 October 2015, TCC 2016 and Journal of Cryptology 31(3) 698–736 (2018), latter publication corroborated on author homepage. The abstract distinguishes OWF-only black-box impossibility without domain invariance from a separate domain-invariant barrier with oracle-aided iO. Direct ePrint/archive full PDFs did not open in this check, so their full proofs were not reread.',
 'Read Rudich thesis primary Berkeley abstract and metadata, UCB/CSD-88-468, December 1988. The original abstract qualifies its OWF-to-OWP barrier with a combinatorial conjecture; this is a statement about the historical thesis rather than a claim the conjecture remains open.',
 'Read Matsuda–Matsuura, TCC 2011, publisher abstract: the fully black-box separation allows an injective starting OWF with only one bit of expansion and adaptive one-wayness. The restriction is on constructions, not the truth of the unrestricted ordinary-model implication.',
 'Read Shmueli–Zhandry, arXiv:2507.12456v1 of 16 July 2025: Theorem 6 printed p. 6 requires subexponentially secure iO and OWFs; §1.4 printed p. 10 distinguishes key-domain from input-domain invariance. Read their full-domain and sparse-domain discussion pp. 4–5 and 9; no full cryptographic proof audit.',
 'Checked June 2026 ECCC26/091 primary abstract and indexed Lemma 16 on p. 18: its use of full-domain trapdoor permutations still assumes subexponential OWF and iO. It is not a construction from the ordinary OWF premise alone.',
 f'Bounded primary-source checks through {DATE} found no verified resolution of the retained keyed full-domain existence implication. Oracle and black-box barriers are not treated as ordinary-model nonexistence proofs.',
]
complete(identifier,dict(
 title='One-way permutations from one-way functions',criterion='assumptions',question_type='yes_no',
 formal=r'''Does the existence of a classical one-way function secure against every nonuniform polynomial-size classical adversary imply the existence of an efficiently generated public-key family of one-way permutations on full Boolean cubes, with the same adversary convention? Require a bijection on the entire cube for every key the generator can output, and negligible inversion probability averaged over an honestly generated public key and a uniform input. No trapdoor is required.''',
 definitions=r'''All inputs and outputs are finite binary strings. Uniform polynomial time means one finite classical Turing program with a polynomial worst-case bit-operation bound in its input length. Randomized programs use independent fair random bits within that bound. A nonuniform polynomial-size adversary is a family of polynomial-size Boolean circuits, with polynomially many random input bits allowed. Its description and any auxiliary advice have polynomial length in the security parameter and may depend on that parameter, but not on independently sampled secret experiment coins.

A function \(\mu:\mathbb N\to[0,1]\) is negligible if, for every integer \(a\ge1\), there exists \(N_a\) such that \(\mu(n)\le n^{-a}\) for all \(n\ge N_a\).

The premise is that a single deterministic polynomial-time program computes a family
\[
 f_n:\{0,1\}^n\longrightarrow\{0,1\}^{\ell(n)},
\]
where \(\ell(n)\) is a nonnegative integer, polynomially bounded and computable in polynomial time from \(1^n\), such that every nonuniform polynomial-size randomized family \(I_n\) has negligible success probability in the following experiment. Sample \(X\) uniformly from \(\{0,1\}^n\), give \((1^n,f_n(X))\) to \(I_n\), and declare its output \(Z\) successful exactly when \(Z\in\{0,1\}^n\) and \(f_n(Z)=f_n(X)\). Any preimage counts. The function's description is public, and no injectivity or subexponential hardness is assumed.

The desired permutation family consists of a fixed polynomially bounded integer function \(m(n)\ge n\), computable in polynomial time from \(1^n\), a uniform probabilistic polynomial-time algorithm \(\operatorname{Gen}(1^n)\to pk\), and a uniform deterministic polynomial-time evaluation algorithm \(\operatorname{Eval}(1^n,pk,x)\). Let \(K_n\) be the support of Gen: the finite set of keys that occur with positive probability. For every \(n\ge1\) and every \(pk\in K_n\), evaluation on the whole input cube defines a map
\[
 \pi_{n,pk}:\{0,1\}^{m(n)}\longrightarrow\{0,1\}^{m(n)},
 \qquad \pi_{n,pk}(x)=\operatorname{Eval}(1^n,pk,x),
\]
and this map must be a bijection. Equivalently, for each output in that cube there is exactly one input in the cube with that output. This is an exact structural property for every generated key, not a property permitted to fail on a negligible fraction of keys or inputs.

One-wayness requires that, for every nonuniform polynomial-size randomized adversary \(A_n\), the probability of the event
\[
 Z=A_n(1^n,pk,\pi_{n,pk}(X))\in\{0,1\}^{m(n)}
 \quad\text{and}\quad
 \pi_{n,pk}(Z)=\pi_{n,pk}(X)
\]
is negligible in \(n\), where \(pk\leftarrow\operatorname{Gen}(1^n)\), \(X\) is independently uniform on \(\{0,1\}^{m(n)}\), and adversary coins are independent. An incorrectly sized or malformed output fails. Each adversary may have its own polynomial resource bound and negligible success bound. The public key and all algorithm descriptions are available to the adversary; the generator's private coins are not supplied.

Full domain refers to each permutation's input and output sets, both the complete Boolean cube. It does not require \(K_n\) to contain all strings of some length, to have efficiently recognizable membership, or to be independent of the construction's building blocks. No requirement is imposed on bijectivity for keys outside \(K_n\), although the evaluation program must still terminate within its polynomial bound on all inputs. No inverse algorithm, secret trapdoor, key recovery or hardness for every individual key is demanded. A trapdoor construction would qualify if its public family has the required properties and satisfies the stated security.

All algorithms and security guarantees are classical. The implication is about existence in the ordinary model with no ideal oracles. It may use the full description of an underlying one-way function, and its polynomial bounds may depend on that function. It is not restricted to a black-box compiler or reduction and assumes no obfuscator, additional cryptographic primitive or stronger security level.''',
 answer_criterion=r'''Give a complete Lean-checked proof of the stated existence implication, supplying uniform generation and evaluation, the length function, every-key bijectivity and the negligible inversion bound against all stated adversaries; or give a complete Lean-checked proof of its negation in the ordinary computational model.

A restricted-domain permutation or merely injective length-expanding function does not satisfy the target. Additional assumptions must themselves be derived from ordinary one-way functions. An oracle separation or exclusion of a class of black-box constructions is a barrier, not a refutation of this unrestricted implication. Proving that ordinary one-way functions do not exist would establish the implication vacuously, not refute it. No numerical approximation tolerance applies.''',
 source_formulation=dict(text='Asharov and Segev revisit the longstanding task of obtaining one-way permutation families from one-way functions and establish barriers for specified construction models. The card retains its existing explicit convention of efficiently generated public keys and permutations on a full Boolean cube, and asks the unrestricted existence implication beyond those construction restrictions.',caption='Paraphrase of the inherited ePrint 2015/752 abstract and its OWF-only barrier discussion; the full-domain keyed convention is explicit in this card and distinguished in Shmueli–Zhandry §1.4.',citation='primary',format='editorial_paraphrase'),
 references=[
 ref('primary','On Constructing One-Way Permutations from Indistinguishability Obfuscation','Gilad Asharov; Gil Segev',2015,'https://eprint.iacr.org/2015/752','Revision 11 October 2015; primary abstract, two distinct barrier statements; TCC 2016 and Journal of Cryptology 31(3), 698–736 (2018)'),
 ref('rudich','Limits on the Provable Consequences of One-way Functions','Steven Rudich',1988,'https://www2.eecs.berkeley.edu/Pubs/TechRpts/1988/6060.html','Berkeley dissertation UCB/CSD-88-468, December 1988; primary abstract explicitly qualifies the historical permutation barrier'),
 ref('injective','On Black-Box Separations among Injective One-Way Functions','Takahiro Matsuda; Kanta Matsuura',2011,'https://doi.org/10.1007/978-3-642-19571-6_36','TCC 2011 pp. 597–614; publisher abstract, fully black-box one-bit-expanding injective/adaptive separation'),
 ref('permutable','On One-Shot Signatures, Quantum vs Classical Binding, and Obfuscating Permutations','Omri Shmueli; Mark Zhandry',2025,'https://arxiv.org/abs/2507.12456v1','Version 1, 16 July 2025; Theorem 6 printed p. 6, full-domain permutations under subexponential iO and OWF; §1.4 p. 10, input versus key domains'),
 ],
 context_blocks=[
 block('A general one-way function can merge distinct inputs and miss possible outputs. A permutation is exactly bijective; its average-case inversion hardness must coexist with a unique preimage for every output.'),
 block('This target retains a publicly indexed family of permutations of complete Boolean cubes. Sparse input domains, an unkeyed single permutation family, and the distribution or recognition of valid keys are distinct conventions and must be identified when comparing results.'),
 block('The historical thesis describes its original permutation barrier conditionally on a combinatorial conjecture. Its oracle method studies limits of techniques rather than the unrestricted ordinary-model implication.','rudich'),
 block('Even injective one-way functions expanding their input by only one bit face a fully black-box barrier under the 2011 theorem. The result does not rule out every method that can inspect the underlying code.','injective'),
 block('The inherited paper has two separate conclusions: an OWF-only black-box barrier that permits domains to depend on the building blocks, and a barrier with oracle-aided obfuscation under a domain-invariance requirement. Combining them into an unrestricted nonexistence theorem would lose essential hypotheses.'),
 block('The July 2025 theorem gives full-domain trapdoor permutations from subexponentially secure obfuscation and one-way functions. Its stronger output property does not remove either additional premise.','permutable'),
 block('The 2025 paper explains compatibility with the older obfuscation barrier: full input domains do not imply that the valid-key domain is independent of the building blocks. This card places no such invariance condition on valid public keys.','permutable'),
 ],
 progress=[progress('1988','The thesis develops the historical conditional oracle barrier.','rudich'),progress('2011','The fully black-box barrier is strengthened to one-bit-expanding injective functions with adaptive security.','injective'),progress('2015-10-11','The revised inherited paper separates the OWF-only and domain-invariant obfuscation barriers.'),progress('2018','The inherited work appears in Journal of Cryptology 31(3).'),progress('2025-07-16','The full-domain trapdoor construction is posted under subexponential obfuscation and OWF assumptions.','permutable')],
),notes,sources,'The inherited source treats the OWF-to-permutation task as a fundamental construction question and proves restricted barriers. The inspected 2025 full-domain positive theorem needs subexponential iO and OWFs, still retained in its 2026 uses. Bounded primary-source checks through 17 September 2026 found no verified resolution from ordinary OWFs alone under the keyed full-domain convention fixed here. The cited cryptographic proofs were not independently certified.',summary=[
 'A one-way permutation is an efficiently computable bijection whose inverse is hard to compute on a random input.',
 'This card asks whether ordinary one-way functions imply an efficiently generated public-key family of such permutations.',
 'Every generated key must define a permutation of the whole Boolean cube, while inversion hardness is averaged over honest keys and uniform inputs.',
 'Known black-box barriers do not settle this unrestricted implication, and the recent full-domain construction uses stronger assumptions.',
 'A complete Lean-checked answer must prove this exact existence implication or its ordinary-model negation.',
],expected_sha256=claim['input_sha256'],claim_token=claim['token'])
