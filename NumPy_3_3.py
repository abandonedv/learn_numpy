from NumPy_2 import blank
import numpy as np

if __name__ == "__main__":

    blank()
    print('np.arange(1, 10)')
    a = np.arange(1, 10)
    print(a)
    # [1 2 3 4 5 6 7 8 9]
    blank()

    print('np.arange(1, 5, 0.5)')
    a = np.arange(2, 5, 0.5)
    print(a)
    # [2.  2.5 3.  3.5 4.  4.5]
    blank()

    a = np.arange(0, np.pi, 0.1)
    print('b = np.cos(a)')
    b = np.cos(a)
    print(b)
    # [ 1.          0.99500417  0.98006658  0.95533649  0.92106099  0.87758256
    #   0.82533561  0.76484219  0.69670671  0.62160997  0.54030231  0.45359612
    #   0.36235775  0.26749883  0.16996714  0.0707372  -0.02919952 -0.12884449
    #  -0.22720209 -0.32328957 -0.41614684 -0.5048461  -0.58850112 -0.66627602
    #  -0.73739372 -0.80114362 -0.85688875 -0.90407214 -0.94222234 -0.97095817
    #  -0.9899925  -0.99913515]
    blank()

    print("np.linspace(0, np.pi, 15)")
    a = np.linspace(0, np.pi, 15)
    print(a)
    # [0.         0.22439948 0.44879895 0.67319843 0.8975979  1.12199738
    #  1.34639685 1.57079633 1.7951958  2.01959528 2.24399475 2.46839423
    #  2.6927937  2.91719318 3.14159265]
    blank()
