# Gibbs preparation from Ramsey coins

A short Ramsey experiment converts the unknown energy splitting into a coin
bias. An analytic coin-simulation theorem then converts those coins into the
Gibbs populations. Truncating the simulation gives an unconditional output
with exponentially small error in the number of interrogations.

We use the [known-axis model](model.md),

```math
H_y=\frac{y}{\beta}Z,\qquad y\in[-1,1],\qquad \beta\gt0,
```

and the target population

```math
q(y)=\langle0|\gamma_y|0\rangle=\frac{1}{1+e^{2y}}.
```

All preparations, measurements and decision rules are independent of the
unknown parameter. The only dependence on $`y`$ enters through evolution
under $`H_y`$. The [finite-control construction](finite_controls.md) implements
the resulting finite circuit while counting every control pulse in the
elapsed time. Together with the [deadline lower bound](deadline_bound.md),
it establishes the logarithmic accuracy cost in the model.

## The Ramsey coin

Choose the interrogation duration

```math
t_0=\frac{\beta\hbar}{4},\qquad
U_y=e^{-iH_yt_0/\hbar}=e^{-iyZ/4}.
```

Prepare $`|+\rangle=(|0\rangle+|1\rangle)/\sqrt2`$, evolve for
$`t_0`$, and measure $`Y`$. The evolved Bloch vector has $`Y`$ component
$`\sin(y/2)`$, so the probability of the $`+Y`$ outcome is

```math
p(y)=\frac{1+\sin(y/2)}2.
```

Fresh preparations give independent copies of this coin for each fixed
unknown $`y`$. No estimate of the parameter is needed. Its possible biases
form the fixed compact interval

```math
I=\left[\frac{1-\sin(1/2)}2,\frac{1+\sin(1/2)}2\right]
\subset(0,1).
```

Define the known function

```math
F(p)=\frac{1}{1+\exp\!\left[4\arcsin(2p-1)\right]}.
```

On this interval the principal arcsine satisfies
$`\arcsin(2p(y)-1)=y/2`$. Therefore

```math
F(p(y))=\frac{1}{1+e^{2y}}=q(y).
```

The function $`F`$ is real analytic on a neighborhood of $`I`$. Its values
lie in

```math
F(I)=\left[\frac{1}{1+e^2},\frac{1}{1+e^{-2}}\right]\subset(0,1).
```

Thus both the input interval and output probabilities stay away from the
endpoints. The interval and function are dimensionless and independent of
$`\beta`$.

## The analytic coin-simulation theorem

[Nacu and Peres, Theorem 2](../references/RELATED_WORK.md#nacu-peres-analytic-coin-simulation)
prove that a real-analytic function from a closed interval inside $`(0,1)`$
to $`(0,1)`$ admits exact coin simulation with exponentially decaying input
counts. Their Proposition 21 makes the tail constants uniform on the closed
interval. Applied to $`F`$, one fixed simulator has output
$`B\in\{0,1\}`$ and stopping count $`N`$ satisfying

```math
\Pr_p(B=1)=F(p),\qquad
\sup_{p\in I}\Pr_p(N\gt n)\le C e^{-\lambda n}
\quad(n=0,1,2,\ldots),
```

for constants $`C\ge1`$ and $`\lambda\gt0`$. These constants depend only
on the fixed function and interval, hence are independent of $`\beta`$ and
the desired accuracy. This theorem supplies the exact simulator and its
uniform exponential tail.

### Finite words specify every decision

The simulation uses the observed coin word, without knowing its bias.
Nacu–Peres Proposition 3 gives a finite-word representation of such rules.
It can be described as follows. Let $`\mathcal A_n\subseteq\mathcal B_n`$
be subsets of $`\{0,1\}^n`$. For an observed word $`s`$ of length $`n`$:

- Output one if $`s\in\mathcal A_n`$.
- Output zero if $`s\notin\mathcal B_n`$.
- Continue if $`s\in\mathcal B_n\setminus\mathcal A_n`$.

Write $`\mathrm{Ext}(A)`$ for the set of one-bit extensions of words
in $`A`$. Consistency of already made decisions is expressed by

```math
\mathrm{Ext}(\mathcal A_n)
\subseteq\mathcal A_{n+1}
\subseteq\mathcal B_{n+1}
\subseteq\mathrm{Ext}(\mathcal B_n).
```

Thus decisions, once made, are preserved under extension. For $`s\in\{0,1\}^n`$, let $`|s|`$ denote its number of ones.
The probabilities of the two sets are finite polynomials,

```math
g_n(p)=\sum_{s\in\mathcal A_n}p^{|s|}(1-p)^{n-|s|},\qquad
h_n(p)=\sum_{s\in\mathcal B_n}p^{|s|}(1-p)^{n-|s|}.
```

Exact termination and the tail bound give

```math
g_n(p)\uparrow F(p),\qquad h_n(p)\downarrow F(p),\qquad
h_n(p)-g_n(p)=\Pr_p(N\gt n)\le C e^{-\lambda n}.
```

For any fixed cutoff, the decision is therefore a finite table of binary
labels. All labels are specified by the chosen simulator and are independent
of $`y`$. No additional coin with an unknown, freely supplied bias is part of
the construction.

## Truncation retains every timeout branch

Fix a cutoff $`n`$. Couple the exact and truncated simulators using the same
infinite sequence of Ramsey outcomes. If the simulator has stopped by
$`n`$, keep its output. Otherwise output the fixed fallback zero. Denote this
bit by $`B_n`$ and let $`q_n(y)=\Pr_y(B_n=1)`$. The two outputs can differ
only on the event $`N\gt n`$, so

```math
|q_n(y)-q(y)|
=|\Pr_y(B_n=1)-\Pr_y(B=1)|
\le\Pr_y(N\gt n)
\le C e^{-\lambda n}.
```

In the finite-word description this simply means
$`B_n=\mathbf1_{\mathcal A_n}(s)`$ and $`q_n(y)=g_n(p(y))`$.
Prepare $`|0\rangle`$ for output one and $`|1\rangle`$ for output zero.
The unconditional state is

```math
\gamma_{n,y}
=q_n(y)|0\rangle\langle0|
+[1-q_n(y)]|1\rangle\langle1|.
```

Because both states are diagonal in the same basis,

```math
D(\gamma_{n,y},\gamma_y)
=\frac12\|\gamma_{n,y}-\gamma_y\|_1
=|q_n(y)-q(y)|\le C e^{-\lambda n}.
```

Timeouts contribute their ordinary probabilities to this state. There is no
normalization by a success probability. The Gibbs claim concerns the output
after the branch record is discarded; conditioning on a stopping count or a
particular history can give different statistics.

## Replacement of an arbitrary input

The incoming state can be swapped into a machine register and discarded.
Since the coin generation uses fresh probes, the ideal truncated channel is

```math
\mathcal R_{\gamma_{n,y}}(X)=\mathrm{Tr}(X)\gamma_{n,y}.
```

For an arbitrary input $`\rho_{SR}`$ entangled with an untouched reference,
its output is exactly $`\gamma_{n,y}\otimes\rho_R`$. The difference between
two replacement channels has diamond norm equal to the trace norm of their
replacement states. Indeed, its action on a joint input is the state
difference tensored with the reference marginal; the trace channel has
completely bounded trace norm one. Consequently,

```math
\frac12\|\mathcal R_{\gamma_{n,y}}-\mathcal G_y\|_\diamond
=D(\gamma_{n,y},\gamma_y)
\le C e^{-\lambda n}.
```

The [finite unitary realization](finite_controls.md#one-common-schedule)
implements this replacement and the complete decision table while retaining
the word register until the final trace.

## Number of interrogations

For $`0\lt\varepsilon\lt1/2`$, choose

```math
n_\varepsilon=
\left\lceil\frac{\log(2C/\varepsilon)}{\lambda}\right\rceil.
```

The ideal truncated channel then has error at most $`\varepsilon/2`$ in
half the diamond norm. It uses $`n_\varepsilon`$ Ramsey exposures, with
ideal interrogation time $`n_\varepsilon\beta\hbar/4`$. Running all these
slots on every branch gives a common schedule. The remaining accuracy
allowance permits [finite-duration control pulses](finite_controls.md),
with the full elapsed-time bound

```math
T_\varepsilon\le\beta\hbar\left[
\frac14\left\lceil\frac{\log(2C/\varepsilon)}{\lambda}\right\rceil
+\frac{\varepsilon}{2}\right].
```

The analytic theorem supplies finite constants; their numerical values and
a practical gate table are not needed for this matching-order existence
bound. Controller size, table construction and gate count remain
unrestricted as specified in the [model](model.md).

## Exact output with random stopping

In the ideal-instrument model, omitting the cutoff gives exact Gibbs output
at $`\tau=t_0N`$, almost surely, with uniform exponential tails and uniform
expected interrogation time $`O(\beta\hbar)`$. These properties follow from
the same attributed Nacu–Peres simulator. The [stopping-time analysis](stopping_time.md)
gives the expectation and tail bounds, as well as their matching lower
bounds. This exact construction permits unbounded stopping counts and
potentially unbounded memory; the finite-control result above concerns each
fixed positive accuracy.

For the primary theorem and its finite-word construction, see Nacu and Peres,
[Fast simulation of new coins from old](https://doi.org/10.1214/105051604000000549),
*The Annals of Applied Probability* **15**(1A), 93–115 (2005),
[author manuscript](https://arxiv.org/pdf/math/0309222).
