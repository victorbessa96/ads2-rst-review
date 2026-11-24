import Mathlib
import AdS2RST.Core
import AdS2RST.Profile

/-!
# The total-flux criterion for arbitrary nonnegative incoming flux

Let `Q : ℝ → ℝ` be the cumulative incoming flux in units of `λ²`,
`Q(x) = λ⁻² ∫_{[0,x]} dT_{++}`.  Positivity of the flux is the statement that
`Q` is monotone.  Jumps of `Q` are atoms (impulsive shells), so no measure
theory beyond monotone functions is needed.  The matter profile is
`A(x) = ∫₀ˣ Q`, and on the mixed ray `x_m = -y` the normalized excess is

  `F(x) = μ + y²/2 + y x - ∫₀ˣ Q`.

Main results (`C = μ + y²/2 > 0`):

* `Fray_neg_after`     : once `F ≤ 0` it is strictly negative afterwards;
* `Q_gt_of_Fray_nonpos`: at a hit the cumulative flux exceeds `y`
                         (the ray is already inside the apparent horizon);
* `hit_iff`            : a hit exists iff `Q` exceeds `y` somewhere;
* `existsUnique_hit`   : the hit is unique;
* `no_hit_of_le`       : if `Q ≤ y` everywhere the ray is regular for all `x ≥ 0`.

Specializations recover the sustained formula of `Core.lean` and the
Kim-Son impulsive band.
-/

namespace AdS2RST

open Set MeasureTheory

/-- Mixed-ray normalized excess for a cumulative flux `Q`. -/
noncomputable def Fray (Q : ℝ → ℝ) (mu y x : ℝ) : ℝ :=
  mu + y ^ 2 / 2 + y * x - ∫ s in (0 : ℝ)..x, Q s

/-- The matter profile attached to `Q`. -/
noncomputable def Aflux (Q : ℝ → ℝ) (x : ℝ) : ℝ := ∫ s in (0 : ℝ)..x, Q s

lemma Fray_eq_Fhat (Q : ℝ → ℝ) (mu : ℝ) {y x : ℝ} (hx : 0 ≤ x) (hy : 0 ≤ y) :
    Fray Q mu y x = Fhat mu (Aflux Q) x (-y) := by
  rw [Fhat_mixed mu (Aflux Q) hx hy]
  rfl

lemma Fray_zero (Q : ℝ → ℝ) (mu y : ℝ) : Fray Q mu y 0 = mu + y ^ 2 / 2 := by
  simp [Fray]

variable {Q : ℝ → ℝ}

lemma Fray_sub (hQ : Monotone Q) (mu y a b : ℝ) :
    Fray Q mu y b - Fray Q mu y a = ∫ s in a..b, (y - Q s) := by
  have hint : ∀ a b : ℝ, IntervalIntegrable Q volume a b := fun a b => hQ.intervalIntegrable
  rw [intervalIntegral.integral_sub intervalIntegrable_const (hint a b),
    intervalIntegral.integral_const]
  have hadd := intervalIntegral.integral_add_adjacent_intervals (hint 0 a) (hint a b)
  simp only [Fray, smul_eq_mul]
  linarith

lemma Fray_continuous (hQ : Monotone Q) (mu y : ℝ) : Continuous (fun x => Fray Q mu y x) := by
  have hint : ∀ a b : ℝ, IntervalIntegrable Q volume a b := fun a b => hQ.intervalIntegrable
  have hprim : Continuous fun x : ℝ => ∫ s in (0 : ℝ)..x, Q s :=
    intervalIntegral.continuous_primitive hint 0
  unfold Fray
  fun_prop

/-- At any point of the ray where the excess is nonpositive, the cumulative flux
already exceeds `y`.  In `∂_x F = y - Q` language: the ray crossed the apparent
horizon before reaching the critical curve. -/
lemma Q_gt_of_Fray_nonpos (hQ : Monotone Q) {mu y a : ℝ} (hC : 0 < mu + y ^ 2 / 2)
    (ha : 0 ≤ a) (hFa : Fray Q mu y a ≤ 0) : y < Q a := by
  by_contra hcon
  have hle : Q a ≤ y := not_lt.mp hcon
  have hnonneg : 0 ≤ ∫ s in (0 : ℝ)..a, (y - Q s) := by
    apply intervalIntegral.integral_nonneg ha
    intro s hs
    have := hQ hs.2
    linarith
  have hsub := Fray_sub hQ mu y 0 a
  rw [Fray_zero] at hsub
  linarith

/-- Past a point where the excess is nonpositive, it is strictly negative. -/
lemma Fray_neg_after (hQ : Monotone Q) {mu y a b : ℝ} (hC : 0 < mu + y ^ 2 / 2)
    (ha : 0 ≤ a) (hFa : Fray Q mu y a ≤ 0) (hab : a < b) : Fray Q mu y b < 0 := by
  have hQa := Q_gt_of_Fray_nonpos hQ hC ha hFa
  have hint : ∀ a b : ℝ, IntervalIntegrable Q volume a b := fun a b => hQ.intervalIntegrable
  have hmono : ∫ s in a..b, (y - Q s) ≤ ∫ s in a..b, (y - Q a) := by
    apply intervalIntegral.integral_mono_on hab.le
      (intervalIntegrable_const.sub (hint a b)) intervalIntegrable_const
    intro s hs
    have := hQ hs.1
    linarith
  rw [intervalIntegral.integral_const, smul_eq_mul] at hmono
  have hsub := Fray_sub hQ mu y a b
  have hneg : (b - a) * (y - Q a) < 0 :=
    mul_neg_of_pos_of_neg (sub_pos.mpr hab) (by linarith)
  linarith

/-- Before a hit the ray is on the physical side. -/
lemma Fray_pos_before (hQ : Monotone Q) {mu y x a : ℝ} (hC : 0 < mu + y ^ 2 / 2)
    (hx : 0 ≤ x) (hxa : x < a) (hFa : Fray Q mu y a = 0) : 0 < Fray Q mu y x := by
  by_contra hcon
  have := Fray_neg_after hQ hC hx (not_lt.mp hcon) hxa
  linarith

/-- The hit, if it exists, is unique. -/
lemma Fray_root_unique (hQ : Monotone Q) {mu y a b : ℝ} (hC : 0 < mu + y ^ 2 / 2)
    (ha : 0 ≤ a) (hb : 0 ≤ b) (hFa : Fray Q mu y a = 0) (hFb : Fray Q mu y b = 0) : a = b := by
  rcases lt_trichotomy a b with h | h | h
  · have := Fray_neg_after hQ hC ha hFa.le h
    linarith
  · exact h
  · have := Fray_neg_after hQ hC hb hFb.le h
    linarith

/-- If the cumulative flux never exceeds `y`, the ray never reaches the critical curve. -/
lemma no_hit_of_le (hQ : Monotone Q) {mu y : ℝ} (hC : 0 < mu + y ^ 2 / 2)
    (hle : ∀ s, Q s ≤ y) {x : ℝ} (hx : 0 ≤ x) : 0 < Fray Q mu y x := by
  by_contra hcon
  have := Q_gt_of_Fray_nonpos hQ hC hx (not_lt.mp hcon)
  linarith [hle x]

/-- If the cumulative flux exceeds `y` somewhere, the ray reaches the critical curve. -/
lemma exists_hit_of_exceeds (hQ : Monotone Q) {mu y : ℝ} (hC : 0 < mu + y ^ 2 / 2)
    (hex : ∃ s, y < Q s) : ∃ x, 0 < x ∧ Fray Q mu y x = 0 := by
  obtain ⟨s, hs⟩ := hex
  set a : ℝ := max s 0 with ha_def
  have ha : 0 ≤ a := le_max_right _ _
  have hQa : y < Q a := lt_of_lt_of_le hs (hQ (le_max_left _ _))
  have hint : ∀ a b : ℝ, IntervalIntegrable Q volume a b := fun a b => hQ.intervalIntegrable
  set g : ℝ := Q a - y with hg_def
  have hg : 0 < g := sub_pos.mpr hQa
  set X : ℝ := a + (|Fray Q mu y a| + 1) / g with hX_def
  have hpos : 0 < (|Fray Q mu y a| + 1) / g := div_pos (by positivity) hg
  have haX : a < X := by linarith
  have hX0 : 0 ≤ X := by linarith
  have hFX : Fray Q mu y X < 0 := by
    have hmono : ∫ t in a..X, (y - Q t) ≤ ∫ t in a..X, (y - Q a) := by
      apply intervalIntegral.integral_mono_on haX.le
        (intervalIntegrable_const.sub (hint a X)) intervalIntegrable_const
      intro t ht
      have := hQ ht.1
      linarith
    rw [intervalIntegral.integral_const, smul_eq_mul] at hmono
    have hsub := Fray_sub hQ mu y a X
    have hXa : X - a = (|Fray Q mu y a| + 1) / g := by simp [hX_def]
    have hprod : (X - a) * (y - Q a) = -(|Fray Q mu y a| + 1) := by
      rw [hXa]
      have : y - Q a = -g := by simp [hg_def]
      rw [this]
      field_simp
    have habs := le_abs_self (Fray Q mu y a)
    linarith
  have hcont := (Fray_continuous hQ mu y).continuousOn (s := Icc 0 X)
  have hsubset := intermediate_value_Icc' hX0 hcont
  have hmem : (0 : ℝ) ∈ Icc (Fray Q mu y X) (Fray Q mu y 0) := by
    rw [Fray_zero]
    exact ⟨hFX.le, hC.le⟩
  obtain ⟨c, hc, hFc'⟩ := hsubset hmem
  have hFc : Fray Q mu y c = 0 := hFc'
  refine ⟨c, ?_, hFc⟩
  rcases eq_or_lt_of_le hc.1 with h0 | h0
  · rw [← h0, Fray_zero] at hFc
    linarith
  · exact h0

/-- **Total-flux criterion.**  For monotone cumulative flux `Q`, the mixed ray
`x_m = -y` reaches the critical curve iff `Q` exceeds `y` somewhere, that is
iff `y < E_tot = sup Q`. -/
theorem hit_iff (hQ : Monotone Q) {mu y : ℝ} (hC : 0 < mu + y ^ 2 / 2) :
    (∃ x, 0 < x ∧ Fray Q mu y x = 0) ↔ ∃ s, y < Q s := by
  constructor
  · rintro ⟨x, hx, hFx⟩
    exact ⟨x, Q_gt_of_Fray_nonpos hQ hC hx.le hFx.le⟩
  · exact exists_hit_of_exceeds hQ hC

/-- Existence and uniqueness of the hit together. -/
theorem existsUnique_hit (hQ : Monotone Q) {mu y : ℝ} (hC : 0 < mu + y ^ 2 / 2)
    (hex : ∃ s, y < Q s) : ∃! x, 0 < x ∧ Fray Q mu y x = 0 := by
  obtain ⟨x, hx, hFx⟩ := exists_hit_of_exceeds hQ hC hex
  refine ⟨x, ⟨hx, hFx⟩, ?_⟩
  rintro z ⟨hz, hFz⟩
  exact Fray_root_unique hQ hC hz.le hx.le hFz hFx

/-! ## Sustained flux: `Q(x) = p x` after onset -/

/-- Cumulative flux of a constant density `p` switched on at `x = 0`. -/
noncomputable def Qsust (p : ℝ) (x : ℝ) : ℝ := p * max x 0

lemma Qsust_monotone {p : ℝ} (hp : 0 ≤ p) : Monotone (Qsust p) := by
  intro a b hab
  unfold Qsust
  exact mul_le_mul_of_nonneg_left (max_le_max hab le_rfl) hp

lemma Fray_sustained (p mu y : ℝ) {x : ℝ} (hx : 0 ≤ x) :
    Fray (Qsust p) mu y x = F p y mu x := by
  have hcongr : ∫ s in (0 : ℝ)..x, Qsust p s = ∫ s in (0 : ℝ)..x, p * s := by
    apply intervalIntegral.integral_congr
    intro s hs
    rw [uIcc_of_le hx] at hs
    simp [Qsust, max_eq_left hs.1]
  rw [Fray, hcongr, intervalIntegral.integral_const_mul, integral_id]
  simp only [F]
  ring

/-- The general criterion applied to sustained flux: every mixed ray is hit. -/
theorem sustained_every_ray_hit {p mu y : ℝ} (hp : 0 < p) (hy : 0 < y) (hmu : 0 ≤ mu) :
    ∃! x, 0 < x ∧ Fray (Qsust p) mu y x = 0 := by
  have hC : 0 < mu + y ^ 2 / 2 := by positivity
  apply existsUnique_hit (Qsust_monotone hp.le) hC
  refine ⟨y / p + 1, ?_⟩
  have hpos : 0 < y / p + 1 := by positivity
  simp only [Qsust, max_eq_left hpos.le]
  have : p * (y / p + 1) = y + p := by field_simp
  linarith

/-- The hit found by the general theorem is the closed formula of `Core.lean`. -/
theorem sustained_hit_is_xHit {p mu y x : ℝ} (hp : 0 < p) (hy : 0 < y) (hmu : 0 ≤ mu)
    (hx : 0 < x) (hF : Fray (Qsust p) mu y x = 0) : x = xHit p y mu := by
  rw [Fray_sustained p mu y hx.le] at hF
  exact (F_eq_zero_iff p y mu hp hy hmu hx).mp hF

/-! ## Impulsive shell: `Q(x) = α` after onset (Kim-Son) -/

/-- Cumulative flux of an impulsive shell of strength `α` at `x = 0`. -/
noncomputable def Qimp (alpha : ℝ) (x : ℝ) : ℝ := if 0 ≤ x then alpha else 0

lemma Qimp_monotone {alpha : ℝ} (ha : 0 ≤ alpha) : Monotone (Qimp alpha) := by
  intro a b hab
  unfold Qimp
  by_cases h1 : 0 ≤ a
  · have h2 : 0 ≤ b := le_trans h1 hab
    simp [h1, h2]
  · by_cases h2 : 0 ≤ b
    · simp [h1, h2, ha]
    · simp [h1, h2]

/-- Kim-Son's impulsive band from the general criterion: hit iff `y < α`. -/
theorem impulse_hit_iff {alpha mu y : ℝ} (ha : 0 ≤ alpha) (hC : 0 < mu + y ^ 2 / 2) :
    (∃ x, 0 < x ∧ Fray (Qimp alpha) mu y x = 0) ↔ y < alpha := by
  rw [hit_iff (Qimp_monotone ha) hC]
  constructor
  · rintro ⟨s, hs⟩
    unfold Qimp at hs
    by_cases h : 0 ≤ s
    · simpa [h] using hs
    · simp only [h, ite_false] at hs
      linarith
  · intro h
    exact ⟨0, by simp [Qimp, h]⟩

/-! ## Finite total flux: the event-horizon statement -/

/-- If the total flux is `E` (so `Q ≤ E` everywhere and `Q` reaches every value
below `E`), then the ray `x_m = -y` is hit iff `y < E`. -/
theorem finite_total_flux_hit_iff (hQ : Monotone Q) {mu y E : ℝ} (hC : 0 < mu + y ^ 2 / 2)
    (hle : ∀ s, Q s ≤ E) (hsup : ∀ e, e < E → ∃ s, e < Q s) :
    (∃ x, 0 < x ∧ Fray Q mu y x = 0) ↔ y < E := by
  rw [hit_iff hQ hC]
  constructor
  · rintro ⟨s, hs⟩
    exact lt_of_lt_of_le hs (hle s)
  · intro h
    exact hsup y h

/-! ## Linear bounds, escaping rays, and the region after a pulse -/

/-- If `Q ≤ E` everywhere then `F ≥ C + (y - E) x` for `x ≥ 0`.  For `E < y`
this is the linear growth of the excess along an escaping ray. -/
lemma Fray_ge_linear (hQ : Monotone Q) {mu y E x : ℝ} (hle : ∀ s, Q s ≤ E) (hx : 0 ≤ x) :
    mu + y ^ 2 / 2 + (y - E) * x ≤ Fray Q mu y x := by
  have hint : ∀ a b : ℝ, IntervalIntegrable Q volume a b := fun a b => hQ.intervalIntegrable
  have hmono : ∫ _s in (0 : ℝ)..x, (y - E) ≤ ∫ s in (0 : ℝ)..x, (y - Q s) := by
    apply intervalIntegral.integral_mono_on hx intervalIntegrable_const
      (intervalIntegrable_const.sub (hint 0 x))
    intro s _
    linarith [hle s]
  rw [intervalIntegral.integral_const, smul_eq_mul, sub_zero] at hmono
  have hsub := Fray_sub hQ mu y 0 x
  have h0 : Fray Q mu y 0 = mu + y ^ 2 / 2 := by simp [Fray]
  linarith

/-- If `Q ≥ 0` from onset then `F ≤ C + y x` for `x ≥ 0`. -/
lemma Fray_le_linear (hQ : Monotone Q) {mu y x : ℝ} (h0Q : 0 ≤ Q 0) (hx : 0 ≤ x) :
    Fray Q mu y x ≤ mu + y ^ 2 / 2 + y * x := by
  have hint : ∀ a b : ℝ, IntervalIntegrable Q volume a b := fun a b => hQ.intervalIntegrable
  have hmono : ∫ s in (0 : ℝ)..x, (y - Q s) ≤ ∫ _s in (0 : ℝ)..x, y := by
    apply intervalIntegral.integral_mono_on hx
      (intervalIntegrable_const.sub (hint 0 x)) intervalIntegrable_const
    intro s hs
    have := hQ hs.1
    linarith
  rw [intervalIntegral.integral_const, smul_eq_mul, sub_zero] at hmono
  have hsub := Fray_sub hQ mu y 0 x
  have h0 : Fray Q mu y 0 = mu + y ^ 2 / 2 := by simp [Fray]
  linarith

/-- The excess up to `x` depends only on the flux on `[0, x]` (domain of dependence). -/
lemma Fray_congr {Q' : ℝ → ℝ} {mu y x : ℝ} (hx : 0 ≤ x)
    (h : ∀ t, 0 ≤ t → t ≤ x → Q t = Q' t) : Fray Q mu y x = Fray Q' mu y x := by
  have hI : ∫ t in (0 : ℝ)..x, Q t = ∫ t in (0 : ℝ)..x, Q' t := by
    apply intervalIntegral.integral_congr
    intro t ht
    rw [Set.uIcc_of_le hx] at ht
    exact h t ht.1 ht.2
  simp only [Fray, hI]

/-- After the flux has stopped (`Q = E` on `[s, ∞)`), the excess is linear in `x`. -/
lemma Fray_after_const (hQ : Monotone Q) {mu y E s x : ℝ} (hconst : ∀ t, s ≤ t → Q t = E)
    (hsx : s ≤ x) : Fray Q mu y x = Fray Q mu y s + (y - E) * (x - s) := by
  have hsub := Fray_sub hQ mu y s x
  have hcongr : ∫ t in s..x, (y - Q t) = ∫ _t in s..x, (y - E) := by
    apply intervalIntegral.integral_congr
    intro t ht
    rw [Set.uIcc_of_le hsx] at ht
    simp [hconst t ht.1]
  rw [hcongr, intervalIntegral.integral_const, smul_eq_mul] at hsub
  linarith

/-- Root of the linear after-pulse excess. -/
lemma after_pulse_root {Fs y E s x : ℝ} (hyE : y < E) :
    Fs + (y - E) * (x - s) = 0 ↔ x = s + Fs / (E - y) := by
  have h : E - y ≠ 0 := by linarith
  have e : Fs / (E - y) * (E - y) = Fs := div_mul_cancel₀ Fs h
  constructor
  · intro h0
    have hx : x - s = Fs / (E - y) := by
      rw [eq_div_iff h]
      linarith
    linarith
  · intro hx
    rw [hx]
    linarith

/-- Closed form of the after-pulse hit for a uniform pulse `E = p s`. -/
lemma pulse_after_formula {p s mu y : ℝ} (hyE : y < p * s) :
    s + (mu + y ^ 2 / 2 + y * s - p * s ^ 2 / 2) / (p * s - y)
      = (mu + y ^ 2 / 2 + p * s * s / 2) / (p * s - y) := by
  have h : p * s - y ≠ 0 := by linarith
  rw [eq_div_iff h, add_mul, div_mul_cancel₀ _ h]
  ring

/-- The ray is captured during a uniform pulse of length `s` exactly when
`y ≤ -s + √((1+p) s² - 2 μ)`. -/
lemma pulse_during_iff {p s mu y : ℝ} (hy : 0 < y) (hs : 0 ≤ s) :
    mu + y ^ 2 / 2 + y * s - p * s ^ 2 / 2 ≤ 0
      ↔ y ≤ -s + Real.sqrt ((1 + p) * s ^ 2 - 2 * mu) := by
  have hpos : 0 < y + s := by linarith
  have hiff : y ≤ -s + Real.sqrt ((1 + p) * s ^ 2 - 2 * mu)
      ↔ y + s ≤ Real.sqrt ((1 + p) * s ^ 2 - 2 * mu) := by
    constructor <;> intro h <;> linarith
  rw [hiff, Real.le_sqrt' hpos]
  constructor <;> intro h <;> nlinarith [h]

end AdS2RST
