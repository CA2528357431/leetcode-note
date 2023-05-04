class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x: x[0])
        n = len(points)
        res = 0
        for i in range(1, n):
            res = max(res, points[i][0] - points[i - 1][0])

        return res