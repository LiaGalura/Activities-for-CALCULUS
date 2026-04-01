import sympy as sp

x = sp.symbols('x')
y = x**2 + x

dy_dx = sp.diff(y, x)
sp.init_printing()
dy_dx

f = x**2 - 3*x + 5
sp.diff(f, x)

r = (3*x)/5 - x**0.3/4 + 5/(2*x**1.4) - 8
sp.diff(r, x)

y = x**10.3/2 + 99*x**(-1)
sp.diff(y, x)

expr = (x**2 + 3*x + 2)/(x**2 + x)
sp.limit(expr, x, -1)

import sympy as sp
from IPython.display import display

sp.init_printing()

t = sp.symbols('t')
N = -180*t**2 + 440*t + 320

dN = sp.diff(N, t)

display(dN)              # shows: -360t + 440
display(dN.subs(t, 2))   # shows: -280



