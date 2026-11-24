# **1. Updated referee verdict**

Major mathematical issues from the previous revision addressed

Packaging defect remains

I have now inspected the actual `Archive.zip`, rather than relying on the previous summaries.

This is a substantial improvement in the presentation and mathematical formulation.

In particular, I confirm three important corrections:

- The cumulative-flux theorem now explicitly covers **nonnegative Radon measures**, not just locally integrable flux densities.
- The manuscript now distinguishes ordinary derivatives from one-sided derivatives at discontinuities.
- The wall-slope formula has been corrected:

\\[ \boxed{ \left.\frac{dx_m}{dx_p}\right|\_+ = -\frac{Q(x\_{\mathrm{hit}})-y} {x\_{\mathrm{hit}}+y}<0. } \\]

This resolves the principal mathematical presentation error I identified previously.

The manuscript also incorporates the general apparent-horizon precursor and acknowledges that the measure-valued result is not fully formalized in Lean.

These are meaningful improvements.

There is, however, a new packaging issue I independently identified.

**The embedded&#x20;**`Archive.zip.sha256`**&#x20;does not match the actual uploaded archive.**

| Item                           | SHA-256               |
| ------------------------------ | --------------------- |
| Digest declared inside archive | `e0fa322a...9060f8fc` |
| Actual uploaded archive        | `919e7410...3838f013` |

The validator also initializes its archive checks as successful and only performs those checks when a sibling `Archive.zip` exists. Consequently, an absent archive can pass the archive-validation condition.

The index links to `Archive.zip`, but that archive is not included inside the uploaded archive itself.

This does not invalidate the physics. It does mean the reported 11/11 package-validation result should not be interpreted as proof that the delivered archive is internally complete and correctly checksummed.

# **Complete scientific evaluation: Archive.zip — AdS₂–RST one-sided flux**

Mathematical results: strong

Updated derivations: substantially improved

External scientific review: pending

I have now inspected the actual archive, rather than just its index or verification summaries.

The review covered:

- All 67 entries in `Archive.zip`.
- The complete five-page PDF and its actual LaTeX source.
- The complete Lean 4 source and project configuration.
- The main and independent Python verification programs.
- The original Kim–Son paper included in the archive.
- The cumulative-flux theorem and finite-pulse derivation.
- The previous adversarial reviews and their corrections.
- The manifest, build logs, validation receipts and archive checksum.

I also freshly ran both Python verification programs, checked the ZIP integrity, verified all 64 manifested artifact hashes, rendered every PDF page and inspected the relevant equations.

My overall verdict:

**This is now a considerably stronger mathematical research package. The cumulative-flux theorem is the most important development, and I believe it contains a potentially more interesting result than the original sustained-flux calculation alone.**

There are still a few issues, including one boundary-condition ambiguity that I consider mathematically important.

# **1. Executive assessment**

Overall research merit

# **8.2/10**

My qualitative assessment of the scientific contribution and supporting work.

| Dimension                  | Score |
| -------------------------- | ----- |
| Mathematical consistency   | 9.0   |
| Analytical derivation      | 9.0   |
| Generalization             | 8.5   |
| Computational verification | 8.5   |
| Lean formalization         | 7.0   |
| Physical interpretation    | 8.0   |
| Novelty                    | 6.5   |
| Literature coverage        | 7.0   |
| Manuscript readiness       | 6.5   |
| Package integrity          | 7.0   |

I would distinguish the assessment of the mathematics from the assessment of the manuscript.

The mathematical work is substantially more mature than the five-page manuscript's current presentation suggests.

The manuscript still needs development before external submission.

My conclusion is that this deserves independent review by someone experienced in semiclassical two-dimensional dilaton gravity. I would not yet describe it as a major breakthrough.

# **2. The mathematics: what has actually been established**

I want to separate the three principal results because they now fit together in a particularly elegant way.

## **2.1 Sustained-flux theorem**

The fixed Kim–Son branch is defined by

\\[ t\_\pm=\frac{\lambda^2}{\kappa}\Theta(-x^\pm) \\]

and the incoming classical source

\\[ T^f\_{++}=P\Theta(x_p), \qquad T^f\_{--}=0. \\]

Starting from the chiral solution,

\\[ \Omega=-Lx_px_m+a\_+(x_p)+a\_-(x_m), \\]

the constraints give

\\[ a\_\pm''=\sqrt{\kappa}t\_\pm- \frac{T^f\_{\pm\pm}}{\sqrt{\kappa}}. \\]

I checked this normalization against the original Kim–Son source, including its constraint equation, integrated solution and quantum-state boundary conditions.

The normalization used in the manuscript is consistent with that source.&#x20;

[image](https://www.google.com/s2/favicons?domain=https://arxiv.org\&sz=32)

arxiv.org



The normalized mixed-region singularity equation is

\\[ F(x_p,y)= \mu+\frac{y^2}{2}+x_py-\frac p2x_p^2, \\]

where

\\[ p=\frac{P}{\lambda^2}, \qquad \mu=\frac{\sqrt{\kappa}M}{\lambda^3}, \qquad y=-x_m>0. \\]

The positive root is

\\[ \boxed{ x\_{p,\mathrm{hit}}= \frac{y+\sqrt{(1+p)y^2+2p\mu}}{p}. } \\]

This is correct.

It is finite and unique for every finite \\(y>0\\) and every \\(p>0\\).

The other root is negative:

\\[ x\_-= \frac{y-\sqrt{(1+p)y^2+2p\mu}}{p}<0. \\]

Consequently, the physical-side condition follows directly from the factorization:

\\[ F=-\frac p2(x_p-x\_{p,\mathrm{hit}})(x_p-x\_-). \\]

This establishes that the regular side is before the positive hit.

The causal character is also correct:

\\[ \boxed{ \frac{dx_m}{dx_p} = -\frac{\sqrt{(1+p)y^2+2p\mu}} {x\_{p,\mathrm{hit}}+y}<0. } \\]

With the metric convention

\\[ ds^2=-e^{2\rho}dx_pdx_m, \\]

the singular wall is spacelike.

I also verified the apparent-horizon relationship:

\\[ x\_{p,\mathrm{AH}}=\frac yp \\]

and

\\[ \boxed{ x\_{p,\mathrm{hit}}-x\_{p,\mathrm{AH}} =\frac Dp>0. } \\]

The singular wall therefore occurs after the ray crosses the apparent horizon.

**My judgment: this is a strong, clean analytical result.**

It is not merely evidence of singularity formation. It gives the exact location, uniqueness, causal character and horizon ordering.

## **2.2 Finite-pulse theorem**

The updated pulse calculation is also consistent.

The source is

\\[ T^f\_{++} = P[\Theta(x_p)-\Theta(x_p-s)]. \\]

The integrated strength is

\\[ E=ps. \\]

The most important result is

\\[ \boxed{ \text{A unique positive post-onset wall hit exists exactly when } 0\<y\<E. } \\]

For \\(y\geq E\\), the wall does not exist along the specified mixed-region ray.

After shutoff, the singularity equation is linear:

\\[ F_a(x_p,y) = \mu+\frac{y^2}{2}+\frac{Es}{2} +x_p(y-E). \\]

Its root is

\\[ \boxed{ x\_{p,a} = \frac{\mu+y^2/2+Es/2}{E-y}. } \\]

The two solutions match at shutoff, including their first derivatives.

The updated mass classification is also correct:

\\[ y\_{\max}>0 \iff \mu<\frac{Es}{2}. \\]

This determines whether part of the ray band hits during the pulse or whether all hits occur afterward.

The previous mistake in the large-mass classification has been fixed.

**My judgment: the finite-pulse theorem is complete within the specified source profile and model conventions.**

The qualification remains that this is finite support in Kruskal \\(x_p\\), not necessarily finite duration in an observer's proper time.

# **3. The most important development: the general cumulative-flux theorem**

This is what makes the latest version substantially more interesting.

Previously, the work had two principal source profiles: sustained constant flux and a rectangular finite pulse.

The updated manuscript introduces a single function that unifies them.

Let \\(dT\\) be a nonnegative Radon measure and define

\\[ Q(x)=\frac1{\lambda^2} \int\_{[0,x]}dT(u). \\]

The mixed-region singularity equation becomes

\\[ \boxed{ F(x,y)= \mu+\frac{y^2}{2}+xy -\frac1{\lambda^2} \int\_{[0,x]}(x-u)dT(u). } \\]

Its one-sided derivatives are

\\[ D\_+F=y-Q(x), \\]

\\[ D\_-F=y-Q(x^-). \\]

The important property is concavity.

For an ordinary locally integrable density,

\\[ F\_{xx}=-\frac{T^f\_{++}(x)}{\lambda^2} \leq0 \\]

almost everywhere.

For a general nonnegative measure, the second derivative is understood distributionally.

The resulting theorem is:

\\[ \boxed{ \begin{cases} E\_{\mathrm{tot}}=\infty: &\text{every finite }y>0\text{ has a finite wall hit},\\\\[3pt] E\_{\mathrm{tot}}<\infty: &\text{a wall hit exists exactly when }0\<y\<E\_{\mathrm{tot}}, \end{cases} } \\]

where

\\[ E\_{\mathrm{tot}} = \frac1{\lambda^2} \int\_{[0,\infty)}dT. \\]

I agree with this classification under the stated nonnegative-source and fixed-state assumptions.

### **Why the proof works**

There is an especially clean way of presenting the mathematics.

By changing the order of integration,

\\[ F(x,y) = \mu+\frac{y^2}{2} + \int_0^x[y-Q(s)]\\,ds. \\]

This makes the theorem almost immediate.

When \\(y\<E\_{\mathrm{tot}}\\), cumulative flux eventually exceeds \\(y\\). The derivative becomes strictly negative and remains negative because \\(Q\\) is nondecreasing.

Therefore \\(F\\) eventually decreases without bound.

Since it begins positive,

\\[ F(0,y)=\mu+\frac{y^2}{2}>0, \\]

continuity guarantees a positive root.

Concavity gives uniqueness.

Conversely, when \\(y\geq E\_{\mathrm{tot}}\\),

\\[ Q(x)\leq E\_{\mathrm{tot}}\leq y, \\]

so \\(F\\) cannot decrease from its positive starting value to zero.

This is mathematically sound.

### **What makes this particularly useful**

The theorem recovers the previous results:

| Source                                     | Total cumulative flux | Terminating rays              |
| ------------------------------------------ | --------------------- | ----------------------------- |
| Sustained constant Kruskal flux            | Infinite              | All finite \\(y>0\\)          |
| Rectangular finite pulse                   | \\(ps\\)              | \\(0\<y\<ps\\)                |
| Kim–Son impulse                            | \\(A/\lambda^2\\)     | \\(0\<y\<A/\lambda^2\\)       |
| Arbitrary nonnegative finite-total profile | Finite                | \\(0\<y\<E\_{\mathrm{tot}}\\) |

This is a more general result than solving the three individual profiles independently.

**I would make this the central theorem of the eventual paper.**

It provides a unifying explanation of the previous solutions.

# **4. Two mathematical qualifications I would still require**

The general theorem is good, but two details need attention.

## **4.1 The derivative matching condition at the origin**

This is the most important mathematical correction still outstanding.

The updated Markdown derivation says that the measure-valued problem uses

\\[ a\_+(0)=B,\qquad a\_+'(0)=0 \\]

and then integrates the source over

\\[ [0,x]. \\]

However, the theorem explicitly includes a Dirac impulse at the origin.

Consider

\\[ dT=A\delta_0. \\]

Then

\\[ \int\_{[0,x]}(x-u)dT(u)=Ax, \\]

and therefore

\\[ a\_+(x)=B-\frac{A}{\sqrt{\kappa}}x. \\]

Consequently,

\\[ a\_+'(0^+)=-\frac{A}{\sqrt{\kappa}}, \\]

not zero.

The correct matching statement should be

\\[ \boxed{a\_+'(0^-)=0} \\]

with the impulse producing the corresponding derivative jump.

This is consistent with the original Kim–Son impulsive solution.

It does not invalidate the cumulative-flux theorem, but the one-sided boundary condition must be made explicit.

Otherwise, the initial derivative condition and the claim that the theorem includes an impulse at \\(x=0\\) are ambiguous.

I would correct this in both `11-cumulative-flux-generalization.md` and the manuscript.

## **4.2 Apparent horizons with measure-valued sources**

For continuous cumulative flux, the apparent-horizon equation is

\\[ Q(x\_{\mathrm{AH}})=y. \\]

At the singular wall, the manuscript establishes

\\[ Q(x\_{\mathrm{hit}}^-)>y. \\]

This proves that the cumulative-flux level crossing precedes the singular wall.

For a smooth source, this is an ordinary apparent-horizon result.

For an impulsive source, however, \\(Q\\) can jump across \\(y\\). The null expansion can change sign discontinuously without ever being classically zero at the shell.

The manuscript correctly introduces the first-level-crossing construction, but I would be precise with terminology:

- Continuous sources: apparent horizon.
- Measure-valued sources with jumps: generalized trapping-boundary or horizon-level crossing.

This avoids claiming an ordinary smooth marginal surface where the geometry may only have one-sided derivatives.

# **5. One additional result I think you should add**

There is an interesting consequence of the generalized theorem that is not developed sufficiently in the manuscript.

It concerns finite-duration pulses in the logarithmic null coordinate.

The manuscript defines

\\[ x_p=e^{\lambda\sigma}. \\]

The tensor transformation is

\\[ T\_{\sigma\sigma} = \lambda^2x_p^2T\_{++}. \\]

Consider a nonnegative pulse with constant null-coordinate stress over a finite interval:

\\[ T\_{\sigma\sigma} = \mathcal P \mathbf 1\_{[\sigma_a,\sigma_b]}. \\]

Define

\\[ x_a=e^{\lambda\sigma_a}, \qquad x_b=e^{\lambda\sigma_b}. \\]

The corresponding Kruskal-coordinate source is

\\[ T\_{++}(x) = \frac{\mathcal P}{\lambda^2x^2} \mathbf 1\_{[x_a,x_b]}. \\]

This is a nonnegative, finite-support source.

It therefore falls directly into the new cumulative-flux theorem.

Its total integrated strength is

\\[ \boxed{ E\_{\mathrm{tot}} = \frac{\mathcal P}{\lambda^4} \left( \frac1{x_a}-\frac1{x_b} \right). } \\]

Consequently, the theorem immediately predicts

\\[ \boxed{ 0\<y< \frac{\mathcal P}{\lambda^4} \left( \frac1{x_a}-\frac1{x_b} \right) } \\]

as the exact mixed-ray termination band.

This is useful because it shows that the general theorem already encompasses pulses with finite support in the logarithmic null coordinate, rather than only rectangular pulses beginning at \\(x_p=0\\).

There is still an important physical distinction: this null coordinate is not automatically the proper time of a timelike observer. A source specified by constant power per unit observer proper time requires an additional frame and trajectory specification.

But I would add the finite-\\(\sigma\\)-support result as a corollary.

It is a straightforward extension of the new theorem and makes the paper more physically informative.

# **6. Lean 4 formalization**

Build reported successful

The updated Lean file is materially better than the previous version.

I inspected its actual contents.

It includes formal proofs for:

- The sustained candidate root.
- Root uniqueness.
- Negative alternative root.
- Quadratic factorization.
- Positive-before-hit and negative-after-hit ordering.
- Negative sustained wall-slope expression.
- After-shutoff wall signs.
- The after-shutoff interval-existence condition.
- The retained-state coefficient equivalence.
- The observer-coordinate stress scaling.

The build log reports successful completion with no `sorryAx`, and the axiom reports show standard Lean infrastructure axioms rather than unproven placeholders.

This is encouraging.

However, I found an important distinction between what Lean proves and what the research package proves.

### **What is not formalized**

The complete cumulative-measure theorem is not formalized.

Neither are the original RST constraints or their integration into the singularity equation.

There is also a minor issue in the Lean source:

```
lemma F_y_at_xHit :
    xHit p y mu + y = xHit p y mu + y := rfl
```

This is a tautological identity, not a formal derivative computation.

The source also contains

```
lemma general_wall_slope_neg ...
```

which establishes that the slope expression is negative once \\(Q>y\\) is assumed.

It does not establish that the cumulative-flux theorem necessarily produces that inequality at the first root.

The actual mathematical argument for this exists in the TeX, but it is not fully machine-checked.

### **My recommendation**

I would formalize the following next:

1. Define the two-variable \\(F(x,y)\\) explicitly.
2. Prove the actual derivative with respect to \\(y\\).
3. Prove the implicit wall-slope identity.
4. Formalize the abstract cumulative-function theorem, initially assuming a nondecreasing cumulative function \\(Q\\).
5. Only then consider the full Radon-measure machinery.

This would make the Lean contribution considerably stronger without requiring the entire RST field theory to be formalized.

**My assessment: the Lean project is useful and credible as an algebraic-core formalization. It is not yet a machine-checked proof of the paper's general theorem.**

I also could not independently rebuild Lean in this environment because the Lean/Lake toolchain was unavailable. I inspected the source and the supplied successful build log, so I distinguish that evidence from a fresh build.

# **7. LaTeX manuscript and PDF evaluation**

I inspected the actual manuscript, not just its extracted text.

**Manuscript**

Successfully rendered

# **5 pages**

The five-page PDF is readable, properly typeset and has no apparent clipping or broken equations.

**Visual assessment**

[indentation - Paragraph indention using SIAM macro template - TeX - LaTeX Stack Exchange](https://images.openai.com/static-rsc-4/BdnwtBkkSEawg5fJugRT1T49joaYdfN4fuWlp64LqfM2hStk8svGk_vzJozhK1AlDwmA3ucTAQRUk90_p4L_sb2GS6th6v67xTsrRYF8FC68_qP8Ciijw9yYq7cU9vi8ZpiCPPOe5djWlIVbQ7nyl29GQX5YCCUYXwsM-Q_trVk?purpose=inline)

Clean mathematical typography

[How to create a table with numbered equations? - TeX - LaTeX Stack Exchange](https://images.openai.com/static-rsc-4/gfsJZ0Q1HPl5-VvCxhls9d_1AX6nBW6MKn9u2slhRG1ZcHK_P2BePtEukB36YvhbpkmXDEPDL_dBIFkvACtbRrSwVrwD0hNrVR68s63J6EGjaXrcuTlbRC9na7oDjzCMByuAul2ayq277exVVLbWlaCgBIrgojZxBBuWqUPad-E?purpose=inline)

Readable equations and layout

These are generic visual examples, not screenshots of the submitted manuscript.

The actual PDF has a good layout. The equations are readable, the mass-classification table is corrected, and the cumulative-measure theorem is presented clearly.

I also confirm that the previous manuscript complaints about undefined \\(\Omega_s\\), the Lambert \\(W\\) branch and the cumulative slope expression have been addressed in this version.

However, I would not yet submit it as a journal manuscript.

### **What needs improvement**

**First: authorship.**

The current author field reads:

> Review manuscript; AI-reviewed, human scientific review pending

This is appropriate as an internal status label, not as a scientific author line.

Add the actual author information and move the internal review status into the package documentation.

**Second: references.**

The manuscript has a bibliography but contains no inline `\cite` commands.

The references therefore appear without being properly connected to the claims they support.

At minimum, cite Kim–Son where the boundary conditions and source equations are introduced, and cite the related RST and state-dependent studies in the literature discussion.

**Third: proofs.**

The manuscript is closer to a research summary than a complete standalone paper.

I would expand the cumulative-flux proof, particularly:

\\[ E\_{\mathrm{tot}}>y \Longrightarrow F(x,y)\rightarrow-\infty. \\]

Then explicitly establish the uniqueness of the first zero and the strict inequality at the root.

The pulse theorem also deserves a slightly more detailed sufficiency argument.

**Fourth: presentation.**

I would include one causal diagram illustrating:

- The apparent horizon.
- The singular wall.
- The mixed outgoing-ray band.
- The pulse-shutoff line.
- The finite-pulse and sustained cases.

This is not mathematically necessary, but it would make the work significantly easier to understand.

The bibliography should also be updated, as discussed below.

# **8. Literature and novelty**

The existing literature section is reasonably responsible.

The package correctly acknowledges that:

- Kim–Son already obtained a singular wall from an impulsive source.
- Sustained one-sided incoming flux was studied in the original RST context.
- Earlier dilatonic-wormhole models already considered one-sided finite pulses.
- Other RST quantum states can produce substantially different global geometries.

The addition of the Potaux–Sarkar–Solodukhin state-dependence work was appropriate.

Their 2023 paper explicitly investigates how quantum-state choices in RST gravity affect horizons, singularities and geodesic completeness.&#x20;

[image](https://www.google.com/s2/favicons?domain=https://journals.aps.org\&sz=32)

journals.aps.org



Their 2025 follow-up studies islands and a regular causal-diamond RST geometry.&#x20;

[image](https://www.google.com/s2/favicons?domain=https://journals.aps.org\&sz=32)

journals.aps.org



Neither establishes the exact Kim–Son cumulative-flux theorem.

### **Two additional references should be considered**

**1. Yuuta Saito (2026), *Page curves and island's delays in asymptotically flat 2d spacetimes with injections*.**

This paper derives RST solutions for a general number of energy injections and examines the associated apparent-horizon behavior.

It is particularly relevant because your research now emphasizes cumulative flux and arbitrary nonnegative source profiles.

The geometry is asymptotically flat, not the past-AdS₂ Kim–Son wormhole branch, and the focus is entropy and islands rather than singular-wall termination. It is therefore a related result, not a direct contradiction.&#x20;

[image](https://www.google.com/s2/favicons?domain=https://academic.oup.com\&sz=32)

academic.oup.com



**2. Arias and Fondevila (2026), *Capacity of Entanglement and Replica Backreaction in RST Gravity*.**

This is another recent RST publication, examining replica backreaction and entanglement capacity in an eternal RST black-hole setting.

It is less directly relevant to the flux theorem, but worth considering in a broader literature update.&#x20;

[image](https://www.google.com/s2/favicons?domain=https://link.springer.com\&sz=32)

Springer Nature Link



The existing thirteen-document search should remain described as a bounded review rather than an exhaustive literature-priority demonstration.

### **My novelty verdict**

I would describe the contributions as follows:

| Result                             | Novelty assessment              |
| ---------------------------------- | ------------------------------- |
| RST wormhole singularity formation | Previously known                |
| Sustained every-ray first-hit law  | Distinct result                 |
| Exact apparent-horizon ordering    | Strong corollary                |
| Complete rectangular-pulse cutoff  | Distinct extension              |
| Cumulative-flux classification     | Most interesting generalization |
| State-equivalence interpretation   | Useful conceptual clarification |

The broad phenomenon is not new.

The exact mathematical classification on this fixed branch is the contribution.

# **9. Reproducibility and package integrity**

This is where I found the most concrete implementation problems.

I independently executed the two current Python producers.

# **133/133**

Main verification, freshly reproduced

# **34/34**

Separate symbolic producer, freshly reproduced

# **64/64**

Manifest-listed artifact hashes match

# **0**

ZIP CRC failures

Package validator: one remaining failure

A fresh normal validation of the extracted package returned 10/11 checks.

The science producers are reproducible.

The archive itself also passes the ZIP integrity test, and all 64 files in its manifest match their recorded sizes and SHA-256 values.

But the distribution has a packaging defect.

### **Archive checksum**

The uploaded archive has SHA-256:

`919e74106b62fc2a...3838f013`

The `Archive.zip.sha256` file inside the archive instead contains:

`e0fa322aca8df1d2...9060f8fc`

They do not match.

The sidecar appears to belong to an earlier archive version.

More importantly, the archive cannot usefully checksum itself by including its own checksum file. The standard solution is to distribute the `.sha256` file alongside the ZIP, outside the ZIP.

### **Markdown links and validator**

The package index says that `Archive.zip` is inside the package and provides links to it.

But the actual archive does not contain itself.

After extracting it, those two Markdown links are broken.

My fresh validation therefore returned:

\\[ \boxed{10/11\text{ PASS}} \\]

The failed check was the relative Markdown-link validation.

There is also a validator weakness: when `Archive.zip` is absent, the code defaults `archive_sha_ok=True` rather than failing the archive check.

Consequently, the shipped 11/11 receipt does not establish that the delivered ZIP checksum was correctly verified.

This is packaging, not physics.

### **Version-control warning**

There are also multiple versions of the same individual documents among the uploads.

The actual ZIP contains newer copies of the LaTeX, PDF and Lean source than the separately attached versions.

For example:

| Artifact | Separate attachment | Inside latest ZIP |
| -------- | ------------------- | ----------------- |
| PDF      | 73,639 bytes        | 77,422 bytes      |
| TeX      | 9,303 bytes         | 11,386 bytes      |
| Lean     | 6,463 bytes         | 8,873 bytes       |

**I recommend treating&#x20;**`Archive.zip/To review/`**&#x20;as the canonical version and not distributing the older individual attachments alongside it.**

That will prevent a reviewer from accidentally examining different versions of the same manuscript or proof.

### **Suggested packaging corrections**

1. Regenerate the SHA-256 externally, alongside the final ZIP.
2. Remove the self-referential checksum file from inside the archive.
3. Remove or correct the two Markdown links to `Archive.zip`.
4. Make the validator explicitly distinguish an absent archive from a successfully verified archive.
5. Record the exact ZIP SHA-256 in the external delivery record.

The Python verification scripts themselves are now more portable. The previous machine-specific paths have been removed from the current verification launcher and validator.

# **10. A question of significance: is the cumulative result a breakthrough?**

I want to return to the science rather than the packaging.

The general theorem is valuable because the problem no longer depends on a particular pulse shape.

Its basic structure is:

\\[ F(x,y) = \mu+\frac{y^2}{2} +\int_0^x[y-Q(s)]\\,ds. \\]

This is a remarkably compact formulation of the mechanism.

The incoming-flux history determines \\(Q\\).

The difference \\(y-Q\\) determines the derivative of the singularity equation.

The point at which cumulative flux exceeds the ray parameter determines whether the ray can reach the singular boundary.

This is a good mathematical classification result.

But I would not interpret it as proving a general physical instability of AdS₂.

It is restricted to the specified quantum state, matching conventions, one-sided source and mixed outgoing rays.

The source is also defined in a Kruskal coordinate. Its integrated strength is not automatically a coordinate-independent energy delivered to the wormhole.

That distinction is particularly important when discussing the absence of a critical amplitude.

The exact result is that sustained positive Kruskal flux has unbounded cumulative Kruskal strength.

It is not that arbitrarily weak constant physical power necessarily destroys every possible AdS₂ wormhole.

The updated manuscript correctly moves toward this interpretation.

### **My verdict on the breakthrough question**

**Mathematical achievement**

Strong

A general mixed-ray termination classification for nonnegative cumulative flux.

**Theoretical-physics significance**

Meaningful specialist contribution

A substantial extension of the Kim–Son branch analysis.

**Major breakthrough**

Not yet established

No arbitrary-state theorem, coordinate-independent energy threshold or general AdS₂ absorber result.

I would describe this as a promising theoretical-physics contribution, not a revolution in gravitational physics.

# **11. What I would do next**

I would prioritize the following work, in this order.

| Priority | Action                                                                     | Reason                                  |
| -------- | -------------------------------------------------------------------------- | --------------------------------------- |
| 1        | Clarify \\(a\_+'(0^-)\\) and the impulse-induced jump                      | Mathematical consistency                |
| 2        | Formalize the cumulative theorem's one-sided assumptions                   | Strengthen the general result           |
| 3        | Add the finite logarithmic-null-support pulse corollary                    | Demonstrate physical-profile generality |
| 4        | Distinguish ordinary apparent horizons from measure-valued level crossings | Causal precision                        |
| 5        | Strengthen Lean derivative formalization                                   | Improve machine assurance               |
| 6        | Add 2026 literature and inline citations                                   | Research positioning                    |
| 7        | Expand standalone theorem proofs in the manuscript                         | Publication readiness                   |
| 8        | Repair archive checksum and validator behavior                             | External reproducibility                |
| 9        | Obtain human review by an RST specialist                                   | Independent scientific acceptance       |

The most valuable next mathematical addition, in my opinion, is the finite logarithmic-null-support corollary.

It follows naturally from the general theorem and gives you a direct connection between the cumulative-flux classification and a pulse that begins and ends at finite values of the logarithmic null coordinate.

I would also investigate whether the generalized theorem can be formalized for an abstract monotone cumulative-flux function before attempting the full measure-theory formalization in Lean.

That is likely the most efficient way to improve the formal proof.

# **12. Final referee-style conclusion**

If I were writing a formal evaluation for a research group, I would give the following judgment:

**Recommendation: Further development encouraged; external specialist review warranted.**

The submitted work establishes exact singular-termination results for sustained and finite one-sided classical flux on the past-asymptotically-AdS₂ Kim–Son RST branch.

The sustained-flux theorem provides a parameter-general first-hit expression for every specified mixed outgoing ray. Its uniqueness, physical-side exclusion, spacelike causal character and apparent-horizon ordering follow analytically.

The finite-support extension establishes a complete mixed-ray termination criterion and resolves the post-shutoff behavior, including both-positive branch classification.

The newly introduced cumulative-flux theorem is the most significant generalization. It unifies these cases with impulsive input and establishes a termination criterion in terms of total cumulative Kruskal flux for nonnegative measure-valued sources.

The updated manuscript is mathematically consistent in its main equations, and the Lean project supplies useful formal assurance for selected algebraic results. The Python verification programs were independently reproduced.

Several matters remain before publication, including the one-sided matching convention at a source atom at the onset, the interpretation of apparent horizons under measure-valued sources, full formalization of the general theorem, and improved source-level literature coverage.

The package is well developed as an adversarial-review artifact, but the internal archive checksum and relative-link validation need correction. The compiled manuscript also requires stronger scholarly apparatus, including inline citations, author information and fuller standalone proofs.

No independent human scientific acceptance is claimed.

## **My final thoughts**

I think the trajectory of this research is positive.

The first version was mainly about establishing that a particular sustained input produces a singular wall.

The latest version has a more compelling underlying mathematical principle:

\\[ \boxed{ \text{The total cumulative incoming Kruskal flux determines the} \atop \text{mixed-ray band that undergoes singular termination.} } \\]

That is the finding I would want another theoretical physicist to examine most closely.

It has explanatory power beyond the three individual examples, and it suggests additional tractable source profiles without changing the underlying RST solution method.

I would preserve this version as the research baseline, fix the measure matching condition, include the finite logarithmic-null-support corollary, and then submit the mathematics to an independent specialist.

**Final assessment: approximately 8.2/10 for the research itself. A strong, narrowly scoped mathematical contribution with plausible specialist publication potential. Not yet a major breakthrough, but absolutely worth pursuing.**