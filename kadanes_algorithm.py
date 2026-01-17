def maxSubArray(nums):

    current_max = nums[0]
    global_max = nums[0]

    for num in nums[1:]:

        current_max = max(num, num+current_max)

        if current_max > global_max:

            global_max = current_max

    return global_max

nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print(maxSubArray(nums))