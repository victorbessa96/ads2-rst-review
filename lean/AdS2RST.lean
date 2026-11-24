import Mathlib

/-!
# Algebraic core of the AdS2-RST wall theorems

This file proves the sustained mixed-ray root, its uniqueness, the other root's
sign, the negative wall slope, and the after-shutoff both-positive sign domain.
It contains no `sorry` placeholders and no physics-level absorber assumptions.
-/

namespace AdS2RST

variable (p y mu : ℝ)

/-- Alternate retained-t_+ mixed-region excess. -/
noncomputable abbrev FAlt (x : ℝ) : ℝ := mu + y ^ 2 / 2 + x * y + (1 - p) * x ^ 2 / 2

/-- Positive square-root discriminant of the sustained wall equation. -/
noncomputable abbrev D : ℝ := Real.sqrt ((1 + p) * y ^ 2 + 2 * p * mu)

/-- The positive candidate first-hit coordinate. -/
noncomputable abbrev xHit : ℝ := (y + D p y mu) / p

/-- Normalized sustained mixed-region excess. -/
noncomputable abbrev F (x : ℝ) : ℝ := mu + y ^ 2 / 2 + x * y - p * x ^ 2 / 2

lemma D_sq (hp : 0 < p) (hy : 0 < y) (hmu : 0 ≤ mu) :
    (D p y mu) ^ 2 = (1 + p) * y ^ 2 + 2 * p * mu := by
  rw [D]
  exact Real.sq_sqrt (by positivity)

lemma D_gt_y (hp : 0 < p) (hy : 0 < y) (hmu : 0 ≤ mu) :
    y < D p y mu := by
  rw [D]
  apply (Real.lt_sqrt (le_of_lt hy)).mpr
  have hpy : 0 < p * y ^ 2 + 2 * p * mu := by positivity
  nlinarith [hpy]

lemma xHit_pos (hp : 0 < p) (hy : 0 < y) (hmu : 0 ≤ mu) :
    0 < xHit p y mu := by
  dsimp [xHit]
  apply div_pos _ hp
  exact add_pos_of_pos_of_nonneg hy (Real.sqrt_nonneg _)

lemma F_xHit (hp : 0 < p) (hy : 0 < y) (hmu : 0 ≤ mu) :
    F p y mu (xHit p y mu) = 0 := by
  have hD := D_sq p y mu hp hy hmu
  dsimp [F, xHit]
  field_simp [hp.ne']
  nlinarith [hD]

lemma other_root_neg (hp : 0 < p) (hy : 0 < y) (hmu : 0 ≤ mu) :
    (y - D p y mu) / p < 0 := by
  apply div_neg_of_neg_of_pos
  · linarith [D_gt_y p y mu hp hy hmu]
  · exact hp

/-- The sustained wall has a unique positive post-onset hit. -/
lemma F_eq_zero_iff (hp : 0 < p) (hy : 0 < y) (hmu : 0 ≤ mu)
    {x : ℝ} (hx : 0 < x) : F p y mu x = 0 ↔ x = xHit p y mu := by
  have hD := D_sq p y mu hp hy hmu
  constructor
  · intro hzero
    have hform : (p * x - y) ^ 2 = (D p y mu) ^ 2 := by
      dsimp [F] at hzero
      simp only [D] at hD
      nlinarith [hD]
    have hfactor : (p * x - y - D p y mu) * (p * x - y + D p y mu) = 0 := by
      nlinarith [hform]
    rcases mul_eq_zero.mp hfactor with hplus | hminus
    · change x = (y + D p y mu) / p
      field_simp [hp.ne']
      linarith
    · have hxother : x = (y - D p y mu) / p := by
        field_simp [hp.ne']
        linarith
      have hneg := other_root_neg p y mu hp hy hmu
      rw [hxother] at hx
      exact (lt_asymm hx hneg).elim
  · intro hxeq
    subst x
    exact F_xHit p y mu hp hy hmu

/-- The mixed-wall tangent is negative, hence spacelike in the actual metric. -/
lemma slope_neg (hp : 0 < p) (hy : 0 < y) (hmu : 0 ≤ mu) :
    -D p y mu / (xHit p y mu + y) < 0 := by
  have hden : 0 < xHit p y mu + y := by
    have hx := xHit_pos p y mu hp hy hmu
    linarith
  have hDpos : 0 < D p y mu := lt_trans hy (D_gt_y p y mu hp hy hmu)
  exact div_neg_of_neg_of_pos (by linarith [hDpos]) hden

/-- Derivative numerator used by the implicit wall-tangent argument. -/
lemma F_x_at_xHit (hp : 0 < p) (hy : 0 < y) (hmu : 0 ≤ mu) :
    y - p * xHit p y mu = -D p y mu := by
  dsimp [xHit]
  field_simp [hp.ne']
  ring

/-- Actual derivative of the two-variable excess with respect to y. -/
lemma F_hasDerivAt_y (x : ℝ) : HasDerivAt (fun y : ℝ => F p y mu x) (x + y) y := by
  dsimp [F]
  convert (((hasDerivAt_const y mu).add (((hasDerivAt_id y).pow 2).div_const 2)).add
    ((hasDerivAt_const y x).mul (hasDerivAt_id y))).sub (hasDerivAt_const y (p * x ^ 2 / 2)) using 1
  · funext z
    simp [id_eq]
  · simp [id_eq]
    ring

/-- Factorization with the positive and negative quadratic roots. -/
lemma F_factor (x : ℝ) (hp : 0 < p) (hy : 0 < y) (hmu : 0 ≤ mu) :
    F p y mu x = -(p / 2) * (x - xHit p y mu) * (x - (y - D p y mu) / p) := by
  have hD := D_sq p y mu hp hy hmu
  dsimp [F, xHit]
  field_simp [hp.ne']
  nlinarith [hD]

/-- Physical side before the first positive hit. -/
lemma F_pos_before (x : ℝ) (hp : 0 < p) (hy : 0 < y) (hmu : 0 ≤ mu)
    (hx : 0 < x) (hxhit : x < xHit p y mu) : 0 < F p y mu x := by
  rw [F_factor p y mu x hp hy hmu]
  have hother := other_root_neg p y mu hp hy hmu
  have hleft : 0 < x - (y - D p y mu) / p := by linarith
  have hright : x - xHit p y mu < 0 := sub_neg.mpr hxhit
  have hprod : (x - xHit p y mu) * (x - (y - D p y mu) / p) < 0 :=
    mul_neg_of_neg_of_pos hright hleft
  nlinarith [hprod, hp]

/-- Excluded side after the first positive hit. -/
lemma F_neg_after (x : ℝ) (hp : 0 < p) (hy : 0 < y) (hmu : 0 ≤ mu)
    (hxhit : xHit p y mu < x) : F p y mu x < 0 := by
  rw [F_factor p y mu x hp hy hmu]
  have hother := other_root_neg p y mu hp hy hmu
  have hxpos : 0 < x := lt_trans (xHit_pos p y mu hp hy hmu) hxhit
  have hleft : 0 < x - (y - D p y mu) / p := by linarith
  have hright : 0 < x - xHit p y mu := sub_pos.mpr hxhit
  have hprod : 0 < (x - xHit p y mu) * (x - (y - D p y mu) / p) := mul_pos hright hleft
  nlinarith [hprod, hp]

/-- General cumulative-flux slope sign once Q(x_hit)>y. -/
lemma general_wall_slope_neg (Q x y : ℝ) (hx : 0 < x) (hy : 0 < y) (hQy : y < Q) :
    -(Q - y) / (x + y) < 0 := by
  apply div_neg_of_neg_of_pos
  · linarith
  · linarith

/-- Zero crossing of the after-shutoff both-positive branch. -/
noncomputable abbrev x0 (s mu E : ℝ) : ℝ := s / 2 + mu / E

/-- After-shutoff both-positive wall expression. -/
noncomputable abbrev zAfter (s mu E x : ℝ) : ℝ := (mu + E * s / 2) / x - E

lemma zAfter_eq (s mu E x : ℝ) (hE : 0 < E) (hx : 0 < x) :
    zAfter s mu E x = E * (x0 s mu E / x - 1) := by
  dsimp [zAfter, x0]
  field_simp [hx.ne', hE.ne']
  ring

/-- Exact sign of the after-shutoff expression. -/
lemma zAfter_pos_iff (s mu E x : ℝ) (hE : 0 < E) (hx : 0 < x) :
    0 < zAfter s mu E x ↔ x < x0 s mu E := by
  rw [zAfter_eq s mu E x hE hx]
  constructor
  · intro h
    have hfac : 0 < x0 s mu E / x - 1 := (mul_pos_iff_of_pos_left hE).mp h
    have hone : 1 < x0 s mu E / x := sub_pos.mp hfac
    exact (one_lt_div hx).mp hone
  · intro hx0
    have hone : 1 < x0 s mu E / x := (one_lt_div hx).mpr hx0
    have hfac : 0 < x0 s mu E / x - 1 := sub_pos.mpr hone
    exact mul_pos hE hfac

lemma zAfter_neg_of_gt (s mu E x : ℝ) (hE : 0 < E) (hx : 0 < x)
    (hx0 : x0 s mu E < x) : zAfter s mu E x < 0 := by
  rw [zAfter_eq s mu E x hE hx]
  have hdiv : x0 s mu E / x < 1 := (div_lt_one hx).mpr hx0
  exact mul_neg_of_pos_of_neg hE (sub_neg.mpr hdiv)

lemma zAfter_zero (s mu E : ℝ) (hE : 0 < E) (hs : 0 < s) (hmu : 0 ≤ mu) :
    zAfter s mu E (x0 s mu E) = 0 := by
  have hx0pos : 0 < x0 s mu E := by
    have hdiv : 0 ≤ mu / E := div_nonneg hmu (le_of_lt hE)
    have hs2 : 0 < s / 2 := by positivity
    exact add_pos_of_pos_of_nonneg hs2 hdiv
  rw [zAfter_eq s mu E (x0 s mu E) hE hx0pos]
  simp [div_self (ne_of_gt hx0pos)]

/-- Exact interval invariant used by the automated package checks. -/
lemma x0_sub_s (s mu E : ℝ) (hE : 0 < E) :
    x0 s mu E - s = (2 * mu - E * s) / (2 * E) := by
  dsimp [x0]
  field_simp [hE.ne']
  ring

/-- The after-shutoff both-positive interval exists iff mu > E*s/2. -/
lemma after_interval_nonempty_iff (s mu E : ℝ) (hE : 0 < E) :
    s < x0 s mu E ↔ mu > E * s / 2 := by
  have hEq := x0_sub_s s mu E hE
  constructor
  · intro h
    have hnum : 0 < (2 * mu - E * s) / (2 * E) := by linarith [hEq]
    have hden : 0 < 2 * E := by positivity
    have htop : 0 < 2 * mu - E * s := by
      have hmul : 0 < ((2 * mu - E * s) / (2 * E)) * (2 * E) := mul_pos hnum hden
      have hcancel : ((2 * mu - E * s) / (2 * E)) * (2 * E) = 2 * mu - E * s := by
        field_simp [hE.ne']
      rwa [hcancel] at hmul
    linarith
  · intro h
    have htop : 0 < 2 * mu - E * s := by linarith
    have hnum : 0 < (2 * mu - E * s) / (2 * E) := div_pos htop (by positivity)
    linarith [hEq]

/-- The retained step-off is exactly the alternate t_+-on mixed sector with p_eff=1+p. -/
lemma retained_state_equiv (x : ℝ) : FAlt (1 + p) y mu x = F p y mu x := by
  dsimp [FAlt, F]
  ring

/-- Small-p observer-coordinate stress scaling after P=lambda^2*p. -/
lemma stress_scaling (lam y p : ℝ) (hp : 0 < p) :
    lam * (lam ^ 2 * p) * (2 * y / p) ^ 2 / 2 = 2 * lam ^ 3 * y ^ 2 / p := by
  field_simp [hp.ne']

/-- Reviewer's concrete sign counterexample: x_m(4)=5/8. -/
example : zAfter 3 10 3 4 = 5 / 8 := by
  norm_num [zAfter]

/-- Reviewer's concrete sign counterexample: x_m(5)=-1/10. -/
example : zAfter 3 10 3 5 = -1 / 10 := by
  norm_num [zAfter]

example : x0 3 10 3 = 29 / 6 := by
  norm_num [x0]

example : x0 3 10 3 - 3 = (2 * 10 - 3 * 3) / (2 * 3) := by
  norm_num [x0]

/-- Abstract intermediate-value form of the signed accumulated-excess criterion. -/
lemma first_hit_iff {A : ℝ → ℝ} {C : ℝ} (hA : Continuous A) (hA0 : A 0 = 0) (hC : 0 < C) :
    (∃ z > 0, A z = C) ↔ ∃ x > 0, C ≤ A x := by
  constructor
  · rintro ⟨z, hz, hEq⟩
    exact ⟨z, hz, hEq.ge⟩
  · rintro ⟨x, hx, hAx⟩
    have hsubset := intermediate_value_Ioc (f := A) (a := 0) (b := x) hx.le hA.continuousOn
    have hmem : C ∈ Set.Ioc (A 0) (A x) := by
      rw [hA0]
      exact ⟨hC, hAx⟩
    rcases hsubset hmem with ⟨z, hz, hAz⟩
    exact ⟨z, hz.1, hAz⟩

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

end AdS2RST
