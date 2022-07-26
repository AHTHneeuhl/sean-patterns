# Time - O(N) | Space O(N)
def singleNumber(nums):
    res = 0
    for num in nums:
        res ^= num
    return res


if __name__ == '__main__':
    nums1 = [2, 2, 1]
    nums2 = [4, 1, 2, 1, 2]
    nums3 = [1]
    print(singleNumber(nums1))  # 1
    print(singleNumber(nums2))  # 4
    print(singleNumber(nums3))  # 1
