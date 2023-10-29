
def buildArray(nums):
    n = len(nums)
    ans = [0] * n  # Initialize the ans array with zeros.

    for i in range(n):
        ans[i] = nums[nums[i]]  # Set ans[i] to nums[nums[i]].

    return ans
nums = [0, 2, 1, 5, 4, 3]
result = buildArray(nums)
print(result)  # This will print the resulting array.

