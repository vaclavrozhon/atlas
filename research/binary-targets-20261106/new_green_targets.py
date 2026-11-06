"""Follow-up review of cards turned green during the owner's session."""

for number in ['0949', '1005', '6508', '6586', '6640', '6728', '6731', '6821', '6851', '7289', '7478']:
    retain(number, 'Turned green in the shared selection during this review. The existing statement already has a concrete binary target; no formulation change is needed.')
retain('7473', 'Turned green during the review. Retained the deterministic online-bin-packing optimum to absolute 0.01; the source does not single out a canonical exact threshold.')

d=original('6590')
revise('6590', 'Factor-two subtour-LP gap for asymmetric TSP',
       r'Is \(\operatorname{OPT}_{\mathrm{ATSP}}(c)\le2\,\mathrm{LP}_{\mathrm{ATSP}}(c)\) for every integer \(n\ge2\) and every nonnegative directed metric \(c\) on \(n\) vertices with \(\mathrm{LP}_{\mathrm{ATSP}}(c)>0\), using the Hamiltonian-tour objective and degree-constrained subtour linear program below? Equivalently, is the universal integrality gap \(\Gamma_{\mathrm{ATSP}}=2\), since the matching lower bound is known? This is an existence inequality; no efficient rounding algorithm is required.',
       'Newly green during the session; restored the explicit factor-two conjecture in Traub–Vygen Open Problem 3.19 while retaining the directed-metric subtour LP.',
       ['An asymmetric traveling-salesman tour visits every city once, and travel costs may depend on direction.', 'The subtour linear program permits fractional arcs while enforcing degree and cut constraints.', 'The card asks whether an optimal tour always costs at most twice this fractional optimum.', 'The factor concerns the strength of this specific relaxation and does not require an efficient construction.', 'The directed-metric model is distinct from the symmetric traveling-salesman conjecture.'],
       context={0:'The selected binary question is the factor-two subtour-LP integrality-gap conjecture. A proof of the universal inequality or one instance with a strictly larger ratio answers it; a complete determination of any alternative gap is not required.'},
       refs=['https://www.or.uni-bonn.de/tspbook/book.pdf'])

