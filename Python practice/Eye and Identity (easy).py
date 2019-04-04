import numpy as np
np.set_printoptions(sign=' ')

if __name__ == '__main__':
    size = np.array(input().strip().split(), int)
    print (np.eye(size[0], size[1]))
