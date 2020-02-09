class Solution:
    def isNumber(self, s: str) -> bool:
        states = [
            {'b': 0, 's': 1, 'd': 2, '.': 4},
            {'d': 2, '.': 4 },
            {'d': 2, '.': 3, 'e': 5, 'b': 8},
            {'d': 3, 'e': 5, 'b': 8},
            {'d': 3},
            {'s': 6, 'd': 7},
            {'d': 7},
            {'d': 7, 'b': 8},
            {'b': 8}
        ]
        p = 0
        for c in s:
            if '0' <= c <= '9':
                typ = 'd'
            elif c == ' ':
                typ = 'b'
            elif c == '.':
                typ = '.'
            elif c == 'e':
                typ = 'e'
            elif c in "+-":
                typ = 's'
            else:
                typ = '?'
            if typ not in states[p]:
                return False
            p = states[p][typ]

        return p in [2, 3, 7, 8]
