import numpy as np
import scipy.sparse as sp

ex_1 = np.array([[1, 2, 0], [5, 4, -2], [0, -1, 0]])

determ = np.linalg.det(ex_1)
print("the determinant of example 1 on page 202 is: ", determ)
