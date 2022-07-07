import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 2 * np.pi, 100)

y1 = np.sin(x)
y2 = np.cos(x)

fig = plt.figure(figsize=(9, 5))

axis1 = fig.add_subplot(221)
axis1.plot(x, y1)
axis1.set_title("sinx(x)")

axis2 = fig.add_subplot(222)
axis2.plot(x, y2)
axis2.set_title("cos(x)")

axis3 = fig.add_subplot(223)
axis3.plot(x, y1 + y2)
axis3.set_title("sin(x) + cos(x)")

axis4 = fig.add_subplot(224)
axis4.plot(x, y1 - y2)
axis4.set_title("sin(x) - cos(x)")

fig.tight_layout()

fig.savefig("subplots.png")
