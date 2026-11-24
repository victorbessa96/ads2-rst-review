import AdS2RST.Core
import AdS2RST.Profile
import AdS2RST.Cumulative
import AdS2RST.Structure
import AdS2RST.Global
import AdS2RST.Affine

/-!
# AdS2-RST one-sided flux: formal development

* `Core`       : closed-form sustained root, uniqueness, signs, finite-pulse branch algebra.
* `Profile`    : chiral profile of the Kim-Son state from the constraint, sector formulas.
* `Cumulative` : total-flux criterion for arbitrary monotone cumulative flux.
* `Structure`  : zero-flux wall, trapping, symmetries, critical value, affine comparison.
* `Global`     : two-sided flux, future-set theorem, achronal critical curve, final mass parameter, horizon monotonicity.
* `Affine`     : weak-branch bounds and the affine length of both ends.

The axiom audit below lists the headline results.  Only the three standard
axioms of Lean's classical logic may appear.
-/

#print axioms AdS2RST.first_hit_iff
#print axioms AdS2RST.F_hasDerivAt_y
#print axioms AdS2RST.F_eq_zero_iff
#print axioms AdS2RST.F_factor
#print axioms AdS2RST.F_pos_before
#print axioms AdS2RST.F_neg_after
#print axioms AdS2RST.slope_neg
#print axioms AdS2RST.general_wall_slope_neg
#print axioms AdS2RST.retained_state_equiv
#print axioms AdS2RST.stress_scaling
#print axioms AdS2RST.zAfter_pos_iff
#print axioms AdS2RST.after_interval_nonempty_iff
#print axioms AdS2RST.aState_hasDerivAt
#print axioms AdS2RST.aState_second_deriv_neg
#print axioms AdS2RST.aState_second_deriv_pos
#print axioms AdS2RST.Fhat_pre
#print axioms AdS2RST.Fhat_mixed
#print axioms AdS2RST.Fhat_post
#print axioms AdS2RST.Fhat_hasDerivAt_xm
#print axioms AdS2RST.Q_gt_of_Fray_nonpos
#print axioms AdS2RST.Fray_neg_after
#print axioms AdS2RST.Fray_pos_before
#print axioms AdS2RST.hit_iff
#print axioms AdS2RST.existsUnique_hit
#print axioms AdS2RST.no_hit_of_le
#print axioms AdS2RST.sustained_every_ray_hit
#print axioms AdS2RST.sustained_hit_is_xHit
#print axioms AdS2RST.impulse_hit_iff
#print axioms AdS2RST.finite_total_flux_hit_iff
#print axioms AdS2RST.zero_flux_wall_iff
#print axioms AdS2RST.zero_flux_wall_slope
#print axioms AdS2RST.zero_flux_trapped_minus
#print axioms AdS2RST.zero_flux_trapped_plus
#print axioms AdS2RST.wormhole_regular
#print axioms AdS2RST.zero_flux_mixed_regular
#print axioms AdS2RST.mirror_regular
#print axioms AdS2RST.symmetry_pre
#print axioms AdS2RST.symmetry_post
#print axioms AdS2RST.symmetry_mixed
#print axioms AdS2RST.OmegaOf_phiCrit
#print axioms AdS2RST.OmegaCrit_le
#print axioms AdS2RST.conformal_factor_bound
#print axioms AdS2RST.affine_tail_bounded
#print axioms AdS2RST.affine_future_unbounded
#print axioms AdS2RST.horizon_before_wall
#print axioms AdS2RST.excess_pos_at_horizon
#print axioms AdS2RST.Fhat_mirror
#print axioms AdS2RST.eternal_wormhole_regular
#print axioms AdS2RST.mixed_derivative_field_equation
#print axioms AdS2RST.Fray_root_unique
#print axioms AdS2RST.Fray_ge_linear
#print axioms AdS2RST.Fray_le_linear
#print axioms AdS2RST.Fray_congr
#print axioms AdS2RST.Fray_after_const
#print axioms AdS2RST.after_pulse_root
#print axioms AdS2RST.pulse_after_formula
#print axioms AdS2RST.pulse_during_iff
#print axioms AdS2RST.retained_state_regular
#print axioms AdS2RST.retained_state_hit_iff
#print axioms AdS2RST.Fhat2_eq_Fhat
#print axioms AdS2RST.Fhat2_mixed
#print axioms AdS2RST.Fhat2_neg_after_p
#print axioms AdS2RST.singular_future
#print axioms AdS2RST.regular_past
#print axioms AdS2RST.critical_curve_achronal
#print axioms AdS2RST.mirror_hit_iff
#print axioms AdS2RST.Fray_late
#print axioms AdS2RST.late_exterior_eq_zero_flux
#print axioms AdS2RST.first_moment_nonneg
#print axioms AdS2RST.event_horizon_mono
#print axioms AdS2RST.apparent_horizon_mono
#print axioms AdS2RST.weak_branch_lower'
#print axioms AdS2RST.weak_branch_upper
#print axioms AdS2RST.affine_finite_of_quadratic
#print axioms AdS2RST.affine_infinite_of_linear
#print axioms AdS2RST.ads_end_affine_finite
#print axioms AdS2RST.future_end_affine_infinite
