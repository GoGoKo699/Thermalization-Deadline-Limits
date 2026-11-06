# Related work and attribution

The question is whether one machine, given physical access to an unknown Hamiltonian, can prepare the appropriate Gibbs marginal with a common deadline. The contribution established in the [scientific account](../science/README.md) is the sharp accuracy dependence of that deadline on a continuous qubit family, together with its separation from exact random stopping.

Several ingredients have substantial antecedents. This page identifies the theorem or model used from each source and the precise distinction relevant to the present result. Bibliographic entries are collected in [references.bib](references.bib).

## Planckian thermalization

**Paolo Abiuso, Alberto Rolandi, John Calsamiglia, Pavel Sekatski and Martí Perarnau-Llobet, “An information-theoretic proof of the Planckian bound for thermalization.”** Nature Physics, published 24 September 2026, [DOI: 10.1038/s41567-026-03397-y](https://www.nature.com/articles/s41567-026-03397-y). The complete source used for theorem-level comparison is [arXiv:2506.19188v1](https://arxiv.org/html/2506.19188v1).

Section II formulates thermalization by an apparatus whose initial information and controls are independent of the unknown Hamiltonian. Its information-geometric comparison gives the scale $`\beta\hbar`$. Section III.3 and Appendix F construct exact saturation for a specified pair of Hamiltonians. The approximate pairwise bound in Appendix E remains finite as the error vanishes.

The present result retains that operational premise and requires one machine to work on an interval. The [analytic-response bound](../science/analytic_response.md) and [Gibbs coefficient calculation](../science/deadline_bound.md) then give a uniform logarithmic precision cost. This does not contradict exact pairwise saturation.

**Comparison boundary:** the publisher's article metadata and abstract were verified, but its published Supplementary Information was not retrieved. The detailed comparison above is to the specified complete preprint; it is not a claim that an uninspected supplement lacks a theorem.

## Nacu-Peres analytic coin simulation

**Şerban Nacu and Yuval Peres, “Fast simulation of new coins from old.”** Annals of Applied Probability **15**(1A), 93–115 (2005), [DOI: 10.1214/105051604000000549](https://doi.org/10.1214/105051604000000549); full primary text [arXiv:math/0309222v5](https://arxiv.org/pdf/math/0309222).

Theorem 2 supplies exact simulation of a real-analytic target bias with an exponentially decaying input-coin count. Proposition 21 makes the tail bound uniform over a closed domain. The finite-word stopping formulation, including Proposition 3, supports truncation to a finite Boolean decision table.

This is the constructive theorem used here. The [Ramsey experiment](../science/thermal_coin.md) supplies the input bias, and a specified analytic transformation produces the Gibbs population. Both exactness and the uniform exponential tail are inherited from Nacu and Peres. The present account derives the physical realization, the finite-control deadline bound and its comparison with the quantum converse; it does not claim a new general Bernoulli-factory theorem.

## Analytic ensemble control

**Karine Beauchard, Jean-Michel Coron and Pierre Rouchon, “Controllability issues for continuous-spectrum systems and ensemble controllability of Bloch Equations.”** Communications in Mathematical Physics **296**, 525–557 (2010), [DOI: 10.1007/s00220-010-1008-9](https://doi.org/10.1007/s00220-010-1008-9); [arXiv:0903.2720](https://arxiv.org/pdf/0903.2720).

Theorem 5(i) establishes holomorphic dependence of finite-time Bloch evolution on an unknown frequency under square-integrable transverse controls. Part (ii) gives a reachability obstruction under its bounded-control assumptions. This is a direct antecedent for using parameter analyticity in a continuously varying quantum ensemble.

The present converse permits an arbitrary apparatus, discarded records and mixed output marginals. It controls exponential type by the charged signal action and uses noncancelling Gibbs coefficients to obtain an explicit error floor. The qualitative analytic method is established background; the target-specific quantitative consequence and stopping comparison are the statements proved here.

## Gibbs-preparation lower bounds

**Jordi Weggemans, “Lower Bounds for Unitary Property Testing with Proofs and Advice.”** Quantum **9**, 1717 (2025), [DOI: 10.22331/q-2025-04-18-1717](https://doi.org/10.22331/q-2025-04-18-1717); [arXiv:2401.07912v3](https://arxiv.org/html/2401.07912v3).

Section 4.2.1, Claim 4, gives an $`\Omega(\beta)`$ block-encoding query lower bound for Gibbs preparation at trace-distance error at most $`1/24`$. Its reduction compares two diagonal qubit Hamiltonians. It does not state the vanishing-error logarithm for a continuous family.

**Chi-Fang Chen, Michael J. Kastoryano, Fernando G. S. L. Brandão and András Gilyén, “Quantum Thermal State Preparation.”** [arXiv:2303.18224v2](https://arxiv.org/pdf/2303.18224), 15 November 2023.

Appendix G, Propositions G.4–G.5, establishes an $`\Omega(\beta)`$ Hamiltonian-simulation time requirement for Gibbs-related reflection and preparation, using sensitivity to a Hamiltonian perturbation. This continuous-time resource is closely related to the present one. The additional conclusion here concerns uniform precision on an interval and the distinction between deterministic and random termination.

These prior bounds supply relevant thermal-scale obstructions. Their algorithmic setting alone is not grounds to dismiss them; the model, error regime and quantifiers determine the comparison.

## Precision bounds for quantum transformations

**Nikhil S. Mande and Ronald de Wolf, “Tight Bounds for Quantum Phase Estimation and Related Problems.”** Quantum **10**, 2140 (2026), [DOI: 10.22331/q-2026-06-15-2140](https://quantum-journal.org/papers/q-2026-06-15-2140/); [arXiv:2305.04908v3](https://arxiv.org/pdf/2305.04908).

Theorem 1.3 gives $`\Omega(\delta^{-1}\log(1/\epsilon))`$ queries for phase estimation with precision $`\delta`$ and failure probability $`\epsilon`$, matching the corresponding upper order. Its trigonometric approximation argument is an important precision-method precedent. Here the error is the trace distance of one smooth Gibbs output, rather than failure of a classical estimate. A correctly biased sample need not reveal the unknown parameter accurately, so the phase-estimation theorem does not directly imply the sampling converse.

**Anthony Yuezhang Liu, Adam Wesołowski, Jayne Thompson, Mile Gu and Lirandë Pira, “Optimal query complexity for fractional quantum evolution.”** [arXiv:2610.01940v1](https://arxiv.org/abs/2610.01940), 1 October 2026.

Theorems 2–4 establish matching $`\Theta(\delta^{-1}\log(1/\epsilon))`$ fixed-unitary query complexity for fractional evolution $`U^t`$. Here $`\delta`$ is the spectral gap from the branch cut, and $`t`$ is bounded away from zero and one, with constants depending on that separation. Appendix A includes dilated feedback; Appendix E gives a functional lower bound for a prescribed finite frequency set. These are close approximation-method antecedents. Fixed applications of $`U`$ and $`U^\dagger`$ differ from arbitrary-duration Hamiltonian interrogation, a distinction explicitly discussed in that paper. Its fractional-unitary target and spectral-access assumptions do not establish the mixed Gibbs-marginal or random-stopping statements here.

## Quantum Bernoulli factories

**Howard Dale, David Jennings and Terry Rudolph, “Provable quantum advantage in randomness processing.”** Nature Communications **6**, 8203 (2015), [DOI: 10.1038/ncomms9203](https://www.nature.com/articles/ncomms9203).

This work studies processing copies of coherent qubits with an unknown bias and demonstrates advantages over classical coin processing. Its input-copy resource and random input length differ from a common deadline for unknown-Hamiltonian exposure. The matching construction in this repository uses classical processing of Ramsey bits; it requires no quantum advantage for the factory itself.

## The resulting distinction

| Ingredient | Attribution or role |
|---|---|
| Hamiltonian-independent thermalization machine | Planckian framework and standard quantum control/query models |
| Analytic dependence on an unknown frequency | Bounded-perturbation analysis; explicit ensemble-control antecedent |
| Approximation hardness as a quantum resource converse | Established polynomial and analytic methods |
| Exact analytic coin simulation with uniform exponential tails | Nacu–Peres theorem |
| Action-controlled response plus noncancelling Gibbs coefficients | The quantitative deadline converse derived in this project |
| Ramsey realization and charged finite control pulses | Matching construction derived in this project |
| Necessary stopping tails, sharp deadline quantiles and sharp worst-case mean order | Operational consequences proved in this project |

The source comparison supports a bounded distinction, not an exhaustive priority guarantee. The central claim includes the model and both termination requirements. The logarithm alone is not presented as a new universal law, and the construction does not establish fixed-strength runtime, efficient compilation or economical memory.
