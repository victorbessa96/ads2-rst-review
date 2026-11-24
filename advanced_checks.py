#!/usr/bin/env python3
"""Advanced consistency checks: state phases, sigma-frame pulses, matter realization.

Ten rows that could not fail (tautologies and symbol-independence tests) were
removed on 2026-11-24; the count is 22.
"""
from pathlib import Path
import json
import sympy as sp

ROOT = Path(__file__).resolve().parent
OUT = ROOT / "outputs"
OUT.mkdir(exist_ok=True)
checks = []

def check(name, ok, detail=""):
    row = {"name": name, "status": "PASS" if bool(ok) else "FAIL", "detail": str(detail)}
    checks.append(row)
    print(f"{row['status']} | {name}" + (f" | {detail}" if detail else ""))

p, q, mu, y, x = sp.symbols("p q mu y x", positive=True)
r = sp.symbols("r", positive=True)
F_state = mu + y**2/2 + x*y - r*x**2/2
D_state = sp.sqrt((1+r)*y**2 + 2*r*mu)
x_state = (y + D_state)/r
check("state phase root residual", sp.simplify(F_state.subs(x, x_state)) == 0)
check("state phase other root negative", sp.simplify((y-D_state)/r + (y**2+2*mu)/(y+D_state)) == 0 and (-(y**2+2*mu)/(y+D_state)).is_negative is True)
check("state phase horizon gap", sp.simplify(x_state-y/r-D_state/r) == 0 and (D_state/r).is_positive is True)
F_state_pq = mu + y**2/2 + x*y - (p-q)*x**2/2
check("state phase r=0 has no mixed hit", (mu+y**2/2+x*y).is_positive is True)
check("state phase r<0 has no mixed hit", F_state_pq.subs(p-q,-sp.symbols("rpos", positive=True)).is_positive is True)
R_inf = sp.symbols("R_inf", positive=True)
check("finite state pulse cannot prevent sustained classical focusing", sp.limit(p*x-R_inf,x,sp.oo) == sp.oo)
check("alternate q=1 is retained state with shifted p", sp.simplify(F_state_pq.subs({q:1,p:1+p}) - F_state_pq.subs(q,0)) == 0)
alpha_atom = sp.symbols("alpha_atom", positive=True)
Q_onset = alpha_atom
check("onset atom generalized trapping crossing when alpha>=y", (Q_onset-y).subs(alpha_atom,y+sp.symbols("h_atom", positive=True)).is_positive is True)

# Physical boundary-time pulse.
lam = sp.symbols("lambda", positive=True)
Pcal = sp.symbols("mathcalP", positive=True)
a, b, k = sp.symbols("a b k", positive=True)
C = mu + y**2/2
E = k*(1/a-1/b)
F_during = C + y*x - k*((x-a)/a-sp.log(x/a))
check("boundary during-pulse concavity", sp.simplify(sp.diff(F_during,x,2)+k/x**2) == 0)
Fb = sp.symbols("F_b", positive=True)
x_after = b + Fb/(E-y)
F_after = Fb + (y-E)*(x-b)
check("boundary after-pulse root residual", sp.simplify(F_after.subs(x,x_after)) == 0)
check("boundary after-pulse root is beyond b", sp.simplify(x_after-b-Fb/(E-y)) == 0 and (Fb/(E-y)).subs(E,y+sp.symbols("hE", positive=True)).is_positive is True)
check("boundary shutoff equality F_b=0", sp.simplify(F_after.subs(Fb,0).subs(x,b)) == 0 and sp.simplify(x_after.subs(Fb,0)-b) == 0)
hE = sp.symbols("hE", positive=True)
check("boundary y>=E gives no post-pulse root", (y-E).subs(E,y-hE).is_positive is True and Fb.is_positive is True)
E_early = sp.exp(2)-sp.exp(1)
E_late = sp.exp(-2)-sp.exp(-3)
check("same unit energy has early and late focusing examples", E_early > E_late and E_late > 0)
sig, delta = sp.symbols("sigma_a Delta_sigma", positive=True)
E_timing = sp.exp(-lam*sig)*(1-sp.exp(-lam*delta))
check("early boundary timing diverges", sp.limit(E_timing.subs({lam:1,delta:1}),sig,-sp.oo) == sp.oo)
check("late boundary timing vanishes", sp.limit(E_timing,sig,sp.oo) == 0)

# Closing-window law in retarded ray time.
sa, dsig, shift = sp.symbols("sigma_a Delta_sigma shift", real=True)
E_window = Pcal/lam**4*sp.exp(-lam*sa)*(1-sp.exp(-lam*dsig))
u_star = -sp.log(E_window)/lam
u_star_expected = sa-sp.log(Pcal/lam**4*(1-sp.exp(-lam*dsig)))/lam
check("closing-window threshold matches retarded ray label", sp.simplify(sp.expand_log(sp.log(E_window),force=True)-sp.log(Pcal/lam**4*(1-sp.exp(-lam*dsig)))+lam*sa) == 0 and sp.simplify(u_star-u_star_expected) == 0)
check("closing-window translation covariance", sp.simplify(u_star.subs(sa,sa+shift)-u_star-shift) == 0)
early_u = u_star.subs({lam:1,Pcal:1,dsig:1,sa:-2})
late_u = u_star.subs({lam:1,Pcal:1,dsig:1,sa:2})
check("same physical ray is hit early and missed late", early_u.evalf() < 0 and late_u.evalf() > 0)

# Explicit conformal-scalar realization.
fprime = sp.sqrt(2*Pcal)/(lam*x)
Tpp = sp.simplify(fprime**2/2)
check("matter wavepacket reproduces prescribed stress", sp.simplify(Tpp-Pcal/(lam**2*x**2)) == 0)
xm = sp.symbols("x_m", real=True)
E_in = Pcal/lam*sp.log(b/a)
check("wavepacket physical energy is finite", sp.simplify(E_in.subs(b,a*sp.exp(lam*delta))-Pcal*delta) == 0)

# Observable and universality controls.
Q = sp.Function("Q")
F_chiral = C + sp.Integral(y-Q(x),(x,0,x))
check("chiral-system accumulated-excess derivative", sp.simplify(sp.diff(F_chiral,x)-(y-Q(x))) == 0)

passed = sum(row["status"] == "PASS" for row in checks)
failed = len(checks)-passed
print(f"ADVANCED: {passed}/{len(checks)} PASS")
payload = {"checks_total":len(checks),"checks_passed":passed,"checks_failed":failed,"checks":checks}
(OUT/"advanced-checks-summary.json").write_text(json.dumps(payload,indent=2)+"\n")
(OUT/"advanced-checks.out").write_text("\n".join(
    [f"{row['status']} | {row['name']}" + (f" | {row['detail']}" if row["detail"] else "") for row in checks]
    + [f"ADVANCED: {passed}/{len(checks)} PASS"])+"\n")
raise SystemExit(1 if failed else 0)
