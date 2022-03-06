import numpy as np


def blank():
    print(10 * "-")


if __name__ == "__main__":
    blank()
    print("np.array([1, 2, 3, 4])")
    a = np.array([1, 2, 3, 4])
    print(a)
    # [1 2 3 4]
    blank()

    print("np.array([1, 2, 3, 4], 'float64')")
    a = np.array([1, 2, 3, 4], "float64")
    print(a)
    # [1. 2. 3. 4.]
    blank()

    print("np.sctypeDict")
    print(np.sctypeDict)
    # узать все типы
    blank()

    print("np.array([1, 2, 3, 4], dtype='str_'")
    a = np.array([1, 2, 3, 4], dtype="str_")
    print(a)
    # ['1' '2' '3' '4']
    blank()

    print("np.array([1, 2, 5000, 1000], dtype='int8'")
    a = np.array([1, 2, 5000, 1000], dtype="int8")
    b = np.complex64(a)
    print("np.complex64(a)")
    print(b)
    # [   1.+0.j    2.+0.j -120.+0.j  -24.+0.j]
    blank()

    print("np.array((1, 2, 3))")
    a = np.array((1, 2, 3))
    print(a)
    # [1 2 3]
    blank()

    print("np.array('Hello', dtype='<U5')")
    a = np.array("Hello", dtype="<U5")
    print(a)
    # Hello
    blank()

    print("np.array([[1, 2], [3, 4], [5, 6]])")
    a = np.array([[1, 2], [3, 4], [5, 6]])
    print(a)
    # [[1 2]
    #  [3 4]
    #  [5 6]]
    blank()
