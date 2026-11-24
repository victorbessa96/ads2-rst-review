---
created: 2026-11-23
type: state-sensitivity-frame-and-novelty
---

# State, frame, impulsive comparison, and novelty

## 1. Alternate state data: the mixed-ray threshold is real but scoped

Claude FR-01 asks what happens if `t_+` remains on after onset. Then

$$a_+''=\frac{\lambda^2-P}{\sqrt\kappa},$$

and the normalized mixed excess becomes

$$F_{\mathrm{alt}}=\mu+\frac{y^2}{2}+x_py+\frac{1-p}{2}x_p^2.$$

For `0<p<1`, every term is positive. At `p=1`, it reduces to `mu+x_py+y^2/2>0`. Thus there is no mixed-ray hit for `p<=1`. For `p>1`, the downward quadratic has the unique positive hit

$$x_{p,\mathrm{alt}}=\frac{y+\sqrt{p y^2+2(p-1)\mu}}{p-1}.$$

This is an explicit state-sensitivity result. It does not contradict the retained Kim-Son state used in the main theorem, whose `t_+` steps off at `x_0` by the paper's past-wormhole and no-radiation conditions (`wormholeRST_jhep.tex:214-225`).

### Exact retained-state equivalence

Set `p_eff=1+p`. Then the alternate coefficient is

$$\frac{1-p_{\mathrm{eff}}}{2}=-\frac p2,$$

exactly the retained-state coefficient. The retained step-off therefore supplies the critical `lambda^2` in this comparison, and every `p>0` corresponds to `p_eff>1`. “No critical amplitude” is a state-specific Kruskal-profile statement, not a universal physical threshold claim.

### Not an all-wall elimination theorem

For alternate data with `p=1`, the both-positive excess is `mu-x_px_m`, so `x_m=mu/x_p` remains a wall for `mu>0`. For `0<p<1`, the both-positive quadratic can have real roots when `x_m^2>=2mu(1-p)`. Therefore the correct statement is only that the **mixed outgoing-ray hit** is absent for `p<=1`, not that every singular wall disappears.

## 2. Kruskal-constant flux is a profile choice

The main source is constant in `x_p`. In a natural exponential null coordinate `x_p=e^{lambda sigma}`,

$$T^f_{\sigma\sigma}=\lambda^2x_p^2P.$$

So the same source grows as a tensor component in that coordinate. The integrated coordinate stress up to `x_p` is

$$\int T^f_{\sigma\sigma}\,d\sigma=\frac{\lambda P x_p^2}{2}.$$

For small `p`, `x_hit~2y/p`, giving `2 lambda^3 y^2/p` at the hit. This explains why the absence of a critical-flux threshold cannot be transferred naively to an observer-frame energy statement. The coordinate transformation and scaling are exact; a complete physical energy budget for a designated observer remains a separate problem.

## 3. Impulsive Kim-Son already has a spacelike wall band

With `alpha=A/lambda^2`, the impulsive mixed excess is

$$F_A=\mu+\frac{y^2}{2}+x_p(y-\alpha).$$

For `0<y<alpha`, the unique positive hit is

$$x_{p,A}=\frac{\mu+y^2/2}{\alpha-y},$$

with

$$\frac{dx_m}{dx_p}=-\frac{\alpha-y}{x_p+y}<0,$$

so the edge is spacelike. For `y>=alpha`, there is no mixed hit.

For `mu>0`, the complete post-onset impulsive singular curve is

$$x_{m,A}(x_p)=
\begin{cases}
\mu/x_p-\alpha, & 0<x_p\leq\mu/\alpha,\\[2pt]
x_p-\sqrt{x_p^2+2\alpha x_p-2\mu}, & x_p\geq\mu/\alpha.
\end{cases}$$

At `x_p=mu/alpha`, the branches satisfy `x_m=0` and have common slope `-alpha^2/mu`. The second branch approaches `x_m->-alpha` as `x_p->infinity`; every finite point is spacelike, with asymptotically null limiting tangent.

**Novelty verdict:** the broad existence of an AdS2-RST singular wall is not new. The distinct result is the sustained theorem's unique finite termination on **every** mixed ray `y>0` for **every** `p>0`, its exact first-hit law, and its finite-pulse completion.

## 4. Bounded literature finding

A fresh primary-literature pass inspected thirteen full-text documents, including Kim-Son, Kim-Son-Yoon, original RST general-flux work, earlier dilatonic wormholes, related forward citations, and moving-mirror literature. The exact constant-Kruskal-`P`, one-sided, every-ray first-hit formula was **not found in that corpus**.

This is absence of evidence within the named corpus, not exhaustive novelty. The same pass found:

- sustained one-sided input in original RST work, but in a different asymptotically flat energy coordinate and boundary problem;
- a finite one-sided step in earlier classical dilatonic-wormhole work, but in a different model;
- no printed every-ray first-hit formula for the Kim-Son past-asymptotically-AdS2 branch.

Read the full [bounded literature check](reviews/literature-check.md), including its thirteen-document scope and source links. A separate direct fetch of the two load-bearing precursor papers corroborates its sustained-input and finite-pulse claims; see [primary-source spot check](reviews/primary-source-spot-check.md). The later [2025–2026 literature spot check](reviews/recent-literature-2025-2026.md) covers Saito's multiple-injection RST Page curves, Arias–Fondevila replica capacity, Espíndola–Jahnke–Kim bath-induced traversable wormholes, and Castro et al.'s near-AdS2 backreaction. None supplies the present wall criterion. No publication-priority claim is made.

## 5. Additional state-dependence reference

Potaux, Sarkar, and Solodukhin's *Hybrid quantum states in 2D dilaton gravity* (2023) is directly relevant to the broader role of quantum-state choice in RST geometry. It studies state-dependent horizons, curvature singularities, and geodesic completeness, not the exact constant-`P` every-ray formula. Their 2025 *Islands for black holes in a hybrid quantum state* studies a regular causal-diamond hybrid geometry and radiation entropy, not the present wall criterion. See [Additional state-dependence literature](reviews/additional-state-dependence.md).

## 6. Future boundary and absorber scope

No future transparent or reflecting AdS2 boundary, coupled absorber action, or unique physical response under arbitrary state data is constructed here. Those are different boundary-value problems, not corollaries of the fixed solution.

The fixed solution does determine explicit interior proper-time intervals and null affine intervals. Those results must not be converted into a future-asymptotic observer or absorber claim.

Next: [Finite-pulse theorem](06-finite-pulse.md).
