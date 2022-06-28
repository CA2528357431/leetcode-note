class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        sol = []
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

        def dfs(l):
            if l == n:
                res.append(sol.copy())
            for r in range(l, n):
                if mat[l][r]:
                    sol.append(s[l:r + 1])
                    dfs(r + 1)
                    sol.pop()

        dfs(0)
        return res