from typing import List


class Solution:
    def patternMatching(self, pattern: str, value: str) -> bool:
        if not value and not pattern:
            return True
        if not pattern:
            return False
        if not value:
            if len(pattern) == 1:
                return True
            else:
                return False
        if len(set(pattern)) == 1:
            if len(value) % len(pattern) != 0:
                return False
            length = len(value) // len(pattern)
            return all([value[i:i+length] == value[0:length] for i in range(0, len(value), length)])

        if pattern.count('a') == 1 or pattern.count('b') ==1 :
            return True

        cnt_a = pattern.count('a')
        cnt_b = pattern.count('b')

        for i in range(len(value) // cnt_a):
            remain = len(value) - i * cnt_a 
            if remain % cnt_b != 0:
                continue
            j = remain // cnt_b
            set_a = set()
            set_b = set()
            p = 0
            for s in pattern:
                if s == 'a':
                    set_a.add(value[p:p+i])
                    p += i
                else:
                    set_b.add(value[p:p+j])
                    p += j
            if len(set_a) == len(set_b) == 1:
                return True
        return False
