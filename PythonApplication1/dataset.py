import numpy as np

def get_beans(counts):
	xs = np.random.rand(counts)
	xs = np.sort(xs)
	ys = []
	for x in range(counts):
		ys.append(xs[x]*1.2+np.random.rand()/10)
	return xs,ys

