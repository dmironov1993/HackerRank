import numpy as np

n = input().strip().split()
print (np.zeros(tuple(map(int, n)), dtype=np.int))
print (np.ones(tuple(map(int, n)), dtype=np.int))
