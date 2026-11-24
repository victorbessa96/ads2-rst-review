---
created: 2026-11-23
type: sustained-flux-theorem-and-observer-clocks
---

# Sustained-flux theorem and explicit clocks

## 1. Unique positive post-onset hit

Set

$$p=\frac{P}{\lambda^2}>0,\qquad \mu=\frac{\sqrt\kappa M}{\lambda^3}\geq0,\qquad y=-x_m>0.$$

Multiplying the mixed-region excess by `sqrt(kappa)/lambda^2` gives

$$F(x_p,y)=\mu+\frac{y^2}{2}+x_py-\frac{p}{2}x_p^2.$$

Define

$$D=\sqrt{(1+p)y^2+2p\mu}.$$

Since `D^2-y^2=p(y^2+2mu)>0`, `D>y`. The two roots are `(y +/- D)/p`; the minus root is negative by the rationalized identity

$$\frac{y-D}{p}=-\frac{y^2+2\mu}{y+D}<0.$$

Thus the unique positive root is

$$\boxed{x_{p,\mathrm{hit}}=\frac{y+D}{p}}.$$

At onset `F(0,y)=mu+y^2/2>0`, while `F -> -infinity` as `x_p -> +infinity`. With only one positive root, `F>0` before the hit and `F<0` after it. This proves first positive post-onset-hit ordering and physical-side exclusion for every allowed parameter set. When `mu=0`, “first” does not mean first singularity formation globally, because the pre-onset line is already singular.

## 2. Spacelike edge and global representation

Implicit differentiation gives

$$F_{x_p}=y-px_{p,\mathrm{hit}}=-D,\qquad F_y=x_{p,\mathrm{hit}}+y,$$

so

$$\boxed{\frac{dx_m}{dx_p}=-\frac{D}{x_{p,\mathrm{hit}}+y}<0.}$$

Because `ds^2=-e^{2rho}dx_pdx_m`, the induced wall norm is positive: the edge is spacelike. The conformal factor at the wall is finite and equals `4/kappa`.

The equivalent mixed-wall representation is

$$\boxed{x_m^{\mathrm{wall}}(x_p)=x_p-\sqrt{(1+p)x_p^2-2\mu}},\qquad x_p\geq\sqrt{\frac{2\mu}{p}}.$$

At large `x_p`,

$$x_m^{\mathrm{wall}}\sim-(\sqrt{1+p}-1)x_p.$$

For `mu=0`, this becomes the exact line `x_m=-(\sqrt{1+p}-1)x_p`. For `mu>0`, the both-positive branch is `x_m=mu/x_p-p x_p/2`, valid for `0<x_p<sqrt(2mu/p)`. Position and slope match the mixed branch at `x_p=sqrt(2mu/p)`.

The zero-flux control has `F=mu+x_py+y^2/2>0`, with no positive mixed wall. For fixed `mu,y`, `x_hit~2y/p` as `p->0^+`; there is no uniform bound over arbitrarily small positive flux.

## 3. Apparent-horizon ordering

In the mixed region,

$$\partial_p\Omega=L(y-px_p),$$

so the apparent horizon on each fixed ray is `x_{p,AH}=y/p`. Since

$$x_{p,\mathrm{hit}}-x_{p,AH}=\frac{D}{p}>0,$$

the ray crosses the apparent horizon before it reaches the singular edge. The leading description is therefore **spacelike singular termination behind an apparent horizon**. See [Horizon and causal structure](04-horizon-and-causal-structure.md).

## 4. Finite forward null affine parameter

For a fixed-`x_m` null geodesic,

$$\frac{d^2x_p}{d\ell^2}+2\partial_p\rho\left(\frac{dx_p}{d\ell}\right)^2=0,$$

hence

$$\frac{dx_p}{d\ell}=C e^{-2\rho},\qquad d\ell=\frac{e^{2\rho}}{C}dx_p.$$

On the weak branch, `0<e^{2rho}<=4/kappa`. Therefore, from any finite earlier `x_i`,

$$\ell_{\mathrm{hit}}-\ell_i=\frac1C\int_{x_i}^{x_{\mathrm{hit}}}e^{2\rho(x,-y)}dx
\leq\frac{4(x_{\mathrm{hit}}-x_i)}{C\kappa}<\infty.$$

This strengthens the original finite-`x_p` statement to finite forward affine parameter. It does not assign a nonzero proper time to a null ray, and it does not supply a uniform bound over rays or as `p->0`.

## 5. Explicit interior timelike observers

Use the interior chart

$$x_p=e^{\lambda(\sigma_0+\sigma_1)},\qquad x_m=-e^{-\lambda(\sigma_0-\sigma_1)}.$$

Then

$$ds^2=-\lambda^2K e^{2\rho}\left[(d\sigma_0)^2-(d\sigma_1)^2\right],
\qquad K=e^{2\lambda\sigma_1}>0,$$

so constant-`sigma_1` curves are timelike, with

$$d\tau=\lambda\sqrt K\,e^\rho\,d\sigma_0.$$

These are boost-hyperbola, generally accelerated **interior** observers, not future-asymptotic boundary observers. They also lie inside the trapped region before the hit. The finite proper-time result is an explicit consistency control for this family, not a theorem for all inextendible future-directed timelike geodesics.

Define

$$R=-\frac{x_m}{x_p}=e^{-2\lambda\sigma_0}.$$

Along constant `K`, the wall condition reduces to

$$K R^2+2(K+\mu)R-Kp=0,$$

whose positive root is

$$\boxed{R_w=\sqrt{\left(1+\frac{\mu}{K}\right)^2+p}-\left(1+\frac{\mu}{K}\right)}.$$

Thus

$$\boxed{\sigma_{0,w}=-\frac{\ln R_w}{2\lambda}}$$

is finite for every finite `K>0`. The proper-time integral from any finite earlier `sigma_{0,*}` is finite because the integrand is continuous and bounded on that closed interval:

$$\tau_w-\tau_*=\lambda\sqrt K\int_{\sigma_{0,*}}^{\sigma_{0,w}}e^\rho d\sigma_0
\leq\frac{2\lambda\sqrt K}{\sqrt\kappa}(\sigma_{0,w}-\sigma_{0,*})<\infty.$$

For `mu=0`, `R_w=sqrt(1+p)-1`, matching the global straight wall. For `mu>0`, `R_w` is smaller and still positive. No future-asymptotic boundary or boundary clock is inferred.

### Executed observer controls

| `sigma_1` | `sigma_0` at wall | Proper time from `sigma_0=-2` |
|---:|---:|---:|
| -1 | 1.4118043725926659663 | 0.90085319827996572666 |
| 0 | 0.72181773758940517125 | 1.3360038212268260491 |
| 1 | 0.48695421853797283617 | 1.599113461833509751 |

All three wall residuals have absolute value below `1e-89`, and all three proper-time quadratures are finite.

## 6. Coordinate meaning of the source

The source is constant only in the chosen Kruskal coordinate. If `x_p=e^{lambda sigma}`, then

$$T^f_{\sigma\sigma}=\left(\frac{dx_p}{d\sigma}\right)^2P=\lambda^2x_p^2P.$$

The integrated coordinate stress up to `x_p` is

$$\int T^f_{\sigma\sigma}\,d\sigma=\frac{\lambda P x_p^2}{2},$$

which scales as `2 lambda^3 y^2/p` at the small-`p` hit `x_hit~2y/p`. This is a tensor-component transformation and scaling control, not a complete observer-energy theorem. It makes the physical interpretation of “sustained constant flux” explicitly frame-dependent without changing the fixed-model algebra.

Next: [Horizon and causal structure](04-horizon-and-causal-structure.md).
