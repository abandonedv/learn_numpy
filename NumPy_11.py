import numpy as np
from NumPy_2 import blank

if __name__ == "__main__":
    blank()
    a = np.arange(1, 10).reshape(3, 3)
    b = np.arange(10, 19).reshape(3, 3)
    print(a)
    blank()
    print(b)
    blank()

    print("np.dot(a, b)")
    c = np.dot(a, b)
    print(c)
    # [[ 84  90  96]
    #  [201 216 231]
    #  [318 342 366]]
    blank()

    print("np.matmul(a, b)")
    c = np.matmul(a, b)
    print(c)
    # [[ 84  90  96]
    #  [201 216 231]
    #  [318 342 366]]
    blank()

    a = np.arange(1, 10)
    b = np.ones(9, dtype=int)
    print(a)
    blank()
    print(b)
    blank()

    print("np.inner(a, b)")
    c = np.inner(a, b)
    print(c)
    # 45
    blank()

    print("np.outer(b, a)")
    c = np.outer(b, a)
    print(c)
    # [[1 2 3 4 5 6 7 8 9]
    #  [1 2 3 4 5 6 7 8 9]
    #  [1 2 3 4 5 6 7 8 9]
    #  [1 2 3 4 5 6 7 8 9]
    #  [1 2 3 4 5 6 7 8 9]
    #  [1 2 3 4 5 6 7 8 9]
    #  [1 2 3 4 5 6 7 8 9]
    #  [1 2 3 4 5 6 7 8 9]
    #  [1 2 3 4 5 6 7 8 9]]
    blank()

    a = np.arange(1, 10).reshape(3, 3)
    b = np.arange(10, 19).reshape(3, 3)
    print("c = a @ b")
    c = a @ b
    print(c)
    # [[ 84  90  96]
    #  [201 216 231]
    #  [318 342 366]]
    blank()

    a = np.arange(1, 10)
    b = np.ones(9, dtype=int)
    print("c = a @ b")
    c = a @ b
    print(c)
    # 45
    blank()

    a = np.array([1, 2, 3])
    b = np.array([[1, 2], [3, 4], [5, 6]])
    c = np.dot(a, b)
    print(c)
    # [22 28]
    blank()

    a = np.array([1, 2])
    print("Для numpy не нужно преобразовывать строку в столбец\n"
          "Он сам понимает как выполнить произведение")
    print("np.dot(b, a)")
    c = np.dot(b, a)
    print(c)
    # [5 11 17]
    blank()

    a = np.array([(1, 2, 3), (1, 4, 9), (1, 8, 27)])
    print("c = np.linalg.matrix_rank(a)")
    c = np.linalg.matrix_rank(a)
    print(c)
    # 3
    blank()

    y = np.array([10, 20, 30])
    print("c = np.linalg.solve(a, y)")
    c = np.linalg.solve(a, y)
    print(c)
    # [-5.         10.         -1.66666667]
    blank()

    print("invA = np.linalg.inv(a)")
    invA = np.linalg.inv(a)
    print(invA)
    # [ 3.         -2.5         0.5       ]
    #  [-1.5         2.         -0.5       ]
    #  [ 0.33333333 -0.5         0.16666667]]
    blank()

    print("c = a @ invA")
    c = a @ invA
    print(c)
    # 1.00000000e+00  0.00000000e+00 -2.77555756e-17]
    #  [ 3.33066907e-16  1.00000000e+00 -8.32667268e-17]
    #  [ 9.99200722e-16  0.00000000e+00  1.00000000e+00]]
    blank()

    print("c = invA @ y")
    c = invA @ y
    print(c)
    # [-5.         10. - 1.66666667]
    blank()


