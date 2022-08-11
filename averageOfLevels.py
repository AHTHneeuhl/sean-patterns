from collections import deque


# Time O(N) | Space O(N)
def averageOfLevels(root):
    res = []
    if not root:
        return res
    queue = deque()
    queue.append(root)
    while len(queue):
        qlen, total = len(queue), 0
        for _ in range(qlen):
            cur = queue.popleft()
            total += cur.val
            if cur.left:
                queue.append(cur.left)
            if cur.right:
                queue.append(cur.right)
        res.append(total / qlen)
    return res
