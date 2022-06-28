class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if len(matrix) == 1:
            for x in matrix[0]:
                if x == "1":
                    return 1
            return 0
        if len(matrix[0]) == 1:
            for x in matrix:
                if x[0] == "1":
                    return 1
            return 0

        res = [0] * len(matrix[0])
        big = 0
        for x in range(len(matrix[0])):
            if matrix[0][x] == "0":
                res[x] = 0
            else:
                res[x] = 1
                big = 1
        for x in range(1, len(matrix)):
            la = res.copy()
            if matrix[x][0] == "0":
                res[0] = 0
            else:
                res[0] = 1
                big = max(big, 1)
            for y in range(1, len(matrix[0])):
                if matrix[x][y] == "0":
                    res[y] = 0
                else:
                    res[y] = min(la[y], la[y - 1], res[y - 1]) + 1
                    big = max(res[y], big)
        return big ** 2