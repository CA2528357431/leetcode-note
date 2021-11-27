class Solution:
    def minCost(self, startPos: List[int], homePos: List[int], rowCosts: List[int], colCosts: List[int]) -> int:
        costy = 0
        if startPos[0] <= homePos[0]:
            for y in range(startPos[0] + 1, homePos[0] + 1):
                costy += rowCosts[y]
        else:
            for y in range(startPos[0] - 1, homePos[0] - 1, -1):
                costy += rowCosts[y]

        costx = 0
        if startPos[1] <= homePos[1]:
            for x in range(startPos[1] + 1, homePos[1] + 1):
                costx += colCosts[x]
        else:
            for x in range(startPos[1] - 1, homePos[1] - 1, -1):
                costx += colCosts[x]

        return costy + costx