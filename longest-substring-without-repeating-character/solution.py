class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longStr = set([])
        curStr = set([])
        max = 0

        for i in range(len(s)):
            longStr = set([s[i]])
            curStr = set([s[i]])
            for j in range(i + 1, len(s)):
                longStr.add(s[j])
                if len(longStr) > len(curStr):
                    curStr.add(s[j])
                else:
                    break
            if len(longStr) > max:
                max = len(longStr)

        return max
