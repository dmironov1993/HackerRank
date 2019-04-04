import numpy as np

n = int(input())
a,b = (np.array([input().strip().split() for _ in range(n)], dtype=np.int) for _ in range(2))

print (np.dot(a,b))
