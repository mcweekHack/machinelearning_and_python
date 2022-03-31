import numpy as np

def get_beans(counts):
	xs = np.random.rand(counts)
	ys = np.random.rand(counts)
	ys = np.sort(ys)
	xs = np.sort(xs)
	zs = []
	for x in range(counts):
		zs.append(xs[x]*1.2+ys[x]*2.5+np.random.rand()/10)
	return xs,ys,zs

