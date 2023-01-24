def almost_double_factorial(n):
    i = 1
    factorial = 1
    if n == 0:
        return factorial
    else:
        for i in range(n + 1):
            if i % 2 != 0:
                factorial = factorial * i
            i +=1
        return factorial
