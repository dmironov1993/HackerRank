import numpy as np

if __name__ == '__main__':
    size = np.array(input().strip().split(), int)
    list_to_array = []
    for _ in range(size[0]):
        list_to_array.append(list(np.array(input().strip().split(), int)))
    print (np.transpose(np.array(list_to_array)))
    print (np.array(list_to_array).flatten())
