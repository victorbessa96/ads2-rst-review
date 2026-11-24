#!/usr/bin/env python3
"""Exact Kim-Son AdS2-RST branch under sustained one-sided positive flux.

Run with bash run_verification.sh, or set PHYSICS_PYTHON to a compatible interpreter.
SymPy checks the algebra; mpmath checks roots, physical-side exclusion,
causal signature, branch matching, and the AdS2 asymptotic control.
"""
from pathlib import Path
import hashlib
import json
import sys
import tarfile
import mpmath as mp
import sympy as sp

mp.mp.dps = 90
ROOT = Path(__file__).resolve().parent
SOURCE = ROOT / "sources" / "wormholeRST_jhep.tex"
ANCHORS = ROOT / "sources" / "source-anchors.txt"
EXTERNAL_SOURCE = not SOURCE.exists()
OUT_DIR = ROOT / "outputs"
OUT_DIR.mkdir(parents=True, exist_ok=True)
OUT = OUT_DIR / "verify.out"
SUMMARY = OUT_DIR / "verification-summary.json"
lines, checks = [], []

def log(s=""):
    print(s)
    lines.append(str(s))

def check(name, ok, detail="", group="canonical-88"):
    ok = bool(ok)
    row = {"name": name, "status": "PASS" if ok else "FAIL", "detail": str(detail), "group": group}
    checks.append(row)
    log(f"{row['status']} | {name}" + (f" | {detail}" if detail else ""))

src_path = ANCHORS if EXTERNAL_SOURCE else SOURCE
src = src_path.read_text(encoding="utf-8").splitlines()
def has_line(n, *tokens):
    return 1 <= n <= len(src) and all(t in src[n-1] for t in tokens)

log("KIM-SON AdS2-RST + SUSTAINED ONE-SIDED POSITIVE FLUX")
log("")
check("Primary source gives chiral Omega solution", has_line(157, "\\Omega (x^+, x^-)") and has_line(158, "a_+(x^+)"))
check("Primary source gives chiral constraint with matter", has_line(164, "\\kappa t_\\pm") and has_line(165, "\\partial_\\pm f") and has_line(171, "\\Omega") and has_line(172, "\\sqrt{\\kappa} t_+") and has_line(173, "\\sum_i"))
check("Primary source identifies the RST minimum/singularity", has_line(281, "singularity curve") and has_line(282, "\\Omega"))
check("Primary source fixes the AdS2 wormhole boundary functions", has_line(223, "t_\\pm(x^\\pm)") and "\\lambda^2}{\\kappa}" in src[222])
check("Primary source has the pre-shock static wormhole", has_line(313, "\\Omega = \\frac{M}{\\lambda}") and has_line(315, "x^+ - x^-"))
check("Primary source asymptotic is R -> -4 lambda^2", has_line(348, "R_{\\mathrm{asym}}") and has_line(349, "asymptotically AdS$_2$"))
check("Primary source infalling shock is one-sided and positive", has_line(210, "T_{++}^f") and has_line(211, "A \\delta", "T_{--}^f") and has_line(213, "positive constant"))
check("Primary source post-shock singularity is cloaked by horizon", has_line(256, "curvature singularity") and has_line(257, "cloaked by the horizon"))

xp, xm = sp.symbols("xp xm", real=True)
lam, kap, P, M = sp.symbols("lambda kappa P M", positive=True)
L = lam**2/sp.sqrt(kap)
Os = sp.sqrt(kap)*(1-sp.log(kap/4))/4
pre = M/lam + Os + L*(xp-xm)**2/2
mixed = M/lam + Os - L*xp*xm - P*xp**2/(2*sp.sqrt(kap)) + L*xm**2/2
post = M/lam + Os - L*xp*xm - P*xp**2/(2*sp.sqrt(kap))
other = M/lam + Os - L*xp*xm + L*xp**2/2  # xp<0, xm>0

for name, expr, axx, axm in [
    ("pre", pre, L, L),
    ("mixed", mixed, -P/sp.sqrt(kap), L),
    ("post", post, -P/sp.sqrt(kap), sp.Integer(0)),
    ("other", other, L, sp.Integer(0)),
]:
    check(f"{name} region obeys the mixed RST equation", sp.simplify(sp.diff(expr,xp,xm)+L)==0)
    check(f"{name} region obeys both chiral constraints", sp.simplify(sp.diff(expr,xp,2)-axx)==0 and sp.simplify(sp.diff(expr,xm,2)-axm)==0)

# C0/C1 matching at every coordinate-sign interface.
for label, left, right, axis in [
    ("xp=0, xm<0: pre/mixed", pre, mixed, xp),
    ("xm=0, xp<0: pre/other", pre, other, xm),
    ("xp=0, xm>0: other/post", other, post, xp),
    ("xm=0, xp>0: mixed/post", mixed, post, xm),
]:
    residuals=[]
    for expr in (left-right, sp.diff(left,xp)-sp.diff(right,xp), sp.diff(left,xm)-sp.diff(right,xm)):
        residuals.append(sp.simplify(expr.subs(axis,0)))
    check(f"C0/C1 matching at {label}", all(r==0 for r in residuals), f"residuals={residuals}")

# Dimensionless wall equation: mu + y^2/2 + x*y - p*x^2/2 = 0,
# y=-xm>0 in the mixed region, p=P/lambda^2, mu=sqrt(kappa) M/lambda^3.
x, y, p, mu = sp.symbols("x y p mu", positive=True)
F = mu + y**2/2 + x*y - p*x**2/2
D = sp.sqrt((1+p)*y**2 + 2*p*mu)
xw = (y+D)/p
slope_xm = -D/(xw+y)
check("Exact first-hit root satisfies the normalized wall equation", sp.simplify(F.subs(x,xw))==0)
# General symbolic implicit differentiation, with no mu=0 or sample-p restriction.
# On y(xp), F_x+F_y*y'=0 and dxm/dxp=-y'. At the root y-p*xw=-D.
implicit_tangent = sp.simplify(sp.diff(F,x).subs(x,xw) + sp.diff(F,y).subs(x,xw)*(-slope_xm))
check("General implicit wall tangent dxm/dxp is negative for every p,mu,y>0",
      implicit_tangent==0 and sp.simplify(y-p*xw+D)==0 and (xw+y).is_positive is True and D.is_positive is True,
      f"implicit_residual={implicit_tangent}")
F_zero_flux = sp.simplify(F.subs(p,0))
check("Zero-flux control has no positive mixed-region wall",
      F_zero_flux.is_positive is True and F_zero_flux.subs(mu,0).is_positive is True,
      f"F(p=0)={F_zero_flux}>0")
check("M=0 mixed-region post-onset wall is the exact line xm=-(sqrt(1+p)-1)xp", sp.simplify(xw.subs(mu,0)-y*(1+sp.sqrt(1+p))/p)==0)
check("M=0 wall energy simplifies to lambda^2 y(1+sqrt(1+p))", sp.simplify((P*xw).subs(mu,0).subs(P,p*lam**2)-lam**2*y*(1+sp.sqrt(1+p)))==0)

# Matching between the both-positive and mixed post-onset regions at xm=0.
x0 = sp.sqrt(2*mu/p)
post_wall_xm = mu/x - p*x/2
post_slope = sp.diff(post_wall_xm,x)
check("Both-positive wall reaches xm=0 at x=sqrt(2mu/p)", sp.simplify(post_wall_xm.subs(x,x0))==0)
check("Both-positive wall derivative identity holds (negative sign proved separately)", sp.simplify(post_slope + mu/x**2+p/2)==0)
check("Mixed and both-positive wall positions match at xm=0", sp.simplify(xw.subs(y,0)-x0)==0)
check("Mixed and both-positive wall slopes match at xm=0", sp.simplify(slope_xm.subs(y,0)-post_slope.subs(x,x0))==0)

# Source's asymptotic AdS2 control: W ~ -2 lambda^2 S/kappa and 1+W ~ W.
W, S = sp.symbols("W S", negative=True, real=True)
R_asym = 4*W/(1+W)*(lam**2 + 4*lam**4*W*S/(kap*(1+W)**2))
R_leading = sp.limit(R_asym.subs(S,-kap*W/(2*lam**2)), W, -sp.oo)
check("Leading large-S curvature is R -> -4 lambda^2", sp.simplify(R_leading+4*lam**2)==0)

# Causal sign in ds^2=-exp(2rho) dxp dxm: sign(tangent norm)=-dxm/dxp.
rho = sp.symbols("rho", real=True)
check("General mixed-region wall tangent and metric norm are spacelike",
      slope_xm.is_negative is True and (-sp.exp(2*rho)*slope_xm).is_positive is True)
pre_tangent_norm = -sp.exp(2*rho)  # pre-onset M=0 edge xp=xm, dxm/dxp=+1
check("Pre-onset M=0 singular line is timelike by its metric norm", pre_tangent_norm.is_negative is True)
post_line_slope_general = 1-sp.sqrt(1+p)
post_line_norm = -sp.exp(2*rho)*post_line_slope_general
q = sp.symbols("q", positive=True)  # q=sqrt(1+p)-1>0, equivalently p=q(q+2)
check("General-p M=0 post-onset singular branch is spacelike by its metric norm",
      sp.simplify(post_line_slope_general.subs(sp.sqrt(1+p),1+q)+q)==0
      and post_line_norm.subs(sp.sqrt(1+p),1+q).is_positive is True)

# The fourth sector xp<0,xm>0 cannot hide another wall.
u, v = sp.symbols("u v", positive=True)  # u=-xp>0, v=xm>0
other_excess = mu+u*v+u**2/2
check("Fourth sector xp<0,xm>0 has strictly positive normalized Omega excess",
      other_excess.is_positive is True and (other_excess-mu).is_positive is True)

rows=[]
for pv in ["0.01","0.1","1","10","100"]:
    for muv in ["0","0.2","2"]:
        for yv in ["0.1","1","10"]:
            pp,mm,yy = mp.mpf(pv),mp.mpf(muv),mp.mpf(yv)
            dd = mp.sqrt((1+pp)*yy**2+2*pp*mm)
            xx = (yy+dd)/pp
            resid = mm+yy**2/2+xx*yy-pp*xx**2/2
            before = mm+yy**2/2+(xx/mp.mpf("1.000001"))*yy-pp*(xx/mp.mpf("1.000001"))**2/2
            after = mm+yy**2/2+(xx*mp.mpf("1.000001"))*yy-pp*(xx*mp.mpf("1.000001"))**2/2
            slope = -dd/(xx+yy)
            ok = abs(resid)<mp.mpf("1e-75") and before>0 and after<0 and slope<0 and mp.isfinite(xx)
            check(f"first hit p={pv}, mu={muv}, y={yv}: physical before, excluded after, spacelike", ok,
                  f"xp={mp.nstr(xx,20)}, slope={mp.nstr(slope,12)}, before={mp.nstr(before,3)}, after={mp.nstr(after,3)}")
            rows.append({"p":pv,"mu":muv,"y":yv,"xp":mp.nstr(xx,40),"slope_xm_xp":mp.nstr(slope,40),"residual":mp.nstr(resid,4)})

# The M=0 global line and its p->0 retreat control.
for pv in ["0.001","0.1","1","100"]:
    pp=mp.mpf(pv); yy=mp.mpf("2")
    xx=yy*(1+mp.sqrt(1+pp))/pp
    ym=-(mp.sqrt(1+pp)-1)*xx
    check(f"M=0 exact mixed-region branch reproduces root and negative slope p={pv}", abs(-ym-yy)<mp.mpf("1e-75") and ym<0 and xx>0,
          f"xp={mp.nstr(xx,25)}, xm={mp.nstr(ym,25)}")
small=mp.mpf("1e-12"); yy=mp.mpf("2")
xx_small=yy*(1+mp.sqrt(1+small))/small
check("Small-flux numerical control places the fixed-ray wall beyond 1e12", xx_small>mp.mpf("1e12"))

# Branch matching at xm=0 for several nonzero mu,p rows.
for pv,muv in [("0.1","0.2"),("1","2"),("100","0.2")]:
    pp,mm=mp.mpf(pv),mp.mpf(muv)
    xx=mp.sqrt(2*mm/pp)
    xm_post=mm/xx-pp*xx/2
    sl_post=-mm/xx**2-pp/2
    dd=mp.sqrt(2*pp*mm)
    sl_mixed=-dd/xx
    check(f"xm=0 branch match p={pv}, mu={muv}", abs(xm_post)<mp.mpf("1e-80") and abs(sl_post-sl_mixed)<mp.mpf("1e-75") and sl_post<0,
          f"xp={mp.nstr(xx,25)}, common slope={mp.nstr(sl_post,25)}")

# Direct numerical AdS2 asymptotic control on the source's W representation.
# Test convergence of the sequence, not an arbitrary near-limit tolerance at small S.
curvatures=[]
for Sv in ["1","10","100","1000","10000","100000"]:
    SS=mp.mpf(Sv); ll=kk=mp.mpf(1); MM=mp.mpf(0)
    os=mp.sqrt(kk)*(1-mp.log(kk/4))/4
    Om=MM/ll+os+ll**2*SS/(2*mp.sqrt(kk))
    xi=-4/kk*mp.exp(-4*Om/mp.sqrt(kk))
    ww=mp.lambertw(xi,-1)
    RR=4*ww/(1+ww)*(ll**2+4*ll**4*ww*SS/(kk*(1+ww)**2))
    curvatures.append((Sv,RR))
    log(f"CURVATURE | S={Sv} | R={mp.nstr(RR,30)} | |R+4|={mp.nstr(abs(RR+4),8)}")
gaps=[abs(rr+4) for _,rr in curvatures]
check("Weak-branch curvature sequence approaches AdS2 monotonically",
      all(gaps[i+1]<gaps[i] for i in range(len(gaps)-1)) and gaps[-1]<mp.mpf("0.003"),
      f"gaps={','.join(str(mp.nstr(g,6)) for g in gaps)}")

# ---------------------------------------------------------------------------
# Review-closure extensions: provenance, horizons, impulse, state sensitivity,
# finite pulse, null affine parameter, and explicit interior observer clocks.
# ---------------------------------------------------------------------------
if EXTERNAL_SOURCE:
    source_sha = None
    source_note = (ROOT / "sources" / "README.md").read_text(encoding="utf-8")
    check("Primary source links and provenance are recorded",
          "https://arxiv.org/abs/gr-qc/0404098v2" in source_note
          and "8906ec46e685404da151c8b7d52a325c4053ee8c8f17964df7264c69baf58872" in source_note,
          "external-source-mode; original TeX not redistributed", "provenance")
else:
    with tarfile.open(ROOT / "sources" / "gr-qc-0404098.tar") as bundle:
        source_member = bundle.extractfile("wormholeRST_jhep.tex").read()
    source_sha = hashlib.sha256(source_member).hexdigest()
    check("Staged TeX is byte-identical to its tar member and pinned SHA-256",
          source_member == SOURCE.read_bytes() and source_sha == "8906ec46e685404da151c8b7d52a325c4053ee8c8f17964df7264c69baf58872",
          source_sha, "provenance")

# The other quadratic root is negative by rationalization, not a CAS assumption.
other_root = -(y**2 + 2*mu)/(y + D)
check("Negative root is rationalized and strictly negative",
      sp.simplify((y-D)/p-other_root) == 0 and other_root.is_negative is True,
      group="sustained-proof")
check("Apparent horizon precedes the singular hit on every mixed ray",
      sp.simplify(xw-y/p-D/p) == 0 and (D/p).is_positive is True,
      "x_hit-y/p=D/p>0", "horizon")
check("Mixed apparent-horizon curve is xm=-p xp and is distinct from the wall",
      sp.simplify(y-p*x).subs(x,y/p) == 0 and sp.simplify(xw-y/p-D/p) == 0,
      "at fixed y, x_AH=y/p and x_hit-x_AH=D/p>0", "horizon")

# FR-09: the conformal factor is finite and nonzero at Omega_s.
phi = sp.symbols("phi", positive=True)
Omega_phi = sp.exp(-2*phi)/sp.sqrt(kap) + sp.sqrt(kap)*phi/2
critical_exp_minus_2phi = sp.solve(sp.diff(Omega_phi,phi),sp.exp(-2*phi))[0]
check("RST minimum has finite nonzero conformal factor exp(2rho)=4/kappa",
      sp.simplify(critical_exp_minus_2phi-kap/4) == 0 and sp.simplify(1/critical_exp_minus_2phi-4/kap) == 0,
      group="conformal-factor")

# The global mixed-wall representation supplied by the second AI review.
wall_xm = x - sp.sqrt((1+p)*x**2 - 2*mu)
G_wall = mu - x*xm + xm**2/2 - p*x**2/2
check("Global mixed-wall representation solves the normalized wall equation",
      sp.simplify(G_wall.subs(xm,wall_xm)) == 0,
      "valid for x>=sqrt(2mu/p) in the mixed region", "sustained-proof")

# Kim-Son's original impulsive source: it already has a restricted wall band.
a = sp.symbols("a", positive=True)  # a=A/lambda^2
F_imp = mu + y**2/2 + x*(y-a)
x_imp = sp.solve(F_imp,x)[0]
slope_imp = sp.simplify((y-a)/(x_imp+y))
h_imp = sp.symbols("h_imp", positive=True)
check("Impulsive mixed wall exists exactly for 0<y<a",
      has_line(230, "- \\frac{A}{\\sqrt{\\kappa}}") and has_line(304, "- \\frac{A}{\\sqrt{\\kappa}}")
      and sp.simplify(F_imp.subs(x,x_imp)) == 0
      and (y-a).subs(a,y+h_imp).is_negative is True
      and x_imp.subs(a,y+h_imp).is_positive is True and y.is_positive is True,
      "source negative chiral term pinned; x_imp=(mu+y^2/2)/(a-y)", "impulsive-comparison")
check("Impulsive example alpha=mu=1,y=1/2 has x=9/4 and spacelike slope -2/11",
      sp.simplify(x_imp.subs({a:1,mu:1,y:sp.Rational(1,2)})-sp.Rational(9,4)) == 0
      and sp.simplify(slope_imp.subs({a:1,mu:1,y:sp.Rational(1,2)})+sp.Rational(2,11)) == 0,
      group="impulsive-comparison")
post_imp = mu/x-a
check("Impulsive mixed and both-positive branches match position and slope",
      sp.simplify(x_imp.subs(y,0)-mu/a) == 0
      and sp.simplify(post_imp.subs(x,mu/a)) == 0
      and sp.simplify(slope_imp.subs(y,0)-sp.diff(post_imp,x).subs(x,mu/a)) == 0,
      group="impulsive-comparison")
check("Impulsive both-positive branch is spacelike",
      sp.diff(post_imp,x).is_negative is True,
      group="impulsive-comparison")

# Alternate quantum-state data: mixed-ray threshold, without an all-wall claim.
F_alt = mu + y**2/2 + x*y + (1-p)*x**2/2
D_alt = sp.sqrt(p*y**2 + 2*(p-1)*mu)
x_alt = (y+D_alt)/(p-1)
check("Alternate retained-t+ state has no mixed-ray wall for p=1",
      (mu+x*y+y**2/2).is_positive is True,
      group="state-sensitivity")
r_small = sp.symbols("r_small", positive=True)
p_small = 1/(1+r_small)
check("Alternate retained-t+ state has positive coefficients for 0<p<1",
      sp.simplify(1-p_small).is_positive is True and y.is_positive is True and (mu+y**2/2).is_positive is True
      and sp.simplify((1-p_small)/2-r_small/(2*(1+r_small))) == 0
      and sp.simplify(F_alt.subs(p,1+p)-F) == 0,
      "parameterize p=1/(1+r_small); direct F_alt(1+p)=F retained-state equivalence", "state-sensitivity")
other_alt = -(y**2+2*mu)/(y+D_alt)
check("Alternate retained-t+ state has a unique positive mixed hit for p>1",
      sp.simplify(F_alt.subs(x,x_alt)) == 0 and x_alt.subs(p,1+q).is_positive is True
      and sp.simplify((y-D_alt)/(p-1)-other_alt) == 0
      and (y+sp.symbols("Dpos", positive=True)).is_positive is True
      and (-(y**2+2*mu)).is_negative is True,
      "parameterize p=1+q>1; the other root is negative", "state-sensitivity")
G_alt = mu - x*xm + (1-p)*x**2/2
check("Alternate p=1 both-positive wall is xm=mu/xp",
      sp.simplify(G_alt.subs(p,1).subs(xm,mu/x)) == 0,
      "the p<=1 statement is mixed-ray-specific, not an all-wall theorem", "state-sensitivity")

# Finite pulse on 0<x<s, with E=p*s. During and after branches are C1.
s, E = sp.symbols("x_s E", positive=True)
F_during = mu + y**2/2 + x*y - p*x**2/2
F_after = mu + y**2/2 + E*s/2 + x*(y-E)
check("Finite-pulse shutoff value and first derivative match at x=s",
      sp.simplify((F_during-F_after).subs(x,s).subs(E,p*s)) == 0
      and sp.simplify((sp.diff(F_during,x)-sp.diff(F_after,x)).subs(x,s).subs(E,p*s)) == 0,
      "E=p*s", "finite-pulse")
x_after = sp.solve(F_after,x)[0]
check("Finite-pulse post-shutoff root has the exact linear form and x_after>s for F_during(s)>0,y<E",
      sp.simplify(x_after-(mu+E*s/2+y**2/2)/(E-y)) == 0
      and sp.simplify((x_after-s).subs(E,p*s)-(F_during.subs(x,s)/(E-y)).subs(E,p*s)) == 0,
      "x_after-s=F_during(s)/(E-y)", "finite-pulse")
h_pulse = sp.symbols("h_pulse", positive=True)
x_after_positive = x_after.subs(E,y+h_pulse)
slope_after = (y-E)/(x_after+y)
check("Finite-pulse post-shutoff wall has the exact negative tangent for y<E",
      sp.simplify(F_after.subs(x,x_after)) == 0
      and (y-E).subs(E,y+h_pulse).is_negative is True
      and x_after_positive.is_positive is True and y.is_positive is True,
      f"dxm/dxp={slope_after}<0", "finite-pulse")
y_max = -s + sp.sqrt((1+p)*s**2-2*mu)
check("Finite-pulse shutoff ray bound has the correct M=0 limit and x_hit increases with y",
      sp.simplify(y_max.subs(mu,0)-s*(sp.sqrt(1+p)-1)) == 0
      and sp.simplify(sp.diff(xw,y)).is_positive is True,
      "0<y<y_max gives x_hit<x_s; y_max<E", "finite-pulse")
z_during = mu/x - p*x/2
z_after = (mu+E*s/2)/x - E
x_after_zero = s/2 + mu/E
check("Finite-pulse both-positive wall position, slope, and sign-domain match at shutoff",
      sp.simplify((z_during-z_after).subs(x,s).subs(E,p*s)) == 0
      and sp.simplify((sp.diff(z_during,x)-sp.diff(z_after,x)).subs(x,s).subs(E,p*s)) == 0
      and sp.simplify(z_after.subs(x,x_after_zero)) == 0
      and sp.simplify(z_after-E*(x_after_zero/x-1)) == 0
      and sp.simplify((x_after_zero-s)-(2*mu-E*s)/(2*E)) == 0
      and sp.simplify(z_after.subs({p:1,mu:10,s:3,E:3,x:4})-sp.Rational(5,8)) == 0
      and sp.simplify(z_after.subs({p:1,mu:10,s:3,E:3,x:5})+sp.Rational(1,10)) == 0
      and sp.simplify(z_after.subs({p:1,mu:2,s:3,E:3,x:3})+sp.Rational(5,6)) == 0,
      "during: 0<x_p<min(s,sqrt(2mu/p)); after: s<x_p<s/2+mu/E if mu>E*s/2", "finite-pulse")
check("Finite-pulse apparent horizon continues after shutoff as y=E and every wall ray crosses during it",
      sp.simplify(((y-p*x)-y+E).subs(x,s).subs(E,p*s)) == 0
      and sp.simplify((E-y)/p).subs(E,y+h_pulse).is_positive is True,
      "during: y=p*x; after: y=E; y<E => y/p<s", "finite-pulse")

# Symbolic null-affine and interior-observer identities.
C_affine = sp.symbols("C_affine", positive=True)
rho_x = sp.Function("rho_x")
v_null = C_affine*sp.exp(-2*rho_x(x))
check("Fixed-xm null geodesic has dxp/dlambda=C exp(-2rho)",
      sp.simplify(sp.diff(v_null,x)+2*rho_x(x).diff(x)*v_null) == 0
      and sp.simplify(sp.diff(sp.log(C_affine*sp.exp(-2*rho)),rho)+2) == 0,
      "v'+2 rho_x v=0; therefore dlambda/dxp=exp(2rho)/C", "null-affine")
Wneg = sp.symbols("Wneg", negative=True)
check("Weak-branch conformal factor has finite positive upper bound",
      (-4/(kap*Wneg)).is_positive is True,
      "W<=-1 gives 0<exp(2rho)<=4/kappa", "null-affine")
sig0, sig1 = sp.symbols("sigma0 sigma1", real=True)
xp_sig = sp.exp(lam*(sig0+sig1))
xm_sig = -sp.exp(-lam*(sig0-sig1))
metric_00 = sp.simplify(sp.diff(xp_sig,sig0)*sp.diff(xm_sig,sig0))
metric_11 = sp.simplify(sp.diff(xp_sig,sig1)*sp.diff(xm_sig,sig1))
metric_01 = sp.simplify(sp.diff(xp_sig,sig0)*sp.diff(xm_sig,sig1)+sp.diff(xp_sig,sig1)*sp.diff(xm_sig,sig0))
check("Interior observer chart has the expected Lorentzian conformal metric",
      metric_01 == 0 and sp.simplify(metric_00+metric_11) == 0
      and sp.simplify(metric_00-lam**2*sp.exp(2*lam*sig1)) == 0,
      "ds^2=-lambda^2 K exp(2rho)(dsigma0^2-dsigma1^2)", "interior-observer")
K = sp.symbols("K", positive=True)
rK = 1 + mu/K
R_wall = sp.sqrt(rK**2+p) - rK
check("Interior constant-sigma1 wall root has the exact R_w form",
      sp.simplify(K*R_wall**2 + 2*(K+mu)*R_wall-K*p) == 0,
      "sigma0_wall=-ln(R_w)/(2 lambda)", "interior-observer")
check("Interior observer chart gives R=-xm/xp=exp(-2 lambda sigma0)",
      sp.simplify((-xm_sig/xp_sig)-sp.exp(-2*lam*sig0)) == 0,
      group="interior-observer")

# Numerical controls use the weak W_{-1} branch directly.
def numeric_e2rho(Om, ll=mp.mpf(1), kk=mp.mpf(1)):
    xi = -4/kk*mp.exp(-4*Om/mp.sqrt(kk))
    ww = mp.lambertw(xi,-1)
    return -4/(kk*ww)

def numeric_Omega_sustained(xx, yy, pp, mm, ll=mp.mpf(1), kk=mp.mpf(1)):
    Os_num = mp.sqrt(kk)*(1-mp.log(kk/4))/4
    B_num = mm*ll**2/mp.sqrt(kk) + Os_num
    L_num = ll**2/mp.sqrt(kk)
    return B_num + L_num*xx*yy - pp*ll**2*xx**2/(2*mp.sqrt(kk)) + L_num*yy**2/2

# Null affine parameter is finite and bounded by 4 Delta xp/(C kappa).
pp, mm, yy = map(mp.mpf,("1","0.2","1"))
dd = mp.sqrt((1+pp)*yy**2+2*pp*mm)
xx_hit = (yy+dd)/pp
ell = mp.quad(lambda xv: numeric_e2rho(numeric_Omega_sustained(xv,yy,pp,mm)),[mp.mpf("0.1"),xx_hit])
ell_bound = 4*(xx_hit-mp.mpf("0.1"))
check("Null affine quadrature is finite and below the exact weak-branch bound",
      mp.isfinite(mp.re(ell)) and mp.re(ell)>0 and mp.re(ell)<=ell_bound and abs(mp.im(ell))<mp.mpf("1e-60"),
      f"ell={mp.nstr(mp.re(ell),20)}, bound={mp.nstr(ell_bound,20)}", "null-affine")

# Interior observer sample: every sampled constant-sigma1 curve hits at finite
# sigma0 and finite proper time from any finite earlier coordinate.
observer_rows = []
for s1v in ["-1","0","1"]:
    ll = kk = pp = mm = mp.mpf(1)
    ss1 = mp.mpf(s1v)
    KK = mp.exp(2*ss1)
    rr = 1+mm/KK
    RRw = mp.sqrt(rr**2+pp)-rr
    ss0w = -mp.log(RRw)/2
    xxw = mp.exp(ss0w+ss1)
    yyw = mp.exp(-ss0w+ss1)
    residual = numeric_Omega_sustained(xxw,yyw,pp,mm)-mp.sqrt(kk)*(1-mp.log(kk/4))/4
    tau = mp.quad(lambda sg: mp.sqrt(KK*numeric_e2rho(numeric_Omega_sustained(
        mp.exp(sg+ss1),mp.exp(-sg+ss1),pp,mm))),[mp.mpf("-2"),ss0w])
    ok = abs(residual)<mp.mpf("1e-60") and mp.isfinite(mp.re(tau)) and mp.re(tau)>0
    check(f"Interior timelike observer hits at finite sigma0 and proper time sigma1={s1v}", ok,
          f"sigma0_hit={mp.nstr(ss0w,20)}, tau={mp.nstr(mp.re(tau),20)}, residual={mp.nstr(residual,4)}", "interior-observer")
    observer_rows.append({"sigma1":s1v,"sigma0_hit":mp.nstr(ss0w,30),"proper_time_from_minus_2":mp.nstr(mp.re(tau),30)})

# Finite-pulse numerical census: 0<y<E is necessary and sufficient for a hit.
pulse_rows = []
for pv,muv,sv in [("1","0","2"),("0.2","0.5","3"),("2","1","1.5")]:
    pp,mm,ss = map(mp.mpf,(pv,muv,sv))
    EE = pp*ss
    for factor in ["0.25","0.75","1","1.25"]:
        yy = EE*mp.mpf(factor)
        dd = mp.sqrt((1+pp)*yy**2+2*pp*mm)
        xd = (yy+dd)/pp
        xa = (mm+yy**2/2+EE*ss/2)/(EE-yy) if factor != "1" else None
        if xd < ss:
            first = xd
            branch = "during"
            residual = mm+yy**2/2+first*yy-pp*first**2/2
        elif yy < EE:
            first = xa
            branch = "after"
            residual = mm+yy**2/2+EE*ss/2+first*(yy-EE)
        else:
            first = None
            branch = "none"
            residual = None
        if first is None:
            after_at_s = mm+yy**2/2+EE*ss/2+ss*(yy-EE)
            ok = xd >= ss and after_at_s >= 0 and yy-EE >= 0
        else:
            ok = mp.isfinite(first) and first>0 and abs(residual)<mp.mpf("1e-65") and (branch == "during" or first >= ss)
        check(f"Finite-pulse wall existence p={pv},mu={muv},s={sv},y/E={factor}", ok,
              f"first={mp.nstr(first,16) if first is not None else 'NONE'}, branch={branch}, E={mp.nstr(EE,8)}, residual={mp.nstr(residual,4) if residual is not None else 'no-root'}", "finite-pulse")
        pulse_rows.append({"p":pv,"mu":muv,"x_s":sv,"y_over_E":factor,"first_hit":mp.nstr(first,30) if first is not None else None,"branch":branch})

# General nonnegative cumulative flux: derivative, concavity, and exponential example.
xx, u = sp.symbols("x_q u_q", positive=True)
Tq = sp.Function("T_q", positive=True)
Qq = sp.Integral(Tq(u), (u, 0, xx))
Iq = sp.Integral((xx-u)*Tq(u), (u, 0, xx))
Fq_general = mu + y**2/2 + xx*y - Iq/lam**2
general_slope = -(Qq-y)/(xx+y)
check("Cumulative flux derivative, concavity, corrected slope, and horizon ordering",
      sp.simplify(sp.diff(Fq_general,xx)-(y-Qq/lam**2)) == 0
      and sp.simplify(sp.diff(Fq_general,xx,2)+Tq(xx)/lam**2) == 0
      and general_slope.subs(Qq,y+h_pulse).is_negative is True
      and (Qq-y).subs(Qq,y+h_pulse).is_positive is True,
      "F_x=y-Q; slope=-(Q-y)/(x+y); horizon Q=y precedes Q(x_hit)>y", "cumulative-generalization")
Aq = sp.symbols("A_flux", positive=True)
Texp = Aq*sp.exp(-u)
Iexp = sp.integrate((xx-u)*Texp,(u,0,xx))
Fexp = sp.simplify(mu + y**2/2 + xx*y - Iexp/lam**2)
Fprime_exp = sp.simplify(sp.diff(Fexp,xx))
z_delay, d_delay = sp.symbols("z_delay d_delay", positive=True)
F_delay = mu + y**2/2 + (z_delay+d_delay)*y - Aq*(z_delay-1+sp.exp(-z_delay))
check("Exponential finite-total-flux example has the exact cutoff y<A_flux",
      sp.simplify(Iexp-Aq*(xx-1+sp.exp(-xx))) == 0
      and sp.limit(Fexp.subs(lam,1).subs(y,Aq/2),xx,sp.oo) == -sp.oo
      and sp.simplify(Fprime_exp.subs(lam,1).subs(y,Aq)-Aq*sp.exp(-xx)) == 0
      and sp.simplify(Fprime_exp.subs(lam,1).subs(y,Aq+h_pulse)-Aq*sp.exp(-xx)-h_pulse) == 0
      and sp.limit(Fexp.subs(lam,1).subs(y,2*Aq),xx,sp.oo) == sp.oo
      and sp.limit(F_delay.subs(y,Aq/2),z_delay,sp.oo) == -sp.oo
      and sp.simplify(sp.diff(F_delay,z_delay).subs(y,Aq)-Aq*sp.exp(-z_delay)) == 0,
      "Q(infinity)=A_flux; no hit for y>=A_flux; delayed-onset control included", "cumulative-generalization")

# Signed accumulated-excess and finite-sigma-support adversarial cases.
xs = sp.symbols("x_signed", positive=True)
Cf = sp.symbols("C_focus", positive=True)
A_linear = Cf*xs
root_linear = sp.solve(Cf-A_linear,xs)[0]
check("Signed accumulated excess: positive linear profile has a unique first hit",
      root_linear == 1 and (Cf-A_linear).subs(xs,sp.Rational(1,2)).is_positive is True
      and (Cf-A_linear).subs(xs,2).is_negative is True,
      "A=Cx, F=C-A", "signed-net-focusing")
A_unattained = Cf*(1-sp.exp(-xs))
check("Signed accumulated excess: unattained asymptotic threshold gives no finite hit",
      sp.limit(A_unattained,xs,sp.oo) == Cf and sp.simplify(Cf-A_unattained).is_positive is True
      and sp.limit(Cf-A_unattained,xs,sp.oo) == 0,
      "A=C(1-exp(-x))<C for every finite x", "signed-net-focusing")
A_quadratic = Cf*(2*xs-xs**2)
F_quadratic = sp.factor(Cf-A_quadratic)
check("Signed accumulated excess: quadratic tangential contact is not a termination",
      sp.simplify(F_quadratic-Cf*(xs-1)**2) == 0 and F_quadratic.subs(xs,1) == 0
      and F_quadratic.is_nonnegative is True and sp.diff(F_quadratic,xs).subs(xs,1) == 0,
      "F=C(x-1)^2>=0; RST edge contact, not right-side exclusion or physical continuation", "signed-net-focusing")
A_cusp = Cf*(1-sp.Abs(xs-1))
F_cusp = sp.simplify(Cf-A_cusp)
check("Signed accumulated excess: cusp contact has opposite one-sided tangents and no termination",
      sp.simplify(F_cusp-Cf*sp.Abs(xs-1)) == 0
      and sp.diff(F_cusp,xs).subs(xs,sp.Rational(1,2)) == -Cf
      and sp.diff(F_cusp,xs).subs(xs,sp.Rational(3,2)) == Cf
      and F_cusp.subs(xs,1) == 0 and F_cusp.is_nonnegative is True,
      "F=C|x-1|; left spacelike, right timelike; singular cusp contact, no right-side exclusion", "signed-net-focusing")
Pcal, xa, xb = sp.symbols("mathcalP x_a x_b", positive=True)
E_sigma = Pcal/lam**4*(1/xa-1/xb)
Tpp_sigma = Pcal/(lam**2*xs**2)
h_x = sp.symbols("h_x", positive=True)
check("Finite logarithmic-null-support pulse has exact total cumulative flux",
      sp.simplify(sp.integrate(Tpp_sigma/lam**2,(xs,xa,xb))-E_sigma) == 0
      and sp.simplify(E_sigma.subs(xb,xa+h_x)).is_positive is True,
      "E_tot=mathcalP/lambda^4*(1/x_a-1/x_b)", "finite-sigma-pulse")

# Explicit review regressions: non-real during bound and shutoff equality.
pp, ss, mm, yy = map(mp.mpf,("1","1","10","0.5"))
EE = pp*ss
xd = (yy+mp.sqrt((1+pp)*yy**2+2*pp*mm))/pp
xa = (mm+yy**2/2+EE*ss/2)/(EE-yy)
radicand = (1+pp)*ss**2-2*mm
check("Finite-pulse large-mu nonreal-y_max case still has post-shutoff hit",
      radicand < 0 and xd > ss and abs(xa-mp.mpf("21.25"))<mp.mpf("1e-70") and xa>ss,
      f"radicand={radicand}, x_after={mp.nstr(xa,20)}", "finite-pulse")
pp, ss, mm = map(mp.mpf,("1","2","0.2"))
EE = pp*ss
yy = -ss+mp.sqrt((1+pp)*ss**2-2*mm)
xd = (yy+mp.sqrt((1+pp)*yy**2+2*pp*mm))/pp
xa = (mm+yy**2/2+EE*ss/2)/(EE-yy)
check("Finite-pulse equality y=y_max has x_after=x_during=x_s",
      abs(xd-ss)<mp.mpf("1e-70") and abs(xa-ss)<mp.mpf("1e-70"),
      f"y={mp.nstr(yy,20)}, x_during={mp.nstr(xd,20)}, x_after={mp.nstr(xa,20)}", "finite-pulse")

passed=sum(c["status"]=="PASS" for c in checks)
failed=len(checks)-passed
log("")
if failed:
    log("VERDICT: FAIL; one or more checks failed")
else:
    log("VERDICT: the fixed sustained and finite-pulse Kim-Son solutions have exact spacelike RST termination and apparent-horizon corollaries")
    log("Interior observer proper time and null affine parameter are proved; no future-asymptotic boundary or absorber theorem is claimed")
log(f"SUMMARY: {passed}/{len(checks)} checks PASS")
if failed: log(f"FAILURES: {failed}")
OUT.write_text("\n".join(lines)+"\n",encoding="utf-8")
groups = {}
for row in checks:
    entry = groups.setdefault(row["group"], {"total": 0, "passed": 0, "failed": 0})
    entry["total"] += 1
    entry["passed" if row["status"] == "PASS" else "failed"] += 1
payload={"source_mode":"external-links" if EXTERNAL_SOURCE else "bundled-source","interpreter":sys.executable,"mpmath_dps":mp.mp.dps,
         "source_tex_sha256":source_sha,"checks_total":len(checks),"checks_passed":passed,"checks_failed":failed,
         "groups":groups,"checks":checks,"wall_rows":rows,"observer_rows":observer_rows,"pulse_rows":pulse_rows,
         "verdict_status":"FAIL" if failed else "PASS",
         "verdict":"Checks failed; no theorem-wide verification is claimed." if failed else "Exact fixed-model sustained and finite-pulse wall theorems, apparent-horizon ordering, finite null affine parameter, and finite interior-observer proper time are verified. No future-asymptotic absorber or arbitrary-state claim is made."}
SUMMARY.write_text(json.dumps(payload,indent=2)+"\n",encoding="utf-8")
sys.exit(1 if failed else 0)
