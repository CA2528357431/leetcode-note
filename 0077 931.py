class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        if len(matrix) == 1:
            return matrix[0][0]

        road = [[0] * len(matrix) for _ in matrix]

        for x in range(len(matrix)):
            road[0][x] = matrix[0][x]

        for x in range(1, len(matrix)):
            road[x][0] = min(road[x - 1][0], road[x - 1][1]) + matrix[x][0]
            road[x][-1] = min(road[x - 1][-1], road[x - 1][-2]) + matrix[x][-1]
            for y in range(1, len(matrix) - 1):
                road[x][y] = min(road[x - 1][y - 1], road[x - 1][y], road[x - 1][y + 1]) + matrix[x][y]
        return min(road[-1])
