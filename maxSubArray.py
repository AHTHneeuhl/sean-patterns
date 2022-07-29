import math


# Time - O(N) | Space - O(1)
def maxSubArray(nums):
    max_sum_so_far = -math.inf
    curr_sum = 0
    for num in nums:
        curr_sum += num
        max_sum_so_far = max(max_sum_so_far, curr_sum)
        curr_sum = max(curr_sum, 0)
    return max_sum_so_far


if __name__ == '__main__':
    nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    print(maxSubArray(nums))  # 6
    nums = [1]
    print(maxSubArray(nums))  # 1
