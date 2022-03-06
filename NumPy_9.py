import numpy as np
from NumPy_2 import blank

if __name__ == "__main__":
    blank()
    a = np.array([x for x in range(9)])
    print("print(a[a > 5])")
    print(a[a > 5])
    blank()

    b = np.array([0, 1, 2, 3, 4, 5, 10, 11, 12])
    print("print(a == b)")
    print(a == b)
    # [ True  True  True  True  True  True False False False]
    blank()

    print("print(a != b)")
    print(a != b)
    # [False False False False False False  True  True  True]
    blank()

    print("print(a != 3)")
    print(a != 3)
    # [ True  True  True False  True  True  True  True  True]
    blank()

    print("print(np.greater(b, a))")
    print(np.greater(b, a))
    # [False False False False False False  True  True  True]
    blank()

    print("print(np.less(a, b))")
    print(np.less(a, b))
    # [False False False False False False  True  True  True]
    blank()

    print("print(np.equal(a, b))")
    print(np.equal(a, b))
    # [ True  True  True  True  True  True False False False]
    blank()

    print("print(np.array_equiv(a, b))")
    print(np.array_equiv(a, b))
    # False
    blank()

    print("print(np.any(a > 5))")
    print(np.any(a > 5))
    # True
    blank()

    print("print(np.any(b == 6))")
    print(np.any(b == 6))
    # False
    blank()

    print("print(np.all(a > 5))")
    print(np.all(a > 5))
    # False
    blank()

    print("b = a / 0")
    b = a / 0
    print(b)
    blank()

    print("b = np.array([1, 2, np.inf])")
    b = np.array([1, 2, np.inf])
    print(b)
    # [ 1.  2. inf]
    blank()

    print("c = b * 0")
    c = b * 0
    print(c)
    # [ 0.  0. nan]
    blank()

    a = np.array([1, 2, np.nan, np.inf, -np.inf])
    print(a)
    blank()
    print("print(np.isinf(a))")
    print(np.isinf(a))
    blank()
    print("print(np.isnan(a))")
    print(np.isnan(a))
    blank()

    i = np.isinf(a)
    print("b = a[~i]")
    b = a[~i]
    print(b)
    blank()

    i = np.isfinite(a)
    print("i = np.isfinite(a)")
    b = a[i]
    print(b)
    blank()

    print("np.array([1+2j, 3-4j, 5])")
    a = np.array([1+2j, 3-4j, 5])
    print(a)
    # [1.+2.j 3.-4.j 5.+0.j]
    blank()
    print("print(np.iscomplex(a))")
    print(np.iscomplex(a))
    # [ True  True False]
    blank()
    print("print(np.isreal(a))")
    print(np.isreal(a))
    # [False False  True]
    blank()

    x = np.array([True, False, True, False])
    y = np.array([True, True, False, False])

    print("a = np.logical_and(x, y)")
    a = np.logical_and(x, y)
    print(a)
    # [True False False False]
    blank()

    print("a = np.logical_or(x, y)")
    a = np.logical_or(x, y)
    print(a)
    # [ True  True  True False]
    blank()

    print("a = np.logical_not(x)")
    a = np.logical_not(x)
    print(a)
    # [False  True False  True]
    blank()

    print("a = np.logical_xor(x, y)")
    a = np.logical_xor(x, y)
    print(a)
    # [False  True  True False]
    blank()

    print("x = np.array([1, 0, 2, 0])\n"
          "y = np.array([3, 4, 0, 0])")
    x = np.array([1, 0, 2, 0])
    y = np.array([3, 4, 0, 0])
    print("a = np.logical_and(x, y)")
    a = np.logical_and(x, y)
    print(a)
    # [ True False False False]
    blank()

