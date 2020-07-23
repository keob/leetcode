class Solution:
    def computeArea(self, A: int, B: int, C: int, D: int, E: int, F: int, G: int, H: int) -> int:
        area = (C-A)*(D-B) + (G-E)*(H-F)
        if A > G or C < E or D < F or B > H:
            return area
        else:
            x1 = max(A, E)
            x2 = min(C, G)
            y1 = max(B, F)
            y2 = min(D, H)
            return area - (y2-y1)*(x2-x1)
