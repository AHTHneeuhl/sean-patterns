# Time O(N) | Space O(1)
def climbStairs(n):
    a = b = 1
    for _ in range(n):
        a, b, = b, a + b
    return a


if __name__ == '__main__':
    n1 = 2
    n2 = 3
    print(climbStairs(n1))  # 2
    print(climbStairs(n2))  # 3
