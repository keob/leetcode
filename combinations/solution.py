from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        nums = list(range(1, k + 1)) + [n + 1]
        res, j = [], 0

        while j < k:
            res.append(nums[:k])
            j = 0
            while j < k and nums[j + 1] == nums[j] + 1:
                nums[j] = j + 1
                j += 1
            nums[j] += 1

        return res
