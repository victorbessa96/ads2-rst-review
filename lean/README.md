# Lean verification

The project uses Lean 4.36.0 and Mathlib. `AdS2RST.lean` proves the algebraic core and the abstract continuous first-hit criterion:

- the sustained mixed-ray candidate root is a zero;
- every positive zero equals that candidate;
- the other root is negative;
- the mixed-wall tangent is negative;
- the quadratic factorization and positive-before/negative-after ordering;
- the derivative factors `F_x(xHit)=-D` and an actual `HasDerivAt` computation for `F_y`;
- the abstract signed first-hit criterion by the intermediate value theorem;
- the general cumulative slope sign once `Q(x_hit)>y`;
- the after-shutoff both-positive sign identity and interval existence condition;
- the reviewer's explicit `5/8` and `-1/10` sign controls;
- the retained-state `p_eff=1+p` coefficient identity and the small-`p` observer-coordinate stress scaling.

The file contains no `sorry` placeholders. Build with the pinned toolchain and downloaded Mathlib cache:

```bash
lake build
# Or, from the package root:
LAKE_BIN=/path/to/lake ./run_verification.sh
```

The build receipt is recorded in `outputs/lean-build.out` after running the command from this directory. The formal proof verifies the algebraic core, including root factor/sign ordering, derivative factors, state equivalence, stress scaling, and general slope sign. It does not formalize the full measure-theoretic cumulative theorem, an arbitrary-state absorber, or a future-boundary theorem.
