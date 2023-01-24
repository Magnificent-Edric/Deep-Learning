import numpy as np #не стирать!        

def diag_2k(a):
    summa = 0
    diag = np.diagonal(a)
    for i in range(len(diag)):
            if diag[i] % 2 == 0:
                summa += diag[i]
    return summa