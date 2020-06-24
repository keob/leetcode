from typing import List


class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        if not nums or len(nums) < 2:
            return 0

        minima, maxima = min(nums), max(nums)

        if minima == maxima:
            return 0

        margin = max(1, (maxima - minima) // (len(nums) -1))
        bkt_size = (maxima - minima) // margin + 1
        bkt_min, bkt_max = [float("inf")] * bkt_size, [0] * bkt_size

        for num in nums:
            idx = (num - minima) // margin
            bkt_min[idx] = min(bkt_min[idx], num)
            bkt_max[idx] = max(bkt_max[idx], num)

        res = lastBktIdx = 0

        for i in range(1, bkt_size):
            if bkt_min[i] == float("inf") or bkt_max == 0:
                continue
            res = max(res, bkt_min[i] - bkt_max[lastBktIdx])
            lastBktIdx = i
        return res
