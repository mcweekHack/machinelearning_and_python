import numpy as np
import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d as  A3D
import datam
import FunctionGather as Fun
from matplotlib import cm
#*******************************
[x,y,z] = datam.Get_data(10,0)
Fun.Spot_map_Create(x,y,z)
Fun.equation_Create(x,y,z)
plt.show()
