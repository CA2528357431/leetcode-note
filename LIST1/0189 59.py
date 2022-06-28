class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:

        matrix = [[0] * n for _ in range(n)]

        i = 1
        x = 0
        y = 0
        tar = 0
        while i <= n * n:

            matrix[y][x] = i
            i += 1

            if tar == 0 and x + 1 < n and not matrix[y][x + 1]:
                x += 1
            elif tar == 1 and y + 1 < n and not matrix[y + 1][x]:
                y += 1
            elif tar == 2 and x - 1 >= 0 and not matrix[y][x - 1]:
                x -= 1
            elif tar == 3 and y - 1 >= 0 and not matrix[y - 1][x]:
                y -= 1
            else:
                for xx, yy in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]:
                    if xx >= 0 and xx < len(matrix[0]) and yy >= 0 and yy < len(matrix) and not matrix[yy][xx]:
                        x = xx
                        y = yy
                        tar += 1
                        tar = tar % 4
                        break

        return matrix