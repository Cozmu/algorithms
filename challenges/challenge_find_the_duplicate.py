def find_duplicate(nums):
    if len(nums) <= 1:
        return False

    dictionary_of_repeating_numbers = {}
    for num in nums:
        if type(num) != int or num < 0:
            return False
        if num in dictionary_of_repeating_numbers:
            dictionary_of_repeating_numbers[num] += 1
        else:
            dictionary_of_repeating_numbers[num] = 1

    for num, quantity in dictionary_of_repeating_numbers.items():
        if quantity > 1:
           return quantity
        else:
            return False

print(find_duplicate([3, 1, 2, 4, 6, 5, 7, 7, 7, 8]))