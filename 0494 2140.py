class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        n = len(questions)
        dp = [0] * n
        dp[-1] = questions[-1][0]
        for i in range(n - 2, -1, -1):
            point, skip = questions[i]
            if i + skip + 1 >= n:
                dp[i] = max(point, dp[i + 1])
            else:
                dp[i] = max(dp[i + 1], dp[i + 1 + skip] + point)

        return dp[0]