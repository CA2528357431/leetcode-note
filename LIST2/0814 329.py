class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        dic = {}
        m = len(matrix)
        n = len(matrix[0])

        def do(i, j):
            if (i, j) in dic:
                return dic[(i, j)]
            res = 1
            for ii, jj in [(i, j + 1), (i, j - 1), (i + 1, j), (i - 1, j)]:
                if ii < 0 or ii >= m or jj < 0 or jj >= n:
                    continue
                if matrix[ii][jj] > matrix[i][j]:
                    res = max(res, do(ii, jj) + 1)
            dic[(i, j)] = res
            return res

        res = 1
        for i in range(m):
            for j in range(n):
                neo = do(i, j)
                res = max(neo, res)
        return res
