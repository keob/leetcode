from typing import List


class Solution:
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        d = {}

        def dfs(cur, i, d):
            if i < len(nums) and (cur, i) not in d:
                d[(cur, i)] = dfs(cur + nums[i], i + 1, d) + dfs(
                    cur - nums[i], i + 1, d)
            return d.get((cur, i), int(cur == S))

        return dfs(0, 0, d)
