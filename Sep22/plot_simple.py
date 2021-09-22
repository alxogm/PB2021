import numpy as np
import matplotlib.pyplot as plt

data=np.loadtxt("parabola.txt").T
x=data[0]
y=data[1]

plt.plot(x,y)
plt.xlabel("x")
plt.ylabel("y")
plt.savefig("parabola.png")
