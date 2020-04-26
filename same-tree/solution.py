class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if p and not q:
            return False
        if not p and q:
            return False
        if p is None and q is None:
            return True

        if p.val == q.val:
            result = self.isSameTree(p.left,q.left)
            if not result:
                return False 
            result = self.isSameTree(p.right,q.right)
            if not result:
                return False
            return True
        else:
            return False
