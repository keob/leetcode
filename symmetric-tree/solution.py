class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        return self.isMirror(root, root)

    def isMirror(self, leftRoot: TreeNode, rightRoot: TreeNode):
        if leftRoot is None and rightRoot is None:
            return True
        if leftRoot is None or rightRoot is None:
            return False
        if leftRoot.val != rightRoot.val:
            return False
        return self.isMirror(leftRoot.left, rightRoot.right) and self.isMirror(
            leftRoot.right, rightRoot.left)
