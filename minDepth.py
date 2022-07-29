# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val) -> None:
        self.val = val
        self.left = None
        self.right = None


class Solution:
    def minDepth(self, root) -> int:
        if not root:
            return 0
        left, right = self.minDepth(root.left), self.minDepth(root.right)
        return 1 + (min(left, right) or max(left, right))
