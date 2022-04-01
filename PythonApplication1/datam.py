import numpy as np

def Get_data(counts,value):#生成数据集
    xs = np.random.rand(counts*counts)
    ys = []
    zs = []
    for x in range(counts*counts):
        ys.append(np.random.rand())
        zs.append(xs[x]*1.5+ys[x]*2.5+np.random.rand()*0.1+value)
    ys = np.array(ys)
    zs = np.array(zs)
    return xs,ys,zs
