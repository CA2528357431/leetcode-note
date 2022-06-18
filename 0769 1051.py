class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        neo = heights.copy()
        neo.sort()
        res = 0
        for i in range(len(heights)):
            if heights[i]!=neo[i]:
                res+=1
        return res