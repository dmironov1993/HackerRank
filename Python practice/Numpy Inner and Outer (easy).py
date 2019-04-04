import numpy as np

a,b = (np.array([input().strip().split() for _ in range(2)], dtype=np.int))
print (np.inner(a,b))
print (np.outer(a,b))
