from typing import List


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        res = []
        visited = [0] * numCourses
        adjacent = [[] for _ in range(numCourses)]

        def dfs(i):
            if visited[i] == 1:
                return False
            if visited[i] == 2:
                return True
            visited[i] = 1
            for j in adjacent[i]:
                if not dfs(j):
                    return False

            visited[i] = 2
            res.append(i)
            return True

        for cur, pre in prerequisites:
            adjacent[cur].append(pre)

        for i in range(numCourses):
            if not dfs(i):
                return []

        return res
