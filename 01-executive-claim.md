---
created: 2026-11-23
type: executive-claim-and-scope
---

# Executive claim and scope

> [!note] Reading note, 2026-11-24
> This document predates [19 Global structure](19-global-structure.md). Its formulas stand. Two points of reading change: (a) rays with `x_m > 0` reach the critical curve with no classical flux at all, so the theorems here concern which rays with `x_m < 0` are captured; (b) the cumulative criterion is the Kim-Son-state analogue of the RST/Thorlacius general-infall formula. In the table of section 5, "Proved" means derived on paper and, as of 2026-11-24, formalized in Lean where [lean/README.md](lean/README.md) says so; items 3 and 4 of section 1 (affine parameter, interior curves) are paper and numerical results only.

## 1. Contribution, narrowed to what is actually new

The contribution is not the first discovery of a singularity on a past-AdS2 RST branch. Kim-Son already has an impulsive positive-shock singularity, and the impulse already produces a spacelike wall on a restricted mixed-ray band.

The contribution is a family of exact, parameter-general termination theorems for sustained and finite one-sided classical flux on that fixed branch:

1. **Sustained every-ray theorem.** For every `p>0`, `mu>=0`, and fixed finite `y>0`, the mixed ray `x_m=-y` has a unique first `Omega_s` hit at
   $$x_{p,\mathrm{hit}}=\frac{y+\sqrt{(1+p)y^2+2p\mu}}{p}.$$
   The edge is spacelike.
2. **Horizon theorem.** The apparent-horizon coordinate on that ray is `x_{p,AH}=y/p`, strictly before the hit:
   $$x_{p,\mathrm{hit}}-x_{p,AH}=\frac{D}{p}>0.$$
3. **Null affine theorem.** The same ray reaches the edge at finite forward affine parameter.
4. **Interior-observer consistency control.** Every constant-`sigma_1` curve in the explicit interior chart is timelike and reaches the wall at finite `sigma_0` and finite proper time from any finite earlier coordinate. These are generally accelerated, already trapped interior curves, not an all-geodesics theorem.
5. **Finite-pulse theorem.** For a pulse with `E=p*x_s`, a wall exists exactly for `0<y<E`, remains spacelike through shutoff, and has an apparent-horizon precursor.

**State-equivalence corollary.** In the alternate `t_+`-on problem, replace `p` by `p_eff=1+p`. Its coefficient `(1-p_eff)/2` becomes `-p/2`, exactly the retained Kim-Son coefficient. Thus the retained `t_+` step-off supplies the critical `lambda^2` in that comparison: every `p>0` gives `p_eff>1`. The every-ray statement is therefore a state-specific equivalence, not a claim that arbitrary weak physical flux has no threshold.

6. **State-pulse phase diagram.** Constant post-onset state level `q` gives `r=p-q`: every-ray termination for `r>0`, no mixed-ray hit for `r<=0`. Identical classical flux gives different outcomes for `q=0` and `q=1`.
7. **Finite logarithmic-null injection.** For `y=e^{-lambda u}`, termination is exactly `u>u_*`, with `u_*=sigma_a-lambda^{-1}ln[(mathcal P/lambda^4)(1-e^{-lambda Delta sigma})]`. Moving the pulse translates the window; no threshold depending only on injected energy determines it.
8. **Matter realization and universality.** An explicit conserved conformal scalar produces the pulse and its backreaction. The theorem extends to linear chiral systems, not to arbitrary dilaton potentials or JT by analogy.

The main regular-wormhole statement uses `mu>0`. The `mu=0` limit is retained separately because the pre-onset geometry is already singular.

See [Sustained theorem](03-sustained-flux-theorem.md), [Horizon structure](04-horizon-and-causal-structure.md), and [Finite-pulse theorem](06-finite-pulse.md).

## 2. Exact review object

Let `lambda>0`, `kappa>0`, `P>0`, and `M>=0`. Retain the Kim-Son boundary functions

$$t_\pm=\frac{\lambda^2}{\kappa}\Theta(-x^\pm),$$

with onset shifted to `x_0=0`, and prescribe one-sided classical flux

$$T^f_{++}=P\Theta(x_p),\qquad T^f_{--}=0.$$

The phrase **constant flux** always means constant in Kruskal `x_p`. It is not a claim of constant stress measured by every asymptotic observer. For example, if `x_p=e^{lambda sigma}`, the transformed component is `T_{\sigma\sigma}=\lambda^2x_p^2P`, and the integrated coordinate stress up to `x_p` is

$$\int T_{\sigma\sigma}\,d\sigma=\frac{\lambda P x_p^2}{2}.$$

For small `p`, `x_hit~2y/p`, so this integral scales as `2 lambda^3 y^2/p` at the hit. The Kruskal-profile “no critical amplitude” statement therefore carries an observer-coordinate budget that grows as `p` weakens.

The solution is fixed by the pre-influx branch and `C^0/C^1` matching. Retaining these `t_pm` values is a quantum-state/boundary-data choice, not a uniqueness theorem under arbitrary admissible state functions.

## 3. Terminology that survives review

Use **spacelike RST singular termination behind an apparent horizon**. Do not use unqualified “AdS2 cannot absorb,” “AdS2 never piles up is false everywhere,” or “collector pileup” as the main description.

The older pure-JT statement is a different model claim. This calculation does not refute it. It also does not independently re-derive pure-JT immunity from the JT action.

## 4. What the new finite-pulse result closes

The finite-Kruskal-support pulse question is no longer an open hunt. This means compact support in Kruskal `x_p`, not finite duration in an observer-adapted time coordinate:

- during the pulse, the sustained solution applies by domain of dependence;
- after shutoff, the wall equation is linear in `x_p`;
- the complete existence criterion is `0<y<E`;
- the shutoff ray bound is
  $$y_{\max}=\sqrt{(1+p)x_s^2-2\mu}-x_s,$$
  so `0<y<y_max` gives a pre-shutoff hit;
- for `y>y_max` and `y<E`, the exact post-shutoff hit is
  $$x_{p,\mathrm{after}}=\frac{\mu+y^2/2+E x_s/2}{E-y}>x_s.$$
  At `y=y_max`, `x_{p,\mathrm{after}}=x_s`. If the `y_max` radicand is negative, the during-hit set is empty, but post-shutoff hits can still exist for `0<y<E`.

All wall branches and first derivatives match at `x_s`. The full formulas and degeneracies are in [Finite-pulse theorem](06-finite-pulse.md).

## 5. Binding claim fence

| Claim | Status |
|---|---|
| Finite `x_p` first hit on every specified sustained mixed ray | Proved |
| Spacelike edge behind an apparent horizon | Proved |
| Finite forward null affine parameter | Proved |
| Finite proper time on explicit interior constant-`sigma_1` curves | Proved |
| Finite-pulse wall exactly for `0<y<E` | Proved |
| Future-asymptotic observer hits at finite proper time | Not established; no such boundary observer is constructed |
| Arbitrary quantum-state or future-boundary response | Not established |
| Transparent or reflecting absorber theorem | Not established |
| All singular walls vanish for alternate `t_+` data when `p<=1` | False; only the mixed-ray hit is excluded there |
| Literature-wide priority | Not claimed |
| Black hole present at zero classical flux (both-positive quadrant) | Proved, Lean `zero_flux_wall_iff`; see document 19 |
| Timelike AdS boundary exists | False; the AdS2 ends are null at finite affine distance |
| External human peer review | Not performed |

## 6. Why this matters

Asymptotic AdS2 curvature does not determine the global dilaton-edge structure or its response to a prescribed source. The result identifies exactly which state data, source profile, and matching prescription produce the singular termination, and it distinguishes that mathematical fact from absorber, future-boundary, and publication-priority claims.

Next: [Primary source and derivation](02-source-and-derivation.md).
