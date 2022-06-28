class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m = len(heights)
        n = len(heights[0])

        pac = [[False] * n for _ in range(m)]
        pac[0][0] = True

        for i in range(1, n):
            pac[0][i] = True

        for i in range(1, m):
            pac[i][0] = True

        used = [[False] * n for _ in range(m)]

        for i in range(1, n):
            used[0][i] = True

        for i in range(1, m):
            used[i][0] = True

        def judgepac(x, y):
            for xx, yy in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]:
                if xx >= m or yy >= n or xx < 0 or yy < 0 or used[xx][yy] == True:
                    continue
                if heights[xx][yy] >= heights[x][y]:
                    pac[xx][yy] = True
                    used[xx][yy] = True
                    judgepac(xx, yy)

        for i in range(n):
            judgepac(0, i)

        for i in range(m):
            judgepac(i, 0)

        used = [[False] * n for _ in range(m)]

        for i in range(n):
            used[-1][i] = True

        for i in range(m):
            used[i][-1] = True

        res = []

        def judgeatl(x, y):
            for xx, yy in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]:
                if xx >= m or yy >= n or xx < 0 or yy < 0 or used[xx][yy] == True:
                    continue
                if heights[xx][yy] >= heights[x][y]:
                    if pac[xx][yy] == True:
                        res.append((xx, yy))
                    used[xx][yy] = True
                    judgeatl(xx, yy)

        for i in range(n):
            if pac[m - 1][i] == True:
                res.append((m - 1, i))
            judgeatl(m - 1, i)

        for i in range(m - 1):
            if pac[i][n - 1] == True:
                res.append((i, n - 1))
            judgeatl(i, n - 1)

        return res