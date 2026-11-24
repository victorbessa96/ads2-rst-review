# Collapse of the Kim–Son AdS₂ wormhole in the RST model

**An exactly solvable, machine-checked account of how a two-dimensional semiclassical wormhole turns into a black hole.**

Authors: **Razul (AI agent)** and **Victor Bessa**

Paper: [manuscript/ads2-rst-one-sided-flux.pdf](manuscript/ads2-rst-one-sided-flux.pdf) · Proofs: [lean/](lean/README.md) (Lean 4 + Mathlib, 77 audited results, no `sorry`) · Status: **independent human scientific review pending**

---

## Why this is worth a look

Wormholes that can be crossed need negative energy, and the question of what happens when that support is disturbed (does the throat close, does a black hole form, is the outcome predictable?) is usually only answerable numerically. Two-dimensional dilaton gravity is the standard laboratory where such questions can be answered exactly, because the quantum back-reaction of matter is included in closed form. The Russo–Susskind–Thorlacius (RST) model is the best known example, and it is where the modern picture of black-hole evaporation was first worked out in a solvable setting.

In 2004 W. T. Kim and E. J. Son found a static wormhole in the RST model whose two ends approach AdS₂, supported by a constant quantum state, and showed that an infalling shell of matter turns it into a black hole ([arXiv:gr-qc/0404098](https://arxiv.org/abs/gr-qc/0404098)). That paper treats one shell. This repository works out the general case and the global structure, and finds that the accepted reading of the solution needs correcting in several places.

## What is established here

All statements are theorems about the RST equations in Kruskal gauge with the Kim–Son boundary state. The notation is `Fhat = (Omega - Omega_s)/L`, with the singularity at `Fhat = 0`.

| # | Result | Why it matters | Lean |
|---|---|---|---|
| 1 | **The black hole is there with no matter at all.** With zero classical flux the region to the future of the switch-off point is exactly the interior of the eternal RST black hole in the Hartle–Hawking state. | The wormhole collapses because its supporting state is switched off, not because matter falls in. Kim and Son attribute the collapse to the shell. | yes |
| 2 | **Total-flux criterion.** For any nonnegative incoming flux (continuous, pulsed or impulsive), an outgoing ray `x^- = -y` is captured if and only if `y < E_tot`, the total Kruskal null momentum over `lambda^2`. The hit is unique and lies behind the apparent horizon; `x^- = -E_tot` is the event horizon. | One inequality replaces the case-by-case formulas. It is the Kim–Son-state analogue of the classical RST/Thorlacius horizon formula and is credited as such. | yes |
| 3 | **Global causal structure.** With nonnegative flux in both directions, the singular set is a future set: the singularity is acausal, future-trapped and never naked. | Unlike the evaporating RST black hole, no boundary condition at the singularity is needed: the exact solution is fixed by the data on the past null boundaries. | yes |
| 4 | **Final state.** After the flux ends, the exterior is again a Kim–Son zero-flux exterior with a larger parameter. The mass parameter grows by `M_inf + P_+^2/(2 lambda)`. | The first term is the classical mass. The second is new and comes from the wormhole's own supporting state. | yes |
| 5 | **Horizon monotonicity.** `e^{-2 phi}` (the dilaton-gravity analogue of area) never decreases to the future along the event horizon, and grows outward along the apparent horizon. | An area-theorem-type statement on the event horizon for the full semiclassical solution. | yes |
| 6 | **Outgoing radiation.** The flux at future infinity that Kim and Son computed for one shell holds for every matter profile, with the shell strength replaced by `E_tot`. In the asymptotically flat frame it is the Hawking value `kappa lambda^2/4` minus a decaying transient `lambda^4 e^{-2 lambda sigma^-}`. | The transient is the wormhole's negative energy leaving (Kim and Son already identify it as background, not radiation). The black hole does not evaporate: it is in equilibrium with incoming thermal radiation. | no (paper + numerics) |
| 7 | **The AdS₂ ends are not boundaries.** They are null, reached at finite affine distance (at most `2/lambda^2` beyond unit separation), with bounded curvature. There is no timelike conformal boundary. | Holographic notions (boundary observers, reflecting walls, baths) have no referent in this solution without further construction. | yes, given the dilaton branch |
| 8 | **State dependence.** If the incoming part of the supporting state is kept, sustained matter closes the wormhole only above the threshold `P > lambda^2`. | The "arbitrarily weak flux closes the wormhole" statement is a property of the switch-off convention. | yes |

A short guide to the physics is in [19-global-structure.md](19-global-structure.md) and [20-causal-structure-and-final-state.md](20-causal-structure-and-final-state.md).

## What is and is not claimed

- **Credit.** Results 2, 3 and the first term of 4 extend standard results of the classical model (CGHS, RST, Thorlacius, Strominger). The Kruskal-frame formula in result 6 is Kim and Son's for the shell. Result 1 is the semiclassical counterpart of a classical observation by Hayward, Kim and Lee. The manuscript states this where each result appears.
- **Novelty.** A bounded literature search (the INSPIRE citation record of the Kim–Son paper and the RST/CGHS literature cited in the manuscript) did not find results 1, 2, 7 and 8 for this solution. Results 3 to 6 were added afterwards and were checked only against the sources already collected for that search, not by a new one. No priority is claimed beyond that search.
- **Review.** The work was produced by an AI agent working with a human author and checked by machine. **No independent human specialist has reviewed it.** AI reviews kept under [reviews/](reviews/) are history, not peer review.
- **Mathematical difficulty.** The theorems are elementary. Their interest is in what they say about the model.

## What "machine-checked" means here

The Lean 4 development ([lean/](lean/README.md)) proves the statements marked "yes" above from the normalized constraint equation onward. It contains no `sorry` and depends only on the three standard axioms (`propext`, `Classical.choice`, `Quot.sound`); the build log prints the axiom dependencies of 77 named results and the validator checks them.

Not formalized, and stated as such in the manuscript:

- the reduction of the RST action to the Kruskal-gauge equations (taken from the literature);
- existence of the weak-coupling dilaton branch (the Lambert-W inversion), which enters the affine-length theorems as a hypothesis;
- the identification of spacetime causal order with coordinate order in conformal gauge;
- result 6 and the curvature limits, which are paper arguments checked numerically.

Python scripts (SymPy, mpmath) integrate the constraints sector by sector, compare with the printed Kim–Son solution and test every result numerically. They are consistency controls. Their count carries no evidential weight.

## Open problems

1. **Evaporation.** Replace the equilibrium state after switch-off by the future vacuum. The effective flux is then not monotone, result 3 fails, and a naked timelike singularity with a boundary condition is expected. This is the natural next step.
2. **Entropy.** A generalized-entropy or island computation on this background, and whether result 5 extends to it.
3. **Energy.** Whether the mass parameter of result 4 is an energy measured at the future end.
4. **Admissibility of the state.** The Hadamard property of the step-function boundary state.
5. **Beyond the null ends.** Any extension that would give the solution a timelike boundary.
6. **Formalization.** The dilaton branch and the action reduction in Lean.

## Reproduce

```bash
python3 -m pip install -r requirements.txt
bash run_verification.sh            # Python checks, archive, package validation
RUN_LEAN=1 bash run_verification.sh # also rebuilds the Lean proofs and the PDF
READ_ONLY=1 python3 validate_package.py   # validate a fresh clone without rewriting anything
```

`RUN_LEAN=1` needs `lake` (Lean 4.36.0, Mathlib; first build downloads the Mathlib cache) and `tectonic` on `PATH`, or `LAKE_BIN` and `TECTONIC_BIN`. `PHYSICS_PYTHON` selects the interpreter.

| Surface | Expected result |
|---|---:|
| Main verification (`verify.py`) | **138/138 PASS** |
| Separate symbolic checks (`independent_symbolic.py`) | **39/39 PASS** |
| Advanced consistency checks (`advanced_checks.py`) | **22/22 PASS** |
| Structure checks (`structure_checks.py`) | **45/45 PASS** |
| Lean build | **no `sorry`; 77 axiom audits, standard axioms only** |
| Package validation | **13/13 PASS** |
| Markdown links | **242 resolved, 0 unresolved** |

The validator runs a relocated reproduction, compares manifest hashes, and checks that the Lean and PDF receipts match the current sources.

## Repository map

| Path | Content |
|---|---|
| [manuscript/](manuscript/ads2-rst-one-sided-flux.pdf) | The paper ([TeX source](manuscript/ads2-rst-one-sided-flux.tex)) with a table mapping each statement to its Lean name |
| [lean/](lean/README.md) | Lean 4 project: `Core`, `Profile`, `Cumulative`, `Structure`, `Global`, `Affine` |
| [19-global-structure.md](19-global-structure.md), [20-causal-structure-and-final-state.md](20-causal-structure-and-final-state.md) | Plain-language statements of the main results; these take precedence over earlier wording |
| [00-index.md](00-index.md) | Full map of the working documents 01 to 18 (derivation, special cases, review history) |
| [structure_checks.py](structure_checks.py), [verify.py](verify.py), [independent_symbolic.py](independent_symbolic.py), [advanced_checks.py](advanced_checks.py) | Symbolic and numerical checks |
| [validate_package.py](validate_package.py), [run_verification.sh](run_verification.sh), [build_archive.py](build_archive.py) | Reproduction and integrity tooling |
| [outputs/](outputs/) | Logs and receipts of the last run |
| [reviews/](reviews/) | Literature checks and the AI review history |
| [Archive.zip](Archive.zip) | Snapshot of the package with [checksum](Archive.zip.sha256) |

Documents 01 to 18 are the dated working record. They contain the closed formulas for sustained flux, finite pulses and logarithmic-time pulses, and the history of corrections. Where their wording differs from documents 19 and 20 or from the manuscript, the later documents are authoritative.

## Primary source and license

The original Kim–Son TeX, figure and tarball are **not redistributed**. [sources/README.md](sources/README.md) links to the arXiv abstract, PDF, source and DOI and records the hash of the TeX that was checked. `sources/source-anchors.txt` keeps only the short equation fragments used by the lexical checks.

## Citation

Cite the original model first:

> W. T. Kim and E. J. Son, *Wormhole phase in the RST model*, JHEP 0408:006 (2004), arXiv:gr-qc/0404098, DOI 10.1088/1126-6708/2004/08/006.

Then this repository, with the commit used:

> Razul (AI agent) and V. Bessa, *Collapse of the Kim–Son AdS₂ wormhole in the RST model: zero-flux black hole, total-flux criterion, and global causal structure*, 2026. Research manuscript, human scientific review pending.
