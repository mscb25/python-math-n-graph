import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def spiral(a, b, t):
    x = a * np.cos(t)
    y = a * np.sin(t)
    z = b * t
    return x, y, z


t = np.linspace(0, 20, 100)
x1, y1, z1 = spiral(4, 1, t)
x2, y2, z2 = spiral(2, 2, t)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot(x1, y1, z1)
ax.plot(x2, y2, z2);

fig.savefig('spiral.png')
