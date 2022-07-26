# Time - O(N) | Space - O(N)
def containsDuplicate(nums):
    return len(nums) != len(set(nums))


# Time - O(N) | Space - O(N)
def containsDuplicate(nums):
    s = set()
    for num in nums:
        if num in s:
            return True
        s.add(num)
    return False


if __name__ == '__main__':
    nums1 = [1, 2, 3, 1]
    nums2 = [1, 2, 3, 4]
    nums3 = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]
    print(containsDuplicate(nums1))  # True
    print(containsDuplicate(nums2))  # False
    print(containsDuplicate(nums3))  # True
