---
created: 2026-11-24
type: finite-null-injection
---

# Finite logarithmic-null injection and weighted focusing

The filename is retained for link stability. The completed result is a finite logarithmic-null-coordinate calculation, not yet a boundary-normalized AdS energy theorem.

## 1. Classical transformation and weighted focusing

Let a null coordinate `u` be related to Kruskal `x_p` by an orientation-preserving, strictly increasing map `x_p=f(u)>0` with `f'(u)>0`. Then

$$T_{uu}=[f'(u)]^2T_{++}.$$

The cumulative focusing variable is

$$Q(x)=\frac1{\lambda^2}\int_0^xT_{++}(s)\,ds,$$

not automatically physical injected energy. Once `f` and the boundary trajectory are specified, `Q` is determined. The same transformation gives the useful identity

$$\boxed{E_{\mathrm{focus}}=\frac1{\lambda^2}\int\frac{T_{uu}(u)}{f'(u)}\,du,}$$

because `dx=f'(u)du`. This identity is covariant under reparameterization of `u` when `f` is transformed consistently.

Choose the logarithmic null coordinate `u=sigma`, `x_p=e^{lambda sigma}`. Then

$$T_{\sigma\sigma}=\lambda^2x_p^2T_{++},\qquad E_{\mathrm{focus}}=\frac1{\lambda^3}\int T_{\sigma\sigma}(\sigma)e^{-\lambda\sigma}\,d\sigma.$$

This is the exact **classical tensor** coordinate transformation, not an observer-proper-time claim.

The quantum-state function `t_+` is not assumed to transform as an ordinary weight-two tensor. A renormalized anomalous stress tensor generally acquires a Schwarzian term under conformal reparameterization. The formula above therefore transforms the classical `T_{++}` only; it does not assert a covariant transformation of the full `S_eff=T^f_{++}-kappa t_+`. A boundary-injection model that changes the state frame must derive the `t_+` transformation law, including its Schwarzian contribution, before transforming `Q_eff`.

## 2. Exact finite pulse

Prescribe

$$T_{\sigma\sigma}=\mathcal P\mathbf 1_{[\sigma_a,\sigma_b]},\qquad \sigma_a<\sigma_b.$$

Set

$$a=e^{\lambda\sigma_a},\qquad b=e^{\lambda\sigma_b},\qquad k=\frac{\mathcal P}{\lambda^4},\qquad E=k\left(\frac1a-\frac1b\right).$$

Then

$$T_{++}(x)=\frac{\mathcal P}{\lambda^2x^2}\mathbf 1_{[a,b]},$$

and

$$Q(x)=\begin{cases}
0,&0<x<a,\\
k(1/a-1/x),&a\le x\le b,\\
E,&x\ge b.
\end{cases}$$

On a mixed ray `x_m=-y`, write `C(y)=mu+y^2/2`. Before the pulse,

$$F=C(y)+yx>0,$$

so no hit occurs. During the pulse,

$$\boxed{F(x,y)=C(y)+yx-k\left[\frac{x-a}{a}-\ln\frac xa\right],\qquad a\le x\le b.}$$

Define

$$F_b=C(y)+yb-k\left[\frac{b-a}{a}-\ln\frac ba\right].$$

After the pulse,

$$F(x,y)=F_b+(y-E)(x-b).$$

The three cases are explicit:

1. `F_b<0`: a unique hit occurs during the pulse, since `F(a)=C+ya>0` and concavity gives exactly one root.
2. `F_b=0`: the hit is exactly at shutoff, `x_hit=b`.
3. `F_b>0`: no hit has occurred by shutoff. If `y<E`, the exact post-pulse hit is

$$\boxed{x_{\mathrm{hit}}=b+\frac{F_b}{E-y}>b.}$$

If `y>=E`, no hit exists. The cumulative-flux theorem gives the unified existence criterion `0<y<E`.

The during-pulse concavity `F_{xx}=-T_{++}/\lambda^2<0` proves uniqueness and excludes a second hit.

## 3. Closing-window law in retarded ray time

Define the retarded ray label `u` by

$$x_m=-e^{-\lambda u},\qquad y=e^{-\lambda u}.$$

Then the termination band `0<y<E` becomes

$$\boxed{u>u_*,\qquad u_*=-\frac1\lambda\ln E.}$$

For the constant pulse,

$$E=\frac{\mathcal P}{\lambda^4}e^{-\lambda\sigma_a}\left(1-e^{-\lambda\Delta\sigma}\right),$$

so

$$\boxed{u_*=\sigma_a-\frac1\lambda\ln\!\left[\frac{\mathcal P}{\lambda^4}\left(1-e^{-\lambda\Delta\sigma}\right)\right].}$$

Thus the pulse terminates precisely those outgoing rays emitted after `u_*`. The threshold depends logarithmically on amplitude and duration. Under a pulse translation `sigma_a->sigma_a+delta`, `u_*` shifts by the same `delta`, while `u_*-sigma_a` is invariant.

For `lambda=1`, `mathcal P=1`, and `Delta sigma=1`:

- Early pulse `[-2,-1]`: `E=e^2-e` and `u_*=-2-\ln(e^2-e)`.
- Late pulse `[2,3]`: `E=e^{-2}-e^{-3}` and `u_*=2-\ln(e^{-2}-e^{-3})`.

The same outgoing null ray in the fixed Kruskal chart, `u=0`, satisfies `u>u_*` for the early pulse and `u<u_*` for the late pulse. Thus it is hit by the early pulse and not by the late pulse. The ray has not changed; the pulse has moved relative to it.

## 4. Why energy alone is not a threshold

The integrated incoming `sigma`-coordinate flux is

$$E_{\mathrm{in}}=\int_{\sigma_a}^{\sigma_b}T_{\sigma\sigma}\,d\sigma=\mathcal P\Delta\sigma,$$

whereas

$$\boxed{E_{\mathrm{focus}}=\frac{E_{\mathrm{in}}}{\lambda^4\Delta\sigma}\left(e^{-\lambda\sigma_a}-e^{-\lambda\sigma_b}\right).}$$

For fixed `E_in` and `Delta sigma`,

$$\lim_{\sigma_a\to-\infty}E_{\mathrm{focus}}=+\infty,\qquad \lim_{\sigma_a\to+\infty}E_{\mathrm{focus}}=0.$$

Therefore no critical value `E_crit(mu,y)` depending only on `E_in` can decide whether a fixed ray terminates. This is a corollary of the closing-window law, not a replacement for it. The invariant statement is the ray-time window `u>u_*`; energy alone does not determine that window.

The physical idea is a **redshift-weighted focusing moment**, not an unweighted total energy:

$$\text{incoming energy}\quad\ne\quad\text{cumulative focusing}\quad\ne\quad\text{termination outcome}.$$

## 5. Proper-time and boundary-system limits

- `sigma` and `u` are null coordinates, not the proper time of a timelike boundary observer.
- A physical boundary-energy theorem requires the boundary embedding, induced metric, flux normalization, and an invariant definition of the ray being held fixed.
- The state anomaly must be transformed before moving to a different state frame.
- The theorem classifies the incoming sector before any later boundary reflection or bath response.
- A complete reflecting-boundary or bath-coupled evolution requires additional boundary dynamics.

[Back to index](00-index.md) · [Finite-sigma corollary](12-signed-net-focusing.md#6-finite-logarithmic-null-support-corollary) · [Matter realization](16-conformal-matter-realization.md).
