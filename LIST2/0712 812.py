class Solution:
    def largestTriangleArea(self, points: List[List[int]]) -> float:
        res = 0
        n = len(points)
        for a in range(n):
            for b in range(a+1,n):
                for c in range(b+1,n):
                    ax,ay = points[a]
                    bx,by = points[b]
                    cx,cy = points[c]
                    l1x = bx-ax
                    l1y = by-ay
                    l2x = cx-ax
                    l2y = cy-ay
                    s = abs(l1x*l2y-l1y*l2x)
                    res = max(res,s)
        return res/2