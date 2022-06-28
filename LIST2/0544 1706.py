class Solution:
    def findBall(self, grid: List[List[int]]) -> List[int]:
        m = len(grid)
        n = len(grid[0])

        def judge(x, y):
            if grid[x][y] == 1:
                if y + 1 == n or grid[x][y + 1] == -1:
                    return False
                else:
                    return True
            else:
                if y - 1 == -1 or grid[x][y - 1] == 1:
                    return False
                else:
                    return True

        res = [-1] * n

        def do(yy):
            x = 0
            y = yy
            while x < m:

                if not judge(x, y):
                    return
                else:

                    if grid[x][y] == 1:
                        x += 1
                        y += 1
                    else:
                        x += 1
                        y -= 1

                    if x == m:
                        res[yy] = y
                        return

            return

        for i in range(n):
            do(i)

        return res
