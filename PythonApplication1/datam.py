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
#生成高维数据集,Unknown是未知参数,data_是数据集,theta.transpose()是实际参数,num数据个数
def Get_Pro_data(num,Unknown,value):
    data_ = np.zeros((num,Unknown))
    theta = np.random.randint(1,10,(Unknown,1))
    res = np.array([])
    for x1 in range(Unknown):
        for x2 in range(num):
            data_[x2][x1] = np.random.rand()
    res = data_@theta + value
    for x3 in range(num):
        res[x3][0]+=np.random.rand()*1.5
    res = res.transpose()
    return data_,res, theta.transpose()
