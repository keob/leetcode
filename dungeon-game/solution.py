from typing import List


class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        x = len(dungeon)
        y = len(dungeon[0])
        dp = [[None for __ in range(y)] for __ in range(x)]
        dp[-1][-1] = 1 if dungeon[-1][-1] >= 0 else -dungeon[-1][-1]+1

        for i in range(x-2, -1, -1):
            tmp = dp[i+1][-1]-dungeon[i][-1]
            dp[i][-1] = 1 if tmp <= 0 else tmp
        for i in range(y-2, -1, -1):
            tmp = dp[-1][i+1]-dungeon[-1][i]
            dp[-1][i] = 1 if tmp <= 0 else tmp
        for i in range(x-2, -1, -1):
            for j in range(y-2, -1, -1):
                tmp = min(dp[i][j+1], dp[i+1][j])-dungeon[i][j]
                dp[i][j] = 1 if tmp <= 0 else tmp

        return dp[0][0]
