from collections import Counter


class Solution:
    def frequencySort(self, s: str) -> str:
        dic = dict(Counter(s))
        l1 = ['' for e in range(len(s) + 1)]
        for key, value in dic.items():
            l1[value] += key * value
        res = ''
        for i in range(-1, -len(l1) - 1, -1):
            if l1[i] != '':
                res += l1[i]
        return res
