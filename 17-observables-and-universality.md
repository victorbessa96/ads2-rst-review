---
created: 2026-11-24
type: observables-and-universality
---

# Observables and the exact universality boundary

## 1. Free-scalar two-point functions do not automatically see the wall

For a free conformal scalar in a conformal vacuum, the Wightman function has the standard null-coordinate logarithmic form, up to the usual normalization and `i epsilon` prescription:

$$G(x,x')=-\frac1{4\pi}\ln\big[(x_p-x_p')(x_m-x_m')-i\epsilon\big].$$

Conformal invariance removes the explicit metric conformal factor from this coordinate expression. On a fixed mixed ray `x_m=-y`, before the wall, distinct points therefore produce no universal term involving `Omega_s` or `x_hit(y)`.

The wall appears only through **domain truncation**: the point `x_p=x_hit(y)` is the endpoint of the allowed region. There is no automatic singular-wall signature in the free conformal-vacuum two-point function beyond that truncation.

**Verdict.** A distinctive boundary or holographic wall signature is not automatic. It requires a specified quantum state, boundary trajectory, and possibly nonconformal or interacting matter. The free conformal vacuum is insufficient.

## 2. Incoming energy and information are not outgoing observables

For the explicit scalar realization, `f=f_+(x_p)` before any boundary response, so `T_{--}=0` in the incoming sector. There is no outgoing scalar energy flux to read as a recovery signal before the first reflection or bath interaction.

The incoming packet reaches the singular edge in the wall-forming cases, but this does not by itself answer information recovery. A recovery statement requires the outgoing `f_-`, the boundary condition, and a definition of the asymptotic observer.

Consequently:

- `T_{--}=0` pre-reflection is an exact statement, not evidence of information loss.
- Domain truncation is an exact geometric statement, not a boundary entropy formula.
- Entanglement entropy, islands, and generalized entropy require additional state and subsystem data.

## 3. Sufficient structure for a generalized chiral focusing theorem

The accumulated-excess theorem is not tied to a particular pulse shape, but it does depend on a precise gravitational structure.

Suppose a two-dimensional model admits a chiral scalar `Omega` satisfying

$$\partial_+\partial_-\Omega=-L,\qquad \Omega=-Lx_px_m+a_+(x_p)+a_-(x_m),$$

with a scalar singularity condition `Omega=Omega_s` and the same pre-onset matching conventions. Define the normalized excess by subtracting `Omega_s` and scaling by `lambda^2/sqrt(kappa)`. Then the entire cumulative and signed-net-focusing analysis follows verbatim:

- Nonnegative sources give concavity and the total-flux criterion.
- Signed sources give `F=C-A_y` and the exact finite-hit criterion.
- One-sided derivative signs determine the causal class.
- State functions enter through `Q_eff`.

This is a genuine model-class theorem for **RST-like chiral systems**, not merely a collection of Kim-Son examples.

## 4. Why generalized dilaton gravity does not inherit it automatically

For the general action

$$S=\int d^2x\sqrt{-g}\left[XR+U(X)(\nabla X)^2+V(X)\right]+S_m,$$

the field equations do not generally yield a linear chiral `Omega` with `partial_+partial_-\Omega=-L`. The mixed derivative is generally nonlinear and potential-dependent. The singularity condition also need not be a fixed `Omega_s` with finite conformal factor.

Therefore the exact accumulated-excess formula does not follow without additional structure. A generalized theorem must identify a mass or focusing function obeying an analogous integrable first-order equation.

## 5. Pure JT is a counterexample to naive transplantation

Pure JT has different dilaton and boundary dynamics and does not possess the RST `Omega_s` edge used here. The RST cumulative theorem therefore cannot be quoted as a JT theorem. This is consistent with the original motivation: the RST edge is what makes the present wall calculation possible.

CGHS-like models require the same test explicitly: find the chiral variable, its mixed equation, and the singular threshold before claiming the cumulative criterion.

## 6. Final universality verdict

| Claim | Status |
|---|---|
| Exact criterion for RST-like linear chiral systems | Proved by the same derivation |
| Cumulative theorem for arbitrary dilaton potentials | False as a general claim; the required structure is absent |
| Automatic JT analogue | Not established and structurally unsupported |
| Universal free-scalar two-point wall signature | Not present |
| Boundary entropy/island signature | Requires a new, explicitly defined quantum/boundary model |

The strongest honest universality statement is the chiral-system theorem above. Anything broader must be derived from the generalized field equations, not inferred from the success of RST.

[Back to index](00-index.md) · [Matter realization](16-conformal-matter-realization.md) · [Breakthrough program](13-breakthrough-program.md).
