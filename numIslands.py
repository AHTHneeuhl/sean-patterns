from itertools import product


# Time O(N) | Space O(1)
def numIslands(grid):
    m, n, count = len(grid), len(grid[0]), 0

    def check(x, y):
        if not 0 <= x < m or not 0 <= y < n or grid[x][y] != '1':
            return
        grid[x][y] = '0'
        for i, j in [[i+1, j], [i-1, j], [i, j+1], [i, j-1]]:
            check(i, j)

    for i, j in product(range(m), range(n)):
        if grid[i][j] == '1':
            check(i, j)
            count += 1

    return count
