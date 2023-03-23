def sort_string(string):
    for i in range(0, len(string)):
        i_short = i
        for j in range(i + 1, len(string)):
            if string[j] < string[i_short]:
                i_short = j
        if i_short != i:
            aux = string[i_short]
            string[i_short] = string[i]
            string[i] = aux
    return (''.join(string))


def is_anagram(first_string, second_string):
    first_string = sort_string(list(first_string.casefold()))
    second_string = sort_string(list(second_string.casefold()))
    if first_string == second_string:
        return (first_string, second_string, True)
    else:
        return (first_string, second_string, False)
