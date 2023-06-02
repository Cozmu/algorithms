def is_palindrome_recursive(word, low_index, high_index):
    if word[low_index] != word[high_index]:
        return False
    else:
        is_palindrome_recursive(word, low_index + 1, high_index - 1)
        return True

word = 'AMA'
print(is_palindrome_recursive(word, 0, len(word) - 1))