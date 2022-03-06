from NumPy_2 import blank
import numpy as np

if __name__ == "__main__":
    blank()
    a = np.array([6, 4, 3, 1, 3, 5, 2, 14, 32, 1])
    b = a[[1, 4, 6, 3]]
    print(b)
    # [4 3 2 1]
    blank()

    boolI = [True, True, False, False, False, False, False, True, True, True]
    print("b = a[boolI]")
    b = a[boolI]
    print(b)
    # [ 6  4 14 32  1]
    blank()

    print("i = a > 5")
    i = a > 5
    b = a[i]
    print(b)
    # [ 6 14 32]
    blank()

    a = np.arange(5, 16)
    print(a)
    blank()
    print("i = np.array([(0, 1), (2, 3)])\n"
          "print(a[i])")
    i = np.array([(0, 1), (2, 3)])
    print(a[i])
    # [[5 6]
    #  [7 8]]
    blank()

    a = np.arange(1, 13).reshape(3, 4)
    print("np.arange(1, 13).reshape(3, 4)")
    i = np.array([2, 0, 1])
    print(a[i])
    # [[ 9 10 11 12]
    #  [ 1  2  3  4]
    #  [ 5  6  7  8]]
    blank()

    print("ix = np.array([[1, 0], [2, 1]])\n"
          "print(a[ix])")
    ix = np.array([[1, 0], [2, 1]])
    print(a[ix])
    blank()

    i0 = [0, 1]
    i1 = [1, 2]
    print("b = a[i0, i1]")
    b = a[i0, i1]
    print(b)
    blank()

    print("b = a[:, i1]")
    b = a[:, i1]
    print(b)
    # [[ 2  3]
    #  [ 6  7]
    #  [10 11]]
    blank()

    print("b = a[:, 1]")
    b = a[:, 1]
    print(b)
    # [ 2  6 10]
    blank()

    a = a.ravel()
    print("a[[1, 3, 5, 7]] = [9, 99, 999, 9999]")
    a[[1, 3, 5, 7]] = [9, 99, 999, 9999]
    print(a)
    # [   1    9    3   99    5  999    7 9999    9   10   11   12]
    blank()



