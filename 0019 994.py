class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        judge = False

        queue = []

        for x in range(len(grid)):
            for y in range(len(grid[0])):
                if grid[x][y] == 2:
                    queue.append((x,y))
                if grid[x][y] in (1,2):
                    judge = True

        if not judge:
            # 是否全无水果
            return 0

        i = -1
        while queue:
            neo = []
            for x,y in queue:
                for (xx, yy) in ((x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)):
                    if 0 <= xx < len(grid) and 0 <= yy < len(grid[0]):
                        if grid[xx][yy] == 1:
                            neo.append((xx,yy))
                            grid[xx][yy] = 2
            queue = neo
            i += 1

        for x in range(len(grid)):
            for y in range(len(grid[0])):
                if grid[x][y]==1:
                    i = -1
                    # 有未感染的

        return i