from typing import List


class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        l, r, t, b = 0, n - 1, 0, n - 1
        res = [[0 for _ in range(n)] for _ in range(n)]
        num, tar = 1, n * n

        while num <= tar:
            for i in range(l, r + 1):
                res[t][i] = num
                num += 1
            t += 1
            for i in range(t, b + 1):
                res[i][r] = num
                num += 1
            r -= 1
            for i in range(r, l - 1, -1):
                res[b][i] = num
                num += 1
            b -= 1
            for i in range(b, t - 1, -1):
                res[i][l] = num
                num += 1
            l += 1

        return res
