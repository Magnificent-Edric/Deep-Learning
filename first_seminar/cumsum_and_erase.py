def cumsum_and_erase(A, erase = 1):
    B = []
    i = 0
    lenght = len(A)
    while i < lenght:
        j = 0
        variable = 0
        while j <= i:
            variable += A[j]
            j += 1
        if variable != erase:
            B.append(variable)
        i += 1
    return B