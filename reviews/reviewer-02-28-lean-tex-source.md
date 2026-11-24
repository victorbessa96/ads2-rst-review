I'll read the Lean and TeX sources directly, since only their metadata and the PDF render reached me.

# Evaluation of the Lean proof and LaTeX manuscript

**Scope.** I read `AdS2RST.lean` and the `.tex` line by line, plus the PDF, `lakefile.toml`, `lake-manifest.json`, `lean-toolchain` and the Lean README. I could not rebuild the Lean project because the sandbox has no Lean, Lake or Mathlib, so I rely on your build receipt. I did not read `verify_1.py` or the new `reviews/` files. I checked the Potaux–Sarkar–Solodukhin citation against arXiv: title, authors, arXiv:2310.18745 and Phys. Rev. D 108, 125012 all match. It is a paper on hybrid quantum states in the RST model, so "relevant state-dependence literature, not the same calculation" is a fair description.

## 1. Verdict

- **Lean:** correct to the extent I can read it, and honestly scoped in its own docstring. It is narrower than the surrounding prose suggests, and two README claims are stronger than what the file contains.
- **Manuscript:** the mathematics matches the verified derivations and the cumulative-theorem slope error does not appear in it. As a standalone paper it is an incomplete statement sheet with undefined symbols.

## 2. Lean file

**What it proves (by reading).**
- **Root and uniqueness.** `F_xHit` and `F_eq_zero_iff` prove the sustained root is a zero, and that any positive zero equals it. The proof goes through `(px−y)² = D²`, factors the difference, and excludes the minus root via `other_root_neg`. The algebra is right: multiplying `F=0` by `p` gives `(px−y)² = (1+p)y²+2pμ`.
- **Other lemmas.** `D_gt_y`, `xHit_pos`, `other_root_neg` and the after-shutoff lemmas (`zAfter_eq`, `zAfter_pos_iff`, `zAfter_neg_of_gt`, `zAfter_zero`, `x0_sub_s`, `after_interval_nonempty_iff`) are all sound as written.
- **Library calls.** The Mathlib lemma names I could check from memory (`Real.lt_sqrt`, `one_lt_div`, `div_lt_one`, `mul_pos_iff_of_pos_left`) have the signatures used. I cannot confirm that the proofs compile.
- **Dependencies.** `Mathlib` is pinned by `rev` and by the manifest hash, which is good for reproducibility. There is no `sorry`, `admit` or custom `axiom` anywhere in the file (grep-verified).

**Problems.**
1. **`slope_neg` proves less than its docstring says.**
   - It proves that the expression `−D/(xHit+y)` is negative. It does not derive that expression as `dx_m/dx_p`.
   - The derivation needs `F_x(xHit) = y − p·xHit = −D` and `F_y = xHit + y`. Neither is a lemma.
   - Both are one-line additions. The physical step, implicit differentiation, still stays outside Lean.
2. **The ordering `F>0` before the hit and `F<0` after it is not formalized.**
   - The identity `F(x) = −(p/2)(x−x₊)(x−x₋)` would give uniqueness and the sign ordering in one lemma.
   - The docs cite this ordering as the physical-side exclusion, so it is the more valuable lemma.
3. **The three `example` blocks are not theorems.**
   - The README lists the `p_eff = 1+p` coefficient identity and the stress scaling among things the file proves. In the file they are anonymous `example`s.
   - `(1−(1+p))/2 = −p/2` is a bare `ring` fact. It never mentions `F`, and nothing connects `F_alt(p→1+p)` to `F`.
   - The stress example states `λP(2y/p)²/2 = 2λPy²/p²`. That gives `2λ³y²/p` only after substituting `P = λ²p`, which the Lean does not do.
   - The `#print axioms` lines cover only four lemmas.
4. **Coverage is narrower than the prose.** Not in Lean:
   - the finite-pulse existence criterion `0<y<E`, `y_max` and `x_a − s = F_d(s)/(E−y)`;
   - horizon ordering `D/p > 0`;
   - the cumulative-flux theorem, including concavity and uniqueness;
   - the constraint integration.

   Only the quadratic and the after-shutoff sign algebra are formalized. The index row "Lean 4: Build completed successfully" and the tex line "a Lean 4 proof of the sustained root, uniqueness…" should say "algebraic core formalized".
5. **Gate weakness, still present.**
   - The validator greps the build log for the string `sorryAx`, but Lean's warning for an unfinished proof reads "declaration uses 'sorry'". An unfinished lemma outside the four `#print axioms` targets could slip through.
   - Grep for `sorry` as well, or fail the build on warnings.
   - The gate also does not check that the receipt is newer than the `.lean` file.
6. **A hardcoded path remains.** The Lean README's build command still points to `/home/bessa/.hermes/...`, as does `run_verification.sh` under `RUN_LEAN=1`. This is the same external-reproduction problem as before.

## 3. Manuscript (`.tex` and PDF)

**Content checks.**
- **Normalization.** `μ = √κM/λ³` and `p = P/λ²` follow correctly from `Ω − Ω_s` multiplied by `√κ/λ²`. I re-derived all four coefficients: `μ`, `y²/2`, `xy` and `p/2`.
- **Theorems.** The sustained root and slope, the pulse cases, the mass-classification table and the cumulative-flux statement agree with what I derived earlier.
- **Table fix.** The `μ > Es/2` row now says "All mixed hits after shutoff" instead of the earlier incorrect "`y_max` nonreal", so that item is fixed.
- **Slope formula.** The cumulative section gives only "`Q(x_hit) > y`, so the wall is spacelike", with no displayed slope. The inverted-sign formula from `11-cumulative-flux-generalization.md` is not copied here. I did not see whether doc 11 itself was corrected. Re-upload it if you want me to check.
- **PDF.** The stray `√` placement I see in the PDF text extraction (around the `dx_m/dx_p` line and `√(2µ/p)`) looks like a glyph artifact of extraction, not a typesetting error.

**Defects.**
1. **Undefined symbols.** `Ω_s` appears in the definition of `B` without being defined. `W ≤ −1` appears without saying that `W` is the Lambert `W_{−1}` branch. The weak-branch bound `0 < e^{2ρ} ≤ 4/κ` is used in the affine and proper-time arguments and is stated without its derivation.
2. **"Locally integrable" versus the impulse.** The abstract and §5 state the cumulative theorem for locally integrable `T`, then list the delta (`Q = α`) as a special case. A delta is a measure, not a locally integrable function. Restate the hypothesis for nonnegative Radon measures, with `Q` nondecreasing and right-continuous.
3. **Statement sheet, not a paper.** Several results are asserted without proof in the manuscript:
   - the cumulative theorem has no proof (concavity gives uniqueness; `F_x ≥ 0` gives non-existence), which lives only in doc 11;
   - the pulse necessity argument is missing;
   - the horizon corollary is one line;
   - the constraint integration is cited to TeX line numbers, not shown.

   Unless this is meant as an appendix, add the short proofs.
4. **Authorship and tone.**
   - The author line "Review package generated from the verified derivations" is not an author. "Verified" also overclaims, given the AI-reviewed, human-pending status stated elsewhere.
   - The abstract uses "I derive" while the byline is generated text. Pick one voice and add a status line.
5. **§7 Verification** should replace "a Lean 4 proof of…" with "a Lean 4 formalization of the algebraic core (quadratic root, uniqueness, after-domain sign)".
6. **Scope in the abstract.** "Arbitrary nonnegative locally integrable incoming profiles" reads wider than the theorem, which fixes the Kim–Son state and covers only mixed-ray hits. §6 states the limits, but the abstract does not carry them.

## 4. Remaining recommendations, in priority order

1. Add the Lean lemmas `F_x(xHit) = −D`, `F_y = xHit + y` and `F x = −(p/2)(x−x₊)(x−x₋)`. Turn the three `example`s into named theorems, or drop them from the README's list of what is proved.
2. Make the validator grep for `sorry`, check receipt freshness, and replace the hardcoded `/home/bessa` paths in `run_verification.sh`, the Lean README and the validator's relocation directory.
3. Fix the manuscript's undefined `Ω_s` and `W`, the locally-integrable versus delta mismatch, the byline, and the "Lean proof" wording.
4. Add the cumulative-theorem and pulse proofs to the manuscript, or label it as a summary.
5. The substantive open item is unchanged. Someone with Kim–Son in hand must confirm the `kruskal:cons` normalization (TeX 163–178) and the `t₊` step-off justification (214–225). None of the Lean, scripts or manuscript checks that.