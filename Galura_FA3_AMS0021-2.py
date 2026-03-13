import sympy as sp

x = sp.symbols('x')

expr = (x**2 - x - 6)/(x-3)

limit_value = sp.limit(expr, x, 3)

limit_value

import numpy as np
import matplotlib.pyplot as plt

# create x values
x = np.linspace(-3,3,400)

# example function pieces (approximation of graph)
y = np.piecewise(
    x,
    [x < 0, (x >= 0) & (x < 2), x >= 2],
    [lambda x: -2 + (x+1)**2,
     lambda x: 2 - (x-1)**2,
     lambda x: (x-2)**2 - 1]
)

plt.figure(figsize=(6,4))
plt.plot(x,y)

plt.scatter([0],[ -2], facecolors='none', edgecolors='blue')
plt.scatter([2],[1], color='blue')

plt.axhline(0)
plt.axvline(0)

plt.title("Graph of f(x)")
plt.xlabel("x")
plt.ylabel("y")

plt.show()

import sympy as sp

x = sp.symbols('x')

expr = (x**2 - x - 6)/(x - 3)

limit_value = sp.limit(expr, x, 3)

limit_value

import sympy as sp

x = sp.symbols('x')

expr = (4*x**2 + 1)/x

left = sp.limit(expr, x, 0, dir='-')
right = sp.limit(expr, x, 0, dir='+')

left, right

import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-2,2,100)
y = x**2 - 1

plt.plot(x,y)

plt.scatter([0],[-1],color='red') # minimum point

plt.axhline(0)
plt.axvline(0)

plt.title("Example where derivative = 0 at minimum")
plt.show()



