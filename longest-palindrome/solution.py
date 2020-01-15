from collections import Counter


class Solution:
    def longestPalindrome(self, s: str) -> int:
        ans = 0
        counter = Counter(s)

        for key in counter.keys():
            v = counter[key]
            ans += v // 2 * 2
            if ans % 2 == 0 and v % 2 == 1:
                ans += 1

        return ans
