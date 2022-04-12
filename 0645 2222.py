class Solution:
    def numberOfWays(self, s: str) -> int:
        n = len(s)
        left = [0] * n
        for i in range(1, n):
            left[i] = left[i - 1]
            if s[i - 1] == "0":
                left[i] += 1
        right = [0] * n
        for i in range(n - 2, -1, -1):
            right[i] = right[i + 1]
            if s[i + 1] == "0":
                right[i] += 1
        res = 0
        for i in range(n):
            if s[i] == "1":
                res += left[i] * right[i]
            else:
                res += (i - left[i]) * (n - i - 1 - right[i])
        return res

