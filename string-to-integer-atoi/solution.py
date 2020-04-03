import re


class Solution:
    def myAtoi(self, str: str) -> int:
        re_str = r"\s*[-|+]?\d+"
        res = re.match(re_str, str)
        try:
            res = int(res[0].strip(" "))
        except:
            return 0
        else:
            return max(min(res, 2**31 - 1), (-2)**31)
