class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        def findis(mat):
            m = len(mat)
            n = len(mat[0])
            used = [[False] * n for _ in range(m)]
            res = []

            for x in range(m):
                for y in range(n):
                    if used[x][y] or mat[x][y] == 0:
                        continue
                    island = [[x, y]]
                    cur = [[x, y]]
                    used[x][y] = True
                    while cur:
                        nxt = []
                        for i, j in cur:
                            for ii, jj in [(i, j + 1), (i, j - 1), (i + 1, j), (i - 1, j)]:
                                if ii < 0 or jj < 0 or ii >= m or jj >= n or used[ii][jj] or mat[ii][jj] == 0:
                                    continue
                                used[ii][jj] = True
                                nxt.append([ii, jj])
                                island.append([ii, jj])
                        cur = nxt
                    res.append(island)

            for i in range(m):
                for j in range(n):
                    if mat[i][j] == 1 and used[i][j] == False:
                        print(i, j)

            return res

        def contain(b):
            for i, j in b:
                if grid1[i][j] == 0:
                    return False
            return True

        pbs = findis(grid2)

        cnt = 0
        for pb in pbs:
            if contain(pb):
                cnt += 1
        return cnt

