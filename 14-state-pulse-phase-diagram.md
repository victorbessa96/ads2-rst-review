---
created: 2026-11-24
type: state-pulse-phase-diagram
---

# State-pulse phase diagram for constant post-onset state data

> [!note] Reading note, 2026-11-24
> The threshold `p = q` is the statement that capture is decided by net null flux, matter plus state ([19](19-global-structure.md), section 6). "Same energy, different outcome" compares different states, and the `q = 0` state already has a black hole at zero flux.

## 1. One state parameter, three exact regimes

Let the post-onset state function be constant in units of the RST anomaly scale:

$$t_+(x)=\frac{q\lambda^2}{\kappa}\qquad(x>0),$$

with `q` real. The classical source remains `T^f_{++}=P>0`, and `p=P/\lambda^2`. Then

$$S_{\mathrm{eff}}=P-q\lambda^2,\qquad Q_{\mathrm{eff}}(x)=(p-q)x.$$

The mixed-ray excess is

$$F(x,y)=\mu+\frac{y^2}{2}+xy-\frac{p-q}{2}x^2.$$

Set `r=p-q`. The exact phase diagram is:

| Regime | Mixed-ray outcome |
|---|---|
| `r>0` | Unique finite positive hit on every `y>0` |
| `r=0` | `F>0` for every finite `x>0`, no mixed-ray hit |
| `r<0` | Every term of `F` is positive, no mixed-ray hit |

For `r>0`, define

$$D_r=\sqrt{(1+r)y^2+2r\mu}.$$

Then the other root is negative and

$$\boxed{x_{\mathrm{hit}}=\frac{y+D_r}{r},\qquad x_{\mathrm{AH}}=\frac yr,\qquad x_{\mathrm{hit}}-x_{\mathrm{AH}}=\frac{D_r}{r}>0.}$$

The wall slope is

$$\frac{dx_m}{dx_p}=-\frac{D_r}{x_{\mathrm{hit}}+y}<0,$$

so the termination is spacelike. The same formulas hold for any real `q`, including negative `q`, provided `r=p-q>0`.

### Proof

For `r>0`, this is the sustained theorem with `p` replaced by `r`. For `r=0`, `F=C(y)+xy>0`. For `r<0`, the quadratic coefficient is positive and all terms are positive. ∎

## 2. Same classical energy, different state outcome

Take the same `P>0`:

- Retained Kim-Son post-onset data `q=0` give `r=p>0`, hence every mixed ray terminates.
- Alternate `t_+`-on data `q=1` give `r=p-1`, hence termination only for `p>1`; for `p<=1`, there is no mixed-ray hit.

Thus the identical classical Kruskal source produces different outcomes solely through the state function. This is an exact same-energy/different-outcome example, not a numerical trend.

The earlier retained-state equivalence is the special case `q=1`: `p_alt=p+1` gives `r_alt=p`, matching the retained `q=0` solution.

## 3. General time-dependent state data

For arbitrary post-onset `t_+(x)`, define

$$R(x)=\frac1{\lambda^2}\int_0^x\kappa t_+(u)\,du,\qquad Q_{\mathrm{eff}}(x)=px-R(x).$$

Then

$$F(x,y)=C(y)+\int_0^x[y-ps+R(s)]\,ds,$$

and the signed accumulated-excess theorem applies with no monotonicity assumption on `R`.

Consequences:

1. A sustained state contribution `q>p` prevents mixed-ray termination.
2. The phase boundary for constant post-onset data is exactly `p=q`.
3. A finite-support state pulse has finite `R(+\infty)`, so sustained classical `P>0` eventually dominates and every finite `y>0` terminates. A finite state pulse can delay termination but cannot prevent it in this sustained classical case.
4. A sustained sign-changing `t_+` can create multiple roots, tangential contacts, and nonmonotonic horizons. No unique-wall or strict-horizon-precedence claim follows without further assumptions.

## 4. State admissibility fence

This is a phase diagram for mathematically admissible post-onset `t_+` data in the fixed chiral solution. It does not prove that every `q(x)` is realized by a physical Hadamard state. Physical state admissibility requires the quantum-state construction and positivity conditions. Hybrid-state literature with wrong-sign fields remains a separate, explicitly labeled comparison.

Both-positive walls are not classified by the mixed-ray phase diagram. They can persist even where the mixed hit is absent.

## 5. Why this matters

The phase boundary is not a universal classical-energy threshold. It is a **net-focusing threshold** `p=q`, set by competition between classical input and the state function. This is the cleanest exact example of the broader signed-net-focusing mechanism.

[Back to index](00-index.md) · [Signed net focusing](12-signed-net-focusing.md) · [Physical boundary injection](15-physical-boundary-injection.md).
