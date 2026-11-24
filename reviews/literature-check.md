# Bounded primary-literature check: constant one-sided flux on the Kim–Son RST wormhole branch

**Verdict (checked 2026-11-23).** I fetched and inspected 13 full-text primary documents, reading the relevant flux, solution, singularity, and bibliography sections: the Kim–Son paper and its same-model follow-up, the topically relevant forward citation, earlier dilatonic-wormhole work, general-flux RST papers, and constant-flux moving-mirror papers. **The exact constant-\(P\), one-sided, every-ray first-hit formula specified below was not found in this searched corpus.** This is a bounded absence-of-evidence result, not a claim of exhaustive novelty.

A broader claim that sustained or constant one-sided flux had never been treated would be false: the original RST paper has a sustained subcritical incoming flux, and Hayward–Kim–Lee has a one-sided step pulse through a classical dilatonic wormhole. Neither is the constant-Kruskal-\(P\) drive on the past-asymptotically-AdS\(_2\) Kim–Son branch.[12][8]

## Exact target used for the comparison

To make the found/not-found statement precise, take the Kim–Son \(t_\pm\) branch and replace its shock by
\[
T^f_{++}=P\,\theta(X),\qquad T^f_{--}=0,\qquad P>0,\qquad X=x^+-x_0,\quad z=x^--x_0 .
\]
Write \(\Omega_c=(\sqrt\kappa/4)[1-\ln(\kappa/4)]\). Direct integration of Kim–Son Eq. (2.13), using their Eq. (2.15), gives the first \(\Omega=\Omega_c\) intersection along each fixed-\(x^-\) null ray as follows.[2]
\[
\boxed{\;
X_s(z)=\frac{-\lambda^2z+\sqrt{\lambda^4z^2+P\lambda^2z^2\,\mathbf 1_{z<0}+2P\sqrt\kappa\,M/\lambda}}{P},\qquad z\in\mathbb R .\;}
\]
Here \(x^+_s=x_0+X_s(z)\). For \(z<0\), the radicand is \(\lambda^2(\lambda^2+P)z^2+2P\sqrt\kappa M/\lambda\); for \(z\geq0\), it is \(\lambda^4z^2+2P\sqrt\kappa M/\lambda\). For \(M>0\), the root is positive, finite, and continuous at \(z=0\). For \(M=0\) and \(z\geq0\), it degenerates to onset contact \(X_s=0\), not a strictly positive post-onset root. This displayed target is my notation-fixing substitution, **not a quotation from the literature**. Symbolic substitution checks gave zero residual in both regions; \(X_s(0)=\sqrt{2\sqrt\kappa M/(\lambda P)}\), while \(X_s z\to\sqrt\kappa M/\lambda^3\) as \(z\to+\infty\).

## Verified primary-source findings

1. **Kim–Son, *Wormhole phase in the RST model*, gr-qc/0404098v2 (JHEP 08 (2004) 006).** The arXiv record verifies authors Won Tae Kim and Edwin J. Son, v2 dated 2004-09-08, and DOI 10.1088/1126-6708/2004/08/006.[1] The infalling **classical** source immediately before Eq. (2.15) is an impulse, not a sustained flux:
   \[
   T^f_{++}=A\delta(x^+-x_0),\qquad T^f_{--}=0,
   \]
   with
   \[
   C_\pm=\lambda^2x_0/\sqrt\kappa,\qquad
   t_\pm(x^\pm)=(\lambda^2/\kappa)\theta(x_0-x^\pm) \tag{2.15}.
   \]
   The pre-shock static solution is Eq. (2.22),
   \[
   \Omega=\frac{M}{\lambda}+\frac{\sqrt\kappa}{4}\left(1-\ln\frac\kappa4\right)
   +\frac{\lambda^2}{2\sqrt\kappa}(x^+-x^-)^2,
   \]
   and the singularity condition following Eq. (2.19) is \(\Omega=\Omega_c\).[2]

   The same paper **does contain a constant one-sided quantum background** in the past. Section 3 gives
   \[
   \langle T^f_{--}\rangle_{\mathcal I^-_L}\longrightarrow-\lambda^2\theta(x_0-x^-),
   \]
   explicitly calls this background “not a real radiation,” and concludes: “at the past null infinities the geometry was AdS\(_2\), which is related to the fact that the energy momentum tensor is constant, \(-\lambda^2\) at \(\mathcal I^-_L\).”[2][5] This is prior constant negative quantum stress supporting the wormhole, **not** an arbitrary positive classical \(P\) inserted after \(x_0\), and the paper gives no all-ray first-hit root.

2. **Kim–Son–Yoon, *Exactly Soluble Quantum Wormhole in Two Dimensions*, gr-qc/0407106v2 (Phys. Rev. D 70, 104020).** Eq. (29) again uses \(t_\pm=\lambda^2/\kappa\); Eq. (31) adds finite-interval \(\beta_\pm\) corrections to restore the wormhole after a localized D-particle passes. Eq. (35) is the resulting time-dependent solution, and Eqs. (41)–(43) analyze singularity avoidance. The Discussion gives asymptotic quantum sources \(\langle T^f_{\pm\pm}\rangle\approx-\lambda^2\), later \(-\lambda^2(1+\beta_\pm)\). This is a different boundary-condition maintenance construction, not a one-sided classical constant-\(P\) collapse calculation; no every-ray hit formula appears.[3][4]

3. **Russo–Susskind–Thorlacius, *The Endpoint of Hawking Radiation*, hep-th/9206070.** Section 4 is genuine prior sustained one-sided RST input. Eq. (4.6) sets
   \[
   T_{++}(x^+)=\frac{\epsilon}{\lambda(x^+)^2}\,\theta(x^+-x^+_0),
   \qquad \epsilon<\kappa\lambda/4,
   \]
   and calls \(\epsilon\) “the constant energy flux”; Eq. (4.7) gives the exact logarithmic \(\Omega=\chi\) solution and the text divides rays by the critical line and constructs a reflecting static region.[12] The constancy is in the asymptotically flat energy coordinate: the Kruskal tensor falls as \((x^+)^{-2}\). The background is the linear-dilaton/asymptotically flat RST boundary problem, not Kim–Son’s AdS\(_2\) branch, and Eq. (4.7) is not the boxed algebraic every-ray root.

4. **Hayward–Kim–Lee, *Dilatonic wormholes: construction, operation, maintenance and collapse to black holes*, gr-qc/0110080.** Eq. (40) uses a finite one-sided step \(F_+=\Delta\) for \(0\leq x^+<x_0\), \(F_-=0\). During the pulse, Eq. (44) includes
   \[
   r=a+2\lambda^2(x^+-x^-)^2-\frac{\Delta^2}{2}(x^+)^2,
   \]
   and the text states that an arbitrarily weak pulse eventually produces a spatial \(r=0\) singularity.[8] This is the closest structural wormhole precursor found, but it is a **finite pulse in the classical CGHS-plus-ghost model**, not sustained constant \(P\) in quantum RST, and the authors do not print the boxed every-ray first-hit formula.

5. **Other constant/general-flux RST works checked.** Hawking’s *The Superscattering Matrix For Two Dimensional Black Holes* has static Euclidean solutions with “a constant positive flux of energy coming in at infinity and a similar flux going out,” hence balanced incoming/outgoing flux, not the one-sided Kim–Son drive.[6]

   Susskind–Thorlacius–Uglum’s *The Stretched Horizon and Black Hole Complementarity* considers constant incoming \(T_{++}(\sigma^+)=\bar T\) **of finite duration \(\tau\)**, with boundary result Eq. (3.34), again on the usual RST reflecting-boundary problem.[7]

   *Cosmic Censorship in Two-Dimensional Gravity* and Fabbri–Russo’s *Soluble models in 2d dilaton gravity* provide general incoming-matter solutions and singularity/boundary equations, but not the Kim–Son constant-\(P\) every-ray root.[16][15]

   Basavaraju–Lowe’s *Black hole mining in the RST model* treats general flux over finite intervals, assumes no flux after evaporation, and derives thunderpop/lifetime formulas rather than the branch-specific ray map.[10]

6. **Moving-mirror comparison.** Carlitz–Willey’s *Reflections on moving mirrors* explicitly chooses a trajectory generating constant flux (their Eq. (3.11)); Good–Linder’s *Möbius Mirrors* states it cleanly as \(p(u)=-e^{-\kappa u}/\kappa\) (Eq. (8)), with eternal outgoing thermal flux \(\mathcal F=\kappa^2/(48\pi)\) (Eq. (10)).[13][9] These are flat-space moving-boundary emission results, not incoming back-reaction on the Kim–Son wormhole, and contain no RST singularity first-hit formula.

7. **Forward-citation check.** The topically relevant citing paper located, Kim–Lee–Yeom’s *Black hole complementarity and firewall in two dimensions*, uses the usual single-shock asymptotically flat RST solution (its Eq. (14)); it does not extend the Kim–Son branch to constant \(P\) or give an every-ray first-hit map.[11] The other INSPIRE `refersto` return, *Near-horizon geometries of supersymmetric AdS(5) black holes*, was also fetched and checked; its full text has no RST/Kim–Son wormhole analysis relevant to the target.[14]

## Scope limit

The “not found” verdict covers only the 13 documents listed in Sources and their explicitly identified equation/statement locations. Full-text phrase scans for `first-hit`, `first hit`, `every ray`, `all rays`, and `constant-P` returned no hits; those scans supplemented, rather than replaced, reading the flux and singularity sections. Uncited papers, non-indexed work, alternate notation, and later work outside this bounded corpus remain unchecked.

## Sources

[1] https://arxiv.org/abs/gr-qc/0404098 — Wormhole phase in the RST model
[2] https://arxiv.org/pdf/gr-qc/0404098v2 — Wormhole phase in the RST model (v2 PDF)
[3] https://arxiv.org/abs/gr-qc/0407106 — Exactly Soluble Quantum Wormhole in Two Dimensions
[4] https://arxiv.org/pdf/gr-qc/0407106v2 — Exactly Soluble Quantum Wormhole in Two Dimensions (v2 PDF)
[5] https://ar5iv.labs.arxiv.org/html/gr-qc/0404098 — Wormhole phase in the RST model (ar5iv full text)
[6] https://arxiv.org/pdf/hep-th/9401109 — The Superscattering Matrix For Two Dimensional Black Holes
[7] https://arxiv.org/pdf/hep-th/9306069 — The Stretched Horizon and Black Hole Complementarity
[8] https://arxiv.org/pdf/gr-qc/0110080 — Dilatonic wormholes: construction, operation, maintenance and collapse to black holes
[9] https://arxiv.org/pdf/2108.07451 — Möbius Mirrors
[10] https://arxiv.org/pdf/1611.01758 — Black hole mining in the RST model
[11] https://arxiv.org/pdf/1301.5138 — Black hole complementarity and firewall in two dimensions
[12] https://arxiv.org/pdf/hep-th/9206070 — The Endpoint of Hawking Radiation
[13] https://jcsphysics.net/lit/carlitz1987a.pdf — Reflections on moving mirrors
[14] https://arxiv.org/pdf/0708.3695 — Near-horizon geometries of supersymmetric AdS(5) black holes
[15] https://arxiv.org/pdf/hep-th/9510109 — Soluble models in 2d dilaton gravity
[16] https://arxiv.org/pdf/hep-th/9209012 — Cosmic censorship in two-dimensional gravity
