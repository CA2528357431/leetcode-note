class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        m = len(mat)
        n = len(mat[0])
        line = [0] * m
        row = [0] * n
        for i in range(m):
            for j in range(n):
                line[i] += mat[i][j]
                row[j] += mat[i][j]

        res = 0
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 1 and line[i] == 1 and row[j] == 1:
                    res += 1

        return res

