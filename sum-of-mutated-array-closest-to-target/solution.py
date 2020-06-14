from typing import List


class Solution:
    def findBestValue(self, arr: List[int], target: int) -> int:
        if sum(arr) <= target:
            return max(arr)

        l = len(arr)
        left, right = target // l, min(max(arr), target)

        while left < right:
            mid = (left + right) // 2
            summ = 0
            for v in arr:
                summ += min(v, mid)
            if target < summ:
                right = mid - 1
            else:
                left = mid + 1
        summ, sumright, sumleft= 0, 0, 0
        for v in arr:
            summ += min(v, left)
            sumright += min(v, left + 1)
            sumleft += min(v, left - 1)
        if abs(target - sumright) >= abs(target - summ):
            return left if abs(target-summ) < abs(target - sumleft) else left - 1
        else:
            return left + 1
