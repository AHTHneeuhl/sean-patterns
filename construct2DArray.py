def construct2DArray(original, m: int, n: int):
    if m * n != len(original):
        return []
    res = [[0] * n for _ in range(m)]
    for idx in range(len(original)):
        res[idx//n][idx % n] = original[idx]
    return res


if __name__ == '__main__':
    original, m, n = [1, 2, 3],  1,  3
    print(construct2DArray(original, m, n))  # [[1, 2, 3]]
    original, m, n = [1, 2], 1,  1
    print(construct2DArray(original, m, n))  # []
