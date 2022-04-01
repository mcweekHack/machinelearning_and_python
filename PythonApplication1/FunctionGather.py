import numpy as np
import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d as  A3D
import datam
from matplotlib import cm
#------------------------------------------------
def Spot_map_Create(x,y,z):#显示数据集函数
    fig = plt.figure("data set")
    ax = A3D.Axes3D(fig)
    ax.set_xlabel("x-bar")
    ax.set_ylabel("y-bar")
    ax.set_zlabel("z-bar")
    ax.scatter(x,y,z)
    return fig
def equation_Create(x1,y1,z1):#两参数代价函数生成(适用于过零点的数据集)
    val1 = sum(x1*x1)
    val2 = sum(y1*y1)
    val3 = sum(z1*z1)
    val1_val2 = sum(x1*y1)
    val3_val1 = sum(z1*x1)
    val3_val2 = sum(z1*y1)
    xs = np.arange(-10,10,1)
    ys = np.arange(-10,10,1)
    xs,ys = np.meshgrid(xs, ys)
    length = x1.shape
    equation = (xs*xs*val1+2*xs*ys*val1_val2+ys*ys*val2-2*xs*val3_val1-2*ys*val3_val2+val3)/(2*length[0])
    fig = plt.figure("Cost function")
    axe = A3D.Axes3D(fig)
    axe.set_xlabel("x1-value")
    axe.set_ylabel("x2-value")
    axe.set_zlabel("disparity")
    axe.plot_surface(xs,ys,equation,rstride = 1,cstride = 1,cmap = cm.coolwarm)
    return fig
def equation_task(x1,y1,z1,Acceptance):#返回两个未知参数的值,Acceptance表示精度
    Alpha = 0.05
    val1 = sum(x1*x1)
    val2 = sum(y1*y1)
    val3 = sum(z1*z1)
    val1_val2 = sum(x1*y1)
    val3_val1 = sum(z1*x1)
    val3_val2 = sum(z1*y1)
    length = x1.shape
    xs = 0
    ys = 0
    track1 = 0
    traack2 = 0
    while  (xs*xs*val1+2*xs*ys*val1_val2+ys*ys*val2-2*xs*val3_val1-2*ys*val3_val2+val3)/(2*length[0])>Acceptance:
        track = xs - Alpha*(xs*val1+ys*val1_val2-val3_val1)/length[0]
        track2 = ys - Alpha*(ys*val2+xs*val1_val2-val3_val2)/length[0]
        xs = track1
        ys = track2
        print("analysing...")
    print("The model's parameter:",xs,ys)
    return xs,ys
def map_Create_Fun(x2,y2):#画出一个二元1次方程,即验证结果
    xs = np.arange(-10,10,1)
    ys = np.arange(-10,10,1)
    xs,ys = np.meshgrid(xs,ys)
    equation = xs*x2+ys*y2
    fig = plt.figure("Prediction function")
    axe = A3D.Axes3D(fig)
    axe.set_xlabel("x1-value")
    axe.set_ylabel("x2-value")
    axe.set_zlabel("res-value")
    axe.plot_surface(xs,ys,equation,rstride = 1,cstride = 1)
    return 0