# The scientific account

A thermalization machine knows the temperature and a range of possible
Hamiltonians. It must produce the Gibbs state appropriate to the Hamiltonian
it encounters. This project asks how the finishing-time requirement changes
the attainable accuracy.

For one unknown known-axis qubit on a fixed thermal interval, the optimal
deterministic deadline is

```math
T_\varepsilon^{\mathrm{opt}}
=\Theta\!\left(\beta\hbar\log\frac1\varepsilon\right).
```

With ideal instruments and random stopping, exact preparation instead has
optimal worst-case mean interrogation time $`\Theta(\beta\hbar)`$.
Necessary rare long runs reconcile these two statements.

## Reading route

| Question | Authoritative account |
|---|---|
| What is unknown, what is charged, and which output must be accurate? | [The task and exact statements](model.md) |
| Why do arbitrary controls and measurements still give a bounded analytic response? | [Finite-time responses](analytic_response.md) |
| Why does a Gibbs response force an exponentially small but nonzero error? | [The deadline lower bound](deadline_bound.md) |
| How can physical interrogations generate the correct thermal probabilities? | [Ramsey coins and Gibbs preparation](thermal_coin.md) |
| Does the construction survive finite pulses while the unknown Hamiltonian remains on? | [Finite controls](finite_controls.md) |
| How can exact output have finite mean time, and which late runs are unavoidable? | [Stopping times and quantiles](stopping_time.md) |
| How does the result change the thermalization-timescale question? | [Physical interpretation](interpretation.md) |

The argument has two complementary parts. On the converse side, a finite
exposure budget limits the complex growth of every output observable.
The poles of the Gibbs response then force a quantitative approximation error.
On the construction side, Ramsey experiments make biased coins, and an
existing analytic coin-simulation theorem converts them into thermal
statistics. A finite cutoff produces the deadline upper bound; leaving the
factory running produces the exact stopping process.

The [related-work account](../references/RELATED_WORK.md) identifies the
Planckian framework, analytic ensemble-control and quantum-query antecedents,
and the inherited Bernoulli-factory theorem. The
[finite checks](../verification/README.md) independently verify the scalar
identities, normalization and selected control examples.

The conclusions are uniform for the declared thermal band. They allow broad
control resources and score the output marginal after the apparatus is
discarded. Each proof keeps its deadline, reference-system and stopping-time
quantifiers explicit.
