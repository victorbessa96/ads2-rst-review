#!/usr/bin/env python3
"""Structural checks: derivation from the constraints, global structure, clocks.

Every check here starts from the RST Kruskal-gauge equations, not from an
entered wall formula.  Symbolic checks use SymPy; asymptotic and affine-length
checks use mpmath with the exact Lambert-W inversion of Omega(phi).

Normalization.  L = lambda^2/sqrt(kappa), Omega = Omega_s + L*Fhat, where
Omega_s = (sqrt(kappa)/4)(1 - ln(kappa/4)) is the RST critical value.  The
chiral constraint in Kruskal gauge is
    kappa t_pm = sqrt(kappa) d_pm^2 Omega + T_pm pm ,
so ahat_pm'' = (kappa/lambda^2) t_pm - T_pm pm / lambda^2.
"""
from pathlib import Path
import json
import mpmath as mp
import sympy as sp

mp.mp.dps = 40
ROOT = Path(__file__).resolve().parent
OUT = ROOT / "outputs"
OUT.mkdir(exist_ok=True)
checks = []


def check(name, ok, detail="", group="structure"):
    row = {"name": name, "group": group, "status": "PASS" if bool(ok) else "FAIL", "detail": str(detail)}
    checks.append(row)
    print(f"{row['status']} | {name}" + (f" | {detail}" if detail else ""))


xp, xm = sp.symbols("x_p x_m", real=True)
lam, kap = sp.symbols("lambda kappa", positive=True)
mu, p, alpha, E, s, d = sp.symbols("mu p alpha E s d", positive=True)
L = lam**2 / sp.sqrt(kap)
Omega_s = sp.sqrt(kap) / 4 * (1 - sp.log(kap / 4))

# ---------------------------------------------------------------------------
# A. Field equations and constraints in Kruskal gauge (chi = Omega).
# ---------------------------------------------------------------------------
chi, Om = sp.Function("chi")(xp, xm), sp.Function("Omega")(xp, xm)
constraint_general = sp.sqrt(kap) * sp.diff(chi, xp, 2) - sp.diff(chi, xp) ** 2 + sp.diff(Om, xp) ** 2
check("A1 constraint reduces to sqrt(kappa) d^2 Omega in Kruskal gauge",
      sp.simplify(constraint_general.subs(chi, Om).doit() - sp.sqrt(kap) * sp.diff(Om, xp, 2)) == 0,
      "kappa t = sqrt(kappa) Omega'' + T", "derivation")

ap, am = sp.Function("a_p")(xp), sp.Function("a_m")(xm)
Omega_general = -L * xp * xm + ap + am
check("A2 general solution solves d_+ d_- Omega = -lambda^2/sqrt(kappa)",
      sp.simplify(sp.diff(Omega_general, xp, xm) + L) == 0, "", "derivation")

# Chiral profiles: the unique C^1 solutions of ahat'' = source with ahat(0)=ahat'(0)=0.
# State source theta(-x); sustained matter source p*theta(x).
z = sp.symbols("z", real=True)
u1, u2 = sp.symbols("u1 u2", real=True)


def integrate_twice(source_neg, source_pos):
    """Integrate a piecewise-constant-in-sign source twice from 0 on each side."""
    neg = sp.integrate(sp.integrate(source_neg.subs(z, u1), (u1, 0, u2)), (u2, 0, z))
    pos = sp.integrate(sp.integrate(source_pos.subs(z, u1), (u1, 0, u2)), (u2, 0, z))
    return sp.expand(neg), sp.expand(pos)


state_neg, state_pos = integrate_twice(sp.Integer(1), sp.Integer(0))
check("A3 state profile from t = (lambda^2/kappa) theta(-x)",
      state_neg == z**2 / 2 and state_pos == 0, f"x<0: {state_neg}; x>0: {state_pos}", "derivation")
flux_neg, flux_pos = integrate_twice(sp.Integer(0), -p)
check("A4 sustained matter profile from T_++ = p lambda^2 theta(x)",
      flux_neg == 0 and sp.simplify(flux_pos + p * z**2 / 2) == 0, f"x>0: {flux_pos}", "derivation")
check("A5 profiles are C^1 at the onset point",
      all(e.subs(z, 0) == 0 and sp.diff(e, z).subs(z, 0) == 0 for e in (state_neg, state_pos, flux_neg, flux_pos)),
      "value and first derivative vanish on both sides", "derivation")

# The four sectors assembled from the derived profiles.
a_plus = {"neg": state_neg.subs(z, xp), "pos": (state_pos + flux_pos).subs(z, xp)}
a_minus = {"neg": state_neg.subs(z, xm), "pos": state_pos.subs(z, xm)}
sector = {(i, j): sp.expand(mu - xp * xm + a_plus[i] + a_minus[j]) for i in ("neg", "pos") for j in ("neg", "pos")}
check("A6 pre-onset sector is the static wormhole",
      sp.simplify(sector[("neg", "neg")] - (mu + (xp - xm) ** 2 / 2)) == 0, sector[("neg", "neg")], "derivation")
check("A7 mixed sector formula",
      sp.simplify(sector[("pos", "neg")] - (mu - xp * xm + xm**2 / 2 - p * xp**2 / 2)) == 0, sector[("pos", "neg")], "derivation")
check("A8 both-positive sector formula",
      sp.simplify(sector[("pos", "pos")] - (mu - xp * xm - p * xp**2 / 2)) == 0, sector[("pos", "pos")], "derivation")

# Kim-Son's printed solution with onset at x0 and an impulse A, re-derived with constants.
x0, A, Dc, M = sp.symbols("x_0 A D M", real=True)
theta = sp.Heaviside
KS_printed = (M / lam + Omega_s - L * (xp - x0) * (xm - x0) - A / sp.sqrt(kap) * (xp - x0) * theta(xp - x0)
              + L / 2 * (x0 - xp) ** 2 * theta(x0 - xp) + L / 2 * (x0 - xm) ** 2 * theta(x0 - xm))
ok = True
for sp_sign, sm_sign in ((-1, -1), (1, -1), (-1, 1), (1, 1)):
    cp = sp.Integer(1) if sp_sign < 0 else sp.Integer(0)
    cm = sp.Integer(1) if sm_sign < 0 else sp.Integer(0)
    a_p = sp.integrate(sp.integrate(cp, (u1, x0, u2)), (u2, x0, xp)) - (A / lam**2) * (xp - x0) * (1 - cp)
    a_m = sp.integrate(sp.integrate(cm, (u1, x0, u2)), (u2, x0, xm))
    derived = M / lam + Omega_s + L * (-(xp - x0) * (xm - x0) + a_p + a_m)
    printed = KS_printed.subs({theta(xp - x0): 1 - cp, theta(x0 - xp): cp, theta(x0 - xm): cm})
    ok = ok and sp.simplify(derived - printed) == 0
check("A9 Kim-Son printed impulsive solution follows from the constraints in all four sectors", ok,
      "C_pm = lambda^2 x0/sqrt(kappa), D fixed by M", "derivation")

# ---------------------------------------------------------------------------
# B. Zero classical flux: the retained state alone gives a black hole.
# ---------------------------------------------------------------------------
post0 = sector[("pos", "pos")].subs(p, 0)
mixed0 = sector[("pos", "neg")].subs(p, 0)
check("B1 zero-flux both-positive sector is mu - x_p x_m", sp.simplify(post0 - (mu - xp * xm)) == 0, post0, "zero-flux")
check("B2 zero-flux wall is the hyperbola x_p x_m = mu", sp.solve(post0, xm) == [mu / xp], "x_m = mu/x_p", "zero-flux")
check("B3 both-positive quadrant is trapped at zero flux",
      sp.diff(post0, xp) == -xm and sp.diff(post0, xm) == -xp, "d_+ = -x_m < 0, d_- = -x_p < 0", "zero-flux")
yy, xx = sp.symbols("y x", positive=True)
check("B4 zero-flux mixed sector is regular",
      (mixed0.subs({xm: -yy, xp: xx})).is_positive is True, mixed0.subs({xm: -yy, xp: xx}), "zero-flux")
check("B5 without the state switch-off the wormhole is eternal and regular",
      sp.simplify(sector[("neg", "neg")] - mu - (xp - xm) ** 2 / 2) == 0, "Fhat >= mu > 0 on the whole plane", "zero-flux")
slope0 = sp.diff(mu / xp, xp)
check("B6 zero-flux wall is spacelike", sp.simplify(slope0 + mu / xp**2) == 0, "dx_m/dx_p = -mu/x_p^2 < 0", "zero-flux")

# Hartle-Hawking identification: t_pm = 0 static RST black hole; linear dilaton vacuum has t = 1/(4x^2).
M_bh = sp.symbols("M_bh", positive=True)
Omega_bh = -L * xp * xm + M_bh / (lam * sp.sqrt(kap))
check("B7 both-positive sector equals the t=0 static RST black hole",
      sp.simplify((Omega_s + L * post0) - Omega_bh.subs(M_bh, lam * sp.sqrt(kap) * (Omega_s + L * mu))) == 0,
      "M_bh/(lambda sqrt(kappa)) = Omega_s + M/lambda", "zero-flux")
xpp, xmn = sp.symbols("x_pp x_mn", positive=True)  # x_p > 0, x_m = -x_mn < 0
Omega_ldv = L * xpp * xmn - sp.sqrt(kap) / 4 * sp.log(lam**2 * xpp * xmn)
check("B8 linear dilaton vacuum has t_+ = 1/(4 x_p^2), so t = 0 is not the vacuum",
      sp.simplify(sp.sqrt(kap) * sp.diff(Omega_ldv, xpp, 2) / kap - 1 / (4 * xpp**2)) == 0,
      "kappa t_+ = sqrt(kappa) d_+^2 Omega", "zero-flux")

# ---------------------------------------------------------------------------
# C. Symmetries.  A symmetry preserves Omega and the metric, which forces
#    xi = (a + c x_p) d_p + (b - c x_m) d_m.
# ---------------------------------------------------------------------------
a, b, c = sp.symbols("a b c", real=True)


def symmetries(expr):
    res = sp.expand((a + c * xp) * sp.diff(expr, xp) + (b - c * xm) * sp.diff(expr, xm))
    return sp.solve(sp.Poly(res, xp, xm).coeffs(), [a, b, c], dict=True)


check("C1 pre-onset wormhole: translation only", symmetries(sector[("neg", "neg")]) == [{a: b, c: 0}],
      symmetries(sector[("neg", "neg")]), "symmetry")
check("C2 zero-flux mixed sector: no symmetry", symmetries(mixed0) == [{a: 0, b: 0, c: 0}], symmetries(mixed0), "symmetry")
check("C3 zero-flux both-positive sector: boost only", symmetries(post0) == [{a: 0, b: 0}], symmetries(post0), "symmetry")

# ---------------------------------------------------------------------------
# D. Total-flux criterion and its frame dependence.
# ---------------------------------------------------------------------------
# Delayed rectangular pulse of density p on [d, d+s]: after shutoff the excess is linear in x.
F_after = mu + yy**2 / 2 + yy * xx - sp.integrate(sp.integrate(p, (u1, d, u2)), (u2, d, d + s)) - p * s * (xx - d - s)
check("D1 after any pulse the mixed excess is linear with slope y - E_tot",
      sp.simplify(sp.diff(F_after, xx) - (yy - p * s)) == 0 and sp.diff(F_after, xx).has(d) is False,
      "slope independent of the delay d", "criterion")
dens = sp.Function("tau")
P_cum = sp.Function("Q")
ident = sp.integrate((xx - u1) * dens(u1), (u1, 0, xx))
check("D2 double-integral identity behind the CGHS mass and momentum functions",
      sp.simplify(sp.diff(ident, xx, 2) - dens(xx)) == 0, "d^2/dx^2 int_0^x (x-s) tau(s) ds = tau(x)", "criterion")
# Sigma-frame energy of a Kruskal pulse on [d, d+s] with x_p = exp(lambda sigma)/lambda:
#   T_sigma sigma = (lambda x_p)^2 T_++, d sigma = dx_p/(lambda x_p).
E_sigma = sp.integrate(lam * u1 * p * lam**2, (u1, d, d + s))
check("D3 sigma-frame energy of a fixed Kruskal pulse depends on its position",
      sp.simplify(sp.diff(E_sigma, d)) != 0 and sp.simplify(sp.diff(p * s, d)) == 0,
      f"E_sigma = {sp.factor(E_sigma)}; E_tot = p s", "criterion")

# ---------------------------------------------------------------------------
# E. Exact geometry through the Lambert-W inversion (lambda = kappa = 1).
# ---------------------------------------------------------------------------
Os = (1 - mp.log(mp.mpf(1) / 4)) / 4


def e2rho(Fhat):
    """Weak-coupling conformal factor e^{2 rho} = e^{2 phi} for Omega = Omega_s + Fhat."""
    Om_val = Os + Fhat
    return (-4 / mp.lambertw(-4 * mp.exp(-4 * Om_val), -1)).real


def phi_of(Fhat):
    return mp.log(e2rho(Fhat)) / 2


vals = [mp.mpf(v) for v in ("0.01", "0.5", "3", "40", "900")]
check("E1 Lambert-W inversion reproduces Omega(phi)",
      all(abs(phi_of(v) / 2 + mp.exp(-2 * phi_of(v)) - (Os + v)) < mp.mpf(10) ** -30 for v in vals), "", "geometry")
check("E2 conformal factor bound e^{2 rho} <= 1/(sqrt(kappa) Omega) at weak coupling",
      all(e2rho(v) <= 1 / (Os + v) for v in vals if phi_of(v) <= 0), "holds wherever phi <= 0", "geometry")

muv = mp.mpf("0.2")
ratio = [e2rho(muv + X**2 / 2) * X**2 / 2 for X in (mp.mpf(10) ** k for k in (2, 4, 6))]
check("E3 pre-onset conformal factor tends to 2/(lambda^2 (x_p - x_m)^2)",
      abs(ratio[-1] - 1) < mp.mpf(10) ** -10 and abs(ratio[0] - 1) > abs(ratio[1] - 1) > abs(ratio[2] - 1),
      [mp.nstr(r, 12) for r in ratio], "geometry")


def curvature(F, xpv, xmv, h=mp.mpf("1e-6")):
    """R = 8 e^{-2 rho} d_+ d_- rho for ds^2 = -e^{2 rho} dx_p dx_m."""
    rho = lambda a_, b_: mp.log(e2rho(F(a_, b_))) / 2
    mixed = (rho(xpv + h, xmv + h) - rho(xpv + h, xmv - h) - rho(xpv - h, xmv + h) + rho(xpv - h, xmv - h)) / (4 * h * h)
    return 8 * mixed / e2rho(F(xpv, xmv))


F_pre = lambda a_, b_: muv + (a_ - b_) ** 2 / 2
Rs = [curvature(F_pre, mp.mpf(-X), mp.mpf(0)) for X in (30, 100, 300)]
check("E4 curvature tends to -4 lambda^2 at the AdS2 ends and stays finite",
      abs(Rs[-1] + 4) < mp.mpf("0.01") and abs(Rs[0] + 4) > abs(Rs[-1] + 4), [mp.nstr(r, 8) for r in Rs], "geometry")

affine = [mp.quad(lambda X: e2rho(muv + X**2 / 2), [0, 10, 100, T]) for T in (mp.mpf(10) ** 3, mp.mpf(10) ** 5, mp.mpf(10) ** 7)]
check("E5 null rays reach the AdS2 end at finite affine parameter",
      abs(affine[2] - affine[1]) < mp.mpf("3e-5") and abs(affine[1] - affine[0]) < mp.mpf("3e-3"),
      [mp.nstr(v, 12) for v in affine], "geometry")
proper = [mp.quad(lambda r: mp.sqrt(e2rho(muv + 2 * r**2)), [0, 1, 10, T]) for T in (mp.mpf(10) ** 2, mp.mpf(10) ** 4, mp.mpf(10) ** 6)]
steps = (proper[1] - proper[0], proper[2] - proper[1])
check("E6 the same end is at infinite proper distance along static slices (logarithmic growth)",
      abs(steps[0] - steps[1]) < mp.mpf("0.02") and steps[0] > 3, [mp.nstr(v, 8) for v in proper], "geometry")
check("E7 the dilaton field diverges at the AdS2 end (weak coupling)",
      phi_of(muv + mp.mpf(10) ** 12 / 2) < -13, mp.nstr(phi_of(muv + mp.mpf(10) ** 12 / 2), 8), "geometry")

# Future end of an escaping ray after a pulse of total strength E < y.
Ev, yv, sv = mp.mpf("0.5"), mp.mpf("1.5"), mp.mpf(1)
F_escape = lambda X: muv + yv**2 / 2 + Ev * sv / 2 + (yv - Ev) * X
flat = [e2rho(F_escape(X)) * (yv - Ev) * X for X in (mp.mpf(10) ** k for k in (3, 6, 12))]
check("E8 escaping rays end in a linear-dilaton region: e^{2 rho} lambda^2 x_p (y - E) -> 1",
      abs(flat[-1] - 1) < mp.mpf(10) ** -9 and abs(flat[0] - 1) > abs(flat[1] - 1), [mp.nstr(v, 12) for v in flat], "geometry")
aff_future = [mp.quad(lambda X: e2rho(F_escape(X)), [sv, 10, 100, T]) for T in (mp.mpf(10) ** 3, mp.mpf(10) ** 6, mp.mpf(10) ** 9)]
growth = (aff_future[1] - aff_future[0], aff_future[2] - aff_future[1])
check("E9 the future end is at infinite affine parameter (logarithmic divergence)",
      abs(growth[0] - growth[1]) < mp.mpf("0.01") and abs(growth[0] - mp.log(1000) / (yv - Ev)) < mp.mpf("0.02"),
      [mp.nstr(v, 10) for v in aff_future], "geometry")

# Event horizon: rays with y < E_tot hit the critical curve, rays with y > E_tot never do.
def first_zero(yval):
    C = muv + yval**2 / 2
    during = lambda X: C + yval * X - (Ev / sv) * X**2 / 2
    if during(sv) <= 0:
        return (yval + mp.sqrt(yval**2 + 2 * (Ev / sv) * C)) / (Ev / sv)
    slope = yval - Ev
    return None if slope >= 0 else sv + during(sv) / (-slope)


hits = [first_zero(mp.mpf(v)) for v in ("0.1", "0.3", "0.49")]
misses = [first_zero(mp.mpf(v)) for v in ("0.5", "0.51", "2")]
check("E10 event horizon of the pulse spacetime is x_m = -E_tot",
      all(h is not None and h > 0 for h in hits) and all(m is None for m in misses),
      f"hits at {[mp.nstr(h, 8) for h in hits]}; y >= E escape", "geometry")


# ---------------------------------------------------------------------------
# F. Two-sided flux and the global causal character of the critical curve.
# ---------------------------------------------------------------------------
import random

Ap, Am = sp.Function("A_p"), sp.Function("A_m")
a_neg = lambda v: v**2 / 2
ok = True
for sp_sign in (-1, 1):
    for sm_sign in (-1, 1):
        F2 = mu - xp * xm + (a_neg(xp) if sp_sign < 0 else 0) + (a_neg(xm) if sm_sign < 0 else 0) - Ap(xp) - Am(xm)
        ok &= sp.simplify(sp.diff(F2, xp, xm) + 1) == 0
        ok &= sp.simplify(sp.diff(F2, xp, 2) - ((1 if sp_sign < 0 else 0) - sp.diff(Ap(xp), xp, 2))) == 0
        ok &= sp.simplify(sp.diff(F2, xm, 2) - ((1 if sm_sign < 0 else 0) - sp.diff(Am(xm), xm, 2))) == 0
check("F1 two-sided solution satisfies field equation and both constraints in all four sectors", ok, group="global")

rng = random.Random(20261124)


def random_flux():
    """Monotone cumulative flux: atom at onset, a ramp, and a later atom; zero before onset."""
    a0, rate, stop, a1, t1 = rng.uniform(0, 0.6), rng.uniform(0, 1.2), rng.uniform(0.2, 3), rng.uniform(0, 0.8), rng.uniform(0.1, 4)

    def Q(v):
        return 0.0 if v < 0 else a0 + rate * min(v, stop) + (a1 if v >= t1 else 0.0)

    def A(v):
        if v <= 0:
            return 0.0
        ramp = rate * (v**2 / 2 if v <= stop else stop**2 / 2 + stop * (v - stop))
        return a0 * v + ramp + a1 * max(v - t1, 0.0)

    return Q, A, a0 + rate * stop + a1


def F2num(m, Apf, Amf, x, z):
    return m - x * z + min(x, 0) ** 2 / 2 + min(z, 0) ** 2 / 2 - Apf(x) - Amf(z)


violations = 0
tested = 0
grad_bad = 0
zeros = 0
for _ in range(400):
    Qp, Apf, Ep = random_flux()
    Qm, Amf, Em = random_flux()
    m = rng.uniform(0.05, 3)
    for _ in range(60):
        x, z = rng.uniform(-4, 8), rng.uniform(-4, 8)
        if F2num(m, Apf, Amf, x, z) <= 0:
            dx, dz = rng.uniform(0, 3), rng.uniform(0, 3)
            if dx + dz > 1e-9:
                tested += 1
                if not F2num(m, Apf, Amf, x + dx, z + dz) < 0:
                    violations += 1
    # locate zeros along rays by bisection and test both one-sided gradients
    for _ in range(10):
        z = rng.uniform(-3, 6)
        lo, hi = -50.0, 200.0
        if F2num(m, Apf, Amf, hi, z) >= 0:
            continue
        for _ in range(80):
            mid = (lo + hi) / 2
            if F2num(m, Apf, Amf, mid, z) > 0:
                lo = mid
            else:
                hi = mid
        zeros += 1
        gp = -z + min(hi, 0) - Qp(hi)
        gm = -hi + min(z, 0) - Qm(z)
        if not (gp < 0 and gm < 0):
            grad_bad += 1
check("F2 the non-positive set is a future set (causal future of F<=0 has F<0), two-sided random fluxes with atoms",
      violations == 0 and tested > 2000, f"{tested} point pairs, {violations} violations", "global")
check("F3 both null gradients of F are negative on the critical curve (spacelike, future-trapped)",
      grad_bad == 0 and zeros > 500, f"{zeros} zeros, {grad_bad} exceptions", "global")

mirror_ok = True
for _ in range(200):
    Qm, Amf, Em = random_flux()
    m = rng.uniform(0.05, 3)
    yl = rng.uniform(0.01, 3)
    if abs(yl - Em) < 1e-3:
        continue
    hit = any(F2num(m, lambda v: 0.0, Amf, -yl, zz * 0.05) <= 0 for zz in range(0, 40000))
    mirror_ok &= (hit == (yl < Em))
check("F4 mirror sector: the ray x_p=-y' is captured iff y' < E_tot of the outgoing flux", mirror_ok, group="global")

# ---------------------------------------------------------------------------
# G. Late-time exterior, final mass parameter, horizon monotonicity.
# ---------------------------------------------------------------------------
yy, xx = sp.symbols("y x", positive=True)
Epulse = p * s
m1 = Epulse * s / 2                      # first moment int_0^inf (E - Q) = int x dQ for the uniform pulse
F_after = mu + yy**2 / 2 + yy * xx - Epulse * (xx - s / 2)
mu_f = mu + m1 + Epulse**2 / 2
yt = yy - Epulse
check("G1 after a uniform pulse the mixed sector is the zero-flux form with mu_f = mu + m1 + E^2/2 in shifted coordinates",
      sp.simplify(F_after - (mu_f + yt**2 / 2 + yt * (xx + Epulse))) == 0, group="mass")
check("G2 first moment of the uniform pulse: int_0^s x p dx = E s/2", sp.simplify(sp.integrate(xx * p, (xx, 0, s)) - m1) == 0, group="mass")
F_imp = mu + yy**2 / 2 + (yy - alpha) * xx
check("G3 impulsive shell: mu_f = mu + alpha^2/2 (m1 = 0)",
      sp.simplify(F_imp - (mu + alpha**2 / 2 + (yy - alpha)**2 / 2 + (yy - alpha) * (xx + alpha))) == 0, group="mass")

mono_ok = True
for _ in range(300):
    Qp, Apf, Ep = random_flux()
    m = rng.uniform(0.05, 3)
    pts = sorted(rng.uniform(0, 9) for _ in range(12))
    FH = [m + Ep**2 / 2 + Ep * v - Apf(v) for v in pts]                  # F on the event horizon y = E
    FA = [m + Qp(v)**2 / 2 + Qp(v) * v - Apf(v) for v in pts]            # F on the apparent horizon y = Q(x)
    mono_ok &= all(b >= a - 1e-12 for a, b in zip(FH, FH[1:])) and all(b >= a - 1e-12 for a, b in zip(FA, FA[1:]))
check("G4 F is nondecreasing along the event horizon and along the apparent horizon", mono_ok, group="mass")


def lambert_u(kv, W):
    """Weak-branch e^{-2phi} from sqrt(kappa)*Omega = W:  u - (kappa/4) ln u = W, u >= kappa/4."""
    return -(kv / 4) * mp.lambertw(-(4 / kv) * mp.e ** (-4 * W / kv), -1).real


def ks_flux_minus(kv, lv, Fval, dmF, dmmF, tminus):
    """Kim-Son's <T_--> = 2 sqrt(k) d^2 Omega/(1+W) - 4 (d Omega)^2 (1-W)/(1+W)^3 - k t_-."""
    Lv = lv**2 / mp.sqrt(kv)
    Om_s = mp.sqrt(kv) / 4 * (1 - mp.log(kv / 4))
    Wsk = mp.sqrt(kv) * (Om_s + Lv * Fval)
    Wl = -(4 / kv) * lambert_u(kv, Wsk)
    return 2 * mp.sqrt(kv) * Lv * dmmF / (1 + Wl) - 4 * (Lv * dmF) ** 2 * (1 - Wl) / (1 + Wl) ** 3 - kv * tminus


flux_ok = True
detail = []
for kv, lv, mv, pv, sv_, yv in [(1, 1, 0.7, 0.5, 1.2, 1.5), (6, 1.3, 0.2, 2.0, 0.4, 1.1), (0.5, 0.8, 1.5, 0.3, 2.0, 2.4)]:
    kv, lv, mv, pv, sv_, yv = map(mp.mpf, (kv, lv, mv, pv, sv_, yv))
    Ev_ = pv * sv_
    target = -lv**2 + kv / (4 * (yv - Ev_) ** 2)
    res = []
    for X in (mp.mpf(10) ** 8, mp.mpf(10) ** 12, mp.mpf(10) ** 16):
        Fv = mv + yv**2 / 2 + yv * X - Ev_ * (X - sv_ / 2)
        res.append(abs(ks_flux_minus(kv, lv, Fv, -(X + yv), 1, lv**2 / kv) - target))   # d_m F = -x_p + x_m, d_m^2 F = 1
    flux_ok &= res[0] > res[1] > res[2] and res[2] < mp.mpf(10) ** -12
    detail.append(mp.nstr(res[2], 3))
check("G5 outgoing flux at right future infinity: -lambda^2 + kappa/(4 (y - E_tot)^2), Kim-Son's formula with A/lambda^2 -> E_tot",
      flux_ok, f"residuals at x_p=1e16: {detail}, decreasing in x_p", "mass")

ysig, sig = sp.symbols("ytilde sigma", real=True)
kruskal_limit = -lam**2 + kap / (4 * ysig**2)
sigma_form = sp.simplify((lam * ysig) ** 2 * kruskal_limit)          # tensor law with dx^-/dsigma^- = lambda*ytilde
check("G6 asymptotic frame: outgoing flux is kappa lambda^2/4 - lambda^4 exp(-2 lambda sigma^-), Hawking value plus decaying transient",
      sp.simplify(sigma_form.subs(ysig, sp.exp(-lam * sig)) - (kap * lam**2 / 4 - lam**4 * sp.exp(-2 * lam * sig))) == 0, group="mass")

# ---------------------------------------------------------------------------
# H. Weak-branch bounds used in the Lean affine-length theorems.
# ---------------------------------------------------------------------------
bound_ok = True
for kv in ("0.3", "1", "4", "9", "40"):
    kv = mp.mpf(kv)
    Ws = kv / 4 * (1 - mp.log(kv / 4))
    for Fl in ("0", "0.001", "0.5", "3", "200", "1e6"):
        lamF = mp.mpf(Fl)                       # lambda^2 * Fhat
        u = lambert_u(kv, Ws + lamF)
        lower = kv / 4 + lamF
        upper = 2 * (Ws + lamF) + (kv / 2) * (mp.log(kv / 2) - 1)
        bound_ok &= (u >= lower - mp.mpf(10) ** -25) and (u <= upper + mp.mpf(10) ** -25) and (u >= kv / 4 - mp.mpf(10) ** -25)
check("H1 weak branch: kappa/4 + lambda^2 Fhat <= e^{-2 phi} <= 2 sqrt(kappa) Omega + (kappa/2)(ln(kappa/2) - 1)", bound_ok, group="affine")

tail_ok = True
for kv, lv, mv in [(1, 1, 0.2), (1, 1, 2), (7, 0.6, 0.9), (0.4, 2, 0.05)]:
    kv, lv, mv = map(mp.mpf, (kv, lv, mv))
    Ws = kv / 4 * (1 - mp.log(kv / 4))
    val = mp.quad(lambda t: 1 / lambert_u(kv, Ws + lv**2 * (mv + t**2 / 2)), [1, 10, 100, mp.inf])
    tail_ok &= val <= 2 / lv**2
check("H2 affine length of the AdS2 end beyond unit distance is at most 2/lambda^2", tail_ok, group="affine")

passed = sum(row["status"] == "PASS" for row in checks)
failed = len(checks) - passed
print(f"STRUCTURE: {passed}/{len(checks)} PASS")
payload = {"checks_total": len(checks), "checks_passed": passed, "checks_failed": failed, "mpmath_dps": mp.mp.dps, "checks": checks}
(OUT / "structure-checks-summary.json").write_text(json.dumps(payload, indent=2) + "\n")
(OUT / "structure-checks.out").write_text("\n".join(
    [f"{row['status']} | {row['name']}" + (f" | {row['detail']}" if row["detail"] else "") for row in checks]
    + [f"STRUCTURE: {passed}/{len(checks)} PASS"]) + "\n")
raise SystemExit(1 if failed else 0)
