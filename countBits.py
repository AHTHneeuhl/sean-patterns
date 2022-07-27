# Time O(N) | Space O(N)
def countBits(n):
    res = [0] * (n + 1)
    for i in range(n + 1):
        res[i] = res[i >> 1] + (i & 1)
    return res


if __name__ == '__main__':
    n1 = 2
    n2 = 5
    print(countBits(n1))  # [0, 1, 1]
    print(countBits(n2))  # [0, 1, 1, 2, 1, 2]
