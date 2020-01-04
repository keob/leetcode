from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs) == 0:
            return []

        ret = []
        memo = dict()
        k = 0

        for one in strs:
            lone = list(one)
            lone.sort()
            tone = "".join(lone)
            if tone not in memo:
                memo[tone] = k
                k += 1
                ret.append([])
            ret[memo[tone]].append(one)

        return ret
