---
created: 2026-11-23
type: review-finding-disposition-ledger
---

# Review adjudication and closure ledger

## 1. Disposition vocabulary

- **Resolved:** a real evidence or derivation gap was closed.
- **Resolved by scoping:** the mathematics stands, but the wording or taxonomy was narrowed.
- **Rejected:** the review premise fails against the source or exact algebra.
- **External sign-off:** no calculation remains, but a human reviewer has not signed.

No finding below remains in `open` status.

## 2. Claude findings

| ID | Disposition | Evidence and resolution |
|---|---|---|
| FR-01, alternate `t_+` | **Resolved by scoping** | The main theorem already retains explicit Kim-Son state data. The alternate variant is now derived: no mixed hit for `p<=1`, a unique positive mixed hit for `p>1`. The both-positive wall caveat is added, so there is no false all-wall elimination claim. See [State sensitivity](05-state-frame-and-novelty.md#1-alternate-state-data-the-mixed-ray-threshold-is-real-but-scoped). |
| FR-02, impulsive-source novelty | **Resolved by scoping** | Kim-Son's impulse already has a spacelike wall on `0<y<alpha`. The new contribution is narrowed to every-ray sustained termination, exact first-hit laws, and the finite-pulse completion. The corrected impulsive sign is verified. See [Impulsive comparison](05-state-frame-and-novelty.md#3-impulsive-kim-son-already-has-a-spacelike-wall-band). |
| FR-03, Kruskal-constant flux | **Resolved by scoping** | Every main statement now says constant in Kruskal `x_p`. The tensor transformation `T_{sigma sigma}=lambda^2x_p^2P` is included and distinguished from a complete observer-energy theorem. |
| FR-04, apparent horizon | **Resolved** | Full sector horizon census, `x_AH=y/p`, `x_hit-x_AH=D/p>0`, finite-pulse continuation `y=E`, and interior-observer horizon-before-wall proof added. See [Horizon structure](04-horizon-and-causal-structure.md). |
| FR-05, finite pulse | **Resolved** | Complete during/after `C^1` solution, exact `0<y<E` existence criterion, post-shutoff root, causal class, both-positive branch, horizon, and degeneracies are proved and executed. See [Finite-pulse theorem](06-finite-pulse.md). |
| FR-06, source derivation | **Resolved** | The constraint integration, chiral functions, four sectors, and matching constants are written explicitly in [Primary source and derivation](02-source-and-derivation.md). |
| FR-07, portable reproduction | **Resolved** | Producers, independent generator, source anchors and official links, canonical legacy evidence, and supplied reviews are included locally. Commands use package-relative paths and require no network. |
| FR-08, missing independent generator | **Resolved** | `independent_symbolic.py` is included and freshly returns 39/39 PASS. The older generator-less receipt is demoted to legacy context. |
| FR-09, conformal factor | **Rejected** | At `Omega_s`, `e^{-2phi}=kappa/4`, so `e^{2rho}=4/kappa` is finite and nonzero. No limiting-conformal-factor caveat is needed. See [Physical branch](02-source-and-derivation.md#3-physical-branch-and-conformal-factor). |
| FR-10, producer labels | **Resolved** | The both-positive label now says derivative identity, and the small-flux label says numerical control. Exact sign and limit proofs remain in the theorem notes. |
| FR-11, evidence presentation | **Resolved** | The package leads with the scoped theorem and derivation. Gates, grids, links, and hash metrics are isolated in the evidence appendix rather than presented as the physics. |

## 3. Second-review obligations

| Obligation | Disposition and evidence |
|---|---|
| Finite-pulse behavior | **Resolved** by the exact `0<y<E` theorem in [Finite-pulse theorem](06-finite-pulse.md). |
| Quantum-state sensitivity | **Resolved** by the alternate `t_+` threshold and both-positive qualification in [State sensitivity](05-state-frame-and-novelty.md). |
| Global causal structure | **Resolved to local trapping scope** by the full horizon census and horizon-before-wall proof. No unsupported global event-horizon claim is added. |
| Boundary and observer completion | **Resolved by scoping** | Explicit interior timelike curves and finite proper-time intervals are proved. Future-asymptotic boundary observers and absorbers remain correctly outside the fixed model. |
| `M=0` interpretation | **Resolved by scoping** | `mu>0` is the principal regular-wormhole case; `mu=0` is a separate already-singular limit. |
| “Pileup” terminology | **Resolved by scoping** | Leading wording is spacelike singular termination behind an apparent horizon. |
| Literature novelty | **Resolved to bounded evidence** | Thirteen primary documents checked; exact target not found there. No exhaustive priority claim. See [Bounded literature check](reviews/literature-check.md). |
| Independent source-to-code audit | **Resolved by explicit source derivation, independent fresh-agent re-derivation, and two producers.** The 138-check and 39-check scripts test the entered candidates; they are not themselves independent derivations, and are not presented as such. |
| “Potentially publishable” assessment | **Resolved by scoping** | No publication-readiness or priority verdict is advertised. The package is an adversarial-review object. |

## 4. Reviewer errors and scope failures handled without hiding them

1. **Impulsive transcription error:** a research subagent briefly wrote `y+alpha` instead of `y-alpha`. Direct TeX reconciliation and a numeric control corrected the verdict. The final impulsive theorem uses the source's negative chiral contribution.
2. **Finite-pulse scope mismatch:** another subagent solved the alternate retained-`t_+` problem with `q=P-lambda^2`, not the assigned Kim-Son step-off state. That work is excluded as evidence for this package's pulse theorem. The assigned model was re-derived independently and is what `verify.py` tests.
3. **Claude FR-09:** rejected explicitly rather than implemented.
4. **Legacy labels and missing generator:** corrected in the new producer instead of being excused only in prose.

## 5. Remaining non-claims, not open calculations

The following are deliberately not asserted and therefore are not hidden open threads:

- future-asymptotic boundary observer completion;
- transparent, reflecting, or coupled absorber dynamics;
- arbitrary admissible quantum-state response;
- full quantum-gravity continuation through `Omega_s`;
- exhaustive literature priority;
- external human scientific acceptance.

Every actionable review finding is closed. [Formal sign-off](10-formal-signoff.md) contains the acceptance checklist.
