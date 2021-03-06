from typing import List



class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        def findWord(s: str, left: int, right: int) -> int:
            return indices.get(s[left:right+1], -1)

        def isPalindrome(s: str, left: int, right: int) -> bool:
            return (sub := s[left:right+1]) == sub[::-1]

        n = len(words)
        indices = {word[::-1]: i for i, word in enumerate(words)}        
        res = list()

        for i, word in enumerate(words):
            m = len(word)
            for j in range(m + 1):
                if isPalindrome(word, j, m - 1):
                    leftId = findWord(word, 0, j - 1)
                    if leftId != -1 and leftId != i:
                        res.append([i, leftId])
                if j and isPalindrome(word, 0, j - 1):
                    rightId = findWord(word, j, m - 1)
                    if rightId != -1 and rightId != i:
                        res.append([rightId, i])

        return res
