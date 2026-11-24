# Independent mathematical review

Review handle: `deleg_58ea3d2e`, task 0 (`sa-0-4fed028f`). Fresh-eyes subagent, no file edits. The reviewer independently re-derived the load-bearing equations rather than relying on the parent's 80/80 battery.

## Verdict

PASS. The sustained-flux coefficients, normalization, first-hit root, branch matching, M=0 line, and causal classifications are correct. No normalization, branch, or metric-sign correction is required.

From `a_pm''=sqrt(kappa)t_pm-T^f_pm/sqrt(kappa)` and `t_pm=(lambda^2/kappa)Theta(-x_pm)`, with constant `T^f_++=P` after onset and `T^f_--=0`, double integration gives

```text
Omega = B - L xp xm + (L/2)xp^2 Theta(-xp)
        + (L/2)xm^2 Theta(-xm) - (P/(2 sqrt(kappa)))xp^2 Theta(xp),
B = M/lambda + Omega_s, L=lambda^2/sqrt(kappa).
```

The reviewer also checked all four coordinate-sign sectors and C0/C1 matching across both onset axes. The fourth sector `xp<0,xm>0` has normalized excess `mu-xp*xm+xp^2/2>0`, so it contains no overlooked wall.

Multiplying `Omega-Omega_s` by `sqrt(kappa)/lambda^2` gives exactly `p=P/lambda^2` and `mu=sqrt(kappa)M/lambda^3`. For `y=-xm>0`, the normalized wall function is `G=mu+y^2/2+xp y-p xp^2/2`. Since `D=sqrt((1+p)y^2+2p mu)>y`, only `(y+D)/p` is positive; `G_x=-D<0` there, proving the physical-before/excluded-after verdict. Implicit differentiation gives `dxm/dxp=-D/(xp_hit+y)<0`, hence `ds^2=-exp(2rho)dxp dxm>0` along the wall: spacelike.

## Producer caveats handed back to the parent

- The 80/80 battery is consistency checking, not an independent derivation: its Omega expressions are entered as ansatze and its source checks are substring checks.
- The general tangent check substituted `mu=0`; the pre-onset timelike check was hard-coded; the post-onset line check tested only `p=1`. The independent symbolic identities close those gaps, and the parent is adding explicit regression checks.
- Use `M=0 mixed-region post-onset branch`, not an unqualified `global line`; the pre-onset `xp=xm` branch is separate.

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
print('88/88 PASS: independently reviewed Kim-Son algebra and causal signs')
```
