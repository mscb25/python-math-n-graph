# SciPy is a package that contains tools that are built on top of NumPy

import numpy as np
import matplotlib.pyplot as plt
'''import scipy as sc'''
from scipy.integrate import quad, dblquad
from scipy import *
from scipy import optimize
from scipy import fftpack

#creating the same graph in numpy vs scipy
#graph looks the same --> compiler says to use numpy for these functs

np_x = np.arange(0, 2 * np.pi, 0.1)
np_y = np.sin(np_x)

plt.plot(np_x, np_y)
'''
sc_x = sc.arange(0, 2 * sc.pi, 0.1)
sc_y = sc.sin(sc_x)

plt.plot(sc_x, sc_y)
'''

#integration in scipy

def f(x):
    return (2 * sin(x) * cos(x))

value, error = quad(f, 0, pi/2) #calling quad to integrate f from 0 to pi/2
print("Value of integral is: ", value)
print("Error in integral is: ", error)

# can do double/higher order integration too

def g(x, y):
    return x**2 * y

doub_val, doub_err = dblquad(g, 0, 3, lambda x: 0, lambda x:2)
'''
print("Actual val = 18") #calculated by hand
print("Calculated val = ", doub_val)
print("Calculated error = ", doub_err)
'''
# if you want to do triple integral, be sure to also import tplquad()

# interpolation can be done with scipy too

'''
from scipy.interpolate import *

the_funct = interpld(x, y, kind='linear')

'''

# fitting data to a polynomial
# returns an array of the coefficients

r_x = np.arange(-8, 15)
r_y = np.random.randn(len(r_x))
r_z = np.polyfit(r_x, r_y, 3) #last val is saying i want a polynomial of order 3

print(r_z)


#to compute the best possile polynomial that fits raw data, you need to see which has the least amount of error
# can be calculated with RMSE()

# curvefit() can be used to fit an arbitary function

# optimize package is imported and used to calculate min and max

#fmin takes in two arguments: 1. the function to minimize 2. inital val to start searching for the minimum

def o(x):
    return sin(x) - (2 * exp(-(x - 0.5)**2))

opt_x = arange(-8, 8, 0.1)
opt_y = o(x)

point1 = -1.0
point2 = 3.0

min1 = optimize.fmin(o, point1) #fmin() returns a NumPy array that contains one number
min2 = optimize.fmin(o, point2)
'''from there you can graph to see the representation'''

# can additionally find the minimum of a funct in a given range

minima = optimize.fminbound(o, point1, point2)


# can calculate Fourier transform, which expresses a funct as a weighted sum of sinusoids
# computed with fft() and inverse transform with ifft()
