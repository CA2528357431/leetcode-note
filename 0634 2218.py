class Solution:
    def maxValueOfCoins(self, piles: List[List[int]], k: int) -> int:
        n = len(piles)

        mat = [[0] * (n) for _ in range(k + 1)]

        for kk in range(1, k + 1):
            for nn in range(n):
                if kk > len(piles[nn]):
                    mat[kk][nn] = 0
                else:
                    mat[kk][nn] = mat[kk - 1][nn] + piles[nn][kk - 1]

        dic = {}

        def dfs(cnt, nn):
            if (cnt, nn) in dic:
                return dic[(cnt, nn)]
            if cnt == 0:
                return 0
            if nn == n:
                return 0
            big = 0
            for i in range(0, min(cnt + 1, len(piles[nn]) + 1)):
                big = max(big, dfs(cnt - i, nn + 1) + mat[i][nn])
            dic[(cnt, nn)] = big
            return big

        # 背包问题记忆化搜索

        x = dfs(k, 0)
        return x
