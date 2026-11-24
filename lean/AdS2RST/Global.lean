import Mathlib
import AdS2RST.Core
import AdS2RST.Profile
import AdS2RST.Cumulative

/-!
# Two-sided flux, global causal structure, late-time exterior

Both chiral sectors may now carry nonnegative classical flux, switched on at
the onset point.  With cumulative fluxes `Qp`, `Qm` (monotone, nonnegative at
onset) the normalized excess is

  `F̂ = μ - x_p x_m + a(x_p) + a(x_m) - A_p(max x_p 0) - A_m(max x_m 0)`.

Main results:

* `singular_future`           : the causal future of a point with `F̂ ≤ 0` has `F̂ < 0`;
* `regular_past`              : the causal past of a regular point is regular;
* `critical_curve_achronal`   : no two distinct points of `F̂ = 0` are causally related;
* `mirror_hit_iff`            : the mirror-sector total-flux criterion;
* `late_exterior_eq_zero_flux`: after the flux stops, the mixed sector is the
                                zero-flux solution with `μ_f = μ + m₁ + E²/2`;
* `event_horizon_mono`, `apparent_horizon_mono` : `F̂` is nondecreasing along both horizons.
-/

namespace AdS2RST

open Set MeasureTheory

/-- Two-sided normalized excess for the Kim-Son state. -/
noncomputable def Fhat2 (mu : ℝ) (Qp Qm : ℝ → ℝ) (xp xm : ℝ) : ℝ :=
  mu - xp * xm + aState xp + aState xm - Aflux Qp (max xp 0) - Aflux Qm (max xm 0)

lemma Aflux_zero (Q : ℝ → ℝ) : Aflux Q 0 = 0 := by
  simp [Aflux]

lemma Fhat2_symm (mu : ℝ) (Qp Qm : ℝ → ℝ) (xp xm : ℝ) :
    Fhat2 mu Qp Qm xp xm = Fhat2 mu Qm Qp xm xp := by
  unfold Fhat2
  ring

/-- With no outgoing flux the two-sided excess is the one-sided one. -/
lemma Fhat2_eq_Fhat (mu : ℝ) (Qp : ℝ → ℝ) (xp xm : ℝ) :
    Fhat2 mu Qp (fun _ => 0) xp xm = Fhat mu (fun x => Aflux Qp (max x 0)) xp xm := by
  simp [Fhat2, Fhat, Aflux]

lemma Fhat2_pre (mu : ℝ) (Qp Qm : ℝ → ℝ) {xp xm : ℝ} (hp : xp ≤ 0) (hm : xm ≤ 0) :
    Fhat2 mu Qp Qm xp xm = mu + (xp - xm) ^ 2 / 2 := by
  rw [Fhat2, aState_of_nonpos hp, aState_of_nonpos hm, max_eq_right hp, max_eq_right hm,
    Aflux_zero, Aflux_zero]
  ring

/-- Mixed sector: the two-sided excess on an outgoing ray is the one-sided `Fray`. -/
lemma Fhat2_mixed (mu : ℝ) (Qp Qm : ℝ → ℝ) {xp xm : ℝ} (hp : 0 ≤ xp) (hm : xm ≤ 0) :
    Fhat2 mu Qp Qm xp xm = Fray Qp mu (-xm) xp := by
  rw [Fhat2, aState_of_nonneg hp, aState_of_nonpos hm, max_eq_left hp, max_eq_right hm,
    Aflux_zero]
  simp only [Fray, Aflux]
  ring

lemma aState_antitone {a b : ℝ} (hab : a ≤ b) : aState b ≤ aState a := by
  unfold aState
  have h1 : min a 0 ≤ min b 0 := min_le_min hab le_rfl
  have h2 : min b 0 ≤ 0 := min_le_right _ _
  nlinarith

lemma Aflux_mono {Q : ℝ → ℝ} (hQ : Monotone Q) (h0 : 0 ≤ Q 0) {a b : ℝ} (ha : 0 ≤ a)
    (hab : a ≤ b) : Aflux Q a ≤ Aflux Q b := by
  have hint : ∀ a b : ℝ, IntervalIntegrable Q volume a b := fun a b => hQ.intervalIntegrable
  have hadd := intervalIntegral.integral_add_adjacent_intervals (hint 0 a) (hint a b)
  have hnn : 0 ≤ ∫ u in a..b, Q u := by
    apply intervalIntegral.integral_nonneg hab
    intro u hu
    exact le_trans h0 (hQ (le_trans ha hu.1))
  simp only [Aflux]
  linarith

/-- For `x_m > 0` the excess is strictly decreasing along the ray `x_m = const`. -/
lemma Fhat2_strictAnti_p {mu : ℝ} {Qp Qm : ℝ → ℝ} (hQp : Monotone Qp) (h0p : 0 ≤ Qp 0)
    {xm a b : ℝ} (hm : 0 < xm) (hab : a < b) : Fhat2 mu Qp Qm b xm < Fhat2 mu Qp Qm a xm := by
  have h1 := aState_antitone hab.le
  have h2 := Aflux_mono hQp h0p (le_max_right a 0) (max_le_max hab.le le_rfl)
  have h3 : a * xm < b * xm := mul_lt_mul_of_pos_right hab hm
  unfold Fhat2
  linarith

/-- Along any ray `x_m = const`: once the excess is nonpositive it is negative afterwards. -/
lemma Fhat2_neg_after_p {mu : ℝ} {Qp Qm : ℝ → ℝ} (hQp : Monotone Qp) (h0p : 0 ≤ Qp 0)
    (hmu : 0 < mu) {xm a b : ℝ} (hFa : Fhat2 mu Qp Qm a xm ≤ 0) (hab : a < b) :
    Fhat2 mu Qp Qm b xm < 0 := by
  rcases lt_or_ge 0 xm with hm | hm
  · exact lt_of_lt_of_le (Fhat2_strictAnti_p hQp h0p hm hab) hFa
  · have ha : 0 < a := by
      by_contra hcon
      have hpre := Fhat2_pre mu Qp Qm (not_lt.mp hcon) hm
      nlinarith [sq_nonneg (a - xm)]
    have hC : 0 < mu + (-xm) ^ 2 / 2 := by positivity
    rw [Fhat2_mixed mu Qp Qm ha.le hm] at hFa
    rw [Fhat2_mixed mu Qp Qm (ha.trans hab).le hm]
    exact Fray_neg_after hQp hC ha.le hFa hab

lemma Fhat2_neg_after_m {mu : ℝ} {Qp Qm : ℝ → ℝ} (hQm : Monotone Qm) (h0m : 0 ≤ Qm 0)
    (hmu : 0 < mu) {xp a b : ℝ} (hFa : Fhat2 mu Qp Qm xp a ≤ 0) (hab : a < b) :
    Fhat2 mu Qp Qm xp b < 0 := by
  rw [Fhat2_symm] at hFa ⊢
  exact Fhat2_neg_after_p hQm h0m hmu hFa hab

/-- **Global causal structure.**  For arbitrary nonnegative two-sided flux, every
point in the causal future of a point with `F̂ ≤ 0` has `F̂ < 0`. -/
theorem singular_future {mu : ℝ} {Qp Qm : ℝ → ℝ} (hQp : Monotone Qp) (h0p : 0 ≤ Qp 0)
    (hQm : Monotone Qm) (h0m : 0 ≤ Qm 0) (hmu : 0 < mu) {x1 z1 x2 z2 : ℝ}
    (h : Fhat2 mu Qp Qm x1 z1 ≤ 0) (hx : x1 ≤ x2) (hz : z1 ≤ z2) (hne : x1 < x2 ∨ z1 < z2) :
    Fhat2 mu Qp Qm x2 z2 < 0 := by
  rcases hx.eq_or_lt with hxe | hxl
  · subst hxe
    rcases hne with h' | h'
    · exact absurd h' (lt_irrefl _)
    · exact Fhat2_neg_after_m hQm h0m hmu h h'
  · have h1 := Fhat2_neg_after_p (Qm := Qm) hQp h0p hmu h hxl
    rcases hz.eq_or_lt with hze | hzl
    · subst hze
      exact h1
    · exact Fhat2_neg_after_m hQm h0m hmu h1.le hzl

/-- The regular region is a past set. -/
theorem regular_past {mu : ℝ} {Qp Qm : ℝ → ℝ} (hQp : Monotone Qp) (h0p : 0 ≤ Qp 0)
    (hQm : Monotone Qm) (h0m : 0 ≤ Qm 0) (hmu : 0 < mu) {x1 z1 x2 z2 : ℝ}
    (h : 0 < Fhat2 mu Qp Qm x2 z2) (hx : x1 ≤ x2) (hz : z1 ≤ z2) :
    0 < Fhat2 mu Qp Qm x1 z1 := by
  by_contra hcon
  rcases hx.eq_or_lt with hxe | hxl
  · rcases hz.eq_or_lt with hze | hzl
    · subst hxe
      subst hze
      exact hcon h
    · have := singular_future hQp h0p hQm h0m hmu (not_lt.mp hcon) hx hz (Or.inr hzl)
      linarith
  · have := singular_future hQp h0p hQm h0m hmu (not_lt.mp hcon) hx hz (Or.inl hxl)
    linarith

/-- The critical curve is achronal: two causally related points on it coincide. -/
theorem critical_curve_achronal {mu : ℝ} {Qp Qm : ℝ → ℝ} (hQp : Monotone Qp) (h0p : 0 ≤ Qp 0)
    (hQm : Monotone Qm) (h0m : 0 ≤ Qm 0) (hmu : 0 < mu) {x1 z1 x2 z2 : ℝ}
    (h1 : Fhat2 mu Qp Qm x1 z1 = 0) (h2 : Fhat2 mu Qp Qm x2 z2 = 0) (hx : x1 ≤ x2)
    (hz : z1 ≤ z2) : x1 = x2 ∧ z1 = z2 := by
  by_contra hcon
  have hne : x1 < x2 ∨ z1 < z2 := by
    by_contra hno
    push Not at hno
    exact hcon ⟨le_antisymm hx hno.1, le_antisymm hz hno.2⟩
  have := singular_future hQp h0p hQm h0m hmu h1.le hx hz hne
  linarith

/-- Mirror-sector criterion: the ingoing ray `x_p = -y` is captured iff `y` is
below the total outgoing flux. -/
theorem mirror_hit_iff {mu y : ℝ} {Qp Qm : ℝ → ℝ} (hQm : Monotone Qm)
    (hC : 0 < mu + y ^ 2 / 2) (hy : 0 ≤ y) :
    (∃ z, 0 < z ∧ Fhat2 mu Qp Qm (-y) z = 0) ↔ ∃ s, y < Qm s := by
  have key : ∀ z, 0 ≤ z → Fhat2 mu Qp Qm (-y) z = Fray Qm mu y z := by
    intro z hz
    rw [Fhat2_symm, Fhat2_mixed mu Qm Qp hz (by linarith), neg_neg]
  rw [← hit_iff hQm hC]
  constructor
  · rintro ⟨z, hz, h⟩
    exact ⟨z, hz, by rw [← key z hz.le]; exact h⟩
  · rintro ⟨z, hz, h⟩
    exact ⟨z, hz, by rw [key z hz.le]; exact h⟩

/-! ## Late-time exterior and the final mass parameter -/

/-- After the incoming flux has stopped (`Q = E` on `[s, ∞)`), the mixed sector is
`μ_f + ỹ²/2 + ỹ x̃` with `ỹ = y - E`, `x̃ = x + E`, `μ_f = μ + m₁ + E²/2`,
`m₁ = E s - ∫₀ˢ Q`. -/
theorem Fray_late {Q : ℝ → ℝ} (hQ : Monotone Q) {mu y E s x : ℝ}
    (hconst : ∀ t, s ≤ t → Q t = E) (hsx : s ≤ x) :
    Fray Q mu y x
      = (mu + (E * s - Aflux Q s) + E ^ 2 / 2) + (y - E) ^ 2 / 2 + (y - E) * (x + E) := by
  rw [Fray_after_const hQ hconst hsx]
  simp only [Fray, Aflux]
  ring

/-- The same statement as an identification with the zero-flux solution. -/
theorem late_exterior_eq_zero_flux {Q : ℝ → ℝ} (hQ : Monotone Q) {mu y E s x : ℝ}
    (hconst : ∀ t, s ≤ t → Q t = E) (hsx : s ≤ x) :
    Fray Q mu y x
      = Fray (fun _ => 0) (mu + (E * s - Aflux Q s) + E ^ 2 / 2) (y - E) (x + E) := by
  rw [Fray_late hQ hconst hsx]
  simp [Fray]

/-- The first moment `m₁ = ∫₀ˢ (E - Q)` is nonnegative. -/
lemma first_moment_nonneg {Q : ℝ → ℝ} (hQ : Monotone Q) {E s : ℝ} (hs : 0 ≤ s)
    (hle : ∀ t, Q t ≤ E) : 0 ≤ E * s - Aflux Q s := by
  have hint : ∀ a b : ℝ, IntervalIntegrable Q volume a b := fun a b => hQ.intervalIntegrable
  have hmono : ∫ t in (0 : ℝ)..s, Q t ≤ ∫ _t in (0 : ℝ)..s, E := by
    apply intervalIntegral.integral_mono_on hs (hint 0 s) intervalIntegrable_const
    intro t _
    exact hle t
  rw [intervalIntegral.integral_const, smul_eq_mul, sub_zero] at hmono
  simp only [Aflux]
  linarith

/-! ## Monotonicity along the horizons -/

/-- `F̂` is nondecreasing along the event horizon `y = E`. -/
theorem event_horizon_mono {Q : ℝ → ℝ} (hQ : Monotone Q) {mu E a b : ℝ}
    (hle : ∀ t, Q t ≤ E) (hab : a ≤ b) : Fray Q mu E a ≤ Fray Q mu E b := by
  have hsub := Fray_sub hQ mu E a b
  have hnn : 0 ≤ ∫ t in a..b, (E - Q t) := by
    apply intervalIntegral.integral_nonneg hab
    intro t _
    linarith [hle t]
  linarith

/-- `F̂` is nondecreasing along the apparent horizon `y = Q(x)`. -/
theorem apparent_horizon_mono {Q : ℝ → ℝ} (hQ : Monotone Q) (h0 : 0 ≤ Q 0) {mu a b : ℝ}
    (ha : 0 ≤ a) (hab : a ≤ b) : Fray Q mu (Q a) a ≤ Fray Q mu (Q b) b := by
  have hint : ∀ a b : ℝ, IntervalIntegrable Q volume a b := fun a b => hQ.intervalIntegrable
  have hadd := intervalIntegral.integral_add_adjacent_intervals (hint 0 a) (hint a b)
  have hmono : ∫ t in a..b, Q t ≤ ∫ _t in a..b, Q b := by
    apply intervalIntegral.integral_mono_on hab (hint a b) intervalIntegrable_const
    intro t ht
    exact hQ ht.2
  rw [intervalIntegral.integral_const, smul_eq_mul] at hmono
  have hQa : 0 ≤ Q a := le_trans h0 (hQ ha)
  have hQab : Q a ≤ Q b := hQ hab
  have h1 : 0 ≤ a * (Q b - Q a) := mul_nonneg ha (sub_nonneg.mpr hQab)
  have h2 : 0 ≤ (Q b - Q a) * (Q b + Q a) := mul_nonneg (sub_nonneg.mpr hQab) (by linarith)
  simp only [Fray]
  nlinarith
end AdS2RST
