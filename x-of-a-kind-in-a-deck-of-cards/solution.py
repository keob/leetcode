from typing import List


class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        def gcd(x, y):
            for i in range(2, (y if x > y else x) + 1):
                if x % i == y % i==0:
                    return i
            return 1

        count_deck = [deck.count(n) for n in set(deck)]

        if len(count_deck) == 1:
            return True if count_deck[0]>1 else False
        else:
            count_deck=list(set(count_deck))
            for i in range(1, len(count_deck)):
                if gcd(count_deck[i], count_deck[i-1]) == 1:
                    return False
                else:
                    continue
            return True
