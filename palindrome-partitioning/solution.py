from typing import List


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        track = []

        def backtrack(s, track):
            if not s:
                res.append(track)

            for i in range(1, len(s) + 1):
                if s[:i] == s[:i][::-1]:
                    backtrack(s[i:], track + [s[:i]])

        backtrack(s, track)

        return res
