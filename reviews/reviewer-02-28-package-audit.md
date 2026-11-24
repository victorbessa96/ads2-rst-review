# Update evaluation: revised package (133/133, 34/34, Lean, manuscript, cumulative-flux theorem)

**Scope.** I read the revised documents 00-11, `independent_symbolic_1.py`, `validate_package_1.py`, `run_verification_1.sh`, and the manifest and validation JSON. I did not read `verify_1.py`, `lean/AdS2RST.lean`, the manuscript `.tex`/PDF, or the new `reviews/` files, and I ran nothing. This is still an AI review.

## 1. Verdict

The package is materially better. Most of my earlier points are now handled in the text, and the new theorem is sound. I found one sign error in it, one wrong table cell, and one new portability bug in the validator. Theorems: **accept with wording changes**. Reproduction: **pass with instrument caveats**, down from "caveats plus theater".

## 2. My earlier points: status

| Earlier point | Status |
|---|---|
| 3.1 The `p_eff = 1+p` equivalence | **Done.** Coefficient `(1−p_eff)/2 = −p/2` checks out, and it is in the index, claim doc and doc 05. Framing it as state-specific is the right call. |
| 3.2 Observer-frame energy scaling | **Done.** I re-derived `∫T_σσ dσ = λPx²/2`, and at `x_hit ≈ 2y/p` it gives `2λ³y²/p`. Correct. |
| 3.3 Observer results over-billed | **Done.** They are now labeled "consistency control, not an all-geodesics theorem". |
| 3.4 Constraint normalization | **Partly.** There are now explicit TeX line citations (163–178), but it is still a lexical anchor. A human still has to read the source equation. |
| Validator theater | **Mostly done.** Red-run counts are read from the summaries (129/125/4 and 129/128/1). Relocation is now run fresh. Read-only mode is separate. The `PHYSICS_PYTHON` fix in the final step is done. |
| Weak or proxy checks | **Not fixed.** See 4.4. |
| Status language | **Done.** "AI-reviewed, human review pending" is now at the top. |

The "first hit" caveat for `μ=0` is a good addition I had not asked for.

## 3. The new cumulative-flux theorem (doc 11)

I verified the following:
- **Excess and derivatives.** `F = μ + y²/2 + xy − λ⁻²∫(x−u)T du` is right. So are `F_x = y−Q` and `F_xx = −T/λ² ≤ 0`.
- **Criterion.** "Hit exists iff `y < E_tot`" holds:
  - concavity gives a unique crossing, since `{F≥0}` is an interval containing 0;
  - for `y ≥ E_tot`, `F_x ≥ 0`, so `F` never reaches zero.
- **Special cases.** The sustained, rectangular and impulsive cases are recovered. The exponential example is correct: `F_x = A·e^{−x}` at `y=A`.

**Errors and nits:**
1. **Sign and inversion error in the slope formula.** The boxed formula `dx_m/dx_p = (x_hit+y)/(Q(x_hit)−y) < 0` is positive, since `Q > y` at the first root, and it is inverted. Implicit differentiation gives
   $$\frac{dx_m}{dx_p}=-\frac{Q(x_{\rm hit})-y}{x_{\rm hit}+y}<0.$$
   For the sustained case `Q−y = D`, which reproduces doc 03. The spacelike conclusion survives, but the displayed formula is wrong. It is not caught by any check: the new independent check covers the derivative and concavity, not the slope. Check whether the manuscript copied it.
2. **Scope of the hypothesis.** "Nonnegative locally integrable" excludes the delta that the special-cases table includes. State it for nonnegative Radon measures, with `Q` nondecreasing and right-continuous.
3. **Mixed region only.** The theorem concerns mixed-ray hits. It says nothing about both-positive walls, which the package itself shows can exist separately.

## 4. Remaining problems

**4.1 Mass-classification table (doc 06).** The `μ > Es/2` row says "`y_max` nonreal". That is true only for `μ > (1+p)s²/2`. For `ps²/2 < μ < (1+p)s²/2`, `y_max` is real and negative. The surrounding prose says "nonpositive-or-nonreal", which is correct, so fix the cell. The identities `y_max > 0 ⇔ μ < Es/2` and `x₀−s = (2μ−Es)/(2E)` are right.

**4.2 New portability bug.**
- `validate_package.py` creates its relocation directory with `dir="/home/bessa/.hermes/cache/scratch"`.
- On any other machine that raises, the `except` records `portability: FAIL`, and the whole validation fails.
- `run_verification.sh` calls the validator in normal mode, so `./run_verification.sh` fails at the last step for an external reviewer. This undoes the "portable bundle" claim, and the fresh-relocation feature is what introduced it.
- Use `tempfile.gettempdir()` by default. `LAKE_BIN` and `TECTONIC_BIN` have the same hardcoded-path problem under `RUN_LEAN=1`.

**4.3 The Lean and PDF gates are receipt checks.**
- The validator greps `lean-build.out` for "Build completed successfully" and no `sorryAx`, and checks that the PDF is non-trivial in size.
- It never rebuilds either, and it cannot tell whether the receipts are newer than `AdS2RST.lean` or the `.tex`. Stale receipts pass.
- Per doc 07, Lean covers the quadratic's root, uniqueness, slope and sign domain. That is algebra on entered formulas. It does not cover the constraint integration, concavity, or the cumulative theorem.
- The index table row "Lean 4: Build completed successfully" reads as stronger than that. Label it "algebraic core formalized".

**4.4 Proxy checks persist.**
- "Alternate state p<1 coefficient is positive" now tests `1−1/(1+r) > 0` and `(1−1/(1+r))/2 = r/(2(1+r))`. That is a pure identity in `r`. It never touches `1−p`, and the substitution `p → 1+p_eff` is not mapped onto the claim.
- The new `p_eff` equivalence appears to have no direct check in the independent script. A one-line `F_alt(p→1+p) − F = 0` would fix this. I could not see whether `verify_1.py` has one.

**4.5 Smaller items.**
- Doc 09 §6 still says the receipt was "regenerated at 131/131 and 32/32". That is historical but sits next to current 133/34 numbers, so mark it as history.
- I did not verify the new Potaux–Sarkar–Solodukhin citation. Check the reference and the description in `reviews/additional-state-dependence.md`.
- `Archive.zip` is excluded from the manifest and the validator never checks it. Only a `.sha256` file is listed.
- The validator also writes `outputs/portability-receipt.json`. Note this next to the "writes only under outputs/ plus root receipts" description.

## 5. Bottom line

The sustained, pulse and cumulative results are mathematically consistent. The cumulative theorem is a clean unification and the best addition in this revision, once the slope formula is corrected. The physical-interpretation fixes I asked for are in. What remains is mostly housekeeping: one wrong formula, one wrong table cell, one hardcoded path that breaks external reproduction, and some proxy checks. The substantive open item is unchanged: someone with the source in hand must confirm the constraint normalization and the `t₊` step-off justification in Kim–Son. That is human review, not more scripts.

I can read `verify_1.py`, the Lean file or the `.tex` next if you want those checked as well.