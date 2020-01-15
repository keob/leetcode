from typing import List


class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        def max_points_on_a_line_containing_point_i(i):
            def add_line(i, j, count, duplicates):
                x1 = points[i].x
                y1 = points[i].y
                x2 = points[j].x
                y2 = points[j].y

                if x1 == x2 and y1 == y2:
                    duplicates += 1
                elif y1 == y2:
                    nonlocal horisontal_lines
                    horisontal_lines += 1
                    count = max(horisontal_lines, count)
                else:
                    slope = (x1 - x2) / (y1 - y2)
                    lines[slope] = lines.get(slope, 1) + 1
                    count = max(lines[slope], count)

                return count, duplicates

            lines, horisontal_lines = {}, 1
            count = 1
            duplicates = 0

            for j in range(i + 1, n):
                count, duplicates = add_line(i, j, count, duplicates)
            return count + duplicates

        n = len(points)

        if n < 3:
            return n

        max_count = 1

        for i in range(n - 1):
            max_count = max(max_points_on_a_line_containing_point_i(i),
                            max_count)
        return max_count
