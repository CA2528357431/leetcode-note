class Solution:
    def oddCells(self, m: int, n: int, indices: List[List[int]]) -> int:
        ms = {}
        ns = {}
        for r, c in indices:
            ms[r] = ms.get(r, 0) + 1
            ns[c] = ns.get(c, 0) + 1
        mat = [[0] * n for _ in range(m)]

        for k, v in ms.items():
            for i in range(n):
                mat[k][i] += v
        for k, v in ns.items():
            for i in range(m):
                mat[i][k] += v
        res = 0
        for i in range(m):
            for j in range(n):
                if mat[i][j] % 2 == 1:
                    res += 1

        return res