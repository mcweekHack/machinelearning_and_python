import numpy as np
import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d as  A3D
import datam
from matplotlib import cm
#------------------------------------------------
#散点图生成
def Spot_map_Create(x,y,z):
    fig = plt.figure("data set")
    ax = A3D.Axes3D(fig)
    ax.set_xlabel("x-bar")
    ax.set_ylabel("y-bar")
    ax.set_zlabel("z-bar")
    ax.scatter(x,y,z)
    return fig
#代价函数生成
def equation_Create(x1,y1,z1):
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
#梯度下降,Acceptance精度
def equation_task(x1,y1,z1,Acceptance):
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
        track1 = xs - Alpha*(xs*val1+ys*val1_val2-val3_val1)/length[0]
        track2 = ys - Alpha*(ys*val2+xs*val1_val2-val3_val2)/length[0]
        xs = track1
        ys = track2
    print("The model's parameter:",xs,ys)
    return xs,ys
#结果函数生成
def map_Create_Fun(x2,y2):
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
#梯度下降优化算法,Acceptance为精度
def equation_Task_up(x1,y1,z1,Acceptance):
    Alpha = 0.01
    theta = np.array(0)
    theta = np.append(theta,0)
    data = np.array([x1,y1])
    data = data.transpose()
    length = x1.shape[0]
    pic = data@theta.transpose()-z1.transpose()
    cost = pic@pic.transpose()/(2*length)
    while cost > Acceptance:
        theta = theta - (data.transpose()@(data@theta.transpose()-z1.transpose()))*Alpha/length
        pic = data@theta.transpose()-z1.transpose()
        cost = pic@pic.transpose()/(2*length)
        theta = theta.transpose()
    print("The model's parameter：",theta)
    return theta
#通用散点图显示函数,只支持三维显示,三维以上只显示前三个参数
def Dot_map(map_data,res):
    map_ = map_data.transpose()
    fig = plt.figure("data set")
    ax = A3D.Axes3D(fig)
    ax.set_xlabel("x-bar")
    ax.set_ylabel("y-bar")
    ax.set_zlabel("z-bar")
    ax.scatter(map_[0],map_[1],res)
    return fig
#通用梯度优化生成函数,number为未知参数个数,data_为数据集,Acceptance为精度
def gradient_descent(number,data_,Acceptance):
    res = np.zeros(number+1,1)

    return 0