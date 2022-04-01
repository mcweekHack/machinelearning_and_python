import numpy as np
import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d as  A3D
import datam
from matplotlib import cm
#------------------------------------------------
def Spot_map_Create(x,y,z):#显示数据集函数
    fig = plt.figure("mark")
    ax = A3D.Axes3D(fig)
    ax.set_xlabel("x-bar")
    ax.set_ylabel("y-bar")
    ax.set_zlabel("z-bar")
    ax.scatter(x,y,z)
def equation_Create(x1,y1,z1):#两参数代价函数生成(适用于过零点的数据集)
    val1 = sum(x1*x1)
    val2 = sum(y1*y1)
    val3 = sum(z1*z1)
    val1_val2 = sum(x1*y1)
    val3_val1 = sum(z1*x1)
    val3_val2 = sum(z1*y1)
    xs = np.arange(0,1,0.1)
    ys = np.arange(0,1,0.1)
    xs,ys = np.meshgrid(xs, ys)
    length = x1.shape
    equation = (xs*xs*val1+2*xs*ys*val1_val2+ys*ys*val2-2*xs*val3_val1-2*ys*val3_val2+val3)/length[0]
    fig = plt.figure()
    axe = A3D.Axes3D(fig)
    axe.set_xlabel("x1-value")
    axe.set_ylabel("x2-value")
    axe.set_zlabel("disparity")
    axe.plot_surface(xs,ys,equation,rstride = 1,cstride = 1,cmap = cm.coolwarm)
    return 0