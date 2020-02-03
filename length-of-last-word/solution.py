class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.rstrip()

        if s.count(' ') == 0:
            return len(s)

        x = 0

        while True:
            if s[-(x + 1)] == ' ':
                return x
            x += 1
