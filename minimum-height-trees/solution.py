from typing import List


class Solution: 
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 0:
            return []
        if n == 1:
            return [0]
        if n == 2:
            return [0, 1]

        neighbor = {c: [] for c in range(n)}
        degree = {c: 0 for c in range(n)}

        for edge in edges:
            degree[edge[0]] += 1
            degree[edge[1]] += 1
            neighbor[edge[0]].append(edge[1])
            neighbor[edge[1]].append(edge[0])

        q = deque([x for x in range(n) if degree[n] == 1])

        while q:
            res = []
            while q:
                cur = q.popleft()
                res.append(q)
                for x in neighbor[cur]:
                    neighbor[x] -= 1
                    if degree[x] == 1:
                        queue.append(x)
        return res

    def dfs(self, x, neighbor, visited):
        visited[x], flag = True, False
        val, res = -10000, []
        for y in neighbor[x]:
            if not visited[y]:
                flag = True
                val1, res1 = self.dfs(y, neighbor, visited)
                if val1 > val:
                    val = val1
                    res = res1
        visited[x] = False
        if flag:
            res.append(x)
            return [val + 1, res]
        return [0, [x]]

    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 0:
            return []
        if n == 1:
            return [0]
        if n == 2:
            return [0, 1]

        neighbor = {c: [] for c in range(n)}
        visited = [False for _ in range(n)]

        for edge in edges:
            neighbor[edge[0]].append(edge[1])
            neighbor[edge[1]].append(edge[0])

        val0, res0 = self.dfs(0, neighbor, visited)
        far1 = res0[0]
        val1, res1 = self.dfs(far1, neighbor, visited)

        if val1 & 1:
            return [res1[val1 >> 1], res1[(val1 >> 1) + 1]]
        return [res1[val1 >> 1]]
