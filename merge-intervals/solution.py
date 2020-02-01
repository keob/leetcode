from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        if len(intervals) == 0:
            return []

        intervals.sort()

        stack = [intervals[0][0],intervals[0][1]]

        for i in range(1,len(intervals)):
            if intervals[i][0] <= stack[-1]:
                if intervals[i][1] <= stack[-1]:
                    continue
                else:
                    stack.pop()
                    stack.append(intervals[i][1])
            else:
                stack.append(intervals[i][0])
                stack.append(intervals[i][1])

        res = []

        for i in range(0,len(stack),2):
                res.append([stack[i],stack[i+1]])

        return res
