class Solution:
    def findNumberIn2DArray(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix:
            return False

        m = len(matrix)
        n = len(matrix[0])

        x = 0
        y = n - 1

        while x < m and y >= 0:
            cur = matrix[x][y]

            if cur == target:
                return True

            if cur > target:
                y -= 1
            else:
                x += 1

        return False
