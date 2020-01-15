from typing import List
import bisect


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        minend = [float("inf")] * len(nums)

        for n in nums:
            minend[bisect.bisect_left(minend, n)] = n

        return bisect.bisect_left(minend, float("inf"))
