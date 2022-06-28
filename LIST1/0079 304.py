class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.cal = [[0]*(len(matrix[0])+1) for _ in range(len(matrix)+1)]
        for x in range(1,len(matrix)+1):
            for y in range(1,len(matrix[0])+1):
                self.cal[x][y] = self.cal[x][y-1]+matrix[x-1][y-1]
        for y in range(1,len(matrix[0])+1):
            for x in range(1,len(matrix)+1):
                self.cal[x][y] += self.cal[x-1][y]


    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return self.cal[row2+1][col2+1]-self.cal[row2+1][col1]-self.cal[row1][col2+1]+self.cal[row1][col1]