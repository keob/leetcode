from typing import List


class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        n = days[-1] + 1
        dp = [0 for _ in range(n)]

        days_idx = 0
        for i in range(1, n):
            if i != days[days_idx]:
                dp[i] = dp[i-1]
            else:
                dp[i] = min(dp[max(0, i-1)] + costs[0], 
                            dp[max(0, i-7)] + costs[1], 
                            dp[max(0, i-30)]+costs[2])

                days_idx += 1

        return dp[-1]
