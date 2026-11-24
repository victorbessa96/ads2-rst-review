---
created: 2026-11-22
updated: 2026-11-22
type: frontier-analysis
tags: [frontier, physics, wall-mechanism, collector, rst, ads2, one-sided-flux, wormhole, computation, verification, origin]
spark: spark_20261110_154351_a10e80
parent_spark: spark_20261102_014500_wallcensus1
related:
  - "[[2026-11-10-collector-pileup-flat-rst-test]]"
  - "[[2026-11-22-timelike-collector-wall-test]]"
  - "[[2026-11-02-ads2-wall-mechanism-census]]"
papers:
  - "Kim and Son, gr-qc/0404098v2, Wormhole phase in the RST model"
assets: "frontier/assets/2026-11-22-ads2-rst-one-sided-flux/"
status: answered-with-scope — exact constant-flux solution forms a spacelike Omega-minimum singularity on specified outgoing null rays in the past-AdS2 Kim-Son branch
---

# Past-AdS2 Kim-Son RST under constant one-sided flux: spacelike singular edges on outgoing null rays

## Scoped question and model identification

The target is not pure JT. The explicit primary-source realization used here is Kim-Son's RST wormhole branch (`gr-qc/0404098v2`). Its running `Omega` has the usual RST minimum, its pre-influx static wormhole is asymptotically AdS2 with `R -> -4 lambda^2` (`wormholeRST_jhep.tex:281-299,311-349`), and its boundary functions are `t_pm=(lambda^2/kappa)Theta(x0-x_pm)` (`:220-235`). A constant-dilaton AdS2 CGHS/RST solution would not answer this spark because it lacks the running Omega edge.

The question is whether sustained incoming-only classical positive flux on this past-AdS2 RST branch is absorbed while every wall stays depletion-type, or creates a spacelike Omega-minimum edge.

## Exact result: finite-xp null-ray termination at a spacelike singularity

Set `x0=0` by chiral translations and define

```text
Omega_s = sqrt(kappa)/4 * [1-log(kappa/4)],
L = lambda^2/sqrt(kappa),
p = P/lambda^2,
mu = sqrt(kappa) M/lambda^3.
```

For constant `T^f_++=P>0` after `xp=0`, `T^f_--=0`, with Kim-Son's `t_pm` retained, the mixed region `xp>0, xm<0` has

```text
Omega = M/lambda + Omega_s - L xp xm - P xp^2/(2 sqrt(kappa)) + L xm^2/2.
```

This follows by integrating the paper's chiral constraint twice; it is not an ad hoc metric ansatz. The wall `Omega=Omega_s` is therefore, with `y=-xm>0`,

```text
F(xp,y) = mu + y^2/2 + xp y - p xp^2/2 = 0,
xp_hit(y) = [y + sqrt((1+p)y^2 + 2p mu)]/p.
```

For every `p>0`, `mu>=0`, and `y>0`, this is the unique positive first hit: `F>0` before it and `F<0` after it. Its causal tangent is

```text
dxm/dxp = -sqrt((1+p)y^2 + 2p mu)/(xp_hit+y) < 0.
```

In the conformal metric `ds^2=-exp(2rho)dxp dxm`, negative slope means a spacelike curve. Thus, for each fixed finite `y>0`, the outgoing null ray `xm=-y` first reaches the RST minimum at finite Kruskal coordinate `xp_hit`; the singular edge has spacelike tangent and the regular physical domain terminates there. Within this fixed solution, no regular wall-free continuation exists along these rays. Absorption, reflection, transmission, and coupled absorber dynamics are not computed.

`Finite` here means finite `xp` per specified ray, not finite proper time, finite affine parameter, a compact wall, or a uniform bound: `xp_hit` diverges as `p->0` and as `y->infinity`.

In the degenerate `M=0` singular limit, the pre-onset singular line is `xp=xm` with positive slope, hence timelike, while the mixed-region post-onset singular branch is exactly

```text
xm_wall = -(sqrt(1+p)-1) xp.
```

So the pre-onset timelike singular line is followed by a spacelike singular branch after onset. This is not a regular wormhole or collector edge. As `p->0`, the fixed-`xm` hit retreats to `xp->+infinity`; the zero-flux control has no positive mixed-region wall.

For `mu>0`, the both-positive region `xp,xm>0` has the wall branch `xm=mu/xp-p xp/2`, also spacelike. It meets the mixed-region branch at `xm=0`, `xp=sqrt(2mu/p)`, with common slope `-p`.

## Scope already binding

- This proves a model-internal Omega-minimum singularity in Kim-Son's past-asymptotically-AdS2 RST branch. It does not prove that every conceivable definition of "AdS2-RST" piles up.
- The constant-P solution is a new exact extension of Kim-Son's impulsive-source branch for the retained `t_pm` and C1 matching. It is not a unique physical response under arbitrary quantum-state or future-boundary data.
- Constant sustained flux is the exact case solved here. A finite pulse, a transparent or reflecting future AdS2 boundary, and a physical absorber action are separate boundary-value problems. No such future boundary is constructed, and absorption in that separate problem is neither modeled nor excluded.
- The hit is established on fixed-`xm` outgoing null rays. A future asymptotic timelike-observer clock is not constructed, so "observer-hittable" is not promoted beyond finite-xp null-ray termination and spacelike singularity.
- The fourth coordinate sector `xp<0,xm>0` has normalized excess `mu-xp*xm+xp^2/2>0`, so no wall is overlooked there. All four sectors match C0/C1 across the onset axes.
- The older flat-space `|dxm/dxp|>1` classifier is not used. The correct Kruskal-conformal rule is negative slope = spacelike, positive slope = timelike, as independently repaired in [[2026-11-22-timelike-collector-wall-test]].

## Verification: 88/88 PASS

Durable producer: `frontier/assets/2026-11-22-ads2-rst-one-sided-flux/ads2_rst_flux_verify.py`, run with `~/.venvs/physics/bin/python`. Primary source is staged in `sources/`; structured output is `verification-summary.json`; full output is `ads2_rst_flux_out.txt` and `final-console.out`.

Final observed result: **88/88 PASS, exit 0**, with mpmath at 90 dps and exact SymPy algebra. The battery checks source equations, all four region-wise constraints, C0/C1 matching at every coordinate-sign interface, exact first-hit roots, physical-side exclusion, general-p/general-mu causal sign, the `M=0` mixed-region post-onset branch, fourth-sector exclusion, zero-flux retreat, and the asymptotic AdS2 curvature control.

The first run was **77/83**, preserved as `red-first.out` and `red-first-summary.json`. Three assertions had incorrect source-line targets. Three curvature checks incorrectly demanded an asymptotic limit already at finite `S`; the replacement tests the full convergent sequence. A second run at **79/80** exposed that the convergence sequence needed one further decade, not a physics change. Final curvature residuals `|R+4|` for `lambda=1` at `S=1,10,100,1000,10000,100000` are `1.60061, 0.663636, 0.151041, 0.0243565, 0.00336032, 0.000428224`, monotonically approaching zero. No failing physics check was deleted.

Illustrative exact-root rows in the `M=0` mixed-region post-onset branch:

| `p=P/lambda^2` | `y=-xm` | `xp_hit` | `dxm/dxp` | causal verdict |
|---|---|---|---|---|
| 0.01 | 1 | 200.4987562112089 | -0.00498756211209 | spacelike |
| 0.1 | 1 | 20.48808848170152 | -0.04880884817020 | spacelike |
| 1 | 1 | 2.414213562373095 | -0.41421356237310 | spacelike |
| 100 | 1 | 0.110498756211209 | -9.04987562112089 | spacelike |

## Independent reviews and strengthened close-out

Two fresh-eyes reviews (`deleg_58ea3d2e`) independently re-derived the result. The mathematical review upheld all coefficients, roots, branch matches, and metric signs, and supplied the fourth-sector exclusion. The model-scope review required the past-AdS2, degenerate-M=0, finite-xp, and no-absorber-theorem qualifications now binding above. Full summaries: `independent-math-review.md` and `independent-scope-review.md` in the assets directory.

Their producer caveats were converted into regression checks. The review-strengthened run briefly read **87/88** because SymPy did not infer `sqrt(1+p)>1` from `p>0`; substituting the equivalent positive variable `q=sqrt(1+p)-1` made the sign proof explicit. Final **88/88** includes that general-p causal check, all four sectors, and C0/C1 matching at every interface.

## Asserting reproduction fence

```python
# spark_20261110_154351_a10e80
from pathlib import Path
import subprocess
p = Path('/home/bessa/Documents/Obsidian Vault/frontier/assets/2026-11-22-ads2-rst-one-sided-flux/ads2_rst_flux_verify.py')
r = subprocess.run(['/home/bessa/.venvs/physics/bin/python', str(p)], capture_output=True, text=True, timeout=240)
out = r.stdout + r.stderr
assert r.returncode == 0, out[-5000:]
assert 'SUMMARY: 88/88 checks PASS' in out, out[-5000:]
assert 'FAIL |' not in out, out[-5000:]
print('88/88 PASS: past-AdS2 Kim-Son constant-flux singular-edge battery')
```

## ADDITIVE DELTA — 2026-11-23 formal review package

The structured, linked review package is indexed at [[frontier/assets/2026-11-22-ads2-rst-one-sided-flux/formal-review/00-index|AdS2-RST one-sided-flux formal review]]. It separates the scoped theorem, evidence and reproduction record, formal sign-off protocol, and a second-session verification pass. Package validation does not constitute external scientific peer review.
