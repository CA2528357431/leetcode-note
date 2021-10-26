class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])

        i = 0
        j = n - 1
        while i < m and j >= 0:
            cur = matrix[i][j]
            if cur > target:
                j -= 1
            elif cur < target:
                i += 1
            else:
                return True
        return False
