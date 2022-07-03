class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:

        mod = 10 ** 9 + 7
        m = len(grid)
        n = len(grid[0])

        res = 0

        used = [[False] * n for _ in range(m)]
        cur = []

        dic = {}

        def do(i, j):
            if (i, j) in dic:
                return dic[(i, j)]

            re = 1

            mov = [(0, 1), (1, 0), (0, -1), (-1, 0)]

            for m1, m2 in mov:
                ii = i + m1
                jj = j + m2
                if 0 <= ii < m and 0 <= jj < n and grid[i][j] < grid[ii][jj]:
                    neo = do(ii, jj)
                    re += neo
                    re %= mod
            re = re % mod
            dic[(i, j)] = re
            return re

        for i in range(m):
            for j in range(n):
                neo = do(i, j)
                res += neo
                res %= mod

        return res % mod