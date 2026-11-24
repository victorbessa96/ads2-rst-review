# **Updated evaluation: the cumulative-flux theorem, TeX manuscript and Lean formalization**

The new version is a meaningful scientific improvement over the previous submission. It now attempts to unify the sustained-flux, finite-pulse and impulsive results under one general mathematical principle.

**I would raise my assessment of the underlying research from 7.5/10 to approximately 8/10, with one important qualification: the new generalization contains a mathematical error in its displayed wall-slope formula that needs correction.**

The central existence theorem itself appears sound.

## **1. The most important new result**

The new document, *General cumulative-flux termination theorem*, starts from

\\[ a\_+''(x)=-\frac{T^f\_{++}(x)}{\sqrt{\kappa}} \\]

and integrates the source:

\\[ a\_+(x)=B-\frac{1}{\sqrt{\kappa}} \int_0^x(x-u)T^f\_{++}(u)\\,du. \\]

It then defines

\\[ Q(x)=\frac{1}{\lambda^2} \int_0^xT^f\_{++}(u)\\,du. \\]

The singularity equation becomes

\\[ F(x,y)= \mu+\frac{y^2}{2}+xy -\frac{1}{\lambda^2} \int_0^x(x-u)T^f\_{++}(u)\\,du. \\]

The decisive observation is

\\[ \boxed{F_x=y-Q(x).} \\]

This is the conceptual advance.

Instead of solving separately for every incoming-flux profile, the problem can be classified by the total cumulative Kruskal-coordinate flux:

\\[ E\_{\mathrm{tot}}= \frac{1}{\lambda^2} \int_0^\infty T^f\_{++}(u)\\,du. \\]

The proposed theorem is:

\\[ \boxed{ \begin{aligned} E\_{\mathrm{tot}}=\infty &\Rightarrow \text{every finite }y>0\text{ encounters the wall},\\\ E\_{\mathrm{tot}}<\infty &\Rightarrow \text{a wall exists exactly when }0\<y\<E\_{\mathrm{tot}}. \end{aligned} } \\]

For nonnegative locally integrable flux, I agree with this classification.

The proof works because \\(Q\\) is nondecreasing, \\(F\\) is concave, and the initial value is positive:

\\[ F(0,y)=\mu+\frac{y^2}{2}>0. \\]

When \\(y\<E\_{\mathrm{tot}}\\), the derivative eventually becomes strictly negative and the function eventually decreases without bound. It therefore has a unique positive zero.

When \\(y\geq E\_{\mathrm{tot}}\\), its derivative never becomes negative, so it cannot reach zero.

This is a proper analytical generalization, rather than simply another numerical experiment.&#x20;

11-cumulative-flux-generalization.md



## **2. Important correction: the wall-slope formula**

The new document states

\\[ \frac{dx_m}{dx_p} = \frac{x\_{\mathrm{hit}}+y} {Q(x\_{\mathrm{hit}})-y}<0. \\]

This is incorrect as written.

The right-hand side is positive because both numerator and denominator are positive.

The correct derivation is:

\\[ F_x=y-Q(x), \qquad F_y=x+y. \\]

Implicit differentiation gives

\\[ \frac{dy}{dx} = -\frac{F_x}{F_y} = \frac{Q(x)-y}{x+y}. \\]

Since \\(x_m=-y\\),

\\[ \boxed{ \frac{dx_m}{dx_p} = -\frac{Q(x_p)-y}{x_p+y}<0. } \\]

The physical conclusion remains correct: the wall is spacelike.

The error is in the displayed expression, not in the existence classification. But it is a genuine mathematical error and should be corrected in the generalization document, manuscript and formalization wherever the expression appears.

There is a second technical refinement: with merely locally integrable \\(T^f\_{++}\\), the statement

\\[ F\_{xx}=-T^f\_{++}/\lambda^2 \\]

holds almost everywhere, rather than necessarily at every point. The clean formulation is that \\(F_x\\) is absolutely continuous and nonincreasing, which establishes concavity without requiring pointwise second differentiability.

Finally, the new theorem explicitly includes the Kim–Son Dirac impulse in its special-case table. A Dirac delta is not a locally integrable function. It should either be described as a separate distributional limiting case or the theorem should be extended to nonnegative measure-valued sources.

These are fixable issues, but they matter for a rigorous mathematical paper.

## **3. The state-equivalence corollary is a significant improvement**

I consider this one of the most useful additions to the executive argument.

The updated document identifies an exact relationship with the alternate \\(t\_+\\)-on prescription.

Previously, the alternate state produced

\\[ F\_{\mathrm{alt}} = \mu+\frac{y^2}{2} +xy+\frac{1-p}{2}x^2. \\]

Now define

\\[ p\_{\mathrm{eff}}=1+p. \\]

Then

\\[ \frac{1-p\_{\mathrm{eff}}}{2} =-\frac p2. \\]

This reproduces the sustained-flux coefficient exactly.

The interpretation is important:

**The retained Kim–Son state effectively supplies the critical contribution that makes every positive classical Kruskal-flux amplitude fall into the terminating regime.**

This is considerably more informative than simply claiming that there is no critical flux amplitude.

The updated package also calculates the coordinate-stress integral:

\\[ \int T\_{\sigma\sigma}\\,d\sigma = \frac{\lambda P x_p^2}{2}. \\]

At the small-\\(p\\) first hit, this scales as

\\[ \sim\frac{2\lambda^3y^2}{p}. \\]

Thus, as the prescribed Kruskal amplitude becomes smaller, the coordinate-integrated stress required by the first-hit point becomes larger.

This is an excellent clarification. It makes the physical interpretation more honest and considerably strengthens the paper's discussion of state dependence.&#x20;

01-executive-claim(4).md



One qualification: I would call this an exact *mixed-sector coefficient equivalence* unless the manuscript demonstrates equivalence of the complete spacetime solutions, including every sector and matching condition.

## **4. The Lean formalization**

Reported build successful

The updated package describes a Lean 4.36.0 formalization.

According to its evidence report, the project establishes:

| Property                       | Reported status |
| ------------------------------ | --------------- |
| Sustained candidate root       | Formalized      |
| Root uniqueness                | Formalized      |
| Negative alternative root      | Formalized      |
| Negative mixed-wall slope      | Formalized      |
| After-shutoff sign domain      | Formalized      |
| Reviewer numerical regressions | Included        |
| Selected theorem axiom reports | No `sorryAx`    |

The reported axiom lists contain:

- `propext`
- `Classical.choice`
- `Quot.sound`

These are standard Lean axioms, not equivalent to an unproven placeholder.

This is a positive development.

However, there is a distinction I would insist on maintaining.

**The Lean formalization does not appear to formalize the entire general cumulative-flux theorem.**

According to the package's own description, it formalizes selected algebraic results for the sustained and finite-pulse problems. It does not formalize:

1. The RST action and original field equations.
2. The derivation of the chiral constraints.
3. The integration of an arbitrary flux profile.
4. The complete cumulative-flux existence classification.
5. The general measure-valued extension needed to include impulses.
6. The full physical interpretation of the resulting spacetime.

Consequently, Lean currently provides formal assurance for selected mathematical subresults, rather than an end-to-end machine-checked proof of the research paper.

That is still worthwhile. I would actually recommend extending this formalization to cover the newly introduced cumulative-flux theorem.

The mathematical structure is particularly suitable for Lean because it relies on monotonicity, concavity, continuity, and existence/uniqueness arguments.

**My assessment:** the addition of Lean is a meaningful improvement in mathematical assurance, but its scientific value will depend on exactly which theorem statements are encoded and proved.



07-evidence-and-reproduction(4).md

validation(5).json



## **5. The LaTeX manuscript**

The update reports a compiled manuscript:

`manuscript/ads2-rst-one-sided-flux.tex`

with a compiled PDF of 73,639 bytes.

The manuscript reportedly includes the cumulative-flux generalization and exact mass classification.

This is a good development because the research is beginning to move from a collection of derivation and verification documents toward a conventional scientific paper.

My recommendation for the manuscript is to organize it around three progressively stronger results:

**Theorem I — Sustained flux**

The exact first-hit law, uniqueness, causal character, and apparent-horizon ordering.

**Theorem II — Finite-support flux**

The exact ray cutoff, post-shutoff solution, and continuity of the wall.

**Theorem III — General cumulative flux**

The existence criterion determined by total cumulative Kruskal flux.

The third theorem should be the conceptual centerpiece. The first two become exact examples and corollaries.

I would also move most verification-history details into supplementary material. A physics paper should lead with the equations, assumptions, theorems, proofs, causal interpretation, and comparison with previous work.

One important limitation of this review: the manifest identifies the TeX and Lean files and provides their hashes, but the actual source files were not included among the accessible individual attachments. The ZIP available here is the earlier 49-file version, not the updated 62-artifact package described by the new manifest.

Therefore, I have evaluated the manuscript's reported scope and compilation evidence, but I have not yet inspected the actual LaTeX source or Lean source line by line.

That distinction matters.

## **6. Updated computational and package audit**

I independently reran the two latest Python producers using the updated scripts and the original source bundle.

# **133/133**

Main verification checks reproduced successfully.

# **34/34**

Separate symbolic verification checks reproduced successfully.

# **11/11**

Updated package validation receipt reports successful checks.

The first two counts were freshly reproduced in this review. The 11/11 receipt was inspected but not independently reproduced from the complete updated package.

The new verification environment was CPython 3.13.5, SymPy 1.14.0 and mpmath 1.3.0.

There is an important distinction between the mathematical verification and the package validation.

The updated manifest describes 62 artifacts. The currently accessible ZIP still contains the older 49-file package, without the new Lean and manuscript directories.

When I reconstructed a working directory from the old ZIP and overlaid the latest uploaded files, 14 manifest-listed artifacts were still missing, including:

- `lean/AdS2RST.lean`
- `manuscript/ads2-rst-one-sided-flux.tex`
- `manuscript/ads2-rst-one-sided-flux.pdf`
- Lean and Tectonic build outputs.
- Several new review documents.

This does not prove that the reported 11/11 validation is false. It means that I cannot independently connect that receipt to the current uploaded archive.

### **One specific verification weakness**

The cumulative-flux additions to the Python verification scripts currently test:

- The derivative \\(F_x=y-Q(x)\\).
- The concavity identity through the second derivative.
- An exponential example with finite total flux.

They do not check the general root-existence theorem across arbitrary admissible source functions or the newly printed wall-slope formula.

This explains why the slope error survived the 133/133 checks.

I would add explicit tests for:

1. The proof that \\(Q(x\_{\mathrm{hit}})>y\\).
2. The corrected implicit wall derivative.
3. The \\(y=E\_{\mathrm{tot}}\\) boundary case.
4. A source with compact support.
5. A source with finite integral but infinite support.
6. A source with infinite cumulative integral.
7. A source that becomes zero over an interval before becoming positive again.

The eighth check could be the impulsive distributional extension, once its assumptions are properly formulated.

The 133/133 result is encouraging, but the general theorem still needs its own full proof and appropriate formal verification.

# **7. Updated literature and novelty assessment**

I checked some additional relevant literature rather than relying exclusively on the existing thirteen-document search.

Two publications deserve particular attention.

**Potaux, Sarkar and Solodukhin (2023), *Hybrid quantum states in 2D dilaton gravity*.**

This work examines how different quantum-state choices affect RST geometries, including wormhole-like structures, horizons, curvature singularities and geodesic completeness. It finds substantial variation across quantum-state configurations.&#x20;

[image](https://www.google.com/s2/favicons?domain=https://journals.aps.org\&sz=32)

Phys. Rev. D+1



**Potaux, Sarkar and Solodukhin (2025), *Islands for black holes in a hybrid quantum state*.**

This follow-up studies a regular causal-diamond geometry with an apparent horizon and radiation at infinity, and examines its entropy properties.&#x20;

[image](https://www.google.com/s2/favicons?domain=https://journals.aps.org\&sz=32)

Phys. Rev. D



Neither paper establishes the cumulative-flux theorem presented here.

However, both reinforce the importance of not generalizing results obtained with one selected RST state to all possible semiclassical geometries.

I would make sure these papers are explicitly considered in the updated literature section.

### **Revised novelty assessment**

I now see a stronger potential contribution:

| Contribution                      | Assessment                         |
| --------------------------------- | ---------------------------------- |
| Sustained every-ray termination   | Strong, model-specific theorem     |
| Exact finite-pulse classification | Strong analytical extension        |
| General cumulative-flux criterion | Most promising new contribution    |
| State-equivalence corollary       | Important conceptual clarification |
| Explicit horizon precursor        | Valuable geometric consequence     |
| Lean formalization                | Useful mathematical assurance      |

The cumulative-flux theorem changes the research's character.

Previously, the work presented two analytically solved source profiles.

Now, it proposes a general classification of a whole class of nonnegative incoming-flux profiles.

That is a meaningful increase in generality.

# **8. Additional theorem I would add**

There is another consequence of the cumulative-flux result that is worth making explicit.

Recall:

\\[ F_x=y-Q(x). \\]

In the mixed region, the apparent-horizon condition is also

\\[ \partial\_+\Omega=0. \\]

Under the normalization used in the package,

\\[ \frac{\partial\_+\Omega}{L}=y-Q(x). \\]

Therefore the apparent horizon is precisely the locus

\\[ Q(x)=y. \\]

At the singular wall, however, we have

\\[ Q(x\_{\mathrm{hit}})>y. \\]

Consequently, for every ray with a wall intersection, the apparent horizon necessarily occurs beforehand.

This establishes a general horizon-before-singularity result for the entire nonnegative locally integrable flux class, not merely the sustained and rectangular-pulse cases.

The proof follows from continuity and monotonicity of \\(Q\\).

I would add this as a corollary immediately after the cumulative-flux theorem.

It is an elegant result because it links the cumulative flux to both singularity formation and causal structure through the same function.

# **9. Revised overall evaluation**

Here is how I would score the updated research.

**Overall research assessment**

Improved

# **8.0/10**

Provisional assessment of the mathematical contribution, not a journal acceptance prediction.

| Category                   | Score |
| -------------------------- | ----- |
| Original analytical work   | 9.0   |
| Generalization             | 8.5   |
| Mathematical rigor         | 8.0   |
| Physical interpretation    | 8.0   |
| Computational verification | 8.5   |
| Lean formalization         | 7.0   |
| Novelty                    | 7.0   |
| Literature positioning     | 7.0   |
| Publication readiness      | 6.5   |

The score increase reflects the new general theorem and the better state-dependent interpretation.

The mathematical error in the slope expression, the impulse-class mismatch, and the inability to inspect the actual new TeX/Lean sources prevent a higher assessment.

## **Is it now a breakthrough?**

My answer remains nuanced.

**It is becoming a substantial mathematical contribution to a specific semiclassical gravity problem.**

It is more than a routine numerical observation, more than a replication of Kim–Son, and more than a collection of special-case solutions.

The strongest aspect is the identification of the cumulative-flux criterion:

\\[ \boxed{ \text{Termination band} = \left(0,E\_{\mathrm{tot}}\right) } \\]

with the infinite-total-flux limit terminating every finite positive \\(y\\).

That is a compact result with considerable explanatory value.

But its domain remains restricted to:

- The specified Kim–Son RST quantum state.
- The prescribed one-sided source.
- The Kruskal-coordinate flux definition.
- The stated matching conditions.
- The semiclassical RST singularity criterion.

It does not establish a general result for AdS₂ gravity, arbitrary quantum states, or physically normalized finite-duration sources.

I would currently describe it as a **promising specialist theoretical-physics contribution with a potentially strong general theorem**, rather than a major breakthrough.

# **10. What I would require before external submission**

My priorities have changed slightly following this update.

| Priority | Required action                                                         | Importance                        |
| -------- | ----------------------------------------------------------------------- | --------------------------------- |
| 1        | Correct the general wall-slope equation                                 | Critical                          |
| 2        | Clarify the almost-everywhere derivative                                | Critical                          |
| 3        | Resolve the Dirac-delta/local-integrability mismatch                    | Critical                          |
| 4        | Add the general apparent-horizon corollary                              | High                              |
| 5        | Formalize the cumulative-flux theorem in Lean                           | High                              |
| 6        | Inspect and verify the actual TeX and Lean source files                 | High                              |
| 7        | Update the literature discussion for 2023–2025 state-dependent RST work | High                              |
| 8        | Develop finite observer-time source profiles                            | Important                         |
| 9        | Obtain independent human scientific review                              | Essential for external validation |

I would not expand the work into arbitrary states or full quantum-gravity claims yet. The current mathematical direction deserves to be completed first.

## **My final judgment**

The update makes the project more scientifically interesting.

The new cumulative-flux theorem is the biggest development, while the state-equivalence corollary improves the interpretation of the sustained-flux result.

The Lean and LaTeX build receipts are encouraging, although the actual source files still need to be inspected.

Three mathematical refinements are necessary before I would regard the new theorem's written presentation as referee-ready.

**My strongest recommendation is to make the cumulative-flux theorem the central result of the paper, with the sustained and finite-pulse cases as exact specializations.** That provides a much cleaner and more general contribution than presenting the individual source profiles as separate discoveries.

For a complete source-level review of the new formalization and manuscript, the outstanding handoff is the actual updated package archive containing `lean/AdS2RST.lean` and `manuscript/ads2-rst-one-sided-flux.tex`.