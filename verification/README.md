# Reproduce the finite checks

The proofs establish the deadline and stopping-time results. The numerical
checks here independently compare the displayed scalar formulas, constants,
and several finite quantum evolutions. They help catch normalization, sign,
and complex-conjugation errors.

## Run

From the repository root, install the pinned numerical dependency and run:

```bash
python -m pip install -r verification/requirements.txt
python verification/check_identities.py
python verification/constants_certificate.py
```

The script uses 60 decimal digits and a comparison tolerance of `1e-48`.
It raises an exception if an identity or inequality fails and compares its
deterministic output with [expected/identities.json](expected/identities.json).

| Check | Independent calculations | Scientific role |
|---|---|---|
| Gibbs population and Ramsey coin | Matrix exponentials and a Y measurement versus the sine formula; Gibbs matrix versus the analytic factory map | Checks the sign, interrogation duration and factor of two in the construction |
| Chebyshev coefficients | Numerical integration versus the infinite pole sum, at five odd and four even indices | Checks normalization, parity and the noncancelling pole contributions |
| Lower-bound constants | Computes the prefactor and exponent from the ellipse parameters; tests the chosen odd degree at five durations | Checks the conservative displayed error bound |
| Complex response | Nine complex-parameter evaluations of a two-qubit machine with two noncommuting control stages | Checks the analytic adjoint convention and growth estimate in finite examples |

The output gives `A = 0.0075370147177976880864` and
`B = 11.957972650959502896`, supporting the deliberately looser displayed
constants `0.0075` and `12`. These constants are not claimed optimal.

The separate [constants certificate](constants_certificate.py) uses only
Python's standard library and exact rational arithmetic. Alternating
arctangent series bound pi, rational square-root brackets bound the ellipse
parameters, and a convergent logarithm series with an explicit remainder
certifies that the exact prefactor exceeds `3/400` and the exact exponent
constant is below `12`. Its assertions do not depend on floating-point
rounding. The [deadline proof](../science/deadline_bound.md) derives the
inequalities certified by the script.

The complex extension uses the adjoint of the propagator evaluated at the
conjugated parameter. Taking the ordinary adjoint at the same complex
parameter would be nonanalytic and would invalidate the proof method.

## Scope

The general control theorem, coefficient comparison and random-stopping
statements are established in the [scientific account](../science/README.md).
The [Nacu–Peres theorem](../references/RELATED_WORK.md#nacu-peres-analytic-coin-simulation)
supplies the existence and exponential tail of the analytic Bernoulli
factory. This repository does not benchmark a finite-precision implementation
of that factory. Its arithmetic, memory, reset and work costs are outside
the stated interrogation-time objective.

Finite numerical samples do not establish a bound for every Hamiltonian,
controller or stopping rule. They do not replace the proofs or establish
priority. No actual-host rendering claim follows from running this script.

The maintenance option `--write-expected` regenerates the JSON only after
an intentional, independently reviewed formula change. Ordinary verification
uses the command above and leaves the committed output unchanged.
