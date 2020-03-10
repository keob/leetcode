class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self.res = 1
        def depth(node):
            if not node:
                return 0
            L = depth(node.left)
            R = depth(node.right)
            self.res = max(self.res, L + R + 1)
            return max(L, R) + 1

        depth(root)
        return self.res - 1
