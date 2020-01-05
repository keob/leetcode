from typing import List


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        n = len(nums)

        if (n <= 1):
            return False

        recode = set()

        for i in range(n):
            if nums[i] in recode:
                return True
            recode.add(nums[i])
            if len(recode) > k:
                recode.remove(nums[i - k])

        return False
