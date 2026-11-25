---
created: 2026-11-24
type: global-structure-and-reframing
status: machine-checked-human-scientific-review-pending
---

# Global structure of the Kim-Son solution and what the flux results mean

This document records four structural facts found on 2026-11-24 while completing the formal proof. They do not invalidate any formula in documents 03 to 16. They change how those formulas should be read, and they take precedence over earlier wording wherever the two disagree. The manuscript in [manuscript/](manuscript/ads2-rst-one-sided-flux.tex) is written around them.

Notation: `L = lambda^2/sqrt(kappa)`, `mu = sqrt(kappa) M / lambda^3 > 0`, `Fhat = (Omega - Omega_s)/L`, onset at `x_0 = 0`, `y = -x_m`.

## 1. One formula for all four sectors

For the Kim-Son boundary functions `t_pm = (lambda^2/kappa) Theta(-x^pm)` and any nonnegative incoming flux with cumulative function `Q` and `A(x) = int_0^x Q`,

$$\widehat F(x_p,x_m)=\mu-x_px_m+a(x_p)+a(x_m)-A(x_p),\qquad a(x)=\tfrac12x^2\,\Theta(-x).$$

The four sector formulas of [02](02-source-and-derivation.md) are this expression restricted to each quadrant. It follows from the constraint `kappa t_pm = sqrt(kappa) d_pm^2 Omega + T_pm` by two integrations, with `a` the unique `C^1` solution of `a'' = Theta(-x)`, `a(0) = a'(0) = 0`.

Lean: `aState_hasDerivAt`, `aState_second_deriv_neg`, `aState_second_deriv_pos`, `Fhat_pre`, `Fhat_mixed`, `Fhat_post`, `Fhat_mirror`. Script: `structure_checks.py` group A, which also compares against the printed Kim-Son solution in every sector.

## 2. The black hole is present with no classical matter

Set the flux to zero. Then

$$\Omega=\underbrace{\Omega_s+L(\mu-x_px_m)}_{\text{eternal RST black hole, } t_\pm=0}+\frac L2\left[x_p^2\Theta(-x_p)+x_m^2\Theta(-x_m)\right].$$

The first term is the static `t_pm = 0` solution of the RST model, which RST and later authors identify as the black hole in equilibrium with thermal radiation (the Hartle-Hawking, or Kruskal-vacuum, state). Its mass parameter here is `M_BH/(lambda sqrt(kappa)) = Omega_s + M/lambda`.

Consequences:

1. In the quadrant `x_p > 0, x_m > 0` the solution is exactly that black hole's future interior. The critical curve is `x_p x_m = mu`, it is spacelike, and the quadrant is trapped (`d_+ Omega < 0` and `d_- Omega < 0`).
2. The pre-onset, mixed and mirror sectors are regular for zero flux: `Fhat >= mu > 0`.
3. If the boundary functions are not switched off, `Fhat = mu + (x_p - x_m)^2/2` everywhere and nothing is singular.

So the wormhole collapses because the state that supports it is switched off at `x^pm = 0`. Incoming matter is not needed. This zero-flux sector is already implicit in Kim and Son's equations; our contribution is its explicit identification and the unified global analysis, not a new geometry. Kim and Son's text attributes the black hole to the infalling shell; their own solution with `A = 0` has the same critical curve in the both-positive quadrant. The classical analogue is in Hayward, Kim and Lee (gr-qc/0110080), whose abstract states that the wormhole collapses into a black hole if the ghost field is turned off.

**Effect on earlier documents.** The headline "arbitrarily weak sustained flux terminates every ray" in [01](01-executive-claim.md) and [03](03-sustained-flux-theorem.md) is correct for mixed rays (`x_m < 0`), and should be read together with the fact that rays with `x_m > 0` terminate with no flux at all. What matter controls is which mixed rays are captured.

Lean: `zero_flux_wall_iff`, `zero_flux_wall_slope`, `zero_flux_trapped_plus`, `zero_flux_trapped_minus`, `wormhole_regular`, `zero_flux_mixed_regular`, `mirror_regular`, `eternal_wormhole_regular`. Script: group B.

## 3. The total-flux criterion is the Kim-Son version of a known formula

For classical dilaton gravity with general infalling matter, the apparent horizon is at `x^- = -P_+(x^+)/lambda^2` and the event horizon at `x^- = -P_+(infinity)/lambda^2`, where `P_+` is the cumulative Kruskal momentum of the matter (RST eqs. 4.1 to 4.4; Thorlacius hep-th/9411020 eqs. 13 to 18; Strominger hep-th/9501071 eqs. 3.71 to 3.72). In the notation of this package `Q = P_+/lambda^2`.

The cumulative theorem of [11](11-cumulative-flux-generalization.md) is the same statement on the Kim-Son state:

- a mixed ray `y` is captured iff `y < E_tot = sup Q`;
- the hit is unique and `Q > y` there, so the apparent horizon `x_m = -Q(x_p)` is crossed first;
- if `E_tot < infinity`, the line `x_m = -E_tot` is the event horizon of the right future region and rays with `y > E_tot` escape; if `E_tot = infinity`, every mixed outgoing ray is captured and no finite horizon line of this form exists.

What differs from the classical case: the extra `y^2/2` from the retained outgoing state, the offset `mu`, the critical value `Omega_s` in place of `e^{-2 phi} = 0`, and the fact that the proof needs only monotonicity of `Q` (atoms allowed, no density).

This must be credited whenever the criterion is presented. It is a careful extension, not a new mechanism.

Lean: `hit_iff`, `existsUnique_hit`, `Fray_neg_after`, `Fray_pos_before`, `Q_gt_of_Fray_nonpos`, `no_hit_of_le`, `finite_total_flux_hit_iff`, with the specializations `sustained_every_ray_hit`, `sustained_hit_is_xHit`, `impulse_hit_iff`. This closes the gap that the previous Lean file left open: the cumulative theorem itself is now formalized for arbitrary monotone `Q`.

## 4. Two clocks, two moments of the matter

A vector field preserving metric and dilaton has the form `xi = (a + c x_p) d_p + (b - c x_m) d_m` with `xi(Fhat) = 0`. At zero flux:

| Sector | Symmetry |
|---|---|
| pre-onset | translation `d_p + d_m` only |
| both-positive | boost `x_p d_p - x_m d_m` only |
| mixed | none |

So the static time of the wormhole is linear in `x^pm`. The logarithmic coordinate `sigma` (`x_p = e^{lambda sigma}`) is the natural time only at the future linear-dilaton end, where escaping rays see `e^{2 rho} lambda^2 (y - E_tot) x_p -> 1`, and in the both-positive quadrant.

Infalling matter has two moments, `P_+(infinity) = int dT_{++} = lambda^2 E_tot` and `M_infinity = lambda int x_p dT_{++} = int T_{sigma sigma} d sigma`. Capture is decided by the first alone.

**Effect on earlier documents.** The "closing-window law" and "no energy-only threshold" of [15](15-physical-boundary-injection.md), [16](16-conformal-matter-realization.md) and [18](18-close-out.md) are the statement that `M_infinity` does not determine `P_+(infinity)`: a `sigma`-frame pulse sent later has the same `M_infinity` and exponentially smaller `E_tot`. The formulas are correct. The wording "no threshold depending only on injected energy" is frame dependent, because in Kruskal variables the threshold `y < E_tot` depends on one integrated quantity only. The same remark applies to the "same-energy/different-outcome" example in [14](14-state-pulse-phase-diagram.md).

Lean: `symmetry_pre`, `symmetry_post`, `symmetry_mixed`. Script: group C.

## 5. The AdS2 ends are null-geodesically incomplete

Along a null ray toward the pre-onset ends `|x_p - x_m| -> infinity`:

- the affine parameter `int e^{2 rho} dx` converges (for `lambda = kappa = 1`: 2.4443 at `mu = 0.2`, 1.2913 at `mu = 2`, from the exact Lambert-W inversion);
- the curvature tends to `-4 lambda^2` and stays bounded;
- `e^{-2 phi}` diverges (weak coupling);
- proper distance along static slices diverges logarithmically.

The leading metric is `ds^2 ~ -2 dx^+ dx^- / (lambda^2 (x^+ - x^-)^2)`, Poincaré AdS2 with `z = (x^+ - x^-)/2`. The ends are at `z -> infinity`, the Poincaré-horizon side. The conformal boundary `z -> 0` would be the throat, where the geometry is not AdS2. The constructed patch has no timelike conformal boundary at these ends, and no extension is constructed. The numerical affine bound uses `d lambda = C e^{2 rho} dx` with `C=1`; constant affine rescaling changes the number but not finiteness.

**Effect on earlier documents.** Language about boundary injection, boundary observers, reflecting walls or baths ([13](13-breakthrough-program.md), [15](15-physical-boundary-injection.md), [17](17-observables-and-universality.md), [18](18-close-out.md) section 4) has no referent in this solution as it stands. Those programs first need an extension or a modified model. The title of document 15 was already qualified for this reason.

The future end is of the other kind: for `y > E_tot` it is a complete linear-dilaton region.

Lean: `OmegaCrit_le`, `conformal_factor_bound`, `Fray_ge_linear`, `Fray_le_linear`, `affine_tail_bounded`, `affine_future_unbounded`, and since the later update of the same day the conclusions themselves, `ads_end_affine_finite` (at most `2/lambda^2` beyond unit separation) and `future_end_affine_infinite`, with the weak-branch function taken as a hypothesis; see [20](20-causal-structure-and-final-state.md) section 6. The Lambert-W asymptotics, the curvature limit and the numerical affine lengths are script-only (group E).

## 6. Retained incoming state

If `t_+` is not switched off, sustained flux `P` captures mixed rays iff `P > lambda^2` ([14](14-state-pulse-phase-diagram.md), Lean `retained_state_hit_iff`). Capture is decided by the net null flux, matter plus state. The zero threshold of the Kim-Son convention and the zero-flux black hole of section 2 are the same fact.

## 7. What is and is not new

A targeted follow-up check against Kim-Son, Kim-Son-Yoon, RST, Thorlacius, the dilatonic-wormhole literature, state-dependent RST geometries, and recent RST injection work found no complete duplicate of the unified global theorem or final identities. The zero-flux geometry is implicit in Kim-Son's equations, state switching is explicit in Kim-Son-Yoon, and the cumulative-horizon and late-time universality structures extend RST and Thorlacius. This is bounded evidence, not an exhaustive priority determination. Human scientific review is pending.

The results on two-sided flux, global causal structure, the final mass parameter, horizon monotonicity and the outgoing radiation are in [20](20-causal-structure-and-final-state.md).

[Back to index](00-index.md)
