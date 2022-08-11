# Time O(N) | Space O(N)
def sortedSquares(nums):
    res = [0] * len(nums)
    l, r = 0, len(nums) - 1

    while l <= r:
        left, right = abs(nums[l]), abs(nums[r])

        if left > right:
            res[r - l] = left * left
            l += 1
        else:
            res[r - l] = right * right
            r -= 1

    return res


if __name__ == '__main__':
    nums = [-4, -1, 0, 3, 10]
    print(sortedSquares(nums))  # [0, 1, 9, 16, 100]
    nums = [-7, -3, 2, 3, 11]
    print(sortedSquares(nums))  # [4, 9, 9, 49, 121]
