#!/usr/bin/env python3
"""Finite high-precision checks of the displayed formulas, not theorem proofs."""

import json
import pathlib
import sys

import mpmath as mp


mp.mp.dps = 60
TOL = mp.mpf("1e-48")


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def text_number(x):
    return mp.nstr(x, 20)


def coeff_integral(n):
    return 2 / mp.pi * mp.quad(
        lambda theta: mp.tanh(mp.cos(theta)) * mp.cos(n * theta),
        [0, mp.pi / 2, mp.pi],
    )


def coeff_poles(n):
    def term(k):
        b = mp.pi * (k + mp.mpf("0.5"))
        s = mp.sqrt(1 + b * b)
        return (b + s) ** (-n) / s

    return 4 * (-1) ** ((n - 1) // 2) * mp.nsum(term, [0, mp.inf])


def check_coefficients():
    rows = []
    largest = mp.mpf(0)
    for n in (1, 3, 5, 9, 15):
        integral, poles = coeff_integral(n), coeff_poles(n)
        difference = abs(integral - poles)
        require(difference < TOL, f"Chebyshev normalization failed at n={n}")
        require((-1) ** ((n - 1) // 2) * integral > 0, "Wrong odd sign")
        largest = max(largest, difference)
        rows.append({"n": n, "coefficient": text_number(integral)})
    for n in (0, 2, 4, 8):
        require(abs(coeff_integral(n)) < TOL, "Even coefficient is not zero")
    return {
        "odd_coefficients": rows,
        "even_indices": [0, 2, 4, 8],
        "agreement_below_1e-48": bool(largest < TOL),
    }


def check_constants():
    b = mp.pi / 2
    s = mp.sqrt(1 + b * b)
    r = b + s
    c0 = 4 / s
    R = 2 * r
    d = (R - 1 / R) / 2
    A = c0 / 8 * r ** (-(mp.log(4 / c0) / mp.log(2) + 2))
    B = 2 * d * mp.log(r) / mp.log(2)
    require(A > mp.mpf("0.0075"), "Displayed prefactor is too large")
    require(B < 12, "Displayed exponent is too small")
    rows = []
    for tau in map(mp.mpf, ("0", "0.1", "1", "5", "20")):
        threshold = (2 * tau * d + mp.log(4 / c0)) / mp.log(2)
        n = max(1, int(mp.ceil(threshold)))
        if n % 2 == 0:
            n += 1
        entire_bound = 2 * mp.exp(2 * tau * d) * R ** (-n)
        target_lower = c0 * r ** (-n)
        require(entire_bound <= target_lower / 2 * (1 + TOL), "Ellipse choice failed")
        trace_lower = c0 / 8 * r ** (-n)
        conservative = mp.mpf("0.0075") * mp.exp(-12 * tau)
        require(trace_lower >= conservative, "Conservative lower bound failed")
        rows.append({"T_over_beta_hbar": text_number(tau), "odd_index": n})
    return {"A": text_number(A), "B": text_number(B), "ellipse_checks": rows}


def check_ramsey():
    I = mp.eye(2)
    Z = mp.diag([1, -1])
    Y = mp.matrix([[0, -1j], [1j, 0]])
    plus = mp.matrix([1, 1]) / mp.sqrt(2)
    rows = []
    for y in map(mp.mpf, ("-1", "-0.65", "0", "0.15", "0.9", "1")):
        U = mp.expm(-1j * y * Z / 4)
        psi = U * plus
        probability = (psi.H * (I + Y) / 2 * psi)[0]
        p_formula = (1 + mp.sin(y / 2)) / 2
        require(abs(probability - p_formula) < TOL, "Ramsey sign or factor failed")
        q_factory = 1 / (1 + mp.exp(4 * mp.asin(2 * p_formula - 1)))
        unnormalized = mp.expm(-y * Z)
        q_gibbs = unnormalized[0, 0] / (
            unnormalized[0, 0] + unnormalized[1, 1]
        )
        require(abs(q_factory - q_gibbs) < TOL, "Factory target population failed")
        rows.append({"y": text_number(y), "p": text_number(p_formula), "q": text_number(q_gibbs)})
    return {"state_evolution_matches_coin": True, "factory_matches_gibbs": True, "points": rows}


def kron(A, B):
    return mp.matrix([
        [A[i // B.rows, j // B.cols] * B[i % B.rows, j % B.cols]
         for j in range(A.cols * B.cols)]
        for i in range(A.rows * B.rows)
    ])


def check_complex_response():
    I = mp.eye(2)
    X = mp.matrix([[0, 1], [1, 0]])
    Y = mp.matrix([[0, -1j], [1j, 0]])
    Z = mp.diag([1, -1])
    signal = kron(Z, I)
    K1 = mp.mpf("0.7") * kron(X, X) + mp.mpf("0.2") * kron(I, Z)
    K2 = -mp.mpf("0.4") * kron(Y, I) + mp.mpf("0.3") * kron(Z, X)
    t1, t2 = mp.mpf("0.3"), mp.mpf("0.4")
    psi = mp.matrix([1, 0, 1, 0]) / mp.sqrt(2)
    initial = psi * psi.H

    def evolution(z):
        return mp.expm(-1j * t2 * (K2 + z * signal)) * mp.expm(
            -1j * t1 * (K1 + z * signal)
        )

    largest_ratio = mp.mpf(0)
    count = 0
    for x in map(mp.mpf, ("-1.3", "0.2", "1.7")):
        for v in map(mp.mpf, ("0", "0.3", "1")):
            z = x + 1j * v
            # U(conj(z))^dagger, not U(z)^dagger, is the analytic extension.
            density_extension = evolution(z) * initial * evolution(mp.conj(z)).H
            value = sum((signal * density_extension)[i, i] for i in range(4))
            bound = mp.exp(2 * (t1 + t2) * abs(v))
            ratio = abs(value) / bound
            require(ratio <= 1 + TOL, "Complex-response growth bound failed")
            largest_ratio = max(largest_ratio, ratio)
            count += 1
    return {"finite_control_examples": count, "largest_bound_ratio": text_number(largest_ratio)}


def main():
    result = {
        "scope": "Finite formula and matrix checks; general bounds and factory existence are established by proofs and cited theorems.",
        "decimal_precision": mp.mp.dps,
        "tolerance": "1e-48",
        "chebyshev": check_coefficients(),
        "constants": check_constants(),
        "ramsey": check_ramsey(),
        "complex_response": check_complex_response(),
    }
    encoded = json.dumps(result, indent=2, ensure_ascii=False) + "\n"
    if len(sys.argv) == 2 and sys.argv[1] == "--write-expected":
        path = pathlib.Path(__file__).with_name("expected") / "identities.json"
        path.parent.mkdir(exist_ok=True)
        path.write_text(encoded)
    elif len(sys.argv) != 1:
        raise SystemExit("Usage: python verification/check_identities.py [--write-expected]")
    else:
        expected = pathlib.Path(__file__).with_name("expected") / "identities.json"
        require(json.loads(expected.read_text()) == result, "Committed finite-check output differs")
    print(encoded, end="")


if __name__ == "__main__":
    main()
