from collections import deque
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def rightSideView(self, root: TreeNode, level = 1) -> List[int]:
        if not root:
            return []
        res = []
        tmp_layer = collections.deque()
        tmp_layer.append(root)
        while len(tmp_layer) > 0:
            count = 0
            next_layer = []
            while len(tmp_layer) > 0:
                tmp_node = tmp_layer.popleft()
                if count == 0:
                    res.append(tmp_node.val)
                count += 1
                if tmp_node.right is not None:
                    next_layer.append(tmp_node.right)
                if tmp_node.left is not None:
                    next_layer.append(tmp_node.left)
            tmp_layer = collections.deque(next_layer)

        return res
