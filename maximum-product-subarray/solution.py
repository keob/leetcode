from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        prefix, suffix, res = 0, 0, -float('inf')

        for i in range(len(nums)):
            prefix = nums[i] if not prefix else nums[i]*prefix
            suffix = nums[-i - 1] if not suffix else nums[-i - 1]*suffix
            res = max(res, prefix, suffix)

        return res
