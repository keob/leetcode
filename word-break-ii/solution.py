from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        n=len(s)
        valid_dp=[False for _ in range(n+1)]

        for i in range(n+1):
            for j in range(i):
                if j==0 and s[j:i] in wordDict:
                     valid_dp[i]=True
                elif valid_dp[j]==True and s[j:i] in wordDict:
                     valid_dp[i]=True

        dp=[[] for _ in range(n+1)]

        if valid_dp[-1]!=True:
             return []

        for i in range(n+1):
             if valid_dp[i]!=True:
                 continue
             for j in range(i):
                 if j==0 and s[j:i] in wordDict:
                       dp[i].append(s[j:i])
                 elif  dp[j]!=[] and s[j:i] in wordDict:
                       for k in dp[j]:
                           dp[i].append(k+" "+s[j:i])
        return dp[-1]
