class Solution:
    def getMaxRepetitions(self, s1: str, n1: int, s2: str, n2: int) -> int:
        leapto = [0] * len(s2)
        repeat = [0] * len(s2)

        for i in range(len(s2)):
            cnt = 0
            idx = i
            for j in range(len(s1)):
                if s1[j] == s2[idx]:
                    idx += 1
                    if idx == len(s2):
                        idx = 0
                        cnt += 1
            leapto[i] = idx
            repeat[i] = cnt

        res = 0
        pos = 0

        for i in range(n1):
            res += repeat[pos]
            pos = leapto[pos]

        return res // n2

