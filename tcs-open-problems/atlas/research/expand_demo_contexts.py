"""Editorial context additions to the first demo; no new progress claims."""
import json,sys
from pathlib import Path
BASE=Path(__file__).resolve().parents[1];sys.path.insert(0,str(BASE))
from publish import publish
additions={
'TCS-0506':[
'A sample-complexity characterization should tell us how many labelled examples are necessary from the structure of the hypothesis class, rather than from a particular learning algorithm. Two classes can have the same ordinary capacity measure while differing in how difficult it is to hide the influence of an individual training example.',
'The quantitative issue matters even after learnability is settled. Knowing that some finite sample size works does not distinguish a useful bound from an enormous one. The proposed relation asks whether the extra price of privacy can be controlled by ordinary statistical complexity together with a very slowly growing function of online-learning complexity.'
],
'TCS-6446':[
'Normalization makes the target meaningful. Multiplying a Hamiltonian by a large number could enlarge its energy gap, but would also violate the bound on individual terms. The conjecture asks for a constant gap in average local energy while every constraint retains bounded strength.',
'A useful way to read the two cases is that one input admits a low-energy global state, while in the other every state has appreciably higher average energy. The challenge is to preserve computational hardness at that coarse resolution. Checking a few local terms can detect a constant average discrepancy, but constructing a reduction with that discrepancy is the unresolved step.'
],
'TCS-6447':[
'Imagine a verifier that can inspect only a few qubits from a much larger proof message. Allowing several exchanges might help it ask better questions, but each extra message adds communication and potentially gives it more quantum information to retain. The strong model restricts the latter resource by requiring the message register to be returned.',
'A small number of inspected qubits is therefore not enough on its own. If the protocol requires an exponentially large transmitted proof, the communication target fails; if it relies on retaining a large quantum register, the strong-model target fails. The question asks for efficient communication and extremely limited quantum access simultaneously, with a reliable acceptance gap.'
],
'TCS-6448':[
'The same quantum verifier is used on both sides of the comparison. What changes is the proof supplied by a prover: either a classical string or a quantum state. A classical proof is still allowed to instruct the verifier to perform a sophisticated quantum computation, so this is not simply a comparison between classical and quantum algorithms.',
'To prove a separation, one needs a verification task whose positive instances admit useful quantum proofs but no comparably short classical proofs for any efficient quantum verifier. Observing that a particular state has a long classical description is not sufficient: a different classical argument might certify the same claim without describing that state.'
],
'TCS-6449':[
'For a fixed input length, the advice must support all inputs of that length. It cannot be tailored after seeing the particular instance. This makes it different from a witness, which is chosen to establish a claim about one input. A fresh copy of the same quantum advice state can be supplied for each computation.',
'The possible advantage is not that a measurement reveals an arbitrary amount of classical information from a few qubits. Instead, the algorithm might use the input to choose which computation to perform with the advice. The open question is whether polynomial-length classical advice can always support an equally effective computation for every input.'
],
'TCS-6450':[
'Alice receives x and Bob receives y. They need to compute a function of both inputs while exchanging as little information as possible. The classical protocol may use randomness, and the quantum protocol may begin with shared entanglement. The cost being compared is the communication, not the complexity of their local computation.',
'Totality means every pair of legal individual inputs must receive a correct answer, including pairs that a promise problem would exclude. A universal polynomial simulation would limit quantum communication savings across all such functions. A bound for a special composition, or one with an additional dependence on the input length, does not automatically supply that universal relation.'
],
'TCS-6451':[
'The goal is to select a nearly best candidate from a finite menu. A candidate might be a hypothesis or a model configuration, and its loss is evaluated on a private database. The algorithm needs one good choice; accurately estimating every candidate’s loss can be much more information than the task requires.',
'The interface restriction is the substance of the question. The algorithm sees only noisy answers and must split a fixed budget among its queries. Spending less budget on a query increases its Gaussian noise. Adaptively narrowing the candidate set might save information, but later decisions are based on earlier noisy comparisons. The target asks whether that process can lose no asymptotic factor relative to optimal direct selection.'
],
'TCS-6452':[
'Here the menu of candidates is finite and each loss changes by at most one when one database record changes. The algorithm tries to choose a candidate whose expected loss is close to the best available loss. Its only observations are sensitivity-bounded statistical queries with Laplace noise.',
'Taking more queries is not free in this interface: the noise scale of each answer grows with the total query count k. A method that estimates all losses can spend too much accuracy on candidates that will never be selected. A method that repeatedly eliminates candidates risks making irreversible choices from noisy comparisons. The problem asks whether a carefully organized query process can still reach logarithmic excess loss.'
],
'TCS-6453':[
'An average-case decision problem asks an algorithm to classify instances drawn from a specified distribution. A one-way function creates a different experiment: sample an input, reveal its efficiently computed image, and ask an adversary to find any valid preimage. The sampling process and the form of the required answer both matter.',
'A reduction has to turn the first kind of difficulty into the second while preserving efficient generation and a meaningful success probability. It cannot simply use a hard yes/no question as a function and assume its inverse is hard. The question is whether some average-case hardness can exist without yielding the basic inversion obstacle on which one-way-function cryptography is built.'
],
'TCS-6454':[
'Without noise, enough independent parity equations reveal the secret by linear algebra. Flipping some answers breaks that direct procedure: the learner must cope with equations whose right-hand sides may be wrong. At a low noise rate, most equations remain correct, which makes the precise source of hardness especially important.',
'A worst-case-to-average-case reduction would start with an arbitrary hard coding instance and turn it into the random samples used by LPN. It must preserve a usable noise regime and show how an LPN solver would solve the original task. Requiring two different coding tasks to be hard simultaneously is a stronger premise than deriving the guarantee from one standard worst-case problem.'
],
'TCS-6455':[
'Interactive proofs separate the effort of checking a computation from the effort of producing a convincing transcript. The usual class equality allows an honest prover to use enormous resources. That is enough for a complexity-class statement, but does not establish that proof generation is efficient relative to the computation being certified.',
'The target compares the honest prover directly with the original running time T. A prover using a polynomial in T would have controlled overhead even when the verifier has only polynomial time in the input length. Soundness still has to hold against a cheating prover of unlimited power; restricting the honest prover does not weaken the adversary in the definition.'
],
'TCS-6456':[
'The two-dimensional picture separates an array into contributions organized by rows and by columns. The desired inequality prevents a large amount of structured contribution from cancelling so thoroughly that the final array has very small support. The constant must work across growing block lengths.',
'In higher dimensions there are more directions and more ways for contributions to overlap. Good distance in each constituent code does not by itself control cancellation between these directional pieces. The question is whether the stated arithmetic structure of the evaluation sets forces a uniform expansion guarantee despite those additional interactions. Such a result must establish the full higher-dimensional decomposition inequality, not just verify individual codewords.'
]
}
for id,paragraphs in additions.items():
 f=BASE/'cards'/(id+'.json');c=json.loads(f.read_text())
 first=c.get('context_blocks',[{'text':c['context'],'citation':c['references'][0]['id']}])[0]
 c['context_blocks']=[first]+[{'text':p} for p in paragraphs]
 c['context']='\n\n'.join(p['text'] for p in c['context_blocks'])
 if id=='TCS-6452':c['formal']=c['formal'].replace('In the same finite-selection setting with sensitivity-1 losses,','Let $Y$ be a finite set of candidates, each with a public loss function $\\ell_y$ of sensitivity one under a one-record database change. To access the database,')
 f.write_text(json.dumps(c,ensure_ascii=False,indent=2));publish()
