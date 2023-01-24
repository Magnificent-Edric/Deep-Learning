def process(sentences):
    result_string = []
    for strsen in sentences:
        i = 0
        append_list = []
        join_string = []
        string = strsen.split(" ")
        while i < len(string):
            if string[i].isalpha() == True:
                join_string.append(string[i])
            i += 1
        append_list = " ".join(join_string)
        result_string.append(append_list)
    return  result_string