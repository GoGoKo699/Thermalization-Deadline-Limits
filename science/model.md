# The thermalization task

Thermal statistics depend on a Hamiltonian. If that Hamiltonian is already
known, a controller can prepare its Gibbs state using a programmed source.
The question here is how quickly a single machine can prepare the right
statistics when the Hamiltonian is known only to belong to a continuous
family. The machine can discover the unknown parameter through dynamics.

The [Planckian thermalization framework](../references/RELATED_WORK.md#planckian-thermalization)
formalizes this distinction and gives a lower timescale proportional to inverse
temperature. The present question resolves the additional cost of accuracy
when one common finishing deadline must work for an interval of Hamiltonians.

## Hamiltonian and target

Let $`S`$ be one qubit, with known Pauli axis $`Z`$. The inverse temperature
$`\beta\gt0`$ is known, and the unknown parameter $`y`$ lies in $`[-1,1]`$.
The only unknown microscopic Hamiltonian is

```math
H_y=\frac{y}{\beta}Z.
```

The two energy eigenvalues are $`\pm y/\beta`$. The eigenvectors are known,
but their energy ordering changes when $`y`$ changes sign. We use the fixed
computational labels $`Z|0\rangle=|0\rangle`$ and
$`Z|1\rangle=-|1\rangle`$ throughout.

The target state and its $`Z=+1`$ population are

```math
\gamma_y=\frac{e^{-\beta H_y}}{\operatorname{Tr}e^{-\beta H_y}}
=\frac{I-\tanh(y)Z}{2},
\qquad
q(y)=\langle0|\gamma_y|0\rangle=\frac{1}{1+e^{2y}}.
```

This is a fixed interval in thermal units: the largest energy splitting is
$`2/\beta`$. All constants below are uniform in $`\beta`$ for this specified
family. Changing temperature while fixing a laboratory gap interval is a
different joint limit.

## A machine with a deterministic deadline

The system and apparatus evolve under

```math
\mathsf H_y(t)=H_y\otimes I_M+K(t),
```

where the initial apparatus state and the control Hamiltonian $`K(t)`$ are
independent of $`y`$. They may depend on the known temperature, the promised
interval and the requested accuracy. We assume a well-defined unitary
propagator. A finite apparatus with piecewise continuous finite-norm controls
is sufficient for every upper bound. The lower bound also permits larger
apparatuses and unbounded apparatus Hamiltonians whenever the interaction
picture is well posed and the unknown perturbation remains bounded.

There is no uniform restriction on apparatus size, control strength or the
number of known control operations. An apparatus can contain an entropy sink,
store measurement histories and discard registers. Its initial state contains
no information about the actual value of $`y`$.

**All elapsed time is charged while the unknown Hamiltonian acts**, including
time used for control pulses. One unknown-Hamiltonian qubit is present. A
generalization with several simultaneous copies must charge their summed
signal action; free parallel replicas would change the resource.

At the common deadline $`T`$, the machine is discarded and the retained system
state is scored. Every branch contributes to that state. A controller can
choose later operations from an observed record, provided that the rule
mapping records to operations is fixed independently of $`y`$. Such feedback
is included through the [coherent record construction](analytic_response.md).

The lower proof also allows ideal instantaneous parameter-independent
instruments. This enlarges the admissible class. The
[finite-control construction](finite_controls.md) supplies a matching upper
in the continuously driven model above, where every pulse has finite duration
and finite strength for each fixed accuracy.

## Accuracy and input states

We use half the trace norm as trace distance:

```math
D(\rho,\sigma)=\frac12\|\rho-\sigma\|_1.
```

For a fixed parameter-independent initial system state, define the error of a
machine by

```math
E(M)=\sup_{y\in[-1,1]}D\bigl(\rho_M(y),\gamma_y\bigr),
\qquad
e(T)=\inf_{M:\,\text{deadline}\le T}E(M).
```

The lower bound holds for every such fixed input, even a favorable pure input.
The matching construction satisfies the stronger requirement of replacing
**any** incoming state. Write

```math
\mathcal G_y(X)=\operatorname{Tr}(X)\gamma_y.
```

The constructed channel $`\Phi_y`$ obeys

```math
\sup_y\frac12\|\Phi_y-\mathcal G_y\|_\diamond\le\varepsilon.
```

Consequently it also works on an input entangled with an untouched reference:
its output is within $`\varepsilon`$ of
$`\gamma_y\otimes\rho_R`$. The reset discards the incoming system state;
the error criterion does not require returning the apparatus or its record
uncorrelated with the output.

## Deterministic deadline theorem

For every $`T\ge0`$,

```math
e(T)\ge\frac{3}{400}
\exp\!\left[-\frac{12T}{\beta\hbar}\right].
```

The constants are conservative. The [proof](deadline_bound.md) gives an exact
closed expression for a slightly stronger pair of constants. In particular,
no finite deterministic deadline gives exact Gibbs preparation on the whole
interval.

Conversely, there are constants $`C\ge1`$ and $`\lambda\gt0`$, independent
of $`\beta`$ and $`\varepsilon`$, such that for every
$`0\lt\varepsilon\lt1/2`$ a finite continuously controlled machine achieves
the stronger channel error above within

```math
T_\varepsilon\le\beta\hbar\left[
\frac14\left\lceil\frac{\log(2C/\varepsilon)}{\lambda}\right\rceil
+\frac{\varepsilon}{2}\right].
```

The constants in this upper bound come from the attributed analytic
coin-simulation theorem. Their numerical values are not needed for the
matching-order statement. Combining both directions gives

```math
T_\varepsilon^{\mathrm{opt}}
=\Theta\!\left(\beta\hbar\log\frac1\varepsilon\right)
\qquad(\varepsilon\downarrow0).
```

This order holds both for preparation from a fixed input and for the stronger
replacement-channel task.

## Exact output at a random time

A second model allows ideal instantaneous instruments and an outcome-dependent
number of interrogations. The terminal system marginal must be exactly
$`\gamma_y`$, after averaging all runs that terminate almost surely. No
finite common deadline is imposed. The resource $`\tau`$ is the accumulated
interrogation time; potentially unbounded memory and discarded records are
allowed.

A stopping protocol has a recorded classical stopping event and can be
interrupted at every deterministic exposure cap. Its bounded prefixes must
belong to the admissible class in the [analytic-response proof](analytic_response.md),
and completed outputs can be stored in protected memory. These conditions
are part of the exact-stopping model below.

In this model exact preparation is possible, and

```math
\inf_{M\,\mathrm{exact}}\sup_y\mathbb E_y[\tau_M]
=\Theta(\beta\hbar).
```

Every exact machine satisfies the necessary tail bound

```math
\sup_y\Pr_y(\tau_M\gt T)
\ge\frac{3}{400}e^{-12T/(\beta\hbar)}.
```

One exact construction has a uniform exponential upper tail as well. Thus
the optimal deadline that is exceeded with probability at most $`\eta`$
has order $`\beta\hbar\log(1/\eta)`$. The supremum over $`y`$ is taken
separately at each deadline; these statements do not identify one parameter
that is hardest at every time. See [stopping times](stopping_time.md).

## What the resource model permits

The results concern information obtained through a bounded unknown
Hamiltonian. Construction cost, gate count, memory, control precision,
bandwidth and thermodynamic work are unrestricted. The finite-accuracy
construction uses finite resources at each accuracy, with strengths that may
grow as accuracy improves. The exact random-time construction uses the ideal
instrument model. A local, autonomous or fixed-strength thermal bath would
be a further physical constraint requiring its own analysis.

The [interpretation](interpretation.md) explains how these choices distinguish
the result from known-Hamiltonian state preparation, pairwise Planckian
saturation, phase estimation and Markovian relaxation.
