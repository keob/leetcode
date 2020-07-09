from typing import List


class Solution:
    def respace(self, dictionary: List[str], sentence: str) -> int:
        d={}

        for i in dictionary:
            d[i]=len(i)

        len_sentence = len(sentence)
        res = [0]*(len_sentence+1)

        for i in range(len_sentence-1, -1, -1):
            res[i] = res[i+1] + 1

            for j in d:
                if sentence[i:i+d[j]] == j:
                    res[i] = min(res[i], res[i+d[j]])

        return res[0]
