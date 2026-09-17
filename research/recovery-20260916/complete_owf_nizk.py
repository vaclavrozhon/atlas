"""Complete the ordinary-OWF foundation question for reusable adaptive NIZK."""
import sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];sys.path.insert(0,str(ROOT/'research/card-completion-20260913'))
from complete_review import complete,ref,block,progress,DATE
from review_queue import read_claims
identifier='TCS-6552';claim=read_claims(ROOT)[identifier]
notes=[
 'Retained the existing reusable adaptive computational-argument target in an honestly generated common reference string; distinguished it from the stronger proof-system and common-random-string formulation in the inherited survey.',
 'Made the OWF premise, nonuniform classical adversaries, unary length bound, proof-length bound, uniform algorithms and negligible-error quantifiers explicit.',
 'Specified the real and simulated adaptive multi-query experiments, including valid-witness checking outside the simulator, auxiliary information, and simulation state.',
 'Separated unrestricted existence from black-box construction, interactive protocols, additional cryptographic assumptions and reverse-direction necessity theorems.',
 'Rechecked the source question and recent primary results through 17 September 2026, including the August ITC reverse implication and June oracle-proof transformation.',
 'Preserved importance score 95 and required a complete Lean-checked proof of the precise implication or its negation.',
]
sources=[
 'Read Damgård–Nielsen, Commitment Schemes and Zero-Knowledge Protocols, title page dated 2011 despite ComZK08 filename; §3.5.2 pp. 27–29, Theorems 3.4–3.5 and the open question following 3.5. Its definition has an unbounded cheating prover and a uniform random setup string. The card explicitly retains its already selected computational-argument/common-reference-string variant rather than presenting it as a verbatim equivalent.',
 'Checked Peikert–Shiehian, June 5 2019 manuscript, primary indexed abstract at ePrint 2019/158 and CRYPTO 2019 publisher metadata: plain LWE suffices. The author-hosted PDF failed to fetch in this check; its full proof was not reread.',
 'Read primary abstract and revision metadata of Bradley–Waters–Wu, ePrint 2023/1938, revised 20 September 2024, TCC 2024. The positive OWF implication additionally assumes an adaptively sound BARG; the weaker somewhere-sound variant retains its stated security assumption.',
 'Read primary abstract and history of Branco et al., ePrint 2024/1514, EUROCRYPT 2025, revised 30 March 2026: LWE or DDH plus LPN; the initial black-box constructions are single-theorem and a non-black-box multi-theorem upgrade retains these assumptions.',
 'Read Chen–Rothblum–Tell, ECCC24/116 revision of 3 April 2025, Corollary 1.11 on printed p. 8 and surrounding discussion: subexponential OWF plus a strong complexity assumption; the paper explicitly calls the minicrypt foundation a major open question and works with uniform soundness.',
 'Read Chakraborty–Hulett–Khurana–Tomer, arXiv:2602.17651v1 of 19 February 2026, abstract; its nontrivial-NIZK-to-OWF implication assumes NP not contained in ioP/poly. This is the reverse direction.',
 'Read Chatterjee–Li–Vasudevan, ITC 2026 Article 5, publisher abstract and metadata, published 12 August 2026: weak NIZK implies OWF under worst-case NP hardness, again a necessity/amplification result rather than the requested sufficiency.',
 'Read Florentz–Konopnicki–Rothblum, ECCC25/162 revised 21 February 2026, Theorem 1.1 printed p. 4: the OWF-only succinct proof is public-coin and interactive. Confirmed CRYPTO 2026 online publication 11 August 2026.',
 'Read Ganesh–Weiss, ePrint 2026/1167, primary abstract, received 4 June and approved 8 June 2026: the oracle-proof-to-NIZK transformation requires appropriate extractable/equivocal commitments and correlation-intractable hashing; the abstract does not derive them from bare OWFs.',
 f'Bounded primary-source checks through {DATE} found no verified resolution of this exact unrestricted existence implication. The cited construction and security proofs were not independently certified.',
]
complete(identifier,dict(
 title='Noninteractive zero knowledge from one-way functions',criterion='assumptions',question_type='yes_no',
 formal=r'''Does the existence of a classical one-way function imply the existence of a reusable, adaptively secure noninteractive zero-knowledge argument for Boolean circuit satisfiability in the honestly generated common-reference-string model? Require computational soundness and computational zero knowledge against every nonuniform polynomial-size classical adversary, with negligible errors and one public proof message per statement. The implication may use the code of the one-way function and has no black-box restriction.''',
 definitions=r'''All strings are finite binary strings. A uniform probabilistic polynomial-time algorithm is one finite classical Turing program with independent fair random bits and a polynomial worst-case bit-operation bound. A nonuniform polynomial-size adversary is a family of Boolean circuits, possibly with polynomially many independent fair random input bits, whose description, advice, input and output lengths are bounded by a polynomial in the security parameter. Its advice may depend on that parameter, but not on independently sampled secret coins of an experiment. Adaptive algorithms are represented by such polynomially bounded computations with the oracle access specified below. A function \(\mu:\mathbb N\to[0,1]\) is negligible if, for every integer \(a\ge1\), there is \(N_a\) such that \(\mu(\lambda)\le\lambda^{-a}\) for every \(\lambda\ge N_a\).

The premise is that some single deterministic polynomial-time program computes maps \(f_n:\{0,1\}^n\to\{0,1\}^{\ell(n)}\), where \(\ell\) is polynomially bounded, and for every nonuniform polynomial-size randomized circuit family \(I_n\),
\[
 \Pr_{X\leftarrow\{0,1\}^n,I_n}
 [\,Z=I_n(1^n,f_n(X))\in\{0,1\}^n\ \text{and}\ f_n(Z)=f_n(X)\,]
\]
is negligible in \(n\). Any preimage counts as successful inversion; the original sampled preimage need not be recovered. The function's description is public. No injectivity, trapdoor, subexponential hardness or algebraic structure is assumed.

Encode a Boolean circuit by a finite explicit gate list over fan-in-two AND and OR gates and NOT gates, with a specified output and input wires. A statement \(x\) is such an encoding. A witness \(w\) assigns its input wires, and \(R(x,w)=1\) exactly when the encoding and assignment are valid and the circuit evaluates to one. The language \(L\) consists of the statements having such a witness. Malformed circuit encodings are outside \(L\).

The desired argument has uniform polynomial-time algorithms
\[
 \operatorname{Setup}(1^\lambda,1^B)\to\mathsf{crs},\qquad
 \operatorname{Prove}(\mathsf{crs},x,w)\to\pi,\qquad
 \operatorname{Verify}(\mathsf{crs},x,\pi)\to\{0,1\}.
\]
The parameter \(B\ge1\) bounds each statement and witness length separately. Both parameters are included in the public string. Setup and Prove are randomized; Verify is deterministic. There is one fixed polynomial \(P\) bounding their time, the setup length and the proof length by \(P(\lambda+B)\) on inputs within the prescribed bounds. The verifier rejects statements longer than \(B\) and proofs longer than the prescribed bound, and rejects malformed inputs; bounded-prefix scanning suffices for rejecting excessively long inputs. Honest setup depends only on \(\lambda,B\), not on later statements. Its private random coins are not published or given to the adversary. Once the string is generated, proving a statement consists of sending only \(\pi\); verification is public.

The following requirements hold for every integer-valued polynomially bounded choice \(B=B(\lambda)\), using the same algorithms. Completeness means that one negligible function \(\mu_B\) bounds
\[
 \Pr[\operatorname{Verify}(\mathsf{crs},x,
        \operatorname{Prove}(\mathsf{crs},x,w))=0]
 \le\mu_B(\lambda)
\]
uniformly over all \(|x|,|w|\le B\) with \(R(x,w)=1\), where the probability uses independent honest setup and prover coins.

Adaptive computational soundness means that, for every nonuniform polynomial-size adversary given \(1^\lambda,1^B,\mathsf{crs}\), the probability of outputting a pair \((x,\pi)\) with \(|x|\le B\), \(x\notin L\), and \(\operatorname{Verify}(\mathsf{crs},x,\pi)=1\) is negligible. The statement may be selected after seeing the setup string. The negligible bound may depend on the adversary and on \(B\).

Reusable adaptive computational zero knowledge means there are fixed uniform polynomial-time algorithms \(\operatorname{SimSetup}\) and \(\operatorname{SimProve}\) satisfying the following experiments. A nonuniform polynomial-size distinguisher, with arbitrary polynomial-size auxiliary information fixed before setup, receives \(1^\lambda,1^B\) and the experiment's public string. It adaptively makes polynomially many queries \((x,w)\), possibly choosing each after seeing earlier answers, and then outputs a bit. In the real experiment the string is sampled by Setup, and each valid query is answered by a fresh honest Prove execution. In the simulated experiment \(\operatorname{SimSetup}(1^\lambda,1^B)\) produces a public string and private simulation state. A valid query is answered by \(\operatorname{SimProve}\) from the public string, current state and \(x\); the simulator may update its state but is not given \(w\). In both experiments the query-handling wrapper checks \(|x|,|w|\le B\) and \(R(x,w)=1\), returning the same distinguished rejection symbol for invalid queries without invoking the prover or simulator. These checks do not reveal witnesses to the simulator. For every such distinguisher and auxiliary-information family, the absolute difference between its two output-one probabilities is negligible in \(\lambda\). The simulated setup distribution need not equal the honest distribution; indistinguishability of the complete experiments is required. Simulation takes polynomial time in the security parameters and total query length.

There is no bound fixed at setup on the number of future proofs beyond each attacker's polynomial total computation. No random oracle, extra cryptographic assumption, online challenge, extraction requirement or succinctness requirement is supplied. The actual system publishes only its honestly generated string and subsequent proofs; simulation state belongs solely to the security definition.''',
 answer_criterion=r'''Give a complete Lean-checked proof that ordinary one-way functions imply a system satisfying all the definitions above, including uniform algorithms, polynomial bounds, completeness, adaptive computational soundness and reusable adaptive computational zero knowledge; or give a complete Lean-checked proof of the negation of that existence implication in the ordinary computational model.

The construction and reduction may inspect and use the full one-way-function code. An oracle separation, an impossibility result limited to a black-box transformation, or a failure of one proposed construction does not refute this unrestricted implication. An additional assumption must itself be derived from the stated OWF premise. An interactive proof, witness-indistinguishable system, stronger-setup model or single-theorem guarantee without a proved reusable upgrade is insufficient. No numerical approximation tolerance applies.''',
 source_formulation=dict(text='After giving a noninteractive proof-system construction from one-way permutations, Damgård and Nielsen ask whether an arbitrary one-way function suffices. Their discussion uses a common random string and unrestricted cheating provers. This card retains the existing, explicitly specified computational-argument variant with reusable adaptive security and an honestly generated common reference string.',caption='Paraphrase of the 2011 survey, §3.5.2 pp. 28–29, Theorem 3.5 and the following open question; the chosen argument and setup conventions are an explicit editorial specialization.',citation='primary',format='editorial_paraphrase'),
 references=[
 ref('primary','Commitment Schemes and Zero-Knowledge Protocols (2011)','Ivan Damgård; Jesper Buus Nielsen',2011,'https://homepages.cwi.nl/~schaffne/courses/crypto/2014/papers/ComZK08.pdf','Title page dated 2011; §3.5.2 pp. 27–29, Theorems 3.4–3.5 and open question following 3.5'),
 ref('lwe','Noninteractive Zero Knowledge for NP from (Plain) Learning With Errors','Chris Peikert; Sina Shiehian',2019,'https://eprint.iacr.org/2019/158','June 5, 2019 manuscript abstract; CRYPTO 2019 pp. 89–114; plain-LWE sufficient assumption'),
 ref('barg','Batch Arguments to NIZKs from One-Way Functions','Eli Bradley; Brent Waters; David J. Wu',2024,'https://eprint.iacr.org/2023/1938','TCC 2024; revision 20 September 2024, primary abstract: adaptively sound BARG plus OWF'),
 ref('vtdh','Black-Box Non-Interactive Zero Knowledge from Vector Trapdoor Hash','Pedro Branco; Arka Rai Choudhuri; Nico Döttling; Abhishek Jain; Giulio Malavolta; Akshayaram Srinivasan',2025,'https://eprint.iacr.org/2024/1514','EUROCRYPT 2025; revised 30 March 2026, primary abstract: assumptions and single/multi-theorem distinction'),
 ref('derandomization','Fiat-Shamir in the Plain Model from Derandomization','Lijie Chen; Ron D. Rothblum; Roei Tell',2025,'https://eccc.weizmann.ac.il/report/2024/116/','Revision 1, 3 April 2025; Corollary 1.11 and discussion, printed p. 8; uniform security and extra hardness'),
 ref('reverse','Non-Trivial Zero-Knowledge Implies One-Way Functions','Suvradip Chakraborty; James Hulett; Dakshita Khurana; Kabir Tomer',2026,'https://arxiv.org/abs/2602.17651v1','Version 1, 19 February 2026; abstract, conditional reverse implication and amplification'),
 ref('weak','Weak Zero-Knowledge and One-Way Functions','Rohit Chatterjee; Yunqi Li; Prashant Nalini Vasudevan',2026,'https://doi.org/10.4230/LIPIcs.ITC.2026.5','ITC 2026 Article 5, published 12 August 2026; primary abstract, necessity under worst-case NP hardness'),
 ref('interactive','Succinct Zero-Knowledge Proofs from One-Way Functions: The Blackbox Way','Eden Florentz–Konopnicki; Ron D. Rothblum',2026,'https://doi.org/10.1007/978-3-032-35424-2_6','CRYPTO 2026, online 11 August 2026; ECCC25/162 revision 21 February 2026, Theorem 1.1 printed p. 4 explicitly bounds public-coin rounds'),
 ref('oracle','Provably-Secure NIZKs From Multi-Round Oracle Proofs','Chaya Ganesh; Mor Weiss',2026,'https://eprint.iacr.org/2026/1167','Received 4 June, approved 8 June 2026; primary abstract: commitments and correlation-intractable hashing prerequisites'),
 ],
 context_blocks=[
 block('The setup resource and soundness convention matter. The inherited survey asks about proof systems with unrestricted cheating provers and a uniformly random shared string. The present card explicitly retains computational soundness and an honestly generated reference string; its precise target should not be substituted for the survey statement without noting those choices.'),
 block('Ordinary one-way functions suffice for interactive zero knowledge. Removing online interaction while keeping one setup reusable for adaptively chosen statements is the additional demand here.'),
 block('Plain LWE supports noninteractive zero knowledge for NP, but this sufficient structured assumption has not thereby been obtained from every one-way function.','lwe'),
 block('The batch-argument theorem keeps an adaptively sound noninteractive batch argument as an additional resource. Its title does not mean that a bare one-way function has been proved sufficient.','barg'),
 block('The updated vector-trapdoor-hash results retain LWE or DDH and LPN. Their distinction between single-theorem and multi-theorem security is relevant because this card requires reuse.','vtdh'),
 block('The derandomization construction assumes subexponential one-way-function security and a further complexity-theoretic hardness statement. Its uniform-adversary convention also differs from the nonuniform requirement here.','derandomization'),
 block('The 2026 weak-zero-knowledge results establish necessity of one-way functions under worst-case hardness and amplify certain existing systems. They do not construct the requested system from ordinary one-way functions alone.','weak'),
 block('The August 2026 succinct OWF-based proof remains interactive. Succinctness of a protocol and noninteractivity of its commitment component do not imply a noninteractive proof system.','interactive'),
 block('The June 2026 oracle-proof transformation uses additional commitment and hashing guarantees. Its abstract supplies no derivation of those guarantees from the sole premise of this card.','oracle'),
 ],
 progress=[progress('2011','The survey explicitly asks whether arbitrary one-way functions suffice for noninteractive zero knowledge.'),progress('2019','A construction from plain LWE is published.','lwe'),progress('2024-09-20','The revised batch-argument implication retains the BARG resource.','barg'),progress('2025-04-03','The revised derandomization result retains additional hardness and uniform security.','derandomization'),progress('2026-03-30','The updated vector-trapdoor-hash paper retains its stronger assumptions.','vtdh'),progress('2026-06-08','The oracle-proof transformation is posted with additional commitment and hashing requirements.','oracle'),progress('2026-08-11','The OWF-based succinct interactive proof appears online in CRYPTO 2026.','interactive'),progress('2026-08-12','ITC publishes weak-NIZK necessity and amplification results.','weak')],
),notes,sources,'The source asks the OWF foundation question, and the inspected later work does not establish the retained reusable adaptive computational-argument implication. BARG, vector-trapdoor-hash, derandomization and oracle-proof results retain additional resources; the OWF-only succinct protocol is interactive and the 2026 weak-NIZK results run in the reverse direction. Bounded primary-source checks through 17 September 2026 found no verified resolution; cited security proofs were not independently certified.',summary=[
 'A prover should send one publicly verifiable message establishing that a Boolean circuit has a satisfying assignment.',
 'The message must reveal no additional information about the assignment, even across adaptively chosen proofs sharing one setup.',
 'The question asks whether ordinary one-way functions alone imply such a system with security against nonuniform polynomial-size classical adversaries.',
 'Known constructions using stronger assumptions and results for interactive or single-theorem systems do not supply this complete implication.',
 'A complete Lean-checked answer must prove the stated unrestricted existence implication or its negation.',
],expected_sha256=claim['input_sha256'],claim_token=claim['token'])
