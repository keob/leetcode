fom typing import List


class Solution:
    def massage(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [0] * (n + 2)
        ans = 0
        for i in range(2, n + 2):
            dp[i] = max(dp[i - 1], dp[i - 2] + nums[i - 2])
            ans = max(ans, dp[i])
        return ans
