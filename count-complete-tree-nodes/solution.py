from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def countNodes(self, root: TreeNode) -> int:
        if not root:
            return 0

        l = root
        r = root
        lh = 0
        rh = 0

        while l:
            l = l.left
            lh += 1
        while r:
            r = r.right
            rh += 1

        if rh == lh:
            return (1 << lh) - 1

        return self.countNodes(root.left) + self.countNodes(root.right) + 1
