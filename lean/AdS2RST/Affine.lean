import Mathlib
import AdS2RST.Core
import AdS2RST.Profile
import AdS2RST.Cumulative
import AdS2RST.Structure

/-!
# Affine length of the two ends

In Kruskal gauge `ρ = φ`, and `u = e^{-2φ}` satisfies
`u - (κ/4) ln u = √κ Ω = (κ/4)(1 - ln(κ/4)) + λ² F̂` with `u ≥ κ/4` on the
weak-coupling branch.  The affine parameter along a null ray is `∫ e^{2ρ} = ∫ 1/u`.

The branch `u` enters as a hypothesis (a continuous function satisfying the
relation and the weak-coupling inequality along the ray); its existence, which
is the Lambert-W inversion, is not constructed here.

* `weak_branch_lower'`        : `e^{-2φ} ≥ κ/4 + λ² F̂`;
* `weak_branch_upper`         : `e^{-2φ} ≤ 2 √κ Ω + (κ/2)(ln(κ/2) - 1)`;
* `affine_finite_of_quadratic`: quadratic growth of `F̂` gives affine length `≤ 2/λ²`;
* `affine_infinite_of_linear` : at most linear growth of `F̂` gives infinite affine length;
* `ads_end_affine_finite`, `future_end_affine_infinite` : the two ends.
-/

namespace AdS2RST

open Set MeasureTheory

lemma weak_branch_lower {kappa u W : ℝ} (hk : 0 < kappa) (hu : kappa / 4 ≤ u)
    (hrel : u - kappa / 4 * Real.log u = W) : W + kappa / 4 * Real.log (kappa / 4) ≤ u := by
  have hk4 : 0 < kappa / 4 := by positivity
  have hlog : Real.log (kappa / 4) ≤ Real.log u := Real.log_le_log hk4 hu
  have := mul_le_mul_of_nonneg_left hlog hk4.le
  linarith

/-- Weak-branch lower bound in the form used below: `e^{-2φ} ≥ κ/4 + G`, `G = λ² F̂`. -/
lemma weak_branch_lower' {kappa u G : ℝ} (hk : 0 < kappa) (hu : kappa / 4 ≤ u)
    (hrel : u - kappa / 4 * Real.log u = kappa / 4 * (1 - Real.log (kappa / 4)) + G) :
    kappa / 4 + G ≤ u := by
  have := weak_branch_lower hk hu hrel
  linarith

/-- Upper bound, valid for every `κ > 0`. -/
lemma weak_branch_upper {kappa u W : ℝ} (hk : 0 < kappa) (hu : 0 < u)
    (hrel : u - kappa / 4 * Real.log u = W) :
    u ≤ 2 * W + kappa / 2 * (Real.log (kappa / 2) - 1) := by
  have hk2 : 0 < kappa / 2 := by positivity
  have h1 := Real.log_le_sub_one_of_pos (div_pos hu hk2)
  rw [Real.log_div hu.ne' hk2.ne'] at h1
  have h2 : kappa / 4 * (u / (kappa / 2)) = u / 2 := by
    field_simp
    ring
  have h3 := mul_le_mul_of_nonneg_left h1 (show (0 : ℝ) ≤ kappa / 4 by positivity)
  nlinarith

/-- Quadratic growth of the excess gives a uniformly bounded affine parameter. -/
theorem affine_finite_of_quadratic {kappa lam : ℝ} (hk : 0 < kappa) (hlam : 0 < lam)
    {u F : ℝ → ℝ} (hcont : Continuous u) (hweak : ∀ t, kappa / 4 ≤ u t)
    (hrel : ∀ t, 1 ≤ t → u t - kappa / 4 * Real.log (u t)
      = kappa / 4 * (1 - Real.log (kappa / 4)) + lam ^ 2 * F t)
    (hF : ∀ t, 1 ≤ t → t ^ 2 / 2 ≤ F t) {T : ℝ} (hT : 1 ≤ T) :
    ∫ t in (1 : ℝ)..T, 1 / u t ≤ 2 / lam ^ 2 := by
  have hk4 : 0 < kappa / 4 := by positivity
  have hupos : ∀ t, 0 < u t := fun t => lt_of_lt_of_le hk4 (hweak t)
  have hbound : ∀ t ∈ Icc 1 T, 1 / u t ≤ 1 / lam ^ 2 * (2 / t ^ 2) := by
    intro t ht
    have ht0 : 0 < t := by linarith [ht.1]
    have hlow := weak_branch_lower' hk (hweak t) (hrel t ht.1)
    have hF' := mul_le_mul_of_nonneg_left (hF t ht.1) (sq_nonneg lam)
    have h1 : lam ^ 2 * (t ^ 2 / 2) ≤ u t := by linarith
    have hpos : 0 < lam ^ 2 * (t ^ 2 / 2) := by positivity
    calc 1 / u t ≤ 1 / (lam ^ 2 * (t ^ 2 / 2)) := one_div_le_one_div_of_le hpos h1
      _ = 1 / lam ^ 2 * (2 / t ^ 2) := by
        field_simp
  have hint1 : IntervalIntegrable (fun t => 1 / u t) volume 1 T :=
    (continuous_const.div hcont (fun t => (hupos t).ne')).intervalIntegrable 1 T
  have hcontg : ContinuousOn (fun x : ℝ => 2 / x ^ 2) (uIcc 1 T) := by
    apply ContinuousOn.div continuousOn_const (continuous_pow 2).continuousOn
    intro x hx
    rw [uIcc_of_le hT] at hx
    have hxpos : 0 < x := by linarith [hx.1]
    exact pow_ne_zero 2 hxpos.ne'
  have hint2 : IntervalIntegrable (fun t : ℝ => 1 / lam ^ 2 * (2 / t ^ 2)) volume 1 T :=
    hcontg.intervalIntegrable.const_mul _
  have hmono := intervalIntegral.integral_mono_on hT hint1 hint2 hbound
  rw [intervalIntegral.integral_const_mul, (affine_tail_bounded hT).1] at hmono
  have hTpos : 0 < T := by linarith
  have h2 : 2 - 2 / T ≤ 2 := by
    have : 0 ≤ 2 / T := by positivity
    linarith
  have h3 : (0 : ℝ) ≤ 1 / lam ^ 2 := by positivity
  have h4 : 1 / lam ^ 2 * (2 - 2 / T) ≤ 1 / lam ^ 2 * 2 := mul_le_mul_of_nonneg_left h2 h3
  have h5 : 1 / lam ^ 2 * 2 = 2 / lam ^ 2 := by ring
  linarith

/-- At most linear growth of the excess gives an unbounded affine parameter. -/
theorem affine_infinite_of_linear {kappa lam c : ℝ} (hk : 0 < kappa) (hlam : 0 < lam)
    (hc : 0 < c) {u F : ℝ → ℝ} (hcont : Continuous u) (hweak : ∀ t, kappa / 4 ≤ u t)
    (hrel : ∀ t, 1 ≤ t → u t - kappa / 4 * Real.log (u t)
      = kappa / 4 * (1 - Real.log (kappa / 4)) + lam ^ 2 * F t)
    (hF : ∀ x, 1 ≤ x → F x ≤ c * x) (B : ℝ) :
    ∃ X : ℝ, 1 ≤ X ∧ B < ∫ x in (1 : ℝ)..X, 1 / u x := by
  have hk4 : 0 < kappa / 4 := by positivity
  have hupos : ∀ t, 0 < u t := fun t => lt_of_lt_of_le hk4 (hweak t)
  obtain ⟨K, hK⟩ : ∃ K : ℝ, K = 2 * (kappa / 4 * (1 - Real.log (kappa / 4)))
      + kappa / 2 * (Real.log (kappa / 2) - 1) := ⟨_, rfl⟩
  obtain ⟨M, hMdef⟩ : ∃ M : ℝ, M = |K| + 2 * lam ^ 2 * c := ⟨_, rfl⟩
  have hM : 0 < M := by
    rw [hMdef]
    have : 0 < 2 * lam ^ 2 * c := by positivity
    linarith [abs_nonneg K]
  have hb : ∀ x : ℝ, 1 ≤ x → 1 / M * (1 / x) ≤ 1 / u x := by
    intro x hx
    have hx0 : 0 < x := by linarith
    have hup := weak_branch_upper hk (hupos x) (hrel x hx)
    have hKx := mul_le_mul_of_nonneg_left hx (abs_nonneg K)
    have hFx := mul_le_mul_of_nonneg_left (hF x hx) (sq_nonneg lam)
    have hux : u x ≤ M * x := by
      rw [hMdef]
      nlinarith [le_abs_self K]
    calc 1 / M * (1 / x) = 1 / (M * x) := by
          field_simp
      _ ≤ 1 / u x := one_div_le_one_div_of_le (hupos x) hux
  obtain ⟨X, hX, hlt⟩ := affine_future_unbounded (B * M)
  refine ⟨X, hX, ?_⟩
  have hint1 : IntervalIntegrable (fun t => 1 / u t) volume 1 X :=
    (continuous_const.div hcont (fun t => (hupos t).ne')).intervalIntegrable 1 X
  have hcontg : ContinuousOn (fun x : ℝ => 1 / x) (uIcc 1 X) := by
    apply ContinuousOn.div continuousOn_const continuousOn_id
    intro x hx
    rw [uIcc_of_le hX] at hx
    have hxpos : 0 < x := by linarith [hx.1]
    exact hxpos.ne'
  have hint2 : IntervalIntegrable (fun t : ℝ => 1 / M * (1 / t)) volume 1 X :=
    hcontg.intervalIntegrable.const_mul _
  have hmono := intervalIntegral.integral_mono_on hX hint2 hint1 (fun x hx => hb x hx.1)
  rw [intervalIntegral.integral_const_mul] at hmono
  have h1 := mul_lt_mul_of_pos_left hlt (one_div_pos.mpr hM)
  have h2 : 1 / M * (B * M) = B := by
    field_simp
  linarith

/-- **AdS₂ end.**  Along a pre-onset null ray, at coordinate distance `t ≥ 1` from the
throat, `F̂ = μ + t²/2`; the affine parameter out to any `T` is at most `2/λ²`. -/
theorem ads_end_affine_finite {kappa lam mu : ℝ} (hk : 0 < kappa) (hlam : 0 < lam)
    (hmu : 0 ≤ mu) {u : ℝ → ℝ} (hcont : Continuous u) (hweak : ∀ t, kappa / 4 ≤ u t)
    (hrel : ∀ t, 1 ≤ t → u t - kappa / 4 * Real.log (u t)
      = kappa / 4 * (1 - Real.log (kappa / 4)) + lam ^ 2 * (mu + t ^ 2 / 2))
    {T : ℝ} (hT : 1 ≤ T) : ∫ t in (1 : ℝ)..T, 1 / u t ≤ 2 / lam ^ 2 :=
  affine_finite_of_quadratic hk hlam hcont hweak hrel (fun t _ => by linarith) hT

/-- **Future end.**  Along an outgoing ray in the mixed sector with nonnegative flux,
the affine parameter is unbounded as `x_p → ∞`. -/
theorem future_end_affine_infinite {kappa lam mu y : ℝ} (hk : 0 < kappa) (hlam : 0 < lam)
    (hmu : 0 < mu) (hy : 0 < y) {Q : ℝ → ℝ} (hQ : Monotone Q) (h0Q : 0 ≤ Q 0)
    {u : ℝ → ℝ} (hcont : Continuous u) (hweak : ∀ t, kappa / 4 ≤ u t)
    (hrel : ∀ x, 1 ≤ x → u x - kappa / 4 * Real.log (u x)
      = kappa / 4 * (1 - Real.log (kappa / 4)) + lam ^ 2 * Fray Q mu y x)
    (B : ℝ) : ∃ X : ℝ, 1 ≤ X ∧ B < ∫ x in (1 : ℝ)..X, 1 / u x := by
  have hc : 0 < mu + y ^ 2 / 2 + y := by positivity
  refine affine_infinite_of_linear hk hlam hc hcont hweak hrel ?_ B
  intro x hx
  have h := Fray_le_linear (mu := mu) (y := y) hQ h0Q (by linarith : (0 : ℝ) ≤ x)
  have h2 : mu + y ^ 2 / 2 ≤ (mu + y ^ 2 / 2) * x := by
    have hpos : 0 ≤ mu + y ^ 2 / 2 := by positivity
    nlinarith
  nlinarith

end AdS2RST
