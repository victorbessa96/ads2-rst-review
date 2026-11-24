---
created: 2026-11-23
type: formal-acceptance-and-signoff
---

# Formal acceptance and sign-off

## 1. Evidence-linked acceptance checklist

| Gate | Requirement | Evidence | Status |
|---|---|---|---|
| R1 | Source identity and bibliographic scope | [Source bundle](sources/README.md), [Source derivation](02-source-and-derivation.md), tar/TeX SHA-256 match | [x] |
| R2 | Four-sector exact solution and matching | [Exact derivation](02-source-and-derivation.md#2-constraints-and-chiral-integration), canonical residuals | [x] |
| R3 | Root uniqueness and physical-side exclusion | [Unique first hit](03-sustained-flux-theorem.md#1-unique-positive-post-onset-hit) | [x] |
| R4 | Causal character and branch coverage | [Spacelike edge](03-sustained-flux-theorem.md#2-spacelike-edge-and-global-representation), both-positive and fourth-sector checks | [x] |
| R5 | Apparent-horizon ordering | [Horizon census](04-horizon-and-causal-structure.md), `x_hit-x_AH=D/p>0` | [x] |
| R6 | Alternate-state and frame sensitivity | [State and frame](05-state-frame-and-novelty.md) | [x] |
| R7 | Finite-pulse completion | [Complete shutoff theorem](06-finite-pulse.md) | [x] |
| R8 | Null affine parameter | [Affine proof](03-sustained-flux-theorem.md#4-finite-forward-null-affine-parameter) | [x] |
| R9 | Interior-observer proper time | [Observer chart](03-sustained-flux-theorem.md#5-explicit-interior-timelike-observers) | [x] |
| R10 | Novelty and impulsive comparison | [Impulsive wall band](05-state-frame-and-novelty.md#3-impulsive-kim-son-already-has-a-spacelike-wall-band) | [x] |
| R11 | Bounded literature position | [Thirteen-document check](reviews/literature-check.md) | [x] |
| R12 | Main reproduction | `verify.py`: 138/138 PASS | [x] |
| R13 | Independent reproduction | `independent_symbolic.py`: 39/39 PASS | [x] |
| R13A | Advanced consistency reproduction | `advanced_checks.py`: 22/22 PASS | [x] |
| R13B | Structure reproduction | `structure_checks.py`: 45/45 PASS | [x] |
| R13C | Lean build | Six modules, no `sorry`, 77 axiom audits standard only | [x] |
| R14 | Red history preserved | [Red-run record](07-evidence-and-reproduction.md#4-red-run-history-and-instrument-corrections) | [x] |
| R15 | Portable review bundle | Package-relative inputs and commands, no network | [x] |
| R16 | Review findings adjudicated | [FR-01 through FR-11 and second-review obligations](08-review-adjudication.md) | [x] |
| R17 | External human scientific review | Not performed; sign-off form below | [ ] |

The unchecked final row is a review seat, not an unresolved derivation or packaging defect.

## 2. Adversarial questions that now have explicit answers

1. **State choice:** retained Kim-Son `t_pm` is explicit; alternate data produce a mixed-ray threshold.
2. **Integration constants:** fixed by the static pre-solution and `C^0/C^1` matching at every interface.
3. **Onset-axis convention:** the continuous `C^1` solution is independent of the pointwise `Theta` convention on the axes.
4. **Weak branch and singularity:** `Omega>Omega_s` is regular; `Omega'=0` marks the curvature edge, while `e^{2rho}=4/kappa` remains finite.
5. **Causal sign:** negative `dx_m/dx_p` is spacelike under the actual metric convention.
6. **`M=0`:** separated as an already-singular limit.
7. **Ray domain:** statements are restricted to `x_p>0`, `x_m=-y<0`, finite `y>0`.
8. **Clocks:** null affine and explicit interior proper-time results are proved; future-asymptotic clocks are not inferred.
9. **AdS2 scope:** only past-asymptotic AdS2 is claimed.
10. **Semiclassical regime:** no full quantum-gravity continuation is claimed.
11. **Terminology:** singular termination behind an apparent horizon replaces unqualified pileup language.
12. **Priority:** a bounded absence-of-evidence result replaces any literature-wide novelty assertion.

## 3. Reproduction sign-off template

```text
Reviewer identity and affiliation:
Review date:
Reviewer roles:

Primary source independently read: YES / NO
Four-sector solution independently re-derived: YES / NO
Impulsive comparison independently re-derived: YES / NO
Finite-pulse solution independently re-derived: YES / NO
Apparent-horizon ordering independently re-derived: YES / NO
Null affine and interior proper-time arguments checked: YES / NO

Canonical battery reproduced: 138 / 138
Independent symbolic battery reproduced: 39 / 39
Advanced research battery reproduced: 32 / 32
Source provenance and official links verified: YES / NO
Manifest hashes reproduced: YES / NO

Sustained theorem verdict: ACCEPT / ACCEPT WITH WORDING CHANGES / REJECT / BLOCKED
Finite-pulse theorem verdict: ACCEPT / ACCEPT WITH WORDING CHANGES / REJECT / BLOCKED
Taxonomy and novelty verdict: ACCEPT / ACCEPT WITH WORDING CHANGES / REJECT / BLOCKED
Reproduction verdict: PASS / PASS WITH INSTRUMENT CAVEATS / FAIL

Findings by ID:
Required wording changes:
Residual disagreements:
Reviewer signature:
```

## 4. Acceptance rule

A scientific acceptance requires independent examination of the source equations and derivations, not just green scripts. A reproduction-only PASS is not a physical-scope PASS. Any stronger future-boundary, absorber, arbitrary-state, or literature-priority claim requires new evidence outside this package.

[Return to index](00-index.md).
