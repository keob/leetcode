class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        if not root:
            return 0

        res = []
        stack = [(root,str(root.val))]

        while stack:
            node,num_sum = stack.pop()
            if node.left:
                stack.append((node.left,num_sum+str(node.left.val)))
            if node.right:
                stack.append((node.right,num_sum+str(node.right.val)))
            if not node.left and not node.right:
                res.append(int(num_sum))

        return sum(res)
