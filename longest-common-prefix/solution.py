from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        res = strs[0]
        i = 1
        while i < len(strs):
            while strs[i].find(res) != 0:
                res = res[0:len(res) - 1]
            i += 1

        return res
