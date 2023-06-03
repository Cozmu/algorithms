def merge_word(word):
    if len(word) <= 1:
        return word

    mid = len(word) // 2
    left_half = word[:mid]
    right_half = word[mid:]

    left_half = merge_word(left_half)
    right_half = merge_word(right_half)

    return merge(left_half, right_half)


def merge(left, right):
    merged = ""
    left_index, right_index = 0, 0

    while left_index < len(left) and right_index < len(right):
        if left[left_index].lower() < right[right_index].lower():
            merged += left[left_index]
            left_index += 1
        else:
            merged += right[right_index]
            right_index += 1

    merged += left[left_index:]
    merged += right[right_index:]
    return merged.lower()

def is_anagram(first_string, second_string):
    first_word = merge_word(first_string)
    second_word = merge_word(second_string)
    if not first_string or not second_string:
        return (first_string, second_string, False)
    if first_word != second_word:
        return (first_word, second_word, False)
    return (first_word, second_word, True)


primeira = "dCba"
segunda = "cabd"

print(is_anagram(primeira, segunda))
