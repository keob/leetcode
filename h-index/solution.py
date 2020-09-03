from typing import List


class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort()
        index = 1
        num = 0

        for i in range(len(citations)-1, -1, -1):
            if citations[i] >= index:
                index += 1
                num += 1
            else:
                return num
        return num
