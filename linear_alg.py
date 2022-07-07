#these are some methods that can be used to solve matrix, systems of eq
#performs cross product and dot product


import numpy as np
import scipy.sparse as sp

A = np.array([[2, 4, 3], [3, 4, 1], [1, 1, -1]])
M = np.array([17, 25, 6])

cross_prod = np.linalg.solve(A, M)
print(cross_prod)

#just to check answer // should get array M as answer

dot_prod = np.dot(A, cross_prod)
print(dot_prod)


#to compute eigenvalues:

eigenval = np.linalg.eigvals(A)
print(eigenval)


#eig method can be used to compute eignvalues and eigenvectors

evals, evecs = np.linalg.eig(A)

print("Eigenvalues", evals)
print("Eigenvectors", evecs)


#for hermitian matrices, use the eigh() method
#same process as above, use when you know matrix is symmetric


#reverse matrix through np.linalg.inv(array mame)

#to get the determinant:

determ = np.linalg.det(A)
print(determ)

#to get the trace of the matrix

trace = np.trace(A)
print(trace)

#to get transpose of the input array

transp = np.transpose(A)
print(transp)

#to get euclidean norm

nrom = np.linalg.norm(A)
print(nrom)


#now for the creation of sparse matrices, aka only the nonzero vals are saved and stored

#dense to sparse

sparse_col = sp.csc_matrix(A)
print("Compressed sparse column: ", sparse_col)

#sparse to dense

sparse_row = sp.csr_matrix(A)
print("compressed sparse row: ", sparse_row)
print("dense matrix: ", sparse_row.todense())
