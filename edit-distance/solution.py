class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m = len(word1)
        n = len(word2)

        if m * n == 0:
            return m + n

        res = [ [0] * (n + 1) for _ in range(m + 1)]

        for i in range(m + 1):
            res[i][0] = i
        for j in range(n + 1):
            res[0][j] = j

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                left = res[i - 1][j] + 1
                down = res[i][j - 1] + 1
                left_down = res[i - 1][j - 1]
                if word1[i - 1] != word2[j - 1]:
                    left_down += 1
                res[i][j] = min(left, down, left_down)

        return res[m][n]