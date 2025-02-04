def has_33(nums):
    for i in range(len(nums) - 1):
        if nums[i] == 3 and nums[i + 1] == 3:
            return True
    return False


nums = list(map(int, input().split()))
Result_True_Or_False = has_33(nums)
print(Result_True_Or_False)