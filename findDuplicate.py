# Time O(N) | Space O(1)
def findDuplicate(nums) -> int:
    while nums[0] != nums[nums[0]]:
        nums[nums[0]], nums[0] = nums[0], nums[nums[0]]
    return nums[0]


if __name__ == '__main__':
    nums = [1, 3, 4, 2, 2]
    print(findDuplicate(nums))  # 2
    nums = [3, 1, 3, 4, 2]
    print(findDuplicate(nums))  # 3
