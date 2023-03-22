def is_palindrome_recursive(word, low_index, high_index):
    if len(word) == 0 or word[low_index] != word[high_index]:
        return False
    if len(word) == 1 or len(word) == 2 and word[low_index] == word[high_index]:
        return True
    return is_palindrome_recursive(word[1:-1], low_index, high_index - 2)
