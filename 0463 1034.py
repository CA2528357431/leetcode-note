class Solution:
    def colorBorder(self, grid: List[List[int]], row: int, col: int, color: int) -> List[List[int]]:
        xl = len(grid)
        yl = len(grid[0])
        used = [[False] * yl for _ in range(xl)]
        used[row][col] = True
        collect = []

        def dfs(x, y):
            judge = False
            for xx, yy in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]:

                if xx < 0 or xx >= xl or yy < 0 or yy >= yl or grid[xx][yy] != grid[row][col]:
                    judge = True
                else:
                    if not used[xx][yy]:
                        used[xx][yy] = True
                        dfs(xx, yy)

            if judge:
                collect.append((x, y))

        dfs(row, col)
        for x, y in collect:
            grid[x][y] = color
        return grid