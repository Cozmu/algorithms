def is_palindrome_iterative(word):
    if word == '':
        return False
    upper_word = word.upper()
    last_char = len(upper_word) - 1
    for index in range(len(upper_word)//2):
        if upper_word[index] != upper_word[last_char - index]:
            return False
    return True
