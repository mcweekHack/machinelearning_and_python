import numpy as np
import matplotlib.pyplot as plt
import dataset
import mpl_toolkits.mplot3d as  A3D
#*******************************
[x,y,z] = dataset.get_beans(100)
fig = plt.figure("mark")
ax = A3D.Axes3D(fig)
ax.set_xlabel("x-bar")
ax.set_ylabel("y-bar")
ax.set_zlabel("z-bar")
ax.scatter(x,y,z)
plt.show()