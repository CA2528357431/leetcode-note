class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        plusmax = values[0] + 0
        totalmax = values[0] + values[1] - 1
        for x in range(1, len(values) - 1):
            plusmax = max(plusmax, values[x] + x)
            totalmax = max(plusmax + values[x + 1] - x - 1, totalmax)
        return totalmax

    # plusmax 维护n[x]+x的max,x遍历n[x]-x,totalmax记录总max