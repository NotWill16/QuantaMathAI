from sympy import symbols,factor,expand
x,y = symbols('x y')
expr = x + 2*y
print(expr)
expr = expr -x
print(expr)
expr = x*(expr+1)
print(expr)
print(expand(expr))
print(factor(expand(expr)))