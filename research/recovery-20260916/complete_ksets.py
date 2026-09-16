"""Individual source and formulation review of the planar k-set function."""
import json
import sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT/'research/card-completion-20260913'))
from complete_review import complete,ref,block,progress
from review_queue import read_claims
identifier='TCS-0318'
old=json.loads((ROOT/'data/cards'/f'{identifier}.json').read_text())
claim=read_claims(ROOT)[identifier]
refs=old['references']
refs[1].update(url='https://courses.cs.duke.edu/fall08/cps234/handouts/dey.pdf',
 locator='Discrete & Computational Geometry 19, 373–382 (1998); §2 definitions and §3 Theorem 3.3; DOI 10.1007/PL00009354')
refs[3]['locator']='Contemporary Mathematics 453, 299–305 (2008); §1: directed-edge correspondence and lower bound (1.2)'
notes=[
 'Preserved the restored planar extremal-function target, full parameter domain, constant-factor acceptance and assessed importance.',
 'Replaced broken inline formulas by a complete set-family definition and exact strict-separation inequalities.',
 'Specified universal constants before all parameter pairs and the all-point-sets upper bound versus per-pair existence lower bound.',
 'Checked the one-index difference between k-sets and directed (k−1)-edges; halving subsets have k=n/2.',
 'Distinguished improvements in a lower-bound exponent constant and subtractive upper-bound terms from closure of the asymptotic gap.',
]
sources=[
 'Read TOPP Problem 7, revision history to 14 June 2025, still labelled open when accessed on 16 September 2026.',
 'Read Dey’s final 1998 paper §1, §2 and Theorem 3.3: the theorem counts (k+1)-sets and yields the stated bound after reindexing.',
 'Read Tóth’s 2001 publisher abstract: the construction is quantified for all n≥2k>0; full proof not independently audited.',
 'Read Nivasch §1, definitions and (1.2), including the every-even-n scope and the factor-two conversion from undirected halving edges.',
 'Read Alonso–López–Rodrigo 2024 abstract, introduction and conclusion: subtractive linear improvement and finite-size bounds, unchanged leading exponent.',
 'A bounded later-work search through 16 September 2026 found no matching general planar upper and lower bounds; papers about nongeometric k-subsets do not address this target.',
]
status=('The TOPP entry revised in June 2025 still lists the planar extremal problem as open. '
 'The checked bounds leave an unbounded gap for growing k. '
 'The 2024 halving-line refinement does not change the upper exponent, and the cited improved halving construction changes a constant in its lower exponent. '
 'No matching general bound was found in the bounded review through 16 September 2026; this review does not independently certify all cited proofs.')
complete(identifier,dict(
 formal=r'''For a finite set \(P\subseteq\mathbb R^2\), let
\[
\mathcal S_k(P)=\bigl\{S\subseteq P:\ |S|=k,\ 
\exists(a,b)\in\mathbb R^2\setminus\{(0,0)\}\ 
\exists t\in\mathbb R:\ 
a x+b y<t\ \forall(x,y)\in S,\ 
a x+b y>t\ \forall(x,y)\in P\setminus S\bigr\}.
\]
For integers \(n\ge2\) and \(1\le k\le\lfloor n/2\rfloor\), define
\[
K_2(n,k)=
\max_{\substack{P\subseteq\mathbb R^2,\ |P|=n\\
                 \text{no three points of }P\text{ are collinear}}}
|\mathcal S_k(P)|.
\]
Determine a positive real-valued function \(F(n,k)\), together with universal real constants \(0<c\le C<\infty\), such that
\[
cF(n,k)\le K_2(n,k)\le CF(n,k)
\quad\text{for every }n\ge2,\quad
1\le k\le\lfloor n/2\rfloor.
\]''',
 definitions=r'''The plane \(\mathbb R^2\) has arbitrary real coordinates. A point set contains distinct points. General position here means exactly that no three points lie on one affine line; there is no grid, precision, distribution or convex-position restriction.

The affine line \(a x+b y=t\) has nonzero normal vector \((a,b)\). The strict inequalities in the definition place all points of \(S\) on one side and all other points on the opposite side. In particular the separating line contains no input point. A member of \(\mathcal S_k(P)\) is a k-set. Each subset is counted once, regardless of how many lines separate it.

The maximum is well-defined: every count is an integer between zero and \(\binom nk\), and there are general-position point sets of each permitted size. Thus the set of attained counts is a nonempty finite set of integers even though coordinates range over infinitely many possibilities.

The domain of \(F\) consists of every integer pair specified in the statement. The constants \(c,C\) must not depend on \(n\), \(k\), the point set or its coordinates. In particular, \(k\) may grow with \(n\). Bounds for a single fixed \(k\), only the balanced case, or only a random model do not determine this whole function.

The upper inequality means that every permitted \(P\) has at most \(CF(n,k)\) k-sets. The lower inequality means that for every permitted pair \(n,k\), at least one such \(P\) has at least \(cF(n,k)\) k-sets. Different pairs may use different point sets. No efficient construction of these sets is required.

Complementing subsets gives the same count for \(k\) and \(n-k\). Sizes zero and \(n\) each give one subset, so the stated domain captures the nontrivial range. The target is a combinatorial extremal function, not the time complexity of listing k-sets.

In the context, a directed j-edge joins two input points and has exactly \(j\) other points strictly to its left. For even \(n\), an undirected halving edge has \((n-2)/2\) other points on each side of its supporting line. The line through this edge is not a strict separator, since it passes through two points.''',
 answer_criterion=r'''Supply \(F,c,C\) and complete mathematically correct proofs checked in Lean of both inequalities throughout the stated domain. The upper proof must cover all permitted point sets, and the lower proof must establish existence for every parameter pair. No predetermined formula grammar or closed form is required, but simply repeating the defining extremum under a new name is insufficient. Finite boundary cases must be covered; they may be absorbed by choosing larger universal constants when justified. This user-retained asymptotic target uses constant-factor precision, not additive \(1/100\). A one-sided bound, a halving-only result or constants depending on a growing parameter does not suffice.''',
 references=refs,
 source_formulation=dict(text='What is the largest number of k-element subsets of an n-point set that can be cut off by a hyperplane?',
 caption='Editorial paraphrase; this card retains the approved planar specialization',citation='problem',format='editorial_paraphrase'),
 context_blocks=[
 block('A linear cut realizes only a restricted collection of subsets of a point set. Fixing the subset size measures this restriction more precisely than counting all possible cuts together. The planar problem already exhibits the persistent gap in the broader higher-dimensional question.','problem'),
 block(r'For \(k=1\), the separable points are precisely the vertices of the convex hull, the smallest convex set containing \(P\). Their maximum number is \(n\). The unresolved part concerns how the count grows when the selected subset size grows too.','upper'),
 block('Point-line duality relates these counts to levels in arrangements of lines. A level follows the positions with a prescribed number of arrangement lines below them. Such complexity bounds occur in geometric selection and parametric optimization, where the preferred solution changes with a parameter.','upper'),
 block(r'Dey’s general upper bound is \(O(nk^{1/3})\) on the domain of this card. Tóth’s constructions give \(n\exp(\Omega(\sqrt{\log k}))\) k-sets. Thus the existing upper and lower estimates do not differ by only a universal constant when \(k\) increases.','lower'),
 block(r'In the plane, k-sets correspond to directed \((k-1)\)-edges. For even \(n\), subsets of size \(n/2\) therefore correspond to the two orientations of undirected halving edges. Consequently \(K_2(n,n/2)\) is twice the maximum number of halving edges. The index \((n-2)/2\) counts points on one side of a halving edge, not the size of a halving subset.','nivasch'),
 block(r'Nivasch’s construction gives \(\Omega\!\left(n\exp(\sqrt{\ln4}\sqrt{\ln n})/\sqrt{\ln n}\right)\) halving edges for every even \(n\), with an asymptotically larger exponent constant than earlier constructions. Here \(\ln\) is the natural logarithm. This lower-bound expression grows faster than \(n(\log n)^A\) for every fixed \(A\), but slower than \(n^{1+\varepsilon}\) for every fixed \(\varepsilon>0\). These comparisons concern the displayed construction, not a proved upper bound on the unknown optimum.','nivasch'),
 block('The 2024 halving-line paper improves a subtractive term proportional to the number of points and some finite-size bounds. Its leading upper growth remains proportional to the four-thirds power. Better lower-order terms alone do not give the matching function requested here.','recent'),
 ],
 progress=[
 progress('1997–1998',r'Dey obtains the planar upper bound \(O(nk^{1/3})\) on the nontrivial domain.','upper'),
 progress('2000–2001',r'Tóth constructs \(n\exp(\Omega(\sqrt{\log k}))\) k-sets for every \(n\ge2k>0\).','lower'),
 progress('2008','Nivasch improves the exponent constant in the known halving-edge construction.','nivasch'),
 progress('2024-07-22','The published halving-line refinement improves subtractive and finite-size upper bounds.','recent'),
 progress('2025-06-14','The revised TOPP entry retains the planar extremal gap.','problem'),
 progress('2026-09-16','The individual review checks the joint parameter domain, strict separation and the halving-edge indexing.','problem'),
 ],
),notes,sources,status,summary=[
 'A planar k-set is a k-element subset strictly separated from the remaining points by a line.',
 'The extremal function maximizes the number of these subsets over n distinct points with no three collinear.',
 'The task is to determine one function within universal constant factors for every n and every k between one and half of n.',
 'Acceptance requires both a bound for all point sets and matching examples for every parameter pair.',
 'The checked general bounds and newer halving-line refinements still leave the asymptotic function unresolved.',
],expected_sha256=claim['input_sha256'],claim_token=claim['token'])
