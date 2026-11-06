# Finite controls with the unknown drift always on

The [Ramsey-coin construction](thermal_coin.md) gives a finite ideal circuit
for each positive accuracy. This page implements that circuit with a finite
apparatus and finite-duration, finite-strength controls. The unknown
Hamiltonian remains present during every pulse, and all of that time is
charged according to the [model](model.md).

Let

```math
H_y=\frac{y}{\beta}Z_S,\qquad y\in[-1,1],\qquad
t_0=\frac{\beta\hbar}{4},\qquad
n_\varepsilon=
\left\lceil\frac{\log(2C/\varepsilon)}{\lambda}\right\rceil.
```

The constants $`C\ge1`$ and $`\lambda\gt0`$ are those of the
[Nacu–Peres analytic coin simulation](../references/RELATED_WORK.md#nacu-peres-analytic-coin-simulation).
The ideal circuit at this cutoff replaces any incoming state by
$`\gamma_{n_\varepsilon,y}`$ and satisfies

```math
\sup_y\frac12
\|\mathcal R_{\gamma_{n_\varepsilon,y}}-\mathcal G_y\|_\diamond
\le\frac{\varepsilon}{2}.
```

We will implement a channel $`\Phi_y`$ with

```math
\sup_y\frac12\|\Phi_y-\mathcal G_y\|_\diamond\le\varepsilon
```

within the common deterministic time

```math
T_\varepsilon\le\beta\hbar\left[
\frac14\left\lceil\frac{\log(2C/\varepsilon)}{\lambda}\right\rceil
+\frac{\varepsilon}{2}\right].
```

The apparatus and each pulse are finite at a fixed accuracy. Their size and
strength are allowed to grow as $`\varepsilon`$ decreases.

## One common schedule

For a fixed cutoff $`n`$, define the Boolean function
$`a_n:\{0,1\}^n\to\{0,1\}`$ by the simulator's first decision, or by
zero if it has not decided after the full word. In the
[finite-word representation](thermal_coin.md#finite-words-specify-every-decision),
$`a_n(s)=\mathbf1_{\mathcal A_n}(s)`$. Each of the $`2^n`$ words has a
prescribed binary label. This is a finite classical table and has a finite
reversible implementation. No evaluation of an unknown parameter is part
of the table lookup.

An explicit ideal circuit uses the sensor $`S`$, fresh probe qubits
$`Q_1,\ldots,Q_n`$ initially in $`|+\rangle`$, and an output qubit $`O`$
initially in $`|0\rangle`$:

1. For each $`j=1,\ldots,n`$, swap $`Q_j`$ into $`S`$, evolve $`S`$
   under $`H_y`$ for exactly $`t_0`$, and swap it back. The probe acquires
   $`U_y|+\rangle`$, where $`U_y=e^{-iyZ/4}`$. The original sensor input
   is parked off the sensor during the exposure and restored afterward.
2. Apply a known change of measurement basis to each probe. For example,
   with the Hadamard gate $`H_{\mathrm{Had}}`$ and phase gate
   $`S_{\mathrm{ph}}=\mathrm{diag}(1,i)`$, take
   $`V=XH_{\mathrm{Had}}S_{\mathrm{ph}}^\dagger`$. This maps the
   $`+Y`$ state to computational bit one and the $`-Y`$ state to bit zero.
3. Apply the known reversible operation
   $`|s\rangle|b\rangle_O\mapsto|s\rangle|b\mathbin{\oplus}[1-a_n(s)]\rangle_O`$.
   Since $`O`$ starts in zero, it stores $`1-a_n(s)`$. Retain the complete
   word register.
4. Swap $`O`$ into $`S`$ and trace all remaining machine registers.

All $`n`$ signal slots run even if a prefix would already have terminated
the simulator. Every branch therefore has the same interrogation duration
$`nt_0`$. The construction uses the single native unknown Hamiltonian on
$`S`$; it supplies no extra parallel copies or controlled unknown evolution.

### Why coherent records give the same channel

After the first two steps the probes have the product state
$`(VU_y|+\rangle)^{\otimes n}`$. After the reversible table operation,
the probe and output state is

```math
|\Psi_y\rangle_{QO}
=\sum_{s\in\{0,1\}^n}c_s(y)
|s\rangle_Q|1-a_n(s)\rangle_O,
\qquad
|c_s(y)|^2=p(y)^{|s|}[1-p(y)]^{n-|s|}.
```

Here $`|s|`$ counts the ones. The orthogonal word register makes all
cross terms vanish when it is traced. The output populations are exactly
those of the classical truncated simulator, so the output state is
$`\gamma_{n,y}`$.

Before the final swap, this state on $`QO`$ is independent of the arbitrary
original input $`\rho_{SR}`$. The final swap places that original sensor
state in a discarded machine register. Consequently the retained joint
output is exactly

```math
\gamma_{n,y}\otimes\rho_R.
```

This proves the ideal replacement-channel property for entangled inputs as
well as uncorrelated inputs. No intermediate measurement is necessary.
The choice of discard maps is independent of $`y`$, although the states in
the discarded records depend on it.

Probe preparation can also be included among the known gates, starting from
standard $`|0\rangle`$ ancillas. It only adds finitely many known operations.
The machine's fresh registers and discarded registers provide the state
preparation and entropy sink permitted in the model.

## Implementing each known gate in positive time

List the finitely many known ideal gates as $`W_1,\ldots,W_m`$. Each has a
Hermitian logarithm $`A_j`$ with

```math
W_j=e^{-iA_j},\qquad \|A_j\|\le\pi.
```

Choose any positive pulse duration $`\delta_j`$ and apply the
parameter-independent control

```math
K_j=\frac{\hbar A_j}{\delta_j}.
```

This is a finite-norm control for every fixed $`\delta_j\gt0`$. The actual
Hamiltonian during the pulse is

```math
H_y\otimes I_M+K_j.
```

Let $`V_j(t)`$ be the control-only propagator and $`U_{j,y}(t)`$ the
actual propagator. For the relative propagator
$`R_{j,y}(t)=V_j(t)^\dagger U_{j,y}(t)`$,

```math
\frac{dR_{j,y}}{dt}
=-\frac{i}{\hbar}
V_j(t)^\dagger(H_y\otimes I_M)V_j(t)R_{j,y}(t).
```

Its generator has norm at most $`1/\beta`$, uniformly in $`y`$. Integrating
this equation, or equivalently using Duhamel's formula, gives

```math
\|U_{j,y}(\delta_j)-W_j\|
\le\frac{\delta_j}{\beta\hbar}.
```

For two unitary channels, half their diamond distance is at most the
operator-norm distance between their unitaries. This follows by adding and
subtracting one cross term in the difference of the output density
operators, including an arbitrary reference. Thus the pulse error obeys

```math
\frac12\|\mathcal U_{j,y}-\mathcal W_j\|_\diamond
\le\frac{\delta_j}{\beta\hbar}.
```

The estimate does not depend on a commutation relation, the control norm,
or the apparatus dimension. The unknown Hamiltonian is physically present
throughout. The control-only propagator is only a reference used to bound
the error.

## Total error and elapsed time

Define the total control duration by

```math
\delta_{\mathrm{ctrl}}=\sum_{j=1}^m\delta_j.
```

The ideal and actual circuits use the same $`n`$ free evolutions of duration
$`t_0`$. Telescoping their difference across the known gates, and using
contractivity under composition and final partial traces, gives

```math
\sup_y\frac12
\|\Phi_y-\mathcal R_{\gamma_{n,y}}\|_\diamond
\le\frac{\delta_{\mathrm{ctrl}}}{\beta\hbar}.
```

This includes any correlations introduced by the drift during the pulses;
it does not assume that the imperfect physical coin experiments remain
independent.

Set $`n=n_\varepsilon`$ and choose

```math
\delta_{\mathrm{ctrl}}=\frac{\varepsilon\beta\hbar}{2}.
```

The ideal truncation error and the pulse error are each at most
$`\varepsilon/2`$. The triangle inequality proves the required channel
accuracy. Every operation occupies its scheduled finite interval, so the
elapsed time is

```math
T=n_\varepsilon t_0+\delta_{\mathrm{ctrl}}
=\beta\hbar\left[
\frac14\left\lceil\frac{\log(2C/\varepsilon)}{\lambda}\right\rceil
+\frac{\varepsilon}{2}\right].
```

Preparation, swaps, the reversible decision table and the final output
transfer are all included in the pulse durations. There is no additional
online classical-processing interval: the finite table is compiled into
the known circuit. A finite implementation with one- and two-qubit gates
can replace a larger known unitary, with the same total time allocated
across its finite number of gates.

For example, if the $`m`$ pulses have equal durations, the logarithm
construction has

```math
\|K_j\|\le\frac{2\pi m}{\varepsilon\beta}.
```

This is finite at fixed accuracy. The proof relies on the model's freedom
to increase control strength and apparatus size as accuracy improves.

## Finite descriptions and timing precision

At finite cutoff, the controller needs only the finite binary table
$`a_n`$. The analytic expression for $`F`$ determines the coin-simulation
problem and its design; it is not evaluated on an unknown parameter during
the experiment. The existence bound places no efficiency requirement on
constructing, storing or compiling the table.

Known gate descriptions and timings can also be approximated to finite
precision while preserving the same time bound. Keep $`n_\varepsilon`$
and choose the nominal total control duration

```math
\delta_{\mathrm{ctrl}}^{\mathrm{nom}}
=\frac{\varepsilon\beta\hbar}{4}.
```

Impose two simultaneous accuracy requirements:

1. The sum of the absolute errors in all pulse and Ramsey-slot durations
   is at most $`\varepsilon\beta\hbar/4`$.
2. Relative to the nominal finite-control circuit, the combined effect of
   gate-description and timing errors has half-diamond norm at most
   $`\varepsilon/4`$, uniformly in $`y`$.

Both requirements are attainable at finite precision because the circuit
is finite and each nominal control has finite norm. More explicitly, for
a constant pulse with nominal control $`K_j`$ and duration $`\delta_j`$,
and approximations $`\widetilde K_j`$ and $`\widetilde\delta_j`$,
Duhamel's formula bounds its unitary error by

```math
\frac{\delta_j}{\hbar}\|\widetilde K_j-K_j\|
+\frac{|\widetilde\delta_j-\delta_j|}{\hbar}
\left(\|\widetilde K_j\|+\frac1\beta\right).
```

For a Ramsey slot this reduces to its absolute timing error divided by
$`\beta\hbar`$. Finitely fine approximations make the sum of these errors
as small as required, uniformly on the parameter interval. Pulse-timing
accuracy accounts for the known control strength as well as the drift.

The resulting total channel error is at most

```math
\frac{\varepsilon}{2}
+\frac{\varepsilon}{4}
+\frac{\varepsilon}{4}
=\varepsilon,
```

from truncation, nominal drift during controls, and finite-precision
perturbations. The reserved timing allowance ensures that actual elapsed
time is at most

```math
n_\varepsilon t_0
+\frac{\varepsilon\beta\hbar}{4}
+\frac{\varepsilon\beta\hbar}{4},
```

which is the same stated deadline.

## Scope of the construction

For each positive accuracy, this gives a finite collection of registers and
a finite externally specified pulse sequence. The [deadline lower bound](deadline_bound.md)
and this construction therefore have the same order even when all control
time is included. The result does not impose a fixed strength ceiling,
bandwidth, locality, autonomous operation, or a work-cost bound; those
would define additional constraints.

The [exact random-stopping construction](stopping_time.md) is a separate
statement in the ideal-instrument model. Its potentially unbounded memory
and stopping count are not converted here into a single finite apparatus
with exact output. The finite positive-accuracy construction uses only the
finite cutoff table and the controls proved above.
