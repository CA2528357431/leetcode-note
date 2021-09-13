class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        num = len(matrix) * len(matrix[0])
        x = 0
        y = 0
        tar = 0
        while num > 0:
            res.append(matrix[y][x])
            matrix[y][x] = None
            num -= 1



            if tar == 0 and x + 1 < len(matrix[0]) and matrix[y][x + 1] is not None:
                x += 1
            elif tar == 1 and y + 1 < len(matrix) and matrix[y + 1][x] is not None:
                y += 1
            elif tar == 2 and x - 1 >= 0 and matrix[y][x - 1] is not None:
                x -= 1
            elif tar == 3 and y - 1 >= 0 and matrix[y - 1][x] is not None:
                y -= 1
            else:
                for xx, yy in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]:
                    if xx >= 0 and xx < len(matrix[0]) and yy >= 0 and yy < len(matrix) and matrix[yy][xx] is not None:
                        x = xx
                        y = yy
                        tar+=1
                        tar = tar%4
                        break

        return res