import numpy as np

def Get_data(counts):
    xs = np.random.rand(counts*counts)
    ys = []
    zs = []
    for x in range(counts*counts):
        ys.append(np.random.rand())
        zs.append(xs[x]*1.2+ys[x]*2.5+np.random.rand()*5)
    return xs,ys,zs
