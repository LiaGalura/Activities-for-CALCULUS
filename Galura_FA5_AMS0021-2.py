import sympy as sp
sp.init_printing(use_unicode=True)

x = sp.symbols('x')
y = sp.Function('y')(x)

# ---------------- 1. PRODUCT RULE ----------------
print("\n=== 1. PRODUCT RULE ===")

u = 2*x**2 + 3*x
v = x**3 - 1

print("\nGiven:")
sp.pprint(sp.Eq(sp.Symbol('y'), u*v), use_unicode=True)

du = sp.diff(u, x)
dv = sp.diff(v, x)

print("\nUsing Product Rule: (uv)' = u'v + uv'")
print("u' ="); sp.pprint(du)
print("v' ="); sp.pprint(dv)

term1 = du*v
term2 = u*dv

print("\nSubstitute:")
sp.pprint(term1 + term2)

dy1 = sp.simplify(term1 + term2)

print("\nFinal Answer:")
sp.pprint(sp.Eq(sp.Symbol("dy/dx"), dy1))


# ---------------- 2. QUOTIENT RULE ----------------
print("\n=== 2. QUOTIENT RULE ===")

u = x**2 + 1
v = x**3 - x

print("\nGiven:")
sp.pprint(sp.Eq(sp.Symbol('y'), u/v))

du = sp.diff(u, x)
dv = sp.diff(v, x)

print("\nUsing Quotient Rule:")
print("(u/v)' = (u'v - uv') / v^2")

num = du*v - u*dv
den = v**2

print("\nNumerator:")
sp.pprint(num)

print("\nDenominator:")
sp.pprint(den)

dy2 = sp.simplify(num/den)

print("\nFinal Answer:")
sp.pprint(sp.Eq(sp.Symbol("dy/dx"), dy2))


# ---------------- 3. CHAIN RULE ----------------
print("\n=== 3. CHAIN RULE ===")

inner = 4*x**2 - 5

print("\nGiven:")
sp.pprint(sp.Eq(sp.Symbol('y'), inner**3))

d_inner = sp.diff(inner, x)

print("\nUsing Chain Rule: (f(g(x)))' = f'(g(x))g'(x)")
print("Inner derivative:")
sp.pprint(d_inner)

dy3 = 3*(inner**2)*d_inner

print("\nFinal Answer:")
sp.pprint(sp.Eq(sp.Symbol("dy/dx"), sp.simplify(dy3)))


# ---------------- 4a. EXPONENTIAL ----------------
print("\n=== 4a. EXPONENTIAL ===")

inner = 2*x**2

print("\nGiven:")
sp.pprint(sp.Eq(sp.Symbol('y'), sp.exp(inner)))

d_inner = sp.diff(inner, x)

print("\nUsing: (e^u)' = u'e^u")
sp.pprint(d_inner)

dy4a = d_inner * sp.exp(inner)

print("\nFinal Answer:")
sp.pprint(sp.Eq(sp.Symbol("dy/dx"), sp.simplify(dy4a)))


# ---------------- 4b. LOGARITHMIC ----------------
print("\n=== 4b. LOGARITHMIC ===")

inner = x**2 + 3*x + 1

print("\nGiven:")
sp.pprint(sp.Eq(sp.Symbol('y'), sp.log(inner)))

d_inner = sp.diff(inner, x)

print("\nUsing: (ln u)' = u'/u")
sp.pprint(d_inner)

dy4b = d_inner / inner

print("\nFinal Answer:")
sp.pprint(sp.Eq(sp.Symbol("dy/dx"), sp.simplify(dy4b)))


# ---------------- 5. COMBINED RULES ----------------
print("\n=== 5. COMBINED RULES ===")

f5 = (x**2 + 1)**3 / sp.sqrt(2*x + 5)

print("\nGiven:")
sp.pprint(sp.Eq(sp.Symbol('y'), f5))

print("\nRewrite:")
sp.pprint((x**2 + 1)**3 * (2*x + 5)**(-sp.Rational(1,2)))

dy5 = sp.diff(f5, x)

print("\nApplying Product + Chain Rules:")

print("\nFinal Answer:")
sp.pprint(sp.Eq(sp.Symbol("dy/dx"), sp.simplify(dy5)))


# ---------------- 6. IMPLICIT DIFFERENTIATION ----------------
print("\n=== 6. IMPLICIT DIFFERENTIATION ===")

y = sp.Function('y')(x)

eq = x**2 + x*y + y**2 - 7

print("\nGiven:")
sp.pprint(sp.Eq(x**2 + x*y + y**2, 7))

print("\nDifferentiate BOTH sides w.r.t x:")

d_eq = sp.diff(eq, x)
sp.pprint(d_eq)

print("\nJustification:")
print("d(x^2)/dx = 2x")
print("d(xy)/dx = x(dy/dx) + y   (Product Rule)")
print("d(y^2)/dx = 2y(dy/dx)     (Chain Rule)")

dy = sp.symbols('dy_dx')

# replace derivative symbol for clarity
expr = d_eq.replace(sp.diff(y, x), dy)

print("\nSubstitute dy/dx as dy_dx:")
sp.pprint(expr)

print("\nGroup dy/dx terms:")

# manually rearrange
solution = sp.solve(d_eq, sp.diff(y, x))[0]

print("\nFinal Answer:")
sp.pprint(sp.Eq(sp.Symbol("dy/dx"), sp.simplify(solution)))

