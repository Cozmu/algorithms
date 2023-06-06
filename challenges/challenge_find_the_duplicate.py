def find_duplicate(nums):
    if len(nums) <= 1:
        return False
    for num in nums:
        if type(num) != int or num <= 0:
            return False
        if nums.count(num) > 1:
            return num
    return False
