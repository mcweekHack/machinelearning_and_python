import numpy as np
#生成数据集(二元一次函数)
def Get_data(counts,value):
    xs = np.random.rand(counts*counts)
    ys = []
    zs = []
    for x in range(counts*counts):
        ys.append(np.random.rand())
        zs.append(xs[x]*5+ys[x]*7.5+np.random.rand()*0.75+value)
    ys = np.array(ys)
    zs = np.array(zs)
    return xs,ys,zs
#生成高维数据集
def Get_Pro_data(num,Unknown,value):
    data_ = []
    part = np.array([])
    theta = np.random.rand(Unknown)
    value = 0
    for i in range(Unknown):
        for i2 in range(num):
            val = np.random.rand()
            part = np.append(part,val)
        data_.append(part)
    data_ = np.array(data_)
    res = data_.transpose()@theta.transpose
    res = res.transpose()
    data_ = np.append(data_,res,axis = 0)
    data_ = data_.transpose()
    return num, data_, theta