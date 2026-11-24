---
created: 2026-11-24
type: causal-structure-and-final-state
status: machine-checked-human-scientific-review-pending
---

# Global causal structure, final state and outgoing radiation

This document records the results added on 2026-11-24 after [19](19-global-structure.md). They are Sections 5 and 6 of the [manuscript](manuscript/ads2-rst-one-sided-flux.pdf). Notation as in document 19: `Fhat = (Omega - Omega_s)/L`, `mu > 0`, onset at `x = 0`, `y = -x_m`, `Q = P_+/lambda^2` the cumulative incoming flux, `E_tot = sup Q`.

## 1. Two-sided flux

Let both chiral sectors carry nonnegative classical flux after onset, with cumulative functions `Q_+`, `Q_-` and `A_pm(x) = int_0^x Q_pm`. Then

$$\widehat F=\mu-x_px_m+a(x_p)+a(x_m)-A_+(x_p)-A_-(x_m).$$

The formula is symmetric under exchange of the two sectors. In the mixed sector `A_-` vanishes, so the total-flux criterion of document 19 is unchanged. In the mirror sector the same criterion holds for the ingoing ray `x_p = -y'` with `Q_-`: capture iff `y' < E_-`.

Lean: `Fhat2`, `Fhat2_symm`, `Fhat2_eq_Fhat`, `Fhat2_pre`, `Fhat2_mixed`, `mirror_hit_iff`. Script: `structure_checks.py` checks F1 and F4.

## 2. The singular set is a future set

**Theorem.** Let `Q_pm` be monotone with `Q_pm(0) >= 0` and `mu > 0`. If `Fhat(x_1, z_1) <= 0`, `x_1 <= x_2`, `z_1 <= z_2` and the two points differ, then `Fhat(x_2, z_2) < 0`.

Consequences:

1. `{Fhat > 0}` is a past set, connected, and contains the wormhole region. It is the spacetime.
2. No two distinct points of the critical curve are causally related. The curve is a strictly decreasing graph in null coordinates, spacelike where differentiable, with both null derivatives of `Fhat` negative on it.
3. No causal curve leaves the critical curve into the spacetime. No boundary condition at the singularity is needed, for any nonnegative flux profile in either sector, including impulsive shells.
4. When `E_pm < infinity`, the event horizons are `x_m = -E_+` and `x_p = -E_-`. If either total flux is infinite, the corresponding side has no finite horizon line of this form. The region `x_m >= -E_+`, `x_p >= -E_-`, from which neither future infinity can be reached, contains the throat points with static time `t >= -min(E_+, E_-)`.

**Why this matters.** In the evaporating black holes of the RST paper the critical curve turns timelike and naked at the endpoint of evaporation, and the solution beyond depends on a boundary condition imposed there. On the Kim-Son state this never happens. The reason is that the state to the future of the switch-off is the equilibrium one (`t_pm = 0`) and the classical flux is nonnegative, so nothing can raise `Fhat` along a future null direction once it has reached zero. The exact solution is therefore fixed by the data on the past null boundaries, with nothing to be supplied at the singularity. This says nothing about data beyond the null AdS2 ends of document 19. The price is that the black hole does not evaporate (section 5).

**Credit.** That the singularity formed by positive-energy infall is spacelike is standard in the classical CGHS model. The statement here is the corresponding one for the full semiclassical solution on this state, with two-sided flux and atoms.

**Traversability.** Outgoing rays start at the left AdS2 end, cross the throat at static time `t = -y` and, when `E_+ < infinity`, reach right future infinity iff `y > E_+`; the ray `y = E_+` is the horizon generator. If `E_+ = infinity`, every mixed outgoing ray is captured and no finite horizon line of this form exists. With no matter the traversing rays are those crossing the throat before `t = 0`. Infalling matter advances this by exactly `E_+ = P_+(infinity)/lambda^2` in static time, whatever its profile.

Lean: `singular_future`, `regular_past` (past-set property), `critical_curve_achronal` (first sentence of consequence 2), `Fhat2_neg_after_p`. Connectedness, the derivative statements, consequence 3 and the horizon sentences of consequence 4 are paper arguments. The Lean theorem is an order statement on the Kruskal plane; that the causal order of the spacetime is the coordinate order is the standard conformal-gauge fact and is not formalized. Script: checks F2 (about 12,000 random causally related point pairs, two-sided fluxes with atoms, zero violations) and F3.

## 3. Final exterior and the mass formula

Assume one-sided flux that ends: `Q = E_tot` for `x >= s`. Let `m_1 = int_0^s (E_tot - Q) = int x dQ = M_infinity/lambda^3`. For `x_p >= s`, `x_m <= 0`:

$$\widehat F=\mu_f+\tfrac12\tilde y^2+\tilde y\,\tilde x_p,\qquad \tilde y=y-E_{\rm tot},\quad \tilde x_p=x_p+E_{\rm tot},\quad \mu_f=\mu+m_1+\tfrac12E_{\rm tot}^2 .$$

In the exterior `x_m <= -E_tot` this is the zero-flux Kim-Son solution with `mu -> mu_f` in shifted Kruskal coordinates. In the RST normalization of the mass parameter,

$$\Delta M_{\rm BH}=M_\infty+\frac{P_+(\infty)^2}{2\lambda}.$$

The first term is the classical mass function of RST and Thorlacius. The second is specific to the Kim-Son state: the matter moves the horizon into the region where the outgoing boundary function is still on. For the Kim-Son impulsive shell `mu_f = mu + alpha^2/2`.

Limits of the statement: the identification holds in the exterior only (inside the horizon the two solutions differ by `ytilde^2/2`), and "mass parameter" means the constant in `Omega`. It is not claimed to be an ADM or Bondi energy.

Lean: normalized late-time identities and `m_1 >= 0` (`Fray_late`, `late_exterior_eq_zero_flux`, `first_moment_nonneg`). The physical mass normalization is a paper argument. Script: G1 to G3.

## 4. Monotonicity along the horizons

`Fhat`, hence `Omega` and `e^{-2 phi}`, is nondecreasing to the future along the event horizon, where `Fhat = mu + E_tot^2/2 + int_0^x (E_tot - Q)` rises to `mu_f`. It is also nondecreasing with increasing `x_p` along the apparent horizon `x_m = -Q(x_p)`; that curve is spacelike where `Q` increases, so this is an outward statement, not one about time evolution. Since `e^{-2 phi}` plays the role of the area in dilaton gravity, the event-horizon statement has the form of an area theorem. No entropy is attached to it here.

Lean: `Fhat` monotonicity only (`event_horizon_mono`, `apparent_horizon_mono`); the conversion to `Omega` and `e^{-2 phi}` is a paper argument. Script: G4.

## 5. Outgoing radiation at right future infinity

For every nonnegative one-sided flux with `E_tot < infinity` and each escaping ray `y > E_tot`, along that ray as `x_p -> infinity`,

$$\langle T_{--}\rangle\to-\lambda^2+\frac{\kappa}{4(y-E_{\rm tot})^2},\qquad \langle T_{\sigma^-\sigma^-}\rangle\to\frac{\kappa\lambda^2}{4}-\lambda^4e^{-2\lambda\sigma^-}.$$

The first form is Kim and Son's expression for the impulsive shell with `A/lambda^2` replaced by `E_tot`; they already note that the `-lambda^2` term is the background of the wormhole state and not radiation. What is added is the extension to every one-sided nonnegative flux with `E_tot < infinity` and the asymptotic-frame form. After the `E_tot`-dependent coordinate shift, the profile is matter-independent: the Hawking flux of the model, here the outgoing half of the equilibrium state, minus a negative background transient inherited from the wormhole state. The non-decaying equilibrium state supplies incoming thermal flux, so the black hole does not evaporate.

Paper argument plus script (G5, G6). Not formalized.

## 6. Affine length, now with explicit bounds

For every `kappa > 0` on the weak branch,

$$\frac\kappa4+\lambda^2\widehat F\le e^{-2\phi}\le2\sqrt\kappa\,\Omega+\frac\kappa2\Bigl(\ln\frac\kappa2-1\Bigr).$$

Hence `e^{2 rho} <= 1/(lambda^2 Fhat)`, and the affine parameter along a pre-onset null ray beyond coordinate separation 1 is at most `2/lambda^2`. The upper bound gives divergence of the affine parameter at the future end.

Lean: `weak_branch_lower'`, `weak_branch_upper`, `affine_finite_of_quadratic`, `ads_end_affine_finite`, `affine_infinite_of_linear`, `future_end_affine_infinite`. These theorems take the branch function `u = e^{-2 phi}` along the ray as a hypothesis (continuous, at least `kappa/4`, satisfying the defining relation). Its existence, the Lambert-W inversion, is not constructed in Lean. Script: H1, H2.

## 7. Open problems

1. **Evaporating version.** Switch the state to the future vacuum `t = 1/(4 x^2)` instead of `t = 0`. The effective flux is then not monotone, the theorem of section 2 does not apply, and a timelike critical curve with a boundary condition is expected. This is the natural next problem and the one closest to current interest in wormhole and black-hole evaporation.
2. **Entropy.** A generalized-entropy or island computation on this background, and whether section 4 extends to it.
3. **Energy.** Whether `mu_f` is a physical energy at the future end, given the non-decaying flux.
4. **The state.** Hadamard admissibility of the step-function boundary functions.
5. **The ends.** Any extension beyond the null AdS2 ends.
6. **Formalization.** Existence and continuity of the weak branch in Lean; the reduction of the RST action to the Kruskal-gauge equations.

## 8. Novelty

The bounded search described in document 19 predates these results. They were checked only against the sources already collected for it (Kim-Son, RST, CGHS, Thorlacius, Strominger and the others cited in the manuscript), where sections 2 to 4 were not found stated for this solution; no new search was run. Section 2 and the first term of the mass formula extend standard classical results, and the Kruskal-frame formula of section 5 is Kim and Son's for the shell. No priority is claimed. Human scientific review is pending.

[Back to index](00-index.md)
