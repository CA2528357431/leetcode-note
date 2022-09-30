class Solution:
    def getKthMagicNumber(self, k: int) -> int:
        x3 = 0
        x5 = 0
        x7 = 0
        dp = [1] * (k)
        for i in range(1, k):
            neo3 = dp[x3] * 3
            neo5 = dp[x5] * 5
            neo7 = dp[x7] * 7
            neo = min(neo3, neo5, neo7)
            if neo == neo3:
                x3 += 1
            if neo == neo5:
                x5 += 1
            if neo == neo7:
                x7 += 1
            dp[i] = neo

        return dp[-1]