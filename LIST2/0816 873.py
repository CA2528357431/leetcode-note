class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        n = len(arr)
        dp = [[0] * n for _ in range(n)]

        index = {}
        for i in range(n):
            index[arr[i]] = i

        res = 0

        for i in range(n):
            for j in range(i):
                if 2 * arr[j] >= arr[i]:
                    break
                fir = arr[i]
                sec = arr[j]
                thi = fir - sec
                if thi not in index:
                    continue
                l = index[thi]

                dp[i][l] = max(3, dp[l][j] + 1)
                res = max(dp[i][l], res)

        return res