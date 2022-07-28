# Time - O(N) | Space O(N)
def twoSum(nums, target):
    lookup = dict()
    for i, num in enumerate(nums):
        d = target - num
        if d in lookup:
            return [lookup[d], i]
        else:
            lookup[num] = i


if __name__ == '__main__':
    nums, target = [2, 7, 11, 15],  9
    print(twoSum(nums, target))  # [0, 1]
    nums, target = [3, 2, 4],  6
    print(twoSum(nums, target))  # [1, 2]
    nums, target = [3, 3],  6
    print(twoSum(nums, target))  # [0, 1]
