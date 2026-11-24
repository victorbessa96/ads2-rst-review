---
created: 2026-11-24
type: signed-net-focusing-theorem
---

# Signed net focusing, first hits, and finite-sigma pulses

## 1. Effective source and exact accumulated-excess form

Retain the same pre-onset branch and matching conventions, but allow signed state and classical contributions. Define

$$S_{\mathrm{eff}}(x)=T^f_{++}(x)-\kappa t_+(x),$$

so the chiral constraint is

$$a_+''=-\frac{S_{\mathrm{eff}}}{\sqrt\kappa}.$$

More generally, allow a signed Radon measure `dS` of locally finite total variation. Define

$$Q_{\mathrm{eff}}(x)=\frac1{\lambda^2}\int_{[0,x]}dS(u).$$

The pre-onset matching conditions are `a_+(0)=B` and `a_+'(0^-)=0`. An onset atom produces a derivative jump, not a violation of the pre-onset condition.

On a mixed outgoing ray `x_m=-y`, integration by parts gives the exact form

$$\boxed{F(x,y)=\mu+\frac{y^2}{2}+\int_0^x[y-Q_{\mathrm{eff}}(s)]\,ds.}$$

Define

$$C(y)=\mu+\frac{y^2}{2}>0,\qquad A_y(x)=\int_0^x[Q_{\mathrm{eff}}(s)-y]\,ds.$$

Then

$$F(x,y)=C(y)-A_y(x),\qquad A_y(0)=0<C(y).$$

For a signed Radon measure, `Q_eff` has locally bounded variation and `A_y` is continuous. For a locally integrable density, `A_y` is absolutely continuous and `A_y'=Q_eff-y` almost everywhere.

## 2. Necessary and sufficient first-hit criterion

**Theorem 1: exact finite-hit criterion.** A finite positive first hit exists if and only if

$$\boxed{\exists x>0\quad A_y(x)\ge C(y).}$$

Equivalently, let `M_y=sup_{x>=0}A_y(x)`. A finite hit exists iff either `M_y>C(y)`, or `M_y=C(y)` and the supremum is attained at finite `x`.

When the set is nonempty, the first hit is

$$x_{\mathrm{hit}}=\min\{x>0:A_y(x)\ge C(y)\},$$

and it satisfies `A_y(x_hit)=C(y)` and `A_y(x)<C(y)` for `0<=x<x_hit`.

### Proof

If some `x>0` has `A_y(x)>=C(y)`, continuity and `A_y(0)=0<C(y)` give an intermediate point with `A_y=C(y)`. The first such point exists because the set is closed and bounded below. Conversely, a finite zero of `F=C-A_y` is precisely a point with `A_y=C(y)`.

If `M_y>C(y)`, some finite point exceeds the threshold, so the first case applies. If `M_y=C(y)` and the supremum is attained, that point is a hit. If `M_y<C(y)`, or if `M_y=C(y)` is approached only asymptotically and never attained, no finite point reaches the threshold. ∎

**Boundary-case warning.** `sup A_y>=C(y)` alone is not sufficient when equality holds only as an unattained limit. The direct criterion `exists x:A_y(x)>=C(y)` is the safe formulation.

## 3. First contact, termination, and formal later roots

Three objects must be distinguished:

| Object | Exact meaning |
|---|---|
| **First contact** | The first `x>0` with `F(x,y)=0`, hence `Omega=Omega_s` and the RST curvature edge is reached |
| **Termination root** | A first contact with `F<0` on a right neighborhood, so the regular physical branch is excluded immediately afterward |
| **Formal later root** | A zero of the algebraic continuation after the first contact; it is not a physical wall or reconnection unless a continuation through the first edge is separately established |

A zero of `F` is always an RST edge contact. It need not terminate the regular domain. Define a **termination root** as a first root for which some `epsilon>0` satisfies

$$F(x,y)<0\qquad\text{for }x_{\mathrm{hit}}<x<x_{\mathrm{hit}}+\epsilon.$$

This is the exact physical-side exclusion condition. A root with `F>=0` on both sides is still an **RST singular-edge contact**, not an absence of singular behavior. Its status may be an isolated curvature singularity, an endpoint of the physical branch, or a point requiring a specified continuation. The accumulated-excess formula alone does not decide that continuation.

At a first root, the left derivative necessarily obeys

$$D_-F(x_{\mathrm{hit}})\le0,$$

because `F>0` immediately before the first root and `F(x_hit)=0`. The right derivative can be negative, zero, or positive for signed sources.

Using `F_y=x+y>0` and `x_m=-y`, the one-sided wall slopes are

$$\left.\frac{dx_m}{dx_p}\right|_\pm=\frac{D_\pm F(x_{\mathrm{hit}})}{x_{\mathrm{hit}}+y}.$$

Consequently:

| One-sided derivative | Wall tangent in `ds^2=-e^{2rho}dx_pdx_m` |
|---|---|
| `D F<0` | Spacelike |
| `D F=0` | Null to first order |
| `D F>0` | Timelike |

A termination root cannot have `D_+F>0`. If `D_+F<0`, the outgoing wall is spacelike. If `D_+F=0`, the next nonzero right-hand jet, or a direct right-neighborhood sign test, decides whether the root is a null-tangent termination or a singular contact without right-side exclusion. A cusp with `D_-F<0<D_+F` has a spacelike incoming branch and a timelike outgoing branch and is not a termination.

**First-jet lemma.** Suppose `F(x_hit)=0`, `D_+F(x_hit)=0` up to order `n-1`, and the first nonzero right derivative has order `n>=2`. Then `D_+^nF<0` gives `F<0` on a right neighborhood, hence termination; `D_+^nF>0` gives `F>0` on a right neighborhood, hence no termination. This follows immediately from the one-sided Taylor expansion with `o((x-x_hit)^n)`. The first-order case is the same statement with `n=1`. If every derivative vanishes but `F` is not identically zero on a right neighborhood, the direct right-neighborhood sign test is still the exact criterion.

For nonnegative `Q_eff`, monotonicity forces `D_+F(x_hit)<0`, recovering the original spacelike termination theorem. Without monotonicity, no such universal causal conclusion is valid.

## 4. Multiplicity and sign alternation

Signed effective focusing permits multiple roots of `A_y=C(y)`. There is no general uniqueness theorem. Between consecutive roots, the sign of `F` can alternate, producing regular and excluded intervals. After the first singular contact, these are intervals of a **formal algebraic continuation**, not evidence of physical wall reconnections. A physical continuation through `Omega_s` must be established independently.

If `F` is real analytic on an interval and not identically zero there, its roots cannot accumulate at an interior point; on a closed bounded interval they are finite. Without analyticity, infinitely many roots and root accumulation are allowed. Thus uniqueness requires extra structure, but the accumulated-excess criterion itself remains valid without it.

A complete classification is therefore:

1. Find the ordered level set `A_y=C(y)`.
2. On each interval between roots, determine the sign of `F`.
3. At each root, evaluate both one-sided derivatives or, at a degenerate derivative, the next nonzero jet.
4. Call a root a termination only when the physical side ends there: `F<0` on a right neighborhood.

This is stronger and more honest than claiming that signed total flux alone determines a unique wall.

## 5. Generalized trapping boundary

The pre-onset value is `Q_eff(0^-)=0<y`. In general,

$$\frac{\partial_+\Omega}{L}=y-Q_{\mathrm{eff}}(x)=D F(x).$$

When `Q_eff` is continuous, the ordinary apparent-horizon equation is `Q_eff(x)=y`. For measure-valued sources, use one-sided measure limits and call the first level crossing a generalized trapping-boundary crossing.

An onset atom `dS=A delta_0` gives `Q_eff(0^+)=A/lambda^2`, not zero. Therefore:

1. If `Q_eff(0^+)>=y`, the generalized trapping-boundary crossing is at onset, `x=0`.
2. If `Q_eff(0^+)<y` and a later first root has `Q_eff(x_hit^-)>=y`, the first subsequent level crossing occurs at or before `x_hit`.
3. If `Q_eff(x_hit^-)>y`, that crossing is strictly earlier.

At any first root, `D_-F(x_hit)<=0` implies `Q_eff(x_hit^-)>=y`; no continuity assumption on `Q_eff` is needed for this one-sided statement. The initial condition used in the first-hit theorem is instead `A_y(0)=0`, because the `ds`-integral has zero length at onset. The atom affects the derivative, not `F(0)`.

**Scope warning.** Signed sources allow `Q_eff(x_hit^-)=y`, so strict horizon-before-wall ordering is not universal. The strict positive-source corollary survives because concavity forces the stronger inequality at the first root.

## 6. Finite logarithmic-null-support corollary

Let `x_p=e^{lambda sigma}` and prescribe a nonnegative source in the logarithmic null coordinate. Tensor transformation gives

$$T_{\sigma\sigma}=\lambda^2x_p^2T_{++},\qquad d\sigma=\frac{dx_p}{\lambda x_p}.$$

Therefore the total cumulative Kruskal flux is

$$\boxed{E_{\mathrm{tot}}=\frac1{\lambda^3}\int T_{\sigma\sigma}(\sigma)e^{-\lambda\sigma}\,d\sigma.}$$

For a finite constant-null-stress pulse

$$T_{\sigma\sigma}=\mathcal P\mathbf 1_{[\sigma_a,\sigma_b]},$$

set `x_a=e^{lambda sigma_a}` and `x_b=e^{lambda sigma_b}`. Then

$$T_{++}(x)=\frac{\mathcal P}{\lambda^2x^2}\mathbf 1_{[x_a,x_b]},$$

and

$$\boxed{E_{\mathrm{tot}}=\frac{\mathcal P}{\lambda^4}\left(\frac1{x_a}-\frac1{x_b}\right).}$$

The nonnegative cumulative-flux theorem therefore gives a unique mixed-ray hit exactly for

$$\boxed{0<y<E_{\mathrm{tot}}.}$$

This proves that finite support in the logarithmic null coordinate is already covered. It does not prove finite duration in the proper time of a timelike observer; `sigma` is a null coordinate, and a physically normalized boundary trajectory remains additional data.

## 7. Recovery of the earlier theorem

For nonnegative `S_eff`, `Q_eff` is nondecreasing, `F` is concave, and the first root is unique. If `E_tot=+infinity`, every finite `y>0` terminates. If `E_tot<+infinity`, termination occurs exactly for `0<y<E_tot`. The sustained, rectangular-pulse, impulsive, and finite-sigma-support cases follow as special cases.

## 8. Claim fence

- This is a theorem about the fixed RST chiral solution and prescribed `t_+`, not an arbitrary-quantum-state admissibility theorem.
- Signed effective focusing does not imply a unique wall, a spacelike wall at every root, or strict horizon precedence at every root.
- Every `F=0` contact reaches the RST edge. Tangential contact is not declared regular, and later algebraic roots are not physical reconnections without a separate continuation theorem.
- A physical boundary-energy threshold requires a specified boundary trajectory and stress normalization, not just a coordinate rename.
- Self-consistent matter, reflecting boundaries, baths, and quantum-information observables are separate dynamical problems.
- The Lean artifact proves the abstract intermediate-value core and algebraic controls, not the full signed-measure theory.

[Back to index](00-index.md) · [Nonnegative cumulative theorem](11-cumulative-flux-generalization.md) · [Breakthrough program](13-breakthrough-program.md).
