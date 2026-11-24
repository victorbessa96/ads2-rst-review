---
created: 2026-11-23
type: primary-source-and-exact-derivation
---

# Primary source and exact derivation

## 1. Source identity and scope

The staged source is Won Tae Kim and Edwin J. Son, **“Wormhole phase in the RST model,” JHEP 0408:006 (2004)**, [arXiv:gr-qc/0404098v2](https://arxiv.org/abs/gr-qc/0404098v2), DOI [10.1088/1126-6708/2004/08/006](https://doi.org/10.1088/1126-6708/2004/08/006).

The full TeX was locally verified as byte-identical to its tar member, with SHA-256 `8906ec46e685404da151c8b7d52a325c4053ee8c8f17964df7264c69baf58872`. The public-facing package retains only short source anchors and official arXiv links rather than redistributing the full paper. See [Source and license](sources/README.md).

| TeX lines | Source content used |
|---|---|
| `96-154` | Action, conformal gauge, `chi/Omega` definitions, constraints, Kruskal gauge `rho=phi` |
| `155-180` | Chiral solution and double-integrated constraints |
| `181-188` | Apparent-horizon definition `partial_pm Omega=0` |
| `209-235` | Positive one-sided impulse and the retained `t_pm` functions |
| `249-258` | Shock-induced black-hole evolution and cloaked singularity |
| `273-310` | Curvature, `Omega'=0`, `Omega_s`, and `M/lambda>0` regularity |
| `311-349` | Static wormhole, weak branch, and `R -> -4 lambda^2` |
| `399-405` | Proper-frame metric convention |
| `461-463` | Past-null-infinity AdS2 identification |

Kim-Son's source is impulsive. The sustained-step and finite-pulse profiles in this package are extensions, not quotations.

## 2. Constraints and chiral integration

In Kruskal gauge,

$$\Omega=-Lx_px_m+a_+(x_p)+a_-(x_m),\qquad L=\frac{\lambda^2}{\sqrt\kappa},$$

and the constraints give

$$a_\pm''=\sqrt\kappa\,t_\pm-\frac{T^f_{\pm\pm}}{\sqrt\kappa}.$$

This is the direct transcription of Kim-Son's `kruskal:cons` equation (TeX lines 163–167) and its integrated form `omegasol` (lines 171–178), including sign and normalization. The lexical source checks are anchors for this equation, not substitutes for reading it.

For the retained state `t_\pm=(\lambda^2/\kappa)\Theta(-x^\pm)` and sustained source `T^f_{++}=P\Theta(x_p)`, integration gives

$$a_+(x_p)=\frac{L}{2}x_p^2\Theta(-x_p)-\frac{P}{2\sqrt\kappa}x_p^2\Theta(x_p),$$

$$a_-(x_m)=\frac{L}{2}x_m^2\Theta(-x_m).$$

Affine integration constants are fixed by the static pre-influx solution and `C^0/C^1` matching. Define

$$\Omega_s=\frac{\sqrt\kappa}{4}\left[1-\log\left(\frac{\kappa}{4}\right)\right],\qquad B=\frac{M}{\lambda}+\Omega_s.$$

Then

$$\boxed{\Omega=B-Lx_px_m+\frac{L}{2}x_p^2\Theta(-x_p)+\frac{L}{2}x_m^2\Theta(-x_m)-\frac{P}{2\sqrt\kappa}x_p^2\Theta(x_p).}$$

| Region | Sector | `Omega` |
|---|---|---|
| Pre | `x_p<0,x_m<0` | `B+(L/2)(x_p-x_m)^2` |
| Mixed | `x_p>0,x_m<0` | `B-Lx_px_m-(P/2sqrt(kappa))x_p^2+(L/2)x_m^2` |
| Post | `x_p>0,x_m>0` | `B-Lx_px_m-(P/2sqrt(kappa))x_p^2` |
| Other | `x_p<0,x_m>0` | `B-Lx_px_m+(L/2)x_p^2` |

Every region satisfies `partial_p partial_m Omega=-L`. Their chiral second derivatives are respectively the retained `t_pm` and matter contributions. At all four onset interfaces, value and both first derivatives match with residuals `(0,0,0)`.

## 3. Physical branch and conformal factor

With

$$\Omega=\frac{e^{-2\phi}}{\sqrt\kappa}+\frac{\sqrt\kappa\,\phi}{2},$$

the minimum obeys

$$\partial_\phi\Omega=0\quad\Longrightarrow\quad e^{-2\phi}=\frac{\kappa}{4},\qquad \Omega=\Omega_s.$$

Thus

$$e^{2\rho}=e^{2\phi}=\frac{4}{\kappa},$$

which is finite and nonzero. Claude FR-09's premise that the conformal factor is singular at the edge is false. The curvature singularity follows from the `Omega'=0` curvature expression, not from a degenerate conformal factor.

The weak branch has `W<=W_{-1}<=-1` and

$$e^{-2\phi}=-\frac{\kappa W}{4}\geq\frac{\kappa}{4},$$

so `0<e^{2rho}<=-4/(kappa W)<=4/kappa`. This bound is used for the null-affine and proper-time finiteness proofs.

For `M>0`, the pre-region excess is strictly positive:

$$\Omega-\Omega_s=\frac{M}{\lambda}+\frac{L}{2}(x_p-x_m)^2>0.$$

At `M=0`, the pre-onset line `x_p=x_m` is already a timelike singularity. The regular wormhole theorem is therefore stated for `mu>0`, with `mu=0` treated as a degenerate limit.

## 4. Impulsive baseline used for novelty control

Replacing the sustained source by `T^f_{++}=A\delta(x_p)` changes the post-onset chiral term to

$$a_+\supset-\frac{A}{\sqrt\kappa}x_p\Theta(x_p).$$

With `alpha=A/lambda^2`, the normalized mixed excess is

$$F_A=\mu+\frac{y^2}{2}+x_p(y-\alpha).$$

This sign is directly fixed by `wormholeRST_jhep.tex:228-235` and `:301-309`. A review subagent's transcription with `y+alpha` was corrected, not propagated.

The resulting impulsive wall band is `0<y<alpha`; the sustained theorem extends this to every `y>0` for every `p>0`. See [State, frame, and novelty](05-state-frame-and-novelty.md).

## 5. Independent derivation status

The derivation above is the source-level worksheet required by Claude FR-06. The producer checks the displayed expressions; it does not replace this integration argument. Exact residuals are exercised by `verify.py` and by the separate `independent_symbolic.py`.

Next: [Sustained-flux theorem](03-sustained-flux-theorem.md).
