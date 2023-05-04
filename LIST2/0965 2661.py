class Solution:
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:

        m, n = len(mat), len(mat[0])

        content1 = [0] * m
        content2 = [0] * n

        dic = {}
        for i in range(m):
            for j in range(n):
                dic[mat[i][j]] = (i, j)

        for x in range(m * n):
            i, j = dic[arr[x]]
            content1[i] += 1
            content2[j] += 1
            if content1[i] == n or content2[j] == m:
                return x

