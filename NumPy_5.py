from NumPy_2 import blank
import numpy as np


if __name__ == "__main__":
    blank()
    a = np.arange(40)
    print(a)
    blank()
    print("a.reshape(-1, 10)")
    a = np.array(a.reshape(-1, 10))
    print(a)
    # [[ 0  1  2  3  4  5  6  7  8  9]
    #  [10 11 12 13 14 15 16 17 18 19]
    #  [20 21 22 23 24 25 26 27 28 29]
    #  [30 31 32 33 34 35 36 37 38 39]]
    blank()

    b = a.reshape(1, -1)
    print(b)
    # [[ 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20 21 22 23
    #   24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39]]
    blank()
    print("b = b.ravel()")
    b = b.ravel()
    print(b)
    # [ 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20 21 22 23
    #  24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39]
    blank()

    print("a.shape = -1")
    a.shape = -1
    print(a)
    # [ 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20 21 22 23
    #  24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39]
    blank()

    print("a.resize(2, 2, 10)")
    a.resize(2, 2, 10)
    # [[[ 0  1  2  3  4  5  6  7  8  9]
    #   [10 11 12 13 14 15 16 17 18 19]]
    #
    #  [[20 21 22 23 24 25 26 27 28 29]
    #   [30 31 32 33 34 35 36 37 38 39]]]
    print(a)

    print("a.resize(3, 3, 3)")
    a.resize(3, 3, 3, refcheck=False)
    # [[[ 0  1  2]
    #   [ 3  4  5]
    #   [ 6  7  8]]
    #
    #  [[ 9 10 11]
    #   [12 13 14]
    #   [15 16 17]]
    #
    #  [[18 19 20]
    #   [21 22 23]
    #   [24 25 26]]]
    print(a)
    blank()

    x = np.arange(10)
    print("x.shape = 1, -1")
    x.shape = 1, -1
    print(x.T)
    # [[0]
    #  [1]
    #  [2]
    #  [3]
    #  [4]
    #  [5]
    #  [6]
    #  [7]
    #  [8]
    #  [9]]
    blank()

    y = np.arange(32).reshape(8, 2, 2)
    print(y.shape)
    blank()
    y1 = np.expand_dims(y, axis=0)
    print("np.expand_dims(y, axis=0)")
    print(y1.shape)
    blank()

    print(y1)
    blank()
    print("np.append(y1, y1, axis=0)")
    a = np.append(y1, y1, axis=0)
    print(a.shape)
    # (2, 8, 2, 2)
    blank()

    print("np.delete(a, 0, axis=0)")
    b = np.delete(a, 0, axis=0)
    print(b.shape)
    # (1, 8, 2, 2)
    blank()

    print("np.expand_dims(y1, axis=-1)")
    b = np.expand_dims(y1, axis=-1)
    print(b.shape)
    # (1, 8, 2, 2, 1)
    blank()

    print("np.squeeze(b)")
    c = np.squeeze(b)
    print(c.shape)
    # (8, 2, 2)
    blank()

    a = np.arange(10)
    print("a[np.newaxis, :]")
    d = a[np.newaxis, :]
    # (1, 10)
    print(d.shape)




