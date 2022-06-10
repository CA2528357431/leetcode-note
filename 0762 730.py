class Solution:
    def countPalindromicSubsequences(self, s: str) -> int:
        mod = 1000000007

        n = len(s)
        if n == 1:
            return 1
        if n == 2:
            return 2

        def index(c):
            return ord(c) - ord("a")

        dp = [[[0] * n for _ in range(n)] for _ in range(4)]

        for i in range(n):
            dp[index(s[i])][i][i] = 1

        for l in range(2, n + 1):
            for i in range(n - l + 1):
                left = i
                right = i + l - 1

                for c in "abcd":

                    ind = index(c)
                    if s[left] == s[right] == c:
                        for ii in range(4):
                            dp[ind][left][right] += dp[ii][left + 1][right - 1]
                        dp[ind][left][right] += 2
                        dp[ind][left][right] %= mod

                    elif s[left] == c:
                        dp[ind][left][right] = dp[ind][left][right - 1]
                    elif s[right] == c:
                        dp[ind][left][right] = dp[ind][left + 1][right]
                    else:
                        dp[ind][left][right] = dp[ind][left + 1][right - 1]

        res = 0
        for i in range(4):
            res += dp[i][0][-1]
        return res % mod





