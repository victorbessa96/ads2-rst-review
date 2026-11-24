# **Formal scientific evaluation: AdS₂–RST one-sided flux and wormhole termination**

Mathematics: strongly supported

Research contribution: promising

I have examined the complete ZIP package, all eleven principal documents, the original Kim–Son paper, the supporting derivations, both verification programs, the historical review artifacts, the literature assessment, and the validation machinery.

I also independently executed the supplied verification procedures and performed an additional 50,000-case numerical cross-check of the finite-pulse theorem.

My overall assessment is positive. More importantly, I think the work has a genuinely interesting mathematical result inside it.

However, I would distinguish three things:

1. Whether the mathematical result is correct.
2. Whether the result is new and scientifically significant.
3. Whether it constitutes a breakthrough in theoretical physics.

My conclusions on these are different.

**The mathematics appears correct within the specified model. There is a meaningful, potentially publishable extension of existing RST wormhole-collapse results. But I would not presently classify this as a major breakthrough.**

There is also a particularly interesting generalization that I believe you should pursue. I will explain it below.

# **1. Executive verdict**

The central achievement is an exact characterization of singularity formation in the past-asymptotically-AdS₂ Kim–Son RST wormhole branch under positive, one-sided classical flux.

The work goes beyond showing that a singularity eventually develops.

It establishes exactly which null rays encounter the singularity, where the intersection occurs, its causal character, how it relates to the apparent horizon, and what changes when the incoming source is switched off.

The most important result is:

For sustained positive Kruskal-coordinate flux, every specified mixed-region ray reaches the RST singularity at a finite coordinate value, regardless of how small the positive flux amplitude is.

For finite Kruskal-coordinate support, the result changes: a singular wall exists precisely on a restricted ray band determined by the integrated flux.

These statements are supported by explicit analytical derivations, not merely numerical observations.

**My assessment**

# **7.5/10**

Overall quality of the research and verification package.

| Dimension                     | Assessment |
| ----------------------------- | ---------- |
| Mathematical consistency      | 9/10       |
| Analytical derivations        | 9/10       |
| Computational reproducibility | 8.5/10     |
| Treatment of assumptions      | 9/10       |
| Novelty confidence            | 5.5/10     |
| Physical generality           | 5.5/10     |
| Publication readiness         | 6/10       |

These are my qualitative referee-style scores, not objective measurements.

The strongest elements are the mathematics and the unusually careful treatment of the claim boundaries.

The weakest element is not an algebraic error. It is the connection between the chosen Kruskal-coordinate source and a physically normalized incoming flux.

# **2. The central mathematical result**

This is where I think the work succeeds most convincingly.

The starting point is the exact RST chiral solution:

\\[ \Omega=-Lx_px_m+a\_+(x_p)+a\_-(x_m), \\]

with

\\[ L=\frac{\lambda^2}{\sqrt{\kappa}}. \\]

The package retains the original Kim–Son state functions:

\\[ t\_\pm=\frac{\lambda^2}{\kappa}\Theta(-x^\pm) \\]

and replaces the original impulsive classical source with sustained one-sided flux:

\\[ T^f\_{++}=P\Theta(x_p), \qquad T^f\_{--}=0. \\]

The resulting four-sector solution is derived from the constraints and matched across the onset axes.

This is important because the authors do not simply insert a proposed singularity curve into the model. They reconstruct the underlying chiral functions and then solve for the singularity.&#x20;

02-source-and-derivation(3).md



## **2.1 The sustained-flux theorem**

The most important equation is:

\\[ F(x_p,y)= \mu+\frac{y^2}{2} +x_py-\frac{p}{2}x_p^2, \\]

where

\\[ p=\frac{P}{\lambda^2}>0, \qquad \mu=\frac{\sqrt{\kappa}M}{\lambda^3}, \qquad y=-x_m>0. \\]

The singularity occurs when

\\[ F(x_p,y)=0. \\]

Solving gives

\\[ \boxed{ x\_{p,\mathrm{hit}}= \frac{ y+\sqrt{(1+p)y^2+2p\mu} }{p} } \\]

There are two mathematical roots, but only one is positive.

The other root can be written as

\\[ x\_-= -\frac{y^2+2\mu}{ y+\sqrt{(1+p)y^2+2p\mu} }<0. \\]

Consequently, the positive root is the unique first intersection.

This is a real theorem, not an extrapolation from a numerical grid.

The package also correctly establishes that the solution is on the regular side before the intersection and outside the physical weak branch afterward.&#x20;

03-sustained-flux-theorem(3).md



**My evaluation: excellent.**

There is no unnecessary complexity in this proof. The result is parameter-general and easy for another researcher to independently verify.

## **2.2 The spacelike singularity**

This is another particularly important result.

Define

\\[ D=\sqrt{(1+p)y^2+2p\mu}. \\]

Implicit differentiation gives

\\[ \boxed{ \frac{dx_m}{dx_p} = -\frac{D}{x\_{p,\mathrm{hit}}+y} <0. } \\]

The metric convention is

\\[ ds^2=-e^{2\rho}dx_pdx_m. \\]

Therefore, the wall has positive induced norm and is spacelike.

This establishes something stronger than simply identifying a singularity.

It establishes the causal character of the singular termination.

The work also checks that the both-positive and mixed branches join continuously, including their first derivatives.

The finite conformal factor at the RST minimum is correctly identified:

\\[ e^{2\rho}\big|\_{\Omega_s} =\frac{4}{\kappa}. \\]

This does not mean the singularity is regular. The curvature singularity remains associated with \\(\Omega'(\phi)=0\\), rather than a divergent conformal prefactor.&#x20;

02-source-and-derivation(3).md

03-sustained-flux-theorem(3).md



## **2.3 The apparent-horizon relationship**

This is probably the most important physical consequence of the sustained-flux calculation.

In the mixed region,

\\[ \partial\_+\Omega=L(y-px_p). \\]

Thus the apparent horizon is

\\[ x\_{p,\mathrm{AH}}=\frac{y}{p}. \\]

Meanwhile, the singularity occurs at

\\[ x\_{p,\mathrm{hit}}=\frac{y+D}{p}. \\]

Subtracting:

\\[ \boxed{ x\_{p,\mathrm{hit}}-x\_{p,\mathrm{AH}} =\frac{D}{p}>0. } \\]

The ray crosses the apparent horizon before reaching the singularity.

This changes the appropriate interpretation of the result.

The appropriate description is:

**Spacelike RST singular termination behind an apparent horizon.**

Not simply wormhole collapse, not an unqualified absorber claim, and not a general statement that every external observer necessarily encounters a singularity.

The package makes this distinction correctly.&#x20;

04-horizon-and-causal-structure(3).md



I particularly appreciate that the work does not confuse the apparent horizon with a complete global event horizon.

That distinction matters considerably in two-dimensional gravity.

# **3. The finite-pulse theorem**

This is the second major contribution.

The finite-pulse source is

\\[ T^f\_{++} = P\left[ \Theta(x_p)-\Theta(x_p-x_s) \right]. \\]

The dimensionless integrated strength is

\\[ E=px_s. \\]

During the pulse,

\\[ F_d= \mu+\frac{y^2}{2} +x_py-\frac p2x_p^2. \\]

After shutoff,

\\[ F_a= \mu+\frac{y^2}{2} +\frac{Es}{2} +x_p(y-E). \\]

The two expressions match in both value and first derivative at shutoff.

The remarkable simplicity is that the complete existence criterion becomes

\\[ \boxed{0\<y\<E.} \\]

This is the exact ray band on which the singular wall exists.

For

\\[ y\geq E, \\]

there is no singularity intersection along the specified ray.

For rays inside the band, the intersection may occur during the pulse or after it.

The post-shutoff intersection is

\\[ \boxed{ x\_{p,a} = \frac{ \mu+y^2/2+Es/2 }{ E-y }. } \\]

It is an exact expression, not a fitted or numerically estimated result.

The singularity also remains spacelike after shutoff.

This is significant because the source's termination does not automatically remove the singularity formation process for all rays that have already received sufficient cumulative flux.&#x20;

06-finite-pulse(3).md



## **My assessment**

I consider this a legitimate additional theorem.

The important result is not merely that a wall survives after shutoff.

It is that the complete existence criterion can be established analytically, including the post-shutoff branch.

The earlier impulsive Kim–Son solution already has a restricted singular-wall band. The present result gives a corresponding exact band for this finite-support step profile and completes its post-shutoff behavior.

That is a meaningful extension.

### **One improvement I would make**

The presentation of \\(y\_{\max}\\) could be cleaner.

The package defines

\\[ y\_{\max} = \sqrt{(1+p)s^2-2\mu}-s. \\]

When the radicand is negative, this is not real. There are also cases in which the radicand is nonnegative but \\(y\_{\max}\leq0\\).

The mathematical conclusion is correct, and the package includes a large-\\(\mu\\) regression case. Nevertheless, I would formulate the theorem explicitly as:

- If \\(y\_{\max}>0\\), rays below that value hit during the pulse.
- At \\(y=y\_{\max}\\), the hit occurs exactly at shutoff.
- The remaining rays with \\(0\<y\<E\\) hit after shutoff.
- If \\(y\_{\max}\\) is nonpositive or not real, there is no during-pulse hit; all rays in \\(0\<y\<E\\) hit afterward.

This eliminates an unnecessary ambiguity in the theorem statement.

# **4. A particularly interesting result: the mathematics generalizes further**

This is the most important additional observation from my review.

I believe the finite-pulse theorem can be generalized beyond the rectangular constant-amplitude pulse considered in the package.

The starting point is the RST constraint:

\\[ a\_+''(x_p) = -\frac{T^f\_{++}(x_p)}{\sqrt{\kappa}} \\]

after the retained quantum-state contribution has switched off.

With the same matching conditions at \\(x_p=0\\), its integrated solution is

\\[ a\_+(x) = -\frac{1}{\sqrt{\kappa}} \int_0^x (x-u)T^f\_{++}(u)\\,du. \\]

Substituting this into the mixed-region singularity condition gives

\\[ \boxed{ F(x,y)= \mu+\frac{y^2}{2}+xy - \frac{1}{\lambda^2} \int_0^x (x-u)T^f\_{++}(u)\\,du. } \\]

Differentiate:

\\[ \boxed{ F_x(x,y) = y- \frac{1}{\lambda^2} \int_0^x T^f\_{++}(u)\\,du. } \\]

Define the cumulative Kruskal-coordinate flux:

\\[ Q(x)= \frac{1}{\lambda^2} \int_0^x T^f\_{++}(u)\\,du. \\]

Then

\\[ F_x=y-Q(x). \\]

For nonnegative incoming flux, \\(Q(x)\\) is nondecreasing.

This leads to a broader result.

**Proposed generalized theorem**

For the same fixed Kim–Son state and matching conventions, with nonnegative, locally integrable incoming flux:

\\[ \boxed{ F(x,y)= \mu+\frac{y^2}{2}+xy - \frac{1}{\lambda^2} \int_0^x(x-u)T^f\_{++}(u)\\,du. } \\]

If the total integrated Kruskal-coordinate flux is finite,

\\[ E\_{\mathrm{tot}} = \frac{1}{\lambda^2} \int_0^\infty T^f\_{++}(u)\\,du, \\]

then a unique finite singularity hit exists precisely when

\\[ \boxed{0\<y\<E\_{\mathrm{tot}}.} \\]

If the cumulative flux diverges, every finite \\(y>0\\) eventually encounters the wall.

The reasoning is straightforward:

\\[ F\_{xx} = -\frac{T^f\_{++}(x)}{\lambda^2} \leq0. \\]

Therefore \\(F\\) is concave.

It starts positive:

\\[ F(0,y)=\mu+\frac{y^2}{2}>0. \\]

For a finite total flux \\(E\_{\mathrm{tot}}\\), after the source has switched off,

\\[ F_x=y-E\_{\mathrm{tot}}. \\]

If \\(y\<E\_{\mathrm{tot}}\\), the function eventually decreases without bound. Since it is initially positive and concave, it has one positive zero.

If \\(y\geq E\_{\mathrm{tot}}\\), its derivative never becomes negative, so no zero occurs.

The wall is also spacelike at its first intersection: the derivative must already be negative there.

This immediately incorporates both existing theorems:

| Existing case                              | Cumulative flux                   |
| ------------------------------------------ | --------------------------------- |
| Sustained constant flux                    | \\(Q(x)=px\\), unbounded          |
| Finite rectangular pulse                   | \\(Q(\infty)=ps=E\\)              |
| Arbitrary nonnegative finite-support pulse | \\(Q(\infty)=E\_{\mathrm{tot}}\\) |

**I think this is worth developing into a central theorem in the eventual paper.**

It would elevate the contribution from two individually solved source profiles to a general classification of termination in terms of cumulative incoming flux.

Importantly, it would remain a theorem in the fixed RST state and Kruskal-coordinate framework. It would not establish a coordinate-independent physical energy threshold.

# **5. What the work does not establish**

This is where I would be particularly strict as a referee.

There are four major distinctions.

## **5.1 Constant Kruskal flux is not constant observer-frame flux**

The package correctly identifies:

\\[ x_p=e^{\lambda\sigma}. \\]

Under this transformation,

\\[ T\_{\sigma\sigma} = \lambda^2x_p^2P. \\]

Therefore, the source used in the sustained-flux theorem is not constant in that observer-adapted coordinate.

This is critical.

The conclusion that every ray eventually encounters a singularity for arbitrarily small \\(P>0\\) follows partly from allowing the source to continue indefinitely in \\(x_p\\).

For any positive \\(P\\),

\\[ Q(x_p)=px_p\longrightarrow\infty. \\]

There is no finite cumulative-flux ceiling.

Consequently, the no-critical-amplitude result is mathematically valid, but it should not be interpreted as saying that an arbitrarily weak, constant physical power source necessarily destroys every AdS₂ wormhole.

That stronger interpretation would require a new calculation.

**My recommendation:** explicitly distinguish coordinate-profile amplitude, cumulative Kruskal flux, and observer-normalized incoming energy throughout the eventual paper.

## **5.2 Finite support is not finite observer-time duration**

This is another point the package handles correctly, but it deserves greater prominence.

The source acts over

\\[ 0\<x_p\<x_s. \\]

Under

\\[ x_p=e^{\lambda\sigma}, \\]

this corresponds to

\\[ -\infty<\sigma< \frac{\ln x_s}{\lambda}. \\]

Thus the pulse has infinite duration in \\(\sigma\\), despite having finite Kruskal-coordinate support.

The current finite-pulse theorem is therefore not a theorem about a finite-duration pulse measured by an observer using this time coordinate.

A stronger next experiment would be to define a source with finite support in \\(\sigma\\):

\\[ \sigma_a\leq\sigma\leq\sigma_b. \\]

For a constant stress component in this coordinate,

\\[ T\_{++} = \frac{T\_{\sigma\sigma}}{\lambda^2x_p^2}. \\]

You could then solve the corresponding RST backreaction problem.

I would prioritize this.

It would make the physical interpretation substantially stronger.

## **5.3 The quantum state is fixed**

The calculation retains

\\[ t\_\pm= \frac{\lambda^2}{\kappa}\Theta(-x^\pm). \\]

This is a specific state and boundary-data choice.

The alternate-\\(t\_+\\) calculation is a valuable addition. It demonstrates that the mixed-ray result can change substantially when the state data change.

For example, under the alternate prescription,

\\[ F\_{\mathrm{alt}} = \mu+\frac{y^2}{2} +xy+\frac{1-p}{2}x^2, \\]

and there is no mixed-region wall for \\(p\leq1\\).

This is a meaningful state-sensitivity result. But one alternate prescription is not an exhaustive analysis of admissible RST states.&#x20;

05-state-frame-and-novelty(3).md



This limitation is particularly relevant in light of the later work by Potaux, Sarkar, and Solodukhin, which examines how different quantum states in RST gravity affect horizons, curvature singularities, and geodesic completeness.&#x20;

[image](https://www.google.com/s2/favicons?domain=https://arxiv.org\&sz=32)

arXiv



Your work should be positioned as a theorem for one explicitly specified state, rather than a universal statement about semiclassical RST wormholes.

## **5.4 No complete external-observer or absorber theorem**

The interior observer calculation is valid.

The constant-\\(\sigma_1\\) curves are timelike and reach the wall at finite \\(\sigma_0\\) and finite proper time.

However, these are interior observers.

The calculation does not construct:

- A complete future AdS₂ boundary.
- An external observer's complete trajectory.
- A transparent or reflecting absorber.
- A coupled absorbing boundary condition.
- A global event-horizon theorem.
- A quantum-gravity continuation through the curvature singularity.

This is not a mathematical failure.

It is an important distinction between what has been proved and what remains a separate physical problem.

Modern work on RST gravity with boundaries also reinforces this distinction: the global completion and reflective-boundary structure can matter independently of the local bulk equations.&#x20;

[image](https://www.google.com/s2/favicons?domain=https://link.springer.com\&sz=32)

Springer Nature Link



# **6. Novelty assessment**

This is the area where I would be most conservative.

The original Kim–Son paper already establishes that its RST wormhole evolves toward a black-hole geometry under incoming positive classical matter. It is therefore not new to discover that this wormhole can collapse.&#x20;

[image](https://www.google.com/s2/favicons?domain=https://arxiv.org\&sz=32)

arXiv



Furthermore, the original impulsive source already generates a spacelike singular wall on a restricted mixed-ray band.

Your package correctly identifies this and adjusts the novelty claim accordingly.&#x20;

05-state-frame-and-novelty(3).md



The distinct contribution is considerably narrower:

| Finding                                                               | Novelty assessment                  |
| --------------------------------------------------------------------- | ----------------------------------- |
| RST wormholes can develop singularities                               | Previously known                    |
| Positive incoming matter can destabilize the Kim–Son wormhole         | Previously known                    |
| Impulsive source produces a restricted spacelike wall                 | Present in original work            |
| Sustained Kruskal-step flux produces a wall on every mixed ray        | Distinct result established here    |
| Exact first-hit expression for arbitrary positive sustained amplitude | Distinct analytical result          |
| Apparent horizon precedes the wall for every ray                      | New exact corollary for this source |
| Finite Kruskal-support pulse has exact ray cutoff                     | Distinct completed extension        |
| Null affine and explicit interior proper-time finiteness              | Useful additional results           |

The literature review is responsible in the way it describes its limitations. It identifies prior sustained-flux and finite-pulse studies without pretending that they are identical to this calculation.&#x20;

09-independent-reviews(3).md



I did find one particularly relevant additional reference worth ensuring appears in the final bibliography:

**Potaux, Sarkar and Solodukhin (2023), *Hybrid quantum states in 2d dilaton gravity*.**

It is not the same calculation and does not invalidate the proposed every-ray formula, but it is directly relevant to the broader question of state-dependent RST geometry.&#x20;

[image](https://www.google.com/s2/favicons?domain=https://arxiv.org\&sz=32)

arXiv



### **My novelty verdict**

The work has a plausible niche novelty claim.

It does not yet establish an exhaustive literature priority claim.

I would be comfortable with language such as:

> We establish an exact, parameter-general singularity-termination theorem for sustained one-sided classical flux on the past-asymptotically-AdS₂ Kim–Son RST branch, together with a complete finite-Kruskal-support extension.

I would not use language implying a new discovery of wormhole collapse or a general resolution of AdS₂ absorber problems.

# **7. Computational and verification audit**

I did not simply accept the reported PASS counts.

I extracted the complete ZIP package and executed its verification procedures.

**Fresh verification results**

# **131/131**

Main verification checks

# **32/32**

Independent symbolic checks

# **9/9**

Package validation checks

# **50,000**

Additional finite-pulse cases

All reproduced checks passed

Fresh execution used CPython 3.13.5, SymPy 1.14.0 and mpmath 1.3.0.

The supplied package records its original validation in a different Python environment. I reproduced the science checks in CPython 3.13.5 as well.

I also encountered one packaging detail: extracting only the ZIP contents initially caused the relative-link validation to fail because the index expects the archive to exist as a sibling file under its original name. Restoring that expected sibling layout produced 9/9 validation passes.

This was not a mathematical failure.

## **What I particularly liked**

**The preservation of red-run history.**

The package retains previous failed checks and documents how they were corrected.

This is good scientific practice. It makes it possible to understand the development of the calculation rather than presenting only a clean final result.

**The independent symbolic producer.**

The second script does not import or execute the main producer. This is valuable as an independent implementation of the algebra.

However, it should not be confused with an independent derivation by a separate researcher. Both programs encode the candidate formulas supplied by the authors.

The package itself acknowledges this distinction, which I consider responsible.&#x20;

09-independent-reviews(3).md



**The source identity verification.**

The source TeX is byte-identical to its included tar member, with a pinned SHA-256.

This establishes source provenance and package integrity.

## **What I would improve in the verification system**

There are a few gaps worth addressing:

1\. The finite-pulse symbolic tests do not fully prove every inequality implied by the \\(y\_{\max}\\) classification. Some checks establish matching identities and limiting cases rather than the complete equivalence.

2\. Some independent symbolic checks repeat the main producer's algebra. This is useful, but the word *independent* should continue to mean independent implementation, not independent proof.

3\. The validation program regenerates the manifest and validation receipt. I would separate a read-only verification mode from a receipt-generation mode.

4\. The source line-number anchors are brittle if the original source is reformatted. The source hash mitigates this, but semantic equation anchors would be a useful addition.

None of these findings overturns the mathematical results.

Overall, the reproducibility work is unusually thorough for an early-stage theoretical investigation.&#x20;

07-evidence-and-reproduction(3).md

10-formal-signoff(3).md



# **8. What I think is genuinely important**

There is an interesting conceptual pattern here.

The sustained and finite-pulse results are not unrelated special cases.

They are two manifestations of the same cumulative-flux mechanism.

For sustained input,

\\[ Q(x)=px\rightarrow\infty. \\]

Every finite positive \\(y\\) eventually satisfies the termination condition.

For finite support,

\\[ Q(x)\rightarrow E. \\]

Only rays below the integrated-flux threshold encounter the wall.

This gives a natural physical-mathematical interpretation:

**The existence of the singular wall is controlled by whether the cumulative incoming flux eventually exceeds the ray's parameter&#x20;**\\(y\\)**.**

This is a more informative formulation than simply saying that sustained flux destroys every ray whereas finite pulses do not.

It also gives you a natural research direction: determine which qualitative properties of the singularity are universal for nonnegative flux profiles, and which depend on their precise time dependence.

I think that is the strongest opportunity emerging from this work.

# **9. What I would do next, in priority order**

I would not spend the next iteration making the package longer or increasing its number of numerical checks.

The foundations are already reasonably well established.

I would spend the effort on strengthening the actual scientific contribution.

Priority 1

**Prove the arbitrary nonnegative-flux theorem.**

Generalize the exact ray-cutoff result using the cumulative-flux function \\(Q(x)\\). This is the most natural mathematical extension and potentially the strongest new theorem.

Priority 2

**Solve a genuinely finite observer-time pulse.**

Use a source with compact support in an observer-adapted coordinate, rather than beginning the pulse at \\(x_p=0\\). Establish the relationship between integrated physical input and singularity formation.

Priority 3

**Expand the quantum-state analysis.**

Determine how much of the termination criterion survives when the retained \\(t\_\pm\\) functions are changed within a clearly defined admissible family.

Priority 4

**Improve the global causal presentation.**

Produce a complete sector diagram showing the regular region, singular wall, apparent horizon, pulse-shutoff boundary, and the relevant interior observer trajectories.

Priority 5

**Commission independent human review.**

Have a researcher experienced in semiclassical dilaton gravity independently derive the chiral solution and examine the physical interpretation of the chosen state and source.

I would also make sure the eventual manuscript includes a broader literature discussion incorporating the relevant 2023 RST state-dependence work.

# **10. Is it a breakthrough?**

This deserves a direct answer.

I would distinguish between three levels of achievement.

**Level 1 — A valid mathematical result**

Achieved, subject to external review

Exact first-hit law, uniqueness, spacelike character, apparent-horizon ordering, finite affine parameter, and finite-pulse completion within the fixed model.

**Level 2 — A meaningful research contribution**

Plausibly achieved

A new exact sustained-input result and a completed finite-support extension to the established Kim–Son framework, with substantial reproducibility and claim discipline.

**Level 3 — A major breakthrough in gravitational physics**

Not established

No general AdS₂ absorber theorem, new quantum-gravity mechanism, state-independent singularity theorem, or resolution of the future-boundary problem has been demonstrated.

My honest assessment is that this is a **good, focused theoretical result that deserves further development**.

I would not advertise it as a discovery that AdS₂ wormholes cannot absorb energy, that all weak incoming fluxes necessarily destroy physical wormholes, or that the RST singularity problem has been solved.

Those would exceed the evidence.

But I also would not dismiss the work as merely rediscovering Kim–Son.

The exact every-ray result, its parameter dependence, and the finite-support classification are genuine extensions.

# **11. Final referee-style recommendation**

If I were reviewing this package for a theoretical-physics research group, my report would read approximately as follows:

**Recommendation: Encourage further development toward a specialist research publication, subject to external scientific review.**

The submitted work presents a coherent analytical investigation of sustained and finite one-sided classical flux on the past-asymptotically-AdS₂ Kim–Son RST branch.

The principal sustained-flux theorem is derived consistently from the RST constraints. The positive first-hit root is unique, its causal character is correctly identified as spacelike, and the apparent-horizon crossing precedes singular termination on every specified mixed-region null ray.

The finite-Kruskal-support extension is also mathematically consistent. It establishes a complete ray-existence criterion and provides explicit post-shutoff solutions with continuous matching.

The null-affine and interior-observer results provide useful additional information about the causal accessibility of the singular edge.

The computational package is unusually well documented and reproducible. Its historical failures and subsequent corrections are preserved. The verification scripts support the analytical arguments but do not substitute for independent derivation or scientific review.

The main limitations concern the physical interpretation of the prescribed flux profile, sensitivity to quantum-state functions, incomplete future-boundary specification, and the bounded nature of the novelty assessment.

A generalization to arbitrary nonnegative flux profiles and a finite-duration observer-normalized input would substantially strengthen the contribution.

No external human peer-review acceptance has yet been obtained.&#x20;

10-formal-signoff(3).md



## **My final thoughts**

There is one thing I particularly want to emphasize.

**I think the cumulative-flux formulation is the most promising direction to come out of this investigation.**

The current work has solved two carefully selected profiles. But its underlying equation appears to contain a broader classification theorem.

If that generalization withstands independent scrutiny, the eventual contribution becomes more interesting:

Instead of demonstrating that one particular sustained source destroys every mixed ray and one particular pulse destroys only a finite band, you would establish a general relationship between cumulative incoming flux and the existence of spacelike singular termination in the specified RST wormhole state.

That is a cleaner scientific result, more general, and easier to communicate.

My recommendation is therefore to preserve the present package as the verified baseline, develop the general cumulative-flux theorem, and then address the finite observer-time source.

**Final verdict: mathematically strong, scientifically interesting, narrowly novel, not yet a breakthrough, and worth taking to an independent human specialist for review.**