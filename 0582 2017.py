class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:

        n = len(grid[0])

        def getleft(li):
            neo = li.copy()
            for i in range(1, n):
                neo[i] += neo[i - 1]
            return neo

        def getright(li):
            neo = li.copy()
            for i in range(n - 2, -1, -1):
                neo[i] += neo[i + 1]
            return neo

        orir = getright(grid[0])
        oril = getleft(grid[1])

        cur = 0
        for i in range(n):
            if max(orir[i] - grid[0][i], oril[i] - grid[1][i]) < max(orir[cur] - grid[0][cur],oril[cur] - grid[1][cur]):
                cur = i
        # 后者可以获取的点数只有左下和右上，因此需要使左上、右下的最大值最小

        return max(orir[cur] - grid[0][cur], oril[cur] - grid[1][cur])