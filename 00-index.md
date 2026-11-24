---
created: 2026-11-23
updated: 2026-11-24
type: adversarial-review-index
status: ai-reviewed-human-scientific-review-pending
---

# Kim-Son AdS2-RST one-sided flux: complete review package

> [!important] Status
> This package is AI-reviewed, with human scientific review pending. Every actionable finding from the supplied AI reviews has been adjudicated and mechanically checked within the fixed Kim-Son state and source conventions. No external human peer review is claimed.

## 1. Verified result in one paragraph

For the Kim-Son past-asymptotically-AdS2 RST branch with retained `t_pm` and one-sided classical flux constant in Kruskal `x_p`, every specified mixed-region ray `x_m=-y`, `y>0`, reaches `Omega=Omega_s` at finite `x_p`. This retained-state every-ray statement is equivalent to an alternate `t_+`-on problem with `p_eff=1+p`: the step-off supplies the critical `lambda^2` in that comparison. It is not an arbitrary-state or observer-frame energy claim. The edge is spacelike and lies behind an apparent horizon. The ray also reaches the edge at finite forward affine parameter. Explicit interior constant-`sigma_1` timelike curves reach it at finite proper time from any finite earlier point. A finite-Kruskal-support pulse on `0<x_p<x_s` has a spacelike wall exactly on the ray band `0<y<E`, where `E=p*x_s`; rays with `y>=E` have no wall. Finite support in this Kruskal coordinate is not finite duration in an observer-adapted time coordinate. The follow-on phase work adds the exact `p=q` state boundary, a retarded closing-window law with no energy-only threshold, an explicit conformal-scalar realization, and a precise RST-like universality boundary. These remain fixed-model results, not arbitrary-state absorber or future-asymptotic-observer theorems.

## 2. Fresh evidence

| Surface | Actual result | Meaning |
|---|---:|---|
| Main producer | **138/138 PASS**, exit 0 | Canonical 88 checks plus 50 review-closure checks |
| Separate symbolic producer | **39/39 PASS**, exit 0 | Separate implementation, not an independent derivation |
| Advanced research producer | **32/32 PASS**, exit 0 | State phases, onset atoms, closing-window law, matter, and universality controls |
| Red-first development run | 125/129 | Four instrument errors, preserved and repaired |
| Red-second instrument run | 128/129 | Whole-quotient substitution defect, preserved and repaired |
| Source provenance | External arXiv links and retained anchors | Full TeX not redistributed; expected hash recorded |
| Interior observers | Three quadrature rows | Finite `sigma_0` hit and finite proper time |
| Finite pulse | Twelve existence rows | Exact `0<y<E` cutoff reproduced |
| Literature | Thirteen primary documents | Exact target not found in that bounded corpus, no priority claim |
| Lean 4 | **Algebraic core and abstract first-hit criterion formalized** | Root, factor/sign ordering, actual derivative, IVT, state equivalence, and after-domain sign |
| LaTeX | **PDF compiled** | Full manuscript with cumulative-flux generalization |
| Package validation | **12/12 PASS** | Includes fresh relocation, advanced checks, Lean/PDF freshness, archive currency, links, provenance, and manifest |

See [Evidence and reproduction](07-evidence-and-reproduction.md) and the raw [verification summary](outputs/verification-summary.json).

## 3. Reading map

| Document | Purpose |
|---|---|
| [01 Executive claim and scope](01-executive-claim.md) | Main theorems, contribution, terminology, and hard claim fence |
| [02 Primary source and derivation](02-source-and-derivation.md) | Kim-Son source map, constraints, four-sector integration, physical branch |
| [03 Sustained flux theorem](03-sustained-flux-theorem.md) | Root, causal class, null affine parameter, and explicit interior observers |
| [04 Horizon and causal structure](04-horizon-and-causal-structure.md) | Apparent-horizon curves and horizon-before-wall ordering |
| [05 State, frame, and novelty](05-state-frame-and-novelty.md) | Alternate state data, impulsive comparison, coordinate flux, bounded literature |
| [06 Finite-pulse theorem](06-finite-pulse.md) | Complete shutoff solution, exact ray band, post-shutoff wall and horizon |
| [07 Evidence and reproduction](07-evidence-and-reproduction.md) | Commands, check taxonomy, red history, limitations, and artifact map |
| [08 Review adjudication](08-review-adjudication.md) | Every FR-01 through FR-11 and second-review obligation closed |
| [09 Independent reviews](09-independent-reviews.md) | Review history, corrected reviewer errors, and final independent verdicts |
| [10 Formal sign-off](10-formal-signoff.md) | Evidence-linked acceptance checklist and external-reviewer form |
| [11 Cumulative-flux generalization](11-cumulative-flux-generalization.md) | Nonnegative measure-valued flux classified by total cumulative flux |
| [12 Signed net focusing](12-signed-net-focusing.md) | Necessary-and-sufficient signed first-hit criterion, causality, finite-sigma pulses |
| [13 Breakthrough program](13-breakthrough-program.md) | Physical boundary injection, self-consistent matter, state phase diagram, observables |
| [14 State-pulse phase diagram](14-state-pulse-phase-diagram.md) | Exact `p=q` net-focusing phase boundary and same-energy/different-outcome example |
| [15 Finite logarithmic-null injection](15-physical-boundary-injection.md) | Exact pulse hits, retarded closing-window law, and no energy-only threshold |
| [16 Conformal matter realization](16-conformal-matter-realization.md) | Explicit conserved scalar wavepacket and backreacted incoming solution |
| [17 Observables and universality](17-observables-and-universality.md) | Free-scalar signature test and exact RST-like universality boundary |
| [18 Research disposition](18-close-out.md) | Completed results and remaining external or new-program gates |
| [Lean proof project](lean/AdS2RST.lean) | Machine-checked algebraic core and abstract intermediate-value theorem |
| [Manuscript](manuscript/ads2-rst-one-sided-flux.tex) | Complete LaTeX derivation and theorem statements |

Supporting material:

- [Primary source bundle](sources/README.md)
- [Bounded literature check](reviews/literature-check.md)
- [Recent 2025–2026 literature spot check](reviews/recent-literature-2025-2026.md)
- [Original Claude review](reviews/claude-opus-5-5-review.md)
- [Original second AI review](reviews/second-ai-review.md)
- [Updated 20:05 review](reviews/updated-reviewer-20-05.md)
- [22:06 recheck](reviews/reviewer-22-06-recheck.md)
- [22:18 formal evaluation](reviews/reviewer-22-18-formal-evaluation.md)
- [Legacy evidence](legacy/canonical-result-note.md)

## 4. Portable reproduction

Run from this directory with the existing physics environment:

```bash
./run_verification.sh
# To use a different Python installation with the pinned dependencies:
PHYSICS_PYTHON=/path/to/python ./run_verification.sh
# Optional formal/PDF rebuild:
RUN_LEAN=1 LAKE_BIN=/path/to/lake TECTONIC_BIN=/path/to/tectonic ./run_verification.sh
```

The producers use package-relative inputs and write only under `outputs/`; the validator separately writes `manifest.json` and `validation.json` at the package root and refreshes `outputs/portability-receipt.json` in normal mode. No network or Obsidian vault access is required for the core Python battery. The relocation test proves same-interpreter filesystem portability, not independent environment setup or container portability. The optional Lean build uses the pinned Lean 4.36.0 toolchain and downloaded Mathlib cache, excluded from the archive; the PDF is already included.

## 5. Binding non-claims

- No general AdS2 instability or pure-JT result is inferred.
- No transparent, reflecting, or coupled future absorber is constructed.
- Interior timelike curves are not future-asymptotic boundary observers.
- A bounded literature search is not exhaustive publication-priority proof.
- Semiclassical singular termination is not a full quantum-gravity resolution.
- External human scientific review remains a sign-off state, not an unresolved calculation.

## 6. Disposition

The complete finding ledger is in [Review adjudication](08-review-adjudication.md). The acceptance gate is in [Formal sign-off](10-formal-signoff.md). Final machine receipts are [manifest.json](manifest.json) and [validation.json](validation.json).

The complete portable archive is generated as `Archive.zip` in this directory, including the source, review, legacy, and output trees. It is not nested inside itself. Its checksum sidecar is external to the archive.
