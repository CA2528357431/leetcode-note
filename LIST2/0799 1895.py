class Solution:
    def largestMagicSquare(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        mat = [[0] * (n + 1) for _ in range(m + 1)]

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                mat[i][j] = grid[i - 1][j - 1] + mat[i - 1][j] + mat[i][j - 1] - mat[i - 1][j - 1]

        def gets(i1, j1, i2, j2):
            return mat[i2 + 1][j2 + 1] + mat[i1][j1] - mat[i2 + 1][j1] - mat[i1][j2 + 1]

        for l in range(min(m, n), 1, -1):
            for i in range(m - l + 1):
                for j in range(n - l + 1):
                    total = gets(i, j, i + l - 1, j + l - 1) // l
                    judge = True
                    for ii in range(l):
                        heng = gets(i + ii, j, i + ii, j + l - 1)
                        shu = gets(i, j + ii, i + l - 1, j + ii)
                        if heng == shu == total:
                            pass
                        else:
                            judge = False
                            break

                    line1 = 0
                    line2 = 0
                    for ll in range(l):
                        line1 += grid[i + ll][j + ll]
                        line2 += grid[i + ll][j + l - 1 - ll]
                    if line1 == line2 == total:
                        pass
                    else:
                        judge = False

                    if judge:
                        return l
        return 1