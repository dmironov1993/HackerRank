import numpy as np

np.set_printoptions(legacy='1.13')
n = int(input())
a = list(np.array([input().strip().split() for _ in range(n)], dtype=np.float))
print (np.linalg.det(a))
