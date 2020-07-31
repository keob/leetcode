from typing import List


class Solution:
    def findMagicIndex(self, nums: List[int]) -> int:
        if not nums:
            return -1

        if nums[0] == 0:
            return 0

        p, n = 0, len(nums)

        while p < n:
            if nums[p] > p:
                p = nums[p]
            elif nums[p] == p:
                return p
            else:
                p += 1

        return -1
