import heapq
from typing import List



class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        heap = []
        n = len(nums)
        MIN = float('inf')
        MAX = float('-inf')

        for i in range(n):
            heapq.heappush(heap, (nums[i][0], 0, i))
            MIN = min(MIN, nums[i][0])
            MAX = max(MAX, nums[i][0])

        res = [MIN, MAX]

        while True:
            cur = heapq.heappop(heap)
            if cur[1] == len(nums[cur[2]]) - 1:
                break

            heapq.heappush(heap, (nums[cur[2]][cur[1]+1], cur[1]+1, cur[2]))
            MAX = max(MAX, nums[cur[2]][cur[1]+1])
            MIN = heap[0][0]

            if MAX-MIN < res[1]-res[0]:
                res = [MIN, MAX]
            elif MAX-MIN == res[1]-res[0] and MIN < res[0]:
                res = [MIN, MAX]

        return res
