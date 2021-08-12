class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        res = [[1] * len(s) for _ in range(len(s))]
        for x in range(len(s) - 1):
            if s[x] == s[x + 1]:
                res[x][x + 1] = 2

        for r in range(2, len(s)):
            for x in range(0, len(s) - r):
                if s[x] == s[x + r]:
                    res[x][x + r] = res[x + 1][x + r - 1] + 2
                else:
                    res[x][x + r] = max(res[x + 1][x + r], res[x][x + r - 1])

        return res[0][-1]