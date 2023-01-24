import numpy as np

def no_numpy_scalar(v1, v2):
    #param v1, v2: lists of 3 ints
    #YOUR CODE: please do not use numpy

    result = v1[0]*v2[0] + v1[1]*v2[1] + v1[2]*v2[2]
    return result

def numpy_scalar (v1, v2):
    #param v1, v2: np.arrays[3]
    #YOUR CODE

    result = np.dot(v1, v2)
    return result