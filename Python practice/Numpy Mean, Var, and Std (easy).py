import numpy as np

np.set_printoptions(legacy='1.13')
n, m = map(int, input().strip().split())
array = np.array([input().strip().split() for _ in range(n)], dtype=np.float)
print (np.mean(array, axis=1))
print (np.var(array, axis=0))
print (np.std(array, axis=None))
