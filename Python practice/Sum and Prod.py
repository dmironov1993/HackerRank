import numpy as np

n, m = map(int, input().strip().split())
array = np.array([input().strip().split() for _ in range(n)], dtype=np.float)
print (np.int(np.prod(np.sum(array, axis=0))))
