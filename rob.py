# Time - O(N) | Space O(1)
def rob(nums):
    prev = curr = 0
    for num in nums:
        prev, curr = curr, max(num + prev, curr)
    return curr


def rob(nums):
    if not nums:
        return 0
    if len(nums) == 1:
        return nums[0]
    memo = [0] * len(nums)
    memo[0] = nums[0]
    memo[1] = max(nums[0], nums[1])
    for i in range(2, len(nums)):
        memo[i] = max(nums[i] + memo[i - 2], memo[i - 1])
    return memo[-1]


if __name__ == '__main__':
    nums = [1, 2, 3, 1]
    print(rob(nums))  # 4
    nums = [2, 7, 9, 3, 1]
    print(rob(nums))  # 12
