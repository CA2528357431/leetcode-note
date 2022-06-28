class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:

        # 二维动态规划

        '''
        if obstacleGrid[0][0] == 1:
            return 0

        res = [[0] * len(obstacleGrid[0]) for _ in range(len(obstacleGrid))]
        res[0][0] = 1

        for x in range(1, len(obstacleGrid)):
            if obstacleGrid[x][0] == 0:
                res[x][0] = res[x - 1][0]
        for y in range(1, len(obstacleGrid[0])):
            if obstacleGrid[0][y] == 0:
                res[0][y] = res[0][y - 1]

        for x in range(1, len(obstacleGrid)):
            for y in range(1, len(obstacleGrid[0])):
                if obstacleGrid[x][y] == 0:
                    res[x][y] = res[x][y - 1] + res[x - 1][y]
        return res[-1][-1]
        '''


        # 二维动态规划滚动优化

        if obstacleGrid[0][0] == 1:
            return 0

        res = [0] * len(obstacleGrid[0])
        res[0] = 1

        for y in range(1, len(obstacleGrid[0])):
            if obstacleGrid[0][y] == 0:
                res[y] = res[y - 1]

        for x in range(1, len(obstacleGrid)):
            if obstacleGrid[x][0] == 1:
                res[0] = 0
            for y in range(1, len(obstacleGrid[0])):
                if obstacleGrid[x][y] == 0:
                    res[y] = res[y - 1] + res[y]
                    # 滚动优化可以对空间降维
                else:
                    res[y] = 0
        return res[-1]