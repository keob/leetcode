from typing import List



class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        from collections import defaultdict
        ticket_dict = defaultdict(list)

        for item in tickets:
            ticket_dict[item[0]].append(item[1])

        path = ['JFK']

        def backtrack(cur_from):
            if len(path) == len(tickets) + 1:
                return True
            ticket_dict[cur_from].sort()
            for _ in ticket_dict[cur_from]:
                cur_to = ticket_dict[cur_from].pop(0)
                path.append(cur_to)
                if backtrack(cur_to):
                    return True
                path.pop()
                ticket_dict[cur_from].append(cur_to)
            return False

        backtrack('JFK')

        return path
