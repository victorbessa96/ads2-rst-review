# Evaluation of the Kim-Son AdS2-RST one-sided-flux review package

**Scope.** I read the 11 narrative documents, `independent_symbolic.py`, `manifest.json`, `validation.json`, `validate_package.py`, `run_verification.sh`, `README.md` and `requirements.txt`. I did not run any script. `verify.py`, the zip contents (`sources/`, `reviews/`, `legacy/`, `outputs/`) and the TeX source were not in my context, so I could not read them. I re-derived the core mathematics by hand. This is an AI review, not the external human review the package leaves pending, and I won't fill in the sign-off form.

## 1. Verdict

**The mathematics is correct as far as I checked. The physical framing oversells it, and the verification and packaging claims are stronger than the evidence supports.** In the package's own vocabulary, that is **ACCEPT WITH WORDING CHANGES** on the theorems, and **PASS WITH INSTRUMENT CAVEATS** on reproduction.

## 2. What I re-derived by hand (all consistent)

- **Mixed-sector excess.** From Ω = B − L·x_p·x_m + a₊ + a₋ with L√κ/λ² = 1, I get F = μ + y²/2 + x·y − p·x²/2. The positive root is (y + D)/p with D² = (1+p)y² + 2pμ, and the other root is negative.
- **Spacelike edge.** F_x = −D at the hit and F_y = x + y, so dx_m/dx_p = −D/(x+y) < 0. With ds² = −e^{2ρ}dx_p dx_m, the edge is spacelike.
- **Global wall.** x_m = x − √((1+p)x² − 2μ) satisfies the wall equation.
- **Horizon ordering.** ∂_pΩ/L = y − p·x_p, so x_AH = y/p and x_hit − x_AH = D/p > 0.
- **Finite pulse.**
  - The chiral function for x > s has slope −Ps/√κ, which gives F_a = μ + y²/2 + Es/2 + x(y − E).
  - Pre-shutoff hits require y < y_max, and y_max < s(√(1+p) − 1) < ps = E, since √(1+p) < 1+p.
  - For y > y_max, F_d(s) > 0 and the linear branch crosses zero iff y < E.
  - The identity x_a − s = F_d(s)/(E − y) holds.
  - So "wall exactly for 0 < y < E" is a genuine iff.
  - The twelve-row census values I spot-checked (p=1, μ=0, s=2) are right.
- **Interior observers.**
  - The metric coefficients are correct.
  - With R = y/x_p and K = x_p·y, the wall polynomial is KR² + 2(K+μ)R − Kp = 0.
  - Q(p) = p[K(p+1) + 2μ] > 0, so R_w < p. Observers cross the horizon before the wall.
- **Finite conformal factor.** Ω_s and e^{2ρ} = 4/κ at the minimum are correct. Rejecting FR-09 is justified.
- **Impulsive case.** The sign (y − α) is right, giving a wall band 0 < y < α.

## 3. Substantive scientific concerns

**3.1 The "no critical flux" headline is mostly an artifact of the state choice.**
The package computes this but does not say it outright. In the alternate state with t₊ left on, F_alt has coefficient (1 − p)/2 and a mixed hit requires p > 1. The retained Kim-Son state (t₊ stepping off at x₀) gives −p/2, which is exactly the alternate problem with **p_eff = 1 + p**. So the t₊ step-off supplies the critical flux λ² by itself, and the sustained source only needs to add any p > 0. "Every ray, every p > 0" is therefore equivalent to "p_eff > 1 in the t₊-on picture". I recommend stating this equivalence as a corollary and moving it to the front. It changes how the headline reads.

**3.2 Constant in Kruskal x_p means exponentially growing in the observer frame.**
The package notes T_σσ = λ²x_p²P but treats it as a caveat. It is closer to a defining feature of the profile. The flux switches on at x_p = 0, which is σ → −∞. The σ-frame energy delivered up to x_p is ∫T_σσ dσ = λP·x_p²/2. At the hit for small p, x_hit ≈ 2y/p, so this is about 2λ³y²/p, which diverges as p → 0. "No threshold" is thus a Kruskal-coordinate statement, and an observer-frame energy budget would show a cost that grows as the flux weakens. I'd put this computation in the document rather than only warning against transferring the result.

**3.3 The observer results are weaker than their billing suggests.**
Constant-σ₁ curves are accelerated, interior and already trapped. Finite coordinate range plus a bounded e^ρ gives finite proper time almost automatically, so the "explicit" proper-time numbers are controls, not content. The stronger statement would be about all inextendible future-directed timelike curves in the trapped region, including free-fall geodesics. The package does not attempt this, and I would not assume it follows trivially.

**3.4 The single point of failure is not mechanically checked.**
The constraint integration (a_±'' = √κ·t_± − T/√κ, including sign and normalization) is only checked lexically against TeX line numbers. Everything downstream assumes it. A sign error would flip the physics. A reviewer should verify it against the paper, and the package says as much.

**3.5 Novelty.**
The narrowing against Kim-Son's impulsive wall band is honest and correct. The remaining contribution is a clean closed-form extension of known physics, not a new phenomenon. It reads as a note-level result.

## 4. Verification and packaging problems

1. **Check counts overstate independence.**
   - The 131 and 32 checks mostly test that entered candidates satisfy entered equations. The package admits this.
   - `independent_symbolic.py` comes from the same pipeline and shares the same candidate formulas, so "independent" means "separate script".
   - Some checks are weak or proxies. "alternate state p<1 coefficient is positive" tests `1 − 1/(1+r) > 0` for r > 0, which says nothing about 1 − p. Several positivity checks are sign-by-substitution (E = y + h).
2. **`validate_package.py` is partly theater.**
   - The `red_first_preserved` and `red_second_preserved` evidence strings are hardcoded text, and only file existence is checked.
   - `relocated_reproduction` reads an old receipt and compares one hash. It does not re-run anything.
   - `manifest_readback` runs right after writing the manifest, so it is nearly tautological.
   - Expected counts (131 and 32) are hardcoded.
3. **Documentation contradicts the code.**
   - Docs say scripts "write only under `outputs/`". `validate_package.py` rewrites `manifest.json` and `validation.json` at the package root with a fresh timestamp each run, so the "final machine receipts" change on every reproduction.
   - `00-index.md` links to `../AdS2-RST-review-package.zip`. The link checker resolves relative to the note, so `relative_markdown_links` passes only when the zip sits next to the extracted folder and would fail elsewhere.
   - `run_verification.sh` defaults to `/home/bessa/.venvs/physics/bin/python`. With `set -e` it dies on any other machine unless `PHYSICS_PYTHON` is set. The final step uses bare `python3`, not the chosen interpreter.
4. **Status language.** "Every actionable finding closed" and "closed review" invite the reading that the work is validated. The reviewers are AI agents whose reports the package author adjudicated, so the loop is circular. The honest framing is "AI-reviewed, human review pending". The package says this, but it is buried under a heavy ledger.
5. **Minor.**
   - The index mentions only the 125/129 red run, while `07-evidence-and-reproduction.md` and `validation.json` also record 128/129.
   - Dense internal identifiers (`spark_...`, "FR-xx", "20:05 updated reviewer") make the package opaque to an outside reader.

## 5. Recommended changes

1. Add a short corollary: retained state ≡ t₊-on with p_eff = 1 + p, critical P = λ² in that picture. Reword the headline from "no threshold" to "threshold absorbed by the t₊ step-off".
2. Add the σ-frame energy scaling (~1/p) next to the Kruskal-profile caveat.
3. Either attempt a theorem for all future timelike curves in the trapped region, or label the observer results as consistency controls.
4. Fix the weak or proxy checks and state per check which are derivations and which are controls.
5. Make `validate_package.py` re-run the relocation test or drop that check. Replace hardcoded evidence strings with real counts. Write only to `outputs/`, and drop or relocate the `../` zip link.
6. Condense into a 4–6 page note (setup, constraint integration, theorems, caveats), with the ledger, red history and manifest as an appendix.

## 6. Bottom line

The algebra holds, and the scoping, especially against the impulsive case, is better than most self-assessments. The gap is in how the result is interpreted: the "every flux works" claim depends on a state choice and a frame choice that the text flags but does not put in the headline. Process machinery substitutes for independent scrutiny in several places. A qualified human relativist should check the constraint normalization and the t₊ step-off justification in Kim-Son before anything stronger is claimed.