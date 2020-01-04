from typing import List


class Solution:
    def numberOfBoomerangs(self, points: List[List[int]]) -> int:
        n = len(points)
        if n < 3:
            return 0

        ret = 0

        for i in range(n):
            memo = dict()
            for j in range(n):
                if (i != j):
                    dict1 = self.dist(points[i], points[j])
                    if dict1 in memo:
                        memo[dict1] += 1
                    else:
                        memo[dict1] = 1
            for key, value in memo.items():
                ret += value * (value - 1)

        return ret

    def dist(self, alist, blist):
        return (alist[0] - blist[0]) * (alist[0] - blist[0]) + (
            alist[1] - blist[1]) * (alist[1] - blist[1])
