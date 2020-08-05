class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def rob(self, root: TreeNode) -> int:
        def helper(root):
            if not root:
                return 0, 0

            left = helper(root.left)
            right = helper(root.right)
            robValue  = root.val + left[1] + right[1]
            skipValue  = max(left) + max(right)

            return robValue , skipValue 

        return max(helper(root))
