---
created: 2026-11-24
type: ambitious-research-program
---

# From exact wall formulas to a genuine breakthrough

## 1. The target

The present package proves a fixed-state, prescribed-source classification. A genuine breakthrough requires answering a physical question that survives changes of coordinates and source conventions:

> Can finite, physically normalized energy destroy a semiclassical AdS2 wormhole, and what determines the boundary between regular evolution and singular termination?

The flagship theorem should not be another positive-pulse example. It should determine a necessary-and-sufficient physical termination criterion for a self-consistent matter/boundary system, or prove that no universal threshold exists and identify exactly why.

## 1.1 Completed hunts

The commissioned full-territory pass has now produced:

- [State-pulse phase diagram](14-state-pulse-phase-diagram.md): exact `p=q` boundary and same-energy/different-outcome example.
- [Finite logarithmic-null injection](15-physical-boundary-injection.md): exact pulse solutions and a retarded closing-window law; no threshold depending only on injected energy determines the window.
- [Conformal matter realization](16-conformal-matter-realization.md): an explicit conserved scalar wavepacket with backreaction.
- [Observables and universality](17-observables-and-universality.md): no automatic free-scalar wall signature and a precise RST-like universality boundary.
- [Research disposition](18-close-out.md): completed results and the remaining external/new-program gates.

## 2. Project A: signed, state-dependent net focusing

**Objective.** Turn the accumulated-excess formula into the general mathematical engine for signed classical and quantum-state sources.

**Completed foundation.** [Signed net focusing](12-signed-net-focusing.md) gives the exact criterion

$$F=C-A_y,\qquad \text{finite hit}\iff\exists x:A_y(x)\ge C,$$

with tangential-contact, causal-sign, multiplicity, and generalized-horizon caveats proved explicitly.

**Next proof obligations.**

1. Characterize when a degenerate root is a termination by the first nonzero one-sided jet.
2. Derive conditions for exactly one root, finitely many roots, and root accumulation.
3. Classify admissible `t_+` data rather than treating every signed function as a physical quantum state.
4. Map the boundary between regular evolution, horizon formation without termination, spacelike termination, and nonmonotonic contact.
5. Formalize the abstract continuous accumulated-excess theorem in Lean, then the nondecreasing special case.

**Acceptance test.** An adversary must be able to insert sign changes, atoms, derivative jumps, and unattained suprema without breaking the theorem statement.

## 3. Project B: physical boundary injection

**Objective.** Replace a convenient Kruskal profile with energy prescribed on a specified boundary trajectory.

Let `x_p=f(u)` for a boundary null coordinate `u`. Then

$$T_{uu}=[f'(u)]^2T_{++}.$$

The cumulative focusing variable, not merely `int T_uu du`, must be computed and related to the injected energy. For monotonic `x_p=f(u)`, the classical identity is `E_focus=lambda^{-2}int T_uu/f'(u) du`. In the logarithmic case the exact termination band is the retarded closing window `u>u_*`, not an unweighted-energy criterion.

**Required results.**

1. Specify the boundary trajectory and normalization before choosing the source.
2. Solve finite boundary-time pulses and determine whether termination is controlled by energy, duration, timing, cumulative focusing, or state data.
3. Establish either an invariant critical-energy criterion or a theorem explaining why no universal criterion exists.
4. Prove the finite-sigma-support formula as the simplest coordinate-controlled case, without mistaking null time for observer proper time.
5. Derive the quantum-state transformation law before changing the state frame. `T_uu` transforms classically, but `t_+` generally has an anomalous Schwarzian contribution; the full effective source must not be treated as an ordinary weight-two tensor.

**Acceptance test.** Re-parameterize `u`. The physical conclusion must be invariant even when the coordinate expression of `Q_eff` changes.

## 4. Project C: self-consistent matter and boundary dynamics

**Objective.** Make the incoming stress tensor the output of an actual matter/boundary system.

**Minimum construction.**

- A conformal matter action with a specified initial state and wave packet.
- The RST semiclassical equations with backreaction.
- A reflecting AdS2 boundary or a transparent boundary coupled to a bath, including the boundary action and energy balance.
- A comparison of repeated reflection with transmission into the bath.

**Key question.** Does finite physical injection produce the singular termination predicted by the prescribed-source theorem, and does a nonzero critical energy exist?

**Acceptance test.** The stress tensor must satisfy the matter equations and conservation laws; it may not be inserted as an unconstrained convenient profile.

## 5. Project D: state-pulse phase diagram

**Objective.** Classify the same classical injection across admissible quantum states.

The proposed regimes are:

1. Regular evolution.
2. Apparent-horizon formation without mixed-ray termination.
3. Spacelike singular termination.
4. Nonmonotonic or tangential contact with signed net focusing.

**Required result.** A transition criterion expressed through state-dependent net focusing or a physical energy condition. A same-energy/different-outcome example would be especially strong.

**Acceptance test.** Every state must satisfy explicit admissibility conditions. Hybrid-state literature with wrong-sign fields must be labeled, not silently treated as physically equivalent.

## 6. Project E: boundary and quantum-information observables

**Objective.** Connect singular termination to something measurable outside the bulk wall equation.

Candidate observables:

- Boundary two-point functions.
- Energy recovery and transmission.
- Entanglement entropy and generalized entropy.
- Quantum extremal surfaces and islands.
- Reconstructability of the injected information.

**Acceptance test.** Compute a genuine boundary or information observable and demonstrate a transition tied to the wall criterion. Geometry alone is not enough for a holographic breakthrough.

## 7. Project F: universality beyond RST

**Objective.** Determine whether cumulative focusing is special to RST or an instance of a broader dilaton-gravity mechanism.

Compare RST, CGHS, JT, and generalized dilaton gravity with potentials `U(X)` and `V(X)`. Identify which structures supply an exactly integrable focusing variable and which require new mass-function or critical-dilaton conditions.

**Acceptance test.** Prove a theorem for a nontrivial model class, or delimit precisely why the RST result is non-universal.

## 8. The ambitious but disciplined sequence

1. Finish the signed-net-focusing theorem and abstract Lean existence proof.
2. Solve finite boundary-time injection with an explicit trajectory.
3. Construct one self-consistent matter/boundary example.
4. Produce the state-pulse phase diagram.
5. Attach a boundary or entanglement observable.
6. Test universality beyond RST.

This order moves from tractable mathematics to physical mechanism to wider significance. It avoids spending the next wave on more checks or more positive-pulse examples.

## 9. What would count as a breakthrough

| Level | Required result |
|---|---|
| Mathematical breakthrough | Necessary-and-sufficient termination theory for signed, state-dependent focusing, including causal and multiplicity classification |
| Physical breakthrough | Coordinate-invariant critical-energy or no-universal-threshold theorem for finite boundary injection |
| Gravitational breakthrough | Self-consistent matter/boundary solution showing when semiclassical AdS2 wormholes terminate |
| Holographic breakthrough | New boundary or quantum-information signature of singular termination |
| Universality breakthrough | A proven focusing criterion across a meaningful class of dilaton-gravity models |

The strongest current path is the second and third rows together: a finite-energy, self-consistent boundary-injection theorem with an explicit state-dependence map.

## 10. Non-negotiable proof discipline

- State the function class, matching side, and one-sided derivative conventions before integrating.
- Never replace `exists x:A_y(x)>=C` by an unattained-supremum shortcut.
- Distinguish roots from termination roots.
- Distinguish apparent horizons from generalized level crossings at atoms.
- Treat signed sources without claiming monotonicity, uniqueness, or strict horizon precedence.
- Separate null-coordinate duration from observer proper time.
- Keep physical state admissibility and boundary dynamics explicit.
- Formalize the abstract theorem before claiming machine assurance for the physical model.
- Obtain independent human re-derivation before calling the result externally validated.

[Back to index](00-index.md) · [Signed net focusing](12-signed-net-focusing.md).
