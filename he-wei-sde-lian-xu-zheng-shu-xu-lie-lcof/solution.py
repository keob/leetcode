from typing import List


class Solution:
    def findContinuousSequence(self, target: int) -> List[List[int]]:
        left = 1
        right = 1
        sum = 0
        res = []

        while left <= target // 2:
            if sum < target:
                sum += right
                right += 1
            elif sum > target:
                sum -= left
                left += 1
            else:
                arr = list(range(left, right))
                res.append(arr)
                sum -= left
                left += 1
        return res
