# Time O(N)
def productExceptSelf(nums):
    n, res = len(nums), [1] * len(nums)

    prefix = 1
    for i in range(n):
        res[i] = prefix
        prefix *= nums[i]

    postfix = 1
    for i in range(n - 1, -1, -1):
        res[i] *= postfix
        postfix *= nums[i]

    return res


if __name__ == '__main__':
    nums = [1, 2, 3, 4]
    print(productExceptSelf(nums))
    nums = [-1, 1, 0, -3, 3]
    print(productExceptSelf(nums))
