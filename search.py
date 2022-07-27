# Time O(logN) | Space O(1)
def search(nums, target):
    l, r = 0, len(nums) - 1

    while l <= r:
        m = l + (r - l) // 2
        if nums[m] == target:
            return m
        elif nums[m] < target:
            l = m + 1
        else:
            r = m - 1

    return -1


if __name__ == '__main__':
    nums1, target1 = [-1, 0, 3, 5, 9, 12], 9
    nums2, target2 = [-1, 0, 3, 5, 9, 12], 2
    print(search(nums1, target1))  # 4
    print(search(nums2, target2))  # -1
