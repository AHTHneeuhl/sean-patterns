# Time - O(N) | Space O(1)
def findDuplicates(nums):
    res = []
    for i, _ in enumerate(nums):
        nums[abs(nums[i]) - 1] = -nums[abs(nums[i]) - 1]
        if nums[abs(nums[i]) - 1] > 0:
            res.append(abs(nums[i]))
    return res


if __name__ == '__main__':
    nums = [4, 3, 2, 7, 8, 2, 3, 1]
    print(findDuplicates(nums))  # [2, 3]
    nums = [1, 1, 2]
    print(findDuplicates(nums))  # [1]
