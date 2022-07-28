from bisect import bisect


# Time - O(logN) | Space - O(1)
def nextGreatestLetter(letters, target):
    idx = bisect(letters, target)
    return letters[idx % len(letters)]


if __name__ == '__main__':
    letters, target = ["c", "f", "j"],  "a"
    print(nextGreatestLetter(letters, target))  # c
    letters, target = ["c", "f", "j"],  "c"
    print(nextGreatestLetter(letters, target))  # f
    letters, target = ["c", "f", "j"], "d"
    print(nextGreatestLetter(letters, target))  # f
