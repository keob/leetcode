from typing import List


class Solution:
    def minimumLengthEncoding(self, words: List[str]) -> int:
        res = 0
        n = len(words)
        reversed_words = []

        for word in words:
            reversed_words.append(word[::-1])

        reversed_words.sort()

        for i in range(n):
            if i + 1 < n and reversed_words[i + 1].startswith(reversed_words[i]):
                pass
            else:
                res += len(reversed_words[i]) + 1

        return res
