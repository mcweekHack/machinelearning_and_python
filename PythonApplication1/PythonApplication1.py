import numpy as np
import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d as  A3D
import datam
import FunctionGather as Fun
from matplotlib import cm
#*******************************
#[x,y,z] = datam.Get_data(10,0)#生成并获取数据集
#Fun.Spot_map_Create(x,y,z)#生成数据集的散点图
#Fun.equation_Create(x,y,z)#生成代价函数的散点图
#a,b = Fun.equation_task(x,y,z,0.1)#计算并返回预测函数的两个模型参数
#Fun.map_Create_Fun(a,b)
#a,b = Fun.equation_Task_up(x,y,z,0.05)#优化的梯度下降
#Fun.map_Create_Fun(a,b)
#plt.show()#输出
[x,y,z] = datam.Get_Pro_data(1000,10,4)
theta = Fun.gradient_descent(10,x,y,0.05)
print(z)
print(theta)
#theta = theta.transpose()
#Fun.Result_show(theta[0][0],theta[0][1],theta[0][2])
#Fun.Dot_map(x,y)
#plt.show()
