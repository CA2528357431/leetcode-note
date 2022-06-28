class Solution:
    def minPathCost(self, grid: List[List[int]], moveCost: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        dic = {}

        def do(i, j):
            if i == m - 1:
                return grid[i][j]
            if (i, j) in dic:
                return dic[(i, j)]

            cur = 999999999
            val = grid[i][j]
            for x in range(n):
                neo = val + moveCost[val][x] + do(i + 1, x)
                cur = min(cur, neo)
            dic[(i, j)] = cur
            return cur

        res = 999999999
        for x in range(n):
            res = min(res, do(0, x))

        return res

