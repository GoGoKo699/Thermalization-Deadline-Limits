# Thirty milestones for thermalization deadline limits

This map follows one question: **how does requiring one common finishing deadline change the time needed to prepare the thermal state of an unknown qubit Hamiltonian?** It connects the operational task, the analytic lower bound, the constructive upper bound, and the distinction between a deadline and a random stopping time. The authoritative claims and proofs remain in the [scientific account](../science/README.md).

## Structure and selected anchor

The map contains **12 background/preliminaries milestones and 18 narrative/innovation milestones**. The background must connect quantum states and operations to three less familiar ingredients: uniform approximation, analytic response, and stopping distributions. Twelve milestones assemble that framework. The eighteen narrative milestones then connect the two proof mechanisms, their physical implementation, and their consequences. Each phase begins with individual objects or mechanisms and ends by integrating them into the project's full task or result.

The selected educational anchor is Michael A. Nielsen and Isaac L. Chuang, *Quantum Computation and Quantum Information*, **10th Anniversary Edition (2010)**. The chapter codes below are used in the source pointers. They identify chapter-level foundations; the [Nielsen–Chuang bridge](NIELSEN_CHUANG_BRIDGE.md) connects those foundations to the repository's notation and arguments.

| Code | Selected anchor chapter | Publisher chapter pages | Role here |
|---|---|---|---|
| NC2 | Chapter 2, Introduction to quantum mechanics | 60–119 | States, observables, unitary dynamics, composite systems and measurement |
| NC4 | Chapter 4, Quantum circuits | 171–215 | Known gates, ancillary registers and finite circuits |
| NC8 | Chapter 8, Quantum noise and quantum operations | 353–398 | Channels, environments, discarded registers and instruments |
| NC9 | Chapter 9, Distance measures for quantum information | 399–424 | Operational comparison of quantum states and processes |

Complex continuation, Chebyshev approximation, the analytic Bernoulli-factory theorem, and the project's deadline and stopping results are supplied by the linked scientific pages and their cited sources. They are not attributed to the textbook. The map provides the connected understanding needed for the project; specialist calculations and technical variants remain in those pages.

| Phase | Progression | Integration point |
|---|---|---|
| Background/preliminaries, [M01](#m01)–[M12](#m12) | Qubit objects → operations and accuracy → mathematical and probabilistic tools → complete task | [M12: The complete operational question](#m12) |
| Narrative/innovation, [M13](#m13)–[M30](#m30) | Response constraint and target obstruction → thermal sampler and finite controls → optimal deadlines and stopping tradeoffs | [M30: The complete scientific conclusion](#m30) |

Dependencies refer to earlier milestones. A source pointer locates the corresponding definition, proof, construction, or interpretation; it does not replace that source's assumptions.

## Phase I: Background and preliminaries

<a id="m01"></a>
### M01: States, populations and observable responses

**Central question.** How can a mixed qubit state be characterized through populations and expectation values?

**Understanding target.** Distinguish a density operator from an individual measurement outcome. Relate the populations in the fixed computational basis to the expectation of $`Z`$, and recognize the Bloch-vector description used by the target and the Ramsey experiment.

**Dependencies and story role.** None. This establishes the local quantum objects whose response to the unknown parameter will be compared.

**Conceptual connection.** A single expectation can witness failure to prepare a state, while a classical random choice of basis states can produce its correct diagonal density operator.

**Sources.** [Hamiltonian and target](../science/model.md#hamiltonian-and-target); [the Ramsey coin](../science/thermal_coin.md#the-ramsey-coin). **Anchor:** NC2.

<a id="m02"></a>
### M02: Gibbs populations in thermal units

**Central question.** What thermal state is required for each promised Hamiltonian?

**Understanding target.** Explain the family $`H_y=(y/\beta)Z`$, the known inverse temperature, and the unknown dimensionless parameter $`y\in[-1,1]`$. Read the target population $`q(y)=1/(1+e^{2y})`$ with fixed computational labels, including the change of energy ordering when the sign of $`y`$ changes.

**Dependencies and story role.** [M01](#m01). This gives the physical target before introducing its preparation cost.

**Conceptual connection.** Fixing the interval in thermal units keeps the response function fixed as temperature changes; fixing a laboratory gap interval would pose a different joint limit.

**Sources.** [Hamiltonian and target](../science/model.md#hamiltonian-and-target); [temperature and bandwidth](../science/interpretation.md#temperature-and-bandwidth). **Anchor:** NC2; the Gibbs family and temperature scaling are specified locally.

<a id="m03"></a>
### M03: Dynamics, phase and signal action

**Central question.** How does interaction time let an unknown Hamiltonian influence a machine?

**Understanding target.** Connect unitary phase accumulation to elapsed time and distinguish a known control from the bounded unknown signal generator. Understand why the dimensionless signal action is $`T/(\beta\hbar)`$ for the single always-on qubit.

**Dependencies and story role.** [M01](#m01), [M02](#m02). This identifies the resource that later controls the machine's parameter dependence.

**Conceptual connection.** Strong known operations can rearrange the experiment, but the analytic estimate charges the integrated norm of the unknown perturbation.

**Sources.** [Signal action](../science/analytic_response.md#signal-action); [a machine with a deterministic deadline](../science/model.md#a-machine-with-a-deterministic-deadline). **Anchor:** NC2, NC4.

<a id="m04"></a>
### M04: One machine for a continuous family

**Central question.** What must be fixed before the unknown parameter is encountered?

**Understanding target.** Separate knowledge of the promised family from knowledge of its actual member. Explain why the initial apparatus, control policy and output rule may depend on temperature and accuracy, but cannot encode the unknown $`y`$.

**Dependencies and story role.** [M02](#m02), [M03](#m03). This turns an individual state-preparation problem into a uniform task for one parameter-independent design.

**Conceptual connection.** Reproducing a response over an interval is a stronger requirement than matching a known value or a specified pair; this distinction drives the accuracy-dependent lower bound.

**Sources.** [A machine with a deterministic deadline](../science/model.md#a-machine-with-a-deterministic-deadline); [a precision cost beyond a thermal timescale](../science/interpretation.md#a-precision-cost-beyond-a-thermal-timescale). **Anchor:** NC2, NC4; the uniform-family requirement is supplied locally.

<a id="m05"></a>
### M05: Channels, ancillary systems and replacement

**Central question.** How can unitary dynamics on a larger system implement reset and mixed-state output?

**Understanding target.** Describe a channel through ancillary registers, joint evolution and a final partial trace. Understand the replacement map $`\mathcal G_y(X)=\mathrm{Tr}(X)\gamma_y`$ and the role of an entropy sink in discarding the incoming state.

**Dependencies and story role.** [M01](#m01), [M04](#m04). This expands the local sensor into the full preparation machine.

**Conceptual connection.** Preparing a target marginal does not require returning the apparatus to its initial state or removing correlations from every discarded record.

**Sources.** [Accuracy and input states](../science/model.md#accuracy-and-input-states); [replacement of an arbitrary input](../science/thermal_coin.md#replacement-of-an-arbitrary-input). **Anchor:** NC2, NC8.

<a id="m06"></a>
### M06: Measurements and feedback as a fixed quantum process

**Central question.** How can a machine adapt to measured data while its design remains parameter independent?

**Understanding target.** Represent an instrument by outcome operators and an orthogonal record. Distinguish a record-dependent operation chosen by a fixed policy from a control supplied with the unknown parameter. Keep the probabilities of every outcome in the unconditional output.

**Dependencies and story role.** [M04](#m04), [M05](#m05). This brings adaptive protocols into the same operational framework as circuits.

**Conceptual connection.** Retaining measurement records coherently and tracing them at the end makes feedback accessible to both the universal lower proof and the finite upper construction.

**Sources.** [Instruments and coherent records](../science/analytic_response.md#instruments-and-coherent-records); [why coherent records give the same channel](../science/finite_controls.md#why-coherent-records-give-the-same-channel). **Anchor:** NC2, NC4, NC8.

<a id="m07"></a>
### M07: State error, observable witnesses and reference systems

**Central question.** What does it mean for the prepared state or preparation channel to be accurate?

**Understanding target.** Use the convention $`D(\rho,\sigma)=\tfrac12\|\rho-\sigma\|_1`$. Explain how the $`Z`$ response bounds state error, why diagonal-qubit error reduces to population error, and why an arbitrary untouched reference belongs in the stronger replacement-channel criterion.

**Dependencies and story role.** [M01](#m01), [M05](#m05), [M06](#m06). This fixes the operational meaning of every later error bound.

**Conceptual connection.** The lower bound needs only a scalar witness for one fixed input; the construction can satisfy the stronger channel requirement for all inputs. The project's diamond-norm details are supplied locally.

**Sources.** [Accuracy and input states](../science/model.md#accuracy-and-input-states); [comparing the coefficients](../science/deadline_bound.md#comparing-the-coefficients); [replacement of an arbitrary input](../science/thermal_coin.md#replacement-of-an-arbitrary-input). **Anchor:** NC2, NC8, NC9.

<a id="m08"></a>
### M08: Unknown-bias coins and sampling

**Central question.** How can observed bits be useful without first estimating their bias?

**Understanding target.** Distinguish a coin of bias $`p(y)`$, its realized binary outcomes, and an estimate of $`y`$. Understand conditional-on-$`y`$ independence from fresh preparations, and how a fixed decision rule can turn an input word into a new random bit.

**Dependencies and story role.** [M01](#m01), [M03](#m03), [M06](#m06). This introduces the statistical objects used by the constructive route.

**Conceptual connection.** Thermal state preparation asks for a correctly distributed sample; it does not demand an accurate numerical estimate of the Hamiltonian on each run.

**Sources.** [The Ramsey coin](../science/thermal_coin.md#the-ramsey-coin); [finite words specify every decision](../science/thermal_coin.md#finite-words-specify-every-decision); [sampling need not estimate the Hamiltonian](../science/interpretation.md#sampling-need-not-estimate-the-hamiltonian). **Anchor:** NC2, NC4; bias conversion is developed locally.

<a id="m09"></a>
### M09: Analytic continuation as a constraint on real responses

**Central question.** Why can a complex parameter help prove a limit for a real experiment?

**Understanding target.** Distinguish an entire response from a meromorphic target, and distinguish analyticity from a quantitative growth bound. Recognize complex continuation as a mathematical extension of the real-parameter response, without assigning it the meaning of a physical state.

**Dependencies and story role.** [M03](#m03), [M04](#m04), [M07](#m07). This supplies the conceptual vocabulary of the lower-bound mechanism.

**Conceptual connection.** Real dynamics determines a response function; its allowed complex growth constrains how accurately it can agree with the Gibbs response throughout a real interval.

**Sources.** [Entire-response bound](../science/analytic_response.md#entire-response-bound); [exact impossibility](../science/deadline_bound.md#exact-impossibility); [why the complex poles matter](../science/interpretation.md#why-the-complex-poles-matter). **Anchor:** NC2 for the underlying quantum dynamics; the complex-analysis bridge is supplied locally.

<a id="m10"></a>
### M10: Uniform approximation through Chebyshev coefficients

**Central question.** How can one coefficient expose an error across a whole interval?

**Understanding target.** Understand the expansion in Chebyshev polynomials on $`[-1,1]`$, its coefficient convention, and the estimate $`|a_n[f]|\le2\|f\|_\infty`$. Identify the roles of complex growth, target singularities and coefficient mismatch without needing every resolvent calculation.

**Dependencies and story role.** [M07](#m07), [M09](#m09). This gives the comparison tool that turns an analytic obstruction into a uniform error floor.

**Conceptual connection.** State accuracy constrains the error of an observable response, which in turn constrains every Chebyshev coefficient of that response.

**Sources.** [Chebyshev coefficients](../science/deadline_bound.md#chebyshev-coefficients); [coefficients allowed by finite signal action](../science/deadline_bound.md#coefficients-allowed-by-finite-signal-action). **Anchor:** NC9 for the operational distance connection; Chebyshev analysis is supplied locally.

<a id="m11"></a>
### M11: Deadlines, tails, expectations and quantiles

**Central question.** Which different finishing-time requirements can be imposed on a randomized protocol?

**Understanding target.** Distinguish a common deterministic cap, almost-sure termination, expected runtime and a deadline exceeded with probability at most $`\eta`$. Understand why a small probability of unfinished runs can bound the error introduced by a fallback output.

**Dependencies and story role.** [M06](#m06), [M07](#m07), [M08](#m08). This prepares the probabilistic connection between approximate deadlines and exact stopping.

**Conceptual connection.** Averaging all eventual outputs differs from conditioning on early completion; a finite expectation can coexist with arbitrarily late possible runs.

**Sources.** [The stopping model](../science/stopping_time.md#the-stopping-model); [truncating an exact protocol](../science/stopping_time.md#truncating-an-exact-protocol); [deadline quantiles](../science/stopping_time.md#deadline-quantiles). **Anchor:** NC2, NC8 for measurement probabilities and instruments; stopping-time reasoning is supplied locally.

<a id="m12"></a>
### M12: The complete operational question

**Central question.** What, precisely, must a universal deadline or stopping claim establish?

**Understanding target.** Assemble the promised thermal interval, one unknown signal qubit, parameter-independent design, charged signal action, discarded apparatus and uniform output error. Distinguish the finite-control elapsed-time task from the ideal-instrument exact-stopping task, including their different resource allowances.

**Dependencies and story role.** [M01](#m01)–[M11](#m11). This completes the background phase by making the full problem and its quantifiers explicit.

**Conceptual connection.** The same target family supports two finishing requirements. Their comparison is meaningful only when the input criterion, charged resource and allowed operations stay visible.

**Sources.** [The task and theorem statements](../science/model.md); [what is deliberately unrestricted](../science/interpretation.md#what-is-deliberately-unrestricted). **Anchor:** NC2, NC4, NC8, NC9, joined through the [anchor bridge](NIELSEN_CHUANG_BRIDGE.md).

## Phase II: Narrative and innovation

<a id="m13"></a>
### M13: From signal action to controlled-propagator growth

**Central question.** Why can arbitrary known controls not remove the analytic cost of obtaining parameter dependence?

**Understanding target.** Explain the interaction-picture Dyson argument: the bounded unknown perturbation produces an entire propagator, and its continuation to $`x+iv`$ has norm at most $`e^{\mathfrak a|v|}`$. Identify the well-posedness assumptions needed for larger apparatuses.

**Dependencies and story role.** [M03](#m03), [M09](#m09), [M12](#m12). This is the local dynamical ingredient of the converse.

**Conceptual connection.** Moving known dynamics into an interaction picture preserves the signal norm; the resulting bound is independent of apparatus dimension and any common control-strength ceiling.

**Sources.** [Signal action](../science/analytic_response.md#signal-action); [analytic continuation of the propagator](../science/analytic_response.md#analytic-continuation-of-the-propagator). **Anchor:** NC2, NC4; the norm estimate is proved locally.

<a id="m14"></a>
### M14: From a propagator to an entire observable response

**Central question.** How does the dynamical bound survive the conversion to a measured output?

**Understanding target.** Explain why the analytic continuation uses $`U_z^\sharp=U_{\bar z}^\dagger`$ and a fixed output observable pulled back through the discard channel. Account for the two propagator factors in

```math
|g(x+iv)|\le e^{2\mathfrak a|v|}.
```

**Dependencies and story role.** [M05](#m05), [M07](#m07), [M09](#m09), [M13](#m13). This turns a joint dynamical estimate into the scalar response used by the approximation proof.

**Conceptual connection.** Positivity and normalization are required for the real physical process; complex continuation needs analyticity and norm control, rather than a fictitious complex-parameter density operator.

**Sources.** [Analytic continuation of the output](../science/analytic_response.md#analytic-continuation-of-the-output). **Anchor:** NC2, NC8, NC9.

<a id="m15"></a>
### M15: Why feedback and limiting protocols remain covered

**Central question.** What makes the response constraint universal over the declared machine class?

**Understanding target.** Connect coherent records, a common cumulative-action clock, protected finished outputs and well-defined bounded-action limits. Explain why branch costs must be aligned by their cumulative action, and why all unnormalized branches remain in the response.

**Dependencies and story role.** [M06](#m06), [M11](#m11), [M12](#m12), [M14](#m14). This extends the local response proof to the full converse class.

**Conceptual connection.** A mathematical dilation may enlarge the allowed controls for a lower bound. The separate finite upper construction must still implement its own physical schedule.

**Sources.** [Instruments and coherent records](../science/analytic_response.md#instruments-and-coherent-records); [branch-dependent interrogation lengths](../science/analytic_response.md#branch-dependent-interrogation-lengths); [well-defined limiting protocols](../science/analytic_response.md#well-defined-limiting-protocols). **Anchor:** NC4, NC8; the action-clock and limiting arguments are supplied locally.

<a id="m16"></a>
### M16: Exact agreement is already impossible at a finite deadline

**Central question.** Why can no finite-action machine reproduce the Gibbs response exactly on the whole interval?

**Understanding target.** Follow the identity-theorem contradiction for $`\cosh z\,g(z)+\sinh z`$, evaluated at $`z=i\pi/2`$. Distinguish this impossibility for an exact response from a uniform positive error bound over every machine at the same deadline.

**Dependencies and story role.** [M02](#m02), [M09](#m09), [M14](#m14), [M15](#m15). This exposes the target obstruction before quantifying it.

**Conceptual connection.** Agreement throughout a continuous real interval determines analytic continuation, whereas agreement at finitely many isolated parameter values need not do so.

**Sources.** [Exact impossibility](../science/deadline_bound.md#exact-impossibility); [why the complex poles matter](../science/interpretation.md#why-the-complex-poles-matter). **Anchor:** NC2 for the target observable; the identity-theorem argument is supplied locally.

<a id="m17"></a>
### M17: The target has unavoidable odd coefficients

**Central question.** Why do the poles of the Gibbs response yield a reliable coefficient lower bound?

**Understanding target.** Understand the partial-fraction representation of $`\tanh`$ and the same-sign contributions to each odd Chebyshev coefficient. Explain why retaining the nearest pole pair gives a lower estimate without assuming away cancellation.

**Dependencies and story role.** [M02](#m02), [M09](#m09), [M10](#m10), [M16](#m16). This supplies the target side of the quantitative obstruction.

**Conceptual connection.** The locations of singularities suggest a decay scale, but the sign calculation is what validates the coefficient lower bound used here.

**Sources.** [Deriving the partial fractions of the target](../science/deadline_bound.md#deriving-the-partial-fractions-of-the-target); [computing the coefficient signs](../science/deadline_bound.md#computing-the-coefficient-signs). **Anchor:** NC2 for the underlying state response; the approximation calculation is supplied locally.

<a id="m18"></a>
### M18: Finite action limits the machine's coefficients

**Central question.** How does the entire-response growth bound restrict a real-interval approximation?

**Understanding target.** Follow the substitution $`z=(w+w^{-1})/2`$ that relates Chebyshev and Laurent coefficients. Explain the roles of the contour radius and the Cauchy estimate in limiting the coefficients available at a given signal action.

**Dependencies and story role.** [M09](#m09), [M10](#m10), [M14](#m14), [M15](#m15). This supplies the machine side of the coefficient comparison.

**Conceptual connection.** More signal action permits greater complex growth, but at every fixed action an appropriate sufficiently high coefficient remains too small to match the target.

**Sources.** [Coefficients allowed by finite signal action](../science/deadline_bound.md#coefficients-allowed-by-finite-signal-action). **Anchor:** NC2, NC9 for the dynamical and error interpretations; the contour estimate is supplied locally.

<a id="m19"></a>
### M19: One coefficient forces a uniform error floor

**Central question.** How do the two coefficient estimates become a thermalization time lower bound?

**Understanding target.** Explain the choice of an odd index proportional to signal action, the resulting coefficient mismatch, and its conversion to trace-distance error. Recover the meaning of

```math
e(T)\ge\frac{3}{400}\exp\!\left[-\frac{12T}{\beta\hbar}\right].
```

**Dependencies and story role.** [M07](#m07), [M17](#m17), [M18](#m18). This integrates the converse ingredients into a bound applying to the infimum over all admissible machines.

**Conceptual connection.** The quantitative growth constraint prevents success through an increasingly elaborate sequence of machines at the same deadline. Exact rational checks certify the conservative displayed constants.

**Sources.** [Comparing the coefficients](../science/deadline_bound.md#comparing-the-coefficients); [certifying the conservative constants](../science/deadline_bound.md#certifying-the-conservative-constants); [the bound](../science/deadline_bound.md#the-bound). **Anchor:** NC9.

<a id="m20"></a>
### M20: A short Ramsey exposure carries the required parameter information

**Central question.** Which accessible random variable can be converted into the desired Gibbs population?

**Understanding target.** Explain how a duration $`t_0=\beta\hbar/4`$ produces bias $`p(y)=[1+\sin(y/2)]/2`$. Identify the known analytic map $`F`$ satisfying $`F(p(y))=q(y)`$, and check why both its input interval and output probabilities stay inside $`(0,1)`$.

**Dependencies and story role.** [M02](#m02), [M03](#m03), [M08](#m08), [M09](#m09), [M12](#m12). This supplies the physical input and the mathematical specification for the constructive route.

**Conceptual connection.** A fixed short interrogation can provide suitable sample information even though it does not reveal the unknown numerical parameter.

**Sources.** [The Ramsey coin](../science/thermal_coin.md#the-ramsey-coin). **Anchor:** NC2, NC4.

<a id="m21"></a>
### M21: An analytic factory turns Ramsey coins into thermal coins

**Central question.** What imported theorem supplies exact bias conversion with controlled stopping tails?

**Understanding target.** State the role of Nacu–Peres Theorem 2 and Proposition 21: one simulator for the fixed analytic map has an exact output bias and a uniform exponential input-count tail. Understand its nested finite-word decisions and their parameter-independent labels.

**Dependencies and story role.** [M08](#m08), [M11](#m11), [M20](#m20). This connects the physical coin to an existing probabilistic construction while making the external proof dependency explicit.

**Conceptual connection.** The unknown bias enters through observed words; a finite-prefix decision table is specified in advance. Exponential stopping tails become the source of logarithmic cutoff accuracy.

**Sources.** [The analytic coin-simulation theorem](../science/thermal_coin.md#the-analytic-coin-simulation-theorem); [finite words specify every decision](../science/thermal_coin.md#finite-words-specify-every-decision). **Anchor:** NC2, NC4 for probabilities and circuit interpretation; the coin-simulation theorem is attributed to Nacu and Peres.

<a id="m22"></a>
### M22: A cutoff produces an unconditional approximate state

**Central question.** Why can unfinished simulations be retained without spoiling the required accuracy?

**Understanding target.** Couple exact and truncated outputs using the same input word. Explain why a fixed fallback changes the output population by at most $`\Pr_y(N\gt n)`$, and why that population error is exactly the trace distance between the two diagonal target states.

**Dependencies and story role.** [M07](#m07), [M11](#m11), [M21](#m21). This turns an unbounded exact factory into a finite-accuracy preparation rule.

**Conceptual connection.** Every timeout contributes to the scored mixture. The guarantee follows from its total probability and does not rely on conditioning on successful completion.

**Sources.** [Truncation retains every timeout branch](../science/thermal_coin.md#truncation-retains-every-timeout-branch); [number of interrogations](../science/thermal_coin.md#number-of-interrogations). **Anchor:** NC8, NC9.

<a id="m23"></a>
### M23: A fixed finite circuit replaces any input

**Central question.** How is the truncated rule realized using one signal qubit and a common schedule?

**Understanding target.** Explain fresh probes, equal-duration Ramsey slots, a reversible finite-word table, the retained word register and the final swap. Show how tracing orthogonal records gives the desired mixture and discards any incoming state while preserving its reference marginal.

**Dependencies and story role.** [M05](#m05), [M06](#m06), [M07](#m07), [M20](#m20), [M22](#m22). This assembles the sampler into a complete ideal preparation channel.

**Conceptual connection.** Running every slot on every branch supplies a true common schedule, and a coherent implementation reproduces the classical mixture without intermediate measurements or free parallel signal copies.

**Sources.** [One common schedule](../science/finite_controls.md#one-common-schedule); [why coherent records give the same channel](../science/finite_controls.md#why-coherent-records-give-the-same-channel); [replacement of an arbitrary input](../science/thermal_coin.md#replacement-of-an-arbitrary-input). **Anchor:** NC2, NC4, NC8, NC9.

<a id="m24"></a>
### M24: Finite pulses tolerate the always-on unknown drift

**Central question.** Does implementing the known gates take additional charged time and introduce additional error?

**Understanding target.** Explain the Hermitian-logarithm implementation of each known gate, its positive pulse duration, and the drift-error estimate. Understand how telescoping the finite circuit bounds total half-diamond error by $`\delta_{\mathrm{ctrl}}/(\beta\hbar)`$.

**Dependencies and story role.** [M03](#m03), [M07](#m07), [M23](#m23). This connects the ideal circuit to continuous finite-strength control while keeping the unknown Hamiltonian present.

**Conceptual connection.** Allocating half the error allowance to control pulses preserves the leading logarithmic deadline. The proof controls the full channel, including pulse-induced correlations.

**Sources.** [Implementing each known gate in positive time](../science/finite_controls.md#implementing-each-known-gate-in-positive-time); [total error and elapsed time](../science/finite_controls.md#total-error-and-elapsed-time). **Anchor:** NC2, NC4, NC8, NC9; the perturbation estimate is proved locally.

<a id="m25"></a>
### M25: Finite descriptions preserve the existence upper bound

**Central question.** Which finiteness claims does the implementation establish at each positive accuracy?

**Understanding target.** Distinguish a finite decision table and finitely specified pulse sequence from an efficient implementation. Explain why finite precision in gate descriptions and timings is sufficient when its error and elapsed-time allowances are reserved together.

**Dependencies and story role.** [M12](#m12), [M21](#m21), [M23](#m23), [M24](#m24). This completes the physical construction and exposes its resource dependence.

**Conceptual connection.** Finiteness at each accuracy allows apparatus size and control strength to grow across accuracies. It does not impose a fixed bandwidth, locality, work budget or efficient table compilation.

**Sources.** [Finite descriptions and timing precision](../science/finite_controls.md#finite-descriptions-and-timing-precision); [scope of the construction](../science/finite_controls.md#scope-of-the-construction). **Anchor:** NC4, NC8, NC9.

<a id="m26"></a>
### M26: The deterministic deadline has matching order

**Central question.** What follows when the universal converse and physical construction are compared?

**Understanding target.** Explain the matching small-error order

```math
T_\varepsilon^{\mathrm{opt}}
=\Theta\!\left(\beta\hbar\log\frac1\varepsilon\right),
\qquad \varepsilon\downarrow0.
```

Distinguish matching asymptotic order from an optimal numerical exponent, and understand why the result holds for both fixed-input preparation and the stronger replacement-channel task.

**Dependencies and story role.** [M12](#m12), [M19](#m19), [M22](#m22)–[M25](#m25). This joins the two proof routes into the deterministic result.

**Conceptual connection.** The lower bound is broad enough to include ideal instruments, and the upper bound is physical enough to charge every finite pulse. Their overlap fixes the optimal scaling for the stated family.

**Sources.** [Deterministic deadline theorem](../science/model.md#deterministic-deadline-theorem); [the bound](../science/deadline_bound.md#the-bound); [total error and elapsed time](../science/finite_controls.md#total-error-and-elapsed-time). **Anchor:** NC2, NC4, NC8, NC9.

<a id="m27"></a>
### M27: Removing the cutoff permits exact random stopping

**Central question.** How can exact thermal output coexist with a finite worst-case mean interrogation time?

**Understanding target.** Explain almost-sure termination of the untruncated exact factory and use its uniform exponential count tail to bound the mean of $`\tau=(\beta\hbar/4)N`$. Keep exactness attached to the unconditional terminal marginal.

**Dependencies and story role.** [M11](#m11), [M12](#m12), [M20](#m20), [M21](#m21), [M26](#m26). This changes the finishing requirement and exhibits the alternative upper bound.

**Conceptual connection.** The exact sampler has potentially unbounded histories and memory in the ideal-instrument stopping model. The finite-accuracy control construction does not assert an exact finite-strength realization of that unbounded process.

**Sources.** [Exact output with random stopping](../science/thermal_coin.md#exact-output-with-random-stopping); [worst-case mean time](../science/stopping_time.md#worst-case-mean-time); [relation to finite controls](../science/stopping_time.md#relation-to-finite-controls). **Anchor:** NC2, NC8; the stopping estimate is supplied locally.

<a id="m28"></a>
### M28: Every exact protocol must allow late runs

**Central question.** What universal stopping constraint follows from the deterministic error floor?

**Understanding target.** Truncate any admissible exact protocol, protect completed outputs and substitute a fixed fallback on unfinished histories. Explain why the induced error is bounded by the unfinished probability, forcing

```math
\sup_y\Pr_y(\tau\gt T)
\ge\frac{3}{400}e^{-12T/(\beta\hbar)}.
```

**Dependencies and story role.** [M11](#m11), [M15](#m15), [M19](#m19), [M27](#m27). This converts the universal approximation bound into a universal exact-stopping tail bound.

**Conceptual connection.** The argument preserves early output marginals without assuming that early completion preserves Gibbs statistics. The parameter giving the worst tail may change with the deadline.

**Sources.** [Truncating an exact protocol](../science/stopping_time.md#truncating-an-exact-protocol); [the quantifier in the tail bound](../science/stopping_time.md#the-quantifier-in-the-tail-bound). **Anchor:** NC2, NC8, NC9.

<a id="m29"></a>
### M29: Optimal expectations and deadline quantiles

**Central question.** What can now be said sharply about the mean runtime and the probability of missing a deadline?

**Understanding target.** Combine the universal tail lower bound with the exact factory's upper tail. Explain the optimal worst-case mean order $`\Theta(\beta\hbar)`$ and the optimal uniform deadline-quantile order $`\Theta(\beta\hbar\log(1/\eta))`$ as $`\eta\downarrow0`$.

**Dependencies and story role.** [M11](#m11), [M27](#m27), [M28](#m28). This integrates the stopping results into a comparison of three operational resources.

**Conceptual connection.** One selected deadline gives the mean lower bound without interchanging a supremum and an integral. Finite mean time and a logarithmic high-confidence deadline are compatible.

**Sources.** [Deadline quantiles](../science/stopping_time.md#deadline-quantiles); [worst-case mean time](../science/stopping_time.md#worst-case-mean-time). **Anchor:** NC2, NC9 for probability and operational-error foundations; the minimax stopping results are proved locally.

<a id="m30"></a>
### M30: The complete scientific conclusion

**Central question.** What has the deadline comparison established, and where do its conclusions stop?

**Understanding target.** Explain the connected result: a common deadline requires logarithmic accuracy cost, exact ideal random stopping has finite optimal mean, and worst-case late runs are unavoidable. State the fixed thermal interval, known axis, single charged signal and broad control allowances that make those conclusions precise.

**Dependencies and story role.** [M12](#m12), [M15](#m15), [M19](#m19), [M21](#m21), [M25](#m25)–[M29](#m29). This completes the narrative phase by connecting mechanisms, operational consequences, attribution and scope.

**Conceptual connection.** The result refines a thermal-timescale question through accuracy and finishing requirements. Its imported coin-simulation theorem, analytic proof ingredients and finite checks have distinct roles; it does not supply a general many-body mixing law, fixed-strength optimum or thermodynamic work bound.

**Sources.** [Physical interpretation](../science/interpretation.md); [exact theorem statements](../science/model.md); [related work and attribution](../references/RELATED_WORK.md); [verification scope](../verification/README.md). **Anchor:** NC2, NC4, NC8, NC9, connected by the [anchor bridge](NIELSEN_CHUANG_BRIDGE.md).

## Routes back to the science

For exact assumptions and quantifiers, return to [the model](../science/model.md). For the converse, follow [analytic response](../science/analytic_response.md) into [the deadline bound](../science/deadline_bound.md). For achievability, follow [thermal coins](../science/thermal_coin.md) into [finite controls](../science/finite_controls.md). For the change in finishing requirement, use [stopping times](../science/stopping_time.md) and the [interpretation](../science/interpretation.md).
