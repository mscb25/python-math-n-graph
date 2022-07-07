import numpy as np
import matplotlib.pyplot as plt

#plotting multiple curves on the same graph


x = np.linspace(0, 2 * np.pi, 100)
y1 = np.sin(x)
y2 = np.cos(x)

plt.plot(x, y1) #curve 1
plt.plot(x, y2) #curve 2
plt.plot(x, y1 + y2) #curve 3

plt.legend(["sin(x)", "cos(x)", "sin(x) + cos(x)"], loc=2)

plt.savefig("multiple.png")
