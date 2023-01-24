import numpy as np
def encode(a):
    i = 0
    len1 = len(a)
    no_repeat_number = []
    count_repeats = []
    while i < len1:
        tmp = 0
        last = a[i]
        j = i
        for j in range(j, len1):
            if last == a[j]:
                tmp += 1
            else:
                break
        count_repeats.append(tmp)
        i += tmp
        no_repeat_number.append(last)
    return(np.array(no_repeat_number), np.array(count_repeats))