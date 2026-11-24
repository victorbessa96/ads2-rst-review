---
created: 2026-11-23
type: finite-pulse-shutoff-theorem
---

# Complete finite-pulse shutoff theorem

**Terminology:** finite pulse means **finite Kruskal support**, not finite duration in an observer-adapted time coordinate. If `x_p=e^{lambda sigma}`, the interval `0<x_p<s` is `-infinity<sigma<ln(s)/lambda`.

## 1. Exact source and chiral solution

Let `s=x_s>0` and prescribe

$$T^f_{++}=P\left[\Theta(x_p)-\Theta(x_p-x_s)\right],\qquad T^f_{--}=0,$$

while retaining the Kim-Son `t_pm`. With `C^1` matching at `0` and `s`,

$$a_+(x)=
\begin{cases}
(L/2)x^2, & x<0,\\[2pt]
-(P/2\sqrt\kappa)x^2, & 0<x<s,\\[2pt]
-(Ps/\sqrt\kappa)(x-s/2), & x>s,
\end{cases}
\qquad a_-(x_m)=\frac{L}{2}x_m^2\Theta(-x_m).$$

Thus `Omega=B-Lx_px_m+a_+(x_p)+a_-(x_m)` is fully specified. Define the integrated dimensionless pulse strength

$$E=p\,s,\qquad p=P/\lambda^2.$$

In the mixed region `x_m=-y`, the normalized excess is

$$F(x,y)=
\begin{cases}
F_d=\mu+y^2/2+xy-p x^2/2, & 0<x<s,\\[2pt]
F_a=\mu+y^2/2+E s/2+x(y-E), & x>s.
\end{cases}$$

At `x=s`, `F_d=F_a` and `partial_x F_d=partial_x F_a` after substituting `E=ps`.

## 2. Exact existence criterion

The complete result is:

$$\boxed{\text{a unique positive post-onset wall hit exists exactly for }0<y<E.}$$

“First” means first positive post-onset hit. When `mu=0`, the pre-onset geometry is already singular, so this is not a claim of first singularity formation in the global spacetime.

For `y>=E`, no wall exists.

During the pulse, the sustained root applies:

$$x_{p,d}=\frac{y+\sqrt{(1+p)y^2+2p\mu}}{p}.$$

Define

$$y_{\max}=\sqrt{(1+p)s^2-2\mu}-s.$$

Then `0<y<y_max` gives `x_{p,d}<s`, with `y=y_max` giving the hit exactly at shutoff. If `y>y_max` and `y<E`, the hit occurs after shutoff at

$$\boxed{x_{p,a}=\frac{\mu+y^2/2+E s/2}{E-y}>s.}$$

At `y=y_max`, `x_{p,a}=s`. The exact identity

$$x_{p,a}-s=\frac{F_d(s)}{E-y}$$

separates pre-shutoff, equality, and post-shutoff hits. If the `y_max` radicand is negative, the during-hit set is empty, but the linear post-shutoff branch can still produce hits for `0<y<E`.

Necessity follows because a pre-shutoff hit requires `y<y_max<E`, while the post-shutoff linear equation can cross from positive to negative only for `y<E`. This closes the finite-pulse existence question, not merely its pre-shutoff subset.

## 3. Causal character through shutoff

During the pulse, the wall has the sustained negative tangent and is spacelike. After shutoff,

$$\frac{dx_m}{dx_p}=\frac{y-E}{x_{p,a}+y}<0\qquad(y<E),$$

so it remains spacelike. At `y=y_max`, the wall reaches `x=s`, and the during and after tangents agree. The both-positive branch also matches in position and first derivative.

For `mu>0`, the both-positive wall is

$$x_m=
\begin{cases}
\mu/x_p-p x_p/2, & 0<x_p<s,\\[2pt]
(\mu+E s/2)/x_p-E, & x_p>s.
\end{cases}$$

The formulas are valid only where they actually lie in `x_m>0`:

- during: `0<x_p<min(s,sqrt(2mu/p))`;
- after: `s<x_p<s/2+mu/E`, with the interval existing only when `mu>E s/2`.

For the after interval, write `x_0=s/2+mu/E`. Then `x_m=E(x_0/x_p-1)`, so `x_m>0` exactly when `x_p<x_0`; combining this with `x_p>s` gives the stated bounded interval. If `x_0<=s`, no both-positive wall segment exists after shutoff. For example, `p=1, mu=10, s=3` gives `x_0=29/6`, with `x_m(4)=5/8>0` and `x_m(5)=-1/10<0`. If `sqrt(2mu/p)<s`, the during formula crosses `x_m=0` before shutoff and the mixed formula applies afterward. At either crossing, `x_m=0` and the mixed branch applies. The wall is spacelike wherever these domains hold, and position and slope match at every crossing.

### Exact mass classification corollary

The during and after conditions are complementary. Since

$$y_{\max}>0\iff \mu<\frac{Es}{2},\qquad x_0-s=\frac{2\mu-Es}{2E},$$

the exact classification is:

| Mass parameter | Mixed-ray termination | Both-positive after-shutoff branch |
|---|---|---|
| `mu<Es/2` | `0<y<y_max` during; `y_max<y<E` after; equality at shutoff | Absent because `x_0<s` |
| `mu=Es/2` | `y_max=0`, so all mixed-ray hits in `0<y<E` occur after shutoff | Degenerates to the boundary `x_p=s` |
| `mu>Es/2` | `y_max<=0` or nonreal, so all mixed-ray hits in `0<y<E` occur after shutoff | Present on `s<x_p<x_0` |

This also makes the nonpositive-or-nonreal-`y_max` convention explicit: in that case there is no during-pulse hit, and every ray with `0<y<E` hits afterward. The exact interval invariant `x_0-s=(2mu-Es)/(2E)` is tested in both producers.

## 4. Apparent horizon and trapped wall rays

During the pulse, `partial_p Omega/L=y-p x_p`, so `y=p x_p` is the apparent horizon. After shutoff, `partial_p Omega/L=y-E`, so the horizon continues as `y=E`.

Every wall ray has `y<E`, hence `x_{p,AH}=y/p<s=E/p`, so it crosses the during-pulse horizon before shutoff and before its singular hit. The distinct boundary ray `y=E` has no wall and is itself the post-shutoff horizon; a fixed `y<E` ray does not cross that later boundary.

## 5. Degeneracies and limits

- **`y=y_max`:** wall exactly at shutoff, with continuous position and tangent.
- **`y=E`:** no wall; this is the post-shutoff apparent-horizon ray.
- **`mu=0`:** `y_max=(sqrt(1+p)-1)s`, and the both-positive branch is absent; the pre-onset geometry is already singular.
- **`p->0`:** `E->0`, so the wall ray band collapses; `x_{p,d}` retreats nonuniformly as in the sustained control.
- **`s->infinity`:** `E->infinity`, recovering the sustained every-ray result.
- **Finite input:** `integral_0^s P dx_p=Ps=lambda^2E` is finite in Kruskal `x_p`. No observer-frame energy invariant is claimed.

## 6. Executed existence census

| `p` | `mu` | `s` | `y/E` | First hit | Branch |
|---:|---:|---:|---:|---:|---|
| 1 | 0 | 2 | 0.25 | 1.207106781186548 | During |
| 1 | 0 | 2 | 0.75 | 6.25 | After |
| 1 | 0 | 2 | 1.00 | None | No wall |
| 1 | 0 | 2 | 1.25 | None | No wall |
| 0.2 | 0.5 | 3 | 0.25 | 3.136111111111111 | After |
| 0.2 | 0.5 | 3 | 0.75 | 10.00833333333333 | After |
| 0.2 | 0.5 | 3 | 1.00 | None | No wall |
| 0.2 | 0.5 | 3 | 1.25 | None | No wall |
| 2 | 1 | 1.5 | 0.25 | 1.569444444444444 | After |
| 2 | 1 | 1.5 | 0.75 | 7.708333333333333 | After |
| 2 | 1 | 1.5 | 1.00 | None | No wall |
| 2 | 1 | 1.5 | 1.25 | None | No wall |

Explicit review-regression rows also pass:

| Case | Result |
|---|---|
| `p=1, mu=10, s=1, y=1/2` | `y_max` radicand `-18<0`, no during hit; exact after hit `x_a=85/4>1` |
| `p=1, mu=1/5, s=2, y=y_max` | `x_d=x_a=s=2`, equality handled separately |
| `p=1, mu=2, s=3` | `x_0=13/6<3`; no after-shutoff both-positive segment exists |
| `p=1, mu=10, s=3` | `x_0=29/6`; after segment `3<x_p<29/6`, with `x_m(4)=5/8>0` and `x_m(5)=-1/10<0` |

The numerical rows reproduce the exact `0<y<E` criterion. They are controls, not the proof.

Next: [Evidence and reproduction](07-evidence-and-reproduction.md).
