from typing import List


class Solution:
    def rankTeams(self, votes: List[str]) -> str:
        res = ''
        score = [[0 for i in range(len(votes[0])+1)] for x in range(26)]
        for vote in votes:
            for i, v in enumerate(vote):
                score[ord(v) - ord('A')][i] += 1
                score[ord(v) - ord('A')][-1] = ord('Z') - ord(v) + 1

        score.sort(reverse=True)

        for i in range(26):
            if score[i][-1] != 0:
                res += chr(26 - score[i][-1] + 65)
        return res
