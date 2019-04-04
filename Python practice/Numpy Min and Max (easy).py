import numpy as np

if __name__=='__main__':
    n, m = map(int, input().strip().split())
    array_1 = np.array([input().strip().split() for _ in range(n)], dtype=np.float)
    print (np.int(np.max(np.min(array_1, axis=1), axis=0)))
