class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        line = False
        row = False
        for x in matrix[0]:
            if x == 0:
                line = True
        for x in matrix:
            if x[0] == 0:
                row = True
        for x in range(1,len(matrix)):
            for y in range(1,len(matrix[0])):
                if matrix[x][y]==0:
                    matrix[x][0] = 0
                    matrix[0][y] = 0
        for x in range(1,len(matrix)):
            for y in range(1,len(matrix[0])):
                if matrix[x][0] == 0 or matrix[0][y] == 0:
                    matrix[x][y] = 0
        if line:
            for x in range(len(matrix[0])):
                matrix[0][x] = 0
        if row:
            for x in range(len(matrix)):
                matrix[x][0] = 0

# 用两个量记录0行0列有没有0
# 随后遍历非0行0列的个体
# 如果有0，则将其所在行和列的0号元素改为0作为标记
# 最后遍历时统一看所在行和列的0号元素即可