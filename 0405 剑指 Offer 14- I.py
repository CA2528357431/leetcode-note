class Solution:
    def cuttingRope(self, n: int) -> int:
        dp = [0]*(n+1)
        dp[1] = 1
        for i in range(2,n+1):
            for l in range(1,i//2+1):
                r = i-l

                bigl = max(dp[l],l)
                bigr = max(dp[r],r)

                dp[i] = max(bigl*bigr,dp[i])

        return dp[-1]