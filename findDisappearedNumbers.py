# Time - O(N) | Space - O(1)
def findDisappearedNumbers(nums):
    for num in nums:
        t = abs(num) - 1
        if nums[t] > 0:
            nums[t] *= -1

    res = []
    for idx, num in enumerate(nums):
        if num > 0:
            res.append(idx + 1)

    return res


if __name__ == '__main__':
    nums1 = [4, 3, 2, 7, 8, 2, 3, 1]
    nums2 = [1, 1]
    print(findDisappearedNumbers(nums1))  # [5, 6]
    print(findDisappearedNumbers(nums2))  # [2]
