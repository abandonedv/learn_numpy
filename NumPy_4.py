from NumPy_2 import blank
import numpy as np


if __name__ == "__main__":
    blank()
    a = np.ones((3, 4, 5))
    print(a)
    blank()

    print("a.ndim")
    print(a.ndim)
    # 3
    blank()

    print("a.shape")
    print(a.shape)
    # (3, 4, 5)
    blank()

    print("b.shape = 3, 20")
    a.shape = 3, 20
    print(a)
    # [[1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1.]
    #  [1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1.]
    #  [1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1.]]
    blank()

    print("a.reshape(3, 2, 10)")
    b = a.reshape(3, 2, 10)
    print(b)
    # [[[1. 1. 1. 1. 1. 1. 1. 1. 1. 1.]
    #   [1. 1. 1. 1. 1. 1. 1. 1. 1. 1.]]
    #
    #  [[1. 1. 1. 1. 1. 1. 1. 1. 1. 1.]
    #   [1. 1. 1. 1. 1. 1. 1. 1. 1. 1.]]
    #
    #  [[1. 1. 1. 1. 1. 1. 1. 1. 1. 1.]
    #   [1. 1. 1. 1. 1. 1. 1. 1. 1. 1.]]]
    blank()

    print("c = b.T")
    c = b.T
    print(c)
    blank()

    b[1][1][1] = 100
    print(a)
    blank()
    print(b)
    blank()

    a = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
    print("b = a.view()")
    b = a.view()
    b.shape = 3, 3
    b[1][1] = 100
    print(a)
    # [  1   2   3   4 100   6   7   8   9]
    blank()
    print(b)
    # [[  1   2   3]
    #  [  4 100   6]
    #  [  7   8   9]]
    blank()

    # a = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
    b = a.view()
    b.shape = 3, 3
    print("b = np.array(b)")
    b = np.array(b)
    b[1][1] = 200
    print(a)
    # [  1   2   3   4 100   6   7   8   9]
    blank()
    print(b)
    # [[  1   2   3]
    #  [  4 200   6]
    #  [  7   8   9]]

