I'll start by locating and reading the requested files.
**Snapshot reviewed:** `verify.py` (sha256 `f248cf6e…`), `independent_symbolic.py` (`5d7d5c91…`), `validate_package.py` (`03677ca9…`), and the shipped 15:08 outputs. I ran copies under the scratch directory; no package files were edited.

## Checks that are correct

- **Impulsive sign:** correctly `y-alpha`, not `y+alpha` — source tex `230-231`/`304-305` has `-(A/√κ)(x⁺-x₀)Θ(x⁺-x₀)`; `02:94,98`, `05:41`, `verify.py:232-244`, and the `x=9/4`, slope `-2/11` example are consistent.
- **Sustained root/order:** `03:29` and `03:65` are correct; `verify.py:89,94` pass.
- **Observer `R_w` root:** `03:113,117` and `verify.py:327-331` are correct; the printed `σ₀` values (`1.411804…`, `0.721817…`, `0.486954…`) match `R_w`.
- **Finite-pulse after-shutoff root:** `06:57` and the first conjunct of `verify.py:285` are correct.
- **`E=p*s` algebra in the notes:** `06:27,37` is correct and the `C⁰/C¹` and both-positive checks pass.
- **Null-affine quadrature:** `verify.py:352` correctly integrates `e^{2ρ}` and satisfies the `03:82` bound.

## Findings

1. **Critical — the shipped producers are red, but the battery’s new check is broken by a missing `E=p*s` substitution.** `verify.py:284-287` adds
   `(x_after-s) - F_during(s)/(E-y) == 0`, but applies `.subs(E,p*s)` only to `F_during`, not to `x_after`. The actual residual is `-s(ps-E)/(2(y-E))`, so it is nonzero for generic `E,p`. Result: `outputs/verify.out:113` FAIL, `:142` **128/129**; `independent_symbolic.py:76` has the same defect, `outputs/independent_symbolic.out:20` FAIL, `:31` **29/30**. The root formula itself is fine; this is a test-implementation bug. Even fixed, the name’s “`x_after>s`” is not established: the check proves the identity but not the implication `F_during(s)>0` for `y>y_max`.

2. **Critical — every package-level green receipt is stale and contradicts the red run.** `00-index.md:22-23`, `07-evidence-and-reproduction.md:31-32,52,80,86`, `10-formal-signoff.md:24-25`, `README.md:14`, and `09-independent-reviews.md:46` claim 129/129 and 30/30. The shipped summaries say otherwise (`outputs/verification-summary.json:7-8`: 128 passed, 1 failed; `outputs/independent-symbolic-summary.json`: 29/30). `validation.json:18-25` still records both counts as PASS, `:59` records overall PASS, and `manifest.json` has **8 stale artifact hashes** (`verify.py`, `independent_symbolic.py`, `05`, `09`, and four `outputs/` files). The portability receipt (`outputs/portability-receipt.json:9`) claims `1c8e26f4…`, but the current `outputs/verify.out` is `6d62ab51…`.

3. **High — the interior-observer proper-time evidence uses `e^{2ρ}` where the theorem specifies `e^{ρ}`.** `03:99,121` define `dτ = λ√K e^ρ dσ₀`; `verify.py:372-373` integrates `√K * numeric_e2rho(...)`, and `numeric_e2rho` returns `e^{2ρ} = -4/(κW)`. The table at `03:130-132` therefore reports `∫√K e^{2ρ}`, not proper time: the stated values `0.688707… / 0.804380… / 0.572304…` should be `0.900853… / 1.336004… / 1.599113…`. `verify.py:374` only checks finite/positive, so it cannot detect this. The analytic finiteness proof remains valid; the executed control and table do not.

4. **Medium — several assertions are tautologies or too weak to detect the claimed failure.** `verify.py:304-306` (“horizon continues as `y=E`”) reduces to `E=p*s` and would pass for any after-region claim; `verify.py:310-312` only differentiates `log(Ce^{-2ρ})` and never checks the geodesic ODE; `:108` is a derivative identity; `:211-213` only verifies `-p(y/p)+y=0`; `:236-240` proves only the `a=y+h` sufficiency of “exactly `0<y<α`”; `:267-269` proves root+positivity, not uniqueness, for `p>1`; `:289-293` never computes the post-shutoff tangent; `:401-403` logs the branch but asserts only existence/positivity, so a wrong branch or wrong finite value would pass. `independent_symbolic.py:77,84` repeat the weak horizon/causal checks.

5. **Medium — the “complete” finite-pulse criterion is not symbolically verified.** `verify.py:294-297` checks only the `μ=0` limit of `y_max`; the `y_max<E` claim appears only in the detail string; there is no check of `x_{p,d}<s ⇔ y<y_max`, of `F_during(s)>0` for `y>y_max`, or of the exact first-hit values. `06:53-59` and `01:56` present this as the complete proof, but the only support is the 12-row existence census. Combined with finding 1, the after-shutoff branch currently has no passing symbolic check.

6. **Medium — `y_max` is undefined in a reachable regime.** `06:53` defines `y_max=√((1+p)s²-2μ)-s`, but `06:55,59` and `01:56` use `y≥y_max` without requiring `(1+p)s²≥2μ`. For `p=1, μ=100, s=2`, `y_max` is imaginary while an after-shutoff wall still exists (`x_a=102.5` for `y=1`) and `0<y<E` still holds. The theorem needs a case split (`y_max` real/negative/imaginary); `verify.py:294-297` cannot catch it because it only tests `μ=0`.

7. **Low — `04:50` displays an incorrect value.** For `Q(R)=KR²+2(K+μ)R-Kp`, `Q(p)=p(Kp+K+2μ)`, not `2p(K+μ)`; the difference is `Kp(p-1)`. The conclusion `R_w<p` survives because `Q(p)>0`, but the displayed equality is wrong, and no test checks `Q(p)`.

8. **Low — `03:134` is false as written.** “All three wall residuals are below `1.5e-90`” contradicts the shipped first residual `-9.327e-90` (the others are `-1.227e-90` and `+1.473e-90`), and the code threshold is `1e-60` at `verify.py:374`.

9. **Low — portability claims conflict with the commands.** `verify.py:5`, `07:46-47`, `00:60-61`, and `README.md:10-11` hardcode `/home/bessa/.venvs/physics/bin/python`; `outputs/portability-receipt.json:3` records an absolute scratch path. The scripts’ input paths are `ROOT`-relative (good), but the advertised “portable commands” are machine-specific, contrary to `08:28` and `10:R15`.

10. **Low — `validate_package.py`’s gate is self-certifying.** `:15` defines `EXPECTED_SCIENCE` but never uses it; `:109-112` hardcodes expected counts read from the producers’ own JSON rather than re-running them; `:114-115` checks only that two red-first files exist and labels “125/129 red-first artifacts”; `:116-118` trusts the receipt’s `status`/boolean and never compares its `sha256` to the shipped output; `:119` compares `len(artifacts)` to `manifest["file_count"]` that it just set, so it is tautological. A current run exits 1, but the shipped `validation.json` still says PASS.

11. **Low — the corrected impulsive sign is not pinned by the battery.** The sign is right, but the source-line checks (`verify.py:43-50`) never assert the `−A/√κ` term at tex `230-231`/`304-305`; `verify.py:236-240` only tests the hand-entered `F_imp`. A regression to `y+α` would not be caught. Add a lexical anchor for the negative impulse term and assert its sign.

12. **Low — after-shutoff horizon wording overstates the geometry.** `06:83`/`04:60` say every wall ray “crosses the horizon before its singular hit”; for `y<E` the crossing is at `x_p=y/p<s` during the pulse, while the post-shutoff horizon is the boundary ray `y=E`, which a fixed-`y<E` ray never crosses. The statement is true only if “horizon crossing” is explicitly assigned to the during-pulse branch; the only test is the tautology in finding 4.

FIX-FIRST
OPENCODE_REVIEW_EXIT=0
