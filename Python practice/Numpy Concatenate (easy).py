import numpy as np

if __name__ == '__main__':
    input_sizes = np.array(input().strip().split(), int)

    n_list = []
    for _ in range(input_sizes[0]):
        n_list.append(np.array(input().strip().split(), int))

    m_list = []
    for _ in range(input_sizes[1]):
        m_list.append(np.array(input().strip().split(), int))

    array_1 = np.array(n_list)
    array_2 = np.array(m_list)
    print (np.concatenate([array_1, array_2], axis=0))
