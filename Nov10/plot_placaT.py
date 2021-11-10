import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
import sys

for i in range(1,len(sys.argv)):
    filename=sys.argv[i]
    data_img=np.loadtxt(filename)
    plt.imshow(data_img)
    plt.colorbar()
    plt.savefig(filename+'.png')
    plt.show()
