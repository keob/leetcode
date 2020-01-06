from typing import List


class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        sums = 0

        for i in range(1, n, 2):
            m = min(nums[i - 1], nums[i])
            sums += m

        return sums
