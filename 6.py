def has_lucky_number(nums):
    for num in nums:
        if num % 7 == 0:
            return True
        else:
            return False
