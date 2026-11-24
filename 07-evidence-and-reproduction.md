---
created: 2026-11-23
type: evidence-and-reproduction-record
---

# Evidence and reproduction

## 1. Evidence hierarchy

1. **Source-level derivations** carry the theorem. Start with [Primary source and derivation](02-source-and-derivation.md).
2. **Exact SymPy identities** check roots, signs, matching conditions, horizon relations, and observer coordinates.
3. **90-digit mpmath controls** check sampled behavior and quadrature. Grids do not prove universal statements.
4. **Lean 4 formalization** machine-checks the statements listed in [lean/README.md](lean/README.md). It is the strongest evidence in the package for those statements and says nothing about the ones it does not cover.
5. **AI review** supplies scrutiny, not external human peer review. A review by an AI system that later contributed to the package is not independent evidence.
6. **Documentation and hash gates** establish package integrity only.

`independent_symbolic.py` is a second implementation of the same formulas, not an independent derivation. `structure_checks.py` (45 checks) integrates the constraints sector by sector and checks the zero-flux, symmetry and geometry statements of [document 19](19-global-structure.md) and the causal-structure, mass, monotonicity and radiation statements of [document 20](20-causal-structure-and-final-state.md). Ten rows of `advanced_checks.py` that could not fail were removed on 2026-11-24.

## 2. Fresh executed results

| Group | Checks | Passed | Failed |
|---|---:|---:|---:|
| Canonical original battery | 88 | 88 | 0 |
| Source provenance | 1 | 1 | 0 |
| Sustained-proof additions | 2 | 2 | 0 |
| Horizon | 2 | 2 | 0 |
| Conformal factor | 1 | 1 | 0 |
| Impulsive comparison | 4 | 4 | 0 |
| State sensitivity | 4 | 4 | 0 |
| Finite pulse | 20 | 20 | 0 |
| Cumulative generalization | 2 | 2 | 0 |
| Signed net focusing | 4 | 4 | 0 |
| Finite-sigma pulse | 1 | 1 | 0 |
| Null affine | 3 | 3 | 0 |
| Interior observer | 6 | 6 | 0 |
| **Total, `verify.py`** | **138** | **138** | **0** |
| **Total, `independent_symbolic.py`** | **39** | **39** | **0** |
| **Total, `advanced_checks.py`** | **32** | **32** | **0** |

Raw artifacts:

- [Main output](outputs/verify.out)
- [Main structured summary](outputs/verification-summary.json)
- [Independent output](outputs/independent_symbolic.out)
- [Independent structured summary](outputs/independent-symbolic-summary.json)

## 3. Portable commands and validation modes

From this directory:

```bash
./run_verification.sh
# To use a different Python installation with the pinned dependencies:
PHYSICS_PYTHON=/path/to/python ./run_verification.sh
```

The producers use package-relative inputs and write only under `outputs/`; the validator separately writes `manifest.json` and `validation.json` at the package root. The primary source and all legacy evidence needed for review are included. `requirements.txt` pins the two scientific dependencies, and `run_verification.sh` allows an external reviewer to select any compatible interpreter through `PHYSICS_PYTHON`.

Receipt generation and read-only verification are separate:

```bash
# Generate fresh receipts:
./run_verification.sh
# Verify existing receipts without rewriting them or running producers:
READ_ONLY=1 python3 validate_package.py
```

A relocated-copy test copied the entire package to a fresh scratch directory, ran all four producers there, and obtained **138/138**, **39/39**, **22/22**, and **45/45** again. The relocated main output is byte-identical to the package output. Normal validator runs now perform this relocation fresh; `READ_ONLY=1` uses the existing receipt without executing anything. See [portability-receipt.json](outputs/portability-receipt.json). This proves same-interpreter filesystem portability, not independent environment setup or container portability.

Validated environment:

| Component | Value |
|---|---|
| Python | CPython 3.14.9 |
| SymPy | 1.14.0 |
| mpmath | 1.3.0, used at 90 dps |
| Platform | Linux 7.2.14-arch1-1 x86_64 GNU/Linux |
| Network required | No |

## 4. Red-run history and instrument corrections

### Original battery

- **77/83:** three wrong source-line targets and three incorrect finite-`S` asymptotic assertions.
- **79/80:** the corrected convergence sequence needed one further decade.
- **87/88:** SymPy did not infer `sqrt(1+p)>1`; `q=sqrt(1+p)-1>0` made the sign proof explicit.
- **88/88:** final canonical battery.

Original red artifacts are retained under `legacy/`.

### Review-closure battery

- **125/129:** one impulsive-sign inference and three finite-pulse substitutions were underspecified.
- The impulsive denominator is proved positive with `a=y+h`, `h>0`.
- `E=p*s` is substituted explicitly for shutoff and horizon identities.
- **128/129:** a strengthened post-shutoff inequality check initially substituted only the numerator rather than the complete quotient. This was another instrument error, not a change in the root formula.
- **129/129:** historical development battery, not the current count. The red outputs and structured summaries are preserved as [red-first.out](outputs/red-first.out), [red-first-summary.json](outputs/red-first-summary.json), [red-second.out](outputs/red-second.out), and [red-second-summary.json](outputs/red-second-summary.json).

No failing physics check was deleted. The producer labels criticized in FR-10 were also narrowed: the both-positive label now identifies a derivative identity, and the small-flux label identifies a numerical control.

## 5. Independent generator provenance

`independent_symbolic.py` is included and produces `INDEPENDENT_SYMBOLIC: 39/39 PASS`. This closes FR-08's missing-generator finding for the current package. The older package's generator-less 7/7 receipt is retained only as legacy context, not as the current independent gate.

## 6. Source and artifact integrity

The full TeX was locally verified as byte-identical to its tar member, with SHA-256 `8906ec46e685404da151c8b7d52a325c4053ee8c8f17964df7264c69baf58872`. The public-facing package now uses official arXiv links and short retained anchors instead of redistributing the full paper. External-source validation checks those links and the anchor file; it does not claim a fresh tar-byte identity check.

Package map:

| Path | Role |
|---|---|
| `verify.py` | Main 138-check producer |
| `independent_symbolic.py` | Separate 39-check producer (second implementation, not a second derivation) |
| `structure_checks.py` | 45-check producer for derivation, zero-flux structure, symmetries, geometry, global causal structure and final state |
| `build_archive.py` | Rebuilds `Archive.zip` and its checksum from the manifest; called by `run_verification.sh` |
| `advanced_checks.py` | Advanced 32-check producer for state phases, onset atoms, closing-window law, matter, and universality |
| `sources/` | Primary tar, TeX, figure, and bibliographic note |
| `legacy/` | Original producer, canonical outputs, red history, and internal reviews |
| `reviews/` | Supplied AI reviews and bounded primary-literature check |
| `outputs/` | Fresh scientific receipts and preserved development red run |
| `manifest.json` | Complete artifact sizes, roles, and hashes |
| `validation.json` | Final gate receipt, distinct from scientific acceptance |

## 7. Lean proof and LaTeX manuscript

The formal Lean 4.36.0 project in `lean/AdS2RST.lean` formalizes the algebraic core and the abstract continuous first-hit criterion: sustained candidate root, uniqueness, factor/sign ordering, an actual `HasDerivAt` computation for `F_y`, negative general slope, retained-state equivalence, stress scaling, and after-shutoff sign domain. It does not formalize the full measure-theoretic cumulative theorem. Selected theorem-axiom reports contain only `propext`, `Classical.choice`, and `Quot.sound`, not `sorryAx`. Build receipt: [lean-build.out](outputs/lean-build.out). The validator checks source/log/PDF hash receipts instead of filesystem timestamps, scans the Lean code for `sorry`/`admit`/`axiom`, and verifies the archive's core files against the current sources. This avoids false freshness failures after ZIP extraction on filesystems with different timestamp behavior.

The full manuscript is [ads2-rst-one-sided-flux.tex](manuscript/ads2-rst-one-sided-flux.tex), with the compiled [PDF](manuscript/ads2-rst-one-sided-flux.pdf) and [Tectonic receipt](outputs/tectonic-build.out). It includes the cumulative-flux generalization, exact mass classification, state-pulse phase boundary, finite-null closing-window theorem, and matter realization.

Optional Lean/PDF build:

```bash
RUN_LEAN=1 LAKE_BIN=/path/to/lake TECTONIC_BIN=/path/to/tectonic ./run_verification.sh
```

The Python battery and PDF are offline. `run_verification.sh` defaults to `python3`; set `PHYSICS_PYTHON` to a compatible interpreter. `RUN_LEAN=1` discovers `lake` and `tectonic` on `PATH`, or accepts `LAKE_BIN`/`TECTONIC_BIN`. Relocation uses the system temporary directory. The optional Lean build requires the pinned toolchain and downloaded Mathlib cache; `lean/.lake/` is excluded from the archive to avoid vendoring thousands of dependency files.

`Archive.zip` is generated in the package directory but is not nested inside itself. `Archive.zip.sha256` is an external sidecar and is deliberately excluded from the ZIP. In an extracted package with no sibling archive, read-only validation reports `archive_status=not-present-not-claimed` and `archive_verified=false` rather than claiming an archive check passed. When an archive is present, the validator checks its core-file currency and sidecar digest.

## 8. Instrument limitations that remain explicit

- The producer checks entered candidate solutions. The source-level integration in [Primary source and derivation](02-source-and-derivation.md) is the actual derivation.
- Source-line checks are lexical anchors for the exact `kruskal:cons` and `omegasol` equations; reviewers must read the cited equations. The package does not treat them as an independent proof of the constraint normalization.
- Numerical grids and quadratures are controls, not general proofs.
- The 138 checks are not 138 independent derivations.
- The literature search is bounded to thirteen named primary documents and is not exhaustive.
- No future-asymptotic absorber or arbitrary-state completion is validated by this battery.

Next: [Review adjudication](08-review-adjudication.md).
