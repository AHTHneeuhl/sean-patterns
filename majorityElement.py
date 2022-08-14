def majorityElement(nums) -> int:
    major = count = 0
    for num in nums:
        if count == 0:
            major = num
        if major == num:
            count += 1
        else:
            count -= 1
    return major


if __name__ == '__main__':
    nums = [3, 2, 3]
    print(majorityElement(nums))  # 3
    nums = [2, 2, 1, 1, 1, 2, 2]
    print(majorityElement(nums))  # 2
