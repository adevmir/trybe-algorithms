def is_anagram(first_string, second_string):
    first_string = list(first_string)
    second_string = list(second_string)
    for i in range(0, len(first_string)):
        i_short = i
        for j in range(i + 1, len(first_string)):
            if first_string[j] < first_string[i_short]:
                i_short = j
        if i_short != i:
            aux = first_string[i_short]
            first_string[i_short] = first_string[i]
            first_string[i] = aux
    for i in range(0, len(second_string)):
        i_short = i
        for j in range(i + 1, len(second_string)):
            if second_string[j] < second_string[i_short]:
                i_short = j
        if i_short != i:
            aux = second_string[i_short]
            second_string[i_short] = second_string[i]
            second_string[i] = aux
            i_short = i
    first_string = ''.join(first_string)
    second_string = ''.join(second_string)
    if first_string == '' or second_string == ''\
            or len(first_string) != len(second_string):
        return (first_string, second_string, False)
    if first_string == second_string:
        return (first_string, second_string, True)
