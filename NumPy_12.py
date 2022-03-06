import numpy as np
from NumPy_2 import blank

if __name__ == "__main__":
    blank()
    a = np.array([1, 2, 3, 4, 4, 3, 2, 1])
    print("setA = np.unique(a)")
    setA = np.unique(a)
    print(setA)
    # [1 2 3 4]
    blank()

    print("np.unique(a, return_counts=True)")
    setA_count = np.unique(a, return_counts=True)
    print(setA_count)
    # (array([1, 2, 3, 4]), array([2, 2, 2, 2], dtype=int64))
    blank()

    print("np.unique(a, return_index=True)")
    setA_index = np.unique(a, return_index=True)
    print(setA_index)
    # (array([1, 2, 3, 4]), array([0, 1, 2, 3], dtype=int64))
    blank()

    print("np.unique(a, return_inverse=True)")
    setA_inverse = np.unique(a, return_inverse=True)
    print(setA_inverse)
    # (array([1, 2, 3, 4]), array([0, 1, 2, 3, 3, 2, 1, 0], dtype=int64))
    blank()

    print("mass, i = setA_inverse")
    mass, i = setA_inverse
    print(mass[i])
    # [1 2 3 4 4 3 2 1]
    blank()

    x = np.array([[0, 1, 1, 2], [0, 1, 1, 2], [9, 1, 1, 2]])
    print("np.unique(a)")
    c = np.unique(x)
    print(c)
    # [0 1 2 9]
    blank()

    print("axis0 = np.unique(x, axis=0)")
    axis0 = np.unique(x, axis=0)
    print(axis0)
    # [[0 1 1 2]
    #  [9 1 1 2]]
    blank()

    print("axis1 = np.unique(x, axis=1)")
    axis1 = np.unique(x, axis=1)
    print(axis1)
    # [[0 1 2]
    #  [0 1 2]
    #  [9 1 2]]
    blank()

    x = np.arange(4)
    y = np.arange(1, 9)
    print(x)
    blank()
    print(y)
    blank()

    print("c = np.in1d(x, y)")
    c = np.in1d(x, y)
    print(c)
    # [False  True  True  True]
    blank()

    print("c = np.intersect1d(x, y)")
    c = np.intersect1d(x, y)
    print(c)
    # [1 2 3]
    blank()

    print("c = np.union1d(x, y)")
    c = np.union1d(x, y)
    print(c)
    # [0 1 2 3 4 5 6 7 8]
    blank()

    print("c = np.setdiff1d(x, y)")
    c = np.setdiff1d(x, y)
    print(c)
    # [0]
    blank()

    print("c = np.setdiff1d(y, x)")
    c = np.setdiff1d(y, x)
    print(c)
    # [4 5 6 7 8]
    blank()

    print("c = np.setxor1d(y, x)")
    c = np.setxor1d(y, x)
    print(c)
    # [0 4 5 6 7 8]
    blank()






