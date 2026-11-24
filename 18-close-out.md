---
created: 2026-11-24
type: research-disposition
---

# Research disposition and open gates

> [!note] Reading note, 2026-11-24
> Superseded in emphasis by [19 Global structure](19-global-structure.md). "Proved" below means derived on paper; Lean coverage is listed in [lean/README.md](lean/README.md). The "no energy-only threshold" wording is frame dependent, and gate 2 (boundary and bath histories) is not well posed for this solution without an extension.

## 1. Completed research and packaging hunts

| Thread | Disposition | Artifact |
|---|---|---|
| Nonnegative sustained, pulse, and cumulative flux | Proved | [11](11-cumulative-flux-generalization.md) |
| Signed focusing, first contact versus termination, formal later roots, degenerate jets | Proved with exact caveats; every contact reaches the RST edge | [12](12-signed-net-focusing.md) |
| State-pulse phase diagram | Exact `p=q` boundary and same-energy/different-outcome example | [14](14-state-pulse-phase-diagram.md) |
| Finite logarithmic-null injection | Exact pulse formulas and retarded closing-window law; no energy-only threshold | [15](15-physical-boundary-injection.md) |
| Self-consistent matter source | Explicit conserved conformal scalar and backreacted incoming solution | [16](16-conformal-matter-realization.md) |
| Quantum-information signature | Free conformal vacuum gives no automatic wall signature | [17](17-observables-and-universality.md) |
| Universality | Proved for RST-like linear chiral systems, delimited elsewhere | [17](17-observables-and-universality.md) |
| Recent literature | Saito, Arias–Fondevila, Espíndola–Jahnke–Kim, Castro et al. scoped | [Recent spot check](reviews/recent-literature-2025-2026.md) |
| Source license | Assumed 1991–2003 arXiv license identified, wider redistribution restricted | [Source note](sources/README.md) |
| Packaging | External checksum, no self-nesting, absent-archive honesty, fresh relocation | [Evidence](07-evidence-and-reproduction.md) |

## 2. Exact new scientific results

1. **State-pulse phase boundary.** Constant post-onset state level `q` gives termination exactly for `r=p-q>0`, with root and horizon formulas generalizing the sustained case. Identical classical flux gives different outcomes for `q=0` and `q=1`.
2. **Closing-window law.** For `y=e^{-lambda u}`, termination is exactly `u>u_*`, with `u_*=sigma_a-lambda^{-1}ln[(mathcal P/lambda^4)(1-e^{-lambda Delta sigma})]`. Moving the pulse translates the window. No threshold depending only on `E_in` determines it.
3. **Explicit matter realization.** A continuous free conformal scalar wavepacket reproduces the finite-sigma source, satisfies conservation, and carries the exact backreacted wall solution.
4. **Universality boundary.** The theorem generalizes to linear chiral systems, not to arbitrary dilaton potentials or JT by analogy.
5. **Observable limitation.** Free conformal two-point functions contain no explicit `Omega_s` term. A wall-specific boundary signature requires a new state and boundary model.

## 3. Verification state

- Main producer: **138/138**.
- Separate symbolic producer: **39/39**.
- Advanced consistency producer: **22/22** (ten rows that could not fail removed).
- Structure producer: **45/45**.
- Package validation: **13/13**.
- Lean: six modules, cumulative theorem for monotone `Q`, zero-flux structure, symmetries, global causal theorem, final mass parameter, horizon monotonicity, affine-length theorems; no placeholders; 77 axiom audits.
- PDF: compiled manuscript with state and boundary-time results.
- Archive: verified, checksum sidecar external, no self-nested ZIP.
- Fresh relocated reproduction and read-only validation: pass.

## 4. Remaining gates are external or genuinely new programs

These are not hidden unfinished calculations in the current package:

1. **Independent human RST review.** Required before claiming external scientific acceptance or priority.
2. **Boundary-normalized and post-reflection/bath histories.** The finite-null theorem is complete, but a physical boundary energy requires the embedding, induced metric, flux normalization, anomalous state transformation, and outgoing solution.
3. **General quantum-state admissibility and frame transformation.** The constant-`q` phase diagram is exact, but arbitrary `t_+(x)` functions are not automatically physical Hadamard states. Changing the state frame requires deriving its anomalous Schwarzian transformation, not treating `t_+` as an ordinary tensor.
4. **Entropy, islands, and generalized entropy.** No wall-specific information observable is claimed. Free conformal two-point functions do not supply one automatically.
5. **General dilaton gravity.** A broader theorem must derive a new focusing variable from the field equations rather than transplant RST formulas.

The appropriate next publication-stage hunt is a specified bath/reflecting-boundary history with an information observable, not another verification cycle.

[Back to index](00-index.md) · [Research program](13-breakthrough-program.md) · [Global structure](19-global-structure.md).
