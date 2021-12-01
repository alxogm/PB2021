import numpy as np
import matplotlib.pyplot as plt
import sys
data=np.loadtxt(sys.argv[1]).T
x=data[0]
y=data[1]
z=data[2]

plt.plot(x,y)
plt.xlabel("x")
plt.ylabel("y")
plt.savefig(sys.argv[1]+".png")
plt.show()
