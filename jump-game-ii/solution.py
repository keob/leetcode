from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0 or n == 1:
            return 0

        MAXSIZE = 9999999
        dp = [MAXSIZE] * n
        dp[0] = 0
        min_i = 0
        addstart = 0
        while dp[n - 1] == MAXSIZE:
            for j in range(min_i + addstart, min_i + nums[min_i] + 1):
                if j < n and dp[j] > dp[min_i] + 1:
                    dp[j] = dp[min_i] + 1

            if dp[-1] != MAXSIZE:
                break

            addstart = nums[min_i]
            min_i += 1

        return dp[-1]
