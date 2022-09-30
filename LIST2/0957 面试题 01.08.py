class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        n = len(matrix[0])
        line = [False] * m
        row = [False] * n

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    line[i] = True
                    row[j] = True

        for i in range(m):
            for j in range(n):
                if line[i] or row[j]:
                    matrix[i][j] = 0

        return
