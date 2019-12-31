class Node:
    def __init__(self, val, neighbors):
        self.val = val
        self.neighbors = neighbors


class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        tmp = {}

        def dfs(node):
            if not node:
                return
            if node in tmp:
                return tmp[node]
            clone = Node(node.val, [])
            tmp[node] = clone
            for n in node.neighbors:
                clone.neighbors.append(dfs(n))

            return clone

        return dfs(node)
