class Solution:
    def minCut(self, s: str) -> int:
        n = len(s)

        mat = [[False] * n for _ in range(n)]

        for i in range(n):
            mat[i][i] = True
            if i != n - 1 and s[i] == s[i + 1]:
                mat[i][i + 1] = True

        for length in range(3, n + 1):
            for l in range(0, n - length + 1):
                if s[l] == s[l + length - 1] and mat[l + 1][l + length - 1 - 1]:
                    mat[l][l + length - 1] = True

        le = [9999] * n

        for i in range(n):
            if i == 0:
                for j in range(n):
                    if mat[0][j]:
                        le[j] = 0
            else:
                for j in range(i, n):
                    if mat[i][j]:
                        le[j] = min(le[i - 1] + 1, le[j])

        return le[-1]