#!/usr/bin/env python3
"""Exact Kim-Son AdS2-RST branch under sustained one-sided positive flux.

Spark: spark_20261110_154351_a10e80.
Run with /home/bessa/.venvs/physics/bin/python.
SymPy checks the algebra; mpmath checks roots, physical-side exclusion,
causal signature, branch matching, and the AdS2 asymptotic control.
"""
from pathlib import Path
import json
import sys
import mpmath as mp
import sympy as sp

mp.mp.dps = 90
ROOT = Path(__file__).resolve().parent
SOURCE = ROOT / "sources" / "wormholeRST_jhep.tex"
OUT = ROOT / "ads2_rst_flux_out.txt"
SUMMARY = ROOT / "verification-summary.json"
lines, checks = [], []

def log(s=""):
    print(s)
    lines.append(str(s))

def check(name, ok, detail=""):
    ok = bool(ok)
    row = {"name": name, "status": "PASS" if ok else "FAIL", "detail": str(detail)}
    checks.append(row)
    log(f"{row['status']} | {name}" + (f" | {detail}" if detail else ""))

src = SOURCE.read_text(encoding="utf-8").splitlines()
def has_line(n, *tokens):
    return 1 <= n <= len(src) and all(t in src[n-1] for t in tokens)

log("KIM-SON AdS2-RST + SUSTAINED ONE-SIDED POSITIVE FLUX")
log("Spark spark_20261110_154351_a10e80")
log("")
check("Primary source gives chiral Omega solution", has_line(157, "\\Omega (x^+, x^-)") and has_line(158, "a_+(x^+)"))
check("Primary source gives chiral constraint with matter", has_line(164, "\\kappa t_\\pm") and has_line(165, "\\partial_\\pm f"))
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
check("Both-positive wall is spacelike", sp.simplify(post_slope + mu/x**2+p/2)==0)
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
check("Vanishing flux retreats the fixed-ray wall to infinite advanced coordinate", xx_small>mp.mpf("1e12"))

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

passed=sum(c["status"]=="PASS" for c in checks)
failed=len(checks)-passed
log("")
log("VERDICT: sustained one-sided positive flux creates a finite, spacelike RST edge in the past-AdS2 Kim-Son branch")
log("No future AdS2 absorber is present in this exact solution; a different transparent-boundary problem is not covered")
log(f"SUMMARY: {passed}/{len(checks)} checks PASS")
if failed: log(f"FAILURES: {failed}")
OUT.write_text("\n".join(lines)+"\n",encoding="utf-8")
payload={"spark":"spark_20261110_154351_a10e80","interpreter":sys.executable,"mpmath_dps":mp.mp.dps,
         "checks_total":len(checks),"checks_passed":passed,"checks_failed":failed,"checks":checks,"wall_rows":rows,
         "verdict":"For every p>0 the mixed-region first hit is finite and spacelike; M=0 gives the exact line xm=-(sqrt(1+p)-1)xp. The past-AdS2 Kim-Son branch therefore does not absorb sustained one-sided positive flux without an RST wall."}
SUMMARY.write_text(json.dumps(payload,indent=2)+"\n",encoding="utf-8")
sys.exit(1 if failed else 0)
