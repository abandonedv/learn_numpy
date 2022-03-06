from NumPy_2 import blank
import numpy as np


if __name__ == "__main__":
    a = np.array([(1, 2), (3, 4)])
    b = np.array([(5, 6), (7, 8)])

    blank()
    c = np.hstack([a, b])
    print(c)
    # [[1 2 5 6]
    #  [3 4 7 8]]
    blank()

    c = np.vstack([a, b])
    print(c)
    # [[1 2]
    #  [3 4]
    #  [5 6]
    #  [7 8]]
    blank()

    a = np.fromiter(range(18), dtype='int32')
    b = np.fromiter(range(18, 36), dtype='int32')
    a.resize(3, 3, 2)
    b.resize(3, 3, 2)
    print(a)
    blank()
    print(b)
    blank()
    c = np.hstack([a, b])
    # [[[ 0  1]
    #   [ 2  3]
    #   [ 4  5]
    #   [18 19]
    #   [20 21]
    #   [22 23]]
    #
    #  [[ 6  7]
    #   [ 8  9]
    #   [10 11]
    #   [24 25]
    #   [26 27]
    #   [28 29]]
    #
    #  [[12 13]
    #   [14 15]
    #   [16 17]
    #   [30 31]
    #   [32 33]
    #   [34 35]]]
    print(c)
    blank()

    a = np.array([1, 2, 3, 4])
    b = np.array([5, 6, 7, 8])
    c = np.column_stack([a, b])
    print(c)
    # [[1 5]
    #  [2 6]
    #  [3 7]
    #  [4 8]]
    blank()

    c = np.row_stack([a, b])
    print(c)
    # [[1 2 3 4]
    #  [5 6 7 8]]
    blank()

    a = np.arange(1, 13)
    b = np.arange(13, 26)
    a.resize(3, 3, 2)
    b.resize(3, 3, 2)

    c0 = np.concatenate([a, b], axis=0)
    print("np.concatenate([a, b], axis=0)")
    print(c0)
    blank()
    c1 = np.concatenate([a, b], axis=1)
    print("np.concatenate([a, b], axis=1)")
    print(c1)
    blank()
    c2 = np.concatenate([a, b], axis=2)
    print("np.concatenate([a, b], axis=2)")
    print(c2)
    blank()

    print("np.r_[[1, 2, 3], 4, 5]")
    a = np.r_[[1, 2, 3], 4, 5]
    print(a)
    # [1 2 3 4 5]
    blank()

    print("np.r_[1:9, 90, 100]")
    a = np.r_[1:9, 90, 100]
    print(a)
    # [1   2   3   4   5   6   7   8  90 100]
    blank()

    print("np.r_[np.array([1, 2, 3]), np.array([4, 5, 6])]")
    a = np.r_[np.array([1, 2, 3]), np.array([4, 5, 6])]
    print(a)
    # [1 2 3 4 5 6]
    blank()

    print("np.r_[[(1, 2, 3), (4, 5, 6)], [(7, 8, 9)]]")
    a = np.r_[[(1, 2, 3), (4, 5, 6)], [(7, 8, 9)]]
    print(a)
    # [[1 2 3]
    #  [4 5 6]
    #  [7 8 9]]
    blank()

    print("np.c_[1:5]")
    a = np.c_[1:5]
    print(a)
    # [[1]
    #  [2]
    #  [3]
    #  [4]]
    blank()

    print("np.c_[[1, 2, 3], [4, 5, 6]]")
    a = np.c_[[1, 2, 3], [4, 5, 6]]
    print(a)
    # [[1 4]
    #  [2 5]
    #  [3 6]]
    blank()

    print("np.c_[[(1, 2, 3), (4, 5, 6)], [[7], [8]]]")
    a = np.c_[[(1, 2, 3), (4, 5, 6)], [[7], [8]]]
    print(a)
    # [[1 2 3 7]
    #  [4 5 6 8]]
    blank()

    a = np.arange(10)
    print("np.hsplit(a, 5)")
    b = np.hsplit(a, 5)
    print(b)
    blank()

    a.shape = -1, 1
    print("np.vsplit(a, 5)")
    b = np.vsplit(a, 5)
    print(b)
    # [array([[0],
    #        [1]]), array([[2], 
    #        [3]]), array([[4],
    #        [5]]), array([[6],
    #        [7]]), array([[8],
    #        [9]])]
    blank()

    a.resize(3, 2, 2, refcheck=False)
    print(a)
    blank()
    b = np.array_split(a, 2, axis=1)
    print(b)
    # [array([[[0, 1]],
    #        [[4, 5]],
    #        [[8, 9]]]), array([[[2, 3]],
    #        [[6, 7]],
    #        [[0, 0]]])]
    blank()








