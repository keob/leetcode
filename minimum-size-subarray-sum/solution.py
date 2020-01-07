from typing import List


class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        if sum(nums) < s:
            return 0
        elif max(nums) >= s:
            return 1
        else:
            min = len(nums)

        i = 0
        j = 1

        while i < j and j < len(nums):
            if sum(nums[i:j + 1]) >= s:
                t = j + 1 - i
                if t < min:
                    min = t
                i += 1
            else:
                j += 1

        return min
