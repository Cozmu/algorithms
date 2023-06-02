def is_palindrome_recursive(word, low_index, high_index):
    if word == '':
        return False
    upper_word = word.upper()
    if upper_word[low_index] != upper_word[high_index]:
        return False
    else:
        if low_index >= high_index:
            return True
        else:
           return is_palindrome_recursive(upper_word, low_index + 1, high_index - 1)

palavra = 'ANNA'
print(is_palindrome_recursive(palavra, 0, len(palavra) - 1))