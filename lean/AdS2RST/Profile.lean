import Mathlib

/-!
# Chiral profiles and the sector formulas

In Kruskal gauge the RST constraint is `κ t_± = √κ ∂_±² Ω + T_±±`.  With
`Ω = Ω_s + L · F̂`, `L = λ²/√κ`, the general solution is

  `F̂(x_p, x_m) = μ - x_p x_m + a_+(x_p) + a_-(x_m)`,

where `a_±'' = (κ/λ²) t_± - T_±±/λ²`.  This file constructs the profile for
the Kim-Son state `t = (λ²/κ) θ(-x)`, proves that it is the `C¹` solution of
`a'' = θ(-x)` with `a(0) = a'(0) = 0`, and derives the sector formulas.  The
matter profile enters through an arbitrary primitive `A` of the cumulative
flux; see `Cumulative.lean`.
-/

namespace AdS2RST

open Set

/-- Normalized state profile for `t = (λ²/κ) θ(-x)`. -/
noncomputable def aState (x : ℝ) : ℝ := (min x 0) ^ 2 / 2

lemma aState_of_nonpos {x : ℝ} (hx : x ≤ 0) : aState x = x ^ 2 / 2 := by
  simp [aState, min_eq_left hx]

lemma aState_of_nonneg {x : ℝ} (hx : 0 ≤ x) : aState x = 0 := by
  simp [aState, min_eq_right hx]

lemma aState_zero : aState 0 = 0 := aState_of_nonneg le_rfl

lemma aState_nonneg (x : ℝ) : 0 ≤ aState x := by
  unfold aState
  positivity

/-- The state profile is differentiable everywhere, with derivative `min x 0`.
In particular it is `C¹` across the onset point. -/
lemma aState_hasDerivAt (x : ℝ) : HasDerivAt aState (min x 0) x := by
  have hsq : ∀ z : ℝ, HasDerivAt (fun w : ℝ => w ^ 2 / 2) z z := by
    intro z
    have h := ((hasDerivAt_id z).pow 2).div_const 2
    convert h using 1 <;> simp
  rcases lt_trichotomy x 0 with h | h | h
  · rw [min_eq_left h.le]
    have hev : aState =ᶠ[nhds x] fun w : ℝ => w ^ 2 / 2 := by
      filter_upwards [Iio_mem_nhds h] with w hw
      exact aState_of_nonpos (le_of_lt hw)
    exact (hsq x).congr_of_eventuallyEq hev
  · subst h
    rw [min_self]
    have h1 : HasDerivWithinAt aState 0 (Iic 0) 0 :=
      ((hsq 0).hasDerivWithinAt).congr (fun w hw => aState_of_nonpos hw) (aState_of_nonpos le_rfl)
    have h2 : HasDerivWithinAt aState 0 (Ici 0) 0 :=
      ((hasDerivAt_const (0 : ℝ) (0 : ℝ)).hasDerivWithinAt).congr
        (fun w hw => aState_of_nonneg hw) (aState_of_nonneg le_rfl)
    have h3 := h1.union h2
    rwa [Iic_union_Ici, hasDerivWithinAt_univ] at h3
  · rw [min_eq_right h.le]
    have hev : aState =ᶠ[nhds x] fun _ : ℝ => (0 : ℝ) := by
      filter_upwards [Ioi_mem_nhds h] with w hw
      exact aState_of_nonneg (le_of_lt hw)
    exact (hasDerivAt_const x (0 : ℝ)).congr_of_eventuallyEq hev

/-- Second derivative before onset: `a'' = 1`, the retained state `t = λ²/κ`. -/
lemma aState_second_deriv_neg {x : ℝ} (hx : x < 0) :
    HasDerivAt (fun w : ℝ => min w 0) 1 x := by
  have hev : (fun w : ℝ => min w 0) =ᶠ[nhds x] fun w : ℝ => w := by
    filter_upwards [Iio_mem_nhds hx] with w hw
    exact min_eq_left (le_of_lt hw)
  exact (hasDerivAt_id x).congr_of_eventuallyEq hev

/-- Second derivative after onset: `a'' = 0`, the state is switched off. -/
lemma aState_second_deriv_pos {x : ℝ} (hx : 0 < x) :
    HasDerivAt (fun w : ℝ => min w 0) 0 x := by
  have hev : (fun w : ℝ => min w 0) =ᶠ[nhds x] fun _ : ℝ => (0 : ℝ) := by
    filter_upwards [Ioi_mem_nhds hx] with w hw
    exact min_eq_right (le_of_lt hw)
  exact (hasDerivAt_const x (0 : ℝ)).congr_of_eventuallyEq hev

/-- Normalized excess `F̂ = (Ω - Ω_s)/L` for the Kim-Son state and an incoming
matter profile `A` (a primitive of the cumulative flux with `A = 0` before onset). -/
noncomputable def Fhat (mu : ℝ) (A : ℝ → ℝ) (xp xm : ℝ) : ℝ :=
  mu - xp * xm + aState xp + aState xm - A xp

/-- Pre-onset sector: the static Kim-Son wormhole. -/
lemma Fhat_pre (mu : ℝ) (A : ℝ → ℝ) {xp xm : ℝ} (hp : xp ≤ 0) (hm : xm ≤ 0) (hA : A xp = 0) :
    Fhat mu A xp xm = mu + (xp - xm) ^ 2 / 2 := by
  rw [Fhat, aState_of_nonpos hp, aState_of_nonpos hm, hA]
  ring

/-- Mixed sector `x_p ≥ 0 ≥ x_m`, written on the ray `x_m = -y`. -/
lemma Fhat_mixed (mu : ℝ) (A : ℝ → ℝ) {xp y : ℝ} (hp : 0 ≤ xp) (hy : 0 ≤ y) :
    Fhat mu A xp (-y) = mu + y ^ 2 / 2 + y * xp - A xp := by
  rw [Fhat, aState_of_nonneg hp, aState_of_nonpos (neg_nonpos.mpr hy)]
  ring

/-- Both-positive sector. -/
lemma Fhat_post (mu : ℝ) (A : ℝ → ℝ) {xp xm : ℝ} (hp : 0 ≤ xp) (hm : 0 ≤ xm) :
    Fhat mu A xp xm = mu - xp * xm - A xp := by
  rw [Fhat, aState_of_nonneg hp, aState_of_nonneg hm]
  ring

/-- Mirror mixed sector `x_p ≤ 0 ≤ x_m`: no classical matter reaches it. -/
lemma Fhat_mirror (mu : ℝ) (A : ℝ → ℝ) {xp xm : ℝ} (hp : xp ≤ 0) (hm : 0 ≤ xm) (hA : A xp = 0) :
    Fhat mu A xp xm = mu - xp * xm + xp ^ 2 / 2 := by
  rw [Fhat, aState_of_nonpos hp, aState_of_nonneg hm, hA]
  ring

/-- The field equation `∂_+ ∂_- F̂ = -1` holds for any profiles: the `x_m`
derivative of `F̂` is `-x_p + a_-'(x_m)`, whose `x_p` derivative is `-1`. -/
lemma Fhat_hasDerivAt_xm (mu : ℝ) (A : ℝ → ℝ) (xp xm : ℝ) :
    HasDerivAt (fun w : ℝ => Fhat mu A xp w) (-xp + min xm 0) xm := by
  unfold Fhat
  have h1 : HasDerivAt (fun w : ℝ => mu - xp * w) (-xp) xm := by
    have h := ((hasDerivAt_id xm).const_mul xp).const_sub mu
    convert h using 1 <;> simp
  have h2 := (h1.add (aState_hasDerivAt xm))
  have h3 := (h2.add_const (aState xp - A xp))
  convert h3 using 1
  funext w
  simp only [Pi.add_apply]
  ring

lemma mixed_derivative_field_equation (xm : ℝ) (xp : ℝ) :
    HasDerivAt (fun w : ℝ => -w + min xm 0) (-1) xp := by
  have h := ((hasDerivAt_id xp).neg).add_const (min xm 0)
  simpa using h

end AdS2RST
