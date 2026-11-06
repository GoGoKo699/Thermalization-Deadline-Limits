# Deadlines, accuracy and thermal statistics

The main result concerns the information required to produce a thermal state when the Hamiltonian is not numerically supplied to the machine. A controller knows a family of Hamiltonians and can interact with the physical system. It must obtain the dependence of its output on the unknown coefficient through that interaction. The [model](model.md) makes this requirement precise.

## A precision cost beyond a thermal timescale

The [Planckian thermalization framework](../references/RELATED_WORK.md#planckian-thermalization) identifies a timescale proportional to $`\beta\hbar`$ by comparing two possible Hamiltonians. A continuous family introduces a further requirement: one response function must approximate every target in the interval, with the same deadline.

For the fixed thermal band studied here, the optimal deadline is

```math
T_\varepsilon^{\mathrm{opt}}
=\Theta\!\left(\beta\hbar\log\frac1\varepsilon\right).
```

The lower bound holds even with arbitrarily strong parameter-independent controls, large auxiliary systems and feedback. It is therefore not a statement about one relaxation equation or one poorly chosen bath. The matching construction also shows that no additional power of inverse accuracy is required by this broad model.

This conclusion is compatible with exact finite-time preparation for a specified pair of Hamiltonians. Matching two values does not require reproducing the full parameter-dependent response on an interval. It is also compatible with immediate programmed preparation when the actual Hamiltonian is already known numerically; that is different initial information.

The deterministic lower bound also covers ideal instantaneous instruments. The deadline-versus-expectation separation therefore holds within that same ideal model. The finite-pulse upper separately shows that the optimal deterministic scaling survives when all physical control time is charged.

## Why the complex poles matter

A finite exposure budget limits how rapidly an output expectation can grow when the unknown Hamiltonian coefficient is continued into the complex plane. The physical parameter remains real; complex continuation is a proof device.

For dimensionless action $`\mathfrak a`$, the [analytic-response proof](analytic_response.md) gives

```math
|g(x+iv)|\le e^{2\mathfrak a|v|}.
```

The thermal response $`-\tanh y`$ instead has poles at imaginary distance $`\pi/2`$ from the real axis. Exact agreement on an interval would contradict analytic continuation. To quantify approximate agreement, the [deadline proof](deadline_bound.md) compares Chebyshev coefficients. The pole contributions to each odd target coefficient have the same sign. A response with the permitted complex growth cannot reproduce all of those coefficients at a fixed action.

The result does not assert that every problem with a complex pole has the same exponent. The stated constants come from this target, interval and action norm. Analytic ensemble control and quantum approximation lower bounds are [methodological antecedents](../references/RELATED_WORK.md#analytic-ensemble-control); the operational consequence here is specific to thermal preparation.

## Sampling need not estimate the Hamiltonian

The upper construction first obtains independent bits with bias

```math
p(y)=\frac{1+\sin(y/2)}2
```

from Ramsey interrogations of duration $`\beta\hbar/4`$. The attributed [analytic Bernoulli factory](thermal_coin.md) converts these bits into one bit of bias $`q(y)=1/(1+e^{2y})`$ without receiving the value of $`y`$. Preparing the corresponding known energy eigenstate produces the Gibbs marginal.

A single correct thermal sample does not provide an accurate numerical estimate of the unknown Hamiltonian. This is why a phase-estimation failure bound cannot simply be substituted for the thermalization lower bound. The error of a classical estimate and the trace error of a sampled mixed state are different operational quantities.

The finite-prefix factory can be encoded in a finite decision table. Its size may be large. The [finite-control proof](finite_controls.md) implements that particular fixed-slot construction with finite-duration pulses and bounds the unknown drift during them. It establishes an existence upper bound for elapsed time, without establishing an efficient gate synthesis or an economical apparatus.

## Why finite expectation permits exactness

Leaving the factory running gives an exact thermal bit after an almost-surely finite number of interrogations. Its input-count tail is uniformly exponential, so its worst-case mean interrogation time is $`O(\beta\hbar)`$. The lower bound supplies the matching order for that mean.

Exactness refers to the terminal marginal after all records are discarded. Individual completed histories can output pure eigenstates. Conditioning on completion before a deadline generally changes their mixture, so exact terminal output does not imply an exact finite-deadline output.

Truncating an exact protocol at time $`T`$ changes the state by at most the probability of an unfinished run. Thus the deterministic error floor forces

```math
\sup_y\Pr_y(\tau\gt T)
\ge\frac3{400}e^{-12T/(\beta\hbar)}.
```

The parameter attaining the worst tail may depend on $`T`$. This minimax statement supplies a necessary supply of late runs without asserting the same lower tail at every fixed parameter. The [stopping-time proof](stopping_time.md) keeps these quantifiers and derives the optimal deadline-quantile order.

## What is deliberately unrestricted

| Resource or requirement | Status in this project |
|---|---|
| Unknown-Hamiltonian exposure | Charged through signal action; one continuously active qubit gives $`T/(\beta\hbar)`$ |
| Physical control-pulse time | Included in the finite-control upper and in elapsed-time lower bounds |
| Apparatus dimension and control strength | Finite for each constructed finite-accuracy machine, with no common bound across accuracies |
| Gate count, compilation and classical memory | Unrestricted; the finite table is an existence construction |
| Input state | The lower needs one parameter-independent input; the upper replaces any input, including entangled input |
| Measurement records and entropy sink | May be retained or discarded; no return or erasure-work condition |
| Parallel copies of the unknown signal | Their joint signal generator must be charged; they are not free copies |
| Exact random stopping | Ideal instruments, protected memory and potentially unbounded histories |
| Autonomous locality, fixed bandwidth or fixed control strength | Additional constraints whose sharp runtime is not established here |

The target is a system marginal. Correlation between that marginal and the discarded controller is permitted. Requiring reusable uncorrelated machinery, bounding heat or work, or insisting on autonomous local relaxation would define additional tasks.

## Temperature and bandwidth

The dimensionless interval $`y\in[-1,1]`$ corresponds to physical eigenvalues $`\pm y/\beta`$. Varying $`\beta`$ while keeping that interval fixed changes the physical range of possible splittings. This is the scaling in which the constants in the theorems are uniform.

If a laboratory instead fixes a positive gap interval and takes temperature to zero, both the dimensionless interval and the target probabilities change. The present proof does not establish the sharp joint crossover for that problem. Likewise, a general many-body mixing law, a best exponent constant and a fixed-strength implementation remain outside the established result.

The completed statement is a sharp comparison of two finishing requirements for the declared unknown-qubit task: a common deadline has a logarithmic accuracy cost, while exact random stopping has finite optimal mean time and unavoidable worst-case late runs.
