from typing import List


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        queue = []
        indegrees = [0 for _ in range(numCourses)]
        adjacency = [[] for _ in range(numCourses)]

        for cur, pre in prerequisites:
            indegrees[cur] += 1
            adjacency[pre].append(cur)

        for i in range(numCourses):
            if indegrees[i] == 0:
                queue.append(i)

        while queue:
            node = queue.pop(0)
            numCourses-=1
            for c in adjacency[node]:
                indegrees[c] -= 1
                if indegrees[c] == 0:
                    queue.append(c)

        return not numCourses
