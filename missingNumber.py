# Time - O(N) | Space - O(1)
def missingNumber(nums):
    total, n = 0, len(nums)
    for num in nums:
        total += num
    return (n * (n + 1) // 2) - total


# Time - O(N) | Space - O(1)
def missingNumber(nums):
    n = len(nums)
    res = n
    for i in range(n):
        res ^= i
        res ^= nums[i]
    return res


if __name__ == '__main__':
    nums1 = [3, 0, 1]
    nums2 = [0, 1]
    nums3 = [9, 6, 4, 2, 3, 5, 7, 0, 1]
    print(missingNumber(nums1))  # 2
    print(missingNumber(nums2))  # 2
    print(missingNumber(nums3))  # 8
