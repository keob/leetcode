from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        stack = []
        maxstack = 0
        res = 0

        for i in range(len(height)):
            h = height[i]

            if not stack:
                if h == 0:
                    continue
                else:
                    stack.append([h, i])
                    maxstack = max(maxstack, h)
            else:
                if h >= maxstack:
                    while stack:
                        last, lastid = stack.pop(-1)
                        res += (maxstack - last)
                    maxstack = max(maxstack, h)
                stack.append([h, i])
        last = 0

        while stack:
            tmp, tmpid = stack.pop(-1)

            if tmp < last:
                res += last - tmp

            last = max(last, tmp)

        return res