class Solution:
    def sellingWood(self, m: int, n: int, prices: List[List[int]]) -> int:
        mat = [[0] * (n + 1) for _ in range(m + 1)]
        for mm, nn, p in prices:
            mat[mm][nn] = p
        for mm in range(1, m + 1):
            for nn in range(1, n + 1):
                for i in range(1, mm // 2 + 1):
                    mat[mm][nn] = max(mat[i][nn] + mat[mm - i][nn], mat[mm][nn])
                for i in range(1, nn // 2 + 1):
                    mat[mm][nn] = max(mat[mm][i] + mat[mm][nn - i], mat[mm][nn])
        return mat[-1][-1]

    # 典型分治