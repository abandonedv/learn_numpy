from NumPy_2 import blank
import numpy as np

if __name__ == "__main__":
    blank()
    print('np.mat("1 5 7 3")')
    a = np.mat("1 5 7 3")
    print(a)
    # [[1 5 7 3]]
    blank()

    print('np.mat("1, 6, 3, 6")')
    a = np.mat("1, 6, 3, 6")
    print(a)
    # [[1 6 3 6]]
    blank()

    print('np.mat("1, 2; 3, 4")')
    a = np.mat("1, 2; 3, 4")
    print(a)
    # [[1 2]
    #  [3 4]]
    blank()

    print("np.mat([1, 7, 8])")
    a = np.mat([1, 7, 8])
    print(a)
    # [[1 7 8]]
    blank()

    print("np.diag([4, 7, 6])")
    a = np.diag([4, 7, 6])
    print(a)
    # [[4 0 0]
    #  [0 7 0]
    #  [0 0 6]]
    blank()

    print("np.diag([(1, 5, 6), (4, 5, 2,), (9, 5, 3)])")
    a = np.diag([(1, 5, 6), (4, 5, 2,), (9, 5, 3)])
    print(a)
    # [1 5 3]
    blank()

    print('np.diagflat([(1, 5, 6), (4, 5, 2,), (9, 5, 3)])')
    a = np.diagflat([(1, 5, 6), (4, 5, 2,), (9, 5, 3)])
    print(a)
    # [[1 0 0 0 0 0 0 0 0]
    #  [0 5 0 0 0 0 0 0 0]
    #  [0 0 6 0 0 0 0 0 0]
    #  [0 0 0 4 0 0 0 0 0]
    #  [0 0 0 0 5 0 0 0 0]
    #  [0 0 0 0 0 2 0 0 0]
    #  [0 0 0 0 0 0 9 0 0]
    #  [0 0 0 0 0 0 0 5 0]
    #  [0 0 0 0 0 0 0 0 3]]
    blank()

    print('np.tri(4)')
    a = np.tri(4)
    print(a)
    # [[1. 0. 0. 0.]
    #  [1. 1. 0. 0.]
    #  [1. 1. 1. 0.]
    #  [1. 1. 1. 1.]]
    blank()

    print('np.tri(3, 5)')
    a = np.tri(3, 5)
    print(a)
    # [[1. 0. 0. 0. 0.]
    #  [1. 1. 0. 0. 0.]
    #  [1. 1. 1. 0. 0.]]
    blank()

    print('np.tril(a)')
    a = np.array([(1, 2, 3), (4, 5, 6), (7, 8, 9)])
    b = np.tril(a)
    print(b)
    # [[1 0 0]
    #  [4 5 0]
    #  [7 8 9]]
    blank()

    print('np.triu(a)')
    b = np.triu(a)
    print(b)
    # [[1 2 3]
    #  [0 5 6]
    #  [0 0 9]]
    blank()

    print("np.tril([4, 5, 6])")
    a = np.tril([4, 5, 6])
    print(a)
    # [[4 0 0]
    #  [4 5 0]
    #  [4 5 6]]
    blank()

    print("np.vander([4, 5, 6])")
    a = np.vander([4, 5, 6])
    print(a)
    # [[16  4  1]
    #  [25  5  1]
    #  [36  6  1]]
    blank()



































