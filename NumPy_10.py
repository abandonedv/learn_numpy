import numpy as np
from NumPy_2 import blank

if __name__ == "__main__":
    blank()
    a = np.array([x for x in range(10)])
    print("print(a.sum())")
    print(a.sum())
    # 45
    blank()
    print("print(a.mean())")
    print(a.mean())
    # 4.5
    blank()
    print("print(a.max())")
    print(a.max())
    # 9
    blank()
    print("print(a.min())")
    print(a.min())
    # 0
    blank()

    a.resize(5, 2)
    print(a)
    blank()

    print("print(a[3].max())")
    print(a[3].max())
    # 7
    blank()

    print("print(a.sum(axis=0))")
    print(a.sum(axis=0))
    # [20 25]
    blank()
    print("print(a.sum(axis=1))")
    print(a.sum(axis=1))
    # [ 1  5  9 13 17]
    blank()

    b = np.array([1, -1, 6, -44, 0])
    print(b)
    blank()
    print("print(b.abs())")
    print(np.abs(b))
    # [ 1  1  6 44  0]
    blank()

    print("print(np.amin(a))")
    print(np.amin(a))
    # 0
    blank()
    print("print(np.amax(a))")
    print(np.amax(a))
    # 9
    blank()

    print("print(np.argmax(b))")
    print(np.argmax(b))
    # 2
    blank()

    print("print(np.argmin(b))")
    print(np.argmin(b))
    # 3
    blank()

    print("c = np.amin(a, axis=0")
    c = np.amin(a, axis=0)
    print(c)
    # [0 1]
    blank()

    print("c = np.amax(a, axis=1)")
    c = np.amax(a, axis=1)
    print(c)
    # [1 3 5 7 9]
    blank()

    print("a = np.linspace(0, np.pi, 10)")
    a = np.linspace(0, np.pi, 10)
    print(a)
    # [0.         0.34906585 0.6981317  1.04719755 1.3962634  1.74532925
    #  2.0943951  2.44346095 2.7925268  3.14159265]
    blank()
    print("print(np.sin(a))")
    print(np.sin(a))
    # [0.00000000e+00 3.42020143e-01 6.42787610e-01 8.66025404e-01
    #  9.84807753e-01 9.84807753e-01 8.66025404e-01 6.42787610e-01
    #  3.42020143e-01 1.22464680e-16]
    blank()

    print("print(np.cos(a))")
    print(np.cos(a))
    # [ 1.          0.93969262  0.76604444  0.5         0.17364818 -0.17364818
    #  -0.5        -0.76604444 -0.93969262 -1.        ]
    blank()

    print("print(np.random.rand(5))")
    print(np.random.rand(5))
    # [0.76917438 0.63918187 0.01738633 0.25832795 0.66325278]
    blank()

    print("print(np.random.rand(5, 5))")
    print(np.random.rand(5, 5))
    # [[0.62122499 0.09522355 0.26823721 0.48015111 0.04400486]
    #  [0.4249707  0.57998599 0.62735992 0.07884002 0.01802143]
    #  [0.37785392 0.38486242 0.6953965  0.80200722 0.54492803]
    #  [0.95733028 0.82188909 0.08768824 0.37347331 0.22217522]
    #  [0.90233622 0.06951994 0.71737572 0.05063544 0.17714354]]
    blank()

    print("print(np.random.randint(1, 100))")
    print(np.random.randint(1, 100))
    blank()

    print("print(np.random.randint(1, 10, size=(3, 3)))")
    print(np.random.randint(1, 100, size=(3, 3)))
    # [[70 87 85]
    #  [ 8 53 95]
    #  [43 14 60]]
    blank()

    print("print(np.random.randn(2, 3))")
    print(np.random.randn(2, 3))
    # [[-0.48040021  0.11983894 -0.42330409]
    #  [-0.40936432 -0.62867493  0.34458427]]
    blank()

    print("np.random.pareto(size=(3, 4))")
    print(np.random.pareto(2, size=(3, 4)))
    # [[1.19386964 0.45771809 4.22792394 0.63920043]
    #  [0.0185064  0.95272656 0.29026373 0.0786299 ]
    #  [0.80733962 0.11943756 0.78960913 0.70747238]]
    blank()

    print("np.random.beta(size=(4, 3))")
    print(np.random.beta(1, 10, size=(4, 3)))
    # [[0.00714106 0.11702611 0.00760099]
    #  [0.41257034 0.25034839 0.02285809]
    #  [0.44534799 0.19591413 0.03923033]
    #  [0.02549285 0.02201614 0.14694183]]
    blank()

    print("np.random.seed(13)")
    np.random.seed(13)
    print(np.random.randn(3, 2))
    # [[-0.71239066  0.75376638]
    #  [-0.04450308  0.45181234]
    #  [ 1.34510171  0.53233789]]
    blank()
    print("np.random.seed(13)")
    np.random.seed(13)
    print(np.random.randn(3, 2))
    # [[-0.71239066  0.75376638]
    #  [-0.04450308  0.45181234]
    #  [ 1.34510171  0.53233789]]
    blank()

    np.random.seed(0)
    a = np.arange(10)
    print("np.random.shuffle(a)")
    np.random.shuffle(a)
    print(a)
    # [7 4 9 0 3 1 2 8 5 6]
    blank()

    a = np.arange(10)
    a.resize(5, 2)
    print("np.random.shuffle(a)")
    np.random.shuffle(a)
    print(a)
    # [[0 1]
    #  [8 9]
    #  [4 5]
    #  [2 3]
    #  [6 7]]
    blank()

    print("print(np.random.permutation(10))")
    print(np.random.permutation(10))
    # [5 2 3 4 9 0 7 6 1 8]










