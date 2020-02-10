from typing import List


class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        res = []
        current_world = 0
        current_sum = 0
        wl = []
        for i, wd in enumerate(words):
            l = len(wd)
            if current_world + l + current_sum > maxWidth:
                if current_sum == 1:
                    res.append(wl[0] + ' ' * (maxWidth-current_world))
                else:
                    left = maxWidth - current_world
                    if left % (current_sum-1) == 0:
                        res.append((' '*(left//(current_sum-1))).join(wl))
                    else:
                        x = left % (current_sum-1)
                        b = left // (current_sum-1)
                        cans = wl[0]
                        for i in range(x):
                            cans += ' ' * (b+1) + wl[i+1]
                        for i in range(x+1, len(wl)):
                            cans += ' ' * b + wl[i]
                        res.append(cans)
                current_world = l
                current_sum = 1
                wl = [wd]
            else:
                current_world += l
                current_sum += 1
                wl.append(wd)

        if current_sum > 0:
            cans = ' '.join(wl)
            cans += ' ' * (maxWidth - len(cans))
            res.append(cans)
        return res
