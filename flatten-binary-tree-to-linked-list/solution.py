class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        dummy = TreeNode(0)
        prev = dummy
        stack = [root]
        while stack:
            rt = stack.pop()
            if not rt:
                continue
            prev.right = rt
            prev.left = None

            stack.append(rt.right)
            stack.append(rt.left)
            prev = rt
        prev.left = None
