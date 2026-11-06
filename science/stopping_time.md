# Exact thermalization at a random stopping time

A common deadline and an outcome-dependent stopping time impose different
requirements. In the [ideal stopping model](model.md), a machine may use an
unbounded number of interrogations, provided that it terminates almost
surely and its unconditional terminal marginal is exactly $`\gamma_y`$ for
every promised $`y`$.

The [thermal-coin construction](thermal_coin.md) achieves this with
worst-case mean interrogation time of order $`\beta\hbar`$. Nevertheless,
the [deterministic deadline bound](deadline_bound.md) forces rare late runs.
This page proves the necessary tail bound, its quantile consequence, and
the matching order of the worst-case mean.

## The stopping model

Let $`\tau`$ be the accumulated interrogation time of an exact protocol.
Stopping is a classical recorded event with a well-defined quantum
instrument on completed histories. The protocol is interruptible at every
deterministic signal-time cap, and its bounded prefixes belong to the
[bounded-action class](analytic_response.md).

Parameter-independent instruments, reset, computation, and protected
memory are ideal and instantaneous in this model. Potentially unbounded
total memory and fresh ancillas are allowed across the unbounded set of
histories. These assumptions do not assert an exact finite-strength,
finite-dimensional autonomous implementation.

Exactness means

```math
\rho_{\mathrm{terminal}}(y)=\gamma_y
\qquad\text{for every }y\in[-1,1],
```

after averaging the terminating histories and discarding the controller's
records. It does not require the state conditioned on each history to be
Gibbs. A protocol that emits a basis-state bit on each run can have an exact
thermal marginal.

## Truncating an exact protocol

Fix a deterministic deadline $`T`$. Decompose the eventual terminal state
according to whether the protocol had completed by that deadline:

```math
\gamma_y=\sigma_y^{\le T}+\sigma_y^{\gt T},
\qquad
p_y(T):=\mathrm{Tr}\,\sigma_y^{\gt T}
       =\Pr_y(\tau\gt T).
```

Both $`\sigma_y^{\le T}`$ and $`\sigma_y^{\gt T}`$ are positive subnormalized
operators. The second is the eventual output contributed by histories
unfinished at $`T`$; it is not necessarily the live system state at $`T`$.

Store every early output in a protected, parameter-independent memory and
leave it untouched until $`T`$. This preserves its marginal even if the
output has coherence or is correlated with other registers. At $`T`$,
return a stored output on completed histories and prepare a fixed state
$`\omega_*`$ on unfinished histories.

The resulting unconditional state is

```math
\rho_y^{(T)}
=\sigma_y^{\le T}+p_y(T)\omega_*.
```

For $`p_y(T)\gt0`$,

```math
\begin{aligned}
D(\rho_y^{(T)},\gamma_y)
&=p_y(T)
D\!\left(\omega_*,
\frac{\sigma_y^{\gt T}}{p_y(T)}\right)\\
&\le p_y(T).
\end{aligned}
```

The conclusion is immediate when $`p_y(T)=0`$. In particular, this truncation
argument does not assume that conditioning on early completion preserves
the Gibbs distribution.

The truncated protocol has action at most $`T/(\beta\hbar)`$, and every
outcome is retained. The universal deadline inequality applies to it.
Combining that inequality with the last estimate proves

```math
\boxed{
\sup_{y\in[-1,1]}\Pr_y(\tau\gt T)
\ge\frac3{400}e^{-12T/(\beta\hbar)}
\qquad(T\ge0).
}
```

## The quantifier in the tail bound

The statement holds for every exact protocol and every chosen deadline.
The supremum over $`y`$ is taken separately at each deadline. A maximizing
or nearly maximizing parameter may change with $`T`$.

Thus the result excludes a uniform superexponential stopping tail over the
promised family. It does not establish a tail lower bound for every fixed
parameter, or identify one parameter that is hardest at all deadlines.
A coherent superposition of runtimes without a specified classical
stopping instrument is not assigned a stopping-time distribution by this
argument.

## Deadline quantiles

For one exact protocol, define its uniform deadline quantile by

```math
Q_\eta
=\inf\left\{T\ge0:
\sup_y\Pr_y(\tau\gt T)\le\eta\right\}.
```

For $`0\lt\eta\lt3/400`$, the tail lower bound gives

```math
Q_\eta\ge
\frac{\beta\hbar}{12}\log\frac3{400\eta}.
```

There is also an exact protocol with a uniform exponential upper tail.
The Ramsey [thermal-coin construction](thermal_coin.md) uses the analytic
Bernoulli-factory theorem of
[Nacu and Peres](https://arxiv.org/pdf/math/0309222).
Their Theorem 2 gives exact simulation for an analytic bias map, and
Proposition 21 makes its exponential input-count tail uniform on the
closed bias interval.

Let $`N`$ be the number of input coins used by this exact factory.
The thermal-coin construction supplies constants $`C\ge1`$ and
$`\lambda\gt0`$, independent of $`\beta`$ and $`y`$, such that

```math
\Pr_y(N\gt n)\le Ce^{-\lambda n},
\qquad n=0,1,\ldots.
```

Each Ramsey input coin costs $`\beta\hbar/4`$, so
$`\tau=(\beta\hbar/4)N`$. Since $`N`$ is integer valued, for every $`T\ge0`$,

```math
\begin{aligned}
\sup_y\Pr_y(\tau\gt T)
&=\sup_y\Pr_y\!\left(
N\gt\left\lfloor\frac{4T}{\beta\hbar}\right\rfloor
\right)\\
&\le C\exp\!\left[
-\lambda\left\lfloor\frac{4T}{\beta\hbar}\right\rfloor
\right]\\
&\le Ce^\lambda
\exp\!\left[-\frac{4\lambda T}{\beta\hbar}\right].
\end{aligned}
```

Thus the uniform exponential upper tail has constants
$`C'=Ce^\lambda`$ and $`c'=4\lambda`$.

Together, the lower and upper show that the optimal uniform deadline
exceeded with probability at most $`\eta`$ has order

```math
Q_\eta^{\mathrm{opt}}
=\Theta\!\left(\beta\hbar\log\frac1\eta\right)
\qquad(\eta\downarrow0).
```

## Worst-case mean time

A lower bound on the worst-case mean follows from one deadline, without
interchanging a supremum and an integral. For every fixed $`T`$,

```math
\begin{aligned}
\sup_y\mathbb E_y[\tau]
&\ge T\sup_y\Pr_y(\tau\gt T)\\
&\ge\frac3{400}T e^{-12T/(\beta\hbar)}.
\end{aligned}
```

Choose $`T=\beta\hbar/12`$. Then

```math
\boxed{
\sup_y\mathbb E_y[\tau]
\ge\frac{\beta\hbar}{1600e}.
}
```

For the exact factory, the tail-sum identity for the nonnegative integer
$`N`$ gives, for every $`y`$,

```math
\begin{aligned}
\mathbb E_y[\tau]
&=\frac{\beta\hbar}{4}
\sum_{n=0}^\infty\Pr_y(N\gt n)\\
&\le\frac{\beta\hbar C}{4}
\sum_{n=0}^\infty e^{-\lambda n}\\
&=\frac{\beta\hbar C}{4(1-e^{-\lambda})}.
\end{aligned}
```

This upper bound is uniform in $`y`$. Combining it with the preceding
worst-case lower bound yields

```math
\inf_{M\,\mathrm{exact}}\sup_y\mathbb E_y[\tau_M]
=\Theta(\beta\hbar).
```

The deterministic logarithmic precision cost therefore does not become a
logarithmic expected-time lower bound. Almost-sure exactness, a finite
mean, and an unavoidable exponential worst-case stopping tail are
compatible.

## Relation to finite controls

The [finite-control construction](finite_controls.md) implements every
fixed-accuracy finite prefix with finite control durations and strengths,
including their elapsed time. That statement establishes the matching
deterministic order.

The exact untruncated construction remains a claim in the ideal stopping
model specified above. Taking a limit of increasingly accurate finite
prefixes does not by itself produce an exact finite-strength apparatus
with the same mean time. See the [model](model.md) and
[interpretation](interpretation.md) for the resource distinctions.

