class Solution:
    def computeArea(self, ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int) -> int:
        cx1 = max(ax1, bx1)
        cy1 = max(ay1, by1)
        cx2 = min(ax2, bx2)
        cy2 = min(ay2, by2)
        x = cx2 - cx1
        y = cy2 - cy1
        s = 0
        if x > 0 and y > 0:
            s = x * y
        ss = (ax2 - ax1) * (ay2 - ay1) + (bx2 - bx1) * (by2 - by1)
        return ss - s



