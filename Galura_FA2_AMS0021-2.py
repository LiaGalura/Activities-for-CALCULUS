import sympy as sp
p = sp.symbols('p')

q = -0.5*p + 140
R = p * q
R = sp.expand(R)
R
dR = sp.diff(R, p)
dR
price = sp.solve(dR, p)
price
max_revenue = R.subs(p, price[0])
max_revenue
float(max_revenue)

import sympy as sp

a, b = sp.symbols('a b')
eq1 = sp.Eq(a*b**2, 36)
eq2 = sp.Eq(a*b**4, 324)
solution = sp.solve((eq1, eq2), (a, b))
solution
a_val, b_val = solution[0]
y = a_val * b_val**sp.symbols('x')
y
float(a_val), float(b_val)

import sympy as sp

# Define the variable
x = sp.symbols('x')

# Define the equation
eq = sp.Eq(63**(x+1), 30)

# Solve the equation
solution = sp.solve(eq, x)

solution

float(solution[0])

import sympy as sp

# Define variable
t = sp.symbols('t')

# Given values
P = 500
A = 700
r = 0.10

# Continuous compounding equation
eq = sp.Eq(A, P * sp.exp(r*t))

# Solve for time
solution = sp.solve(eq, t)

solution

round(float(solution[0]), 4)

import sympy as sp

# Define variable
t = sp.symbols('t')

# Given values
A = 5000
r = 0.10

# Exponential function
f = A * sp.exp(r*t)

f

import sympy as sp

# define symbols
A, b, x = sp.symbols('A b x')

# initial value
A_val = 4.5

# condition: triples every 0.5 increase
eq = sp.Eq(b**0.5, 3)

# solve for b
b_val = sp.solve(eq, b)[0]

# function
f = A_val * b_val**x
f



