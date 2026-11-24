---
created: 2026-11-23
updated: 2026-11-24
type: cumulative-flux-generalization
---

# General cumulative-flux termination theorem

## 1. Fixed state and general nonnegative source

Retain the Kim-Son state `t_\pm=(\lambda^2/\kappa)\Theta(-x^\pm)` and the same pre-onset matching conventions. The theorem concerns **mixed outgoing rays** `x_m=-y`, `y>0`; it is not a classification of every both-positive wall.

The general source class is a nonnegative Radon measure `dT` on `x_p>=0`, with `T^f_{--}=0`. A nonnegative locally integrable density `T^f_{++}(x_p)` is the special case `dT=T^f_{++}(x_p)dx_p`. This formulation includes the Kim-Son Dirac impulse without pretending that a delta is a locally integrable function.

After onset, the chiral constraint is understood distributionally:

$$a_+''=-\frac{dT}{\sqrt\kappa}.$$

With `a_+(0)=B` and the **pre-onset** derivative condition `a_+'(0^-)=0`,

$$a_+(x)=B-\frac{1}{\sqrt\kappa}\int_{[0,x]}(x-u)\,dT(u).$$

Define the right-continuous, nondecreasing cumulative Kruskal flux

$$Q(x)=\frac{1}{\lambda^2}\int_{[0,x]}dT(u).$$

On the mixed ray `x_m=-y`, the normalized excess becomes

$$\boxed{F(x,y)=\mu+\frac{y^2}{2}+xy-\frac{1}{\lambda^2}\int_{[0,x]}(x-u)\,dT(u).}$$

`F` is continuous and concave. Its one-sided derivatives are

$$D_+F(x)=y-Q(x),\qquad D_-F(x)=y-Q(x^-).$$

For a locally integrable density, `F_x=y-Q` and `F_{xx}=-T^f_{++}/\lambda^2<=0` **almost everywhere**; absolute continuity and monotonicity of `F_x`, not pointwise second differentiability, give the proof. For a general measure, the second derivative statement is distributional.

Also, `F(0,y)=mu+y^2/2>0`.

## 2. Exact termination criterion

Define the total cumulative flux

$$E_{\mathrm{tot}}=\lim_{x\to\infty}Q(x)=\frac{1}{\lambda^2}\int_{[0,\infty)}dT(u),$$

allowing `E_tot=+infinity`.

**Theorem.** With the fixed state and matching conventions above:

1. If `E_tot=+infinity`, every finite `y>0` has a unique finite positive post-onset mixed-ray hit.
2. If `E_tot<+infinity`, a unique finite positive post-onset mixed-ray hit exists exactly for `0<y<E_tot`. For `y>=E_tot`, no hit exists.

### Proof

For `y<E_tot`, eventually `Q(x)>y`, so the right derivative is eventually strictly negative. Concavity then forces `F` to decrease without bound. Since `F` starts positive and is continuous, it has a positive zero. Concavity makes the derivative nonincreasing, so the first zero is unique and `F` remains negative afterward.

For `y>=E_tot`, `Q(x)<=E_tot<=y` for every finite `x>0`, hence both one-sided derivatives are nonnegative wherever defined. `F` is nondecreasing from a positive initial value and never reaches zero.

If `E_tot=+infinity`, every finite `y` is eventually exceeded by `Q(x)`, placing the problem in the first case. ∎

## 3. Correct wall slope and general horizon precursor

At the first root, the right derivative is strictly negative:

$$D_+F(x_{\mathrm{hit}})=y-Q(x_{\mathrm{hit}})<0.$$

Implicit differentiation therefore gives the **right-derivative wall tangent**

$$\boxed{\left.\frac{dx_m}{dx_p}\right|_+=-\frac{Q(x_{\mathrm{hit}})-y}{x_{\mathrm{hit}}+y}<0.}$$

For a smooth density this is the ordinary tangent. For an impulsive source it is the appropriate one-sided tangent at the atom. The wall is spacelike under `ds^2=-e^{2rho}dx_pdx_m`.

### General apparent-horizon corollary

In the mixed region,

$$\frac{\partial_+\Omega}{L}=y-Q(x).$$

For a continuous cumulative profile, the apparent horizon on the ray is the level set `Q(x_AH)=y`. At the first wall hit, `Q(x_hit)>y`, so `x_AH<x_hit`: the horizon precedes the singular termination for the entire locally integrable source class.

For a general measure, define the first level crossing `x_AH=inf{x:Q(x)>=y}` and call it a **generalized trapping-boundary level crossing**, not automatically a smooth apparent horizon. The same strict ordering holds. If the first root were reached with `Q(x_hit^-)<=y`, the left derivative there would be nonnegative; concavity would then make `F` nondecreasing up to the root, incompatible with descending from `F(0,y)>0` to its first zero. Hence `Q(x_hit^-)>y`, and the first level crossing is strictly earlier.

## 4. Special cases recovered exactly

| Source profile | `Q(x)` | Total flux | Termination band |
|---|---|---:|---|
| Sustained constant density `T^f_{++}=P` | `px` | Infinite | Every finite `y>0` |
| Rectangular pulse on `0<x<s` | `p min(x,s)` | `E=ps` | `0<y<E` |
| Kim-Son impulse `A delta(x)` as a measure | `alpha=A/lambda^2` for `x>0` | `alpha` | `0<y<alpha` |

The impulsive case therefore matches the previously derived spacelike wall band, rather than the incorrect no-mixed-wall transcription.

## 5. What this does and does not mean

The result classifies mixed-ray termination by cumulative flux, not by coordinate-independent physical energy. `Q(x)` is a Kruskal-coordinate tensor moment. It is not an observer-normalized integrated power.

- Sustained `P>0` has no finite ceiling because `Q(x)=px` diverges.
- A finite Kruskal-support source has finite `E_tot` and only a bounded ray band terminates.
- Finite support in the logarithmic null coordinate `sigma` is already covered by the measure theorem; see [Signed net focusing and finite-sigma pulses](12-signed-net-focusing.md). This is not automatically finite proper time for a timelike observer.
- Changing `t_\pm` can change the conclusion. The theorem fixes the Kim-Son state.
- No future-asymptotic absorber or arbitrary-state completion follows.
- The Lean artifact currently formalizes selected algebraic cores, not this measure-theoretic theorem.

This generalization unifies the sustained, rectangular-pulse, and impulsive calculations into one theorem without enlarging the physical claim fence.

[Back to index](00-index.md) · [Sustained theorem](03-sustained-flux-theorem.md) · [Finite-pulse theorem](06-finite-pulse.md).
