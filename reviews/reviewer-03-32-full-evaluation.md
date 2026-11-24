# Evaluation report: Kim-Son AdS2-RST one-sided-flux review package

This covers both archive versions (`Archive.zip` and the updated `Archive_1.zip`). It is written so you can present it as-is.

## 1. One-paragraph summary

The package proves, for a fixed Kim-Son quantum state, that a classical one-sided flux constant in Kruskal `x_p` produces a spacelike RST singular edge behind an apparent horizon on every mixed outgoing ray. It also gives the exact finite-pulse band `0<y<E` and a general cumulative-flux criterion (`y<E_tot`). The mathematics is correct and reproducible, and the package is very disciplined about what it does not claim. My assessment is that it is **sound but modest in significance**: a clean, correct extension of Kim-Son's impulsive result, and not a standalone physical discovery. The main weaknesses are in framing and evidence presentation, not in the algebra.

## 2. What I did, and the limits of it

| Activity | Result |
|---|---|
| Read all main documents, the adjudication ledger, and the key Kim-Son source equations | Done |
| Re-derived by hand: four-sector Ω, root `(y+D)/p`, spacelike slope, horizon `y/p`, finite-pulse `x_after` and `y_max`, observer wall quadratic, cumulative-theorem proof | All correct |
| Reran `verify.py` and `independent_symbolic.py` (Python 3.12.3; the receipt says 3.14.9) | 133/133 and 34/34 reproduced |
| Manifest hashes, both archive versions | 64/64 match |
| My own check from the constraint equation, using different code | Agrees (details in section 4) |
| Lean source and build receipt inspected | Not rebuilt (no toolchain) |
| PDF and manuscript | Existence and key formulas checked, not recompiled |
| Literature | Not re-fetched, except the one new citation, which I confirmed exists |

This evaluation is itself AI-produced, so it should not be counted as human scientific review.

## 3. What is solid

1. **The derivation matches the source.** The constraint normalization (`a±'' = √κ t± − T/√κ`) and the `t±=(λ²/κ)θ(x₀−x±)` data agree with Kim-Son's own equations, and the matching constants are consistent.
2. **The core results check out.**
   - The first hit is `x_hit=(y+D)/p` with `D=√((1+p)y²+2pμ)`.
   - The edge is spacelike (`dx_m/dx_p=−D/(x+y)<0`).
   - The apparent horizon is `x_AH=y/p`, strictly before the hit.
   - The finite-pulse band is `0<y<E` with `E=p·x_s`, and the post-shutoff hit formula is correct.
3. **The FR-09 rejection is right.** At Ω_s on the physical branch, `e^{2ρ}=4/κ` is finite.
4. **The claim fence is excellent.** It explicitly excludes future-asymptotic observers, absorbers, arbitrary states and priority claims. It also corrects its own overreaches, such as the "all walls vanish for p≤1" claim. Red-run failures are preserved rather than deleted.

## 4. My independent numerical check

I built Ω by direct numerical integration of the constraint, with random λ and κ, and compared against the package's formulas:

- Closed-form hit versus root-finding on 8 random parameter sets: maximum relative error about 4e-16.
- Horizon: at p=0.4, y=1.1, μ=0.7 the numerical horizon is at 2.75, matching `y/p`, before the hit at about 6.50.
- Finite pulse: hit found for y/E = 0.25, 0.75 and 0.99, and none for 1.01 and 1.5.
- Cumulative theorem with an exponential profile (`E_tot=p·w`): a hit at y=0.95·E_tot (x≈63) and none at 1.05·E_tot or 2·E_tot.

## 5. Concerns, in order of importance

**5.1 The headline result is thin.** On a mixed ray the excess is `μ + y²/2 + xy − p x²/2`. A concave quadratic with a negative leading term must eventually cross zero, so "every ray, every p>0" follows in a few lines. The cumulative-flux note shows the real structure: a wall exists iff `y<E_tot`, and the sustained case is simply `E_tot=∞`. Kim-Son's impulse already gives `0<y<α`. I'd make the cumulative theorem the headline and treat the sustained theorem as an example.

**5.2 "No critical amplitude" is largely a profile artifact.** With `x_p=e^{λσ}`, constant Kruskal flux means `T_σσ ∝ e^{2λσ}`, an exponentially growing flux on from σ=−∞. The hit sits at `x_p≈2y/p`, so as p weakens the delay in σ grows only logarithmically (about `ln(2y/p)/λ`). The package notes the frame dependence, but its wording still reads as a physical statement in places. Also, "no critical amplitude" holds for any positive source, including the impulse. What the amplitude controls is the width of the wall band.

**5.3 Note 11 may under-claim.** It says an observer-adapted finite-duration source is not solved by the theorem. The theorem is stated for any nonnegative measure on `x_p≥0` with the state fixed, and classical `T_σσ` transforms tensorially. Under that reading, a source `T_σσ` on `[σ₁,σ₂]` gives `E_tot=(1/λ³)∫T_σσ e^{−λσ}dσ`, with a wall band `y<E_tot`. This is my own derivation and I have not tested it numerically, so it should be checked. If it holds, the most physical case is already covered, and earlier flux counts exponentially more in the σ-frame.

**5.4 The Lean file is thinner than "machine-checked" suggests.**
- Everything is algebra over hand-entered definitions. Ω, the constraints and the source integration never enter Lean.
- `F_y_at_xHit` is `x+y = x+y := rfl`, a tautology, though the README lists it among the derivative factors.
- `general_wall_slope_neg` is a `linarith` on an assumed `y<Q`.
- Derivatives are never connected to Mathlib's `deriv`.
- The axiom report is clean (`propext`, `Classical.choice`, `Quot.sound`), so it is honest. I'd describe it as "algebra sanity-checked in Lean", not as a formalized theorem.

**5.5 The evidence is more circular than the headline counts imply.**
- Both producers are the same author's sympy checking entered candidate formulas, as note 07 admits. The 133 checks are not 133 independent facts.
- The "independent" reviews and the adjudication ledger were produced by the same AI pipeline, so shared blind spots are possible.
- The real evidence is the one-page derivation. A human re-derivation of the four-sector Ω and the impulsive comparison is the actual open gate (R17).

**5.6 Packaging nits.**
- The inner `Archive.zip.sha256` does not match the containing zip in either version (`6c3f…` vs `7c6c…`; `e0fa…` vs `919e…`). This is expected for a self-referential hash. The per-file manifest is the meaningful check.
- The index says the archive "includes" `Archive.zip`, which it does not.
- Running the producers in place overwrites `outputs/` and breaks the manifest until the validator reruns.
- Internal tokens (`spark_…`, a `razul` schema string) leak into an external-review object.
- The arXiv TeX and figure are redistributed, so check the license before wider sharing.

## 6. What the update changed

Between `Archive.zip` and `Archive_1.zip`, only the literature position changed. Eight files differ, and the substantive ones are note 05, `reviews/additional-state-dependence.md` and the manuscript. All code, theorem notes and scientific outputs are byte-identical, so my reproduction carries over.

- **The addition:** Potaux–Sarkar–Solodukhin, *Islands for black holes in a hybrid quantum state* (2025), alongside their 2023 hybrid-states paper.
- **Verified:** arXiv:2411.09574 exists (submitted 14 Nov 2024), and the package's description (a regular causal-diamond geometry with radiation entropy and islands) is accurate.
- **Not confirmed:** the journal reference (PRD 111, 026019, 24 Jan 2025). The arXiv listing I retrieved shows only v1 with no journal reference, so check the publisher page.
- **Why it matters:** the hybrid-state papers work in a regime with negative effective central charge (κ<0), where the geometry is regular, with no horizon or singularity. That is direct evidence the singular edge depends on state choice, and the package could use it to motivate a state-dependence section instead of just listing it.
- **Rebuild:** the PDF recompiles with the new reference, with only cosmetic overfull-box warnings. The manifest is 64/64 and the validation receipt is 11/11.

## 7. Scorecard

| Dimension | Assessment |
|---|---|
| Mathematical correctness | Strong (hand-checked and independently verified numerically) |
| Reproducibility | Strong (reproduced on a different Python version) |
| Scope honesty | Excellent |
| Novelty and significance | Modest |
| Physical interpretation | Weak to moderate (Kruskal-profile dependence) |
| Formal verification | Limited in content (Lean covers only trivial algebra) |
| Independence of review | Low (AI reviewing AI; no human review) |
| Packaging | Good, with minor issues |

## 8. What would take it further

These are in the order I would pursue them.

1. **Make the threshold physical.** Map `E_tot` to a σ-frame energy budget (section 5.3), and identify which rays correspond to boundary-to-boundary communication. This is the cheapest high-value test and may give a clean quantitative statement.
2. **Remove the fixed-state dependence.** A classification across natural states (Boulware-like, Hartle-Hawking-like, hybrid) would be new. The hybrid-state papers are the nearest neighbor.
3. **Say what the edge means.** At Ω_s, `e^{-2φ}=κ/4`, which is order one, where the semiclassical description is least reliable. Either argue the edge is a truncation artifact or give a defensible continuation.
4. **Replace the prescribed source** with an explicit large-N matter field whose `T_{++}` reproduces the profile.
5. **Close the rigor gap.** That means a human re-derivation and Lean statements that start from Ω and use real derivatives. This adds credibility, not novelty.

Realistically, the good outcome is a solid, carefully scoped paper with one result that people cite. I can't judge priority or reception, since my literature coverage is limited, so a short conversation with someone who works on RST/JT wormholes would be worth more than another verification pass.

## 9. Suggested framing when presenting

"The result is correct, reproducible and honestly scoped. It is best read as the observation that infinite total Kruskal flux terminates every ray, inside a general cumulative-flux criterion. Its physical meaning depends on the σ-frame interpretation of the source, which is the main open question. Human re-derivation and a specialist's opinion on novelty are the remaining gates."

## 10. Questions worth putting to a human reviewer

- Does the cumulative theorem cover observer-adapted finite-duration sources, as I suspect?
- Is the Kruskal-constant profile a natural physical source in this model, or only a convenient one?
- How much of the result survives for state data other than the retained `t±`?
- Is the apparent-horizon-before-singularity ordering known in the RST literature for this branch?

I can also put this into an editable doc you can share or export as Word or PDF, if that would be useful.