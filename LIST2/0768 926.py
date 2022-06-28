class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        n = len(s)
        dp = [0] * (n + 1)
        cnt = 0
        for i in s:
            if i == "1":
                cnt += 1
        dp[0] = n - cnt
        for i in range(1, n + 1):
            ii = i - 1
            if s[ii] == "1":
                dp[i] = dp[i - 1] + 1
            else:
                dp[i] = dp[i - 1] - 1
        return min(dp)
