# Definition of a binary tree node.
class TreeNode:
    def __init__(self, val) -> None:
        self.val = val
        self.left = None
        self.right = None


class Solution:
    def hasPathSum(self, root, target):
        if not root:
            return False
        if not root.left and not root.right and root.val == target:
            return True
        return self.hasPathSum(root.left, target - root.val) or self.hasPathSum(root.right, target - root.val)
