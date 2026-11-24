---
created: 2026-11-24
type: conformal-matter-realization
---

# Explicit conformal-matter realization of the injection

## 1. RST-normalized stress tensor and conservation

Use a free conformal scalar in two dimensions. The source convention is fixed by Kim-Son, not guessed from a different Hilbert-stress normalization. Their constraint and matter solution use

$$T^f_{++}=\frac12\sum_i[\partial_+f_i]^2,\qquad T^f_{--}=\frac12\sum_i[\partial_-f_i]^2,$$

and their conformal action contains `1/2 sum_i partial_+f_i partial_-f_i` (source TeX lines 121-131). This package adopts exactly that source coefficient. It does not claim that the canonical stress derived from an independently normalized action has the same overall factor; any such overall factor can be absorbed into `mathcal P`.

For one left-moving profile `f=f(x_p)`, therefore,

$$T^f_{++}=\frac12[f'(x_p)]^2,\qquad T^f_{--}=0,\qquad \partial_+\partial_-f=0.$$

The matter equation implies conservation directly:

$$\partial_-T^f_{++}=f'\partial_+\partial_-f=0.$$

Conversely, any nonnegative locally integrable `T_{++}` can be realized by

$$\boxed{f'(x)=\sqrt{2T_{++}(x)}.}$$

With several scalars, sum their squared derivatives. For a measure-valued source, use smooth wavepackets converging to the measure in the distributional limit. Thus the nonnegative source class is not physically empty or artificially restricted to a convenient stress ansatz.

## 2. Exact scalar wavepacket for the finite-sigma pulse

For the pulse in [Finite logarithmic-null injection](15-physical-boundary-injection.md),

$$T_{++}(x)=\frac{\mathcal P}{\lambda^2x^2}\mathbf 1_{[a,b]},$$

choose

$$f'(x)=\frac{\sqrt{2\mathcal P}}{\lambda x}\mathbf 1_{[a,b]}.$$

A continuous wavepacket is

$$\boxed{f(x)=\begin{cases}
0,&0<x<a,\\[2pt]
\dfrac{\sqrt{2\mathcal P}}{\lambda}\ln\dfrac xa,&a\le x\le b,\\[6pt]
\dfrac{\sqrt{2\mathcal P}}{\lambda}\ln\dfrac ba,&x>b.
\end{cases}}$$

It satisfies `partial_+partial_-f=0` away from the pulse endpoints, has derivative jumps there, and produces exactly

$$T^f_{++}=\frac{\mathcal P}{\lambda^2x^2}\mathbf 1_{[a,b]}.$$

The integrated incoming `sigma`-coordinate flux is finite:

$$E_{\mathrm{in}}=\mathcal P(\sigma_b-\sigma_a)=\frac{\mathcal P}{\lambda}\ln\frac ba.$$

Therefore the closing-window law and the no-energy-only-threshold corollary apply to an explicit conserved free-field wavepacket, not merely to an externally inserted stress tensor.

## 3. Backreaction is included by the chiral solution

The scalar stress enters the same Kim-Son constraint used throughout the package:

$$a_+''=\sqrt\kappa t_+-\frac{T^f_{++}}{\sqrt\kappa}.$$

Substituting the wavepacket stress gives the finite-sigma cumulative function and its exact wall criterion. The gravitational backreaction is therefore included in the fixed RST chiral solution; the source is now also tied to an explicit matter field.

The quantum anomaly/state function `t_+` is additional data. The classical scalar construction does not choose or justify a quantum state, and it does not remove the state-pulse phase boundary proved in [State-pulse phase diagram](14-state-pulse-phase-diagram.md).

## 4. Reflecting boundaries and baths: exact domain-of-dependence statement

The free-field general solution is

$$f(x_p,x_m)=f_+(x_p)+f_-(x_m).$$

Before any boundary response, `f_+` fixes the incoming `T_{++}` and `f_-` fixes the outgoing `T_{--}` independently.

- A reflecting boundary imposes a relation between `f_-` and `f_+` at the boundary.
- A bath or transparent boundary imposes a different outgoing/bath condition and an energy-balance equation.

Those relations affect the outgoing sector after the boundary interaction. They cannot change an incoming-wall hit lying in the causal past of the first reflection. Consequently:

1. The incoming-sector wall theorem is unchanged before the first boundary reflection.
2. Repeated reflection and bath transmission require a specified boundary trajectory and outgoing solution; they are not computed by the incoming theorem.
3. Energy recovery, entropy, and post-bath causal structure must be calculated from `f_-` and the boundary model, not inferred from `f_+` alone.

This is the precise self-consistency boundary of the present result. The matter realization and backreacted incoming solution are complete; a full reflecting/bath history is a separate boundary-value problem.

## 5. What is now closed

- The finite-sigma source is produced by an explicit conserved conformal scalar.
- Its gravitational backreaction is included in the fixed RST chiral solution.
- Its null-coordinate energy and focusing moment are distinct and exactly related.
- The same outgoing null ray in the fixed Kruskal chart can be inside the early-pulse window and outside the late-pulse window.
- Later reflection or bath coupling cannot retroactively alter a pre-reflection hit.

What remains genuinely new work is a specified post-boundary history and its quantum-information observables, not a hidden inconsistency in the incoming model.

[Back to index](00-index.md) · [Finite logarithmic-null injection](15-physical-boundary-injection.md) · [Observables and universality](17-observables-and-universality.md).
