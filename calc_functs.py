from sympy import *

# calculating derviatives


x = Symbol('x')
y = Symbol('y')
z = Symbol('z')

def f(x):
    return (x**4 + x**3 + x**2 + x + 1)

def g(x):
    return (sin(x) + cos(x))

def h(x):
    return (sin(x)*exp(x) + 2 * x)

print("The derivative of f(x) is: ", diff(f(x), x))
print("The derivative of g(x) is: ", diff(g(x), x))
print("The derivative of h(x) is: ", diff(h(x), x))
      

# finding the value of first deriv determines whether funct is increasing or decreasing
# to solve the deriv by plugging in (arbitrary value 3):

print("The value of the derivative of f(x) is: ", diff(f(x), x).subs(x, 3))

# can also calculate higher order derivs by specifiying order of differentiation

print("The second derivative of f(x) is: ", diff(f(x), x, 2)) #third arg can be the order of deriv
print("The third derivative of g(x) is: ", diff(g(x), x, x, x)) #can also include variable that many times as the next arg

#can also calculate partial derivatives

def q(x, y):
    return (y**2)*x*3 + (x**2)*y*2

t =  q(x, y)

print("dt/dy = ", diff(t, y))
print("dt/dx = ", diff(t, x))


# sympy also supports integration

print("The integral of f(x) is: ", integrate(f(x), x))
print("The integral of g(x) is: ", integrate(g(x), x))
print("The integral of h(x) is: ", integrate(h(x), x))

# can calculate a definite integral by specifying the lower bound, upper bound

print("The definite integral of f(x) from 0 to 2 is: ", integrate(f(x), (x, 0, 2)).evalf(3))

#can also do improper

print("The integral of g(x) from 0 to infinity is: ", integrate(g(x), (x, 0, oo)))


#you can calculate multiple integrals
#multiple indefinite:

def s(x, y, z):
    return x**2 + y + z**3

indefi_integ = integrate(s(x, y, z), x, y, z)
print(indefi_integ)

#for multiple definite

def_integ = integrate(s(x, y, z), (x, 0, 6), (y, -4, 3), (z, -1, 1))
print(def_integ)

#you can even solve limits

def exam_limit(x):
    return sin(x) / x

print("The limit of function 'exam limit' is: ", limit(exam_limit(x), x, 0))
# the third variable of the limit funct specifies where x-> 0

# you can calculate limits from different directions too

print("limit from the right is: ", limit(exam_limit(x), x, 0, '+'))
print("limit from the left is: ", limit(exam_limit(x), x, 0, '-'))


# can work with series (calc 2) as well

print("Taylor series for sin(x): ", series(sin(x), x))
print("Taylor series for cos(x): ", cos(x).series(x))

print("The formal power series of e^x is: ", fps(exp(x), x, 0).truncate(5))

# sympy can be used to actually solve equations

#single solution ex

def o(x):
    return 2*x + 7
print(solve(o(x), x))

# mult solutions

def p(x):
    return x**2 -2*x - 4

print(solve(p(x), x))

#computing intervals that are defined


print(solve(o(x) > 0, x))
print(solve(p(x) > 0, x))

# you can also solve trig equations fr fr

print(solve(g(x), x))

#to solve a system of equations, just plug em all in


# now some functs and properties that apply to ordinary differential eqs

#this defines function fu of symbol x
fu = Function('fu')(x)

print(fu.diff(x))
print(fu.diff(x, x))

# dsolve() is used to solve the ordinary diff eqs

