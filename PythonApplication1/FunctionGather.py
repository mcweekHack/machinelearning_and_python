import numpy as np
import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d as  A3D
import datam
#------------------------------------------------
def Spot_map_Create(x,y,z):#��ʾ���ݼ�����
    fig = plt.figure("mark")
    ax = A3D.Axes3D(fig)
    ax.set_xlabel("x-bar")
    ax.set_ylabel("y-bar")
    ax.set_zlabel("z-bar")
    ax.scatter(x,y,z)
    plt.show()
def equation_Create(x1,y1,z1):#���ۺ�������

    return 0