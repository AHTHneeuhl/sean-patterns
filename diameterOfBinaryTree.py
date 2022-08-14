# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def diameterOfBinaryTree(root) -> int:
    diam = 0

    def calc(root):
        if not root:
            return (0, 0)
        left = max(calc(root.left))
        right = max(calc(root.right))
        diam = max(diam, left + right)
        return (left + 1, right + 1)

    calc(root)
    return diam
