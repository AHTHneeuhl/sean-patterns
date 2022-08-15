from itertools import zip_longest


def backspaceCompare(s: str, t: str) -> bool:
    def F(s):
        skip = 0
        for x in reversed(s):
            if x == '#':
                skip += 1
            elif skip:
                skip -= 1
            else:
                yield x

    return all(x == y for x, y in zip_longest(F(s), F(t)))


if __name__ == '__main__':
    s, t = "ab#c", "ad#c"
    print(backspaceCompare(s, t))  # True
    s, t = "a#c", "b"
    print(backspaceCompare(s, t))  # False
