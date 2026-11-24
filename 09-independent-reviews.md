---
created: 2026-11-23
type: independent-review-history
---

# Independent review history

## 1. Supplied AI reviews

### Claude, Opus 5.5

Claude accepted the root and causal algebra, blocked external reproduction, and issued FR-01 through FR-11. Its most valuable findings were the impulsive-source novelty challenge, the apparent-horizon corollary, the finite-pulse domain-of-dependence observation, and the missing portable bundle.

Its FR-09 conformal-factor premise was wrong: `e^{2rho}=4/kappa` at the wall. FR-01 was retained as a state-sensitivity calculation rather than a defect in the stated theorem. Every finding's disposition is in [Review adjudication](08-review-adjudication.md).

### Second AI reviewer

The second reviewer correctly emphasized the compact proof, the `M=0` distinction, future-boundary limits, and the global mixed-wall representation. It was too generous on publication potential and reproduction completeness, and it treated finite-pulse existence as more open than the during-pulse domain of dependence allows.

The complete finite-pulse theorem, horizon analysis, and portable bundle resolve the actionable parts of that review.

## 2. Fresh research passes

### Source, horizon, and observer pass

A fresh mathematical subagent independently confirmed the four-sector solution, apparent-horizon ordering, finite conformal factor, null affine bound, and explicit interior observer chart. It also confirmed that the constant-`sigma_1` curves cross the apparent horizon before the wall and therefore are not future-asymptotic exterior observers.

### Impulsive-source correction

A separate impulsive transcription initially stated that Kim-Son had no mixed-sector wall. Direct reconciliation with `wormholeRST_jhep.tex:228-235` and `:301-309` exposed a sign error in that transcription. The corrected verdict confirms a spacelike mixed wall exactly for `0<y<alpha`, with matching both-positive position and slope. This is the verdict used in [State, frame, and novelty](05-state-frame-and-novelty.md).

### Finite-pulse scope mismatch

One research subagent solved an alternate retained-`t_+` problem with `q=P-lambda^2`, not the assigned Kim-Son step-off state. That work was rejected as evidence for the assigned pulse problem. The complete pulse theorem in this package was independently re-derived and mechanically checked instead. The rejected lane is recorded here so it cannot silently contaminate the conclusion.

### Bounded literature pass

A dedicated literature subagent inspected thirteen full-text primary documents and found no exact constant-Kruskal-`P`, one-sided, every-ray first-hit formula in that corpus. The result is explicitly bounded absence of evidence, not priority. See [Bounded literature check](reviews/literature-check.md). A separate direct fetch of the two load-bearing precursor papers corroborates its sustained-input and finite-pulse claims; see [primary-source spot check](reviews/primary-source-spot-check.md).

## 3. Independent executable review

`independent_symbolic.py` does not import or execute `verify.py`. It independently checks thirty-nine polynomial, causal, horizon, pulse, signed-focusing, and observer identities and returns:

```text
INDEPENDENT_SYMBOLIC: 39/39 PASS
```

The generating script, raw output, and structured summary are all included. This repairs the missing-generator problem in the older handoff.

## 4. Review-driven repairs verified in this package

The fresh adversarial passes found real defects in the first closed draft. They are repaired, not merely recorded:

1. **Observer-horizon polynomial:** `Q(p)` is now `p[K(p+1)+2mu]`, preserving the horizon-before-wall proof with the correct algebra.
2. **Shutoff boundary and large `mu`:** the post-shutoff strict case is `y>y_max`, with `y=y_max` handled separately as `x_a=s`. Non-real `y_max` radicands now have an explicit large-`mu` after-hit example, and both regressions are in the producers.
3. **Observer quadrature:** the proper-time integrand now uses `e^rho=sqrt(e^{2rho})`, not `e^{2rho}`. The three printed proper-time rows were recomputed and replaced.
4. **Finite-pulse no-wall controls:** the census now checks selected-hit residuals and explicit no-root sign conditions rather than only comparing a branch label to `y<E`.
5. **Post-shutoff identity:** `x_after-s=F_during(s)/(E-y)` is tested with the whole quotient substituted, making the strict inequality and equality case explicit.

The current results are **138/138 main checks**, **39/39 independent symbolic checks**, and **22/22 advanced consistency checks** (32 before ten rows that could not fail were removed on 2026-11-24), and **45/45 structure checks**. Older green and red outputs remain as history, never as substitutes for the final run.

## 5. OpenCode code-and-test review

A separate OpenCode/deepseek code review returned `FIX-FIRST` on an intermediate snapshot and independently confirmed several of the defects above. Its verbatim report is preserved in [opencode-code-review.md](reviews/opencode-code-review.md). The final package also addresses its additional demands:

- full-quotient substitution and exact post-shutoff inequality;
- correct `e^rho` proper-time integrand and corrected numerical rows;
- large-`mu` non-real-`y_max` case and shutoff equality regression;
- stronger no-wall residual checks and explicit negative-tangent checks;
- a lexical source anchor for the negative impulsive chiral term;
- corrected `Q(p)` and corrected residual-threshold wording;
- a configurable `PHYSICS_PYTHON` plus `requirements.txt` and `run_verification.sh`;
- fresh producer execution and receipt-hash comparison inside `validate_package.py`, with manifest readback checked against the live tree.

## 6. Final independent-review findings closed

The final literature reviewer confirmed the impulsive wall band and bounded novelty position, but caught a transcription error in Hayward–Kim–Lee Eq. (44): the pulse term is `-Delta^2/2`, not `-Delta^2`. The source-citation file is corrected accordingly. This does not alter the qualitative precursor conclusion or the Kim-Son calculation.

The mathematical reviewer independently reproduced the corrected `Q(p)` and shutoff/equality formulas, confirmed the exact finite-pulse cutoff, and independently recomputed all three corrected proper-time values. The adversarial reviewer independently reproduced the quadrature values and isolated a stale portability receipt. **Historical count:** the receipt was first regenerated at 131/131 and 32/32; the package at that time was 133/133 and 34/34 (later counts are in [00-index.md](00-index.md)), with `validate_package.py` now performing a fresh relocation and checking the current output hash.

The adversarial reviewer also caught the both-positive branch domain: the during formula is restricted to `0<x_p<min(s,sqrt(2mu/p))` and the after formula to `s<x_p<s/2+mu/E`, with the interval existing only when `mu>E s/2`. The sign identity `x_m=E(x_0/x_p-1)` and explicit tests on both sides of `x_0` now pin the domain in both producers. Producer verdict text is conditional on zero failures, and the independent-source-to-code disposition names the source derivation and fresh-agent re-derivation rather than calling the producers themselves independent derivations.

The 20:05 updated reviewer independently confirmed that reversed inequality and the remaining count drift. Its verbatim report is preserved in [updated-reviewer-20-05.md](reviews/updated-reviewer-20-05.md). **Historical count:** that revision synchronized 131/131 and 32/32. The current package also labels the pulse as finite-Kruskal-support and generates the complete source/review/legacy/output tree as `Archive.zip` in the package directory. The archive is not nested inside itself, and its checksum sidecar is external.

The later 22:06 and 22:18 reviews confirmed the complete reproduction and identified a useful cumulative-flux generalization, the exact mass classification corollary, the positive-post-onset wording, and the archive-layout dependency. Their verbatim reports are preserved in [reviewer-22-06-recheck.md](reviews/reviewer-22-06-recheck.md) and [reviewer-22-18-formal-evaluation.md](reviews/reviewer-22-18-formal-evaluation.md). The cumulative-flux theorem is now included in [11-cumulative-flux-generalization.md](11-cumulative-flux-generalization.md), the mass classification is explicit in [06-finite-pulse.md](06-finite-pulse.md), and the archive is generated in the package directory without being nested inside itself.

The 22:21 review independently reproduced the core algebra but identified real interpretation and validation weaknesses. Its verbatim report is preserved in [reviewer-22-21-evaluation.md](reviews/reviewer-22-21-evaluation.md). The package now puts the `p_eff=1+p` state-equivalence and `~1/p` observer-coordinate stress scaling in the main text, labels interior quadratures as consistency controls, uses real red-run counts and fresh relocated reproduction in the validator, respects `PHYSICS_PYTHON` in the final step, and states AI-reviewed/human-pending status at the top.

The three 02:26–02:28 reviews found the cumulative slope inversion/sign error, the locally-integrable/delta mismatch, the almost-everywhere derivative qualification, the overstrong mass-table cell, a hardcoded relocation path, and Lean/manuscript scope issues. Their reports are preserved in [reviewer-02-26-cumulative-tex-lean.md](reviews/reviewer-02-26-cumulative-tex-lean.md), [reviewer-02-28-package-audit.md](reviews/reviewer-02-28-package-audit.md), and [reviewer-02-28-lean-tex-source.md](reviews/reviewer-02-28-lean-tex-source.md). Doc 11 now uses nonnegative Radon measures and the corrected slope, adds the general horizon corollary, and states one-sided/almost-everywhere derivatives precisely. Lean now includes root factor/sign ordering, derivative factors, named state-equivalence and stress-scaling theorems, and a general-slope lemma. The manuscript now includes definitions and short proofs. The validator uses portable tool/tempdir discovery, receipt freshness checks, real placeholder scans, and archive-current checks.

The 03:32–03:57 reviews confirmed the corrected mathematics and identified the onset matching ambiguity, measure-horizon terminology, finite-logarithmic-null pulse corollary, and self-referential archive packaging defect. Their reports are preserved in [reviewer-03-32-full-evaluation.md](reviews/reviewer-03-32-full-evaluation.md), [reviewer-03-55-referee-update.md](reviews/reviewer-03-55-referee-update.md), and [reviewer-03-57-breakthrough-program.md](reviews/reviewer-03-57-breakthrough-program.md). The matching condition is now `a_+'(0^-)=0`; measure jumps are generalized trapping-boundary crossings; the finite-sigma formula is proved; and [Signed net focusing](12-signed-net-focusing.md) adds the exact signed first-hit, contact, multiplicity, and causal classification. [Breakthrough program](13-breakthrough-program.md) turns the physical next steps into acceptance-gated projects. Archive links no longer pretend the ZIP contains itself, and the checksum sidecar is excluded from the archive.

The full-territory research pass then closed the remaining tractable hunts: [state-pulse phase diagram](14-state-pulse-phase-diagram.md), [physical boundary injection](15-physical-boundary-injection.md), [conformal matter realization](16-conformal-matter-realization.md), and [observables/universality](17-observables-and-universality.md). The exact outcomes include the `p=q` phase boundary, no universal injected-energy threshold, an explicit conserved scalar wavepacket, and a delimitation of chiral-system universality. See [Full-territory close-out](18-close-out.md).

The 12:28 review confirmed the signed-source framework and identified two precision requirements. Its report is preserved in [reviewer-12-28-signed-contact-review.md](reviews/reviewer-12-28-signed-contact-review.md). Doc 12 now distinguishes **first RST-edge contact**, **termination with right-side exclusion**, and **formal later algebraic roots**. Tangential contact is no longer described as nonsingular or as physical reconnection. Doc 15 now states explicitly that its coordinate formula transforms the classical stress only; changing the state frame requires deriving the anomalous `t_+` Schwarzian transformation before transforming `Q_eff`.

The 15:14 and 15:16 reviews are preserved in [reviewer-15-14-boundary-matter-review.md](reviews/reviewer-15-14-boundary-matter-review.md) and [reviewer-15-16-closing-window-review.md](reviews/reviewer-15-16-closing-window-review.md). The finite-null note is now titled **Finite logarithmic-null injection and weighted focusing**, not physical boundary injection. It includes the general `E_focus=lambda^{-2}int T_uu/f'(u) du` identity, all three `F_b` cases, and the retarded closing-window law `u>u_*`. The scalar stress is explicitly the Kim-Son constraint normalization, not an unsupported action-variation claim. The second review's "different physical rays" objection is rejected by the explicit `u=0` control: the same ray is inside the early-pulse window and outside the late-pulse window. Closing-window covariance and no energy-only threshold are both true and compatible.

The 16:56–16:57 reviews are preserved in [reviewer-16-56-onset-atom-review.md](reviews/reviewer-16-56-onset-atom-review.md), [reviewer-16-56-formal-evaluation.md](reviews/reviewer-16-56-formal-evaluation.md), and [reviewer-16-57-package-evaluation.md](reviews/reviewer-16-57-package-evaluation.md). The signed-measure trapping-boundary section now uses `Q_eff(0^-)=0` and treats an onset atom through `Q_eff(0^+)`, including an onset crossing when it reaches `y`. Document 15 requires `f'(u)>0`. Manuscript and notes now say integrated incoming `sigma`-coordinate flux and the same outgoing null ray in the fixed Kruskal chart, not physical boundary energy or an observer-independent physical ray. Lean/PDF freshness now uses source/log/PDF hash receipts instead of timestamps. The manuscript adds a boxed assumptions section and a fuller bibliography. The literature note qualifies `M=0,z>=0` as onset contact rather than a strictly positive root. Reproduction commands use `bash run_verification.sh`, so extraction does not depend on executable-bit preservation. For public-facing redistribution, the original Kim-Son TeX, figure, and tarball are now replaced by official arXiv links and a minimal `source-anchors.txt`. External-source mode checks provenance and anchors without claiming a fresh tar-byte identity check.

The 19:33 adversarial documentation audit is preserved in [reviewer-19-33-doc-audit.md](reviews/reviewer-19-33-doc-audit.md). It found a real algebraically ambiguous printed flux formula, overbroad Lean labels, missing finite-flux conditions, an incomplete zero-flux description, overbroad radiation language, a weak novelty fence, and imprecise null-end/autonomy wording. All eight findings were repaired in the README, manuscript, documents 19–20, and the Lean README.

## 7. Review discipline

No AI review in this package is called external human peer review. Reviewer claims were treated as hypotheses and checked against the source. Valid findings were repaired; incorrect premises were rejected with equations; scope-mismatched work was excluded rather than cited as support.

[Review adjudication](08-review-adjudication.md) · [Formal sign-off](10-formal-signoff.md).
