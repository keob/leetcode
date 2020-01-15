from typing import List


class Solution:
    def rotateArray(self, nums: List[int], k: int) -> None:
        n = len(nums)
        k %= n

        nums[:] = nums[n - k:] + nums[:n - k]
