from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def maxPathSum(self, root: TreeNode) -> int:

        self.res = float("-inf")

        def helper(root):
            if not root:
                return 0
            left = helper(root.left)
            right = helper(root.right)
            self.res = max(left + right + root.val, self.res)
            return max(0, max(left,  right) + root.val)

        helper(root)

        return self.res 

