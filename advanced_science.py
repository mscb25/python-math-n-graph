# Jones calculus - used in optical physics
# light polarization represented by Jones vector, with dimensions 2 x 1
# optical elements represented by Jones matrices, with dimensions 2 x 2

# given a number of matrices, determine the System matrix

import numpy as np

M1 = np.array([[1, -1], [1, 0]])
M2 = np.array([[1, 1], [1, 0]])
M3 = np.array([[1, -1], [1, 1]])
M4 = np.array([[1, 0], [0, 1]])
M5 = np.array([[0, 1], [1, 1]])
M6 = np.array([[1, 0], [0, 1]])

arrays = [M1, M2, M3, M4, M5, M6]

system_matrix = np.array([[1, 0], [0, 1]]) #aka unit matrix

#multiplies all the matrices 
for i in range(len(arrays)):
    system_matrix = np.dot(system_matrix, arrays[i])

print(system_matrix)

# now getting the eigenvalues and eigenvectors

evals, evecs = np.linalg.eig(system_matrix)
print("Eigenvalues: ", evals)
print("Eigenvectors: ", evecs)

# to get the input Jones vector, we solve with the system matrix and the given 2 x 1 vector

out_vector = np.array([-1, 1])

in_vector = np.linalg.solve(system_matrix, out_vector)
print(in_vector)



# Next concept: Transfer functions
# ratio of the output of a system to the input of a system
# the behavior of a system is defined by this transfer function
# either add, subtract, or multiply individual transfer functs to get the transfer funct of the whole system

from sympy import *

s = Symbol('s')

G_start = 1/s
G2 = 1 / (s + 1)
G3 = s / (s + 2)
G4 = 4
G5 = 1 / (s**2 + 1)
G_end = 3*s

transfer = together(G_start * ((G2 * G3) + (G4 * G5)) * G_end)
print(transfer)
