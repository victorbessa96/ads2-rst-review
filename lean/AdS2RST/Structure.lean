import Mathlib
import AdS2RST.Core
import AdS2RST.Profile
import AdS2RST.Cumulative

/-!
# Global structure: zero-flux wall, trapping, symmetries, the critical value

* With no classical matter (`A = 0`) the Kim-Son state alone produces a
  critical curve `x_p x_m = μ` in the both-positive quadrant, which is a
  trapped region.  The pre-onset wormhole and the mixed sector are regular.
* The symmetry classification of the three sectors.
* `Ω(φ) = √κ φ/2 + e^{-2φ}/√κ` has its global minimum `Ω_s` at
  `e^{-2φ} = κ/4`, and at weak coupling `e^{2φ} ≤ 1/(√κ Ω)`.
* Ordering of the apparent horizon and the wall under sustained flux.
-/

namespace AdS2RST

open Set

/-! ## Zero classical flux -/

/-- The zero matter profile. -/
def Azero : ℝ → ℝ := fun _ => 0

/-- With no matter, the both-positive sector is `μ - x_p x_m`. -/
lemma zero_flux_post (mu : ℝ) {xp xm : ℝ} (hp : 0 ≤ xp) (hm : 0 ≤ xm) :
    Fhat mu Azero xp xm = mu - xp * xm := by
  rw [Fhat_post mu Azero hp hm]
  simp [Azero]

/-- **Zero-flux wall.**  With no classical matter the critical curve in the
both-positive quadrant is the hyperbola `x_m = μ / x_p`. -/
theorem zero_flux_wall_iff (mu : ℝ) {xp xm : ℝ} (hp : 0 < xp) (hm : 0 < xm) :
    Fhat mu Azero xp xm = 0 ↔ xm = mu / xp := by
  rw [zero_flux_post mu hp.le hm.le]
  constructor
  · intro h
    field_simp
    linarith
  · intro h
    rw [h]
    field_simp
    ring

/-- The zero-flux wall is nonempty exactly when `μ > 0`: every `x_p > 0` carries a wall point. -/
theorem zero_flux_wall_exists {mu xp : ℝ} (hmu : 0 < mu) (hp : 0 < xp) :
    0 < mu / xp ∧ Fhat mu Azero xp (mu / xp) = 0 :=
  ⟨div_pos hmu hp, (zero_flux_wall_iff mu hp (div_pos hmu hp)).mpr rfl⟩

/-- The zero-flux wall is spacelike: `x_m = μ/x_p` has negative slope. -/
theorem zero_flux_wall_slope {mu xp : ℝ} (hmu : 0 < mu) (hp : 0 < xp) :
    HasDerivAt (fun w : ℝ => mu / w) (-mu / xp ^ 2) xp ∧ -mu / xp ^ 2 < 0 := by
  refine ⟨?_, ?_⟩
  · have h := (hasDerivAt_inv hp.ne').const_mul mu
    have hfun : (fun w : ℝ => mu / w) = fun w : ℝ => mu * w⁻¹ := by
      funext w
      rw [div_eq_mul_inv]
    have hval : -mu / xp ^ 2 = mu * -(xp ^ 2)⁻¹ := by
      rw [div_eq_mul_inv]
      ring
    rw [hfun, hval]
    exact h
  · apply div_neg_of_neg_of_pos <;> [linarith; positivity]

/-- Trapping in the `x_m` direction: `∂_- F̂ = -x_p < 0` in the both-positive quadrant. -/
theorem zero_flux_trapped_minus (mu : ℝ) {xp xm : ℝ} (hp : 0 < xp) (hm : 0 < xm) :
    HasDerivAt (fun w : ℝ => Fhat mu Azero xp w) (-xp) xm ∧ -xp < 0 := by
  refine ⟨?_, by linarith⟩
  have h := Fhat_hasDerivAt_xm mu Azero xp xm
  rwa [min_eq_right hm.le, add_zero] at h

/-- Trapping in the `x_p` direction: `∂_+ F̂ = -x_m < 0` in the both-positive quadrant. -/
theorem zero_flux_trapped_plus (mu : ℝ) {xp xm : ℝ} (hp : 0 < xp) (hm : 0 < xm) :
    HasDerivAt (fun w : ℝ => Fhat mu Azero w xm) (-xm) xp ∧ -xm < 0 := by
  refine ⟨?_, by linarith⟩
  have hev : (fun w : ℝ => Fhat mu Azero w xm) =ᶠ[nhds xp] fun w : ℝ => mu - w * xm := by
    filter_upwards [Ioi_mem_nhds hp] with w hw
    exact zero_flux_post mu (le_of_lt hw) hm.le
  have h : HasDerivAt (fun w : ℝ => mu - w * xm) (-xm) xp := by
    have h0 := ((hasDerivAt_id xp).mul_const xm).const_sub mu
    simpa using h0
  exact h.congr_of_eventuallyEq hev

/-- The pre-onset wormhole is regular: `F̂ ≥ μ > 0`. -/
theorem wormhole_regular {mu : ℝ} (A : ℝ → ℝ) {xp xm : ℝ} (hp : xp ≤ 0) (hm : xm ≤ 0)
    (hA : A xp = 0) : mu ≤ Fhat mu A xp xm := by
  rw [Fhat_pre mu A hp hm hA]
  nlinarith [sq_nonneg (xp - xm)]

/-- With no matter, the mixed sector is regular. -/
theorem zero_flux_mixed_regular {mu : ℝ} (hmu : 0 < mu) {xp y : ℝ} (hp : 0 ≤ xp) (hy : 0 ≤ y) :
    0 < Fhat mu Azero xp (-y) := by
  rw [Fhat_mixed mu Azero hp hy]
  simp only [Azero, sub_zero]
  have : 0 ≤ y * xp := mul_nonneg hy hp
  nlinarith [sq_nonneg y]

/-- The mirror mixed sector is regular for any incoming profile. -/
theorem mirror_regular {mu : ℝ} (hmu : 0 < mu) (A : ℝ → ℝ) {xp xm : ℝ} (hp : xp ≤ 0)
    (hm : 0 ≤ xm) (hA : A xp = 0) : 0 < Fhat mu A xp xm := by
  rw [Fhat_mirror mu A hp hm hA]
  have : 0 ≤ -xp * xm := mul_nonneg (neg_nonneg.mpr hp) hm
  nlinarith [sq_nonneg xp]

/-- If the state is never switched off, the wormhole formula holds on the whole
plane and there is no critical curve anywhere. -/
theorem eternal_wormhole_regular {mu : ℝ} (hmu : 0 < mu) (xp xm : ℝ) :
    0 < mu + (xp - xm) ^ 2 / 2 := by
  nlinarith [sq_nonneg (xp - xm)]

/-! ## Symmetries

A symmetry of the solution preserves the dilaton, hence `Ω`, and the metric
`-e^{2ρ(Ω)} dx_p dx_m`.  A conformal Killing field `ξ_p(x_p) ∂_p + ξ_m(x_m) ∂_m`
with `ξ(Ω) = 0` is Killing iff `ξ_p' + ξ_m' = 0`, so
`ξ = (a + c x_p) ∂_p + (b - c x_m) ∂_m`.  The lemmas below classify which of
these annihilate `F̂` in each sector. -/

/-- Pre-onset wormhole: exactly the time translation `∂_p + ∂_m`. -/
theorem symmetry_pre (a b c : ℝ) :
    (∀ xp xm : ℝ, xp < 0 → xm < 0 →
      (a + c * xp) * (xp - xm) + (b - c * xm) * (-(xp - xm)) = 0) ↔ (a = b ∧ c = 0) := by
  constructor
  · intro h
    have h1 := h (-1) (-2) (by norm_num) (by norm_num)
    have h2 := h (-2) (-1) (by norm_num) (by norm_num)
    have h3 := h (-1) (-3) (by norm_num) (by norm_num)
    constructor <;> linarith
  · rintro ⟨rfl, rfl⟩ xp xm _ _
    ring

/-- Zero-flux both-positive sector: exactly the boost `x_p ∂_p - x_m ∂_m`. -/
theorem symmetry_post (a b c : ℝ) :
    (∀ xp xm : ℝ, 0 < xp → 0 < xm →
      (a + c * xp) * (-xm) + (b - c * xm) * (-xp) = 0) ↔ (a = 0 ∧ b = 0) := by
  constructor
  · intro h
    have h1 := h 1 1 (by norm_num) (by norm_num)
    have h2 := h 1 2 (by norm_num) (by norm_num)
    constructor <;> linarith
  · rintro ⟨rfl, rfl⟩ xp xm _ _
    ring

/-- Zero-flux mixed sector `F̂ = μ - x_p x_m + x_m²/2`: no symmetry at all. -/
theorem symmetry_mixed (a b c : ℝ) :
    (∀ xp xm : ℝ, 0 < xp → xm < 0 →
      (a + c * xp) * (-xm) + (b - c * xm) * (-xp + xm) = 0) ↔ (a = 0 ∧ b = 0 ∧ c = 0) := by
  constructor
  · intro h
    have h1 := h 1 (-1) (by norm_num) (by norm_num)
    have h2 := h 2 (-1) (by norm_num) (by norm_num)
    have h3 := h 1 (-2) (by norm_num) (by norm_num)
    refine ⟨?_, ?_, ?_⟩ <;> linarith
  · rintro ⟨rfl, rfl, rfl⟩ xp xm _ _
    ring

/-! ## The RST field variable `Ω(φ)` -/

/-- `Ω` as a function of the dilaton. -/
noncomputable def OmegaOf (kappa phi : ℝ) : ℝ :=
  Real.sqrt kappa * phi / 2 + Real.exp (-2 * phi) / Real.sqrt kappa

/-- The RST critical value. -/
noncomputable def OmegaCrit (kappa : ℝ) : ℝ :=
  Real.sqrt kappa / 4 * (1 - Real.log (kappa / 4))

/-- The critical dilaton, `e^{-2φ_s} = κ/4`. -/
noncomputable def phiCrit (kappa : ℝ) : ℝ := -Real.log (kappa / 4) / 2

lemma exp_phiCrit {kappa : ℝ} (hk : 0 < kappa) : Real.exp (-2 * phiCrit kappa) = kappa / 4 := by
  have : -2 * phiCrit kappa = Real.log (kappa / 4) := by
    unfold phiCrit
    ring
  rw [this, Real.exp_log (by positivity)]

/-- `Ω(φ_s) = Ω_s`. -/
theorem OmegaOf_phiCrit {kappa : ℝ} (hk : 0 < kappa) :
    OmegaOf kappa (phiCrit kappa) = OmegaCrit kappa := by
  have hs : 0 < Real.sqrt kappa := Real.sqrt_pos.mpr hk
  have hsq : Real.sqrt kappa * Real.sqrt kappa = kappa := Real.mul_self_sqrt hk.le
  unfold OmegaOf OmegaCrit
  rw [exp_phiCrit hk]
  unfold phiCrit
  field_simp
  nlinarith [hsq]

/-- `Ω_s` is the global minimum of `Ω(φ)`: the critical curve bounds the range of `Ω`. -/
theorem OmegaCrit_le {kappa : ℝ} (hk : 0 < kappa) (phi : ℝ) :
    OmegaCrit kappa ≤ OmegaOf kappa phi := by
  have hs : 0 < Real.sqrt kappa := Real.sqrt_pos.mpr hk
  have hsq : Real.sqrt kappa * Real.sqrt kappa = kappa := Real.mul_self_sqrt hk.le
  have hk4 : 0 < kappa / 4 := by positivity
  -- e^t ≥ 1 + t with t = -2φ - log(κ/4)
  have hexp := Real.add_one_le_exp (-2 * phi - Real.log (kappa / 4))
  have hsplit : Real.exp (-2 * phi - Real.log (kappa / 4)) = Real.exp (-2 * phi) / (kappa / 4) := by
    rw [Real.exp_sub, Real.exp_log hk4]
  rw [hsplit] at hexp
  have hbound : kappa / 4 * (-2 * phi - Real.log (kappa / 4) + 1) ≤ Real.exp (-2 * phi) := by
    have := mul_le_mul_of_nonneg_left hexp hk4.le
    rwa [mul_div_cancel₀ _ hk4.ne'] at this
  unfold OmegaOf OmegaCrit
  rw [← sub_nonneg]
  have hgoal : Real.sqrt kappa * phi / 2 + Real.exp (-2 * phi) / Real.sqrt kappa
      - Real.sqrt kappa / 4 * (1 - Real.log (kappa / 4))
      = (Real.exp (-2 * phi) - kappa / 4 * (-2 * phi - Real.log (kappa / 4) + 1)) / Real.sqrt kappa := by
    have hsq2 : Real.sqrt kappa ^ 2 = kappa := Real.sq_sqrt hk.le
    field_simp
    rw [hsq2]
    ring
  rw [hgoal]
  exact div_nonneg (by linarith) hs.le

/-- Weak-coupling bound on the conformal factor in Kruskal gauge (`ρ = φ`):
`e^{2ρ} ≤ 1/(√κ Ω)` whenever `φ ≤ 0 < Ω`. -/
theorem conformal_factor_bound {kappa phi : ℝ} (hk : 0 < kappa) (hphi : phi ≤ 0)
    (hOm : 0 < OmegaOf kappa phi) :
    Real.exp (2 * phi) ≤ 1 / (Real.sqrt kappa * OmegaOf kappa phi) := by
  have hs : 0 < Real.sqrt kappa := Real.sqrt_pos.mpr hk
  have hsq : Real.sqrt kappa * Real.sqrt kappa = kappa := Real.mul_self_sqrt hk.le
  have hprod : Real.sqrt kappa * OmegaOf kappa phi = kappa * phi / 2 + Real.exp (-2 * phi) := by
    unfold OmegaOf
    field_simp
    nlinarith [hsq]
  have hle : Real.sqrt kappa * OmegaOf kappa phi ≤ Real.exp (-2 * phi) := by
    rw [hprod]
    nlinarith [mul_nonpos_of_nonneg_of_nonpos hk.le hphi]
  have hpos : 0 < Real.sqrt kappa * OmegaOf kappa phi := mul_pos hs hOm
  have hinv : Real.exp (2 * phi) = 1 / Real.exp (-2 * phi) := by
    rw [one_div, ← Real.exp_neg]
    congr 1
    ring
  rw [hinv]
  exact one_div_le_one_div_of_le hpos hle

/-! ## Affine length of the AdS₂ end

Along a null ray the affine parameter is `∫ e^{2ρ} dx`.  Near the AdS₂ end
`e^{2ρ} ≤ 2/(λ² X²)` by `conformal_factor_bound` and `Ω ≥ L X²/2`.  The
comparison integral is uniformly bounded. -/

theorem affine_tail_bounded {X : ℝ} (hX : 1 ≤ X) :
    ∫ x in (1 : ℝ)..X, 2 / x ^ 2 = 2 - 2 / X ∧ 2 - 2 / X < 2 := by
  refine ⟨?_, ?_⟩
  · have hderiv : ∀ x ∈ uIcc 1 X, HasDerivAt (fun w : ℝ => -2 / w) (2 / x ^ 2) x := by
      intro x hx
      rw [uIcc_of_le hX] at hx
      have hx0 : x ≠ 0 := by linarith [hx.1]
      have h := (hasDerivAt_inv hx0).const_mul (-2 : ℝ)
      have hfun : (fun w : ℝ => -2 / w) = fun w : ℝ => -2 * w⁻¹ := by
        funext w
        rw [div_eq_mul_inv]
      have hval : 2 / x ^ 2 = -2 * -(x ^ 2)⁻¹ := by
        rw [div_eq_mul_inv]
        ring
      rw [hfun, hval]
      exact h
    have hcont : ContinuousOn (fun x : ℝ => 2 / x ^ 2) (uIcc 1 X) := by
      apply ContinuousOn.div continuousOn_const (continuous_pow 2).continuousOn
      intro x hx
      rw [uIcc_of_le hX] at hx
      have hxpos : 0 < x := by linarith [hx.1]
      exact pow_ne_zero 2 hxpos.ne'
    rw [intervalIntegral.integral_eq_sub_of_hasDerivAt hderiv hcont.intervalIntegrable]
    have hX0 : X ≠ 0 := by linarith
    field_simp
    ring
  · have : 0 < 2 / X := by positivity
    linarith

/-- By contrast the linear-dilaton comparison integral `∫ dx/x` is unbounded. -/
theorem affine_future_unbounded (B : ℝ) : ∃ X : ℝ, 1 ≤ X ∧ B < ∫ x in (1 : ℝ)..X, 1 / x := by
  refine ⟨Real.exp (|B| + 1), ?_, ?_⟩
  · exact Real.one_le_exp (by positivity)
  · rw [integral_one_div_of_pos one_pos (Real.exp_pos _)]
    simp only [div_one, Real.log_exp]
    linarith [le_abs_self B]

/-! ## Sustained flux: apparent horizon precedes the wall -/

/-- On each mixed ray the apparent horizon `x = y/p` lies strictly before the wall. -/
theorem horizon_before_wall (p y mu : ℝ) (hp : 0 < p) (hy : 0 < y) (hmu : 0 ≤ mu) :
    y / p < xHit p y mu := by
  have hD : 0 < D p y mu := lt_trans hy (D_gt_y p y mu hp hy hmu)
  unfold xHit
  exact div_lt_div_of_pos_right (by linarith) hp

/-- The ray is still on the physical side at the apparent horizon. -/
theorem excess_pos_at_horizon (p y mu : ℝ) (hp : 0 < p) (hy : 0 < y) (hmu : 0 ≤ mu) :
    0 < F p y mu (y / p) :=
  F_pos_before p y mu (y / p) hp hy hmu (div_pos hy hp) (horizon_before_wall p y mu hp hy hmu)

/-! ## Retained incoming state: the threshold `P = λ²` -/

/-- With the incoming state retained and `p ≤ 1`, the mixed sector is regular. -/
lemma retained_state_regular {p y mu x : ℝ} (hp : p ≤ 1) (hmu : 0 < mu) (hy : 0 ≤ y)
    (hx : 0 ≤ x) : 0 < FAlt p y mu x := by
  have h1 : 0 ≤ (1 - p) * x ^ 2 := mul_nonneg (by linarith) (sq_nonneg x)
  have h2 : 0 ≤ x * y := mul_nonneg hx hy
  dsimp [FAlt]
  nlinarith [sq_nonneg y]

/-- With the incoming state retained, an outgoing ray is captured iff `p > 1`. -/
theorem retained_state_hit_iff {p y mu : ℝ} (hy : 0 < y) (hmu : 0 < mu) :
    (∃ x, 0 < x ∧ FAlt p y mu x = 0) ↔ 1 < p := by
  constructor
  · rintro ⟨x, hx, h0⟩
    by_contra hp
    have := retained_state_regular (not_lt.mp hp) hmu hy.le hx.le
    linarith
  · intro hp
    have hp' : 0 < p - 1 := by linarith
    refine ⟨xHit (p - 1) y mu, xHit_pos (p - 1) y mu hp' hy hmu.le, ?_⟩
    have h := F_xHit (p - 1) y mu hp' hy hmu.le
    have e : FAlt p y mu (xHit (p - 1) y mu) = F (p - 1) y mu (xHit (p - 1) y mu) := by
      dsimp only [FAlt, F]
      ring
    rw [e, h]

end AdS2RST
