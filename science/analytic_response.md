# The analytic response of a finite-time machine

A machine acquires its dependence on an unknown Hamiltonian through the
time for which that Hamiltonian acts. The [thermalization model](model.md)
allows arbitrary parameter-independent control, yet this dependence obeys a
uniform analytic constraint. This page proves that constraint, including
measurements, feedback, branch-dependent interrogation lengths, and
well-defined limiting protocols. The [deadline bound](deadline_bound.md)
then compares it with the response required by a Gibbs state.

## Signal action

It is useful to prove the response estimate for the joint Hamiltonian

```math
\mathsf H_y(t)=K(t)+yV(t),\qquad
\mathfrak a=\frac1\hbar\int_0^T\|V(t)\|\,dt.
```

Here $`K(t)`$ is parameter independent and $`V(t)`$ is a bounded self-adjoint
signal generator. For the single always-on qubit in the model,

```math
V(t)=\frac{Z_S\otimes I_M}{\beta},
\qquad
\mathfrak a=\frac{T}{\beta\hbar}.
```

In finite dimension, measurable Hermitian $`K(t)`$ and $`V(t)`$ with integrable
norms suffice for a well-defined propagator. Piecewise continuous finite
controls are a simpler sufficient case. There is no upper bound on the
control strength or apparatus dimension shared by all machines.

An infinite-dimensional environment is also covered when the
parameter-independent evolution has a strongly continuous unitary propagator
$`U_0(t,s)`$, and the bounded perturbation has integrable norm and a strongly
measurable interaction-picture form. The Dyson integrals then define the
perturbed propagator. These are well-posedness assumptions; a formal
unbounded Hamiltonian without a specified propagator is not sufficient.

## Entire-response bound

Let $`\rho_0`$ be a fixed parameter-independent initial density operator, and
let $`\mathcal R`$ be the fixed final discard/output channel. Define

```math
g(y)=\operatorname{Tr}[Z\rho_M(y)],
\qquad
\rho_M(y)=\mathcal R\!\left(U_y\rho_0U_y^\dagger\right).
```

The response $`g`$ extends to an entire function of a complex parameter $`z`$,
and it satisfies

```math
\boxed{
|g(x+iv)|\le e^{2\mathfrak a|v|}
\qquad(x,v\in\mathbb R).
}
```

For the thermalization model, this becomes

```math
|g(x+iv)|\le
\exp\!\left(\frac{2T|v|}{\beta\hbar}\right).
```

The bound is independent of control strength and apparatus dimension.

### Analytic continuation of the propagator

Continue the coefficient $`y`$ to $`z\in\mathbb C`$ while keeping time real.
In the interaction picture of $`U_0`$, the Dyson series defines $`U_z(T,0)`$.
Its coefficient of $`z^n`$ has operator norm at most
$`\mathfrak a^n/n!`$, so this continuation is entire in operator norm.

For a real value $`x`$, the propagator $`U_x(t,0)`$ is unitary. Write

```math
W(t)=U_x(t,0)^\dagger U_{x+iv}(t,0).
```

In this interaction picture,

```math
\frac{dW}{dt}
=\frac{v}{\hbar}
U_x(t,0)^\dagger V(t)U_x(t,0)\,W(t).
```

When the parameter-independent Hamiltonian is unbounded, this is understood
as the corresponding bounded interaction-picture integral equation. No
formal differentiation on an unstated common operator domain is required.

The Dyson norm estimate gives

```math
\|W(T)\|
\le\exp\!\left(
\frac{|v|}{\hbar}\int_0^T\|V(t)\|\,dt
\right).
```

Since $`U_x(T,0)`$ is unitary,

```math
\|U_{x+iv}(T,0)\|\le e^{\mathfrak a|v|}.
```

Arbitrarily strong known controls cannot increase the integrated norm of the
unknown perturbation in this estimate.

### Analytic continuation of the output

Write $`U_z=U_z(T,0)`$ and introduce the reflected adjoint

```math
U_z^\sharp:=U_{\bar z}^\dagger.
```

If $`U_z=\sum_{n\ge0}A_nz^n`$, then
$`U_z^\sharp=\sum_{n\ge0}A_n^\dagger z^n`$, so it is analytic.
The expression $`U_z^\dagger`$ would instead be nonanalytic.
Both $`U_z`$ and $`U_z^\sharp`$ obey the preceding norm estimate.

The adjoint of the output channel is unital and positive. Consequently,

```math
B=\mathcal R^\dagger(Z),\qquad
B=B^\dagger,\qquad -I\le B\le I.
```

The analytic scalar response is

```math
g(z)=\operatorname{Tr}\!\left[B\,U_z\rho_0U_z^\sharp\right].
```

Products with a trace-class operator are analytic in trace norm. Moreover,

```math
\begin{aligned}
|g(x+iv)|
&\le \|B\|\,
 \|U_{x+iv}\rho_0U_{x+iv}^\sharp\|_1\\
&\le \|U_{x+iv}\|\,\|\rho_0\|_1\,
       \|U_{x+iv}^\sharp\|\\
&\le e^{2\mathfrak a|v|}.
\end{aligned}
```

No positivity of the analytically continued operator at complex $`z`$ is used.
For real $`y`$, it is the physical output state. For a unitary propagator on
the full dilated space, analytic continuation also gives
$`U_z^\sharp U_z=U_zU_z^\sharp=I`$.

A normalized vector-state representation of an infinite environment gives
the same proof with a vector expectation in place of the trace. A specified
bounded positive state functional also obeys the norm estimate. In each
case the representation must admit the well-posed bounded-perturbation
dynamics above; an infinite thermal environment need not be assigned a
trace-class Gibbs density matrix.

## Instruments and coherent records

The analytic bound also permits ideal instantaneous
parameter-independent instruments. A finite-outcome instrument with Kraus
operators $`M_{r,a}`$ satisfies

```math
\sum_{r,a}M_{r,a}^\dagger M_{r,a}=I.
```

It has the isometric realization

```math
W|\psi\rangle
=\sum_{r,a}M_{r,a}|\psi\rangle
 \otimes|r\rangle_R\otimes|r,a\rangle_E.
```

The record $`R`$ controls later operations. The retained environment $`E`$
keeps distinct measured outcomes orthogonal. Extending the isometry to a
unitary on a larger space and tracing the environments at the end reproduces
the adaptive protocol. Preparation and reset are represented with fresh
ancillas and retained or discarded old registers in the same way.

The policy is parameter independent even when a realized control sequence
depends on a record whose distribution contains information about $`y`$.
In the dilated description, that policy is one fixed controlled operator.

This construction retains complete, unnormalized branches. No conditional
state is divided by its outcome probability inside the analytic proof.
All outcomes contribute to the final state. A state normalized only after
postselection is a different scored object.

## Branch-dependent interrogation lengths

A deterministic cap on cumulative interrogation time must hold on every
history. Summing the largest query duration separately at each nominal
round can exceed the largest total duration of any actual branch. To
preserve the correct resource, align histories by their cumulative signal
action.

Consider a finite decision tree. At node $`v`$, remove the known part of the
query in an interaction picture. If its signal cost is $`a_v`$, the change
of clock

```math
q=\frac1\hbar\int\|V_v(t)\|\,dt
```

writes its signal evolution as a generator $`yG_v(q)`$ with
$`\|G_v(q)\|\le1`$. Intervals on which $`V_v=0`$ contribute only a known
operation. The known endpoint operations have zero charged action in this
ideal representation.

Let $`q_v`$ be the sum of the costs of the ancestors of $`v`$. Once the history
label is fixed, $`q_v`$ is a fixed number determined by the protocol. On a
common clock $`q\in[0,\mathfrak a]`$, run the node on
$`[q_v,q_v+a_v]`$ and apply its instrument at the endpoint.

The histories occupy orthogonal record subspaces. At each clock value the
coherent signal generator is

```math
G(q)=\bigoplus_{\text{active }v}G_v(q-q_v)
       \ \oplus\ 0_{\text{finished}},
\qquad
\|G(q)\|\le1.
```

There are finitely many node endpoints, so all controlled isometries can be
scheduled at those points and extended to known unitaries. This preserves
each real-parameter branch's output and probability. Its total signal
action is at most $`\mathfrak a`$.

The representation may grant more controlled access than a particular
laboratory implementation. This is sufficient for a lower bound: every
original response lies in the bounded-action class. It does not assert a
general physical compiler preserving every adaptive branch-budget deadline.
The [matching finite-control construction](finite_controls.md) uses common
fixed-duration Ramsey slots and does not require such a compiler.

For the elapsed-time model with one always-on signal qubit, the signal
generator already has norm $`1/\beta`$ at every time. A hard wall-clock
deadline directly gives its action bound.

### Preserving outputs while padding

A finished branch can store its output in an isolated,
parameter-independent memory until the common deadline. Subsequent
operations on complementary registers cannot change the stored marginal,
even when it is correlated with those registers. A fixed final output map
selects the stored register. In the diagonal-bit construction, a prepared
$`Z`$ eigenstate can also remain on the signal qubit.

Thus padding is valid for coherent record-conditioned outputs as well.
The separate [stopping-time proof](stopping_time.md) uses this storage
property when it truncates an exact random-duration protocol.

## Well-defined limiting protocols

The response bound is closed under specified physical limits with a common
action cap. Suppose $`g_j`$ are responses of finite admissible protocols,
all satisfying

```math
|g_j(x+iv)|\le e^{2\mathfrak a|v|},
```

and $`g_j(y)`$ converges pointwise on the promised real interval.

The complex bound gives local uniform boundedness. Every subsequence
therefore has a further subsequence converging locally uniformly to an
entire function. Any two such limits agree on the real interval and hence
agree everywhere by the identity theorem. The whole sequence consequently
converges locally uniformly to a unique entire extension, which still
obeys the same bound.

This includes nonexplosive adaptive protocols whose finite-history
truncations converge to the output. Pointwise convergence for each $`y`$
suffices; a uniform convergence rate is unnecessary. Continuous-outcome
instruments are covered whenever they have the bounded-action dilation or
arise as such limits. An undefined infinite sequence of ideal operations
is not assigned an additional terminal capability.

The resulting entire-response constraint is the sole dynamical input to
the [uniform deadline theorem](deadline_bound.md).

