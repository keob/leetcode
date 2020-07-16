from typing import List


class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        vis = [0] * len(graph)

        def dfs(pos, color):
            vis[pos] = color
            for i in graph[pos]:
                if vis[i] == color or not (vis[i] or dfs(i, -color)):
                    return False
            return True

        for i in range(len(graph)):
            if not vis[i] and not dfs(i, 1):
                return False

        return True
