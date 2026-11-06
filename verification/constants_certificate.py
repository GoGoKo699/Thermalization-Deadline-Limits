#!/usr/bin/env python3
"""Certify the conservative constants in the thermalization deadline bound.

All acceptance comparisons use fractions.Fraction. Floating-point numbers
are printed only as diagnostics after the exact comparisons have passed.

Run from the repository root:
    python verification/constants_certificate.py
"""

from fractions import Fraction
from math import isqrt


def atan_bounds(x: Fraction, terms: int = 20):
    """Enclose arctan(x) by its alternating series for 0 < x < 1."""
    if not 0 < x < 1 or terms < 1:
        raise ValueError("atan_bounds requires 0 < x < 1 and terms >= 1")
    partial = sum(
        ((-1) ** k * x ** (2 * k + 1) / Fraction(2 * k + 1)
         for k in range(terms)),
        Fraction(0),
    )
    next_term = x ** (2 * terms + 1) / Fraction(2 * terms + 1)
    if terms % 2 == 0:
        return partial, partial + next_term
    return partial - next_term, partial


def sqrt_bounds(q: Fraction, digits: int = 40):
    """Enclose sqrt(q) between consecutive rational decimal grid points."""
    if q < 0 or digits < 0:
        raise ValueError("sqrt_bounds requires q >= 0 and digits >= 0")
    scale = 10 ** digits
    integer = isqrt(q.numerator * scale * scale // q.denominator)
    return Fraction(integer, scale), Fraction(integer + 1, scale)


def log_bounds(q: Fraction, terms: int = 60):
    """Enclose log(q) by an atanh series and a geometric tail bound."""
    if q < 1 or terms < 1:
        raise ValueError("log_bounds requires q >= 1 and terms >= 1")
    t = (q - 1) / (q + 1)
    partial = 2 * sum(
        (t ** (2 * k + 1) / Fraction(2 * k + 1)
         for k in range(terms)),
        Fraction(0),
    )
    tail = (
        2 * t ** (2 * terms + 1)
        / (Fraction(2 * terms + 1) * (1 - t * t))
    )
    return partial, partial + tail


def main():
    # Machin: pi = 16 atan(1/5) - 4 atan(1/239).
    a_lower, a_upper = atan_bounds(Fraction(1, 5))
    b_lower, b_upper = atan_bounds(Fraction(1, 239))
    pi_lower = 16 * a_lower - 4 * b_upper
    pi_upper = 16 * a_upper - 4 * b_lower

    # s = sqrt(1 + pi^2/4), r = pi/2 + s.
    s_lower, _ = sqrt_bounds(1 + pi_lower * pi_lower / 4)
    _, s_upper = sqrt_bounds(1 + pi_upper * pi_upper / 4)
    r_lower = pi_lower / 2 + s_lower
    r_upper = pi_upper / 2 + s_upper

    log2_lower, log2_upper = log_bounds(Fraction(2))
    logr_lower, _ = log_bounds(r_lower)
    _, logr_upper = log_bounds(r_upper)
    _, logs_upper = log_bounds(s_upper)

    # B0 = (2r - 1/(2r)) log(r)/log(2).
    B_lower = (2 * r_lower - 1 / (2 * r_lower)) * logr_lower / log2_upper
    B_upper = (2 * r_upper - 1 / (2 * r_upper)) * logr_upper / log2_lower

    # A0 > 3/400 iff log(1/A0) < log(400/3).
    # log(1/A0) = log(2) + log(s) + 2log(r)
    #              + log(r)log(s)/log(2).
    log_inverse_A_upper = (
        log2_upper + logs_upper + 2 * logr_upper
        + logr_upper * logs_upper / log2_lower
    )
    # 400/3 = 2^7 * 25/24 keeps the logarithm series rapidly convergent.
    log_target_lower = 7 * log2_lower + log_bounds(Fraction(25, 24))[0]

    if not B_upper < Fraction(12):
        raise ArithmeticError("FAIL: the enclosure did not certify B0 < 12")
    if not log_inverse_A_upper < log_target_lower:
        raise ArithmeticError(
            "FAIL: the enclosure did not certify A0 > 3/400"
        )

    print("PASS: exact rational arithmetic certifies B0 < 12.")
    print("PASS: exact rational arithmetic certifies A0 > 3/400.")
    print("PASS: the conservative bound (3/400) exp(-12 a) is certified.")
    print("Diagnostics only; these rounded values are not acceptance checks:")
    print(f"  B0 enclosure, displayed: [{float(B_lower):.16g}, "
          f"{float(B_upper):.16g}]")
    print(f"  Positive margin for B0 < 12: {float(12 - B_upper):.16g}")
    print("  Positive logarithmic margin for A0 > 3/400: "
          f"{float(log_target_lower - log_inverse_A_upper):.16g}")


if __name__ == "__main__":
    main()

