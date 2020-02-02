from typing import List


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        new_start, new_end = newInterval
        idx, n = 0, len(intervals)
        res = []

        while idx < n and new_start > intervals[idx][0]:
            res.append(intervals[idx])
            idx += 1

        if not res or res[-1][1] < new_start:
            res.append(newInterval)
        else:
            res[-1][1] = max(res[-1][1], new_end)
        
        while idx < n:
            interval = intervals[idx]
            start, end = interval
            idx += 1
            if res[-1][1] < start:
                res.append(interval)
            else:
                res[-1][1] = max(res[-1][1], end)

        return res
