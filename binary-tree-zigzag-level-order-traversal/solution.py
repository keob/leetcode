from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        curr = [root]
        res = []
        while curr:
            temp = []
            n = len(curr)
            for i in range(n):
                node = curr.pop(0)
                temp.append(node.val)
                if node.left:
                    curr.append(node.left)
                if node.right:
                    curr.append(node.right)
            res.append(temp)
        for i in range(len(res)):
            if i % 2 != 0:
                res[i].reverse()
        return res
