class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """

        res = 0

        for x in range(len(grid)):
            for y in range(len(grid[0])):
                if grid[x][y] == 1:
                    grid[x][y] = 0
                    queue = [(x, y)]
                    re = 0
                    while queue:
                        x, y = queue.pop()
                        re += 1
                        for xx, yy in ((x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)):
                            if 0 <= xx < len(grid) and 0 <= yy < len(grid[0]):
                                if grid[xx][yy] == 1:
                                    grid[xx][yy] = 0
                                    queue.append([xx, yy])
                    res = max(res, re)

        return res

sol = Solution()
print(sol.maxAreaOfIsland(
[[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]))
# 防止一处二走？
# 修改走过地区的值为“不可走”

# 注意有两处需要如此操作
# 1 每个岛的源头
# 2
