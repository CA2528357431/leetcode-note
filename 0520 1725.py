class Solution:
    def countGoodRectangles(self, rectangles: List[List[int]]) -> int:
        res, maxLen = 0, 0
        for l, w in rectangles:
            k = min(l, w)
            if k == maxLen:
                res += 1
            elif k > maxLen:
                res = 1
                maxLen = k
        return res