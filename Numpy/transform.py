import numpy as np

def transform(X, a=1):
    """
    param X: np.array[batch_size, n]
    """

    Y = X.copy()
    len1 = len(X)
    len2 = len(X[0])
    for i in range(0, len1):
        for j in range(0, len2):
            if j % 2 != 0:
                Y[i][j] = a
            else:
                Y[i][j] = Y[i][j] * Y[i][j] *Y[i][j]
        Y[i] = Y[i][::-1]
    C = np.concatenate((X, Y), axis = 1)
    return C