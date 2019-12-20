from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        return len([i for i in nums if i < target])
