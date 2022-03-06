from NumPy_2 import blank
import numpy as np


def defRange(x, y):
    return 10 * x + y


if __name__ == "__main__":
    blank()
    print("np.fromfunction(defRange, (2, 2))")
    a = np.fromfunction(defRange, (2, 2))
    print(a)
    # [[ 0.  1.]
    #  [10. 11.]]
    blank()

    print('np.fromiter("hello")')
    a = np.fromiter("hello", dtype="<U1")
    print(a)
    # ['h' 'e' 'l' 'l' 'o']
    blank()

    print('np.fromstring("1 3 5", dtype="int8", sep=" ")')
    a = np.fromstring("1 3 5", dtype="int8", sep=" ")
    print(a)
    # [1 3 5]
    blank()
