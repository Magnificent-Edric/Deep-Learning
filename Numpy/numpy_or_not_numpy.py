import numpy as np

def no_numpy_mult(first, second):
    """
    param first: list of "size" lists, each contains "size" floats
    param second: list of "size" lists, each contains "size" floats
    """
    i = 0
    lenght = len(first)
    result = [[0] * lenght for _ in range(lenght)]
    while i < lenght:
        j = 0
        while j < lenght:
            k = 0
            while k < lenght:
                result[i][j] += first[i][k]*second[k][j]
                k += 1
            j += 1
        i += 1
    return result

def numpy_mult(first, second):
    """
    param first: np.array[size, size]
    param second: np.array[size, size]
    """

    #YOUR CODE: please use numpy

    result = first.dot(second)
    return result