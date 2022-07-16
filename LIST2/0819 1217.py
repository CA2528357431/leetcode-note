class Solution:
    def minCostToMoveChips(self, position: List[int]) -> int:
        n = len(position)
        s = 0
        for x in position:
            if x % 2:
                s += 1
        return min(s, n - s)
