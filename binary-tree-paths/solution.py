from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        if not root:
            return []

        stack = [[root, []],]
        res = []

        while stack:
            node,tree_link = stack.pop(0)
            tree_link = tree_link + [str(node.val)]

            if node.left:
                stack.append([node.left, tree_link])
            if node.right:
                stack.append([node.right, tree_link])
            if not node.left and not node.right:
                res.append('->'.join(tree_link))

        return res
