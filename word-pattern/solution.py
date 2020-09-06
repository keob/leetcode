class Solution:
    def wordPattern(self, pattern: str, str: str) -> bool:
        strS = str.split()

        if len(pattern) != len(strS):
            return False

        dct = {}

        for i in range(len(pattern)):
            if pattern[i] not in dct:
                if strS[i] in dct.values():
                    return False
                dct[pattern[i]] = strS[i]
            else:
                if dct[pattern[i]] != strS[i]:
                    return False
        return True
