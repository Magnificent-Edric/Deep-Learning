import numpy as np

def cumsum(A):
    #param A: np.array[m,n]
    #YOUR CODE

    s = []
    for i in range(len(A)):
        s.append(np.cumsum(A[i]))
    return s