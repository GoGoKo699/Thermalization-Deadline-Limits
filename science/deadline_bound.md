# The uniform thermalization deadline

For the [specified Hamiltonian family](model.md), a machine must reproduce
the Gibbs response across a whole interval of unknown energy splittings.
The [analytic-response estimate](analytic_response.md) constrains every
finite-time machine, regardless of its parameter-independent control
strength. Comparing its Chebyshev coefficients with those of the Gibbs
response gives a quantitative error floor.

## The bound

For every elapsed deadline $`T\ge0`$,

```math
\boxed{
e(T)\ge\frac3{400}
\exp\!\left[-\frac{12T}{\beta\hbar}\right].
}
```

Here $`e(T)`$ is the smallest uniform half-trace-distance error defined in
[the model](model.md). Consequently, for $`0\lt\varepsilon\lt3/400`$,

```math
T_\varepsilon\ge
\frac{\beta\hbar}{12}\log\frac3{400\varepsilon}.
```

No finite deterministic deadline yields exact Gibbs preparation throughout
the interval. The [thermal-coin construction](thermal_coin.md) and its
[finite-control implementation](finite_controls.md) attain the same
asymptotic order,

```math
T_\varepsilon^{\mathrm{opt}}
=\Theta\!\left(\beta\hbar\log\frac1\varepsilon\right).
```

The numerical constants in the lower bound are conservative.

## Exact constants and the dynamical input

For a machine of dimensionless signal action at most $`\mathfrak a`$,
the stronger bound proved below is

```math
E(M)\ge A_0e^{-B_0\mathfrak a},
```

where

```math
\begin{aligned}
b&=\frac{\pi}{2},&
s&=\sqrt{1+b^2},&
r&=b+s,\\
A_0&=\frac{1}{2sr^2}\,
s^{-\log r/\log2},&
B_0&=\left(2r-\frac1{2r}\right)\frac{\log r}{\log2}.
\end{aligned}
```

Their values are approximately

```math
A_0=0.007537014717797688\ldots,\qquad
B_0=11.95797265095950\ldots.
```

The conservative comparisons $`A_0\gt3/400`$ and $`B_0\lt12`$ are certified below
using exact rational arithmetic.

Let

```math
g(y)=\mathrm{Tr}[Z\rho_M(y)].
```

The [entire-response theorem](analytic_response.md) gives

```math
|g(x+iv)|\le e^{2\mathfrak a|v|}.
```

The target response is

```math
\mathrm{Tr}[Z\gamma_y]=-\tanh y.
```

For one always-on signal qubit, an elapsed deadline $`T`$ implies
$`\mathfrak a\le T/(\beta\hbar)`$. This entire-function bound is the only
dynamical input to the coefficient comparison.

## Chebyshev coefficients

Use the convention

```math
a_n[f]=\frac2\pi\int_0^\pi
f(\cos\theta)\cos(n\theta)\,d\theta,\qquad n\ge0.
```

The corresponding expansion, when convergent, is

```math
f(x)=\frac{a_0[f]}2+\sum_{n\ge1}a_n[f]T_n(x).
```

The elementary coefficient estimate

```math
|a_n[f]|\le2\|f\|_{\infty,[-1,1]}
```

will convert uniform approximation error into coefficient error.

### Deriving the partial fractions of the target

Set

```math
b_k=\pi\left(k+\frac12\right),\qquad k=0,1,\ldots.
```

We first derive

```math
\tanh z=\sum_{k=0}^\infty\frac{2z}{z^2+b_k^2}.
```

For $`z`$ away from the zeros of $`\cosh z`$, define on $`0\le t\le1`$

```math
u_z(t)=\frac{\sinh(zt)}{z\cosh z},
```

with $`u_0(t)=t`$. Then

```math
u_z''=z^2u_z,\qquad u_z(0)=0,\qquad u_z'(1)=1.
```

The functions $`\sin(b_k t)`$ form an orthogonal complete system on this
interval, with squared norm $`1/2`$. Integration by parts gives

```math
\begin{aligned}
(z^2+b_k^2)\int_0^1u_z(t)\sin(b_k t)\,dt
&=[u_z'(t)\sin(b_k t)-b_ku_z(t)\cos(b_k t)]_0^1\\
&=(-1)^k.
\end{aligned}
```

The Fourier coefficients of $`u_z`$ are therefore
$`2(-1)^k/(z^2+b_k^2)`$. They are absolutely summable. The sine series
converges uniformly to its continuous $`L^2`$ representative, which is
$`u_z(t)`$, including at $`t=1`$. Evaluating there gives

```math
\frac{\tanh z}{z}
=2\sum_{k=0}^\infty\frac1{z^2+b_k^2}.
```

This proves the partial-fraction formula, including its value at zero by
continuity. On every compact set away from the poles the terms are uniformly
$`O(k^{-2})`$, so the series is locally uniformly convergent.

### Computing the coefficient signs

For $`b\gt0`$, write

```math
s_b=\sqrt{1+b^2},\qquad r_b=b+s_b.
```

For $`\zeta\notin[-1,1]`$, choose the branch
$`S(\zeta)=\sqrt{\zeta^2-1}`$ satisfying $`S(\zeta)/\zeta\to1`$ at infinity,
and set $`w=\zeta-S(\zeta)`$. Then $`|w|\lt1`$ and

```math
\zeta=\frac12(w+w^{-1}),\qquad
S(\zeta)=\frac12(w^{-1}-w).
```

The geometric-series identity

```math
1+2\sum_{n\ge1}w^nT_n(x)
=\frac{1-w^2}{1-2wx+w^2}
```

implies the resolvent expansion

```math
\frac1{\zeta-x}
=\frac1{S(\zeta)}
\left[1+2\sum_{n\ge1}w^nT_n(x)\right],
\qquad -1\le x\le1.
```

At $`\zeta=ib`$ one has $`S(\zeta)=is_b`$ and $`w=-i/r_b`$.
At $`\zeta=-ib`$ these values are $`-is_b`$ and $`i/r_b`$.
Apply the expansion to

```math
\frac{x}{x^2+b^2}
=\frac12\left(\frac1{x-ib}+\frac1{x+ib}\right).
```

Its even coefficients vanish. For $`n=2m+1`$,

```math
\begin{aligned}
a_n\left[\frac{x}{x^2+b^2}\right]
&=\frac{i}{s_b}\left[(-i)^n-i^n\right]r_b^{-n}\\
&=\frac{2(-1)^m}{s_b}r_b^{-n}.
\end{aligned}
```

The partial fractions of $`\tanh`$ converge uniformly on $`[-1,1]`$,
so they can be integrated term by term. With

```math
s_k=\sqrt{1+b_k^2},\qquad r_k=b_k+s_k,
```

the exact odd coefficients are

```math
\boxed{
a_n[\tanh]=4(-1)^{(n-1)/2}
\sum_{k=0}^\infty\frac{r_k^{-n}}{s_k},
\qquad n\text{ odd}.
}
```

Every summand has the same sign. Taking only $`k=0`$, and putting $`c=4/s`$,
therefore gives

```math
|a_n[\tanh]|\ge c\,r^{-n}
\qquad(n\text{ odd}).
```

The same-sign formula is what justifies this nearest-pole lower estimate;
no noncancellation assumption is needed.

## Coefficients allowed by finite signal action

For any $`R\gt1`$ and any $`n\ge1`$, the entire response satisfies

```math
|a_n[g]|
\le2\exp\!\left[\mathfrak a(R-R^{-1})\right]R^{-n}.
```

To see this, form

```math
F(w)=g\!\left(\frac{w+w^{-1}}2\right),
```

which is analytic on $`0\lt|w|\lt\infty`$. Its $`n`$th Laurent coefficient is
$`a_n[g]/2`$: integrate on the unit circle and use the Chebyshev definition.
On the circle $`|w|=R`$,

```math
\left|\mathrm{Im}\,\frac{w+w^{-1}}2\right|
\le\frac{R-R^{-1}}2.
```

The entire-response bound and the Cauchy coefficient estimate now give the
claimed inequality.

## Comparing the coefficients

The machine's trace-distance error controls its scalar response:

```math
\delta:=\sup_{|y|\le1}|g(y)+\tanh y|
\le2E(M).
```

Hence

```math
|a_n[g]+a_n[\tanh]|\le4E(M).
```

Choose $`R=2r`$, and let $`n`$ be the smallest positive odd integer satisfying

```math
n\ge
u:=\frac{\mathfrak a(2r-(2r)^{-1})+\log s}{\log2}.
```

Since $`u\gt0`$, this choice obeys $`n\lt u+2`$. The allowed-response coefficient
bound gives

```math
\begin{aligned}
|a_n[g]|
&\le2e^{\mathfrak a(2r-(2r)^{-1})}(2r)^{-n}\\
&\le\frac2s\,r^{-n}
=\frac c2\,r^{-n}.
\end{aligned}
```

The target coefficient is at least twice this last upper bound. Therefore

```math
4E(M)
\ge\big||a_n[\tanh]|-|a_n[g]|\big|
\ge\frac c2\,r^{-n}.
```

It follows that

```math
\begin{aligned}
E(M)
&\ge\frac c8\,r^{-n}\\
&\ge\frac c{8r^2}
\exp\!\left[
-\frac{\log r}{\log2}
\left(\mathfrak a(2r-(2r)^{-1})+\log s\right)
\right]\\
&=A_0e^{-B_0\mathfrak a}.
\end{aligned}
```

This inequality holds for every admissible machine, independently of
apparatus size and control strength. Taking their infimum preserves the
same positive lower bound. Substituting
$`\mathfrak a\le T/(\beta\hbar)`$ and the certified conservative constants
proves the stated bound on $`e(T)`$.

## Exact impossibility

There is a short independent check on exact preparation. If an entire
response obeyed $`g(y)=-\tanh y`$ throughout the real interval, then the
entire function

```math
F(z)=\cosh z\,g(z)+\sinh z
```

would vanish on that interval and hence everywhere. At $`z=i\pi/2`$,
however, it equals $`i`$. This is a contradiction.

Analyticity alone gives this exact impossibility, but does not by itself
quantify the error of an increasingly elaborate sequence of machines at
the same deadline. The bounded-growth coefficient estimate supplies that
uniform exponential error floor.

## Certifying the conservative constants

The [executable constant certificate](../verification/constants_certificate.py)
uses only the Python standard library and exact rational comparisons.
Floating-point values are used only for optional printed diagnostics.

Machin's identity

```math
\pi=16\arctan(1/5)-4\arctan(1/239)
```

follows because $`4\arctan(1/5)-\arctan(1/239)`$ lies in $`(0,\pi/2)`$
and has tangent one. Alternating arctangent series give rational bounds on
$`\pi`$, and squaring gives rational bounds on $`s`$ and $`r`$.

For $`q\ge1`$, set $`t=(q-1)/(q+1)`$. The logarithm has the enclosure

```math
\log q=
2\sum_{k=0}^{n-1}\frac{t^{2k+1}}{2k+1}+R_n,
\qquad
0\le R_n\le
\frac{2t^{2n+1}}{(2n+1)(1-t^2)}.
```

These bounds certify $`B_0\lt12`$. To certify $`A_0\gt3/400`$, the program
checks the equivalent logarithmic inequality

```math
\log2+\log s+2\log r+
\frac{\log r\,\log s}{\log2}
\lt
\log(400/3)
=7\log2+\log(25/24).
```

Thus the rounded constants in the theorem are rigorous outward relaxations
of the exact expressions.

## Consequences and scope

The logarithmic accuracy cost concerns simultaneous approximation on the
fixed thermal interval. It is compatible with exact finite-time preparation
for a known Hamiltonian or for a specified pair, as in the
[Planckian thermalization framework](../references/RELATED_WORK.md#planckian-thermalization).

An outcome-dependent runtime changes the operational question.
[Exact stopping protocols](stopping_time.md) can have finite mean
interrogation time, while the deterministic theorem forces an exponential
worst-case stopping tail. The full stopping argument is given on that page.
The [interpretation](interpretation.md) discusses these distinctions and
the restrictions of the known-axis, single-signal-qubit model.

