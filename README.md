# Thermalization Deadline Limits

**How much extra time does accurate thermalization require when every run must finish by the same deadline?** For one qubit with an unknown energy splitting, this project establishes a sharp distinction between a deterministic deadline and a random stopping time.

The temperature and the Hamiltonian's axis are known. Its coefficient is unknown:

```math
H_y=\frac{y}{\beta}Z,\qquad -1\le y\le1,
\qquad
\gamma_y=\frac{I-\tanh(y)Z}{2}.
```

The same parameter-independent machine must work throughout this interval. It can use coherent controls, auxiliary systems, measurements and feedback. Accuracy is the trace distance of the unconditional output marginal from the Gibbs state.

| Finishing requirement | Optimal time dependence | Control model |
|---|---|---|
| Common deadline, uniform error at most $`\varepsilon`$ | $`\Theta(\beta\hbar\log(1/\varepsilon))`$ as $`\varepsilon\downarrow0`$ | Finite controls at each accuracy; all pulse durations count |
| Exact output after almost-sure termination | Worst-case mean $`\Theta(\beta\hbar)`$ | Ideal instantaneous instruments and potentially unbounded histories |
| Exact stopping with deadline exceeded with probability at most $`\eta`$, uniformly in $`y`$ | $`\Theta(\beta\hbar\log(1/\eta))`$ as $`\eta\downarrow0`$ | The same ideal stopping model |

In particular, every deterministic machine with deadline $`T`$ obeys

```math
\sup_{y\in[-1,1]}D(\rho_T(y),\gamma_y)
\ge\frac{3}{400}\exp\!\left[-\frac{12T}{\beta\hbar}\right].
```

Arbitrary control strength and apparatus size do not remove this error floor. Conversely, a Ramsey experiment combined with the [Nacu–Peres analytic coin-simulation theorem](references/RELATED_WORK.md#nacu-peres-analytic-coin-simulation) gives the matching order. The finite-deadline construction replaces any input state, including one entangled with an untouched reference.

## Read the science

Start with the [operational model and exact claims](science/model.md), then follow the [scientific reading route](science/README.md).

| To understand | Read |
|---|---|
| Why a finite exposure budget restricts every controlled response | [Analytic responses and adaptive instruments](science/analytic_response.md) |
| How the Gibbs poles force a quantitative error floor | [The deadline bound](science/deadline_bound.md) |
| How unknown dynamics produce exactly the needed thermal statistics | [Ramsey coins and Gibbs preparation](science/thermal_coin.md) |
| Why finite control pulses preserve the upper bound | [Finite controls and elapsed time](science/finite_controls.md) |
| How exactness coexists with finite mean time and unavoidable late runs | [Stopping times and deadline quantiles](science/stopping_time.md) |
| What the result says about thermalization and what it leaves open | [Physical interpretation](science/interpretation.md) |
| Which ingredients are inherited and which operational conclusion is established here | [Related work](references/RELATED_WORK.md) and [bibliography](references/references.bib) |

The [LLM reading guide](llms.txt) maps questions to their authoritative files.

## Learn the project

The single educational anchor is **Nielsen and Chuang, *Quantum Computation and
Quantum Information*, 10th Anniversary Edition (2010)**. The
[Nielsen–Chuang bridge](learning/NIELSEN_CHUANG_BRIDGE.md) connects its quantum
foundations to the unknown-Hamiltonian model, the approximation argument and
the stopping-time distinction.

The [30-milestone map](learning/MILESTONES.md) develops the background and then
the research story, with understanding targets, dependencies and links to the
authoritative proofs. Start at the [learning route](learning/README.md), or use
the direct scientific route above.

## Reproduce the checks

From the repository root:

```bash
python3 -m pip install -r verification/requirements.txt
python3 verification/check_identities.py
python3 verification/constants_certificate.py
```

The [verification account](verification/README.md) explains the distinction between the exact rational certificate, high-precision identity checks and the general written proofs. The finite checks do not implement or benchmark a complete Bernoulli factory.

## Scope

The energy interval is fixed in thermal units. The conclusions do not supply a joint low-temperature theorem for a fixed laboratory gap interval. Machine size, control amplitude, gate complexity, memory and thermodynamic work are unrestricted. The exact random-time construction uses ideal operations; the finite-control result establishes finite-accuracy preparation with every physical pulse duration included. A local autonomous bath or a fixed-strength controller would impose further constraints.

## Purpose and contact

This repository serves as a record of the work and a guide for the author’s self-directed learning. For discussion or potential collaboration, please contact Ruge Lin at [gogoko699@gmail.com](mailto:gogoko699@gmail.com).
