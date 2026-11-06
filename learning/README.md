# Learn the thermalization result

A thermal state assigns probabilities to energy levels. If the energy splitting
is unknown, a machine must obtain the right probabilities through its interaction
with the system. This project asks what changes when every run must finish by
the same time, compared with allowing occasional longer runs.

The single educational anchor is **Michael A. Nielsen and Isaac L. Chuang,
*Quantum Computation and Quantum Information*, 10th Anniversary Edition
(Cambridge University Press, 2010)**. The
[source bridge](NIELSEN_CHUANG_BRIDGE.md) identifies the relevant chapters,
translates the notation, and explains the additional ideas needed here.

## A connected route

Start with the [bridge](NIELSEN_CHUANG_BRIDGE.md) for the physical question and
the relation between textbook foundations and this project. Then use the
[30-milestone map](MILESTONES.md) to connect individual concepts into the full
argument. Its 12 background/preliminaries milestones build the framework; its
18 narrative/innovation milestones develop the converse, construction and
stopping-time consequences. Each milestone records an understanding target,
dependencies, a conceptual connection and source pointers.

The map gives a shared route through the scientific story. Detailed derivations
remain in the linked science pages, so it is possible to follow the argument
conceptually and return to a specialist proof when needed.

| Question | Direct scientific source |
|---|---|
| What is unknown, what time is charged, and which output is accurate? | [Model and statements](../science/model.md) |
| Why can controls and measurements not remove the deadline cost? | [Analytic responses](../science/analytic_response.md) and [deadline bound](../science/deadline_bound.md) |
| How is the upper bound physically realized? | [Ramsey coins](../science/thermal_coin.md) and [finite controls](../science/finite_controls.md) |
| How can exact output have finite mean time? | [Stopping times](../science/stopping_time.md) |
| Which distinctions matter when interpreting the result? | [Interpretation](../science/interpretation.md) |

The textbook supplies the quantum foundations. The bridge and canonical proofs
supply the parameter-analytic and approximation arguments. The analytic
coin-simulation theorem is a separately attributed research ingredient from
[Nacu and Peres](../references/RELATED_WORK.md#nacu-peres-analytic-coin-simulation).
It is not an additional educational anchor or a theorem attributed to the textbook.

For the complete source map, see the [scientific reading route](../science/README.md)
and the [LLM reading guide](../llms.txt).
