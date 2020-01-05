from typing import List


class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int,
                                      t: int) -> bool:
        n = len(nums)
        if n <= 1:
            return False

        recode = set()

        for i in range(n):
            if t == 0:
                if nums[i] in recode:
                    return True
            else:
                for one in recode:
                    if abs(nums[i] - one) <= t:
                        return True
            recode.add(nums[i])

            if (len(recode) > k):
                recode.remove(nums[i - k])

        return False
