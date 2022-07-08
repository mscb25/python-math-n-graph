#when doing mathematical operations, you often want to use variables like x and y
#symbolic variables allow for this

from sympy import *

x, y, z = symbols('x y z')

print(x + y + z)

#can set properties for a symbol

a = Symbol('a', real = True, positive = True)

# I is the imaginary unit

b = 2 + 5*I

print(b)
print(I**2)

# can subs numbers for the symbols in eq

eq = (2 * y**3) + (z * x**2) + 7 * y
output = eq.subs({'y': 4, 'x': 2, 'z': 3})
print(output)

#to simplify equations:
print(simplify(eq))

# to simplify trig expressions

trig_eq = (2*tan(x) / (1 - tan(x)**2)) + ((1 - cos(2*x)) / 2)

print(trigsimp(trig_eq))


# expanding equations

ex_eq = ((x + 3) * (x - 4) * (x + 8))
print(expand(ex_eq))

#can do factoring as well

fact = expand(ex_eq)
print(factor(fact))

# to convert from Sympy complex to regular python complex, can use funct

c = complex(b)
print("type of c is", type(c))


#for fractions, can use the rational class to represent

print(Rational(1, 4))
print(Rational(7, 3))

#can now perform calculations

print("multiplication: ", Rational(1, 4) * Rational(7, 3))

# evalf converts to a float with a certain level of precision

q = Rational(9, 17)
print(q.evalf(2))


# partial fraction decomposition of rational funct

dec = (67*x**2 + 35*x - 27)/(4*(3*x**3 + 4*x**2 - 7*x - 2))
print(apart(dec))

#can also combine rational functs to a single fraction and factor

tog = 1/x + 1/x + 1/x**2 + 1/x**3
print(together(tog))
