class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        hashmap = {}
        ismap = {}
        for i in range(len(s)):
            if s[i] in hashmap:
                if hashmap[s[i]] != t[i]:
                    return False
            else:
                if t[i] in ismap:
                    return False
                hashmap[s[i]] = t[i]
                ismap[t[i]] = True
        return True
