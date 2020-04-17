from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n, max_length = len(nums), 0
        for i in range(n):
            if i <= max_length:
                max_length = max(max_length, i + nums[i])
                if max_length >= n - 1:
                    return True
        return False
