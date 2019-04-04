import numpy as np

n, m = map(int, input().strip().split())
array_1, array_2 = (np.array([input().strip().split() for _ in range(n)], int) for _ in range(2))

print (array_1 + array_2, \
       array_1 - array_2, \
       array_1 * array_2, \
       array_1 // array_2, \
       array_1 % array_2, \
       array_1 ** array_2, sep='\n')
