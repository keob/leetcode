import re


class Solution:
    def reverseWords(self, s: str) -> str:
        return ' '.join(re.findall('[^ ]+', s)[::-1])
