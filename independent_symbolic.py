#!/usr/bin/env python3
"""Independent exact-symbolic review for the Kim-Son review package.

This script does not import or execute verify.py. It independently checks the
load-bearing polynomial, causal, horizon, pulse, and observer identities.
"""
from pathlib import Path
import json
import sympy as sp

ROOT = Path(__file__).resolve().parent
OUT_DIR = ROOT / "outputs"
OUT_DIR.mkdir(parents=True, exist_ok=True)
checks = []

def check(name, ok, detail=""):
    row = {"name": name, "status": "PASS" if bool(ok) else "FAIL", "detail": str(detail)}
    checks.append(row)
    print(f"{row['status']} | {name}" + (f" | {detail}" if detail else ""))

x, y, p, mu, a = sp.symbols("x y p mu a", positive=True)
F = mu + y**2/2 + x*y - p*x**2/2
D = sp.sqrt((1+p)*y**2 + 2*p*mu)
x_hit = (y+D)/p
slope = -D/(x_hit+y)
check("sustained root residual", sp.simplify(F.subs(x,x_hit)) == 0)
other = -(y**2+2*mu)/(y+D)
check("negative other root", sp.simplify((y-D)/p-other) == 0 and other.is_negative is True)
check("positive selected root", x_hit.is_positive is True)
check("apparent-horizon ordering", sp.simplify(x_hit-y/p-D/p) == 0 and (D/p).is_positive is True)
check("spacelike mixed tangent", slope.is_negative is True)
check("zero-flux regularity", sp.simplify(F.subs(p,0)).is_positive is True)
post = mu/x - p*x/2
x0 = sp.sqrt(2*mu/p)
check("post interface position", sp.simplify(post.subs(x,x0)) == 0)
check("post interface slope", sp.simplify(sp.diff(post,x).subs(x,x0)+p) == 0)
wall_xm = x - sp.sqrt((1+p)*x**2 - 2*mu)
G = mu - x*sp.symbols("xm", real=True) + sp.symbols("xm", real=True)**2/2 - p*x**2/2
check("global wall representation", sp.simplify(G.subs(sp.symbols("xm", real=True),wall_xm)) == 0)

# Conformal factor at the RST minimum.
kap = sp.symbols("kappa", positive=True)
phi = sp.symbols("phi", positive=True)
Omega_phi = sp.exp(-2*phi)/sp.sqrt(kap) + sp.sqrt(kap)*phi/2
critical = sp.solve(sp.diff(Omega_phi,phi),sp.exp(-2*phi))[0]
check("finite conformal factor at Omega_s", sp.simplify(1/critical-4/kap) == 0)

# Original impulsive source and its restricted ray band.
F_imp = mu + y**2/2 + x*(y-a)
x_imp = sp.solve(F_imp,x)[0]
h = sp.symbols("h", positive=True)
check("impulsive root and positive ray band", sp.simplify(F_imp.subs(x,x_imp)) == 0 and x_imp.subs(a,y+h).is_positive is True)
slope_imp = (y-a)/(x_imp+y)
check("impulsive causal sign", (y-a).subs(a,y+h).is_negative is True and x_imp.subs(a,y+h).is_positive is True)
check("impulsive branch join", sp.simplify(x_imp.subs(y,0)-mu/a) == 0 and sp.simplify(slope_imp.subs(y,0)+a**2/mu) == 0)

# Alternate retained-t+ data: a mixed-ray threshold, not an all-wall theorem.
F_alt = mu + y**2/2 + x*y + (1-p)*x**2/2
D_alt = sp.sqrt(p*y**2 + 2*(p-1)*mu)
x_alt = (y+D_alt)/(p-1)
check("alternate state p=1 has no mixed wall", (mu+x*y+y**2/2).is_positive is True)
r = sp.symbols("r", positive=True)
check("alternate state p<1 coefficient is positive", sp.simplify(1-1/(1+r)).is_positive is True and sp.simplify((1-1/(1+r))/2-r/(2*(1+r))) == 0 and sp.simplify(F_alt.subs(p,1+p)-F) == 0)
q = sp.symbols("q", positive=True)
other_alt = -(y**2+2*mu)/(y+D_alt)
Dpos = sp.symbols("Dpos", positive=True)
check("alternate state p>1 has a positive mixed hit and negative other root", sp.simplify(F_alt.subs(x,x_alt)) == 0 and x_alt.subs(p,1+q).is_positive is True and sp.simplify((y-D_alt)/(p-1)-other_alt) == 0 and (y+Dpos).is_positive is True and (-(y**2+2*mu)).is_negative is True)
G_alt = mu - x*sp.symbols("xm", real=True) + (1-p)*x**2/2
check("alternate p=1 retains a both-positive wall", sp.simplify(G_alt.subs(p,1).subs(sp.symbols("xm", real=True),mu/x)) == 0)

# Finite pulse and its complete ray cutoff.
s, E = sp.symbols("x_s E", positive=True)
F_during = mu + y**2/2 + x*y - p*x**2/2
F_after = mu + y**2/2 + E*s/2 + x*(y-E)
check("pulse C0 at shutoff", sp.simplify((F_during-F_after).subs(x,s).subs(E,p*s)) == 0)
check("pulse C1 at shutoff", sp.simplify((sp.diff(F_during,x)-sp.diff(F_after,x)).subs(x,s).subs(E,p*s)) == 0)
x_after = sp.solve(F_after,x)[0]
check("pulse after-shutoff root and post-shutoff inequality", sp.simplify(x_after-(mu+E*s/2+y**2/2)/(E-y)) == 0 and sp.simplify((x_after-s).subs(E,p*s)-(F_during.subs(x,s)/(E-y)).subs(E,p*s)) == 0)
slope_after = (y-E)/(x_after+y)
check("pulse after-shutoff exact negative tangent", sp.simplify(F_after.subs(x,x_after)) == 0 and (y-E).subs(E,y+h).is_negative is True and x_after.subs(E,y+h).is_positive is True)
y_max = -s + sp.sqrt((1+p)*s**2-2*mu)
check("pulse y_max M=0 limit and x_hit monotonicity", sp.simplify(y_max.subs(mu,0)-s*(sp.sqrt(1+p)-1)) == 0 and sp.simplify(sp.diff(x_hit,y)).is_positive is True)
z_during = mu/x - p*x/2
z_after = (mu+E*s/2)/x - E
check("pulse both-positive position match", sp.simplify((z_during-z_after).subs(x,s).subs(E,p*s)) == 0)
x_after_zero = s/2 + mu/E
check("pulse both-positive slope match and sign-domain", sp.simplify((sp.diff(z_during,x)-sp.diff(z_after,x)).subs(x,s).subs(E,p*s)) == 0 and sp.simplify(z_after.subs(x,x_after_zero)) == 0 and sp.simplify(z_after-E*(x_after_zero/x-1)) == 0 and sp.simplify((x_after_zero-s)-(2*mu-E*s)/(2*E)) == 0 and sp.simplify(z_after.subs({p:1,mu:10,s:3,E:3,x:4})-sp.Rational(5,8)) == 0 and sp.simplify(z_after.subs({p:1,mu:10,s:3,E:3,x:5})+sp.Rational(1,10)) == 0)
check("pulse apparent-horizon continuation and during crossing", sp.simplify(((y-p*x)-y+E).subs(x,s).subs(E,p*s)) == 0 and sp.simplify((E-y)/p).subs(E,y+h).is_positive is True)
# General cumulative-flux derivative and an exponential finite-flux example.
xx, u = sp.symbols("x_q u_q", positive=True)
Tq = sp.Function("T_q", positive=True)
Qq = sp.Integral(Tq(u), (u, 0, xx))
Iq = sp.Integral((xx-u)*Tq(u), (u, 0, xx))
lam = sp.symbols("lambda", positive=True)
Fq_general = mu + y**2/2 + xx*y - Iq/lam**2
general_slope = -(Qq-y)/(xx+y)
check("cumulative derivative, concavity, corrected slope, and horizon ordering", sp.simplify(sp.diff(Fq_general,xx)-(y-Qq/lam**2)) == 0 and sp.simplify(sp.diff(Fq_general,xx,2)+Tq(xx)/lam**2) == 0 and general_slope.subs(Qq,y+h).is_negative is True and (Qq-y).subs(Qq,y+h).is_positive is True)
Aq = sp.symbols("A_flux", positive=True)
Texp = Aq*sp.exp(-u)
Iexp = sp.integrate((xx-u)*Texp,(u,0,xx))
Fexp = sp.simplify(mu + y**2/2 + xx*y - Iexp/lam**2)
Fprime_exp = sp.simplify(sp.diff(Fexp,xx))
z_delay, d_delay = sp.symbols("z_delay d_delay", positive=True)
F_delay = mu + y**2/2 + (z_delay+d_delay)*y - Aq*(z_delay-1+sp.exp(-z_delay))
check("exponential total-flux cutoff", sp.simplify(Iexp-Aq*(xx-1+sp.exp(-xx))) == 0 and sp.limit(Fexp.subs(lam,1).subs(y,Aq/2),xx,sp.oo) == -sp.oo and sp.simplify(Fprime_exp.subs(lam,1).subs(y,Aq)-Aq*sp.exp(-xx)) == 0 and sp.simplify(Fprime_exp.subs(lam,1).subs(y,Aq+h)-Aq*sp.exp(-xx)-h) == 0 and sp.limit(Fexp.subs(lam,1).subs(y,2*Aq),xx,sp.oo) == sp.oo and sp.limit(F_delay.subs(y,Aq/2),z_delay,sp.oo) == -sp.oo and sp.simplify(sp.diff(F_delay,z_delay).subs(y,Aq)-Aq*sp.exp(-z_delay)) == 0)

# Signed accumulated-excess and finite-sigma-support adversarial cases.
xs = sp.symbols("x_signed", positive=True)
Cf = sp.symbols("C_focus", positive=True)
A_linear = Cf*xs
root_linear = sp.solve(Cf-A_linear,xs)[0]
check("signed positive linear unique hit", root_linear == 1 and (Cf-A_linear).subs(xs,sp.Rational(1,2)).is_positive is True and (Cf-A_linear).subs(xs,2).is_negative is True)
A_unattained = Cf*(1-sp.exp(-xs))
check("signed unattained threshold no finite hit", sp.limit(A_unattained,xs,sp.oo) == Cf and sp.simplify(Cf-A_unattained).is_positive is True and sp.limit(Cf-A_unattained,xs,sp.oo) == 0)
A_quadratic = Cf*(2*xs-xs**2)
F_quadratic = sp.factor(Cf-A_quadratic)
check("signed quadratic tangential contact", sp.simplify(F_quadratic-Cf*(xs-1)**2) == 0 and F_quadratic.subs(xs,1) == 0 and F_quadratic.is_nonnegative is True and sp.diff(F_quadratic,xs).subs(xs,1) == 0)
A_cusp = Cf*(1-sp.Abs(xs-1))
F_cusp = sp.simplify(Cf-A_cusp)
check("signed cusp one-sided causal signs", sp.simplify(F_cusp-Cf*sp.Abs(xs-1)) == 0 and sp.diff(F_cusp,xs).subs(xs,sp.Rational(1,2)) == -Cf and sp.diff(F_cusp,xs).subs(xs,sp.Rational(3,2)) == Cf and F_cusp.subs(xs,1) == 0 and F_cusp.is_nonnegative is True)
Pcal, xa, xb = sp.symbols("mathcalP x_a x_b", positive=True)
E_sigma = Pcal/lam**4*(1/xa-1/xb)
Tpp_sigma = Pcal/(lam**2*xs**2)
h_x = sp.symbols("h_x", positive=True)
check("finite sigma pulse cumulative flux", sp.simplify(sp.integrate(Tpp_sigma/lam**2,(xs,xa,xb))-E_sigma) == 0 and sp.simplify(E_sigma.subs(xb,xa+h_x)).is_positive is True)

# Review regressions: large mu with no real during bound, and shutoff equality.
p_large, s_large, mu_large, y_large = sp.Integer(1), sp.Integer(1), sp.Integer(10), sp.Rational(1,2)
E_large = p_large*s_large
x_large = (mu_large+y_large**2/2+E_large*s_large/2)/(E_large-y_large)
check("large-mu nonreal-y_max post-shutoff hit", (1+p_large)*s_large**2-2*mu_large < 0 and x_large == sp.Rational(85,4) and x_large > s_large)
y_eq = -2+sp.sqrt(sp.Rational(38,5))
E_eq = sp.Integer(2)
D_eq = sp.sqrt(2*y_eq**2+sp.Rational(2,5))
x_d_eq = y_eq+D_eq
x_a_eq = (sp.Rational(1,5)+y_eq**2/2+E_eq)/(E_eq-y_eq)
check("shutoff equality x_after=x_during=x_s", abs(sp.N(x_d_eq-2,50)) < 1e-45 and abs(sp.N(x_a_eq-2,50)) < 1e-45)

# Null affine parameter and the explicit interior observer chart.
lam, rho, C = sp.symbols("lambda rho C", positive=True)
rho_x = sp.Function("rho_x")
v_null = C*sp.exp(-2*rho_x(x))
check("null affine relation and geodesic ODE", sp.simplify(sp.diff(v_null,x)+2*rho_x(x).diff(x)*v_null) == 0 and sp.simplify(sp.diff(sp.log(C*sp.exp(-2*rho)),rho)+2) == 0)
sig0, sig1 = sp.symbols("sigma0 sigma1", real=True)
xp_sig = sp.exp(lam*(sig0+sig1))
xm_sig = -sp.exp(-lam*(sig0-sig1))
m00 = sp.simplify(sp.diff(xp_sig,sig0)*sp.diff(xm_sig,sig0))
m11 = sp.simplify(sp.diff(xp_sig,sig1)*sp.diff(xm_sig,sig1))
m01 = sp.simplify(sp.diff(xp_sig,sig0)*sp.diff(xm_sig,sig1)+sp.diff(xp_sig,sig1)*sp.diff(xm_sig,sig0))
check("observer metric coefficients", m01 == 0 and sp.simplify(m00-lam**2*sp.exp(2*lam*sig1)) == 0 and sp.simplify(m00+m11) == 0)
K = sp.symbols("K", positive=True)
rK = 1 + mu/K
R_wall = sp.sqrt(rK**2+p) - rK
check("observer wall root", sp.simplify(K*R_wall**2 + 2*(K+mu)*R_wall-K*p) == 0)
check("observer R coordinate", sp.simplify((-xm_sig/xp_sig)-sp.exp(-2*lam*sig0)) == 0)
check("observer M=0 root matches global wall", sp.simplify(R_wall.subs(mu,0)-(sp.sqrt(1+p)-1)) == 0)

passed = sum(row["status"] == "PASS" for row in checks)
failed = len(checks)-passed
print(f"INDEPENDENT_SYMBOLIC: {passed}/{len(checks)} PASS")
payload = {"checks_total":len(checks),"checks_passed":passed,"checks_failed":failed,"checks":checks}
(OUT_DIR / "independent-symbolic-summary.json").write_text(json.dumps(payload,indent=2)+"\n",encoding="utf-8")
(OUT_DIR / "independent_symbolic.out").write_text("\n".join(
    [f"{row['status']} | {row['name']}" + (f" | {row['detail']}" if row["detail"] else "") for row in checks]
    + [f"INDEPENDENT_SYMBOLIC: {passed}/{len(checks)} PASS"]
)+"\n",encoding="utf-8")
raise SystemExit(1 if failed else 0)
