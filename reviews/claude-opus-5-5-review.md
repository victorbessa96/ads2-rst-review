---
created: 2026-11-23
type: formal-review-response
reviewer: Claude (Opus 5.5), AI reviewer, not an external human review
package: frontier/assets/2026-11-22-ads2-rst-one-sided-flux/formal-review
spark: spark_20261110_154351_a10e80
status: findings-open
---

# Review: AdS2-RST one-sided flux formal-review package

> [!important] Reviewer status
> This is an AI review of the 15 files in the handed-over folder. It is **not** the external human formal review the package requires, and it must not be recorded as one. The producer script, staged TeX, canonical note, and internal reviews were not in the folder, so the source-dependent checks below are marked as not performed.

## 1. Summary verdict

| Item | Verdict |
|---|---|
| T1 (algebra, root, causal sign within the fixed solution) | **ACCEPT**, with wording changes (FR-01, FR-03, FR-09) |
| C1 (taxonomy consequence) | **ACCEPT WITH WORDING CHANGES, significance disputed** (FR-01, FR-02) |
| Reproduction | **BLOCKED for an external reviewer** (FR-07). Local artifact hashes: PASS |

In one sentence: the mathematics is correct and the scope fencing is unusually honest. But the "any P > 0, no threshold" character of the result rests on two untested modelling choices: t_+ switching off at the flux onset, and flux that is constant in the Kruskal coordinate. In addition, the taxonomy point seems to follow already from Kim-Son's own impulsive-shock solution.

## 2. What was examined

| Check | Result |
|---|---|
| Read all 15 files: `00-index.md`, `README.md`, `theorem-and-proof.md`, `evidence-and-reproduction.md`, `review-checklist.md`, `second-pass-verification.md`, `manifest.json`, `validation.json`, `formal-review-reproduction.{out,json}`, `formal-review-claim-gate.out`, `package-claim-gate.out`, `package-link-check.out`, `independent-symbolic.out`, `second-pass-verification.out` | Done |
| SHA-256 of every local file against `manifest.json` | All 14 manifest-listed local files match |
| `manifest.json` hash against `validation.json:manifest_sha256` (`0eb968a2…1a44`) | Match |
| `formal-review-reproduction.out` hash = canonical `ads2_rst_flux_out.txt` hash in manifest | Match (`6b179d2d…f7`) |
| Hand re-derivation of §5–§9 of `theorem-and-proof.md` | Done; see §3 |
| Independent derivation of the four-sector solution from the Kim-Son constraints | **Not performed**: the TeX source was not available |
| Running the canonical battery | **Not performed**: producer not in folder; absolute paths (FR-07) |
| Reading the cited Kim-Son equations | **Not performed**: source not in folder |

## 3. Mathematical verification (T1)

All of the following were re-derived by hand and agree with the package.

1. **Sector second derivatives.** Given a_±'' = √κ t_± − T_±±/√κ with t_± = (λ²/κ)Θ(−x^±), the four Ω expressions in the §3 table have the stated ∂_p², ∂_m², and ∂_p∂_m = −L. They are C⁰/C¹ across all four axes.
2. **Ω_s.** With Ω = e^{−2φ}/√κ + √κ φ/2, the minimum at e^{−2φ} = κ/4 gives Ω_s = (√κ/4)(1 − log(κ/4)). Correct.
3. **Normalized wall equation.** F = μ + y²/2 + x y − p x²/2. The roots of p x² − 2y x − (2μ + y²) = 0 are (y ± D)/p with D = √((1+p)y² + 2pμ). Correct.
4. **Root selection.** D² − y² = p(y² + 2μ) > 0, so D > y and the minus root is negative. F(0) > 0 and F → −∞, so F > 0 before x_hit and F < 0 after it. Correct.
5. **Tangent.** F_x = y − p x_hit = −D, F_y = x_hit + y, so dx_m/dx_p = −D/(x_hit + y) < 0. Correct.
6. **M = 0 branch.** y/x_hit = p/(1 + √(1+p)) = √(1+p) − 1. Correct.
7. **Both-positive branch.** x_m = μ/x − p x/2 vanishes at √(2μ/p), where its slope is −p. The mixed-branch slope as y → 0⁺ is −√(2pμ)/√(2μ/p) = −p. Position and slope match. Correct.
8. **Fourth sector.** μ + uv + u²/2 > 0. Correct.
9. **Asymptotics.** p → 0⁺ gives x_hit ≈ 2y/p + y(μ/y² + 1/2) + O(p). y → ∞ gives y(1 + √(1+p))/p. Correct.

No algebraic, root-selection, or sign error was found.

## 4. Findings

| ID | Severity | Claim affected | Failed step or evidence gap | Required correction | Status |
|---|---|---|---|---|---|
| FR-01 | **High** | C1; the "every P > 0" reading of T1 | The no-threshold result depends on t_+ = 0 for x_p > 0. If t_+ stays on after onset, F = μ + y²/2 + xy + (1−p)x²/2, which is > 0 for all p ≤ 1. There is then no wall unless p > 1 (P > λ²). | Show from the Kim-Son source that t_+'s step is fixed state data, independent of the flux. Otherwise state the result as conditional on that choice and give the threshold variant. Answer adversarial Q1 explicitly. | Open |
| FR-02 | **High** | C1 significance and novelty | `formal-review-reproduction.out` check 8 says "Primary source post-shock singularity is cloaked by horizon". Kim-Son's own one-sided positive impulsive shock therefore already produces an RST singularity in this past-AdS2 model. That alone appears to refute the "AdS2 never piles up" slogan, so the constant-P extension adds little to C1. | Say whether C1 already follows from Kim-Son. If it does, recast T1 as "the sustained-flux analogue of Kim-Son's shock-induced singularity" and reduce the novelty claim. | Open |
| FR-03 | **Medium–High** | Physical meaning of "constant flux" | T^f_{++} = P is constant in the Kruskal coordinate x_p. In an asymptotic time coordinate where x_p grows exponentially, the same flux grows exponentially. That would explain why the familiar RST critical-flux threshold never appears. | Identify the asymptotic observer coordinate for the post-onset region and express P in it. Avoid "sustained constant flux" without the qualifier "in Kruskal x_p". | Open |
| FR-04 | **Medium** | Observer and "pileup" interpretation | The apparent horizon is never computed. In the mixed region ∂_pΩ ∝ y − p x_p vanishes at x_p = y/p, which is before x_hit = (y + D)/p on every ray. If ∂_+Ω = 0 is the trapping condition in these conventions, the edge always lies behind an apparent horizon, i.e. this is ordinary RST black-hole formation. | Compute the apparent-horizon curve in all sectors and add it to the theorem's corollaries. Bear on adversarial Q11 ("pileup" wording). | Open |
| FR-05 | **Medium** | Open hunt `spark_20261122_093132_5b8d4d` (finite pulse) | Ω(x_p, x_m) depends on the flux only for x_p' ≤ x_p. A pulse that switches off at x_s therefore gives the identical wall on every ray with x_hit(y) < x_s. Since x_hit(y → 0⁺) = √(2μ/p), any pulse with x_s > √(2μ/p) produces a wall. | Recast the finite-pulse hunt: the existence part follows from domain of dependence. The open questions are the y > y_max(x_s) rays and the wall's endpoint and causal character after shutoff. | Open |
| FR-06 | **Medium** | R2 (exact solution) | Every check takes the four Ω expressions as input. No artifact derives them from the constraints with the integration constants fixed from the source. This is the step where FR-01 and FR-03 live. This review could not do it either, because the TeX was not available. | Complete the §5 derivation worksheet in `review-checklist.md` from the TeX. | Open |
| FR-07 | **Medium** | R6 (reproduction) | The folder holds 15 of the 32 manifest artifacts. The producer, TeX, tar, canonical note, internal reviews, and `verification-summary.json` are missing. Every command hard-codes `/home/bessa/...`. An external reviewer cannot reproduce anything from this package. | Ship a self-contained bundle (all `core` and `source-bundle` artifacts) with commands that use relative paths. | Open |
| FR-08 | Low | Provenance of `independent-symbolic.out` | `validation.json` cites "INDEPENDENT_SYMBOLIC: 7/7 PASS", but no package document contains the script that prints that string. `theorem-and-proof.md` §12 prints "EXACT PASS…" and has 6 asserts. | Include the generating script or point to it. | Open |
| FR-09 | Low | `theorem-and-proof.md` §2, §5.4 | The causal rules are stated "for a regular conformal factor", but e^{2ρ} is singular on Ω = Ω_s itself. Classifying the edge by its coordinate tangent is standard, but that should be said. | Add one sentence: the causal character is the limit of the classification along nearby regular curves, read from the coordinate tangent. | Open |
| FR-10 | Low | Producer labels | Two check labels claim more than they test: "Both-positive wall is spacelike" and "Vanishing flux retreats … to infinite advanced coordinate". The package already admits this. | Rename the labels in the producer rather than only noting the overstatement in prose. | Open |
| FR-11 | Low | Evidence presentation | The load-bearing mathematics is one quadratic plus sign arguments. It is wrapped in 88 checks (45 grid samples of a closed form), claim gates, and wikilink counts. That volume can read as more evidence than exists, and the "independent" reviews are AI sessions from the same pipeline. | Lead with the one-page proof and the list of unverified assumptions. Move gate and link metrics to an appendix. | Open |

## 5. Adversarial questions (from `review-checklist.md` §4)

| # | Answer from this review |
|---|---|
| 1 | **Yes, plausibly, and it is load-bearing.** See FR-01. |
| 2 | Not determined without the source (FR-06). Within the stated matching, the linear terms are fixed. |
| 3 | No. Θ values on the axes do not enter the C¹ solution. |
| 4 | Ω_s matches the standard RST minimum. The weak-branch restriction to Ω > Ω_s was not checked against the source. |
| 5 | Yes, with the FR-09 caveat about the conformal factor on the edge. |
| 6 | The package already discloses that M = 0 is singular before onset. Handled. |
| 7 | The wording is fine as fenced (x_p > 0, x_m = −y < 0, finite y). The word "outgoing" for constant-x_m rays deserves a convention note. |
| 8 | The package does not make that conversion. Handled. |
| 9 | No, and the package says so. "Past-asymptotically AdS2" is the right phrase. |
| 10 | Open. Related to FR-03: in asymptotic time the source may grow exponentially. |
| 11 | **Yes.** Use "singular termination", and note FR-04 (behind an apparent horizon). |
| 12 | No literature-wide claim is made, but see FR-02: the lineage-level novelty is also thin. |

## 6. Recommended next steps (priority order)

1. **Threshold analysis (FR-01, FR-03).** Redo the mixed sector with t_+ retained after onset, and with the flux expressed in the asymptotic time coordinate. Determine whether a critical flux reappears.
2. **Source derivation (FR-06).** Fill in the worksheet from the TeX, especially how Kim-Son tie t_± to the shock location x_0.
3. **Kim-Son comparison (FR-02).** State explicitly what the constant-P case adds beyond the impulsive-shock singularity.
4. **Apparent horizon (FR-04).** Add the horizon curve, then revisit the "pileup" wording.
5. **Finite-pulse hunt (FR-05).** Rescope it around domain of dependence before spending effort on it.
6. **Portable bundle (FR-07, FR-08).** Make it before sending to any external reviewer.

## 7. Verdict template (from `review-checklist.md` §7)

```text
Reviewer identity and affiliation: Claude (Opus 5.5), AI assistant; not an external human reviewer
Review date: 2026-11-23
Reviewer role(s): Root and branch; Geometry (partial); Model-scope; Adversarial; Reproduction (hash-level only)

Artifacts and hashes verified: YES (15 local files only; 17 manifest artifacts absent)
Independent derivation attached: PARTIAL (root/causal/branch lemmas yes; four-sector derivation from source NO)
Canonical battery reproduced: NO (producer absent)
Source-tar identity reproduced: NO (tar absent)

T1 verdict: ACCEPT WITH WORDING CHANGES
C1 verdict: ACCEPT WITH WORDING CHANGES; significance disputed (FR-01, FR-02)
Reproduction verdict: FAIL for external reproducibility (FR-07); PASS for local hash integrity

Binding final statement:
  Within the fixed Kim-Son solution, with t_+ vanishing for x_p > 0 and T_{++} = P
  constant in Kruskal x_p, each mixed-region ray x_m = -y reaches Omega = Omega_s at
  x_p = (y+D)/p along a spacelike edge. Whether a flux threshold reappears under other
  state or frame choices is open.

Failed or narrowed claims:
  "Any P > 0" narrowed to the t_+ / Kruskal-frame choices (FR-01, FR-03).
  C1 novelty narrowed (FR-02).

Findings by ID: FR-01 … FR-11 (section 4)

Residual disagreements: none recorded; awaiting author response

Required follow-up before citation or publication: FR-01, FR-02, FR-03, FR-06, FR-07

Reviewer signature: n/a (AI review)
```