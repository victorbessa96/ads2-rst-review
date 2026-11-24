# Kim–Son AdS₂–RST one-sided flux research package

A reproducible mathematical-physics package for the Kim–Son past-asymptotically-AdS₂ RST wormhole branch: sustained one-sided flux, finite pulses, nonnegative and signed cumulative focusing, state-dependent phase boundaries, and finite logarithmic-null injection.

**Status:** internal research and adversarial review. Independent human scientific review remains pending. The repository is private by default; it is not presented as accepted or priority-established work.

## Central results

The sustained normalized excess is

\[
F(x,y)=\mu+\frac{y^2}{2}+xy-\frac{p}{2}x^2,\qquad p>0,\ \mu>0,\ y>0.
\]

Its unique positive root is

\[
x_{\mathrm{hit}}=\frac{y+\sqrt{(1+p)y^2+2p\mu}}{p},
\]

with a spacelike singular edge and an apparent-horizon precursor.

For a nonnegative Radon-measure flux, define

\[
Q(x)=\frac1{\lambda^2}\int_{[0,x]}dT(u),\qquad E_{\mathrm{tot}}=Q(+\infty).
\]

The finite-pulse classification is:

- `E_tot = +infinity`: every finite `y>0` terminates.
- `E_tot < +infinity`: termination occurs exactly for `0 < y < E_tot`.

For a finite logarithmic-null pulse, with `y=e^{-lambda u}`, the exact **closing-window law** is

\[
u>u_*,\qquad
u_*=\sigma_a-\frac1\lambda\ln\!\left[
\frac{\mathcal P}{\lambda^4}(1-e^{-\lambda\Delta\sigma})
\right].
\]

Moving the pulse translates the window. Integrated coordinate flux alone does not determine it.

Signed effective sources use `F=C-A_y`, where `C=mu+y^2/2`. A finite first contact exists exactly when some `x>0` has `A_y(x)>=C`. First contact, termination with right-side exclusion, and formal later algebraic roots are explicitly distinguished.

## Start here

| File | Purpose |
|---|---|
| [00-index.md](00-index.md) | Package map, evidence, and links |
| [01-executive-claim.md](01-executive-claim.md) | Main claims and scope |
| [02-source-and-derivation.md](02-source-and-derivation.md) | Primary-source equations and chiral integration |
| [03-sustained-flux-theorem.md](03-sustained-flux-theorem.md) | Sustained theorem and causal structure |
| [06-finite-pulse.md](06-finite-pulse.md) | Exact finite-pulse and mass classification |
| [07-evidence-and-reproduction.md](07-evidence-and-reproduction.md) | Verification, receipts, and portability |
| [11-cumulative-flux-generalization.md](11-cumulative-flux-generalization.md) | Nonnegative measure-valued theorem |
| [12-signed-net-focusing.md](12-signed-net-focusing.md) | Signed sources, contacts, atoms, and multiplicity |
| [14-state-pulse-phase-diagram.md](14-state-pulse-phase-diagram.md) | Exact `p=q` state boundary |
| [15-physical-boundary-injection.md](15-physical-boundary-injection.md) | Finite null injection and closing-window law |
| [16-conformal-matter-realization.md](16-conformal-matter-realization.md) | RST-normalized scalar wavepacket |
| [17-observables-and-universality.md](17-observables-and-universality.md) | Observable limits and structural generalization |
| [18-close-out.md](18-close-out.md) | Completed results and remaining gates |
| [manuscript/ads2-rst-one-sided-flux.tex](manuscript/ads2-rst-one-sided-flux.tex) | Manuscript source |
| [manuscript/ads2-rst-one-sided-flux.pdf](manuscript/ads2-rst-one-sided-flux.pdf) | Compiled manuscript |
| [Archive.zip](Archive.zip) | Complete package archive |
| [Archive.zip.sha256](Archive.zip.sha256) | Archive checksum |

## Reproduction

Python requirements are in [requirements.txt](requirements.txt). The Python battery is offline and package-relative.

```bash
python3 -m pip install -r requirements.txt
bash run_verification.sh
```

To select a compatible interpreter:

```bash
PHYSICS_PYTHON=/path/to/python bash run_verification.sh
```

Optional Lean 4 and LaTeX rebuilds:

```bash
RUN_LEAN=1 bash run_verification.sh
```

Tool discovery uses `lake` and `tectonic` on `PATH`, or explicit `LAKE_BIN` and `TECTONIC_BIN` overrides. The Lean project pins Lean 4.36.0 and Mathlib. Downloaded `lean/.lake/` dependencies are not vendored.

Current expected results:

| Surface | Expected result |
|---|---:|
| Main verification | **138/138 PASS** |
| Separate symbolic checks | **39/39 PASS** |
| Advanced research checks | **32/32 PASS** |
| Package validation | **12/12 PASS** |
| Markdown links | **193 resolved, 0 unresolved** |

The validator also runs a fresh relocated reproduction, compares manifest hashes, and checks source/log/PDF hash receipts instead of filesystem timestamps. `READ_ONLY=1 python3 validate_package.py` validates without rewriting receipts. Producers intentionally regenerate `outputs/`; rerun the validator afterward.

## Primary source and license

The original Kim–Son TeX, figure, and tarball are **not redistributed**. [sources/README.md](sources/README.md) links to the official arXiv abstract, PDF, source, and DOI, records the last verified TeX SHA-256, and explains the license restriction. `sources/source-anchors.txt` retains only the short equation fragments used by the lexical checks.

The arXiv page uses the assumed 1991–2003 non-exclusive distribution license, not a Creative Commons grant. This link-based distribution avoids broader reposting of the paper. Any wider copying of the original source requires author/publisher permission.

## Review and evidence boundaries

- Python checks are symbolic and numerical consistency controls, not hundreds of independent proofs.
- Lean formalizes the algebraic core and abstract continuous first-hit criterion, not the full signed-measure theory or the entire physical model.
- AI reviews are preserved as adversarial history, not counted as independent human peer review.
- The literature search is bounded, not an exhaustive priority claim.
- Apparent horizons are local trapping boundaries, not global event horizons.
- Finite proper-time results concern explicit interior curves, not arbitrary observers.
- Physical boundary-normalized energy, general Hadamard-state admissibility, post-reflection/bath histories, and entropy/island observables remain separate research programs.

## Citation

If using this package, cite the original model first:

> W. T. Kim and E. J. Son, *Wormhole phase in the RST model*, JHEP 0408:006 (2004), arXiv:gr-qc/0404098v2, DOI 10.1088/1126-6708/2004/08/006.

Then cite this repository and the specific commit used. The package status remains **human scientific review pending**.
