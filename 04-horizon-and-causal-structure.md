---
created: 2026-11-23
type: apparent-horizon-and-causal-structure
---

# Horizon and causal structure

## 1. Horizon definition used here

Kim-Son defines the apparent-horizon curves formally by `partial_pm Omega=0` at `wormholeRST_jhep.tex:181-188`. This package computes those local trapping loci directly. It does not silently identify them with a complete global event horizon.

## 2. Sustained-flux sector census

| Sector | `partial_p Omega/L` | `partial_m Omega/L` | Horizon content |
|---|---:|---:|---|
| Pre `x_p<0,x_m<0` | `x_p-x_m` | `x_m-x_p` | Static line `x_p=x_m` |
| Mixed `x_p>0,x_m=-y<0` | `y-p x_p` | `-x_p-y<0` | `y=p x_p`, equivalently `x_m=-p x_p` |
| Post `x_p>0,x_m>0` | `-x_m-p x_p<0` | `-x_p<0` | No new zero locus in the interior |
| Other `x_p<0,x_m>0` | `x_p-x_m<0` | `-x_p>0` | No new zero locus in the interior |

At the onset axes, the sector expressions match by `C^1`. The fourth sector has normalized excess `mu+u v+u^2/2>0`, so it hides neither a wall nor an additional horizon branch.

## 3. Horizon precedes every sustained mixed-ray hit

On a fixed `x_m=-y` ray,

$$x_{p,AH}=\frac{y}{p},\qquad x_{p,\mathrm{hit}}=\frac{y+D}{p},\qquad D>0.$$

Thus

$$x_{p,\mathrm{hit}}-x_{p,AH}=\frac{D}{p}>0.$$

The apparent-horizon curve is `x_m=-p x_p`. It is not the same curve as the singular wall. At `mu=0`, for example, the wall is `x_m=-(\sqrt{1+p}-1)x_p`.

This confirms Claude FR-04's inequality and makes **singular termination behind an apparent horizon** the binding geometric description. It does not prove that a specified future-asymptotic exterior observer reaches the edge.

## 4. Explicit interior observers cross the horizon first

In the chart of [Sustained-flux theorem](03-sustained-flux-theorem.md), `R=e^{-2 lambda sigma_0}` decreases as `sigma_0` increases. The mixed apparent horizon is at `R=p`; the wall is at

$$R_w=\sqrt{(1+\mu/K)^2+p}-(1+\mu/K).$$

The wall polynomial is

$$Q(R)=K R^2+2(K+\mu)R-Kp.$$

For `R>0`, `Q` is strictly increasing. Moreover,

$$Q(0)=-Kp<0,\qquad Q(p)=p\left[K(p+1)+2\mu\right]>0,$$

so its positive root obeys `R_w<p`. Therefore every constant-`sigma_1` interior observer crosses the apparent horizon before reaching the wall. These are trapped interior curves, not future-asymptotic exterior observers.

## 5. Finite-pulse horizon continuation

For a pulse with `E=p*x_s`:

- during `0<x_p<x_s`, the apparent horizon is `y=p x_p`;
- after `x_p>x_s`, `partial_p Omega/L=y-E`, so the horizon continues as `y=E`;
- every wall ray has `y<E`, hence `x_{p,AH}=y/p<s=E/p`. It therefore crosses the **during-pulse** horizon before shutoff and before its singular hit;
- `y=E` is the no-wall boundary ray and the post-shutoff horizon. A fixed `y<E` ray does not cross that distinct boundary ray after shutoff.

At `x_s`, the during and after horizon formulas agree. The wall position and first derivative also agree there.

## 6. Impulsive-source horizon comparison

For Kim-Son's impulse with `alpha=A/lambda^2`, the mixed derivative is `partial_p Omega/L=y-alpha`, so the trapping locus is `y=alpha`. The impulsive wall exists only for `0<y<alpha`; those wall rays are already inside the trapped region from onset. This supports the literature-level interpretation of wormhole-to-black-hole evolution and narrows the sustained extension's novelty to its every-ray, parameter-general law.

## 7. Causal scope that remains binding

The exact calculation supplies local trapping geometry and explicit interior proper-time intervals. It does not supply:

- a complete future AdS2 boundary;
- a global event-horizon uniqueness theorem;
- a transparent or reflecting absorber;
- an arbitrary quantum-state completion;
- a full quantum-gravity continuation through `Omega_s`.

“Behind an apparent horizon” is proved. “Every physical observer necessarily hits the singularity” is not claimed.

Next: [State, frame, and novelty](05-state-frame-and-novelty.md).
