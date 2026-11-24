# Lean verification

Lean 4.36.0 with Mathlib. No `sorry`, no added axioms. The root file `AdS2RST.lean` imports six modules and prints the axiom dependencies of 77 results; each depends only on `propext`, `Classical.choice` and `Quot.sound`. The validator checks this from the build log.

```bash
lake build
# Or, from the package root:
RUN_LEAN=1 ./run_verification.sh
```

## Modules

| Module | Content |
|---|---|
| `AdS2RST/Core.lean` | Sustained flux: `F`, `D`, `xHit`; the root is a zero and the only positive one (`F_eq_zero_iff`); sign before and after; slope of the critical curve; finite-pulse branch algebra (`zAfter_pos_iff`, `after_interval_nonempty_iff`); retained-state identity (`retained_state_equiv`); abstract first-hit criterion by the intermediate value theorem (`first_hit_iff`). |
| `AdS2RST/Profile.lean` | The state profile `aState x = (min x 0)^2/2` is differentiable with derivative `min x 0` (so `C^1` across onset) and has second derivative 1 before onset and 0 after: the constraint for `t = (lambda^2/kappa) Theta(-x)`. General solution `Fhat` and its four sector formulas. Field equation `d_p d_m Fhat = -1`. |
| `AdS2RST/Cumulative.lean` | Total-flux criterion for an arbitrary monotone cumulative flux `Q`, with `Fray Q mu y x = mu + y^2/2 + y x - int_0^x Q`: `hit_iff`, `existsUnique_hit`, `Fray_neg_after`, `Fray_pos_before`, `Q_gt_of_Fray_nonpos`, `no_hit_of_le`, `finite_total_flux_hit_iff`. Specializations: sustained (`Fray_sustained`, `sustained_every_ray_hit`, `sustained_hit_is_xHit`) and impulsive (`impulse_hit_iff`). Linear bounds `Fray_ge_linear`, `Fray_le_linear` (escaping rays). Finite pulse: `Fray_congr` (domain of dependence), `pulse_during_iff` (the `y_max` condition), `Fray_after_const`, `after_pulse_root`, `pulse_after_formula`. |
| `AdS2RST/Structure.lean` | Zero-flux structure (`zero_flux_wall_iff`, `zero_flux_wall_slope`, trapping, regularity of the other sectors, `eternal_wormhole_regular`); symmetry classification (`symmetry_pre`, `symmetry_post`, `symmetry_mixed`); minimum of `Omega(phi)` (`OmegaOf_phiCrit`, `OmegaCrit_le`); `conformal_factor_bound`; comparison integrals for the affine length (`affine_tail_bounded`, `affine_future_unbounded`); `horizon_before_wall`; retained incoming state threshold (`retained_state_regular`, `retained_state_hit_iff`: capture iff `p > 1`). |

| `AdS2RST/Global.lean` | Two-sided flux `Fhat2` with its reduction to `Fhat` and `Fray` (`Fhat2_eq_Fhat`, `Fhat2_mixed`, `Fhat2_symm`); the global causal theorem `singular_future` (the causal future of a point with `Fhat <= 0` has `Fhat < 0`), `regular_past`, `critical_curve_achronal`; mirror-sector criterion `mirror_hit_iff`; late exterior and final mass parameter (`Fray_late`, `late_exterior_eq_zero_flux`, `first_moment_nonneg`); `event_horizon_mono`, `apparent_horizon_mono`. |
| `AdS2RST/Affine.lean` | Weak-branch bounds `weak_branch_lower'`, `weak_branch_upper`; affine length of the AdS2 end at most `2/lambda^2` beyond unit separation (`affine_finite_of_quadratic`, `ads_end_affine_finite`); divergence at the future end (`affine_infinite_of_linear`, `future_end_affine_infinite`). The branch function `u = e^{-2 phi}` along the ray is a hypothesis; for `future_end_affine_infinite` it can only be satisfied on escaping rays, since no such `u` exists where `Fhat < 0`. |

The manuscript's Table 1 maps each statement of the paper to these names.

## What is formalized and what is not

Formalized:

- every algebraic and order-theoretic step of the sustained, finite-pulse and impulsive results;
- the cumulative theorem in full generality for monotone `Q` (no continuity or density assumed), using interval integrals;
- the derivation of the state profile from the normalized constraint, and the sector formulas;
- the zero-flux black hole and the symmetry classification;
- the global causal theorem for arbitrary nonnegative two-sided flux, as an order statement on the Kruskal plane;
- the late-exterior identity with the final mass parameter, and monotonicity of `Fhat` along both horizons;
- the affine-length conclusions for both ends, conditional on the weak-branch function.

Not formalized:

- the reduction of the RST action to `d_+ d_- Omega = -L` and the constraints (the development starts from the normalized constraint);
- the identification of `A'' ` with the flux measure (the development takes `A = int_0^x Q` as the definition);
- the Lambert-W inversion of `Omega(phi)` (existence and continuity of the weak branch), the asymptotic form of the conformal factor, the curvature limit, the numerical affine lengths and the outgoing-flux limit, which are argued on paper and checked in `structure_checks.py` only;
- the identification of the causal order of the spacetime with the coordinate order of the Kruskal plane;
- the signed-source theory of document 12 beyond `first_hit_iff`;
- anything about quantum states, boundaries or observers.

The build receipt is `outputs/lean-build.out`, with a hash over all seven source files in `outputs/lean-build.json`.
