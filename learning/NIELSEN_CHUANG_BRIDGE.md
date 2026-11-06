# From Nielsen–Chuang to thermalization deadline limits

Suppose a device receives a qubit whose energy splitting is unknown. Its energy eigenvectors and the temperature are known. The device can let that qubit evolve, prepare auxiliary systems, apply known controls and use measurement outcomes. It must return the thermal state appropriate to the actual splitting. The question is how much interaction time is needed when the same device must work throughout a continuous interval of possible Hamiltonians.

This project distinguishes two finishing requirements. A common deterministic deadline has an optimal logarithmic cost in inverse error. Exact output is possible with a random stopping time and finite worst-case mean interrogation time in the stated ideal-instrument model. Rare late runs make those conclusions compatible. The [30-milestone map](MILESTONES.md) organizes the complete understanding route; this bridge supplies the connections from the selected textbook to the [canonical scientific account](../science/README.md).

## The selected educational anchor

The single educational anchor is **Michael A. Nielsen and Isaac L. Chuang, _Quantum Computation and Quantum Information_, 10th Anniversary Edition, Cambridge University Press (2010)**, ISBN **9781107002173**, DOI [10.1017/CBO9780511976667](https://doi.org/10.1017/CBO9780511976667). The [Cambridge edition page](https://www.cambridge.org/highereducation/books/quantum-computation-and-quantum-information/01E10196D0A682A6AEFFEA52D53BE9AE) identifies the edition.

Use the following chapter-level pointers as needed. Reading the whole book first is unnecessary. The book supplies the quantum-information foundations; the Gibbs-task reduction, charged-time model, complex approximation argument and deadline comparison are developed here and in the linked project proofs.

| Verified chapter and page range | Foundation used in this project |
|---|---|
| Chapter 2, “Introduction to quantum mechanics,” pp. 60–119 | State vectors, density operators, unitary evolution, measurement and composite systems. |
| Chapter 4, “Quantum circuits,” pp. 171–215 | Known gates, auxiliary registers and coherent implementations of finite decision rules. |
| Chapter 8, “Quantum noise and quantum operations,” pp. 353–398 | Quantum operations, environmental representations, discarded systems and measurement records. |
| Chapter 9, “Distance measures for quantum information,” pp. 399–424 | Distinguishing states operationally and interpreting approximation error. |

These are chapter locations, not claims that Nielsen–Chuang proves the project-specific deadline theorem. The complex-analysis and Chebyshev ingredients are explained below without adding a second textbook prerequisite. The Nacu–Peres coin-simulation theorem is a separately attributed research dependency.

## Translating the objects and notation

A qubit has a two-dimensional state space. Fix the computational basis so that the Pauli operator $`Z`$ has eigenvalue $`+1`$ on $`|0\rangle`$ and $`-1`$ on $`|1\rangle`$. These labels remain fixed even when the energies exchange order.

| Symbol | Role in this project |
|---|---|
| $`S`$ | The one qubit on which the unknown microscopic Hamiltonian acts. |
| $`M`$ | The apparatus: auxiliary qubits, records and registers that may eventually be discarded. |
| $`R`$ | An untouched reference that may initially be entangled with the incoming system. |
| $`y`$ | A dimensionless unknown real number in the promised interval $`[-1,1]`$. |
| $`\beta`$ | The known inverse temperature, with units of inverse energy. |
| $`\hbar`$ | Planck’s reduced constant; $`\beta\hbar`$ therefore has units of time. |
| $`H_y`$ | The unknown system Hamiltonian. |
| $`K(t)`$ | A known, parameter-independent control Hamiltonian acting on system and apparatus. |
| $`\gamma_y`$ | The required Gibbs state on the retained system. |
| $`T`$ and $`\tau`$ | Respectively a common deterministic deadline and a random accumulated interrogation time. |

An operator norm $`\|A\|`$ measures the largest amplification of a vector by $`A`$. The trace norm $`\|A\|_1`$ is the sum of its singular values. For a Hermitian operator, it is the sum of the absolute values of its eigenvalues. Distinguishing these norms matters: the signal generator is bounded in operator norm, while the output error is measured in trace norm.

### From a density operator to Gibbs populations

A density operator $`\rho`$ is positive and has trace one. A pure state $`|\psi\rangle`$ has density operator $`|\psi\rangle\langle\psi|`$; a preparation that chooses states with classical probabilities has their probability-weighted average. The Born rule assigns probability $`\operatorname{Tr}(P\rho)`$ to a measurement projector $`P`$.

Here the Hamiltonian is

```math
H_y=\frac{y}{\beta}Z.
```

Its computational-basis energies are $`y/\beta`$ and $`-y/\beta`$. In a Gibbs state, the weight of an energy $`E`$ is proportional to $`e^{-\beta E}`$. Because the Hamiltonian is diagonal, its matrix exponential is obtained by exponentiating those two eigenvalues:

```math
e^{-\beta H_y}
=e^{-y}|0\rangle\langle0|+e^y|1\rangle\langle1|.
```

Dividing by the trace normalizes the probabilities. Thus

```math
\begin{aligned}
\gamma_y&=q(y)|0\rangle\langle0|
+[1-q(y)]|1\rangle\langle1|,\\
q(y)&=\frac{e^{-y}}{e^{-y}+e^y}=\frac1{1+e^{2y}}.
\end{aligned}
```

For positive $`y`$, $`|0\rangle`$ has the higher energy and the smaller population. At $`y=0`$, both populations are one half. For negative $`y`$, their ordering reverses. The same fixed computational basis works throughout the interval.

The expectation of $`Z`$ is the probability of zero minus the probability of one. The target response is consequently

```math
\operatorname{Tr}(Z\gamma_y)=2q(y)-1=-\tanh y,
\qquad
\gamma_y=\frac{I-\tanh(y)Z}{2}.
```

This simple scalar response is enough for the lower bound, although the task is preparation of a quantum state. The full assumptions and normalization are in [the thermalization model](../science/model.md#hamiltonian-and-target).

## What accuracy means, including a reference system

The project uses trace distance with the factor of one half:

```math
D(\rho,\sigma)=\frac12\|\rho-\sigma\|_1.
```

Operationally, this bounds the change in the probability of any measurement event. In particular, if a machine returns $`\rho_M(y)`$, its measured zero population cannot differ from $`q(y)`$ by more than its trace-distance error. For two states diagonal in the same computational basis, the converse also holds. Their difference has eigenvalues $`d`$ and $`-d`$, where $`d`$ is the difference of their zero populations, so

```math
D\!\left(
q'|0\rangle\langle0|+(1-q')|1\rangle\langle1|,
\gamma_y\right)=|q'-q(y)|.
```

For one fixed machine, its uniform error is

```math
E(M)=\sup_{y\in[-1,1]}D(\rho_M(y),\gamma_y).
```

The supremum enforces accuracy throughout the promised interval for that same machine. For a possibly nondiagonal output, define $`g(y)=\operatorname{Tr}[Z\rho_M(y)]`$. Since $`\|Z\|=1`$, trace-norm duality gives

```math
|g(y)+\tanh y|
\le\|\rho_M(y)-\gamma_y\|_1
=2D(\rho_M(y),\gamma_y).
```

The factor of two is load-bearing in the lower proof: a uniform state error $`E(M)`$ implies a scalar response error at most $`2E(M)`$.

### Preparation and replacement are distinct requirements

For the lower bound, the machine can start from any one fixed state independent of $`y`$, even a favorable pure state. A lower bound in this easier setting also constrains machines required to handle arbitrary incoming states.

The construction handles the stronger reset task. Its ideal target is the replacement channel

```math
\mathcal G_y(X)=\operatorname{Tr}(X)\gamma_y.
```

A channel is a linear, completely positive, trace-preserving map on operators. “Completely positive” ensures that applying it locally also gives a valid state when an untouched reference is present. If the input is $`\rho_{SR}`$, the desired replacement acts as

```math
(\mathcal G_y\otimes\operatorname{id}_R)(\rho_{SR})
=\gamma_y\otimes\rho_R,
\qquad
\rho_R=\operatorname{Tr}_S\rho_{SR}.
```

The reset removes the old system correlations while preserving the reference marginal. Physically, the incoming system state can be swapped into a discarded apparatus register. Fresh probes then supply the new output. An entropy sink and discarded registers are resources permitted by the model.

The diamond norm makes channel error uniform over inputs and their reference systems. For two replacement channels, its half-normalized value reduces exactly to the trace distance of the replacement states:

```math
\frac12\|\mathcal R_{\gamma'}-\mathcal G_y\|_\diamond
=D(\gamma',\gamma_y).
```

Indeed, the output difference on a joint state is $`(\gamma'-\gamma_y)\otimes\rho_R`$; tensoring with the positive trace-one operator $`\rho_R`$ does not change its trace norm. The [replacement argument](../science/thermal_coin.md#replacement-of-an-arbitrary-input) and [coherent realization](../science/finite_controls.md#why-coherent-records-give-the-same-channel) give the channel-level justification. The retained system may remain correlated with apparatus records that are discarded; returning reusable, uncorrelated machinery is a different requirement.

## From circuits and operations to the charged-time model

The joint dynamics obey

```math
\mathsf H_y(t)=H_y\otimes I_M+K(t).
```

The initial apparatus and the rule for choosing $`K(t)`$ are independent of the actual $`y`$. They may depend on the known temperature, the promised interval and the desired error. A measurement record may determine which operation comes next: the distribution of records depends on $`y`$, but the rule mapping a record to an operation is fixed beforehand. That is how a controller can learn from the system without receiving the answer as free initial information.

All elapsed time is charged while the unknown Hamiltonian acts, including control pulses. There is only one native unknown-Hamiltonian qubit. Adding simultaneously exposed copies would change the signal generator and must be charged through their combined action. The model places no common ceiling on control strength, apparatus dimension, gate count or compilation effort across different requested accuracies. These choices are explicit in [the model](../science/model.md#a-machine-with-a-deterministic-deadline).

### Why measurements do not escape the lower bound

A measurement with recorded outcomes can be represented by operators $`M_{r,a}`$ satisfying $`\sum_{r,a}M_{r,a}^\dagger M_{r,a}=I`$. The index $`r`$ is the observed result; $`a`$ can label additional environmental information. The map

```math
|\psi\rangle\longmapsto
\sum_{r,a}M_{r,a}|\psi\rangle
\otimes|r\rangle\otimes|r,a\rangle
```

preserves inner products, so it is an isometry and can be extended to a unitary with enough auxiliary space. The record can coherently control later operations. Keeping distinct outcomes in orthogonal environment states ensures that tracing those records produces the same probabilities as the measured protocol.

This representation retains every branch with its original weight. Dividing by a success probability would instead describe a conditional output. The project scores the unconditional state, including timeouts. The [instrument construction](../science/analytic_response.md#instruments-and-coherent-records) also explains how branch-dependent exposure lengths fit one common action cap: histories occupy orthogonal blocks, so their controlled generator has the largest block norm, rather than the sum of the histories’ norms.

## A complete Ramsey probability example

The constructive route begins with a single experiment. Prepare
$`|+\rangle=(|0\rangle+|1\rangle)/\sqrt2`$, let the system evolve for
$`t_0=\beta\hbar/4`$, and measure the Pauli observable $`Y`$.

The unitary and resulting state are

```math
\begin{aligned}
U_y&=e^{-iH_yt_0/\hbar}=e^{-iyZ/4},\\
|\psi_y\rangle&=
\frac{e^{-iy/4}|0\rangle+e^{iy/4}|1\rangle}{\sqrt2}.
\end{aligned}
```

The $`+Y`$ eigenstate is $`|+Y\rangle=(|0\rangle+i|1\rangle)/\sqrt2`$.
Applying the Born rule gives

```math
\begin{aligned}
p(y)&=|\langle+Y|\psi_y\rangle|^2\\
&=\frac14\left|e^{-iy/4}-ie^{iy/4}\right|^2\\
&=\frac{1+\sin(y/2)}2.
\end{aligned}
```

The phase accumulated between the two energy components has become a measurable probability. Recording $`+Y`$ as one and $`-Y`$ as zero supplies a classical coin whose unknown bias is $`p(y)`$. Fresh preparations give independent copies for each fixed $`y`$ in the ideal experiment.

**Worked example, not a lower-bound witness or a complete thermalizer.** Take $`y=1/2`$ only to evaluate this experiment. The controller still does not receive that value. One exposure of duration $`\beta\hbar/4`$ gives

```math
p(1/2)=\frac{1+\sin(1/4)}2\approx0.623702,
\qquad
q(1/2)=\frac1{1+e}\approx0.268941.
```

If the measured Ramsey bit were used directly to prepare $`|0\rangle`$ on one and $`|1\rangle`$ on zero, the zero population would be approximately $`0.623702`$. Its trace distance from the target would be approximately $`0.354761`$. Thus the Ramsey experiment supplies information in the form of a biased coin; a further transformation of that bias is essential. The [canonical Ramsey construction](../science/thermal_coin.md#the-ramsey-coin) makes that transformation precise.

### Turning Ramsey bits into thermal bits

Across the promised interval, the available biases lie in

```math
I=\left[\frac{1-\sin(1/2)}2,\frac{1+\sin(1/2)}2\right]
\subset(0,1).
```

Define the known function

```math
F(p)=\frac1{1+\exp[4\arcsin(2p-1)]}.
```

Since $`y/2\in[-1/2,1/2]`$, the principal arcsine reverses the sine in the Ramsey formula. Hence $`\arcsin(2p(y)-1)=y/2`$ and $`F(p(y))=q(y)`$. In the worked example, the exponent becomes $`4(1/4)=1`$, which recovers $`q(1/2)=1/(1+e)`$.

This algebra identifies the desired input-output relation. It does not give the controller the unknown number $`p`$ on which to evaluate $`F`$. A **Bernoulli factory** is an algorithm that instead reads independent bits of bias $`p`$ and uses a rule independent of $`p`$ to output one bit of bias $`F(p)`$. Sampling such a bit need not produce an accurate numerical estimate of the Hamiltonian.

**Imported theorem.** Serban Nacu and Yuval Peres, [“Fast simulation of new coins from old”](https://doi.org/10.1214/105051604000000549), _The Annals of Applied Probability_ **15**(1A), 93–115 (2005), provide the required result. Their Theorem 2 gives exact simulation for the real-analytic bias map on a closed interval inside $`(0,1)`$, with values in $`(0,1)`$. Proposition 21 supplies uniform exponential tail constants on the closed interval. The [author manuscript](https://arxiv.org/pdf/math/0309222) and the project’s [attribution and application](../references/RELATED_WORK.md#nacu-peres-analytic-coin-simulation) are the proof sources.

Here $`F`$ is analytic on a neighborhood of the fixed interval $`I`$, and its values stay strictly between zero and one. The theorem therefore yields one simulator, a terminal bit $`B`$ and a random input count $`N`$ such that

```math
\Pr_p(B=1)=F(p),
\qquad
\sup_{p\in I}\Pr_p(N\gt n)\le Ce^{-\lambda n},
```

for fixed constants $`C\ge1`$ and $`\lambda\gt0`$. They are independent of temperature and requested accuracy because $`F`$ and $`I`$ are dimensionless and fixed. The existence and tail theorem are inherited from Nacu–Peres; the physical Ramsey realization and its use in this thermalization task are the project’s construction.

At any finite cutoff, the simulator’s decisions are encoded by a finite table of observed bit strings. Proposition 3 supplies a consistent finite-word description, explained in [the decision-table account](../science/thermal_coin.md#finite-words-specify-every-decision). No actual value of $`y`$ or additional freely supplied unknown-bias coin is used.

## From a finite coin cutoff to a physical deadline

Stop the factory after $`n`$ input coins. If it has decided, retain its bit; if it has not, output the fixed fallback zero. Couple this truncated process to the exact one using the same infinite input sequence. Their outputs can differ only on $`N\gt n`$, so the truncated one-probability $`q_n(y)`$ obeys

```math
|q_n(y)-q(y)|\le\Pr_y(N\gt n)\le Ce^{-\lambda n}.
```

Prepare $`|0\rangle`$ when the resulting bit is one, and $`|1\rangle`$ when it is zero. The retained state is diagonal, so its trace-distance error equals the population error. By the replacement identity above, the same bound holds in half the diamond norm. Every timeout is included with its ordinary probability; the calculation never renormalizes a successful subset.

For $`0\lt\varepsilon\lt1/2`$, choosing

```math
n_\varepsilon=
\left\lceil\frac{\log(2C/\varepsilon)}{\lambda}\right\rceil
```

makes this ideal error at most $`\varepsilon/2`$. The machine can run all $`n_\varepsilon`$ Ramsey slots on every branch and apply one precompiled reversible decision table. Discarding the retained word register removes cross terms and reproduces the classical mixture. This gives a common schedule, whose interrogation portion lasts $`n_\varepsilon\beta\hbar/4`$.

### Accounting for the control pulses

Textbook circuit diagrams often suppress gate durations. The project must put that time back because the unknown Hamiltonian remains on. For each known gate, choose a Hermitian logarithm $`A_j`$ with $`W_j=e^{-iA_j}`$ and $`\|A_j\|\le\pi`$. Applying $`K_j=\hbar A_j/\delta_j`$ for a positive duration $`\delta_j`$ would implement the gate without the unknown drift. In the actual system, integrating that drift in the control interaction picture bounds the gate’s half-diamond error by $`\delta_j/(\beta\hbar)`$.

Adding the finitely many pulse errors bounds the circuit error by their total duration divided by $`\beta\hbar`$. Allocate total control duration $`\varepsilon\beta\hbar/2`$. Truncation and control errors then sum to at most $`\varepsilon`$, with

```math
T_\varepsilon\le\beta\hbar\left[
\frac14\left\lceil\frac{\log(2C/\varepsilon)}{\lambda}\right\rceil
+\frac{\varepsilon}{2}\right].
```

The [finite-control proof](../science/finite_controls.md) covers swaps, preparation, decision processing, output transfer and finite descriptions. Each constructed machine is finite at fixed positive accuracy. This is an existence result with unrestricted compilation and growing control resources, rather than a claim that the table or apparatus is economical. The proof bounds the entire imperfect circuit, so it does not assume that drift-perturbed physical coin experiments remain independent.

## The analytic bridge: why every finite-time machine is constrained

The lower proof begins with the same unitary dynamics but applies to every admissible machine, not just Ramsey experiments. For a general bounded unknown perturbation, write

```math
\mathsf H_y(t)=K(t)+yV(t),
\qquad
\mathfrak a=\frac1\hbar\int_0^T\|V(t)\|\,dt.
```

The dimensionless number $`\mathfrak a`$ is the **signal action**. For this always-on qubit, $`V=Z/\beta`$, giving $`\mathfrak a=T/(\beta\hbar)`$. Strong known controls can rotate the signal generator in an interaction picture, but unitary conjugation preserves its operator norm. They cannot enlarge the unknown signal’s charged action for free.

Temporarily replace the real coefficient $`y`$ by a complex number $`z=x+iv`$. This is a mathematical continuation, not a proposed complex physical Hamiltonian. The propagator’s time-ordered series has its $`n`$th coefficient bounded by $`\mathfrak a^n/n!`$. It therefore converges for every finite complex $`z`$: the propagator is **entire**, meaning complex analytic everywhere.

At a real $`x`$, evolution is unitary. The additional imaginary part can amplify norms by at most $`e^{\mathfrak a|v|}`$. A density-operator expectation contains two propagator factors, giving the project’s central response bound

```math
|g(x+iv)|\le e^{2\mathfrak a|v|}.
```

There is an important algebraic detail. The analytic continuation of the physical real-parameter expression uses the reflected adjoint $`U_z^\sharp=U_{\bar z}^\dagger`$. If $`U_z=\sum_n A_nz^n`$, then $`U_z^\sharp=\sum_n A_n^\dagger z^n`$, which is analytic. Directly using $`U_z^\dagger`$ would introduce $`\bar z`$ and spoil this argument. Positivity at complex $`z`$ is unnecessary; only the real-parameter state has a physical interpretation.

The [entire-response proof](../science/analytic_response.md) gives the complete estimate, its well-posedness assumptions, the coherent-record extension and the treatment of admissible limits. Those are research-level steps. The representation of quantum operations from the selected anchor explains why retained measurement records belong in the same analysis.

### Exact agreement already fails

The Gibbs response $`-\tanh z=-\sinh z/\cosh z`$ has poles where $`\cosh z=0`$, with the closest pair at $`z=\pm i\pi/2`$. An entire function cannot agree with it on a real interval. A short way to see this avoids evaluating a pole directly: if agreement held, the entire function

```math
\cosh z\,g(z)+\sinh z
```

would vanish on the interval. The identity theorem says an analytic function with such an accumulating set of zeros must vanish throughout its connected domain. Yet the displayed expression equals $`i`$ at $`z=i\pi/2`$, a contradiction.

This proves exact impossibility at a finite deadline. Quantitative approximation needs more: entire functions can approximate smooth targets very well on a real interval. The specific growth bound at fixed $`\mathfrak a`$ is what yields an error floor shared by all machines.

## The Chebyshev bridge: converting growth into an error floor

Chebyshev polynomials are defined on $`[-1,1]`$ by $`T_n(\cos\theta)=\cos(n\theta)`$. For example, $`T_0(x)=1`$, $`T_1(x)=x`$ and $`T_2(x)=2x^2-1`$. They turn approximation on the interval into a cosine-series problem. Use the coefficient convention

```math
a_n[f]=\frac2\pi\int_0^\pi
f(\cos\theta)\cos(n\theta)\,d\theta.
```

Since $`|\cos(n\theta)|\le1`$, uniformly changing a function by at most $`\delta`$ changes each coefficient by at most $`2\delta`$. Our trace-error estimate therefore implies

```math
|a_n[g]+a_n[\tanh]|\le4E(M).
```

A single coefficient that the machine cannot reproduce forces a state error. The remaining issue is to compare the coefficients allowed by finite action with those required by the thermal target.

### What a finite action permits

The substitution $`z=(w+w^{-1})/2`$ maps the circle $`|w|=1`$ onto the real interval. A larger circle $`|w|=\varrho\gt1`$ maps to an ellipse with foci at $`-1`$ and $`1`$. Its largest imaginary height is $`(\varrho-\varrho^{-1})/2`$.

The function $`g((w+w^{-1})/2)`$ has Laurent coefficient $`a_n[g]/2`$. Cauchy’s coefficient estimate bounds a coefficient by the maximum function size on a circle, divided by the corresponding radius power. Combining this fact with the entire-response bound gives

```math
|a_n[g]|\le
2e^{\mathfrak a(\varrho-\varrho^{-1})}\varrho^{-n}.
```

This inequality holds for every $`\varrho\gt1`$. Moving to a larger ellipse strengthens the geometric factor $`\varrho^{-n}`$, while the permitted growth contributes the competing exponential factor. The action controls that tradeoff.

### What the Gibbs response requires

The target’s closest poles produce a geometric scale. Put

```math
b=\frac\pi2,
\qquad s=\sqrt{1+b^2},
\qquad r=b+s.
```

The ellipse with parameter $`r`$ reaches imaginary height $`b`$, because $`r-r^{-1}=2b`$. In this project, the odd Chebyshev coefficients satisfy the rigorous lower estimate

```math
|a_n[\tanh]|\ge\frac4s r^{-n}
\qquad(n\text{ odd}).
```

The existence of a nearby pole alone would not justify dropping all other pole contributions: cancellation must be excluded. The [canonical coefficient derivation](../science/deadline_bound.md#computing-the-coefficient-signs) establishes an exact sum in which every pole pair contributes the same sign to each odd coefficient. Retaining the closest pair then gives the displayed inequality. Even coefficients vanish because $`\tanh`$ is odd.

Choose $`\varrho=2r`$. Relative to the target scale $`r^{-n}`$, the machine coefficient now has an additional factor $`2^{-n}`$. Taking an odd $`n`$ large enough to dominate $`e^{\mathfrak a(2r-(2r)^{-1})}`$ makes the allowed machine coefficient at most half the required target coefficient. Such an $`n`$ grows linearly with $`\mathfrak a`$. Consequently $`r^{-n}`$ is exponential in the action, and the coefficient-error inequality forces an exponential state-error floor.

The [full comparison and constant certificate](../science/deadline_bound.md#comparing-the-coefficients) specify the integer choice and certify conservative constants. The resulting universal statement is

```math
e(T)\ge\frac3{400}
\exp\!\left[-\frac{12T}{\beta\hbar}\right],
```

where $`e(T)`$ is the infimum of the worst-case trace error over machines finishing by $`T`$. For $`0\lt\varepsilon\lt3/400`$, any successful deadline must therefore satisfy

```math
T_\varepsilon\ge
\frac{\beta\hbar}{12}\log\frac3{400\varepsilon}.
```

Together with the finite-control upper bound, this yields

```math
T_\varepsilon^{\mathrm{opt}}
=\Theta\!\left(\beta\hbar\log\frac1\varepsilon\right)
\qquad(\varepsilon\downarrow0).
```

The symbol $`\Theta`$ means matching upper and lower bounds up to positive constants in this limit, with the declared thermal interval held fixed. It does not identify an optimal exponent or an efficient controller.

## Why exact random stopping can have finite mean time

Leave the exact factory running instead of imposing a cutoff. It outputs the exact thermal bit after an almost-surely finite count $`N`$. In the ideal stopping model, each input coin costs $`t_0=\beta\hbar/4`$, so $`\tau=t_0N`$. Ideal instantaneous operations, protected storage and potentially unbounded histories are permitted.

Exactness describes the terminal marginal after averaging the completed runs and discarding their records. Each individual run may output a pure basis state. Conditioning on early termination can change the mixture, so early completed runs alone need not have the Gibbs distribution.

For a nonnegative integer count, the tail-sum identity is $`\mathbb E[N]=\sum_{n\ge0}\Pr(N\gt n)`$. Each extra input contributes one unit exactly on the runs that reach it. Thus the uniform tail bound implies

```math
\sup_y\mathbb E_y[\tau]
\le\frac{\beta\hbar C}{4(1-e^{-\lambda})}.
```

The mean is finite although no common finite deadline covers every run. The [stopping-time account](../science/stopping_time.md) proves that late runs are necessary for every exact protocol in the specified stopping model.

### Truncation transfers the deadline lower bound to a tail bound

Fix any exposure cap $`T`$. Store outputs already completed, and return a fixed fallback state on unfinished runs. Let $`p_y(T)=\Pr_y(\tau\gt T)`$. The exact eventual state is the sum of the early contribution and the eventual late contribution. The truncated state changes only the latter, whose total probability is $`p_y(T)`$. Since trace distance between normalized states is at most one, the truncation error is at most $`p_y(T)`$.

This truncated machine has a deterministic action cap, so the converse applies. Hence

```math
\sup_y\Pr_y(\tau\gt T)
\ge\frac3{400}e^{-12T/(\beta\hbar)}.
```

The supremum is taken separately at each $`T`$: a parameter with a large late probability can depend on the chosen deadline. This is not a lower bound on the tail at every individual parameter, nor a claim of one parameter that is hardest at all times.

A mean-time lower bound follows from one deadline. For every $`y`$, $`\mathbb E_y[\tau]\ge T\Pr_y(\tau\gt T)`$. Taking the supremum and choosing $`T=\beta\hbar/12`$ gives

```math
\sup_y\mathbb E_y[\tau]\ge\frac{\beta\hbar}{1600e}.
```

Together with the factory upper bound, the optimal worst-case mean is $`\Theta(\beta\hbar)`$. Requiring the probability of missing a common deadline to be at most $`\eta`$ restores a logarithm: the optimal uniform deadline quantile has order $`\beta\hbar\log(1/\eta)`$ as $`\eta\downarrow0`$. The mean-time argument does not interchange a supremum with a tail integral.

## The complete comparison and its scope

| Finishing requirement | Established conclusion and resource |
|---|---|
| A common deadline and positive target error | Optimal logarithmic accuracy cost; the constructive elapsed time includes every finite-duration control pulse. |
| Exact terminal marginal with random stopping | Finite optimal worst-case mean interrogation time in the ideal-instrument model, with unavoidable worst-case late runs. |
| A common deadline exceeded with small probability | A logarithmic cost in inverse tolerated late probability. |

The finite-control construction implements each positive-accuracy cutoff with finite resources. It does not turn the untruncated exact factory into one finite-dimensional, fixed-strength apparatus with the same mean time. Conversely, the lower bound already allows ideal instruments, so the deadline-versus-expectation distinction exists within that ideal model as well.

The interval is fixed in **thermal units**: the physical energies are $`\pm y/\beta`$ for $`y\in[-1,1]`$. Changing $`\beta`$ while preserving this promise changes the laboratory range of possible gaps. The constants asserted here are not a claim about a fixed laboratory gap interval taken to arbitrarily low temperature. Fixed control ceilings, locality, autonomous baths, reusable machinery and work costs would also add constraints beyond the established task. [Physical interpretation](../science/interpretation.md) develops these boundaries and the comparison with earlier thermalization and approximation results.

The conceptual connection is now complete. Quantum mechanics supplies states, measurement probabilities and controlled evolution. Quantum operations make input reset and retained histories precise. A classical analytic coin-simulation theorem supplies the constructive conversion from Ramsey bits to thermal populations. The finite-action analytic response and its Chebyshev coefficients constrain every admissible deadline machine. Truncation then connects an approximation limit at fixed time to the late-run statistics required by exact random stopping.

For a structured route through that story, return to [the 30 milestones](MILESTONES.md). For exact statements, assumptions and proofs, use [the scientific reading route](../science/README.md); for attribution and source boundaries, use [related work](../references/RELATED_WORK.md); for the scope of executable checks, use [verification](../verification/README.md).
